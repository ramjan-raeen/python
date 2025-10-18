class StartPatterns:
    def __init__(self, num):
        """Initialised the pattern with number of rows."""
        self.num=num

    def left_aligned_right_angle_triangle(self, name):
        """Left Aligned Right-Angle Triangle using Nested Loop."""

        print(f"\n{name} :")
        for r in range(1, self.num+1):
            for c in range(1, r+1):    
                print("*", end="")
            print("")
    def right_aligned_right_angle_triangle(self, name):
        """Right Aligned Right Angle triangle."""

        print(f"\n{name} :")
        for r in range(1, self.num+1):
            for c in range(1, self.num+1-r):
                print(" ", end="")
            for k in range(r):
                print("*", end="")
            print()
    def left_aligned_inverted_triangle(self, name):
        """Left Aligned Inverted Triangle."""
        print(f"\n{name} :")
        for r in range(1, self.num+1):
            for c in range(1, self.num+2-r):
                print('*', end="")
            print()
    def right_aligned_inverted_triangle(self, name):
        """Right Aligned Inverted Triangle."""
        print(f"\n{name} :")
        for r in range(1, self.num+1):
            for c in range(1, r):
                print(" ", end="")
            for k in range(1, self.num+2-r):
                print("*", end="")
            print()
    def pyramid(self, name):
        """Pyramid.."""
        print(f"\n{name} :")
        for r in range(1, self.num+1):
            for c in range(1, self.num+1-r):
                print(" ", end="")
            for k in range(2*r-1):
                print("*", end="")
            print()
    def inverted_pryramid(self, name):
        """Inverted Pyramid.."""
        print(f"\n{name} :")
        for r in range(1, self.num+1):
            for c in range(1, r):
                print(" ", end="")
            for k in range(1, ( (2*self.num+1 )- (2*r-1) )):
                print("*", end="")
            print()
    def diamond(self, name):
        """Diamond.."""
        print(f"\n{name} :")
        for r in range(1, self.num+1):
            for c in range(1, self.num+1-r):
                print(" ", end="")
            for k in range(2*r-1):
                print("*", end="")
            print()
        for r in range(2, self.num+1):
            for c in range(1, r):
                print(" ", end="")
            for k in range(1, (2*self.num+1)-(2*r-1)):
                print("*", end="")
            print()

num_rows = int(input("Enter numbers of rows: "))
pattern = StartPatterns(num_rows)
pattern.left_aligned_right_angle_triangle("Left Aligned Right Angle Triangle..")
pattern.right_aligned_right_angle_triangle("Right Aligned Right Angle Triangle..")
pattern.left_aligned_inverted_triangle("Left Aligned Inverted Triangle..")
pattern.right_aligned_inverted_triangle("Right Aligned Inverted Triangle..")
pattern.pyramid("Pyramid")
pattern.inverted_pryramid("Inverted Pyramid")
pattern.diamond("Daimond")