#!/bin/bash

# This script will be used to automate simulation executions for Part2, step 2 of the project.

# Initialize useful parameters:
declare -A benchmarks
benchmarks["bzip"]="spec_cpu2006/401.bzip2/src/specbzip -o \"spec_cpu2006/401.bzip2/data/input.program 10\""
benchmarks["mcf"]="spec_cpu2006/429.mcf/src/specmcf -o \"spec_cpu2006/429.mcf/data/inp.in\""
benchmarks["hmmer"]="spec_cpu2006/456.hmmer/src/spechmmer -o \"--fixed 0 --mean 325 --num 45000 --sd 200 --seed 0 spec_cpu2006/456.hmmer/data/bombesin.hmm\""
benchmarks["sjeng"]="spec_cpu2006/458.sjeng/src/specsjeng -o \"spec_cpu2006/458.sjeng/data/test.txt\""
benchmarks["lbm"]="spec_cpu2006/470.lbm/src/speclibm -o \"20 spec_cpu2006/470.lbm/data/lbm.in 0 1 spec_cpu2006/470.lbm/data/100_100_130_cf_a.of\""

gem5="./build/ARM/gem5.opt"
se="configs/example/se.py"

base_options="--cpu-type=MinorCPU --caches --l2cache -I 100000000"

output_dirs=() # list for output directories of .ini file

# Loop for running simulations for each benchmark automaticaly
for name in "${!benchmarks[@]}"; do
	bench=${benchmarks[$name]}

	echo "========================================== Simiulating Benchmark: $name =========================================="
	
	# >>>>>>>> Test IV - Different Combinations <<<<<<<<
	# (a): L1i 32kB, L1d 128kB, L2 4MB, L1 4-way, L2 8-way, Line Size 256B
	dir="part2step2_results/${name}_IVa"
    	output_dirs+=("$dir")
    	if [ ! -f "$dir/stats.txt" ]; then
        	echo "---Test IVa---"
        	eval $gem5 -d $dir $se $base_options --l1i_size=32kB --l1d_size=128kB --l2_size=4MB --l1d_assoc=4 --l1i_assoc=4 --l2_assoc=8 --cacheline_size=256 -c $bench
    	fi

	# (b): L1i 64kB, L1d 64kB, L2 4MB, L1 8-way, L2 16-way, Line Size 128B
	dir="part2step2_results/${name}_IVb"
    	output_dirs+=("$dir")
    	if [ ! -f "$dir/stats.txt" ]; then
        	echo "---Test IVb---"
        	eval $gem5 -d $dir $se $base_options --l1i_size=64kB --l1d_size=64kB --l2_size=4MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --cacheline_size=128 -c $bench
    	fi

	# (c): L1i 64kB, L1d 128kB, L2 4MB, L1 4-way, L2 16-way, Line Size 128B
	dir="part2step2_results/${name}_IVc"
    	output_dirs+=("$dir")
    	if [ ! -f "$dir/stats.txt" ]; then
        	echo "---Test IVc---"
        	eval $gem5 -d $dir $se $base_options --l1i_size=64kB --l1d_size=128kB --l2_size=4MB --l1d_assoc=4 --l1i_assoc=4 --l2_assoc=8 --cacheline_size=128 -c $bench
    	fi

	# (d): L1i 64kB, L1d 128kB, L2 4MB, L1 4-way, L2 16-way, Line Size 256B
	dir="part2step2_results/${name}_IVd"
    	output_dirs+=("$dir")
    	if [ ! -f "$dir/stats.txt" ]; then
        	echo "---Test IVd---"
        	eval $gem5 -d $dir $se $base_options --l1i_size=64kB --l1d_size=128kB --l2_size=4MB --l1d_assoc=4 --l1i_assoc=4 --l2_assoc=16 --cacheline_size=256 -c $bench
    	fi

	# (e): L1i 64kB, L1d 64kB, L2 4MB, L1 4-way, L2 16-way, Line Size 256B
	dir="part2step2_results/${name}_IVe"
    	output_dirs+=("$dir")
    	if [ ! -f "$dir/stats.txt" ]; then
        	echo "---Test IVe---"
        	eval $gem5 -d $dir $se $base_options --l1i_size=64kB --l1d_size=64kB --l2_size=4MB --l1d_assoc=4 --l1i_assoc=4 --l2_assoc=16 --cacheline_size=256 -c $bench
    	fi
done 

echo ">>>>>>>>>>>>>>>>>>>> Simulations Finished <<<<<<<<<<<<<<<<<<<<"

# Create .ini file
ini="resultsCombos.ini"
out_txt="results_tableCombos.txt"

echo "[Benchmarks]" > $ini

for dir in "${output_dirs[@]}"; do
    echo "$dir" >> $ini
done

echo "[Parameters]" >> $ini
echo "system.cpu.cpi" >> $ini
echo "system.cpu.dcache.overall_miss_rate::total" >> $ini
echo "system.cpu.icache.overall_miss_rate::total" >> $ini
echo "system.l2.overall_miss_rate::total" >> $ini
echo "sim_seconds" >> $ini

echo "[Output]" >> $ini
echo "$out_txt" >> $ini

bash read_results.sh $ini
cat $out_txt # write results in the same txt file



	