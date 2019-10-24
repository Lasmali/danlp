Datasets
========
This section keeps a list of Danish NLP datasets publicly available.

| Dataset | Task | Words | Sents | License | DaNLP |
|---------|------|-------|-------|---------|-----------------|
| [OpenSubtitles2018](<http://opus.nlpl.eu/OpenSubtitles2018.php>) | Translation | 206,700,000 | 30,178,452 |[None](http://opus.nlpl.eu/OpenSubtitles2018.php) | ❌ |
| [EU Bookshop](http://opus.nlpl.eu/EUbookshop-v2.php) | Translation | 208,175,843 | 8,650,537 | - | ❌ |
| [EuroParl7](http://opus.nlpl.eu/Europarl.php) | Translation | 47,761,381 | 2,323,099	 | [None](http://www.statmt.org/europarl/) | ❌ |
| [ParaCrawl5](https://paracrawl.eu/) | Translation | - | - | [CC0](https://paracrawl.eu/releases.html) | ❌ |
| [WikiANN](https://github.com/alexandrainst/danlp/blob/add-ner/docs/datasets.md#wikiann)| NER | 832.901 | 95.924 |[ODC-BY 1.0](http://nlp.cs.rpi.edu/wikiann/)| ✔️ |
| [Danish Dependency Treebank](https://github.com/alexandrainst/danlp/blob/add-ner/docs/datasets.md#danish-dependency-treebank) | DEP, POS, NER |  100,733 |  5,512 | [CC BY-SA 4.0](https://github.com/UniversalDependencies/UD_Danish-DDT/blob/master/README.md) | ✔️ |
| [Wikipedia](https://dumps.wikimedia.org/dawiki/latest/) | Raw | - | - | [CC BY-SA 3.0](https://dumps.wikimedia.org/legal.html) | ❌ |
| [WordSim-353](https://github.com/alexandrainst/danlp/blob/add-ner/docs/datasets.md#wordsim-353) | Word Similarity  | 353 | - | [CC BY 4.0](https://github.com/fnielsen/dasem/blob/master/dasem/data/wordsim353-da/LICENSE)| ❌ |

#### Danish Dependency Treebank
The DDT dataset (Buch-Kromann et al. 2003) has annotations for dependency parsing, POS and NER.
The dataset was annotated with NER annotations for **PER**, **ORG** and **LOC** by the Alexandra Institute.
To read more about how the dataset was annotated with POS and DEP tags we refer to the
[Universal Dependencies](https://github.com/UniversalDependencies/UD_Danish-DDT/blob/master/README.md) page.
The dataset can be used with the DaNLP package:

```python
from danlp.datasets import DDT
ddt = DDT()

spacy_corpus = ddt.load_with_spacy()
flair_corpus = ddt.load_with_flair()
conllu_format = ddt.load_as_conllu()
```

#### WikiANN
The WikiANN dataset [(Pan et al. 2017)](https://aclweb.org/anthology/P17-1178) is a dataset with NER annotations
for **PER**, **ORG** and **LOC**. It has been constructed using the linked entities in Wikipedia pages for 282 different
languages including Danish. The dataset can be loaded with the DaNLP package:

```python
from danlp.datasets import WikiAnn
wikiann = WikiAnn()

spacy_corpus = wikiann.load_with_spacy()
flair_corpus = wikiann.load_with_flair()
```

#### Dawiki
Wikipedia dump downloaded from [Wikimedia Downloads](https://dumps.wikimedia.org/). Downloads and uses
[attardi/Wikiextractor.py](https://github.com/attardi/wikiextractor) to clean dumps. Corpus is saved as raw  
unprocessed text and may require preprocessing such as removal of empty lines and symbols.

```python
from danlp.datasets import DA_WIKI

dawiki = DA_WIKI()
wiki_corpus = dawiki.load_as_txt()
```

#### OPUS

[OPUS](http://opus.nlpl.eu/) is a collection of datasets including *OpenSubtitles*, *Europarl*,
*EUBookshop* and *ParaCrawl*. Currently only the **monolingual** corpuses are downloadable
through *DaNLP*. This is suitable for language modeling or word embeddings, however OPUS also has parallel corpuses useful for translation application. These could be added at a later stage.

Download and load all OPUS corpuses into memory - **Note:** lazy loading is not implemented due to the relative small data size of *mono-danish-OPUS* (~3.8G), hence downloading and loading all corpuses takes a few minutes.
```python
from danlp.datasets import OPUS

# download all opus corpuses and load them into memory
opus = OPUS()
opus_corpus = opus.load_as_txt()
```

We can also download or load a subset of OPUS corpuses.

```python
from danlp.datasets import OPUS

# specify subset of corpuses to download
opus = OPUS('Europarl','ParaCrawl')
# downloads and loads all corpuses instantiated with the OPUS object - here 'Europarl' and 'ParaCrawl'
opus_corpus = opus.load_as_txt()
# load subset of downloaded corpuses
opus_corpus = opus.load_as_txt(['Europarl'])
# FileNotFound error - 'OpenSubtitles' has not been instantiated with the OPUS object
opus_corpus = opus.load_as_txt(['OpenSubtitles'])
```

Fetch available OPUS corpuses that are accepted as arguments to OPUS() and load_as_txt().

```python
from danlp.datasets import OPUS

opus = OPUS()
available_corpuses = opus.valid_corpuses() # list(str)
# specify all available corpuses for download
opus = OPUS(available_corpuses, verbose=True)
# download and load all corpuses
opus_corpus = opus.load_as_txt()
# or
opus_corpus = opus.load_as_txt(available_corpuses)
```

#### WordSim-353
The WordSim-353 dataset [(Finkelstein et al. 2002)](http://www.cs.technion.ac.il/~gabr/papers/tois_context.pdf)
contains word pairs annotated with a similarity score (1-10). It is common to use it to do intrinsic evaluations
on word embeddings to test for syntactic or semantic relationships between words. The dataset has been
[translated to Danish](https://github.com/fnielsen/dasem/tree/master/dasem/data/wordsim353-da) by Finn Aarup Nielsen.

## 🎓 References
- Xiaoman Pan, Boliang Zhang, Jonathan May, Joel Nothman, Kevin Knight and Heng Ji. 2017. [Cross-lingual Name Tagging and Linking for 282 Languages](https://aclweb.org/anthology/P17-1178). In **ACL**.
- Lev Finkelstein, Evgeniy Gabrilovich, Yossi Matias, Ehud Rivlin, Zach Solan, Gadi Wolfman, and Eytan Ruppin. 2002. [Placing Search in Context: The Concept Revisited](http://www.cs.technion.ac.il/~gabr/papers/tois_context.pdf). In  **ACM TOIS**.
- Matthias T. Buch-Kromann, Line Mikkelsen, and Stine Kern Lynge. 2003. "Danish dependency treebank". In **TLT**.
