#!/bin/bash

i=1
while :
do
    hadoop fs -rm -f -r /output$i
    hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapred.reduce.tasks=1 \
    -file distance.txt \
    -file ./mapper.py \
    -mapper ./mapper.py \
    -file ./reducer.py \
    -reducer ./reducer.py \
    -input /graph.txt \
    -output /output$i \
        
    rm -f distance1.txt
    hadoop fs -copyToLocal /output$i/part-00000 /home/hadoop/distance1.txt

    stopfile=`python stop.py` 

    if [ $stopfile = 1 ]
    then
        rm distance.txt
        hadoop fs -copyToLocal /output$i/part-00000 /home/hadoop/distance.txt
        break
    else
        rm distance.txt
        hadoop fs -copyToLocal /output$i/part-00000 /home/hadoop/distance.txt
    fi
	i=$((i+1))
done

