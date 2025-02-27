import json

class MealyMachine:
    def __init__(self, states, alphabet, transitions, initial_state):
        """
        :param states: Множина станів автомата.
        :param alphabet: Множина символів вхідного алфавіту.
        :param transitions: Словник, що описує функцію переходів.
               Ключ – кортеж (поточний_стан, символ), значення – (наступний_стан, вихідний_символ).
        :param initial_state: Початковий стан автомата.
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.current_state = initial_state
        self.history = []

    def reset(self):
        self.current_state = self.initial_state
        self.history = []

    def process(self, input_string):
        output_of_process = ""
        print("Таблиця переходів:")
        print("{:^13} | {:^5} | {:^6} | {:^10}".format("Поточний стан", "Вхід", "Вихід", "Наступний стан"))
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"Символ '{symbol}' не належить вхідному алфавіту.")
                continue

            key = (self.current_state, symbol)
            if key not in self.transitions:
                print(f"Не визначено перехід для стану {self.current_state} при вході '{symbol}'.")
                continue

            next_state, output_symbol = self.transitions[key]
            print("{:^13} | {:^5} | {:^6} | {:^10}".format(self.current_state, symbol, output_symbol, next_state))
            self.history.append([self.current_state, symbol, output_symbol])
            output_of_process += output_symbol
            self.current_state = next_state
        return output_of_process

    def save_state(self, filename):
        data = {
            "current_state": self.current_state,
            "history": self.history
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Стан автомата збережено у файл {filename}")

    def load_state(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.current_state = data.get("current_state", self.initial_state)
        self.history = data.get("history", [])
        print(f"Стан автомата завантажено з файлу {filename}")


if __name__ == "__main__":
    alphabet = {"a", "b"}
    states = {"S0", "S1"}

    transitions = {
        ("S0", "a"): ("S1", "0"),
        ("S0", "b"): ("S0", "0"),
        ("S1", "a"): ("S1", "0"),
        ("S1", "b"): ("S0", "1")
    }

    initial_state = "S0"

    machine = MealyMachine(states, alphabet, transitions, initial_state)


    input_string = "aab"
    print("Обробка вхідного рядка:", input_string)
    output = machine.process(input_string)
    print("Отриманий вихідний рядок:", output)

    machine.save_state("Mealy.json")

    machine.reset()

    machine.load_state("Mealy.json")
