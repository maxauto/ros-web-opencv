#!/usr/bin/env python
from __future__ import print_function

import numpy as np
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_publisher:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic",Image)

    self.bridge = CvBridge()

  def publish(self,data):
    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(data, "bgr8"))
    except CvBridgeError as e:
      print(e)


def main(args):
  ip = image_publisher()
  rospy.init_node('image_publisher', anonymous=True)
  

  try:
    cap = cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret == True:
            rospy.loginfo('publishing video frame')
            ip.publish(frame)
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cap.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)


# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
