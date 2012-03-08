## Written and experimented with by Daniel Ballard.
## 1:09 AM 3/4/2012

# Standard imports for Panda3d.
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText,TextNode
from direct.task import Task
from direct.task.Task import Task 
from panda3d.core import *
from pandac.PandaModules import Texture, TextureStage, CardMaker
from direct.gui.OnscreenImage import OnscreenImage

# This may not be necessary but configures Panda to use OpenAL.
#loadPrcFileData("", "audio-library-name p3openal_audio")

class Application(ShowBase):
    def __init__(self):
        # Always add this!!! To load/render/etc.
        ShowBase.__init__(self)

        # Make a plane to play the movie on.
        self.cm = CardMaker("plane")
        self.cm.setFrame(-1, 1, -1, 1)

        # Render that plane to the render2d for Panda.
        self.plane = self.render2d.attachNewNode(self.cm.generate())

        # Load movie and its sound (if it has sound).
        self.movie = self.loader.loadTexture("videos/loading_screen.ogm")
        self.sound = self.loader.loadSfx("videos/loading_screen.ogm")

        # Load movie into the texture plane.
        self.plane.setTexture(self.movie)

        # This can prevent squashing or distorting of the video.
        self.plane.setTexScale(TextureStage.getDefault(), self.movie.getTexScale())

        # 0 means do not loop infinitely.
        self.movie.setLoop(0)

        # If it has sound, synchronize it to the video.
        self.movie.synchronizeTo(self.sound)

        # Play the sound.
        self.sound.play()
        

        self.loadingText=OnscreenText("Loading...",1,fg=(1,1,1,1),pos=(0,0),align=TextNode.ACenter,scale=.07,mayChange=1) 
        self.graphicsEngine.renderFrame() #render a frame otherwise the screen will remain black 
        self.graphicsEngine.renderFrame() #idem dito

        taskMgr.doMethodLater(14,self.loadImageAsPlane,"ImageLoader")
		
    def loadImageAsPlane(self, task): 
		#Load image as 3d plane; Arguments: filepath -- image file path yresolution -- pixel-perfect width resolution 
        b = OnscreenImage(parent=render2d, image='models/Fireworks.jpg')
        
        
# Assign the class to a variable.        
app = Application()
# And finally, run it!!
app.run()
