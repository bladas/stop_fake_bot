import requests
import random

starts = ["Hello", "Dear support", "Greetings", "Dear colleagues", "Needs investigation", "Please help",
          "Channel report", "Report ticket", "Guys, please help"]

subjects = ["The channel {} content is", "This channel {} contains", "In the channel {} there are lots of posts with",
            "The following channel {} indicates"]

actions = ["breaking of the integrity", "terrorism", "spreading of fake news", "misleading people and oman",
           "anti ukrainian propaganda", "violent scenes", "populating nacism", "spreading war propaganda",
           "assisting occupant troops", "photos of the dead", "pictures of the blood",
           "weapons and violence images"]

ends = ["Look forward to hearing from you", "Please help to stop the war",
        "Please investigate this and take appropriate actions", "Please review this asap",
        "Will be waiting for your reply"]


def generate_report_msg(url: str) -> str:
    start = random.choice(starts)
    subject = random.choice(subjects).format(url)
    action = random.choice(actions)
    end = random.choice(ends)

    msg = f"{start}! {subject} {action}. {end}."

    return msg


def send_report_task(url: str) -> None:
    data = {
        'text': generate_report_msg(url)
    }
