class ChessCoordinate:

    _interned = {}

    def __new__(cls, file, rank):
        key = (file, rank)

        if key not in cls._interned:
            self = object.__new__(cls)
            self._file = file
            self._rank = rank

            cls._interned[key] = self

        return cls._interned[key]

        # print(f"cls = {cls.__name__}")
        # print(f"args = {args}")
        # print(f"kwargs = {kwargs}")
        # obj = object.__new__(cls)
        # print(f"id(obj) = {id(obj)}")
        # return obj

    # init jest niepotrzebny, bo konstruktor przejął jego rolę
    # def __init__(self, file, rank):
    #     # print(f"id(self) = {id(self)}")
    #     self._file = file
    #     self._rank = rank

    @property
    def file(self):
        return self._file

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f'{self.rank}{self._file}'

    def __repr__(self):
        return f'{type(self).__name__}(file={self._file}, rank={self._rank})'


def starting_board():
    return {
        "white_king": ChessCoordinate("e", 1),
        "white_queen": ChessCoordinate("d", 1),
        "white_rook1": ChessCoordinate("a", 1),
        "white_rook2": ChessCoordinate("h", 1),
        "white_bishop1": ChessCoordinate("c", 1),
        "white_bishop2": ChessCoordinate("f", 1),
        "white_knight1": ChessCoordinate("b", 1),
        "white_knight2": ChessCoordinate("g", 1),
        "white_pawn1": ChessCoordinate("a", 2),
        "white_pawn2": ChessCoordinate("b", 2),
        "white_pawn3": ChessCoordinate("c", 2),
        "white_pawn4": ChessCoordinate("d", 2),
        "white_pawn5": ChessCoordinate("e", 2),
        "white_pawn6": ChessCoordinate("f", 2),
        "white_pawn7": ChessCoordinate("g", 2),
        "white_pawn8": ChessCoordinate("h", 2),

        "black_king": ChessCoordinate("e", 8),
        "black_queen": ChessCoordinate("d", 8),
        "black_rook1": ChessCoordinate("a", 8),
        "black_rook2": ChessCoordinate("h", 8),
        "black_bishop1": ChessCoordinate("c", 8),
        "black_bishop2": ChessCoordinate("f", 8),
        "black_knight1": ChessCoordinate("b", 8),
        "black_knight2": ChessCoordinate("g", 8),
        "black_pawn1": ChessCoordinate("a", 7),
        "black_pawn2": ChessCoordinate("b", 7),
        "black_pawn3": ChessCoordinate("c", 7),
        "black_pawn4": ChessCoordinate("d", 7),
        "black_pawn5": ChessCoordinate("e", 7),
        "black_pawn6": ChessCoordinate("f", 7),
        "black_pawn7": ChessCoordinate("g", 7),
        "black_pawn8": ChessCoordinate("h", 7),
    }


def main():
    import tracemalloc
    tracemalloc.start()

    boards = [starting_board() for _ in range(10000)]

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_kb = peak / 10 ** 3

    print(f"Peak KB: {peak_kb:.0f} kB")

if __name__ == '__main__':
    main()
