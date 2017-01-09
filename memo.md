# ラズパイのIP固定

- 設定内容例

~~~
固定するIP 192.168.0.10
ルータのIP 192.168.0.1
~~~

- __/etc/dhcpcd.conf__ の設定

~~~
interface eth0
static ip_address=192.168.0.10/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
~~~

# DeepBeliefSDK

- 基本的にGitHubのREADMEに沿って設定する

~~~
$ git clone https://github.com/jetpacapp/DeepBeliefSDK.git
~~~
- 下記手順を追加しないと動かない場合がある？

~~~
sudo cp libjpcnn.so /usr/lib/
sudo cp src/include/libjpcnn.h /usr/include/
~~~

# motion

- インストール

~~~
$ sudo apt-get install -y motion
~~~

- 初期設定

~~~
$ sudo vim /etc/motion/motion.conf
(変更)
daemon off
ffmpeg_output_movies off
target_dir /tmp/motion
~~~

- 実行方法

~~~
$ sudo motion -c /etc/motion/motion.conf
~~~

- 取った写真の情報をスクリプトに渡す

~~~
$ sudo vim /etc/motion/motion.conf
(追記)
on_picture_save bash /home/pi/ToriPj/run.sh %f
~~~

# Slack

- インストール

~~~
$ sudo pip install slacker
~~~

- テスト用tokenの作成
 - チーム名クリック
 - TeamSettingクリック
 - 左上のメニューをクリックして出てきたメニューの中のAPIをクリック
 - APIsの中のWeb APIをクリック
 - 下の方のGenerate test tokensをクリック
 - 使うチームのCreate tokenをクリックして作成

- テスト

~~~
$ python
>>> from slacker import Slacker
>>> token = "xxxx-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxx"
>>> slacker = Slacker(token)
>>> channel_name = "#" + "general"
>>> message = 'テスト'
>>> slacker.chat.post_message(channel_name, message)
~~~

# 音を鳴らす

- 音量調節コマンド

~~~
$ alsamixer
~~~

# カメラの映像確認

- インストール

~~~
$ sudo apt-get install -y subversion libjpeg-dev imagemagick
$ svn co https://svn.code.sf.net/p/mjpg-streamer/code/mjpg-streamer mjpg-streamer
$ cd mjpg-streamer
$ make
$ sudo make install
~~~

- mjpg-streamerフォルダ内に起動スクリプトの作成

~~~
$ vi start_server.sh


#!/bin/sh
  
PORT="8080" #ポート番号
ID="user" #ID
PW="passward" #パスワード
SIZE="320x240" #画面サイズ
FRAMERATE="2" #フレームレート
export LD_LIBRARY_PATH=/usr/local/lib
./mjpg_streamer \
    -i "input_uvc.so -f $FRAMERATE -r $SIZE -d /dev/video0 -y -n" \
    -o "output_http.so -w /usr/local/www -p $PORT -c $ID:$PW"
~~~

- 確認

~~~
$ sudo sh start_server.sh
~~~

# 参考

- [Raspberry PiでDeep Learning「DeepBeliefSDKで画像認識」](http://karaage.hatenadiary.jp/entry/2015/12/16/073000)
- [はじめてのRaspberry PIで監視カメラを作ってみた。](http://qiita.com/kinpira/items/bf1df2c1983ba79ba455)
- [Raspberry Piでwav/mp3ファイルを再生する方法(python編)](http://qiita.com/Nyanpy/items/cb4ea8dc4dc01fe56918)
- [USBカメラで監視カメラ](http://make.bcde.jp/raspberry-pi/usb%E3%82%AB%E3%83%A1%E3%83%A9%E3%81%A7%E7%9B%A3%E8%A6%96%E3%82%AB%E3%83%A1%E3%83%A9/)
