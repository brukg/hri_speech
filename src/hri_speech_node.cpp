// 
#include "hri_speech/hri_speech.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "hri_speech_node");
    ros::NodeHandle nh;
    std::string sampling_param;
	// Load sampling type from parameter server
	// if (n.getParam("/sampling_type", sampling_param))
	// 	std::cout<<"Sampling type:="<<sampling_param<<std::endl;
	
    // planner planner_object(n);
    std::string xml_filename;
    nh.param<std::string>("file", xml_filename, ros::package::getPath("hri_speech") +"/params/bt_test.xml");
    ROS_INFO("Loading XML : %s", xml_filename.c_str());
    BehaviorTreeFactory factory;

    // factory.registerNodeType<MoveBase>("MoveBase");

    auto tree = factory.createTreeFromFile(xml_filename);


    ros::spin();
    return 0;
}