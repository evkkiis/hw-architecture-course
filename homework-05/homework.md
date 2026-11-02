# Домашнее задание 23.10

## 1. HTTP (расшифруй и объясни назначение)

**HTTP** — HyperText Transfer Protocol (протокол передачи гипертекста). Прикладной протокол передачи данных, лежащий в основе Всемирной паутины. Он описывает, как клиент и сервер обмениваются сообщениями. Используется для загрузки веб-страниц, работы API, передачи файлов, изображений и др.

## 2. HTTPS — чем отличается от HTTP?

Отличия заключаются в том, что данные между клиентом и сервером зашифрованы и их нельзя прочитать или подменить. Разница в портах: HTTP — 80, HTTPS — 443.

## 3. Клиент-серверная модель — что это?

Архитектура взаимодействия, при которой клиент — это инициатор запросов, то есть он отправляет запросы и обрабатывает ответы, а сервер — это программа, которая принимает запросы и обрабатывает их.

## 4. Идемпотентность — что означает?

Это свойство операции, при котором повторное выполнение того же запроса даёт тот же результат, что и однократное.

---

## 2.1. Разбери запрос

#### Дан HTTP-запрос:

http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Content-Length: 58

{"name": "Иван", "email": "ivan@mail.com"}


#### Ответь на вопросы:

Какой метод используется? — POST

Какой путь (endpoint) запрашивается? — /api/users

Какая версия HTTP? — HTTP/1.1

Что означает заголовок Content-Type? — application/json

Что означает заголовок Authorization? — То, что клиент передаёт токен доступа, который сервер проверяет, чтобы идентифицировать пользователя и проверить его права.

Где находится тело запроса? — {"name": "Иван", "email": "ivan@mail.com"}

---

## 2.3. Собери запрос сам
### Составь HTTP-запрос для:

#### Получения списка всех товаров

GET /api/products HTTP/1.1

Host: example.com

Accept: application/json

Authorization: Bearer <token>

#### Создания нового товара с именем "Ноутбук" и ценой 50000
POST /api/products HTTP/1.1

Host: example.com

Content-Type: application/json

Authorization: Bearer <token>

Content-Length: 46

{"name": "Ноутбук", "price": 50000}

#### Удаления товара с id=7
DELETE /api/products/7 HTTP/1.1

Host: example.com

Authorization: Bearer <token>

#### Обновления товара с id=3 (изменить цену на 45000)
PUT /api/products/3 HTTP/1.1

Host: example.com

Content-Type: application/json

Authorization: Bearer <token>

Content-Length: 53

{"id": 3, "name": "Ноутбук", "price": 45000}

---
