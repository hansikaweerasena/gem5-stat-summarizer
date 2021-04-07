# gem5-stat-summarizer
In default configuration gem5 will dump 1000+ statistics to `stats.txt` file but in most of the cases we want only few of these stats for our exploration. Furthermore, when you're doing benchmarking or exploration with many configurations the `stats.txt` files will grow rapidly. You can use this python script to summarize gem5 stats over many configurations in to a single csv file.

### Dependencies

* python3
* pandas

### Usage

First you have to specify the full stat name in `targetStats` file separated by new lines. Examples stats are in `targetStats` file.

If you have following file structure in m5out folder of gem5:

```
m5out   
└─── FFT
│   └─── config 1
│   │   │   stats.txt
│   │   
│   └─── config 2
│   │   │   stats.txt
│   │   
└─── RADIX
    └─── config 1
    │   │   stats.txt
    │   
    └─── config 2
    │   │   stats.txt

```

Following command will output csv file with for all configurations in FFT folder. 

`python summarizeStat.py ./m5out/FFT ./output/FFT.csv
`
