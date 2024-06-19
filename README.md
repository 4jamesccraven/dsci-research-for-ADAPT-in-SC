<h1 align="center">
  Synthetic Biology Applications of Deep Learning for ADAPT in SC Summer 2024
</h1>
<span align="center">
  
  ![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
  ![image](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
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
│   ├── comparison.csv                   # results of this study
│   ├── mit-data.csv                     # data from Angenent-Mari et al.
│   └── Sensor-Data-Update-9-11-23.csv   # data from Dr. Fernandez at WU
│
├── data_prep.py                         # data preparation utilities
└── Sequence vs Thermodynamic.ipynb    
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

Acknowledgements
----------------
This project is supported by ADAPT in SC, an EPSCoR RII grant (#2242812) from
the National Science Foundation.
