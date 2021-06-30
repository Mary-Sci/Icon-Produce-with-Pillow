from Figure.Figure import Figure
from PIL import Image, ImageDraw

class FigureIconIMG(Figure):


	def __init__(self):
		Figure.__init__(self)
		self.img = Image.new("RGB", (300, 300), (255, 255, 255))
		self.draw = ImageDraw.Draw(self.img)

	def setAlphaIMG(self,alpha = None):
		self.alpha = alpha
		self.img.putalpha(self.alpha)
	
	def RGB(self , R , G , B):
		self.R = R
		self.G = G
		self.B = B
		#return '#%02x%02x%02x' % (R, G, B)
	
	def drawEllipse(self, c1=0, c2=0, x=300, y=300):
		self.c1 = c1
		self.c2 = c2
		self.x = x
		self.y = y
		self.draw.ellipse((c1 , c2, x, y), fill = (self.R, self.G, self.B))

	def drawStar(self):
		self.draw.polygon(((150, 0), (50, 300), (300, 100),(0, 100), (250, 300)), fill = (self.R, self.G, self.B))
		self.draw.polygon(((110, 100), (200, 100), (210, 180),(150, 220), (90, 180)), fill = (self.R, self.G, self.B))

	def drawTriangle(self):
		self.draw.polygon(((150, 0), (0, 300), (300, 300)), fill = (self.R, self.G, self.B))

	def drawRectangle(self):
		self.draw.rectangle(((0), (0), (300), (300)), fill = (self.R, self.G, self.B))

	def alterImage(self, path1 = None, path2 = None):
		self.path1 = path1
		self.path2 = path2
		self.img = Image.open(self.path1)
		self.x, self.y = self.img.size
		self.p = Image.new("RGBA", self.img.size, (self.R, self.G, self.B))
		self.p.paste(self.img, (0, 0, self.x, self.y), self.img)
		self.p.save(self.path2)



	def imageResize(self, scale = (128,128)):
		self.scale = scale
		self.img = self.img.resize(self.scale)

	def imageSave(self, path = "testx.png"):
		self.path = path
		self.img.save(self.path)


