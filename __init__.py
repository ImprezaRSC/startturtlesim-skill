from mycroft import MycroftSkill, intent_file_handler
import subprocess


class Startturtlesim(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

       
        
    @intent_file_handler('startturtlesim.intent')
    def handle_startturtlesim(self, message):
        self.speak_dialog('startturtlesim')
        s="rosrun turtlesim turtlesim_node"    
        subprocess.call([s], shell=True)
def create_skill():
    return Startturtlesim()

