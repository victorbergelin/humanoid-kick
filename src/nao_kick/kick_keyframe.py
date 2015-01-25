# NaoQi frames for the robot
import motion

# keyfram order: adjust, kick, wait, return
kickRightKeyframe = {
    "frames" : [
        {
            "function" : "posture",
            "posture" : "StandInit",
            "speed" : 0.5
        },
        {
            "function" : "setEffectorPosition",
            'space' : motion.FRAME_ROBOT,
            'isAbsolute' : False,
            'path' : [[0.0, 0.086, 0.0, 0.0, 0.0, 0.0]],
            'axisMask' : 63,
            'time': [1.0],
            'effector' : "Torso"
        },
        {
            "function" : "setEffectorPositions",
            'space' : motion.FRAME_ROBOT,
            'isAbsolute' : False,
            'paths' : [
                [[-0.02,  0.0,  0.04, 0.0, 0.0, 0.0],   #RLeg 1
                 [-0.04,  0.0,  0.04, 0.0, 0.0, 0.0],   #RLeg 2
                 [ 0.1,   0.0,  0.04, 0.0, 0.0, 0.0],   #RLeg 3
                 [ 0.07,  0.0,  0.04, 0.0, 0.0, 0.0],   #RLeg 4
                 [ 0.0,   0.0,  0.02, 0.0, 0.0, 0.0]],  #Rleg 5
                [[ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0],   #RArm 1
                 [ 0.08, -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 2
                 [-0.05, -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 3
                 [ 0.0,  -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 4
                 [ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0]],  #RArm 5
                [[ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0],   #LArm 1
                 [-0.03,  0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 2
                 [ 0.08,  0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 3
                 [ 0.0,   0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 4
                 [ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0]]], #LArm 5
            'axisMasks' : [63, 63, 63],
            'times' : [[0.4, 0.6, 0.8, 1.0, 1.6],
                       [0.4, 0.6, 0.8, 1.0, 1.6],
                       [0.4, 0.6, 0.8, 1.0, 1.6]],
            'effectors' : ["RLeg", "RArm", "LArm"]
        },
        {
            "function" : "wait",
            "time" : 0.1
        },
        {
            "function" : "setEffectorPositions",
            'space' : motion.FRAME_ROBOT,
            'isAbsolute' : False,
            'paths' : [
                [[0.0, -0.086, 0.0,  0.0, 0.0, 0.0]],  #Torso
                [[0.0,  0.0,  -0.02, 0.0, 0.0, 0.0]]], #RLeg
            'axisMasks' : [63, 63],
            'times' : [[1.0], [1.0]],
            'effectors' : ["Torso", "RLeg"]
        },
        {
            "function" : "posture",
            "posture" : "StandInit",
            "speed" : 0.5
        }
    ],
    "repeat" : 1,
    "paus" : 0
}

kickLeftKeyframe = {
    "frames" : [
        {
            "function" : "posture",
            "posture" : "StandInit",
            "speed" : 0.5
        },
        {
            "function" : "setEffectorPosition",
            'space' : motion.FRAME_ROBOT,
            'isAbsolute' : False,
            'path' : [[0.0, -0.086, 0.0, 0.0, 0.0, 0.0]],
            'axisMask' : 63,
            'time' : [1.0],
            'effector' : "Torso"
        },
        {
            "function" : "setEffectorPositions",
            'space' : motion.FRAME_ROBOT,
            'isAbsolute' : False,
            'paths' : [
                [[-0.02,  0.0,  0.04, 0.0, 0.0, 0.0],   #LLeg 1
                 [-0.04,  0.0,  0.04, 0.0, 0.0, 0.0],   #LLeg 2
                 [ 0.1,   0.0,  0.04, 0.0, 0.0, 0.0],   #LLeg 3
                 [ 0.07,  0.0,  0.04, 0.0, 0.0, 0.0],   #LLeg 4
                 [ 0.0,   0.0,  0.02, 0.0, 0.0, 0.0]],  #Lleg 5
                [[ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0],   #RArm 1
                 [-0.03, -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 2
                 [ 0.08, -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 3
                 [ 0.0,  -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 4
                 [ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0]],  #RArm 5
                [[ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0],   #LArm 1
                 [ 0.08,  0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 2
                 [-0.05,  0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 3
                 [ 0.0,   0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 4
                 [ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0]]], #LArm 5
            'axisMasks' : [63, 63, 63],
            'times' : [[0.4, 0.6, 0.8, 1.0, 1.6],
                       [0.4, 0.6, 0.8, 1.0, 1.6],
                       [0.4, 0.6, 0.8, 1.0, 1.6]],
            'effectors' : ["LLeg", "RArm", "LArm"]
        },
        {
            "function" : "wait",
            "time" : 0.1
        },
        {
            "function" : "setEffectorPositions",
            'space' : motion.FRAME_ROBOT,
            'isAbsolute' : False,
            'paths' : [
                [[0.0, 0.086, 0.0,  0.0, 0.0, 0.0]],  #Torso
                [[0.0, 0.0,  -0.02, 0.0, 0.0, 0.0]]], #LLeg
            'axisMasks' : [63, 63],
            'times' : [[1.0], [1.0]],
            'effectors' : ["Torso", "LLeg"]
        },
        {
            "function" : "posture",
            "posture" : "StandInit",
            "speed" : 0.5
        }
    ],
    "repeat" : 1,
    "paus" : 0
}
"""
adjustRightKeyframe = {'path' : [[0.0, 0.086, 0.0, 0.0, 0.0, 0.0]],
                       'axisMask' : 63,
                       'time': [1.0],
                       'effector' : "Torso"}

kickRightKeyframe = {'paths' : [
    [[-0.02,  0.0,  0.04, 0.0, 0.0, 0.0],   #RLeg 1
     [-0.04,  0.0,  0.04, 0.0, 0.0, 0.0],   #RLeg 2
     [ 0.1,   0.0,  0.04, 0.0, 0.0, 0.0],   #RLeg 3
     [ 0.07,  0.0,  0.04, 0.0, 0.0, 0.0],   #RLeg 4
     [ 0.0,   0.0,  0.02, 0.0, 0.0, 0.0]],  #Rleg 5
    [[ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0],   #RArm 1
     [ 0.08, -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 2
     [-0.05, -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 3
     [ 0.0,  -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 4
     [ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0]],  #RArm 5
    [[ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0],   #LArm 1
     [-0.03,  0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 2
     [ 0.08,  0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 3
     [ 0.0,   0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 4
     [ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0]]], #LArm 5
                     'axisMasks' : [63, 63, 63],
                     'times' : [[0.4, 0.6, 0.8, 1.0, 1.6],
                                [0.4, 0.6, 0.8, 1.0, 1.6],
                                [0.4, 0.6, 0.8, 1.0, 1.6]],
                     'effectors' : ["RLeg", "RArm", "LArm"]}

returnRightKeyframe = {'paths' : [
    [[0.0, -0.086, 0.0,  0.0, 0.0, 0.0]],  #Torso
    [[0.0,  0.0,  -0.02, 0.0, 0.0, 0.0]]], #RLeg
                       'axisMasks' : [63, 63],
                       'times' : [[1.0], [1.0]],
                       'effectors' : ["Torso", "RLeg"]}


adjustLeftKeyframe = {'path' : [[0.0, -0.086, 0.0, 0.0, 0.0, 0.0]],
                      'axisMask' : 63,
                      'time' : [1.0],
                      'effector' : "Torso"}

kickLeftKeyframe = {'paths' : [
    [[-0.02,  0.0,  0.04, 0.0, 0.0, 0.0],   #LLeg 1
     [-0.04,  0.0,  0.04, 0.0, 0.0, 0.0],   #LLeg 2
     [ 0.1,   0.0,  0.04, 0.0, 0.0, 0.0],   #LLeg 3
     [ 0.07,  0.0,  0.04, 0.0, 0.0, 0.0],   #LLeg 4
     [ 0.0,   0.0,  0.02, 0.0, 0.0, 0.0]],  #Lleg 5
    [[ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0],   #RArm 1
     [-0.03, -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 2
     [ 0.08, -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 3
     [ 0.0,  -0.04, 0.0,  0.0, 0.0, 0.0],   #RArm 4
     [ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0]],  #RArm 5
    [[ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0],   #LArm 1
     [ 0.08,  0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 2
     [-0.05,  0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 3
     [ 0.0,   0.04, 0.0,  0.0, 0.0, 0.0],   #LArm 4
     [ 0.0,   0.0,  0.0,  0.0, 0.0, 0.0]]], #LArm 5
                    'axisMasks' : [63, 63, 63],
                    'times' : [[0.4, 0.6, 0.8, 1.0, 1.6],
                               [0.4, 0.6, 0.8, 1.0, 1.6],
                               [0.4, 0.6, 0.8, 1.0, 1.6]],
                    'effectors' : ["LLeg", "RArm", "LArm"]}

returnLeftKeyframe = {'paths' : [
    [[0.0, 0.086, 0.0,  0.0, 0.0, 0.0]],  #Torso
    [[0.0, 0.0,  -0.02, 0.0, 0.0, 0.0]]], #LLeg
                      'axisMasks' : [63, 63],
                      'times' : [[1.0], [1.0]],
                      'effectors' : ["Torso", "LLeg"]}
"""