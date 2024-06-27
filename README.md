<h1 align="center">
  Synthetic Biology Applications of Deep Learning for ADAPT in SC Summer 2024
</h1>

<span align="center">
  
  ![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
  ![image](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
  ![image](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
  ![image](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
  
</span>

A project focused on designing improved RNA riboswitches using machine learning as a guide. The work in this repository
seeks to explore the effectiveness of this methodology, as well as to demonstrate the particular effectiveness of training
on RNA sequences themselves as opposed to previous attempts to train on derived thermodynamic parameters. Also highlighted
is the impact of data size on the efficacy of these models.

Project Structure & Notes
-------------------------
The project consists of a Jupytr Notebook that compares various machine learning models trained on different data sets
and types.
```
dsci-research-for-ADAPT-in-SC
├── data
│   ├── comparison.csv
│   ├── mit-data.csv                       # Angenent-Mari et al.
│   └── Sensor-Data-Update-9-11-23.csv     # WU Fernandez Lab
├── data_prep.py                           # Data preparation utilities
├── MLPforSensorData.ipynb
├── presentation
│   ├── assets
│   │   └── # images for presentations
│   ├── poster
│   └── SURE Presentation 2024
├── Sequence vs Thermodynamic.ipynb
└── visualization
    └── visualization.ipynb                # Code for graphs
```
NOTE: The data from Angenent-Mari et al. is provided split up, as it is too large to store as one file. It is recommended to
combine these into a single file, `mit-data.csv` to reproduce the results of the Jupytr notebook, or instead to download it directly
from [their direct download link](https://drive.google.com/file/d/1t_OXvtW-hEGRt3-mgNlyBKHBqro2Z572/view?usp=sharing)

Contributors
------------
- James Craven             | [github.com](https://github.com/4jamesccraven) 
- Matthew Lindsey          | [github.com](https://github.com/MatthewLindsey75)
- Kristen Abernathy, Ph.D. | [winthrop.edu](https://www.winthrop.edu/cas/faculty/abernathy-kristen.aspx) | [github.com](https://github.com/kabernathy)
- Zachary Abernathy, Ph.D. | [winthrop.edu](https://www.winthrop.edu/cas/faculty/abernathy-zachary.aspx) | [github.com](https://github.com/zabernathy)
- Timea Fernandez, Ph.D.   | [winthrop.edu](https://www.winthrop.edu/cas/faculty/fernandez-timea.aspx)

References
----------
- [Tuning the Performance of Synthetic Riboswitches using ML (2019)](https://pubs.acs.org/doi/pdf/10.1021/acssynbio.8b00207), Groher et al.
- [A deep learning approach to programmable RNA switches (2020)](https://www.nature.com/articles/s41467-020-18677-1), Angenent-Mari et al. | [GitHub](https://github.com/lrsoenksen/CL_RNA_SynthBio/tree/master)
- [Sequence-to-function deep learning frameworks for engineered riboregulators (2020)](https://www.nature.com/articles/s41467-020-18676-2#MOESM1), Valeri et al.

Acknowledgements
----------------
This work was supported primarily by the National Science Foundation EPSCoR Program under NSF Award #OIA-2242812. Any Opinions, findings and conclusions
or recommendations expressed in this material are those of the author(s) and do not necessarily reflect those of the National Science Foundation.

Licensing scheme adapted from [this comment](https://github.com/github/choosealicense.com/issues/242#issuecomment-221325538).
