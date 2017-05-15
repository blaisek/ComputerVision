
#include "opencv2/opencv.hpp"
#include <iostream>
using namespace cv;
using namespace std;
int main(int, char**) {

    VideoCapture vcap;
    Mat image;

    // This works on a D-Link  DCS-2136L 
    const string videoStreamAddress = "http://admin:cam6353@10.10.7.205/video2.mjpg";

    //open the video stream and make sure it's opened

    if(!vcap.open(videoStreamAddress)) {
        cout << "Error opening video stream or file" << std::endl;
        return -1;
    }
	
 	
    

        if(!vcap.read(image)) {
            std::cout << "No frame" << std::endl;
            
        }
	
		
		
for(;;) {
	
	
        
    		imshow("Output Window", image);
		vcap.read(image);
		cv::waitKey(10);
	

    }   
}
