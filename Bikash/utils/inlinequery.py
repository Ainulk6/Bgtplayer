from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="⏸️ 𝐏𝐚𝐮𝐬𝐞 ⏸️",
            description=f"𝐏𝐚𝐮𝐬𝐞 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐮𝐬𝐢𝐜.",
            thumb_url="https://i.ibb.co/DGyhVrR/Picsart-24-02-19-20-29-56-185.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="⏹️ 𝐑𝐞𝐬𝐮𝐦𝐞 ⏹️",
            description=f"𝐑𝐞𝐬𝐮𝐦𝐞 𝐓𝐡𝐞 𝐏𝐚𝐮𝐬𝐞𝐝 𝐌𝐮𝐬𝐢𝐜.",
            thumb_url="https://i.ibb.co/bPm7ZJj/Picsart-24-02-19-20-31-59-744.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="⏩ 𝐒𝐤𝐢𝐩 ⏩",
            description=f"𝐒𝐤𝐢𝐩 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐮𝐬𝐢𝐜 & 𝐏𝐥𝐚𝐲 𝐍𝐞𝐱𝐭 𝐌𝐮𝐬𝐢𝐜",
            thumb_url="https://i.ibb.co/88pPs8t/Picsart-24-02-19-20-33-49-254.png",
            input_message_content=InputTextMessageContent("/skip", "/next"),
        ),
        InlineQueryResultArticle(
            title="📴 𝐄𝐧𝐝 📴",
            description="𝐄𝐧𝐝 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜.",
            thumb_url="https://i.ibb.co/T46qqZn/Picsart-24-02-19-20-34-42-681.png",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🔉 𝐒𝐡𝐮𝐟𝐟𝐥𝐞 🔉",
            description="𝐒𝐡𝐮𝐟𝐟𝐥𝐞 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐮𝐢𝐜.",
            thumb_url="https://i.ibb.co/S6VTk8g/Picsart-24-02-19-20-35-40-928.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🔈 𝐋𝐨𝐨𝐩 🔈",
            description="𝐋𝐨𝐨𝐩 𝐓𝐡𝐞 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 .",
            thumb_url="https://i.ibb.co/Stc24hy/Picsart-24-02-19-20-36-25-287.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
