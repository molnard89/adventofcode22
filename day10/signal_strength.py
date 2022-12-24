CYCLES_TO_CHECK = [20, 60, 100, 140, 180, 220]

class signal:
    def __init__(self):
        self.register = 1
        self.cycle = 0
        self.signal_strength = 0
        self.signal_strength_sum = 0
        self.pixel_stream = []

    def parseCommand(self, command):
        print(command)
        if "noop" in command:
            self.runCycleProcesses()
        elif "addx" in command:
            self.runCycleProcesses()
            self.runCycleProcesses()
            self.register += int(command.split(" ")[1])

    def runCycleProcesses(self):
        self.cycle += 1
        print(f"During cycle {self.cycle}")
        self.checkPixelLight()
        self.updateSignalStrengthSum()
    def updateSignalStrengthSum(self):
        if self.cycle in CYCLES_TO_CHECK:
            # print(f"The value in the X register during {self.cycle} cycle is {self.register}")
            # print(f"Therefore, the signal strength (X value * cycle number) is {self.cycle*self.register}")
            # print("-------")
            self.signal_strength_sum += self.cycle*self.register

    def checkPixelLight(self):
        sprite_location = [self.register-1, self.register, self.register+1]
        # print(f"Spirte is at {sprite_location}")
        cycle_norm = (self.cycle % 40)-1
        pixel_value = "#" if cycle_norm in sprite_location else "."
        # print(f"CRT pixel is drawing {pixel_value} to {cycle_norm}")
        self.pixel_stream.append(pixel_value)
        # print("---")


with open("cpu_commands.txt") as f:
    commands = f.readlines()
commands = [command.strip() for command in commands]

signal_state = signal()

for command in commands:
    signal_state.parseCommand(command)

print(f"The sum of signal strength at the inspected cycles is {signal_state.signal_strength_sum}")

for i, pixel in enumerate(signal_state.pixel_stream):
    endchar = "\n" if (i+1)%40 == 0 else " "
    print(pixel, end=endchar)
