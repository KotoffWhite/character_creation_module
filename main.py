from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_TRAINING_DESC = 'отважный'

    def __init__(self, char_name: str):
        self.char_name = char_name

    def attack(self):
        """Count attack."""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.char_name} нанёс противнику урон, равный '
                f'{value_attack}')

    def defence(self):

        """Count defence"""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.char_name} блокировал {value_defence} ед. урона'

    def special(self):

        """Count special."""
        return (f'{self.char_name} применил специальное умение '
                f'«{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}»')

    def brief_desc(self):
        """Descr for training."""
        return f'{self.char_name} - {self.BRIEF_TRAINING_DESC}'

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):

    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    BRIEF_TRAINING_DESC = ', ты Воитель — великий мастер ближнего боя.'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    BRIEF_TRAINING_DESC = ', ты Маг — превосходный укротитель стихий.'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    BRIEF_TRAINING_DESC = ', ты Лекарь — чародей, способный исцелять раны.'


def start_training(character: Character) -> str:
    """Starts training."""
    commands = {'attack': character.attack(), 'defence': character.defence(),
                'special': character.special()}
    character.brief_desc()
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = input()
    while cmd != 'skip':
        if cmd not in commands:
            print('Неверная команда, попробуй снова')
        else:
            print(commands[cmd])
        cmd = input()
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """Choose class."""

    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice = None
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def main():
    """Приветствует."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: Character = choice_char_class(char_name)
    print(start_training(char_class))

main()
