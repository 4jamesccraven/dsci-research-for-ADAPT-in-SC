<h1 align="center">
  Synthetic Biology Applications of Deep Learning for ADAPT in SC Summer 2024
</h1>

<span align="center">
  
  ![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
  ![image](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
  ![image](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
  ![image](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
  
</span>

In this project, we seek to understand how we can utilize machine learning (ML) to inform the
design of biosensors to emit a strong fluorescence in the presence of dopamine. Dopamine is a
neurotransmitter and plays a role in a variety of functions such as memory, learning, and reward
systems. Detecting dopamine levels could help with diagnosing addiction, mental illness, and
neurodegenerative disorders. We develop a framework for one-hot encoding nucleotide
sequences for training ML models, create a data preprocessing pipeline to pad sequences and
normalize output values, and construct neural net model architecture for training on both
sequence and numerical data. Using a published toehold switch dataset along with a ribosensor
dataset provided by Dr. Timea Fernandez’s lab, we explore the accuracy of several different
regression models in predicting biosensor effectiveness by training on both nucleotide sequence
data and calculated thermodynamic parameter data. We find that a neural network model,
specifically a multilayer perceptron, typically outperforms other regression models such as linear
regression, random forests, and support vector machines in both datasets, and that training on
sequence data appears to be more predictive than training on thermodynamic parameter data. We
also suggest potential directions to pursue transfer learning between the two datasets.

Project Structure & Notes
-------------------------
The project consists of some Jupyter notebooks that compare various machine learning models trained on different data sets
and types.
```
# Abridged repository structure
📂 dsci-research-for-ADAPT-in-SC
├── 📂 data
├── 📄 data_prep.py                        # Utilities for data cleaning
├── 📄 MLPforSensorData.ipynb              # Tensorflow-based MLP based on the MIT workflow
├── 📄 'Sequence vs Thermodynamic.ipynb'   # Comparisons of model performance based on different data types
└── 📄 visualization.ipynb                 # Visualizations used in presentations etc.
```
NOTE: The data from Angenent-Mari et al. is provided split up, as it is too large to store as one file. It is recommended to
combine these into a single file, `mit-data.csv` to reproduce the results of the Jupytr notebook, or instead to download it directly
from [their direct download link](https://drive.google.com/file/d/1t_OXvtW-hEGRt3-mgNlyBKHBqro2Z572/view?usp=sharing)

If using bash, running this one-liner in the data directory will also produce the file you need:
```
( head -n 1 mit-data-1.csv && tail -n +2 mit-data-*.csv ) > mit-data.csv
```

Contributors
------------
| Name                     | wintrhop.edu                                                          | GitHub                                        |
|--------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| James Craven             |                                                                       | [Link ↗](https://github.com/4jamesccraven)    |
| Matthew Lindsey          |                                                                       | [Link ↗](https://github.com/MatthewLindsey75) |
| Kristen Abernathy, Ph.D. | [Link ↗](https://www.winthrop.edu/cas/faculty/abernathy-kristen.aspx) | [Link ↗](https://github.com/kabernathy)       |
| Zachary Abernathy, Ph.D. | [Link ↗](https://www.winthrop.edu/cas/faculty/abernathy-zachary.aspx) | [Link ↗](https://github.com/zabernathy)       |
| Timea Fernandez, Ph.D.   | [Link ↗](https://www.winthrop.edu/cas/faculty/fernandez-timea.aspx)   |                                               |

References
----------
- [Tuning the Performance of Synthetic Riboswitches using ML (2019)](https://pubs.acs.org/doi/pdf/10.1021/acssynbio.8b00207), Groher et al.
- [A deep learning approach to programmable RNA switches (2020)](https://www.nature.com/articles/s41467-020-18677-1), Angenent-Mari et al. | [GitHub](https://github.com/lrsoenksen/CL_RNA_SynthBio/tree/master)
- [Sequence-to-function deep learning frameworks for engineered riboregulators (2020)](https://www.nature.com/articles/s41467-020-18676-2#MOESM1), Valeri et al.
- [Scikit-learn: Machine Learning in Python (2011)](https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html), Pedregosa et al.

Acknowledgements
----------------
This work was supported primarily by the National Science Foundation EPSCoR Program under NSF Award #OIA-2242812. Any Opinions, findings and conclusions
or recommendations expressed in this material are those of the author(s) and do not necessarily reflect those of the National Science Foundation.
