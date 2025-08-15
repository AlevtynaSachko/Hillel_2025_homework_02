import csv
from pathlib import Path

# Шлях
data_dir = Path(__file__).parent
file1 = data_dir / "random.csv"
file2 = data_dir / "random-michaels.csv"

# Зчитуємо всі рядки з обох файлів
rows = set() # set для автом видалення дублікатів

def read_csv_rows(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        return header, [tuple(row) for row in reader] # рядки як кортежі (щоб додати у set)

# Зчитуємо перший файл
header1, data1 = read_csv_rows(file1)
header2, data2 = read_csv_rows(file2)


# Об’єднуємо без повторів
rows.update(data1)
rows.update(data2)

# Запис результату
output_file = Path("result_Sachko.csv")
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header1) # заголовок
    writer.writerows(sorted(rows)) # зберегти відсортовано, щоб було стабільно

print(f"Готово! Файл збережено: {output_file}")