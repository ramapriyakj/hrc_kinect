#!/usr/bin/env python
import rospy
import tf2_msgs.msg
from std_msgs.msg import String

joint_count = 0;
frame_count = 0;
frame = []
joints = []

class joint:
    def __init__(self,joint_name,joint_x,joint_y,joint_z):
        self.joint_number = self.getRank(joint_name)
        self.joint_name = joint_name;
        self.joint_x = joint_x;
        self.joint_y = joint_y;
        self.joint_z = joint_z;

    def __cmp__(self, other):
        if hasattr(other, 'joint_number'):
            return self.joint_number.__cmp__(other.joint_number)

    #method ranks and arranges joint information from kinect
    def getRank(self,joint_name):
        if joint_name == "torso_1":
            return 0;
        elif joint_name == "neck_1":
            return 1;
        elif joint_name == "head_1":
            return 2;
        elif joint_name == "left_shoulder_1":
            return 3;
        elif joint_name == "left_elbow_1":
            return 4;
        elif joint_name == "left_hand_1":
            return 5;
        elif joint_name == "right_shoulder_1":
            return 6;
        elif joint_name == "right_elbow_1":
            return 7;
        elif joint_name == "right_hand_1":
            return 8;
        elif joint_name == "left_hip_1":
            return 9;
        elif joint_name == "left_knee_1":
            return 10;
        elif joint_name == "left_foot_1":
            return 11;
        elif joint_name == "right_hip_1":
            return 12;
        elif joint_name == "right_knee_1":
            return 13;
        elif joint_name == "right_foot_1":
            return 14;

#print joints
def printJoint(joint_obj):
    value = "";
    for x in joint_obj:
        value = value + str(x.joint_name) + "," + str(x.joint_number) + "," + str(x.joint_x) + "," + str(x.joint_y) + "," + str(x.joint_z) + ",";
    value = "{" + value[:-1] + "}";
    rospy.loginfo(value);

#print frames
def printFrame(frame_obj):
    value = ""
    for joint_obj in frame_obj:
        for x in joint_obj:
            value = value + str(x.joint_x) + "," + str(x.joint_y) + "," + str(x.joint_z) + ",";
    value = "["+ value[:-1] + "]";
    rospy.loginfo(value);

#function to write frames to file
def writeToFile(filename,data):
    with open(filename, "a") as f:
        f.write(data+"\n");
        f.close();

#oncle tensor flow model is ready. It can be plugged in and service can be called here.
def processFrame(frame_obj):
    printFrame(frame_obj)
    value = ""
    for joint_obj in frame_obj:
        for x in joint_obj:
            value = value + str(x.joint_x) + "," + str(x.joint_y) + "," + str(x.joint_z) + ",";
    value = "["+ value[:-1] + "]";
    # append frame to file
    # writeToFile("/home/ramapriya/data/CrossArmsRam.txt", value);
    #call tensor flow code to get human action
    #publish to HumanActionEstimationTopic.
    pub.publish(value)

def initialize():
    global pub;
    rospy.init_node('HumanActionRecognition', anonymous=True);
    pub = rospy.Publisher('HumanActionEstimationTopic', String, queue_size=5000)
    rospy.Subscriber('/tf', tf2_msgs.msg.TFMessage, processMessages)
    rospy.spin()

#Method to process joint information from .bag file.
def processMessages(data):
    global pub;
    global frame;
    global joints;
    global joint_count;
    global frame_count;
    if joint_count < 15:
        obj = joint(data.transforms[0].child_frame_id,data.transforms[0].transform.rotation.x,data.transforms[0].transform.rotation.y,data.transforms[0].transform.rotation.z);
        joints.append(obj);
        joint_count = joint_count+1;
        if joint_count == 15:
            joint_count = 0;
            joints = sorted(joints, key=lambda joint: joint.joint_number)
            if frame_count < 30:
                frame.append(joints);
                joints = []
                frame_count = frame_count+1;
                if frame_count == 30:
                    frame_count = 0;
                    processFrame(frame)
                    frame = []

if __name__ == '__main__':
    try:
        initialize();
    except rospy.ROSInterruptException:
        pass
