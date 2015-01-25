cmake_minimum_required(VERSION 2.8.3)
project(nao_kick)
find_package(catkin REQUIRED COMPONENTS std_msgs geometry_msgs nav_msgs trajectory_msgs
  naoqi_msgs actionlib_msgs)

catkin_python_setup()

add_message_files(FILES
  Path.msg
  Times.msg
  )

add_service_files(FILES
  Kick.srv
  SetEffectorPosition.srv
  SetEffectorPositions.srv
  )

generate_messages(DEPENDENCIES
  std_msgs naoqi_msgs actionlib_msgs nav_msgs trajectory_msgs
  )

catkin_package(CATKIN_DEPENDS
  actionlib_msgs
  )

install(PROGRAMS
  nodes/nao_kick
  nodes/nao_effector
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  )

install(DIRECTORY
  launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  )

install(DIRECTORY conf/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/conf
  )
