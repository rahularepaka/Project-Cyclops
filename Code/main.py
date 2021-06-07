from farmbot import Farmbot, FarmbotToken
import time



fb = Farmbot.login(email="", password="",server="https://my.farm.bot")

#fb = Farmbot(raw_token)

class MyHandler:
    def on_connect(self, bot, mqtt_client):
        request_id2 = bot.send_message("Test 2")
        print("SEND_MESSAGE REQUEST ID: " + request_id2)

        bot.write_pin(7, 1, pin_mode="digital")
        bot.toggle_pin(7)

    def on_change(self, bot, state):
        #print("NEW BOT STATE TREE AVAILABLE:")
        # print(state)
        #print("Current position: (%.2f, %.2f, %.2f)" % bot.position())
        pos = state["location_data"]["position"]
        xyz = (pos["x"], pos["y"], pos["z"])
        #print("Same information as before: " + str(xyz))

    def on_log(self, bot, log):
        print("New message from FarmBot: " + log['message'])

    def on_response(self, bot, response):
        print("ID of successful request: " + response.id)

    def on_error(self, bot, response):
        print("ID of failed request: " + response.id)
        print("Reason(s) for failure: " + str(response.errors))


handler = MyHandler()

fb.connect(handler)
