import pygame


class DrawInformation:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED =  255, 0, 0
	GREY = 128, 128, 128
	BACKGROUND_COLOR = WHITE

	def __init__(self, width, height):
		self.width = width
		self.height = height

		pygame.display.set_caption("Minimal program")
		
		screen = pygame.display.set_mode((width, height))


def main():

	pygame.init()

	ventana = DrawInformation(200,400)
	
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				
if __name__ == "__main__":
	main()
