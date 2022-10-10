import random
import asyncio
from collections import deque
import httpx
from scrapy.selector import Selector

from utils import random_user_agent_headers


async def bcs_parser(httpx_client, posted_q, n_test_chars=50, 
                     timeout=2, check_pattern_func=None, 
                     send_message_func=None, logger=None):
    '''Кастомный парсер сайта bcs-express.ru'''
    bcs_link = 'https://bcs-express.ru/category'
    source = 'www.bcs-express.ru'

    while True:
        try:
            response = await httpx_client.get(bcs_link, headers=random_user_agent_headers())
            response.raise_for_status()
        except Exception as e:
            if not (logger is None):
                logger.error(f'{source} error pass\n{e}')

            await asyncio.sleep(timeout*2 + random.uniform(0, 0.5))
            continue

        selector = Selector(text=response.text)

        for row in selector.xpath('//div[@class="feed__list"]/div/div')[::-1]:

            raw_text = row.xpath('*//text()').extract()

            title = raw_text[3] if len(raw_text) > 3 else ''
            summary = raw_text[5] if len(raw_text) > 5 else ''
            if 'ксперт' in summary:  # Эксперт
                title = f'{title}, {summary}'
                summary = raw_text[11] if len(raw_text) > 11 else ''

            news_text = f'{title}\n{summary}'

            if not (check_pattern_func is None):
                if not check_pattern_func(news_text):
                    continue

            head = news_text[:n_test_chars].strip()

            if head in posted_q:
                continue

            raw_link = row.xpath('a/@href').extract()
            link = raw_link[0] if len(raw_link) > 0 else ''
            if 'author' in link:
                link = raw_link[1] if len(raw_link) > 1 else ''

            post = f'<b>{source}</b>\n{source + link}\n{news_text}'

            if send_message_func is None:
                print(post, '\n')
            else:
                await send_message_func(post)

            posted_q.appendleft(head)

        await asyncio.sleep(timeout + random.uniform(0, 0.5))


if __name__ == "__main__":

    # Очередь из уже опубликованных постов, чтобы их не дублировать
    posted_q = deque(maxlen=20)

    httpx_client = httpx.AsyncClient()

    asyncio.run(bcs_parser(httpx_client, posted_q))