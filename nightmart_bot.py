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
        profit_percent = round(((purchase.profit / purchase.amount) / int(purchase.item.price)) * 100)

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
            username="Night market"
        )


    def shorten_name(self, name):
        if len(name.split(" ")) > 3:
            return " ".join(part for part in name.split(" ")[:3])
        return name

    def send_statistics(self, data, total):

        profits: set = set([data[val]["total_profit"] for val in data])
        profits = sorted(list(profits), reverse=True)

        top_3 = profits[0], profits[1], profits[2]

        for item in data:
            if data[item]["total_profit"] == profits[0]:
                item_one = self.shorten_name(item)
                item_one_amount = data[item]["total_quantity"]

            elif data[item]["total_profit"] == profits[1]:
                item_two = self.shorten_name(item)
                item_two_amount = data[item]["total_quantity"]

            elif data[item]["total_profit"] == profits[2]:
                item_three = self.shorten_name(item)
                item_three_amount = data[item]["total_quantity"]

        embed = discord.Embed(
            type="rich",
            title=f"Your 30min statistic!",
            color=0xf20707,
            description="Heres your top 3 items:"
        )

        embed.set_thumbnail(url="https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg")

        embed.add_field(name=f"#1 {item_one} with {profits[0]} total profit at {item_one_amount} purchases!", value="\u200b", inline=False)
        embed.add_field(name=f"#2 {item_two} with {profits[1]} total profit at {item_two_amount} purchases!", value="\u200b", inline=False)
        embed.add_field(name=f"#3 {item_three} with {profits[2]} total profit at {item_three_amount} purchases!", value="\u200b", inline=False)
 
        embed.set_footer(text="Night market on top!")
        webhook = discord.Webhook.from_url(
            self.url, adapter=discord.RequestsWebhookAdapter()
        )
        webhook.send(
            avatar_url="https://image-cdn-p.azureedge.net/title-image/tomjone/20220211010113113.jpg",
            embed=embed,
            username="Night market"
        )