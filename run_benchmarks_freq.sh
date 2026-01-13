#!/bin/bash

echo "---Starting bzip Sim. (1GHz)---" && \
./build/ARM/gem5.opt -d spec_results/specbzip_1GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=1GHz -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000 && \

echo "---Starting bzip Sim. (4GHz)---" && \
./build/ARM/gem5.opt -d spec_results/specbzip_4GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=4GHz -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000 && \


echo "---Starting mcf Sim. (1GHz)---" && \
./build/ARM/gem5.opt -d spec_results/specmcf_1GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=1GHz -c spec_cpu2006/429.mcf/src/specmcf -o "spec_cpu2006/429.mcf/data/inp.in" -I 100000000 && \

echo "---Starting mcf Sim. (4GHz)---" && \
./build/ARM/gem5.opt -d spec_results/specmcf_4GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=4GHz -c spec_cpu2006/429.mcf/src/specmcf -o "spec_cpu2006/429.mcf/data/inp.in" -I 100000000 && \

echo "---Starting hmmr Sim. (1GHz)---" && \
./build/ARM/gem5.opt -d spec_results/spechmmer_1GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=1GHz -c spec_cpu2006/456.hmmer/src/spechmmer -o "--fixed 0 --mean 325 --num 45000 --sd 200 --seed 0 spec_cpu2006/456.hmmer/data/bombesin.hmm" -I 100000000 && \

echo "---Starting hmmr Sim. (4GHz)---" && \
./build/ARM/gem5.opt -d spec_results/spechmmer_4GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=4GHz -c spec_cpu2006/456.hmmer/src/spechmmer -o "--fixed 0 --mean 325 --num 45000 --sd 200 --seed 0 spec_cpu2006/456.hmmer/data/bombesin.hmm" -I 100000000 && \

echo "---Starting sjeng Sim. (1GHz)---" && \
./build/ARM/gem5.opt -d spec_results/specsjeng_1GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=1GHz -c spec_cpu2006/458.sjeng/src/specsjeng -o "spec_cpu2006/458.sjeng/data/test.txt" -I 100000000 && \

echo "---Starting sjeng Sim. (4GHz)---" && \
./build/ARM/gem5.opt -d spec_results/specsjeng_4GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=4GHz -c spec_cpu2006/458.sjeng/src/specsjeng -o "spec_cpu2006/458.sjeng/data/test.txt" -I 100000000 && \

echo "---Starting libm Sim. (1GHz)---" && \
./build/ARM/gem5.opt -d spec_results/speclibm_1GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=1GHz -c spec_cpu2006/470.lbm/src/speclibm -o "20 spec_cpu2006/470.lbm/data/lbm.in 0 1 spec_cpu2006/470.lbm/data/100_100_130_cf_a.of" -I 100000000 && \

echo "---Starting libm Sim. (4GHz)---" && \
./build/ARM/gem5.opt -d spec_results/speclibm_4GHz configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --cpu-clock=4GHz -c spec_cpu2006/470.lbm/src/speclibm -o "20 spec_cpu2006/470.lbm/data/lbm.in 0 1 spec_cpu2006/470.lbm/data/100_100_130_cf_a.of" -I 100000000 && \

echo "---Finished all Sims---"