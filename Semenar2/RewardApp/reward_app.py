from abc import ABC, abstractmethod
from random import choice

class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class Gem(IGameItem):
    def open(self):
        print('Gem!')


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()
    
class Experience(IGameItem):
    def open(self):
        print('Experience points!')


class Weapon(IGameItem):
    def open(self):
        print('New weapon!')


class Armor(IGameItem):
    def open(self):
        print('New armor!')


class Potion(IGameItem):
    def open(self):
        print('Health potion!')


class Food(IGameItem):
    def open(self):
        print('New food!')


class ExperienceGenerator(ItemFabric):
    def create_item(self):
        return Experience()


class WeaponGenerator(ItemFabric):
    def create_item(self):
        return Weapon()


class ArmorGenerator(ItemFabric):
    def create_item(self):
        return Armor()


class PotionGenerator(ItemFabric):
    def create_item(self):
        return Potion()


class FoodGenerator(ItemFabric):
    def create_item(self):
        return Food()



if __name__ == '__main__':
    ratios = {
        GoldGenerator: 3,
        GemGenerator: 1,
        ExperienceGenerator: 10,
        WeaponGenerator: 10,
        ArmorGenerator: 10,
        PotionGenerator: 10,
        FoodGenerator: 10,
    }

    reward_types = [key for key in ratios for _ in range(ratios[key])] # Создадим список вознаграждений с заданным количеством

    generated_rewards = []  # Для отслеживания генерированных вознаграждений

    for _ in range(54):  
        reward_type = choice(reward_types)
        reward = reward_type().create_item()
        reward.open()
        generated_rewards.append(reward.__class__.__name__)

    # Вычислим количество сгенерированных вознаграждений
    generated_ratio = {reward: generated_rewards.count(reward) for reward in set(generated_rewards)}


    print("\nGenerated ratio of rewards:")
    for reward, count in generated_ratio.items():
        ratio = (count / len(generated_rewards)) * 100
        print(f"{reward}: {count} ({ratio:.2f}%)")