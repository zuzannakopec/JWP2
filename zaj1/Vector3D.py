import math


class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        print("Vector3d({}, {}, {})".format(self.x, self.y, self.z))

    def norm(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def __add__(self, other):
        return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3d(self.x * other, self.y * other, self.z * other)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        new_x = self.y * other.z - self.z + other.y
        new_y = self.z * other.x - self.x + other.z
        new_z = self.x * other.y - self.y + other.x
        return Vector3d(new_x, new_y, new_z)

    @staticmethod
    def are_orthogonal(vector1, vector2):
        if vector1.dot(vector2) == 0:
            return True
        return False


vector = Vector3d(1, 2, 1)
vector1 = Vector3d(2, 1, 3)

print("Dodawanie wektorow")
vector3 = vector + vector1
vector3.__str__()

print("Odejmowanie wektorow")
vector3 = vector - vector1
vector3.__str__()

print("Mnozenie przez skalar")
vector3 = vector3 * 5
vector3.__str__()


print("Iloczyn skalarny")
iloczyn_skalarny = vector3.dot(vector)
print(iloczyn_skalarny)

print("Iloczyn wektorowy")
vector4 = vector.cross(vector1)
vector4.__str__()

print("Czy wektory sa ortogonalne")
print(vector4.are_orthogonal(vector))