import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):

    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher_ = self.create_publisher(String, 'demo_topic', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Test msg'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    simple_publisher = SimplePublisher()
    try:
        rclpy.spin(simple_publisher)
    finally:
        simple_publisher.destroy_node()
        print("rclpy.shutdown")
        rclpy.shutdown()


if __name__ == '__main__':
    main()
