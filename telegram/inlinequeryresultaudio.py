#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2016
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

"""This module contains the classes that represent Telegram
InlineQueryResultAudio"""

from telegram import InlineQueryResult
from telegram.utils.validate import validate_string


class InlineQueryResultAudio(InlineQueryResult):
    def __init__(self,
                 id,
                 audio_url,
                 title,
                 performer=None,
                 audio_duration=None,
                 reply_markup=None,
                 input_message_content=None):

        # Required
        super(InlineQueryResultAudio, self).__init__('audio', id)
        self.audio_url = audio_url
        self.title = title

        # Optional
        self.performer = performer
        self.audio_duration = audio_duration
        if reply_markup is not None:
            self.reply_markup = 'ReplyMarkup'  # TODO
        if input_message_content is not None:
            self.input_message_content = 'InputMessageContent'