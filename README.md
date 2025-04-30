
```
cd ЕС2
cd bonus
sudo docker build -t api .
sudo docker run -p 5000:5000 --name api api
```
```
cd ЕС2
cd tg-bot
sudo docker build -t tg .
sudo docker run --name tg tg
```
---
If you don't have docker. You can install https://docs.docker.com/engine/install/
