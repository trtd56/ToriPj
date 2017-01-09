# 定数の定義
JETPAC_PATH="/home/pi/projects/DeepBeliefSDK/networks/jetpac.ntwk"
TARGET="hummingbird"

# 一時ログが存在する場合は削除する
if [ ! -e log/tmp.log ]; then
  rm log/tmp.log
fi

# USBカメラで写真を撮影
fswebcam pict/tmp.jpg 2>> log/tmp.log
# 認識結果を一時保存
result=`jpcnn -i pict/tmp.jpg -n $JETPAC_PATH -t -m s 2>>log/tmp.log`

# 認識結果を配列に格納
ary=(`echo $result`)

# 目的の物体が認識されているか確認
# 実際の配列は確率と認識物体が交互に格納されているが、確率の方は無視する
echo -e "\n--- predict ---" >> log/tmp.log
is_save=0
for i in `seq 1 ${#ary[@]}`
do
  predict=`echo ${ary[$i-1]}`
  if [ "$predict" = "$TARGET" ] ; then
    is_save=1
  fi
  echo $predict >> log/tmp.log
done

# 目的の物体が認識された場合は写真とログを別名で保存する
if [ $is_save = 1 ] ; then
  date_str=`date -u +"%Y%m%d%H%M%S"`
  cp pict/tmp.jpg "pict/"$date_str".jpg"
  cp log/tmp "log/"$date_str".log"
fi

