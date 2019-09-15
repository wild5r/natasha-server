# Build and run

```
docker build -t natasha-server .
docker run -d -p 127.0.0.1:10101:8080 --user nobody --restart unless-stopped natasha-server
```

# Dev server

```
docker run --rm -it -p 8080:8080 -v $(pwd)/src/natasha_json_server.py:/opt/natasha_json_server.py natasha-server
```

# Test requests

```
POST http://localhost:8080/natasha
Content-Type: application/json

{
  "data": "Простите, еще несколько цитат из приговора. «…Отрицал существование Иисуса и пророка Мухаммеда», «наделял Иисуса Христа качествами ожившего мертвеца — зомби» [и] «качествами покемонов — представителей бестиария японской мифологии, тем самым совершил преступление, предусмотренное статьей 148 УК РФ"
}
```

```
POST http://localhost:8080/natasha
Content-Type: application/json

{
  "data": "Сергей Собянин поручил разработать проект стимулирования к бесплатному донорству - Вечерняя Москва"
}
```
