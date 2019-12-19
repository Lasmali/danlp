from danlp.datasets import WordSim353Da, DSD
from danlp.models.embeddings import AVAILABLE_EMBEDDINGS, load_wv_with_gensim
import tabulate


def load_wv_models():
    for da_wv_model in AVAILABLE_EMBEDDINGS:
        yield da_wv_model, load_wv_with_gensim(da_wv_model)


ws353 = WordSim353Da()
dsd = DSD()

data = []

for model_name, wv in load_wv_models():

    print("DSD words not in vocab of {}: {}".format(model_name, [w for w in dsd.words() if w.lower() not in wv.vocab]))

    correlation_on_dsd = wv.evaluate_word_pairs(dsd.file_path, delimiter="\t")
    spearman_rho_dsd = correlation_on_dsd[1].correlation
    oov_dsd = correlation_on_dsd[2]

    print("WS353 words not in vocab of {}: {}".format(model_name, [w for w in ws353.words() if w.lower() not in wv.vocab]))
    correlation_on_ws353 = wv.evaluate_word_pairs(ws353.file_path, delimiter=',')
    spearman_rho_ws353 = correlation_on_ws353[1].correlation
    oov_ws353 = correlation_on_ws353[2]

    data.append([model_name, len(wv.vocab), wv.vector_size, spearman_rho_ws353, oov_ws353, spearman_rho_dsd, oov_dsd])

headers = ['Model', 'Vocab', 'Vec Size', 'WS353-rho', 'WS353-OOV', 'DSD-rho',
           'DSD-OOV']
aligns = ['left', 'center', 'center', 'center', 'center', 'center', 'center']

print(tabulate.tabulate(data, headers=headers, tablefmt='github', colalign=aligns))

# Outputs:
# | Model              |  Vocab  |  Vec Size  |  WS353-rho  |  WS353-OOV  |  DSD-rho  |  DSD-OOV  |
# |--------------------|---------|------------|-------------|-------------|-----------|-----------|
# | wiki.da.wv         | 312956  |    300     |  0.638902   |  0.849858   |  0.20488  |  1.0101   |
# | cc.da.wv           | 2000000 |    300     |  0.532651   |   1.69972   | 0.313191  |     0     |
# | conll17.da.wv      | 1655870 |    100     |  0.548538   |   1.69972   | 0.149638  |     0     |
# | news.da.wv         | 2404836 |    300     |  0.540629   |   4.24929   | 0.306499  |     0     |
# | sketchengine.da.wv | 2360830 |    100     |  0.625922   |  0.849858   | 0.197373  |     0     |
