from collections import deque


def find_unique_set(beeps, N):
    cutout = deque([], N)
    for i, beep in enumerate(beeps):
        cutout.append(beep)
        index = i+1
        if index > N-1:
            if len(set(cutout)) == N:
                return index
    return None


if __name__ == "__main__":
    with open('signal_stream.txt') as f:
        signal_stream = f.readlines()[0]

    begin_broadcast = find_unique_set(signal_stream, 4)
    start_of_message_marker = find_unique_set(signal_stream, 14)

    print(f"Start of packet = {begin_broadcast}")
    print(f"Start of message = {start_of_message_marker}")
