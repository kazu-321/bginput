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
        self.pressing=set()
        self.start()

    def on_press(self,key):
        try:
            self.press_key.data=str(key.char)
        except AttributeError:
            self.press_key.data=str(key)[4:]
        
        if self.press_key.data not in self.pressing:
            self.press_pub.publish(self.press_key)
            self.pressing.add(self.press_key.data)

        self.show()

    def on_release(self,key):
        try:
            self.release_key.data=str(key.char)
        except AttributeError:
            self.release_key.data=str(key)[4:]
        
        try:
            self.pressing.remove(self.release_key.data)
        except:
            pass
        self.show()
        self.release_pub.publish(self.release_key)
    
    def start(self):
        print("start listener")
        self.listener=keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()
  
    def show(self):
        print("\033[1A\033[Kpressing:"+",".join(self.pressing))

def main():
    rclpy.init()
    node=kb()
    try:
        rclpy.spin(node)
    except:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()