import matplotlib.pyplot as plt
import numpy as np

models = ["ASUS ROG Strix", "Lenovo Legion 5", "HP Omen 15", "MSI GF65"]
name_char = [
    "Процессор (ГГц)",
    "ОЗУ (ГБ)",
    "SSD (ГБ)",
    "Видеокарта (ГБ)",
    "Экран (дюймы)",
    "Вес (кг)",
]
char = [
    [2.6, 16, 512, 8, 15.6, 2.4],
    [3.0, 32, 1000, 6, 15.6, 2.7],
    [2.8, 16, 512, 4, 15.6, 2.3],
    [2.5, 16, 256, 6, 15.6, 2.1],
]


def get_normal(char):
    normal = []
    for item in char:
        normal.append([a / b for a, b in zip(item, char[0])])
    return normal


def get_quality(normal):
    result = []
    for item in normal:
        result.append(round(sum(item) / len(item), 2))
    return result


def create_bar(name, values):
    plt.figure(figsize=(10, 6))
    bars = plt.bar(name, values, color='skyblue', edgecolor='black')
    plt.xlabel("Модель")
    plt.ylabel("Kту")
    plt.title("Сравнение ноутбуков по качеству")
    plt.xticks(rotation=20)
    for bar, val in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,val, ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.show()


def create_radial(models, name, values):
    values_closed = []
    for item in values:
        values_closed.append(item + item[:1])

    angles = np.linspace(0, 2 * np.pi, len(name), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection="polar"))

    for i in range(len(values)):
        ax.plot(angles, values_closed[i], "o-", linewidth=2, label=models[i])
        ax.fill(angles, values_closed[i], alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(name, fontsize=10)
    ax.set_ylim(0, 2)

    # Легенда и заголовок
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    plt.title("Сравнение относительных характеристик ноутбуков", pad=20)
    plt.tight_layout()
    plt.show()


data = get_quality(get_normal(char))
create_bar(models, data)
create_radial(models, name_char, get_normal(char))