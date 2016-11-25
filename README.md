# MagPi-Disaster Response Robot
Disaster Respoense Robot based on Raspberry Pi &amp; Python

#How to install mjpg-streamer

필요한 라이브러리들 먼저 설치

	$ sudo apt-get install git cmake libjpeg8-dev imagemagick libv4l-dev subversion -y

빌드에 필요한 videodev.h 파일이 없으므로 videodev2.h 파일로 연결

	$ sudo ln -s /usr/include/linux/videodev2.h /usr/include/linux/videodev.h

소스 다운로드(repo안에도 있음.)

	$ wget http://sourceforge.net/code-snapshots/svn/m/mj/mjpg-streamer/code/mjpg-streamer-code-182.zip

압축 해제

	$ unzip mjpg-streamer-code-182.zip

빌드

	$ cd mjpg-streamer-code-182/mjpg-streamer
	$ make mjpg_streamer input_file.so output_http.so

인스톨

	$ sudo cp mjpg_streamer /usr/local/bin
	$ sudo cp output_http.so input_file.so /usr/local/lib/
	$ sudo cp -R www /usr/local/www
