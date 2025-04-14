import math

# Link lengths
L1 = 5.0   # coxa
L2 = 10.0  # femur
L3 = 15.0  # tibia

def inverse_kinematics(x, y, z):
    try:
        # α: rotation around z-axis
        alpha = math.atan2(y, x)

        # horizontal distance from coxa joint
        d = math.sqrt(x**2 + y**2) - L1
        r = math.sqrt(d**2 + z**2)

        # Check if the target is reachable
        if r > (L2 + L3):
            return None

        # γ: knee angle using law of cosines
        gamma = math.acos((r**2 - L2**2 - L3**2) / (2 * L2 * L3))

        # β: shoulder angle
        theta = math.atan2(z, d)
        phi = math.acos((r**2 + L2**2 - L3**2) / (2 * r * L2))
        beta = theta - phi

        return round(math.degrees(alpha), 2), round(math.degrees(beta), 2), round(math.degrees(gamma), 2)

    except:
        return None

def test_inverse_kinematics():
    print("Inverse Kinematics Test Cases")

    test_cases = [
        {"label": "Test 1: Typical point", "position": (10, 10, -5)},
        {"label": "Test 2: Close to base", "position": (1, 1, 1)},
        {"label": "Test 3: Near max reach", "position": (20, 0, 0)},
        {"label": "Test 4: Unreachable", "position": (100, 100, 100)},
        {"label": "Test 5: Large negative z", "position": (5, 5, -15)},
    ]

    for case in test_cases:
        label = case["label"]
        x, y, z = case["position"]

        print(f"\n{label}")
        print(f"Target Position: x={x}, y={y}, z={z}")

        result = inverse_kinematics(x, y, z)

        if result is not None:
            theta1, theta2, theta3 = result
            print(f"Computed Angles: θ1={theta1:.2f}°, θ2={theta2:.2f}°, θ3={theta3:.2f}°")
            print("Reachability:  Reachable")
        else:
            print("Reachability:  Unreachable")

        print("-" * 40)

if __name__ == "__main__":
    test_inverse_kinematics()

    # Ask user for input
    x  = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    z = float(input("Enter z coordinate: "))

    result = inverse_kinematics(x, y, z)
    print("\nResult for user input:")
    if result is not None:
        theta1, theta2, theta3 = result
        print(f"θ1 = {theta1:.2f}°, θ2 = {theta2:.2f}°, θ3 = {theta3:.2f}°")
    else:
        print(" Target is unreachable.")
