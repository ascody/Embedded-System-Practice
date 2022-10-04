import time
# GPIO 핀 라이브러리
import RPi.GPIO as GPIO
# adafruit_dht 라이브러리
import adafruit_dht
# 핀 설정
dhtDevice = adafruit_dht.DHT11(18)

while True:
    try:
        # 온습도 측정 및 출력
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} C    Humidity: {}% ".format(temperature, humidity))
    # 런타임 에러(ex.메모리 에러)가 발생한다면
    # 에러 메시지 출력, 2초 대기 후 다시 시작
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    # 예외가 발생한다면 종료
    except Exception as error:
        dhtDevice.exit()
        raise error
