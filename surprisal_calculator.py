import surprisal
from pathlib import Path
from huggingface_hub import login
from stimulus_generator import read_file
import os

# model_name = sys.argv[1]
# stims = sys.argv[2]

def main(model_name):
    with open(Path.home() / "hf-read-gated.key") as f:
        hf_token = f.read().strip()

    login(hf_token)
    
    # filenames = ['alexander_petter-001.txt', 'ghazaleh_petter-001_hel.txt', 'alexander_petter-002.txt', 'ghazaleh_petter-002.txt', 'alexander.txt', 'greta_rebecca-001.txt', 'david_hel.txt', 'greta_rebecca-002.txt', 'ghazaleh_hel.txt',  'greta.txt']
    # filenames = ['greta_rebecca-001_complicated.txt', 'greta_rebecca-002_complicated.txt', 'david_hel.txt', 'alexander_petter-001_complicated.txt', 'alexander_petter-002_complicated.txt']
    filenames = ['alexander_petter-001_complicated.txt', 'alexander_petter-002_complicated.txt', 'david_complicated.txt', 'greta_rebecca-001_complicated.txt', 'greta_rebecca-002_complicated.txt']
    # filenames = ['ghazaleh_petter-001_hel.txt', 'david_hel.txt', 'greta_rebecca-002.txt', 'ghazaleh_hel.txt', 'greta.txt']
    g = surprisal.AutoHuggingFaceModel.from_pretrained(
            model_name,
            model_class='causal')
    # b = surprisal.AutoHuggingFaceModel.from_pretrained(model_id="bert-base-uncased")


    # stims = [
    #    "Ska jag köra?",
    # ]

    # surps = [*g.surprise(stims)] # , *g.surprise(stims, use_bos_token=False)]
    for filename in filenames:
        outputfile = os.path.basename(filename).split('.')[0] + '_surprisal_values_ai_sweden_llama.txt'
        with open(outputfile, 'w', encoding='utf-8', newline='') as p:
            stimuli = read_file(filename)
            for stimulus in stimuli:
                print(g.surprise(stimulus))
                print(filename)
                p.write(str(g.surprise(stimulus)) + '\n')
            
    # *_, surp = surps
    # print(f"tokens: {surp}")

    # for wslc in [0, 1, slice(0, 1)]:
    #    print(f"span of interest (word index): {wslc}")
    #    print(f"recovered surprisal: {surp[wslc, 'word']}")
    #    print("=" * 32)
