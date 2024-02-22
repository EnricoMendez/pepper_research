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
        self.valid_depth = False 
        
        # Define constants
        self.bridge = CvBridge()

        # Create suscriber 
        self.camera_sub = self.create_subscription(Image,'camera/camera/color/image_raw', self.cam_callback, 10)
        self.depth_sub = self.create_subscription(Image,'/camera/camera/aligned_depth_to_color/image_raw', self.depth_callback, 10)
        # Create server
        self.srv = self.create_service(ImageProcessing, 'image_processing_service', self.image_process)
        
    def cam_callback(self,msg):
        self.org_img = self.bridge.imgmsg_to_cv2(msg)
        self.get_logger().info("Image recieved")
        self.capture_time = time.localtime(time.time())
        self.valid_img = True

    def depth_callback(self, msg):
        self.org_img = self.bridge.imgmsg_to_cv2(msg)
        self.get_logger().info("Image recieved")
        self.depth_capture_time = time.localtime(time.time())
        self.valid_depth = True   

    def image_process(self, request, response):
        while not self.valid_img & self.valid_depth: 
            response.data = 'Image is not avilable' 
            return response
        self.get_logger().info("Message recived")
        id = request.id
        segmented_img = self.segmentation(self.org_img)
        distance = self.distance_calc(segmented_img)
        response.data = 'The id is {}'.format(id)
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