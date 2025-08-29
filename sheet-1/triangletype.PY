angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))


if angle1 + angle2 + angle3 == 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Right triangle")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Obtuse triangle")
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("Acute triangle")
    elif angle1 == 60 or angle2 == 60 or angle3 == 60:
        print("Equilateral triangle")
    else:
        print("Acute triangle")
else:
    print("Not a valid triangle - angles must sum to 180 degrees")