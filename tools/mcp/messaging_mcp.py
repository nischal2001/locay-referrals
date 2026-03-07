class MessagingMCP:

    @staticmethod
    def send_messages(candidates, message):

        sent_to = []

        for r in candidates:

            candidate = r["candidate"]

            name = candidate["name"]
            role = candidate["role"]
            company = candidate["company"]

            # Simulate sending message
            print(f"\nSending message to {name} ({role} at {company})")
            print("Message:", message)

            sent_to.append(name)

        return sent_to