from src.Board.Blocks.BackGroundBlock import BackGroundBlock
from src.Board.Blocks.Block import Block
from src.Board.Blocks.CircleBlock import CircleBlock
from src.Board.Blocks.DiamondBlock import DiamondBlock
from src.Board.Blocks.HeartBlock import HeartBlock
from src.Board.Blocks.LowerTriangleBlock import LowerTriangleBlock
from src.Board.Blocks.StarBlock import StarBlock
from src.Board.Blocks.UpperTriangleBlock import UpperTriangleBlock
from src.Board.BoardImage import BoardImage


class BlockClassifier:

    THRESHOLD = 200

    TYPE_LOOKUP_TABLE: dict = {
        (0, 0, 0): BackGroundBlock(),
        (1, 1, 1): BackGroundBlock(),
        (1, 0, 0): HeartBlock(),
        (0, 1, 0): CircleBlock(),
        (0, 0, 1): LowerTriangleBlock(),
        (1, 1, 0): StarBlock(),
        (1, 0, 1): DiamondBlock(),
        (0, 1, 1): UpperTriangleBlock(),
    }

    def classify(self, board_image: BoardImage, x_position: int, y_position: int) -> Block:
        neighborhood_red = [board_image.array[y_position, x_position + i][0]
                            for i in range(-8, 8)]
        neighborhood_green = [board_image.array[y_position, x_position + i][1]
                              for i in range(-8, 8)]
        neighborhood_blue = [board_image.array[y_position, x_position + i][2]
                             for i in range(-8, 8)]

        #lower_neighbor = board_image.array[y_position + 1, x_position]

        red_idx = 1 if max(neighborhood_red) > self.THRESHOLD else 0
        green_idx = 1 if max(neighborhood_green) > self.THRESHOLD else 0
        blue_idx = 1 if max(neighborhood_blue) > self.THRESHOLD else 0

        type_idx = (red_idx, green_idx, blue_idx)

        return self.TYPE_LOOKUP_TABLE[type_idx]
