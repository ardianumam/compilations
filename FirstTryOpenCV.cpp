#include "stdafx.h"//header for Visual Studio
#include <opencv2/core/core.hpp>//header for OpenCV core
#include <opencv2/highgui/highgui.hpp>//header for OpenCV UI
#include <iostream>//header for c++ IO
 
//set opencv and c++ namespaces
using namespace cv;
using namespace std;
 
int main()
{
	Mat image;//create mat variable for our image
	image = imread("lena.jpg", 1); // read image.  1 : read as rgb, 0 : read as grayscale image
	 
	if (!image.data) // check whether the image is found or not
	{
	cout << "Image is not found. Please write the file name and path location correctly." << endl;
	}
	 
	namedWindow("lena", WINDOW_AUTOSIZE);// create window for showing our image
	imshow("lena", image);// showing our image
	waitKey(0);// imshow will show image once the program hit this "waitKey".
	return 0;
}