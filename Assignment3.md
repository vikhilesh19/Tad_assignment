# Applications related to drones or VTOL.

## 1.Path Planning and Obstacle Avoidance for Drones
***<u>Applications </u>*** :  
Drones use graph based pathfinding algorithms like Dijkstra’s or BFS/DFS to find the safest and shortest path to destination.  

- Vertices represent possible waypoints or 3D coordinates in the environment.
- Edges represent valid paths between waypoints (with weights indicating distance, wind resistance, or energy cost).
- Dijkstra’s Algorithm helps in computing the most efficient route, minimizing the energy consumption.
- DFS/BFS can be used for quick exploration in simpler or known environments.

## 2.Path Planning and Navigation in Urban Air Mobility (UAM)
***<u>Applications </u>*** :  
In cities, VTOL more aircraft Should handle mid-air collisions,landing schedules and handle high traffic. Graph algorithms can manage this complex network.

- Vertices represent airspace zones, sky lanes, or vertiports (VTOL landing pads).
- Edges denote viable air routes between those zones.
- Minimum Spanning Tree (Prim’s or Kruskal’s) can help design efficient route networks with minimum infrastructure cost.
- BFS is used to monitor and re-route aircraft in case of air traffic congestion or emergencies.