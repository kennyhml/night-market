from threading import Thread
import discord


class Discord:
    def __init__(self) -> None:
        self.url = "https://discord.com/api/webhooks/991429513340780626/Hm4wv4-7G9XJaBiIiAN28mU5d79mG9vSmdsj5luutodvRetwJdOD7Z_fFJzB1tg6W3_m"
        self.avatar = "https://lostarkcodex.com/icons/use_9_242.webp"
        self.webhook = discord.Webhook.from_url(
            self.url, adapter=discord.RequestsWebhookAdapter()
        )

    def send_message(self, message):
        self.webhook.send(
            content=message, avatar_url=self.avatar, username="Night market"
        )

    def send_image(self, image, message):

        file = discord.File(image, filename="image.png")

        Thread(
            target=lambda: self.webhook.send(
                content=message,
                avatar_url=self.avatar,
                file=file,
                username="Night market",
            ),
            name="Posting to discord!",
        ).start()

    def send_purchase_embed(self, purchase, inventory):
        embed = discord.Embed(
            type="rich",
            title=f"Purchased {purchase.item.name}!",
            color=0x9807F2,
        )

        file = discord.File(f"images/items/{purchase.image}.png", filename="image.png")
        taken, total = inventory.slots_taken, inventory.total_slots
        profit_percent = round(
            ((purchase.profit / purchase.amount) / int(purchase.item.price)) * 100
        )

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
        webhook = discord.Webhook.from_url(
            self.url, adapter=discord.RequestsWebhookAdapter()
        )
        webhook.send(
            file=file,
            avatar_url="https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg",
            embed=embed,
            username="Night market",
        )

    def shorten_name(self, name):
        if len(name.split(" ")) > 4:
            return " ".join(part for part in name.split(" ")[:4])
        return name

    def send_statistics(self, data):

        print("Data:", data)

        embed = discord.Embed(
            type="rich",
            title=f"The inventory has been emptied!",
            color=0xF20707,
            description=f"The inventory has been emptied, here's your stats!\nㅤ",
        )

        embed.set_thumbnail(
            url="https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg"
        )

        embed.add_field(
            name=f"Emptying profit:ㅤㅤ",
            value=f"{data['total_profit']:_}".replace("_", " ") + " ₽"
            if not data["emptying_profit"]
            else f"{data['emptying_profit']:_}".replace("_", " ") + " ₽",
        )

        embed.add_field(
            name=f"Total profit:",
            value=f"{data['total_profit']:_}".replace("_", " ") + " ₽",
        )
        embed.add_field(
            name=f"Current money:",
            value=f"{data['current_money']:_}".replace("_", " ") + " ₽",
        )

        embed.add_field(name=f"Time taken:ㅤㅤ", value=data["empty_time"])
        embed.add_field(name=f"Session time:ㅤㅤ", value=data["session_time"])
        embed.add_field(name=f"Real money value:ㅤㅤ", value=f'{data["profit_in_euro"]}\nㅤ')

        embed.add_field(name=f"Item #1ㅤㅤ", value=data["top_items"][0]["name"])
        embed.add_field(
            name=f"Total profit:ㅤㅤ",
            value=f'{data["top_items"][0]["profit"]:_}'.replace("_", " ") + " ₽",
        )
        embed.add_field(
            name=f"Total purchases:", value=data["top_items"][0]["quantity"]
        )

        embed.add_field(name=f"Item #2ㅤㅤ", value=data["top_items"][1]["name"])
        embed.add_field(
            name=f"Total profit:ㅤㅤ",
            value=f'{data["top_items"][1]["profit"]:_}'.replace("_", " ") + " ₽",
        )
        embed.add_field(
            name=f"Total purchases:", value=data["top_items"][0]["quantity"]
        )

        embed.add_field(name=f"Item #3ㅤㅤ", value=data["top_items"][2]["name"])
        embed.add_field(
            name=f"Total profit:ㅤㅤ",
            value=f'{data["top_items"][2]["profit"]:_}'.replace("_", " ") + " ₽",
        )
        embed.add_field(
            name=f"Total purchases:", value=data["top_items"][0]["quantity"]
        )

        embed.set_footer(text="Night market on top!")

        webhook = discord.Webhook.from_url(
            self.url, adapter=discord.RequestsWebhookAdapter()
        )
        webhook.send(
            avatar_url="https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg",
            embed=embed,
            username="Night market",
        )
