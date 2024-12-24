## Explanation of Design and Assumptions
This application simulates a robot navigating a plateau based on a set of commands. It uses simple control logic to manage directions and movements, ensuring the robot adheres to boundary constraints. The program reads inputs from a file, processes commands for each robot, and writes the resulting positions and directions to an output file.

## Assumptions
### Plateau Dimensions:

The plateau is defined as a grid with the bottom-left corner at (0, 0) and the top-right corner at (plateau_x, plateau_y).
### Input Format:

#### Input is correctly formatted with:
The first line containing plateau dimensions.
Subsequent lines alternating between the robot's starting position and its movement instructions.

#### Commands:

L and R turn the robot left and right, respectively.
M moves the robot forward in the current direction.
#### File Paths:

The input is read from input.txt, and the output is written to output.txt.


## Instructions to Run the Application
### Prerequisites
1. Python 3 must be installed on your system.
2. Ensure the input.txt file is in the same directory as the script.

### Run the Script:
`python powerup.py`

### Check the Output
The program writes the results to output.txt. For the above input, the output file would contain


