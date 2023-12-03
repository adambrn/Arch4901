Для приложения заказа столика в ресторане сделать архитектурные документы:
1) Разработать экранные формы интерфейса(UI/UX) в https://www.figma.com/, https://pixso.net/ru/ или https://app.diagrams.net/.
2) Разработать полную ERD домена в https://www.dbdesigner.net/.
3) Разработать UML диаграмму классов 
ux/ui
1. логотип
логин 
пароль
перейти

2. Карусель зал
время 
количество персон

3. Список столиков
карточки столиков

4. Заказ столика
информация о заказе
кнопка заказать

ERD
costumer
 id
 name
hall
 id
 type
 smoke
 music

table
    id
    places
    hall_id

order
    id
    date
    time

uml
адаптер 
    viwe
логика
    irepo
    service
    domain class
данные
    repo
    crud