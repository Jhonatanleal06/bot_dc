import discord
import random
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def bot():

    @client.event
    async def on_ready():
        print(f'Hemos iniciado sesión como {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send("Hi!")
        elif message.content.startswith('$bye'):
            await message.channel.send("\U0001f642")
        elif message.content.startswith("$password"):
            caracteres = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
            longitud = 10
            contraseña = ""
            for i in range(longitud):
                contraseña += random.choice(caracteres)
            await message.channel.send(contraseña)
            
        else:
            await message.channel.send(message.content)
            

    client.run("MTM2MDM1NjgyMzcyNjU1NT22IyNg.GjsnGz.rStoF0xZglmwnGN4OWk0A4EKmLIuPMDkQq8IIs")


bot()
