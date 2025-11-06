class StampMachine:
    def __init__(self):
        self.reset()
        self.stamped = False

    def reset(self):
        """Reset the stamp machine to initial settings"""
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0
        self.pattern = "no_pattern"
        self.color = "black"

    def mv(self, dx, dy):
        """Move the stamp position by dx and dy"""
        self.x += dx
        self.y += dy

    def rotate(self, r):
        """Rotate by r degrees"""
        self.angle += r
        # Normalize angle to [0, 360)
        self.angle = self.angle % 360

    def set_pattern(self, pattern):
        """Set the pattern"""
        self.pattern = pattern

    def set_color(self, color):
        """Set the color"""
        self.color = color

    def stamp(self):
        """Print the stamp result"""
        print(
            f"Stamping... [position: ({self.x:.2f}, {self.y:.2f}), rotation: {self.angle:.2f} degrees, pattern: {self.pattern}, color: {self.color}]"
        )
        self.stamped = True


# Main program
def main():
    machine = StampMachine()

    # Read 6 lines of commands
    for _ in range(6):
        line = input().strip()
        if not line:
            continue

        parts = line.split()
        command = parts[0]

        if command == "reset":
            machine.reset()
        elif command == "mv":
            dx = float(parts[1])
            dy = float(parts[2])
            machine.mv(dx, dy)
        elif command == "rotate":
            r = float(parts[1])
            machine.rotate(r)
        elif command == "set_pattern":
            pattern = parts[1]
            machine.set_pattern(pattern)
        elif command == "set_color":
            color = parts[1]
            machine.set_color(color)
        elif command == "stamp":
            machine.stamp()

    # If no stamp was called, print cancellation message
    if not machine.stamped:
        print("Stamping canceled")


if __name__ == "__main__":
    main()
