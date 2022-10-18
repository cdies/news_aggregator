https://habr.com/ru/post/689520/

# агрегатор новостей

### Для работы необходимо:

1. Добавить свои значения переменных в файл `config.py`:

> 1.1 Параметры из [my.telegram.org](https://my.telegram.org)
- `api_id = <Твой api_id int>`
- `api_hash = <Твой api_hash str>`

> 1.2 Бот из @BotFather
- `bot_token = <Токен твоего бота str>`

> 1.3 id канала, куда будут сливаться все новости
- `gazp_chat_id = <Id твоего канала c минусом в начале int>`

2. Запустить телеграм парсер `telegram_parser.py`, чтобы пройти аутентификацию в [telethon](https://docs.telethon.dev/en/stable/) и получить свои файлы сессии `bot.session` и `gazp.session`


### Агрегатор по умолчанию парсит новости из:
> телеграм каналы
- [@rbc_news](https://t.me/rbc_news)
- [@gazprom](https://t.me/gazprom)
- [@rian_ru](https://t.me/rian_ru)
- [@prime1](https://t.me/prime1)
- [@interfaxonline](https://t.me/interfaxonline)
- [@markettwits](https://t.me/markettwits)

> RSS каналы
- [www.rbc.ru](https://.rbc.ru)
- [www.ria.ru](https://ria.ru)
- [www.1prime.ru](https://1prime.ru)
- [www.interfax.ru](https://www.interfax.ru)

> новостные сайты
- [www.bcs-express.ru](https://bcs-express.ru)

### Настройка и запуск
Фильтр по умолчанию настроен на газпром, газ и всё с этим связанное (хотя иногда проскакивают и другие новости). 
Добавить/убавить свои каналы или поменять фильтры для новостей можно в файле `main.py`

Каждый парсер написан таким образом, чтобы его можно было запустить отдельно от остальных. 
Это значительно упрощает процесс добавления новых источников, их лучше проверять отдельно, чтобы убедиться в работоспособности. 
Например, feedparser может не прочитать RSS канал и тогда его придется парсить вручную.
- `telegram_parser.py` - парсер телеграм каналов
- `rss_parser.py` - парсер RSS каналов
- `bcs_parser.py` - кастомный парсер сайта [www.bcs-express.ru](https://bcs-express.ru/)
- `main.py` - запускает все парсеры сразу, либо можно запустить в докере через `docker-compose.yml`




<br/><br/>
---
[![](https://habrastorage.org/webt/gz/gc/i6/gzgci6pivvdnk-gmj-kepml5q9y.gif)](https://yoomoney.ru/to/4100117863420642)


