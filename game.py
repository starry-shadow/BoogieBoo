from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
from pygame.locals import*

pygame.init()


class App:
    def __init__(self):
        self.running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        surface = pygame.display.set_mode((600, 400))
        mainmenu = pygame_menu.Menu('Welcome', 600, 400, theme=themes.THEME_SOLARIZED)
        mainmenu.add.text_input('Name: ', default='username', maxchar=20)
        mainmenu.add.button('Play', start_the_game)
        mainmenu.add.button('Levels', level_menu)
        mainmenu.add.button('Quit', pygame_menu.events.EXIT) 
        level = pygame_menu.Menu('Select a Difficulty', 600, 400, 
                                         theme=themes.THEME_BLUE)
        level.add.selector('Difficulty:',[('Hard',1),('Easy',2)], onchange=set_difficulty)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

