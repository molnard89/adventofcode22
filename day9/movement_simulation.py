import math

class Rope:
    head_position = [0, 0]
    previous_head_position = [0, 0]
    tail_position = [0, 0]

    def updateHeadPosition(self, direction):
        self.previous_head_position = list(self.head_position)
        if direction == 'U':
            self.head_position[1] += 1
        elif direction == 'D':
            self.head_position[1] -= 1
        elif direction == 'R':
            self.head_position[0] += 1
        elif direction == 'L':
            self.head_position[0] -= 1


    def updateTailPositon(self, direction):
        x_distance, y_distance = self.getDistance()
        if max([abs(x_distance), abs(y_distance)]) < 2:
            return None
        x_distance, y_distance = self.getPreviousDistance()
        if math.sqrt(x_distance**2 + y_distance**2) > 1:
            self.tail_position = list(self.previous_head_position)
            return None
        if direction == 'U':
            self.tail_position[1] += 1
        elif direction == 'D':
            self.tail_position[1] -= 1
        elif direction == 'R':
            self.tail_position[0] += 1
        elif direction == 'L':
            self.tail_position[0] -= 1
        return None

    def getDistance(self):
        x_distance = self.head_position[0] - self.tail_position[0]
        y_distance = self.head_position[1] - self.tail_position[1]
        return x_distance, y_distance

    def getPreviousDistance(self):
        x_distance = self.previous_head_position[0] - self.tail_position[0]
        y_distance = self.previous_head_position[1] - self.tail_position[1]
        return x_distance, y_distance


if __name__ == "__main__":

    with open("rope_head_moves.txt") as f:
        move_set = f.readlines()
    move_set = [move.strip() for move in move_set]

    simulated_rope = Rope()
    tail_positions = []

    for move in move_set:
        direction, steps = move.split(" ")
        for step in range(int(steps)):
            simulated_rope.updateHeadPosition(direction)
            simulated_rope.updateTailPositon(direction)
            tail_positions.append(list(simulated_rope.tail_position))

    set_of_tail_positions = [list(x) for x in set(tuple(x) for x in tail_positions)]
    print(f"Number of unique positions visited by the tail = {len(set_of_tail_positions)}")