# Author: Enrico Mendez
# Date: 20 Febrero 2024
# Description: Server for the image processing


import time
from sensor_msgs.msg import Image
from interfaces.srv import ImageProcessing
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
import cv2
import numpy as np

class ImageServer(Node):
    def __init__(self):
        super().__init__('Image_process')
        self.get_logger().info('Image_process service initialized')

        # Create variables
        self.org_img = np.array((720, 1280, 3))
        self.valid_img = False
        
        # Define constants
        self.bridge = CvBridge()

        # Create suscriber 
        self.oak_sub = self.create_subscription(Image,'/oak/rgb/image_raw', self.oak_callback, 10)
        self.depth_sub = self.create_subscription(Image,'/oak/', self.depth_callback, 10)
        
        # Create server
        self.srv = self.create_service(ImageProcessing, 'image_processing_service', self.image_process)
        
    def oak_callback(self,msg):
        self.org_img = self.bridge.imgmsg_to_cv2(msg,desired_encoding="bgr8")
        print(self.org_img.shape)
        self.get_logger().info("Image recieved")
        self.capture_time = time.localtime(time.time())
        self.valid_img = True

    def image_process(self, request, response):
        if not self.valid_img: return
        segmented_img = self.segmentation(self.org_img)
        distance = self.distance_calc(segmented_img)
        return response
    def segmentation(self,src):
        return 
    def distance_calc(self,src):
        pass

        
def main(args=None):

    rclpy.init(args=args)

    node = ImageServer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()