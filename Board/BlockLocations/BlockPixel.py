from Board.BoardImage import BoardImage


class BlockPixel:

    RADIUS: int = 8

    def __init__(self, board_image: BoardImage, board_row: int, board_column: int):
        self.x_position = 2 * board_column * self.RADIUS + self.RADIUS
        self.y_position = 2 * board_row * self.RADIUS + self.RADIUS

        self.color = board_image.array[self.y_position, self.x_position]
