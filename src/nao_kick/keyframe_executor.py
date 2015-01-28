import time

import rospy

from std_srvs.srv import Empty
from std_msgs.msg import String, Header

from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from actionlib import SimpleActionClient
from geometry_msgs.msg import Twist, Vector3

from naoqi_msgs.msg import (JointTrajectoryAction, JointTrajectoryGoal,
                          BodyPoseWithSpeedAction, BodyPoseWithSpeedGoal)

from nao_kick.srv import (SetEffectorPosition,
                         SetEffectorPositionResponse, SetEffectorPositions,
                         SetEffectorPositionsResponse)

from nao_kick.msg import Path, Times 

class KeyframeExecutor(object):


    def __init__(self):

        self._goal = ""

        self._aISeq = 0

        rospy.logdebug("Initializing KeyframeExecutor")
        rospy.logdebug("Waiting for set_effector_position")
        rospy.wait_for_service('set_effector_position')
        self._setEffectorPositionProxy = rospy.ServiceProxy(
            "set_effector_position", SetEffectorPosition)

        rospy.logdebug("Waiting for set_effector_positions")
        rospy.wait_for_service('set_effector_positions')
        self._setEffectorPositionsProxy = rospy.ServiceProxy(
            "set_effector_positions", SetEffectorPositions)

        self._postureClient = SimpleActionClient('body_pose_naoqi',
                                                 BodyPoseWithSpeedAction)
        rospy.logdebug("Waiting for body_pose_naoqi")
        self._postureClient.wait_for_server()

        self._client = SimpleActionClient("joint_trajectory",
                                          JointTrajectoryAction)
        rospy.logdebug("Waiting for joint_trajectory")
        self._client.wait_for_server()

        self._functionLookUp = {
            "angleInterpolation" : self._angleInterpolation,
            "wait" : self._wait,
            "setEffectorPosition" : self._setEffectorPosition,
            "setEffectorPositions" : self._setEffectorPositions,
            "posture" : self._posture
        }

    def _packPath(self, path):
        """
        Packs a path in python list to a Twist message type
        """

        result = []

        for twist in path:
            result.append(Twist(Vector3(twist[0], twist[1], twist[2]),
                                Vector3(twist[3], twist[4], twist[5])))

        return Path(result)


    def _packPaths(self, paths):
        """
        Packs a series of paths in a python list
        """

        result = []

        for path in paths:
            result.append(self._packPath(path))

        return result


    def _packTimes(self, times):
        """
        Converts a serie of float to time Ros Time messages
        """

        result = []

        for time in times:
            result.append(Times(time))

        return result

    def _packEffectors(self, effectors):
        """
        Converts a python list of effectors that should be affected by
        the motion to Ros String messages
        """

        result = []

        for effector in effectors:
            result.append(String(effector))

        return result

    def _packJointTrajectoryPoint(self, angles, time):

        return [JointTrajectoryPoint(angles, [0], [0], rospy.Duration(time))]

    def _packTrajectory(self, names, angles, time):

        header = Header(self._aISeq, rospy.Time.now(), "0")
        self._aISeq += 1
        return JointTrajectory(header, names,
                               self._packJointTrajectoryPoint(angles, time))

    def _packJointTrajectoryGoal(self, names, angles, time, absolute):

        return JointTrajectoryGoal(self._packTrajectory(names, angles, time),
                                   absolute)

    def _angleInterpolation(self, frame):

        rospy.logdebug("Waiting for joint_trajectory server.")
        self._client.wait_for_server()
        self._goal = self._packJointTrajectoryGoal(
            frame["names"], frame["angles"], frame["time"], frame["isAbsolute"])
        self._client.send_goal(self._goal)
        rospy.logdebug("Waiting for joint_trajectory result.")
        self._client.wait_for_result()
        rospy.logdebug("Done waiting for joint_trajectory result.")

    def _setEffectorPosition(self, frame):

        rospy.logdebug("Setting effector position.")
        self._setEffectorPositionProxy(String(frame['effector']),
                                       frame['space'],
                                       self._packPath(frame['path']),
                                       frame['axisMask'],
                                       Times(frame['time']),
                                       frame["isAbsolute"])
        rospy.logdebug("Done setting effector position.")

    def _setEffectorPositions(self, frame):

        rospy.logdebug("Setting effector positions.")
        self._setEffectorPositionsProxy(self._packEffectors(frame['effectors']),
                                        frame['space'],
                                        self._packPaths(frame['paths']),
                                        frame['axisMasks'],
                                        self._packTimes(frame['times']),
                                        frame["isAbsolute"])
        rospy.logdebug("Done setting effector positions.")

    def _posture(self, frame):

        rospy.logdebug("Wait for body_pose_naoqi")
        self._postureClient.wait_for_server()
        self._postureClient.send_goal(
            BodyPoseWithSpeedGoal(frame["posture"], frame["speed"]))
        rospy.logdebug("Waiting for body_pose_naoqi result")
        self._postureClient.wait_for_result()
        rospy.logdebug("Done waiting for body_pose_naoqi result")

    def _wait(self, frame):
        time.sleep(frame["time"])

    def execute(self, keyframe):
        """
        Executes the given keyframe
        """

        rospy.logdebug("Executing keyframe.")
        for trial in range(keyframe["repeat"]):
            for frame in keyframe["frames"]:
                self._functionLookUp[frame["function"]](frame)
            time.sleep(keyframe["paus"])

