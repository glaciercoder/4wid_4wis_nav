# 四轮独立转向机器人底盘

## Instalation

+ 源码下载

## 启动：

+ 进入工作空间 4wid_ws并source
  
  ```bash
  cd ~/4wid_ws                 #use the path of your workspace. In this doc, the workspace is placed at ~/ directly
  . install/setup.bash
  ```

+ 启动rviz，Gazebo，以及Nav2（以转移的Turtlebot3为例）
  
  ```bash
  export TURTLEBOT3_MODEL=waffle
  export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/4wid_ws/src/turtlebot3_gazebo/models     # use the path of your workspace
  ros2 launch bringup_4wid bringup_4wid_launch.py headless:=False
  ```
  
  
  
  
  
  
  
  

## WorkSpace介绍

### Packages

#### 启动导航及Rviz、Gazebo：bringup_4wid

+ 包内结构：
  
  ```
  bringup_4wid/                            #root of the package
      CMakeLists.txt
      include/bringup_4wid/
      package.xml
      src/
      launch/                              #launching files
          bringup_4wid_launch.py           #1
          rviz_launch.py                   #2
          bringup_launch.py                #2
          localization_launch.py           #3    
          navigation_launch.py             #3
          slam_launch.py                   #3 (optional, up to a param in 1)
      maps/
          turtlebot3_world.pgm             #map
          turtlebot3_world.yaml            #configuration of the map
      params/
          nav2_params.yaml                 #configuration of ALL PARAMS 
      rviz/
          nav2_default_view.rviz           #configuration of RViz2
      urdf/
          turtlebot3_waffle.urdf           #urdf (including declaring Gazebo plugings)
      worlds/
          waffle.model                     #sdf file of the bot in Gazebo
          world_only.model                 #sdf file of the world in Gazebo    
  ```

+ 对于Nav2导航栈的planner、controller等的配置均在nav2_params.yaml内，具体参数配置方式见[NAV2官方文档_Configuration Guide](https://navigation.ros.org/configuration/index.html)

+ 在控制实际机器人时，可以在bringup_4wid_launch.py内使用 IncludeLaunchDescription() 实现。

+ 


