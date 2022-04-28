import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import os

bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print('Start')
@bot.command()
async def setup(ctx):
    # imsa = Button(label="Imsa Race",style=discord.ButtonStyle.gray,custom_id='imsa')
    # vrs = Button(label="VRS Sprint Race", style=discord.ButtonStyle.gray,custom_id='vrs')
    select_series = Select(
        placeholder='Выбери гоночную серию',
        options=[
            discord.SelectOption(label='VRS', description='VRS_Sprint', value='vrs'),
            discord.SelectOption(label='IMSA', description='IMSA_Sprint', value='imsa'),
            discord.SelectOption(label='VRS_E', description='VRS_Endurance', value='vrs_e'),
            discord.SelectOption(label='IMSA_E', description='IMSA_Endurance', value='imsa_e')
            ]
    )      
    select_week = Select(
        placeholder='Выбери неделю',
        options=[
            discord.SelectOption(label='Week_1', description="Первая неделя", value='week1'),
            discord.SelectOption(label='Week_2', description="Вторая неделя", value='week2'),
            discord.SelectOption(label='Week_3', description="Третья неделя", value='week3'),
            discord.SelectOption(label='Week_4', description="Четвертая неделя", value='week4'),
            discord.SelectOption(label='Week_5', description="Пятая неделя", value='week5'),
            discord.SelectOption(label='Week_6', description="Шестая неделя", value='week6'),
            discord.SelectOption(label='Week_7', description="Седьмая неделя", value='week7'),
            discord.SelectOption(label='Week_8', description="Восьмая неделя", value='week8'),
            discord.SelectOption(label='Week_9', description="Девятая неделя", value='week9'),
            discord.SelectOption(label='Week_10', description="Десятая неделя", value='week10'),
            discord.SelectOption(label='Week_11', description="Одиннадцатая неделя", value='week11'),
            discord.SelectOption(label='Week_12', description="Двенадцатая неделя", value='week12'),
            ]
        )
    select_car = Select(
        placeholder='Автомобиль',
        options=[
            discord.SelectOption(label='Audi', description="Audir8gt3", value='audi'),
            discord.SelectOption(label='BMW', description="BMW4gt3", value='bmw'),
            discord.SelectOption(label='Ferrari', description="Ferrarievogt3", value='ferr'),
            discord.SelectOption(label='Lamborghini', description="Lamborghinievogt3", value='lambo'),
            discord.SelectOption(label='MaLaren', description="MaLarenmp4", value='mclaren'),
            discord.SelectOption(label='Mercedes', description="Mercedesamggt3", value='merc'),
            discord.SelectOption(label='Porsche911R', description="Porsche911rgt3", value='911rgt3'),
            discord.SelectOption(label='Ford', description="Fordgt gt3", value='ford'),
            discord.SelectOption(label='DallaraP217', description="DallaraP217", value='P217')
            ]
        )
    view = View()
    view.add_item(select_series)
    view.add_item(select_week)
    view.add_item(select_car)
    await ctx.send('Выбери Гоночную серию', view=view)
    async def result_callback(interaction):
        await interaction.response.send_message(f'Результат выбора, {select_series.values[0], select_week.values[0], select_car.values[0]}') , print({select_series.values[0], select_week.values[0], select_car.values[0]})
    select_car.callback = result_callback















bot.run("")