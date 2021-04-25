# 3ch
3ch - это плагиат всеми известного анонимного форума 2ch, в котром каждая запись имеет уникальный номер.

В проекте реализовано следующее:
1. Возможность оставлять треды
2. Возможность отвечать на треды

# Использованные технологии
Flask для веб-сервера

SQLAlchemy для работы с базой данных

WTForms для создания тредов и ответов
# Архитектура
app.py - основной фалй сервера, где обрабатываются все запросы

data - файл с классами программы и вспомогательными файлами

db - база данных

forms - хранит формы создания тредов и ответов

static/images - хранит фотографии загруженные анонами на сервер

static/css - тут лежит стиль сайта

templates - html страницы
