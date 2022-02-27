from .bot import bot
from .state import (
    START_REPORTING
)
from .handlers import (
    start_handler,
    start_reporting_handler
)

from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    Dispatcher,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
    PicklePersistence,
)

dispatcher = Dispatcher(
    bot,
    workers=0,
    update_queue=None,
    persistence=PicklePersistence("bot/state"),
)

# Handle start command

start_command_handler = CommandHandler("start", start_handler)

dispatcher.add_handler(
    ConversationHandler(
        name="main",
        persistent=True,
        entry_points=[CommandHandler("start", start_handler)],
        states={
            START_REPORTING: [MessageHandler(filters=Filters.text, callback=start_reporting_handler)]
        },
        fallbacks=[CommandHandler("start", start_handler)],
    )
)
