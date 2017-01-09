# 定数の定義
JETPAC_PATH="/home/pi/projects/DeepBeliefSDK/networks/jetpac.ntwk"
LOG_PATH="/home/pi/ToriPj/log/tmp.log"

pict_path=$1
token=`cat token`
predict=`jpcnn -i $pict_path -n $JETPAC_PATH -t -m s 2>> $LOG_PATH | tr "\t" ":" | tr " " "_" | tr "\n" "@"`

python bot.py $token $pict_path $predict
