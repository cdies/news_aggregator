import logging
import sys
import random
import httpx

from user_agents import user_agent_list  # список из значений user-agent


def create_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s \n%(message)s \n' + '-'*30)
    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


async def get_history(client, chat_id, n_test_chars=50, amount_messages=50):
    '''Забирает из канала уже опубликованные посты для того, чтобы их не дублировать'''
    history = []

    messages = await client.get_messages(chat_id, amount_messages)

    for message in messages:
        if message.raw_text is None:
            continue
        post = message.raw_text.split('\n')

        # Выкидывет источник и ссылку из поста, оставляя только текст
        text = '\n'.join(post[2:])

        history.append(text[:n_test_chars].strip())

    return history


def random_user_agent_headers():
    '''Возвращет рандомный user-agent и друге параметры для имитации запроса из браузера'''
    rnd_index = random.randint(0, len(user_agent_list) - 1)

    header = {
        'User-Agent': user_agent_list[rnd_index],
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
    }

    return header


async def send_error_message(text, bot_token, chat_id, logger=None):
    '''Через бот отправляет сообщение напрямую в канал через telegram api'''
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    params = {
        'text': text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
        "disable_notification": False,
        "reply_to_message_id": None,
        "chat_id": str(chat_id)
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=headers)
            response.raise_for_status()
    except Exception as e:
        if logger is None:
            print(e)
        else:
            logger.error(e)

        return -1

    return response.status_code
