import sys
import pygame
from pygame.sprite import Sprite

class ImageHelper:
    @staticmethod
    def load_image(path, k=1):
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, (image.get_rect().width * k, image.get_rect().height * k))

class PlayerState:
    IDLE = 0
    MovingRight = 1
    MovingLeft = 2
    MovingUp = 3
    MovingDown = 4

class Blocks(Sprite):
    def __init__(self, screen, texturePath):
        super().__init__()
        self.image = ImageHelper.load_image(texturePath)
        self.rect = self.image.get_rect()
        self.screen = screen

    def update(self, *args, **kwargs):
        pass

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def set_coords(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def change_coords(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class Player(Sprite):
    NOT_MOVE = 0
    LEFT_MOVE, UP_MOVE = -1, -1
    RIGHT_MOVE, DOWN_MOVE = 1, 1

    def __init__(self, screen, texturePath):
        super().__init__()
        self.anim_right = [ImageHelper.load_image("sprites/riht_walk1.xcf"),ImageHelper.load_image('sprites/right_walk2.xcf')]
        self.anim_left = [ImageHelper.load_image("sprites/left_walk1.xcf"),ImageHelper.load_image('sprites/left_walk2.xcf')]
        self.anim_up_right = [ImageHelper.load_image("sprites/JumpEl.xcf")]
        self.anim_up_left = [ImageHelper.load_image("sprites/JumpEl.xcf")]
        self.anim_down = [ImageHelper.load_image("sprites/Fall.xcf")]
        self.idle = [ImageHelper.load_image('sprites/Idle.xcf')]
        self.current_anim = self.idle
        self.image = ImageHelper.load_image(texturePath)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speed = 1
        self.speed_jump = 1
        self.direction_x = Player.NOT_MOVE
        self.direction_y = Player.NOT_MOVE


        # self.timer = Timer(0.2)
        self.isJumping = False
        self.startJumpingTime = pygame.time.get_ticks()
        self.jumpSpeed = 200

        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 150

    def drop_anim(self, playerState):
        current_anim = self.idle

        if playerState == PlayerState.MovingLeft:
            current_anim = self.anim_left
        elif playerState == PlayerState.MovingRight:
            current_anim = self.anim_right
        elif playerState == PlayerState.MovingUp:
            if self.direction_x == Player.RIGHT_MOVE:
                current_anim = self.anim_up_right
            else:
                current_anim = self.anim_up_left
        elif playerState == PlayerState.MovingDown:
            current_anim = self.anim_down

        if self.current_anim != current_anim:
            self.frame = 0
            self.current_anim = current_anim



    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self, *args, **kwargs):
        physicEngine = kwargs.get("physicEngine", None)

        if physicEngine is not None:
            phData = physicEngine.get(self, "test")
            #print(phData)


        now = pygame.time.get_ticks()

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1

            if self.frame == len(self.current_anim):
                self.frame = 0

        self.image = self.current_anim[self.frame]

        if self.isJumping:
            if now - self.startJumpingTime > self.jumpSpeed:
                if self.direction_y == Player.UP_MOVE:
                    self.start_jumping_falling()
                elif self.direction_y == Player.DOWN_MOVE:
                    self.direction_y = self.NOT_MOVE
                    self.isJumping = False

        self.rect.y += self.speed_jump * self.direction_y
        self.rect.x += self.speed * self.direction_x

        if self.direction_y == Player.NOT_MOVE and self.direction_x == Player.NOT_MOVE:
            self.drop_anim(PlayerState.IDLE)

    def go_right(self):
        self.direction_x = Player.RIGHT_MOVE

        self.drop_anim(PlayerState.MovingRight)

    def go_left(self):
        self.direction_x = Player.LEFT_MOVE

        self.drop_anim(PlayerState.MovingLeft)

    def stop_move(self):
        self.direction = Player.NOT_MOVE

        self.drop_anim(PlayerState.IDLE)

    def start_falling(self):
        self.direction_y = Player.DOWN_MOVE

        self.drop_anim(PlayerState.MovingDown)

    def start_jumping_falling(self):
        self.startJumpingTime = pygame.time.get_ticks()
        self.start_falling()

    def start_jump(self):
        if self.isJumping:
            return

        self.drop_anim(PlayerState.MovingUp)

        self.isJumping = True
        self.startJumpingTime = pygame.time.get_ticks()
        self.direction_y = Player.UP_MOVE


class PhysicalEnvEngine:
    def __init__(self, **kwargs):   # **kwargs - здесь будет выглядеть как словарь, а где будут передавать будет выглядеть как список параметров
        self.solidObjects = kwargs.get("solidObjects", list())  # получаем значение, которое лежит в ключе solidObjects, но если не передавали, то пустой список будет - значение по умолчанию

    def update(self):
        result = {}

        for obj in self.solidObjects:
            collided = self.check_collision(obj)

            if collided:
                result[obj] = {"collided": True}
                print("COLLIDED!")

        return result

    def check_collision(self, item):
        for obj in self.solidObjects:
            if obj is not item:
                if item.rect.colliderect(obj):
                    return True
        return False


class RockWalkAndJump:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.player = Player(self.screen, "sprites/adventurer_walk1.png")
        self.player.rect.center = self.screen.get_rect().center

        self.block = Blocks(self.screen, texturePath="sprites/Block1.xcf")
        self.block.set_coords(self.player.rect.x + 50, self.player.rect.bottom + 25)

        self.physicalEnv = PhysicalEnvEngine(solidObjects=[self.block, self.player])

        pygame.display.set_caption("Rock walk")
        self.bg_color = (76, 138, 78)

    def run_game(self):
        while True:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()



                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.go_left()
                    elif event.key == pygame.K_d:
                        self.player.go_right()
                    elif event.key == pygame.K_SPACE:
                        self.player.start_jump()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.player.direction_x = Player.NOT_MOVE
                    elif event.key == pygame.K_SPACE:
                        pass
            self.screen.fill(self.bg_color)

            physicalResult = self.physicalEnv.update()

            self.player.blit()
            self.player.update(physicEngine = physicalResult)



            self.block.blit()
            self.block.update(physicEngine = physicalResult)

            pygame.display.flip()


if __name__ == '__main__':
    ai = RockWalkAndJump()
    ai.run_game()
