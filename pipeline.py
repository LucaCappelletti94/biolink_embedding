import yaml
import requests
import pandas as pd
from tqdm.auto import tqdm
from grape.datasets import get_okapi_tfidf_weighted_textual_embedding

# Set of the keys to keep
category_keys = ("subsets", "types", "slots", "classes")

# Retrieve the biolink yaml file.
# Do note that there also exists a JSON version, but
# it does not come with all of the definitions or descriptions
data = yaml.safe_load(requests.get(
    "https://raw.githubusercontent.com/biolink/biolink-model/master/biolink-model.yaml"
).text)

# We retrieve the version of the current data
version = data["version"]

# We convert the data into the DataFrame format we need
df = pd.DataFrame([
    {
        "category": category.replace("_", " "),
        "description": (
            " "
            if attributes.get("description", " ") is None
            else attributes.get("description", " ")
        ).replace(",", " ").replace("\n", " ").replace("\r", " ")
    }
    for group, group_data in data.items()
    if group in category_keys
    for category, attributes in group_data.items()
])

# We set the path for the data
path = f"biolink_{version}.csv"

# We save the data as a CSV
df.to_csv(path, index=False)

# We start to build the BERT-based embeddings
for model_name in tqdm(
    (
        "bert-base-uncased",
        "allenai/scibert_scivocab_uncased",
        "allenai/specter"
    ),
    desc="Building embeddings",
    leave=False,
    dynamic_ncols=True
):
    # We get the name of the model so we can write it in the file
    adjusted_model_name = model_name.replace("/", "_").replace("-", "_")
    
    # We build the target path
    target_path = f"biolink_{version}_{adjusted_model_name}.csv.gz"
    
    # We compute the BM25-weighted BERT-based embedding
    pd.DataFrame(
        get_okapi_tfidf_weighted_textual_embedding(
            path=path,
            separator=",",
            header=True,
            pretrained_model_name_or_path=model_name
        ),
        index=df.category
    ).to_csv(target_path)