from collections import deque

messages = deque()


def process_message(message):
    pass


while True:
    if messages:
        message = messages.pop()
        process_message(message)


# pseudkod zadania z kolejki zdarzeń
def cpu_bound_setup():
    pass


def io_bound_setup():
    pass


def make_request():
    cpu_bound_setup()
    io_bound_setup()
    cpu_bound_setup()


task_one = make_request()
task_two = make_request()
task_three = make_request()
