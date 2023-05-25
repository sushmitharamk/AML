# AML
This project aims to recognize actions using vision transformers(TimeSformer). Dataset used is HMDB_simp.
the model uses AutoFeatureExtactor to extract features from the videos.
Hugging face trainer api to load the data into the model.

create_dataset.py file takes the images in HMDB_simp and converts them into videos.

Note: It takes nearly 3 to 4hrs to load and save the videos.
