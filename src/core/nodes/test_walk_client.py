import rospy
from core.srv import MotionService, WalkService

def walk_client(n, step, side, ang):
    rospy.wait_for_service('walk_service')
    try:
        a = rospy.ServiceProxy('walk_service', WalkService)
        a(n, step, side, ang)
    except rospy.ServiceException as e:
        print("Service call failed:", e)

def motion_client(motion_id):
    rospy.wait_for_service('motion_service')
    try:
        a = rospy.ServiceProxy('motion_service', MotionService)
        a(motion_id)
    except rospy.ServiceException as e:
        print("Service call failed:", e)

if __name__ == "__main__":
    num = 10
    stepLength = 64
    sideLength = 0
    rotation = 0
    walk_client(num, stepLength, 0, 0.0)
    motion_client('test_head')

        