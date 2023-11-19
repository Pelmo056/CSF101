import unittest
import pygame
from pygamefinal import Dino, Ground, Cactus  

class TestDinoGame(unittest.TestCase):
    def test_dino_jump(self):
        def setUp(self):
            pygame.init()
        self.screen = pygame.display.set_mode((900, 500))
        pygame.display.set_caption('Dino game')
        self.clock = pygame.time.Clock()
        self.font = pygame.freetype.Font(None, 40)

    def tearDown(self):
        pygame.quit()

 #Check if the Dino moved upwards
def test_dino_jump(self):
    dino = Dino(pygame.Surface((100, 100)), (100, 400))
    initial_y = dino.rect.y
    dino.jump()
    self.assertTrue(dino.in_jump)
    self.assertTrue(dino.rect.y < initial_y)  

# Check if the ground moved to the left   
    def test_ground_update(self):
        ground = Ground(pygame.Surface((800, 142)), (300, 450))
        initial_x = ground.rect.x
        ground.update()
        self.assertTrue(ground.rect.x < initial_x)

# Check if the cactus moved to the left
    def test_cactus_update(self):
        dino = Dino(pygame.Surface((100, 100)), (100, 400))
        cactus = Cactus(pygame.Surface((50, 80)), (910, 400))
        initial_x = cactus.rect.x
        cactus.update()
        self.assertTrue(cactus.rect.x < initial_x)  

 # Check if collision is detected
    def test_collision_detection(self):
        dino = Dino(pygame.Surface((100, 100)), (100, 400))
        cactus = Cactus(pygame.Surface((50, 80)), (105, 400))
        self.assertTrue(cactus.rect.colliderect(dino.rect))  

if __name__ == '__main__':
    unittest.main()
