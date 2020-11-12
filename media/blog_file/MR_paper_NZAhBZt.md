# Human-robot interaction for robotic manipulator programming in Mixed Reality

#### Abstract

The paper presents an approach for interactive programming of the robotic manipulator using mixed reality. The developed system is based on the HoloLens glasses connected through Robotic Operation System to Unity engine
and robotic manipulators. The system gives a possibility to recognize the real robot location by the point cloud analysis, to use virtual markers and menus for the task creation, to generate a trajectory for execution in the simulator or on the real manipulator. It also provides the possibility of scaling virtual and real worlds for more accurate planning. The proposed framework has been tested on pick-and-place and contact operations execution by UR10e and KUKA iiwa robots.

#### **Authors**: 

##### Mikhail Ostanin, Stanislav Mikhel, Alexey Evlampiev, Valeria Skvortsova, Alexandr Klimchik, IEEE Member

#### Introduction

- The need for effective human robot-interaction is vital in the rapidly developing Industry 4.0 scenario. 
- Traditionally, there have been three methods to program a robot: 
  * Online: human controls robot using an operator console.
  * Offline: Control program is created and uploaded to robot.
  * Programming by demonstration: Manually demonstrating tasks and making the robot learn from actions. While this might be more intuitive and requires lesser training than the other methods, it needs special equipment and hardware for compatibility. This method can advanced with the aid of Mixed Reality (MR). MR is defined as a combination of Virtual reality and augmented reality, where the real and the virtual world co-exist and interact with each other. 
- Why Mixed Reality? 
  * Allows you to teach the robot and play back the result on a "digital-twin" of the robot before being implemented on the physical robot. 
  * Faster prototyping, examination of overall performance and efficiency 
  * Visualization of sensory data and robot configuration 
  * Intuitive interaction with gestures, sound and motion controllers. 
  * Testing in the virtual environment eliminates harm to both robot hardware as well the humans surrounding them.
  * A previous study used Rethink Baxter’s Robotic arm in different scenarios including MR, motion controller, and 2D visualization. They found out that the MR head-mounted display improved overall process time by 62%, precision by 11%, and collision prediction accuracy by 16%. 

* The same group of researchers in their previous work were able to achieve the following: 
  * Used the HoloLens and two robots KUKA iiwa and Agilus 
  * MR system was based on Unity 3D and Mixed Reality Toolkit - Unity 
  * System was broken down into the following: 
    * Application manager 
    * Geometrical Path Planner 
    * Trajectory Planner 
    * Simulator 
  * First, the user built a geometric path that was based on points placement and connects them in different ways (point-to-point, arc, custom paths). 
  * Trajectory planning was then performed and the user could run a simulation before seeing it work on the real robot. 
* In the current work, the main computational tasks are executed on the Robot Operating System (ROS), along with improvements to make the interaction more intuitive. The functionality was also improved with the ability to add various tools, grips and visualize the workspace of the robot. 

#### System Components 

* The system can be broken down as follows: 

1. Visualization and interface on Microsoft HoloLens. Unity 3D game engine and Mixed Reality Toolkit was used for HoloLens development. 
2. Computing & communication with ROS Kinetic. 
3. Robots used: UR10e and KUKA iiwa LBR 14

* The application has an interface, geometrical path planning (using Moveit!, a ROS-based motion planning framework), spatial mapping (visualization of real space in which the user is located), and virtual models. Robots have access to different tools and grippers. 
* This is summarized in the block diagram below: 

![](../../Pictures/MR_paper_1.png)

#### Implementation and Interaction 

The system designed by the authors has features that can be broadly divided into basic functionalities and mixed-reality specific features. 

#### **Basic Features**

1. **Menu**: Mixed reality user interface for accessing various functionalities of the robot, and controlling robot settings.

   <img src="../../Pictures/Screenshot from 2020-11-07 12-46-14.png" alt="Screenshot from 2020-11-07 12-46-14"  /> 

2. **Robot state:** To visualize the state of the robot (e.g., joint positions or pose of the end-effector)

3. **Geometrical path planning:** User-defined geometric path can be defined by defining a sequence of waypoints, each representing the position and orientation of the end-effector. This is shown in Fig 1(c). The individual waypoints or control points can be connected to one another using a path, which can straight lines, arcs, or a custom user-defined path. The control points can also have associated gripper actions such as opening and closing. 

