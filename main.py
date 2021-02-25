from bot import Bot
from commands import Encender, Hablar, Apagar, Dormir

encender = Encender()
hablar = Hablar()
apagar = Apagar()
dormir = Dormir()

object_bot = Bot(encender)
object_bot.execute_command()
object_bot.set_comand(hablar)
object_bot.execute_command()
object_bot.set_comand(apagar)
object_bot.execute_command()
object_bot.set_comand(dormir)
object_bot.execute_command()
