PROJECT: BALL BALANCING BOT
PART A:
1. Mechanical Design
Actuators Used:
 a. Ball Drive System
•	Number of Actuators: 3
•	Type: Omnidirectional wheels + Rotary Motors
•	Arrangement: Equally spaced (typically 120° apart) around the ball
•	Function: Control the rolling of the main spherical ball in X, Y directions
•	How it works: Each motor drives a wheel that contacts the ball. Their combined motion allows the ball to roll in any direction (similar to holonomic drive).
 b. Reaction Wheel System
•	Number of Actuators: 1
•	Type: High-speed rotary motor with a flywheel
•	Placement: Mounted horizontally at the top of the robot
•	Function: Provides angular momentum control in the vertical axis (yaw rotation)
 c. Body Adjustment (Optional in Some Versions)
•	Some ball bots also use servo motors to adjust the center of mass (not clearly shown in this video, but common in enhanced designs)
 
 2. Role of Additional Degrees of Freedom (DoF)
 Degrees of Freedom:
•	Without reaction wheel: 2 DoF (ball tilt control)
•	With reaction wheel: 3 DoF (tilt + yaw)
 
 How Additional DoF Improves the Robot:
 a. Improves Stability
•	The reaction wheel adds rotational control about the vertical axis, allowing the robot to counteract yaw disturbances (e.g., sudden twists).
•	Without it, the robot might spin uncontrollably during turns or dynamic shifts.
 b. Enhances Responsiveness
•	The robot can rapidly adjust orientation without changing its position.
•	This is crucial in dynamic environments or when reacting to uneven terrain or external pushes.
 c. Increases Control Precision
•	With 3D control (X, Y, and Yaw), it can perform smoother and more controlled trajectories.
•	Useful in applications like human-robot interaction, where controlled orientation is as important as position.
3.

4. Pros
i) complexity - Compact and minimalistic structure
                            - Reaction wheel adds only one axis
ii)reliability - Fewer mechanical joints = less wear and tear
                        - Can operate on smooth floors with low friction loss
Cons 
i) complexity - Balancing on a ball requires real-time control + precise sensing
                            - Reaction wheel integration adds to the control algorithm complexity
ii) reliability - Sensitive to slight ground unevenness
                         - Any motor failure (especially drive motors) may lead to immediate            imbalance


PART B:
1)The two approaches for detecting and tracking are –
Common sensor –> IMU (inertial measurement unit) Measuring how much the platform is tilted and which direction to move. Example - MPU6050, MPU9250, BNO055.
i)	Using force sensitive sensors along with IMU – it detects pressure or force  , place it below the platform and it will detect the position of ball by weight shift on the platform. Example – FSR402
ii)	Using infrared sensors along with IMU- Use multiple IR sensors (like IR proximity sensors) arranged in a grid under the platform and detecting how close the ball is to each sensor. Example- analog IR sensor.

  2) How the motion is tracked?
i)  Sensor placement : we will place 3-4 FSRs or IRs under the platform uniformly.
ii)  Sensing the motion : according to the pressure distribution or the infrared waves detection we will analyse the motion of the ball.
iii)Control the platform: once the motion is analyzed the  control algorithm is used to balance the ball- Typical control systems:
•	PID Controller (Proportional, Integral, Derivative)
o	If the ball moves left, tilt platform right slightly.
o	If it moves fast, tilt more aggressively.
o	If it overshoots, reduce tilt.
     3)Pros and cons of FSR and IR sensors 
i) FSR sensor 
Pros:
•	Simple and cheap
•	Fast response time
•	Not affected by lighting or surface color
•	Easy to read with analog pins
Cons:
•	Not highly accurate
•	Needs physical contact and pressure from the ball
•	Hard to detect ball when it's barely touching the surface
•	Slightly nonlinear response curve
ii)IR sensor 
Pros:
•	Can detect the ball without physical contact
•	Good accuracy (especially analog IR)
•	Fast enough for real-time tracking
•	Easy to get small-sized modules
Cons:
•	Affected by ambient light and surface material (dark/rough = low reflection)
•	Needs proper mounting angles to avoid blind spots
•	Calibration needed for distance vs. voltage mapping
•	Analog versions more expensive than FSRs

