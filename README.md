# Biolink BM25-weighted BERT-based embedding
Pipeline to compute Okapi BM25-weighted BERT-based embedding of textual descriptions associated to the [Biolink model](https://biolink.github.io/biolink-model/).

## What is Biolink?
A high level datamodel of biological entities (genes, diseases, phenotypes, pathways, individuals, substances, etc) and their associations. [Biolink](https://biolink.github.io/biolink-model/) Model is designed as a way of standardizing types and relational structures in knowledge graphs (KGs), where the KG may be either a property graph or RDF triple store.

This repository also hosts the resulting embedding for biolink version `3.1.1`.

## What is the Okapi BM25 ranking method
Okapi BM25 is a ranking function that is used to determine the relevance of a document to a given query. It is a probabilistic model that is based on the notion that a good ranking function should rank highly relevant documents higher than less relevant documents. BM25 stands for Best Matching 25, which refers to the fact that it was developed as an improvement over the Okapi Best Matching algorithm, which was the best performing ranking algorithm at the time.

BM25 works by first analyzing the query and the documents that it is trying to rank, and then assigning a score to each document based on how well it matches the query. This score is then used to determine the relevance of the document to the query. In general, the higher the score, the more relevant the document is considered to be.

There are several factors that go into the calculation of the BM25 score, including the term frequency (TF) and inverse document frequency (IDF) of the words in the query and the document, as well as the length of the document and the average length of documents in the collection. These factors are combined using a set of parameters that can be tuned to optimize the performance of the ranking function.

Overall, BM25 is widely used in information retrieval applications, such as search engines, because of its ability to effectively rank documents based on their relevance to a given query.

## Available precomputed embedding
The Biolink ontological model is a powerful tool for representing and organizing knowledge about the biomedical domain. In this section, we make available an Okapi BM25-weighted embedding of the descriptions of the elements in the Biolink model, based on BERT, SciBERT, and Specter natural language processing pre-trained models. These embeddings are created using the huggingface BERT tokenizers, which allow us to generate high-quality representations of the text in the Biolink descriptions. These embeddings can be used in a variety of applications, such as text-based search and retrieval, natural language processing, and machine learning.

### BERT
BERT (Bidirectional Encoder Representations from Transformers) is a state-of-the-art language processing model that is trained to understand the nuances and context of words in a sentence. It is a transformer-based model that uses self-attention mechanisms to process input sequences and generate contextualized word representations. BERT is trained on a large corpus of text data and can be fine-tuned for specific tasks such as language translation or text classification. It has been shown to outperform many previous models on a wide range of natural language processing tasks.

You can download the BERT embedding of Biolink by running:

```python
import pandas as pd

biolink_bert = pd.read_csv("")
```

### SciBERT
SciBERT is a language model that is based on the BERT model and is specifically trained on scientific text. It was trained on a large corpus of scientific publications in various fields including biology, chemistry, physics, and computer science. This specialized training allows SciBERT to better understand the technical vocabulary and complex sentence structures found in scientific texts. It can be used for tasks such as scientific document classification and information extraction. Like BERT, SciBERT can be fine-tuned for specific tasks and has been shown to outperform other models on scientific text processing tasks.

You can download the SciBERT embedding of Biolink by running:

```python
import pandas as pd

biolink_scibert = pd.read_csv("")
```

### Specter
SPECTER is a pre-trained language model to generate document-level embedding of documents. It is pre-trained on a powerful signal of document-level relatedness: the citation graph. Unlike pretrained language models, SPECTER can be easily applied to downstream applications without task-specific fine-tuning.

You can download the Specter embedding of Biolink by running:

```python
import pandas as pd

biolink_specter = pd.read_csv("")
```


## Re-computing the embedding
In this section, we provide a step-by-step guide for re-computing the Okapi BM25-weighted embeddings of the Biolink ontological model elements descriptions. All that is needed to re-compute the embeddings is to clone our GitHub repository:

```bash
git clone https://github.com/LucaCappelletti94/biolink_embedding
```

Then execute the python file therein, `pipeline.py`:

```bash
python3 pipeline.py
```

This script provides all the necessary code and instructions for re-creating the embeddings using the BERT, SciBERT, and Specter pre-trained models and the huggingface BERT tokenizers. By following the steps in the script, you can easily generate your own version of the embeddings, tailored to your specific needs and applications.

## Citing this work
If you have found these datasets useful, please do cite:

```bib
@software{cappellettiBiolink2022,
    author = {Cappelletti, Luca},
    month = {12},
    title = {{BM25-weighted BERT-based embedding of BioLink}},
    url = {https://github.com/LucaCappelletti94/biolink_embedding},
    version = {1.0.0},
    year = {2022}
}
```