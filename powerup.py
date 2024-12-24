# Define the directions and their corresponding movements
DIRECTIONS = ["N", "E", "S", "W"]

# Function to turn left or right
def turn(current_direction, turn_direction):
    idx = DIRECTIONS.index(current_direction)
    if turn_direction == "L":
        idx = (idx - 1) % 4
    elif turn_direction == "R":
        idx = (idx + 1) % 4
    return DIRECTIONS[idx]

# Function to move the robot forward
def move(x, y, direction):
    if direction == "N":
        y += 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y -= 1
    elif direction == "W":
        x -= 1
    return x, y

# Main function to process the robot's movements
def process_robot_movements(plateau_x, plateau_y, start_position, instructions):
    x, y, direction = start_position
    for command in instructions:
        if command in ["L", "R"]:
            direction = turn(direction, command)
        elif command == "M":
            x, y = move(x, y, direction)
            # Ensure the robot stays within the plateau boundaries
            x = max(0, min(x, plateau_x))
            y = max(0, min(y, plateau_y))
    return x, y, direction

# Function to parse input from a file and output results
def main(input_file, output_file):
    with open(input_file, "r") as file:
        lines = file.read().strip().split("\n")
    
    # Read plateau dimensions
    plateau_x, plateau_y = map(int, lines[0].split())

    results = []
    i = 1
    while i < len(lines):
        # Parse robot's initial position
        start_x, start_y, start_direction = lines[i].split()
        start_position = (int(start_x), int(start_y), start_direction)
        # Parse movement instructions
        instructions = lines[i + 1]
        # Process robot movements
        final_position = process_robot_movements(plateau_x, plateau_y, start_position, instructions)
        results.append(f"{final_position[0]} {final_position[1]} {final_position[2]}")
        i += 2

    # Write output to the file
    with open(output_file, "w") as file:
        file.write("\n".join(results))

if __name__ == "__main__":
    # Provide input and output file paths
    print(" input data comes from input.txt and output data in the output.txt")
    main("input.txt", "output.txt")

