**OS: windows**
docker 설치
https://www.docker.com/docker-windows

docker 를 통한 elk 세팅
http://blog.naver.com/PostView.nhn?blogId=tmondev&logNo=220523961787
http://elk-docker.readthedocs.io/#installation
docker Quickstart Terminal 실행
```
$ docker search elk
$ docker pull sebp/elk
$ sudo docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk sebp/elk
```
>가상머신에서 돌릴때 엘라스틱 서치 구동시 오류 발생 
>( 메모리가 부족해서 발생 )
>```
>$ docker-machine ssh
>$ sudo sysctl -w vm.max_map_count=262144
>```
> 로 처리 해 주면 됨

http://elk-docker.readthedocs.io/#installation 페이지에 가이드 잘 되어 있어서 따라 하면 바로 elk 세팅 및 stdin 으로 테스트 가능(kibana로 볼 수 있음) 

 해당 컨테이너를 이용해서 메모 로그를 취합하고 분석 할 수 있는 시스템 구축 하려고 함

> Written with [StackEdit](https://stackedit.io/).