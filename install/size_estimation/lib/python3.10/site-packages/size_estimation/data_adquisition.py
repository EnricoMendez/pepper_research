# Author: Enrico Mendez
# Date: 13 Febrero 2024
# Description: Node for image capture of the peppers

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np

class DataAdquisition(Node):
    def __init__(self):
        super().__init__('Image_capture')
        self.get_logger().info('Image_capture initialized')

        # Create variables
        self.valid_msg = False
        self.img_msg = np.array((720, 1280, 3))
        
        # Define constants
        self.bridge = CvBridge()

        # Create publishers
        
        # Create subscribers
        self.img_sub = self.create_subscription(Image,'/oak/rgb/image_raw', self.img_callback, 10)
        

    def img_callback(self,msg):
        try:
            self.org_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            if not (self.valid_msg): self.get_logger().info("Image recieved")
            self.valid_msg = True
        except:
            self.get_logger().info("Failed to recieved image")
    
    def image_processing(self):
        while not (self.valid_msg): continue
        while (True):
            self.get_logger().info("Ready for capture")
            self.get_logger().info("Press enter to capture")
            keyboard_input = input()
            print(keyboard_input)
        
            


def main(args=None):
    # Required lines for any node
    rclpy.init(args=args)
    node = DataAdquisition()
    rclpy.spin(node)
    # Optional but good practices
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
