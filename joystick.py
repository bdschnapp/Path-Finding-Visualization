import pygame

class ParentController(object):
    clock = pygame.time.Clock()

    def __init__(self, instance):
        self.instance = instance
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            if i == instance:        
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                self.axes = [None] * joystick.get_numaxes()
                self.buttons = [None] * joystick.get_numbuttons()
                self.hats = [None] * joystick.get_numhats()

    def updateParent(self):

        joystick_count = pygame.joystick.get_count()

        #Issue with DS4 joystick that enables the gyro axes only over bluetooth connection. Issue has not been resolved and it is assumed that all DS4 joysticks are using a wired connection
        wiredConnection = True

        for i in range(joystick_count):
            if i == self.instance:        
                joystick = pygame.joystick.Joystick(i)
                joystick.init()

                naxes = joystick.get_numaxes()
                for i in range(naxes):
                    axis = joystick.get_axis(i)
                    self.axes[i] = axis
                
                nbuttons = joystick.get_numbuttons()
                for i in range(nbuttons):
                    button = joystick.get_button(i)
                    self.buttons[i] = button

                nhats = joystick.get_numhats()
                for i in range(nhats):
                    hat = joystick.get_hat(i)
                    self.hats[i] = hat

    def tick(self, frames):
        self.clock.tick(frames)

class DualShock4(object):

    clock = pygame.time.Clock()

    def __init__(self, instance):
        self.instance = instance
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            if i == instance:        
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                self.axes = [None] * joystick.get_numaxes()
                self.buttons = [None] * joystick.get_numbuttons()
                self.hats = [None] * joystick.get_numhats()
        self.x = self.buttons[1]
        self.square = self.buttons[0]
        self.triangle = self.buttons[3]
        self.circle = self.buttons[2]
        self.rtButton = self.buttons[7]
        self.ltButton = self.buttons[6]
        self.lb = self.buttons[4]
        self.rb = self.buttons[5]
        self.rsButton = self.buttons[11]
        self.lsButton = self.buttons[10]
        self.options = self.buttons[9]
        self.ps4 = self.buttons[12]
        self.share = self.buttons[8]
        self.touchpad = self.buttons[13]
        #self.up = list(self.hats[0])[0]
        #self.down = list(self.hats[0])[0]
        #self.left = list(self.hats[0])[1]
        #self.right = list(self.hats[0])[1]
        self.rtAsix = self.axes[2]
        self.ltAxis = self.axes[5]
        self.lsVertical = self.axes[1]
        self.lsHorizontal = self.axes[0]
        self.rsVertical = self.axes[4]
        self.rsHorizontal = self.axes[3]
    
    def update(self):
        #updates arrays of data generalized for all joysticks
        joystick_count = pygame.joystick.get_count()

        #Issue with DS4 joystick that enables the gyro axes only over bluetooth connection. Issue has not been resolved and it is assumed that all DS4 joysticks are using a wired connection
        wiredConnection = True

        for i in range(joystick_count):
            if i == self.instance:        
                joystick = pygame.joystick.Joystick(i)
                joystick.init()

                naxes = joystick.get_numaxes()
                for i in range(naxes):
                    axis = joystick.get_axis(i)
                    self.axes[i] = axis
                
                nbuttons = joystick.get_numbuttons()
                for i in range(nbuttons):
                    button = joystick.get_button(i)
                    self.buttons[i] = button

                nhats = joystick.get_numhats()
                for i in range(nhats):
                    hat = joystick.get_hat(i)
                    self.hats[i] = hat

        #then mapps those arrays to named buttons specific to each type of joystick
        self.x = self.buttons[0]
        self.square = self.buttons[3]
        self.triangle = self.buttons[2]
        self.circle = self.buttons[1]
        self.rtButton = self.buttons[7]
        self.ltButton = self.buttons[6]
        self.lb = self.buttons[4]
        self.rb = self.buttons[5]
        self.rsButton = self.buttons[12]
        self.lsButton = self.buttons[11]
        self.options = self.buttons[9]
        self.ps4 = self.buttons[10]
        self.share = self.buttons[8]
        self.touchpad = self.buttons[13]

        #self.up = self.hats[0][0]
        #self.down = self.hats[0][1]
        #self.left = self.hats[1][0]
        #self.right = self.hats[1][1]
        
        #rt and lt have both button and axis mappings (axis for getting trigger position, and button for boolean value of if trigger is pulled)
        #rs and ls have two axes each as well as a button for clicking
        self.rtAsix = self.axes[2]
        self.ltAxis = self.axes[5]
        self.lsVertical = self.axes[1]
        self.lsHorizontal = self.axes[0]
        self.rsVertical = self.axes[4]
        self.rsHorizontal = self.axes[3]

    def tick(self, frames):
        self.clock.tick(frames)
    
#XB1 mappings have not been verified
class XBoxOne(ParentController):
    def update(self):
        #updates arrays of data generalized for all joysticks
        self.updateParent()

        #then mapps those arrays to named buttons specific to each type of joystick
        self.a = self.buttons[0]
        self.x = self.buttons[2]
        self.y = self.buttons[3]
        self.b = self.buttons[1]
        self.start = self.buttons[7]
        self.back = self.buttons[6]
        self.lb = self.buttons[4]
        self.rb = self.buttons[5]
        self.rsButton = self.buttons[10]
        self.lsButton = self.buttons[9]
        self.xb1 = self.buttons[8]
        

        self.up = self.hats[0][0]
        self.down = self.hats[0][1]
        self.left = self.hats[1][0]
        self.right = self.hats[1][1]
        
        #rs and ls have two axes each as well as a button for clicking
        self.rtAsix = self.axes[2]
        self.ltAxis = self.axes[5]
        self.lsVertical = self.axes[1]
        self.lsHorizontal = self.axes[0]
        self.rsVertical = self.axes[4]
        self.rsHorizontal = self.axes[3]

