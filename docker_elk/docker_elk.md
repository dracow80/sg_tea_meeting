**OS: windows**
docker ��ġ
https://www.docker.com/docker-windows

docker �� ���� elk ����
http://blog.naver.com/PostView.nhn?blogId=tmondev&logNo=220523961787
http://elk-docker.readthedocs.io/#installation
docker Quickstart Terminal ����
```
$ docker search elk
$ docker pull sebp/elk
$ sudo docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk sebp/elk
```
>����ӽſ��� ������ ����ƽ ��ġ ������ ���� �߻� 
>( �޸𸮰� �����ؼ� �߻� )
>```
>$ docker-machine ssh
>$ sudo sysctl -w vm.max_map_count=262144
>```
> �� ó�� �� �ָ� ��

http://elk-docker.readthedocs.io/#installation �������� ���̵� �� �Ǿ� �־ ���� �ϸ� �ٷ� elk ���� �� stdin ���� �׽�Ʈ ����(kibana�� �� �� ����) 

 �ش� �����̳ʸ� �̿��ؼ� �޸� �α׸� �����ϰ� �м� �� �� �ִ� �ý��� ���� �Ϸ��� ��

> Written with [StackEdit](https://stackedit.io/).