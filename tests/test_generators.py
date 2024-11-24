import pytest

from src.generators import card_number_generator

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


def test_filter_by_currency():
    pass


def test_transaction_descriptions():
    pass


@pytest.mark.parametrize(
    "start_number, stop_number, cards_finished",
    [
        (1, 3,
         ["0000 0000 0000 0001",
          "0000 0000 0000 0002",
          "0000 0000 0000 0003"
          ]
         ),
        (9999_9999_9999_9997,
         9999_9999_9999_9999,
         ["9999 9999 9999 9997",
          "9999 9999 9999 9998",
          "9999 9999 9999 9999"
          ]
         ),
        (255001,
         255003,
         ["0000 0000 0025 5001",
          "0000 0000 0025 5002",
          "0000 0000 0025 5003"
          ]
         )
    ]
)
def test_card_number_generator(start_number, stop_number, cards_finished):
    card_number = card_number_generator(start_number, stop_number)

    for ind, number in enumerate(card_number):
        assert number == cards_finished[ind]


@pytest.mark.parametrize(
    "start_wrong, stop_wrong",
    [
        (-1, -3),
        (2, -2),
        (-10, -10),
        (9999_9999_9999_9999_9, 5),
        (10, 9999_9999_9999_9999_9),
        (9999_9999_9999_9999_9, 9999_9999_9999_9999_9)
    ]
)
def test_card_number_generator_wrong(start_wrong, stop_wrong):

    with pytest.raises(ValueError):
        cards_wrong = card_number_generator(start_wrong, stop_wrong)
        assert next(cards_wrong)