4. **Trajectory Generation:** The inbuilt ROS motion planning framework is used for trajectory generation, which builds a model from the provided Unified Robot Description Format (URDF) files. The data of control points and the path taken to connect them are specified to the Moveit! framework, which then carries out trajectory generation by solving the inverse kinematics problems. 

5. **Simulator:** It plays back to the user on simulation the trajectory obtained from Moveit!. With mixed reality, it is possible to model collision detection of a virtual model of the robot in the real robot's physical space. 

6. **Workspace visualization:** With HoloLens, it is possible to visualize the workspace of the robot to instantly assess the accessibility of a point in space by the robot. In addition when the user is away from the robot workspace, indicating that the robot might not be monitored, the robot operation automatically slows down or stops. The green sphere in the image below is the workspace of the robot as viewed through the HoloLens. 

   ![workspace_viz](../../Pictures/workspace_viz.png)

   

#### **Mixed Reality Features**

The above basic functionalities are currently implementable on traditional systems that do not have a mixed reality component. However, the authors have also incorporated some additional features that cannot be realized in a traditional systems and are unique to Mixed Reality platforms. These are as follows: 

1. **Robot Placement:** It is possible to place a virtual robot and superimpose it with a real one to visualize how it would behave before performing any action on the physical robot. It works as follows: 

   * The real robot's pose is taken into consideration for effective superimposition of the real robot and the virtual robot. 

   * The algorithm takes as input the scene from the MR glasses and a point cloud of the robot model. 

   * The steps include preprocessing point clouds, clustering objects, searching for robot-like objects, and finding the position of the robot. The position of the robot is found by comparing the robot model's point cloud with the point cloud input from the HoloLens. The blue cluster of points in the sparse point cloud below is the result of applying the robot-recognition algorithm: 

     ![](../../Pictures/MR_paper_3.png)

   * Let's now have a look at the working of this algorithm in detail. First, both the robot model and the HoloLens model will be in different frames of reference having different origins. The first step will be to carry out a homogeneous transformation between the two frames. 

   * In the robot model's point cloud, we do not need internal points of the robot, as this just makes the system bulky. A sparse point cloud representation will suffice and hence internal points are removed using the Jarvis algorithm. 

   * Next, planar surfaces like the floor and ceiling are removed using the [RANSAC algorithm.](http://www.cse.yorku.ca/~kosta/CompVis_Notes/ransac.pdf)

   * The [DBSCAN algorithm](https://towardsdatascience.com/how-dbscan-works-and-why-should-i-use-it-443b4a191c80), a popular data-clustering algorithm is used to cluster points in the pointcloud belonging to the same object. The volume of each of these clustered objects is compared with the model robot's volume to determine which of those clusters is the robot. Finally localization of the robot and alignment of the virtual and real robot models is carried out using the Iterative Closest Point (ICP) algorithm. 

2. **Shortest Path Avoiding Obstacles**

   * Once the user has provided control points between which a trajectory needs to be planned, they would also need to provide the exact trajectory which avoids the obstacles in the environment. 
   * However, to make the user experience better, an RRT-based obstacle avoidance algorithm has been implemented to automatically plan the shortest path possible avoiding all obstacles.

3. **Path Scaling**

   * This is done for creating a more accurate path. By doubling the scale of the holograms used in control point selection, the accuracy of the path thus obtained will also be much better. Without scaling, the accuracy is about 1-2 cm and after scaling, improves to 0.5 cm. 

     

In the images below, the robot can be seen to be performing two tasks, one of pick and place and the other of drawing an image on a paper with user commands given from the MR device. 

* Robot performing pick and place: 

  ![MR_paper_6](../../Pictures/MR_paper_6.png)

* Robot drawing on a paper: 

  ![MR_paper_5](../../Pictures/MR_paper_5.png)

#### **Conclusion**

The paper presented a MR based approach to interactive robot programming. The unique features presented in addition to the basic functionalities were robot placement, shortest path obstacle avoidance using RRT, and path scaling for improved accuracy. The framework was also validated on two robots performing pick-and-place tasks and contact operation involving the drawing of different shapes on a surface. In the future, the team plans to integrate multi-user capabilities, automatic work-cell construction, teleoperation and integration of AR and VR devices in the MR-based system. 

