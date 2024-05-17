from collections import deque
import typer
import rclpy
from rclpy.node import Node
from InquirerPy.resolver import prompt
from geometry_msgs.msg import Twist, Vector3
from turtlesim.msg import Pose
from math import radians
import time

app = typer.Typer()

prompt_list = deque()

class CLIInterface:
    def __init__(self):
        self.publisher_ = None
        self.prompt_publisher_ = None

    def set_publishers(self, publisher, prompt_publisher):
        self.publisher_ = publisher
        self.prompt_publisher_ = prompt_publisher

    def send_command(self, command):
        msg = Twist()
        msg.linear.x, msg.linear.y, msg.angular.z, duration = map(float, command.split(','))
        msg.linear.x = float(msg.linear.x)
        msg.linear.y = float(msg.linear.y)
        msg.angular.z = float(msg.angular.z)
        duration = float(duration)
        self.publisher_.publish(msg)
        time.sleep(duration)
        self.stop()

    def stop(self):
        stop_msg = Twist()
        self.publisher_.publish(stop_msg)

def show(interface):
    questions = [
        {
            "type": "input",
            "name": "action",
            "message": "Digite o seu input na seguinte ordem: [vx (velocidade x), vy (velocidade em y), vtheta (velocidade angular), tempo_em_segundos]",
        }
    ]
    prompt_response = prompt(questions)["action"]
    prompt_list.append(prompt_response)
    interface.send_command(prompt_response)

def main():
    rclpy.init()

    node = rclpy.create_node('turtle_controller')

    turtle_publisher = node.create_publisher(Twist, 'cmd_vel', 10)
    prompt_publisher = node.create_publisher(Twist, 'prompt_vel', 10)

    interface = CLIInterface()
    interface.set_publishers(turtle_publisher, prompt_publisher)

    while rclpy.ok():
        show(interface)
        print("Lista de prompts:", prompt_list)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
