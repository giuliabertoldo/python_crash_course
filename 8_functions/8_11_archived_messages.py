# 8.4 PASSING A LIST
## EXERCISE 8-11

def send_messages(message_list, sent_messages = []):
    while message_list:
        sent_m = message_list.pop()
        print(f"I am sending {sent_m}.")
        sent_messages.append(sent_m)

    print("Messages to be printed: ")
    for m in message_list:
        print(m)

    print("Printed messages:")
    for s in sent_messages:
        print(s)


messages = ['message1', 'message2','message3']
send_messages(message_list = messages)
print(list(messages))

print('\n')
messages = ['message1', 'message2','message3']
send_messages(message_list = messages[:])
print(list(messages))
