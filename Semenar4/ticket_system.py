import datetime

class Ticket:
    id: int
    departure_zone: int
    arrival_zone: int
    route_number: int
    departure_time: datetime
    arrival_time: datetime
    buyer_id: int
    is_used: bool
    price: float
    place: str

class Account:
    user_account_id: int
    balance: float

class User:
    id: int
    name: str
    tickets: [Ticket]
    login: str
    password_hash_code: int
    account_id: int
