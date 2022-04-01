from src.Board.BoardImage import BoardImage


class BlockPixel:

    RADIUS: int = 8
    LOW_THRESHOLD = 100
    HIGH_THRESHOLD = 100

    def __init__(self, board_image: BoardImage, board_row: int, board_column: int):
        self.x_position = 2 * board_column * self.RADIUS + self.RADIUS
        self.y_position = 2 * board_row * self.RADIUS + self.RADIUS

        self.color = board_image.array[self.y_position, self.x_position]

        self.red_color = self.color[0]
        self.blue_color = self.color[1]
        self.green_color = self.color[2]

    @property
    def is_red_low(self):
        return self.red_color <= self.LOW_THRESHOLD

    @property
    def is_red_high(self):
        return self.red_color >= self.HIGH_THRESHOLD

    @property
    def is_blue_low(self):
        return self.blue_color <= self.LOW_THRESHOLD

    @property
    def is_blue_high(self):
        return self.blue_color >= self.HIGH_THRESHOLD

    @property
    def is_green_low(self):
        return self.green_color <= self.LOW_THRESHOLD

    @property
    def is_green_high(self):
        return self.green_color >= self.HIGH_THRESHOLD
