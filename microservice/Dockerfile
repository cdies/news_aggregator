FROM python:3.10

RUN apt-get install -yqq --no-install-recommends \
    && pip install 'feedparser==6.0.10' \
    && pip install 'Scrapy==2.6.2' \
    && pip install 'Telethon==1.25.0' \
    && pip install 'telethon-cryptg==0.0.4' \
    && pip install 'httpx==0.23.0'

WORKDIR /app

ADD main.py main.py
ADD utils.py utils.py
ADD config.py config.py
ADD user_agents.py user_agents.py
ADD telegram_parser.py telegram_parser.py
ADD rss_parser.py rss_parser.py
ADD bcs_parser.py bcs_parser.py

ADD bot.session bot.session
ADD gazp.session gazp.session