# Author: Enrico Mendez
# Date: 13 Febrero 2024
# Description: Node for image capture of the peppers

import rclpy
import os
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np
import time
from ament_index_python.packages import get_package_share_directory



class DataAdquisition(Node):
    def __init__(self):
        super().__init__('Image_capture')
        self.get_logger().info('Image_capture initialized')

        # Create variables
        self.valid_msg = False
        self.img_msg = np.array((720, 1280, 3))
        
        # Define constants
        package_share_directory = get_package_share_directory('size_estimation')
        self.get_logger().info("Directory found: {}".format(package_share_directory))
        self.bridge = CvBridge()
        self.timer_period = 0.5
        self.timer = self.create_timer(self.timer_period, self.image_processing)

        # Create publishers
        
        # Create subscribers
        self.img_sub = self.create_subscription(Image,'/oak/rgb/image_raw', self.img_callback, 10)
        

    def img_callback(self,msg):
        try:
            self.org_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            self.capture_time = time.localtime(time.time())
            self.valid_msg = True
        except:
            self.get_logger().info("Failed to recieved image")
    
    def image_processing(self):
        while not (self.valid_msg): return
        while (True):
            self.get_logger().info("Ready for capture")
            self.get_logger().info("Press enter to capture")
            keyboard_input = input()
            if keyboard_input == '' : self.get_logger().info("Proceding ...")
            print("Capture time:", time.strftime("%H:%M:%S", self.capture_time))
            print("Printing time:", time.strftime("%H:%M:%S", time.localtime(time.time())))
            return
        
            


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
