from botcity.core import DesktopBot
import sys
import os
import time
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *
sys.platform
'win32'


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id
        # Opens the BotCity website.
        os.startfile(
            "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

        if not self.find("inputLink", matching=0.97, waiting_time=10000):
            self.not_found("inputLink")
        self.click()
        self.paste("https://gshow.globo.com/realities/bbb/bbb22/votacao/paredao-bbb22-vote-para-eliminar-luciano-naiara-azevedo-ou-natalia-269bfafb-9556-4375-b66a-4fbdc9f08396.ghtml")
        self.enter()

        time.sleep(3)

        while True:
            if not self.find("clickVotacao", matching=0.97, waiting_time=10000):
                self.not_found("clickVotacao")
            self.click()

            time.sleep(2)

            if not self.find("clicksouhumano", matching=0.97, waiting_time=10000):
                self.not_found("clicksouhumano")
            self.click()

            time.sleep(2)

            if not self.find("souhumano", matching=0.97, waiting_time=10000):
                self.not_found("souhumano")
            self.click()

            time.sleep(2)

            if not self.find("clickvoltar", matching=0.97, waiting_time=10000):
                self.not_found("clickvoltar")
            self.click()

            time.sleep(2)


# Uncomment to mark this task as finished on BotMaestro
# self.maestro.finish_task(
#     task_id=execution.task_id,
#     status=AutomationTaskFinishStatus.SUCCESS,
#     message="Task Finished OK."
# )


def not_found(self, label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
