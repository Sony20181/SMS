class Vector(object):
    def __init__(self, *args):
        self.values = args

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("У векторов разные размерности")
            return sum(a * b for a, b in zip(self, other))
        elif isinstance(other, int):
            product = tuple(a * other for a in self)
            return self.__class__(*product)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("У векторов разные размерности")
            divided = tuple(self[i] / other[i] for i in range(len(self)))
        elif isinstance(other, int):
            divided = tuple(a / other for a in self)

        return self.__class__(*divided)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("У векторов разные размерности")
            added = tuple(a + b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            added = tuple(a + other for a in self)

        return self.__class__(*added)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            subbed = tuple(a - b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            subbed = tuple(a - other for a in self)

        return self.__class__(*subbed)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __pow__(self, other):
        raise ValueError("Невозможно возвести вектор в степень")

    def __rpow__(self, other):
        return self.__pow__(other)

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return "{" + ";".join(list(map(str, self.values))) + "}"
