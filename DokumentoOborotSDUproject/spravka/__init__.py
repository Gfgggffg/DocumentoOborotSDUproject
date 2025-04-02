import docx
import pandas as pd
import re

# Функция для чтения переменных из вордовского документа
def read_variables_from_word(file_path):
    doc = docx.Document(file_path)
    variables = []
    
    # Поиск переменных в двойных фигурных скобках
    pattern = r'\{\{(.*?)\}\}'
    
    for paragraph in doc.paragraphs:
        matches = re.findall(pattern, paragraph.text)
        variables.extend(matches)
    
    return variables

# Функция для записи переменных в Excel файл
def write_to_excel(variables, output_file):
    df = pd.DataFrame([variables])  # Создаем DataFrame из списка переменных
    df.to_excel(output_file, index=False, header=False)  # Записываем в Excel без индекса и заголовка

# Основная часть программы
word_file_path = 'СТУДЕНЧЕСКИЙ БИЛЕТ.docx'  # Укажите путь к вашему вордовскому документу
excel_file_path = 'выходной_файл.xlsx'  # Укажите путь к выходному Excel файлу

variables = read_variables_from_word(word_file_path)
write_to_excel(variables, excel_file_path)

print("Переменные успешно записаны в Excel.")
