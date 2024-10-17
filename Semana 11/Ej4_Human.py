class Head():
    def __init__(self, eye_color, nose_shape, haircut, hair_color, wear_glasses):
        self.eye_color = eye_color
        self.nose_shape = nose_shape
        self.haircut = haircut
        self.hair_color = hair_color
        self.wear_glasses = wear_glasses

    
    def describe_head(self):
        glasses_status = "wears glasses" if self.wear_glasses else "does not wear glasses"
        return f"Head with {self.eye_color} eyes, {self.nose_shape} nose, {self.hair_color} {self.haircut} haircut, {glasses_status}."


class Torso():
    def __init__(self, abdomen, head, right_arm, left_arm):
        self.abdomen = abdomen
        self.head = head
        self.right_arm = right_arm 
        self.left_arm = left_arm


    def describe_torso (self):
        return f"Torso with {self.abdomen} abdomen, {self.head.describe_head()}, {self.right_arm.describe_arm()} and {self.left_arm.describe_arm()}."
    

class Arm():
    def __init__ (self, elbow_status, shoulder_status, hand):
        self.elbow_status = elbow_status
        self.shoulder_status = shoulder_status
        self.hand = hand

    def describe_arm(self):
        elbow_status = "Elbow not broken" if self.elbow_status else "Elbow broken"
        shoulder_status = "Shoulder not dislocated" if self.shoulder_status else "Shoulder dislocated"
        return f"Arm with {elbow_status} and {shoulder_status}, and {self.hand.describe_hand()}."


class Hand():
    def __init__(self, fingers, palm_line, wrist_status):
        self.fingers = fingers
        self.palm_line = palm_line
        self.wrist_status = wrist_status

    
    def describe_hand(self):
        wrist_status = "Wrist not injured" if self.wrist_status else "Wrist injured"
        return f"Hand with {self.fingers} fingers, {self.palm_line} palm line, and {wrist_status}."


class Leg():
    def __init__(self, thigh, knee_status, feet):
        self.thigh = thigh
        self.knee_status = knee_status
        self.feet = feet

    def describe_leg(self):
        knee_status = "Knee not injured" if self.knee_status else "Knee injured"
        return f"Leg with {self.thigh} thigh, {knee_status}, and {self.feet.describe_feet()}."


class Feet():
    def __init__(self, toe_count, arch_type, ankle_status):
        self.toe_count = toe_count
        self.arch_type = arch_type
        self.ankle_status = ankle_status

    def describe_feet(self):
        ankle_status = "Ankle healthy" if self.ankle_status else "Ankle injured"
        return f"Feet with {self.toe_count} toes, {self.arch_type} arch, and {ankle_status}."

class Human ():
    def __init__ (self, head, torso, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.torso = torso
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


    def introduce_human(self):
        return f"{self.head.describe_head()}\n{self.torso.describe_torso()}\n{self.right_leg.describe_leg()}\n{self.left_leg.describe_leg()}"
    

head = Head("brown", "Greek", "Back Faded", "Black", True)

hand_right = Hand(5, "life", True)
arm_right = Arm(True, True, hand_right)

hand_left = Hand(5, "life", True)
arm_left = Arm(False, True, hand_left)

feet_right = Feet(5, "low", True)
leg_right = Leg("slim", True, feet_right)

feet_left = Feet(5, "low", False)
leg_left = Leg("slim", False, feet_left)

torso = Torso("Flat", head, arm_right, arm_left)

human = Human(head, torso, arm_right, arm_left, leg_right, leg_left)

print(human.introduce_human())
