#include <ros/ros.h>

#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib_msgs/GoalStatusArray.h>
#include <actionlib/client/simple_action_client.h>
#include <std_msgs/String.h>
std_msgs::String msgs;
ros::Publisher pub;


void navStatusCallBack(const actionlib_msgs::GoalStatusArray::ConstPtr &status)
{
    int status_id = 0;
    //uint8 PENDING         = 0  
    //uint8 ACTIVE          = 1 
    //uint8 PREEMPTED       = 2
    //uint8 SUCCEEDED       = 3
    //uint8 ABORTED         = 4
    //uint8 REJECTED        = 5
    //uint8 PREEMPTING      = 6
    //uint8 RECALLING       = 7
    //uint8 RECALLED        = 8
    //uint8 LOST            = 9

    if (!status->status_list.empty()){
    actionlib_msgs::GoalStatus goalStatus = status->status_list[0];
    status_id = goalStatus.status;
    }

    if(status_id==1){
    ROS_INFO("active");
    msgs.data ="1";
    pub.publish(msgs);
    }
//   if((status_id==3)||(status_id==0)){
    if((status_id==3)){
    ROS_INFO("reachead");
    msgs.data ="3";
    pub.publish(msgs);
    
    }
    

}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "move_base_goal_state");
    

    ros::NodeHandle nh;
    ros::Subscriber switch_sub;
    // std_msgs::String msgs;
  

    ros::Subscriber move_base_status_sub;
    move_base_status_sub = nh.subscribe<actionlib_msgs::GoalStatusArray>("/move_base/status", 10, &navStatusCallBack);
    
    pub =nh.advertise<std_msgs::String>("/status_led",10);
    // ros::Rate rate(10);
    
    // while (ros::ok()){
    // pub.publish(msgs);
    // rate.sleep();

    //  } 
    ros::spin();
    
    return 0;
}
// add_executable(talker src/stsss.cpp)
// target_link_libraries(talker ${catkin_LIBRARIES})