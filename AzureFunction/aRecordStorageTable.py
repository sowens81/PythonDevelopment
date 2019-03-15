from azure.storage.queue import QueueService

quename = "mytestqueue"
message = [u"Hello, World!", u"Hello, House!", u"Hello, God!"]
accountname = "sotagteststhg1"
accountkey = "Kfxhs6UnwVjqkI6u4ZatbB0kgOaYuVkcGCgiW9N9J7PygAblk63rB0KV28jqo/5TIJ30cxWmxhfy9F2wlmIFHg=="

queue_service = QueueService(account_name=accountname, account_key=accountkey)

queue_service.create_queue(quename)

for x in message:
    queue_service.put_message(quename,x)
    messages = queue_service.peek_messages(quename)
    for message in messages:
        print(message.content)

metadata = queue_service.get_queue_metadata(quename)
count = metadata.approximate_message_count
print(count)

