import rospy
from std_msgs.msg import String



rospy.init_node('node1')
volta = 'Aguardando conexao com no 2'

def recebe_volta(msg_volta):
    global volta
    volta = msg_volta.data

def timerCallBack(event):

    print(volta)
    msg = String()
    msg.data = '33735'
    pub.publish(msg)


pub = rospy.Publisher('/topic1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)
sub = rospy.Subscriber('/topic2', String, recebe_volta)

rospy.spin()