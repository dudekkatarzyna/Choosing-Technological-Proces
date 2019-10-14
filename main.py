import kivy

from cta import ResourceData, ChoosingTechnologicalProcess
from gui.GuiApp import *

kivy.require('1.10.1')

if __name__ == '__main__':
    # r1 = ResourceData(0.7, 2100, False)
    # r2 = ResourceData(2.5, 1200, False)
    # print(
    #     ChoosingTechnologicalProcess([r1, r2], 5.2, 20).solve()
    # )

    GuiApp().run()
