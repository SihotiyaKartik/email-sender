import threading
import smtplib

from ..kafka_config import consumer
from django.core.management.base import BaseCommand
from confluent_kafka import KafkaError
from django.core.mail import send_mail


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        threads = []

        def consume_and_send_email():

            consumer.subscribe(['bkpzcrni-mail_system'])
            while True:
                msg = consumer.poll(100.0)

                print(msg)

                if msg is None:
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        print(msg.error())
                        break

                recipient = msg.key().decode('utf-8')
                message = msg.value().decode('utf-8')

                # Send the email
                try:
                    send_mail(
                        "TESTING EMAIL",
                        message,
                        None,
                        [recipient],
                        fail_silently=False,
                    )

                except smtplib.SMTPException as e:
                    continue

        for i in range(4):

            thread = threading.Thread(target=consume_and_send_email)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
