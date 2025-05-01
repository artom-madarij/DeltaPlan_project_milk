import serial
import requests

# Відкриваємо з'єднання з послідовним портом (заміни на свій COM порт)
ser = serial.Serial('COM3', 9600)  # 'COM3' може бути іншим, залежно від твоєї конфігурації

# URL локального серверу Flask
server_url = "http://localhost:5000/submit-data"

while True:
    line = ser.readline().decode('utf-8').strip()  # Читання даних з Arduino
    print("Отримано з Arduino:", line)
    
    if line.startswith('T:') and ';H:' in line:
        # Обробка даних
        parts = line.replace('T:', '').split(';H:')
        temperature = parts[0]
        humidity = parts[1]

        print(f"Температура: {temperature}, Вологість: {humidity}")  # Перевірка отриманих даних
        
        # Формуємо дані для надсилання
        data = {
            'temperature': temperature,
            'humidity': humidity
        }
        
        # Відправка POST запиту на сервер
        try:
            response = requests.post(server_url, json=data)
            if response.status_code == 200:
                print('Дані успішно надіслані!')
            else:
                print(f"Помилка при надсиланні даних: {response.status_code} - {response.text}")
        except Exception as e:
            print('Помилка надсилання:', e)
