import discord
import os
from discord import app_commands



#Klasse Button erstellen ohne Timeout damit der knopf nicht ausläuft
class button_view(discord.ui.View):
    def __init__(self,) -> None:
        super().__init__(timeout = None)

    @discord.ui.button(label="Akzeptieren", style = discord.ButtonStyle.green, custom_id="Akzeptieren")
    async def verify(self,interaction:discord.Interaction, button:discord.ui.Button):
        if type(client.role)is not discord.Role:
           client.role = interaction.guild.get_role(1178762589958848542)
        if client.role not in interaction.user.roles:
            await interaction.user.add_roles(client.role)
            await interaction.response.send_message (f"Du wurdest als Drohne in den Schwarm aufgenommen", ephemeral = True)
        else: 
            await interaction.response.send_message (f"...Nagh...was willst du, du bist bereits im Schwarm!", ephemeral = True)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #wird genutzt damit der Bot nicht mehr als 1mal mit Kommandos synchronisiert
        self.role = 1178762589958848542 #Um die Rolle automatisch zu vergeben

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Kontrolliert ob slash Kommandos synchronisiert werden
            await tree.sync(guild = discord.Object(id=1099631623265321092)) #Gildenspezifisch, bei einem Globalen Bot blibt das feld leer
            self.synced = True
        if not self.added:
            self.add_view(button_view())
            self.added = True
            print(f"Nagh was wünscht ihr Meister...")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild=discord.Object(id=1099631623265321092), name = 'welcomebutton', description='Startet den RollenButton') #Gildenspezifisches Slash Kommando
async def button(interaction:discord.Interaction):
    await interaction.response.send_message("Trete ein Drohne...Nagh....", view = button_view())

client.run("")
