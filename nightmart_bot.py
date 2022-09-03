
from threading import Thread
import discord
import json

class Discord:
    """Discord handle to send purchases and statistics
    ------------------------------
    Connects to the user given webhook and posts purchases
    and statistics or errors.

    Uses discord 1.7.3
    """

    def __init__(self) -> None:
        with open("data/settings.json") as f:
            self.data = json.load(f)
        if not self.data["post_discord"]:
            return
        self.url = "https://discord.com/api/webhooks/1012067077512761374/Z5iQrJVYJ65zCH-CGTrBhGEnjCBjj5pp2JIOdvwpD9wacxqZzZtfkXlhSFi_fmKls-OU"
        self.avatar = "https://lostarkcodex.com/icons/use_9_242.webp"
        self.webhook = discord.Webhook.from_url(
            self.url, adapter=discord.RequestsWebhookAdapter()
        )

    def send_message(self, message):
        """Sends the given message to discord"""
        if not self.data["post_discord"]:
            return
        try:
            self.webhook.send(
                content=message, avatar_url=self.avatar, username="Night market"
            )
        except Exception as e:
            print(f"Failed to send message to discord!\n{e}")

    def send_image_to_disc(self, image, message):
        """Sends an image and a message to discord"""
        try:
            file = discord.File(image, filename="image.png")
            self.webhook.send(
                content=message,
                avatar_url=self.avatar,
                file=file,
                username="Night market",
            )
        except Exception as e:
            print(f"Failed to send message to discord!\n{e}")

    def send_image(self, image, message):
        """Starts an image posting thread"""
        if not self.data["post_discord"]:
            return
        Thread(
            target=lambda: self.send_image_to_disc(image, message),
            name="Posting to discord!",
        ).start()

    def send_captcha(self, target, time):
        embed = discord.Embed(
            type="rich",
            title=f"Solved a captcha!",
            color=0x9807F2,
        )

        file = discord.File(f"images/temp/captcha.png", filename="image.png")
        embed.add_field(name="Target item:", value=target)
        embed.add_field(name="Time taken:", value=f"{time}s")
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text="Night market on top!")
        try:
            # post the embed
            self.webhook.send(
                file=file,
                avatar_url="https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg",
                embed=embed,
                username="Night market",
            )
        except Exception as e:
            print(f"Failed to post to discord!\n{e}")
            
    def send_purchase_embed(self, purchase, inventory):
        """Sends a purchase to discord"""
        if not self.data["post_discord"]:
            return
        # create the embed
        embed = discord.Embed(
            type="rich",
            title=f"Purchased {purchase.item.name}!",
            color=0x9807F2,
        )
        try:
            # read the items image into the embed
            img = purchase.image.replace('"', "")
            file = discord.File(f"images/items/{img}.png", filename="image.png")

            # get inventory slots and profit in percent
            taken, total = inventory.slots_taken, inventory.max_slots
            profit_percent = round(
                ((purchase.profit / purchase.amount) / int(purchase.item.price)) * 100
            )

            # create the embed with the data
            embed.set_thumbnail(url="attachment://image.png")
            embed.add_field(name="Bought for:ㅤㅤㅤ", value=f"{purchase.bought_at} ₽")
            embed.add_field(name="Item value:ㅤㅤㅤ", value=f"{purchase.item.price} ₽")
            embed.add_field(name="\u200b", value="\u200b")
            embed.add_field(name="Quantity:ㅤㅤㅤ", value=f"{purchase.amount}")
            embed.add_field(name="Profit made:ㅤㅤㅤ", value=f"{purchase.profit} ₽")
            embed.add_field(name="\u200b", value="\u200b")
            embed.add_field(name="Inventory:ㅤㅤㅤ", value=f"{taken}/{total}")
            embed.add_field(name="Profit in %:ㅤㅤㅤ", value=f"{profit_percent} %")
            embed.add_field(name="\u200b", value="\u200b")

            embed.set_footer(text="Night market on top!")

            # post the embed
            self.webhook.send(
                file=file,
                avatar_url="https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg",
                embed=embed,
                username="Night market",
            )
        except Exception as e:
            print(f"Failed to post to discord!\n{e}")

    def shorten_name(self, name):
        """Shortens a name down"""
        if len(name.split(" ")) > 4:
            return " ".join(part for part in name.split(" ")[:4])
        return name

    def send_statistics(self, data):
        if not self.data["post_discord"]:
            return
        """Sends a statistics embed to discord after emptying the inventory"""
        # create the embed
        embed = discord.Embed(
            type="rich",
            title=f"The inventory has been emptied!",
            color=0xF20707,
            description=f"The inventory has been emptied, here's your stats!\nㅤ",
        )

        # format the both ways of calculating profit and add them together
        profit_diff = f"{data['total_profit'][0]:_}".replace("_", " ")
        profit_items = f"{data['total_profit'][1]:_}".replace("_", " ")
        total_profit = f"{profit_items} ({profit_diff}) ₽"

        hourly_rate = f"{data['hourly_profit']:_}".replace("_", " ") + " ₽"
        current_money = f"{data['current_money']:_}".replace("_", " ") + " ₽"

        # set thumbnail
        rub_image = "https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg"
        embed.set_thumbnail(url=rub_image)
        embed.set_footer(text="Night market!")

        # set main statistics
        embed.add_field(name=f"Profit per hour:ㅤㅤ", value=hourly_rate)
        embed.add_field(name=f"Total profit:", value=total_profit)
        embed.add_field(name=f"Current money:", value=current_money)

        embed.add_field(name=f"Time taken:ㅤㅤ", value=data["empty_time"])
        embed.add_field(name=f"Session time:ㅤㅤ", value=data["session_time"])
        embed.add_field(name=f"RMT value:ㅤㅤ", value=f'{data["profit_in_euro"]}' + "\nㅤ")

        try:
            # set the top 3 items
            profit_1 = f'{data["top_items"][0]["profit"]:_}'.replace("_", " ") + " ₽"
            quantity_1 = data["top_items"][0]["quantity"]

            profit_2 = f'{data["top_items"][1]["profit"]:_}'.replace("_", " ") + " ₽"
            quantity_2 = data["top_items"][1]["quantity"]

            profit_3 = f'{data["top_items"][2]["profit"]:_}'.replace("_", " ") + " ₽"
            quantity_3 = data["top_items"][2]["quantity"]

            embed.add_field(name=f"Item #1ㅤㅤ", value=data["top_items"][0]["name"])
            embed.add_field(name=f"Total profit:ㅤㅤ", value=profit_1)
            embed.add_field(name=f"Total purchases:", value=quantity_1)

            embed.add_field(name=f"Item #2ㅤㅤ", value=data["top_items"][1]["name"])
            embed.add_field(name=f"Total profit:ㅤㅤ", value=profit_2)
            embed.add_field(name=f"Total purchases:", value=quantity_2)

            embed.add_field(name=f"Item #3ㅤㅤ", value=data["top_items"][2]["name"])
            embed.add_field(name=f"Total profit:ㅤㅤ", value=profit_3)
            embed.add_field(name=f"Total purchases:", value=quantity_3)

        except Exception as e:
            print(f"Failed to set top 3 items!\n{e}")

        # send the embed
        self.webhook.send(
            avatar_url="https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg",
            embed=embed,
            username="Night market",
        )
