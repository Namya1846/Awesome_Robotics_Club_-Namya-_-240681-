
# Project : Hexapod 
## Inverse Kinematics Solution

## Link Lengths Used
- Coxa (L1): 5.0 units  
- Femur (L2): 10.0 units 
- Tibia (L3): 15.0 units

## Function: `inverse_kinematics(x, y, z)
This function computes the joint angles `(θ1, θ2, θ3)` for a robotic leg to reach a target point in 3D space.

## Steps:
1. Calculate rotation angle `α' (theta1) using `atan2(y, x)` which mean arctan(y/x).
2. Compute the distance from the coxa to the target.
3. Check reachability using `r <= L2 + L3`.
4. Use trigonometry (law of cosines) to calculate `γ` (theta3) and `β` (theta2).
5. Return angles in degrees, rounded to two decimal places.
\
-> Function: `test_inverse_kinematics()`\
This runs five test cases:\
- Test 1: A normal reachable point.\
- Test 2: A point close to the base.\
- Test 3: A point near the leg\'92s maximum reach.\
- Test 4: An unreachable point.\
- Test 5: A point with a large negative z.\
\
Output\
Each test prints the target position, calculated joint angles (if reachable), and reachability status.\
\
 User Input\
The code also lets the user input `x`, `y`, and `z`, and displays the resulting angles or an error if unreachable.\
\
}
