import sys,rclpy
from pynput import keyboard
from rclpy.node import Node
from std_msgs.msg import String

class kb(Node):
    def __init__(self):
        super().__init__("bginput")
        self.press_pub=self.create_publisher(String,"on_press",10)
        self.release_pub=self.create_publisher(String,"on_release",10)
        self.press_key=String()
        self.release_key=String()
        self.start()

    def on_press(self,key):
        try:
            self.press_key.data=key.char
        except AttributeError:
            self.press_key.data=str(key)[4:]
        print("press   :"+self.release_key.data)
        self.press_pub.publish(self.press_key)

    def on_release(self,key):
        try:
            self.release_key.data=key.char
        except AttributeError:
            self.release_key.data=str(key)[4:]
        print("release :"+self.release_key.data)
        self.release_pub.publish(self.release_key)
    
    def start(self):
        self.listener=keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()

def main():
    rclpy.init()
    node=kb()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
            
