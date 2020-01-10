# TB image preparation

The script in this repository can be used to prepare the data for the paper [Efficient Deep Network Architectures for Fast Chest X-Ray Tuberculosis Screening and Visualization](https://www.ncbi.nlm.nih.gov/pubmed/31000728).

You can download the raw dataset from kaggle [here](https://www.kaggle.com/kmader/pulmonary-chest-xray-abnormalities).

The images will be scaled-down to 512x512 and center-cropped to match the belarus dataset, you can find [here](https://github.com/frapa/tbcnn/tree/master/belarus).

## Dependencies

- Python 3.6+
- pipenv

Use `pipenv install` to install all further dependencies.

## Running

After downloading and extracting the large dataset from kaggle, you can run the script:

```bash
pipenv run python3 main.py --dataset-dir ~/Downloads/pulmonary-chest-xray-abnormalities
```
