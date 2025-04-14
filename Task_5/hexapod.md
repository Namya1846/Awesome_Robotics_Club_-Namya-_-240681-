{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11540\viewh8420\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs36 \cf0 Project : Hexapod 
\fs24 \

\fs28 Inverse Kinematics Solution\
\
->Link Lengths Used\
- Coxa (L1): 5.0 units  \
- Femur (L2): 10.0 units  \
- Tibia (L3): 15.0 units  \
\
-> Function: `inverse_kinematics(x, y, z)`\
This function computes the joint angles `(\uc0\u952 1, \u952 2, \u952 3)` for a robotic leg to reach a target point in 3D space.\
\
-> Steps:\
1. Calculate rotation angle `\uc0\u945 ` (theta1) using `atan2(y, x)` which mean arctan(y/x).\
2. Compute the distance from the coxa to the target.\
3. Check reachability using `r <= L2 + L3`.\
4. Use trigonometry (law of cosines) to calculate `\uc0\u947 ` (theta3) and `\u946 ` (theta2).\
5. Return angles in degrees, rounded to two decimal places.\
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