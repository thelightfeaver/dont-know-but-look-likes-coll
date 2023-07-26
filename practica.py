class Polyma():

    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __add__(self, other):
        return Polyma(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __repr__(self) -> str:
        return f"Polyma(*{self.coeffs})"
    
    def __len__(self):
        return len(self.coeffs)


p1 = Polyma(1, 2, 3)
p2 = Polyma(3, 4, 3)
