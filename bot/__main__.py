#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

from pyrogram import Client, Filters
from bot import (
    TG_BOT_TOKEN,
    APP_ID,
    API_HASH,
    LOGGER
)
from bot.commands import Command
from bot.plugins.incoming_message_fn import (
    incoming_start_message_f,
    incoming_compress_message_f,
    incoming_cancel_message_f
)
from bot.plugins.status_message_fn import (
    exec_message_f,
    upload_log_file
)
from bot.plugins.new_join_fn import (
    new_join_f,
    help_message_f
)
from bot.plugins.call_back_button_handler import button

app = Client(
    ":memory:",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=TG_BOT_TOKEN
)


@app.on_message(Filters.command([Command.START]))
async def start(client, message):
    await incoming_start_message_f(client, message)


@app.on_message(Filters.command([Command.COMPRESS]))
async def compress(client, message):
    await incoming_compress_message_f(client, message)


@app.on_message(Filters.command([Command.CANCEL]))
async def cancel(client, message):
    await incoming_cancel_message_f(client, message)


@app.on_message(Filters.command([Command.HELP]))
async def help_command(client, message):
    await help_message_f(client, message)


@app.on_message(Filters.command([Command.EXEC]))
async def exec_command(client, message):
    await exec_message_f(client, message)


@app.on_message(Filters.command([Command.UPLOAD_LOG_FILE]))
async def upload_log(client, message):
    await upload_log_file(client, message)


@app.on_callback_query()
async def cb_handler(client, query):
    await button(client, query)


@app.on_message(Filters.new_chat_members)
async def new_join(client, message):
    await new_join_f(client, message)


if __name__ == "__main__":
    LOGGER.info("Starting the bot...")
    app.run()
