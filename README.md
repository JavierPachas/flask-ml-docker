# flask-ml-docker

![image](https://github.com/user-attachments/assets/1efd1dc3-c655-42e7-8e49-f5f37dd7c259)


```
docker build --build-arg VERSION=AutoML_7777 -t flask-predict .

docker images flask-predict

docker run -p 5005:5000 -d --name flask-predict flask-predict
```
