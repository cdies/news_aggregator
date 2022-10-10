# аггрегатор новостей

### Для работы необходимо:

1. Добавить свои значения переменных в файл `config.py`:

> 1.1 Параметры из [my.telegram.org](https://my.telegram.org)
- api_id = <Твой api_id int>
- api_hash = <Твой api_hash str>

> 1.2 Бот из @BotFather
- bot_token = <Токен твоего бота str>

> 1.3 id канала, куда будут сливаться все новости
- gazp_chat_id = <Id твоего канала c минсуом в начале int>

2. Запустить телеграм парсер `telegram_parser.py`, чтобы пройти аутентификацию в telethon и получить свои файлы сессии `bot.session` и `gazp.session`


### Аггрегатор по умолчанию парсит новости из:
> телеграм каналы
- [@rbc_news](https://t.me/rbc_news)
- [@gazprom](https://t.me/gazprom)
- [@rian_ru](https://t.me/rian_ru)
- [@prime1](https://t.me/prime1)
- [@interfaxonline](https://t.me/interfaxonline)
- [@markettwits](https://t.me/markettwits)

> RSS каналы
- [www.rbc.ru](https://rssexport.rbc.ru/rbcnews/news/20/full.rss)
- [www.ria.ru](https://ria.ru/export/rss2/archive/index.xml)
- [www.1prime.ru](https://1prime.ru/export/rss2/index.xml)
- [www.interfax.ru](https://www.interfax.ru/rss.asp)

> новостные сайты
- [www.bcs-express.ru](https://bcs-express.ru/)

Фильтр по умолчанию настроен на газпром, газ и всё с этим связанное (хотя иногда проскакивают и другие новости). 
Добавить/убавить свои каналы или поменять фильтры для запроса можно в файле `main.py`





<br/><br/>
---
[![](https://habrastorage.org/webt/gz/gc/i6/gzgci6pivvdnk-gmj-kepml5q9y.gif)](https://yoomoney.ru/to/4100117863420642)


