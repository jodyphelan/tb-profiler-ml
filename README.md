# tb-profiler-ml

## Install

```bash
git clone https://github.com/jodyphelan/tb-profiler-ml.git
cd tb-profiler-ml
conda env create -f env.yml
conda activate tb-profiler-ml
pip install .
```

## Test

```bash
conda activate tb-profiler-ml
tb-profiler-ml profile --model test/mdr.pkl --result test/SRR8651558.results.json --outfile test.result.json 
```