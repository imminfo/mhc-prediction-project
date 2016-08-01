# MHCPred

MHC:peptide binding prediction.

## Algorithm

Gradient Boosting Machine is used for the prediction, with XGBoost library.
Jupyter notebooks for preparing the dataset and training the model are in the `notebooks` directory.

## Dataset

Dataset has been downloaded from the [IEDB website](http://tools.iedb.org/mhci/download/).
Copy of this dataset resides in the `data` directory.

## Web application

A crude sketch of web application can be found in the `webapp` directory.

## References

* [Pan-specific MHC class I predictors: a benchmark of HLA class I pan-specific prediction methods][zhang2009]
* [Predicting Peptide-MHC Binding Affinities With Imputed Training Data][rubinsteyn2016]
* [Gapped sequence alignment using artificial neural networks: application to the MHC class I system][andreatta2016]
* [NetMHC Server][netmhc]
* [MHCflurry Repository][mhcflurry]
* [Python Interface to Immunology Datasets][pepdata]

[zhang2009]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2638932/
[rubinsteyn2016]: http://biorxiv.org/content/early/2016/05/23/054775
[andreatta2016]: http://www.cbs.dtu.dk/services/NetMHC/26515819.pdf
[netmhc]: http://www.cbs.dtu.dk/services/NetMHC/
[mhcflurry]: https://github.com/hammerlab/mhcflurry
[pepdata]: https://github.com/hammerlab/pepdata
