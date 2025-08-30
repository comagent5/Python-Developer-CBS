'''
Урок № 1 Python Essential
'''

class Animal:
    '''Створення когось...'''

    def __init__(self, name: str, weight: int, color: str, voice: str):
        self.name = name
        self.weight = weight
        self.color = color
        self.voice = voice

    def __str__(self):
        return f'{self.name} колір {self.color} вага {self.weight} голос {self.voice}'

    def to_voice(self):
        return f'{self.voice} {self.voice} {self.voice}'

dog = Animal('Собака', 10, 'Чорний', 'Гав')
cat = Animal('Кішка', 2, 'Біла', 'Мяу')

print(dog)
print(cat)