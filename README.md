# Surprisal-measurements
This repository contains the surprisal measurements for a number of .wav files, recorded for the ongoing project 'Comprehension under Pressure', conducted by Petter Kallioinen and others at Stockholm University. Moreover, this repository contains the transcriptions of the .wav-files, a textfile containing basic statistics on the surprisal data for every .wav-file and Python scripts to sentence tokenize the transcriptions, to calculate the surprisal values for every word on a sentence level and to convert the surprisal values into a format, in which one can create histograms of the surprisal distributions in the data. The surprisal values were calculated using the LLM _google/gemma-3-1b-pt_.
## Usage
```python
åsa_wikforss_1_surprisals = surprisal_adjuster2.sp_words_with_scores(surprisal_adjuster2.read_file('åsa_wikforss_surprisalvärden.txt')) # åsa_wikforss.wav contains 1GB data, it has therefore been separated into three parts

data = []

for å in åsa_wikforss_1_surprisals: # do the same with åsa_wikforss_2 and åsa_wikforss_3 without renewing data, to get the whole dataset
  for t in g:
    data.append(t[1]) # use this data to create the histogram  

```
## Installation
To install the surprisal package in surprisal_calculator.py, see https://github.com/aalok-sathe/surprisal.
## License
The scripts are under [MIT](https://choosealicense.com/licenses/mit/). The transcriptions are under ?
