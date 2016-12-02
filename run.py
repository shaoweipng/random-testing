import turibolt as bolt
import time
import random

# This package was made available by installing it in the setup command:
import names

# The turibolt API lets you retrieve values from the config file
#random.seed(bolt.get_current_config()['parameters']['random_seed'])

# status messages will show in the task details at runtime (CLI and Web UI)
#bolt.set_status_message("Starting")

messages = []

for i in range(1, 20):
    time.sleep(5)
    message = "SWtesting Iteration %s" % str(i)
    #bolt.set_status_message(message)
    print(message)
    messages.append(message)

    # demonstrate the reporting of different types of metrics:
    #bolt.send_metrics({
    #    'Progress': i,
    #    'Random Accuracy': random.random(),
    #    'List Value': [random.random() for i in range(i)],
    #    'Progress Text': message,
    #    'Accumulated Progress Text': messages,
    #    'A Random Name': str(names.get_full_name())
    #})

#bolt.set_status_message('Done')
print("I am done!!! Remote Branch on git")
