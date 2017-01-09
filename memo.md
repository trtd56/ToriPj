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


# 参考

- [Raspberry PiでDeep Learning「DeepBeliefSDKで画像認識」](http://karaage.hatenadiary.jp/entry/2015/12/16/073000)
- [はじめてのRaspberry PIで監視カメラを作ってみた。](http://qiita.com/kinpira/items/bf1df2c1983ba79ba455)
