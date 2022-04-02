import numpy as np
from PIL import Image


class BoardImage:

    X_START: int = 88
    X_END: int = 185

    Y_START: int = 22
    Y_END: int = 215

    def __init__(self, game_image):
        self.__image = game_image

        self.__crop_board()
        self.__suppress_noise()
        self.__image.save("board.jpeg")
        self.__image_array = np.array(self.__image)

    def __crop_board(self):
        self.__image = Image.fromarray(
            self.__image[self.Y_START:self.Y_END, self.X_START:self.X_END]
        )

    def __suppress_noise(self):
        r, g, b = self.__image.split()

        r = r.point(lambda i: int(i / 200) * 255)

        g = g.point(lambda i: int(i / 200) * 255)

        b = b.point(lambda i: int(i / 200) * 255)

        self.__image = Image.merge('RGB', (r, g, b))

    @property
    def image(self):
        return self.__image

    @property
    def height(self):
        return self.__image_array.shape[0]

    @property
    def width(self):
        return self.__image_array.shape[1]

    @property
    def array(self):
        return self.__image_array

