class Course:
    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration

    def __str__(self):
        return f"[{self.name}][{self.instructor}][{self.duration}]"

    def __repr__(self):
        return f"[{self.name}][{self.instructor}][{self.duration}]"

    def __hash__(self):
        return hash((self.name, self.instructor, self.duration))

    def __eq__(self, other):
        return self.name == other.name \
               and self.instructor == other.instructor \
               and self.duration == other.duration


c1 = Course("POOP", "Mark", 35)
c2 = c1
c3 = Course("POOP", "Mark", 35)
c4 = Course("BDPY", "Mark", 35)

print(c1, hex(hash(c1)))
print(c2, hex(hash(c2)))
print(c3, hex(hash(c3)))
print(c4, hex(hash(c4)))
print(c1 is c2, c1 is c3, c1 is c4)
print(c1 == c2, c1 == c3, c1 == c4)
s1 = {c1}
print("c1 in", s1)
s1.add(c2)
print("c1 c2 in", s1)
s1.add(c3)
print("c1 c2 c3 in", s1)
s1.add(c4)
print("c1 c2 c3 c4 in", s1)

# -----------
s1 = {'A'}
s2 = {'B'}
# s1.add(s2)
