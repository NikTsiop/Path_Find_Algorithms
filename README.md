# Path Find Algorithms

This repository contains implementations of various pathfinding algorithms, often used in artificial intelligence, robotics, and game development for navigation and shortest-path solutions. These algorithms help in finding the optimal path between two points in a grid, graph, or other structures.

## Algorithms Included

The repository includes the following pathfinding algorithms:

- **Depth-First Search (DFS)**: A traversal algorithm that goes as deep as possible along a path before backtracking. It does not guarantee the shortest path.
- **Breadth-First Search (BFS)**: A simple algorithm that explores all possible paths level by level. BFS guarantees finding the shortest path in unweighted graphs. **(In progress)**
- **Dijkstra's Algorithm**: A shortest path algorithm that works on weighted graphs, providing the shortest path from a start node to all other nodes. **(In progress)**
- **A\***: An informed search algorithm that uses heuristics to find the shortest path more efficiently than Dijkstra's in many cases. It combines the cost to reach the node and an estimate of the cost to reach the goal **(In progress)**
- **Greedy Best-First Search**: Similar to A*, but only considers the heuristic, not the cost from the start. This can make it faster but less reliable in finding the optimal path. **(In progress)**

## Features

- **Visualizations**: Each algorithm includes a visual representation to help understand its pathfinding process and behavior.
- **Adjustable Grid**: Set grid size and customize obstacles to test the algorithms in different scenarios.
- **Performance Comparison**: Evaluate the efficiency and pathfinding speed of each algorithm. **(In progress)**

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/NikTsiop/Path_Find_Algorithms.git
cd Path_Find_Algorithms
```
Make sure you have Python installed, and then install any required libraries by running:
```bash
pip install -r requirements.txt
```
## Usage
To run the visualizations and test each algorithm, execute the main script:
```bash
python main.py
```
You can select the algorithm you want to use and adjust settings such as grid size and obstacles.

Requirements
 - Python 3.x
 - Additional Python libraries (specified in requirements.txt)

## Contributing

Contributions are welcome! If you have improvements or additional algorithms you'd like to add, feel free to fork the repository, create a new branch, and submit a pull request.

 - Fork the repository
 - Create a new branch (git checkout -b feature-branch)
 - Commit your changes (git commit -m "Add new feature")
 - Push to the branch (git push origin feature-branch)
 - Open a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, please reach out via ntsioplos@gmail.com or open an issue in the repository.

Thank you for checking out this repository! 
