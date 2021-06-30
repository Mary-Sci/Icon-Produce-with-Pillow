import sys
sys.path.append("..") # Adds higher directory to python modules path.
from Figure.FigureIcon import FigureIconIMG

print("-------------------------------")

#Create icon object with palette
iconFigurePalette1 = FigureIconIMG()

#make palette full transparent wiht 0. For non-transparent place 128
iconFigurePalette1.setAlphaIMG(0)

#select the RGB color of the icon
iconFigurePalette1.RGB(127, 9, 24)

#draw a circle with default. Change values for eclipse etc. 
#iconFigurePalette1.drawEllipse(c1=0, c2=0, x=300, y=300)
#iconFigurePalette1.drawEllipse(c1=0, c2=200, x=300, y=300)

#draw a star with default. Change values for eclipse etc. 
#iconFigurePalette1.drawStar()


#draw a triangle with default. Change values for eclipse etc. 
#iconFigurePalette1.drawTriangle()

#draw a rectangle with default. Change values for eclipse etc. 
#iconFigurePalette1.drawRectangle()

#fill and image with desired color
#iconFigurePalette1.alterImage("star.png", "star1.png")

#icon resize, actual sizing...
iconFigurePalette1.imageResize((155,155))

#icon Save Test
iconFigurePalette1.imageSave("aaatest2_" + str("red") + ".png" )
#iconFigurePalette1.imageSave()

