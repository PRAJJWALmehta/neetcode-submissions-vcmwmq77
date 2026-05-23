class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0

        for x, y in self.points:
            if abs(px - x) == abs(py-y) and px != x and py != y:
                if (px, y) in self.points and (x, py) in self.points:
                    res += self.points[px, y]*self.points[x, py]*self.points[x, y]
        
        return res
        
