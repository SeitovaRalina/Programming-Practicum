# Л/Р № 2. Тестирование API с использованием Postman
Эта ветка содержит файл по автоматическому тестированию [Restful-Booker](https://restful-booker.herokuapp.com/).

Данный сайт часто используется в учебных целях для изучения работы с RESTful API, включая методы HTTP (GET, POST, PUT, DELETE) и работу с JSON-данными. Он предоставляет функциональность для бронирования номеров в отеле, что позволяет создавать, просматривать, обновлять и удалять бронирования. Сайт также включает в себя возможности для авторизации и аутентификации пользователей.

## Структура проекта
Проект организован следующим образом:
```
.
├── .github/workflows
│   └── practice.yml
├── exported data
│   ├── postman_environment.json
│   └── postman_collection.json
├── .gitignore
└── README.md
```
- `practice.yml` - CI для автоматического API тестирования коллекции restful-booker. Настроен с использованием Postman CLI.
- `exported data` - Папка с экпортированными из Postman окружением и коллекцией.
## Ссылки

Коллекция вместе с окружением [тут](https://www.postman.com/seitovaralina/env-resful-booker/collection/zy7x3rx/restful-booker?action=share&creator=38125094&active-environment=38125094-c13f5c0c-e0b1-4fc5-9cc0-85b4ca528721).