#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
import cv2


class CameraViewerNode(Node):
    def __init__(self):
        super().__init__('camera_viewer_node')

        self.cv_bridge = CvBridge()
        self.window_width = 640  # Largura da janela
        self.window_height = 480  # Altura da janela

        # Subscribers
        self.camera1_image_sub = self.create_subscription(
            Image, '/camera1_sensor/image_raw', self.camera1_callback, 10)
        self.camera2_image_sub = self.create_subscription(
            Image, '/camera2_sensor/image_raw', self.camera2_callback, 10)
        self.camera3_image_sub = self.create_subscription(
            Image, '/camera3_sensor/image_raw', self.camera3_callback, 10)
        self.camera4_image_sub = self.create_subscription(
            Image, '/camera4_sensor/image_raw', self.camera4_callback, 10)

    def resize_image(self, image):
        return cv2.resize(image, (self.window_width, self.window_height))

    def create_window(self, window_name):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, self.window_width, self.window_height)

    def camera1_callback(self, msg):
        image = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        resized_image = self.resize_image(image)
        self.create_window('Camera 1')
        cv2.imshow('Camera 1', resized_image)
        cv2.waitKey(1)

    def camera2_callback(self, msg):
        image = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        resized_image = self.resize_image(image)
        self.create_window('Camera 2')
        cv2.imshow('Camera 2', resized_image)
        cv2.waitKey(1)

    def camera3_callback(self, msg):
        image = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        resized_image = self.resize_image(image)
        self.create_window('Camera 3')
        cv2.imshow('Camera 3', resized_image)
        cv2.waitKey(1)

    def camera4_callback(self, msg):
        image = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        resized_image = self.resize_image(image)
        self.create_window('Camera 4')
        cv2.imshow('Camera 4', resized_image)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    camera_viewer_node = CameraViewerNode()
    rclpy.spin(camera_viewer_node)
    camera_viewer_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

