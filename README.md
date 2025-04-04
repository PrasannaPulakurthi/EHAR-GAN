# Enhancing Human Action Recognition with GAN-based Data Augmentation (EHAR-GAN) [[PDF]](https://prasannapulakurthi.github.io/papers/PDFs/2024_SPIE_EHAR-GAN.pdf)
Code for our **SPIE 2024** paper "**Enhancing human action recognition with GAN-based data augmentation**,"
by [Prasanna Reddy Pulakurthi](https://www.prasannapulakurthi.com/), [Celso M. de Melo](https://celsodemelo.net/), [Raghuveer Rao](https://ieeexplore.ieee.org/author/37281258600), and [Majid Rabbani](https://www.rit.edu/directory/mxreee-majid-rabbani).

The original RoCoG-v2 gesture recognition dataset can be found [here](https://www.cis.jhu.edu/~rocog/data/).

Our generated dataset can be found [here](https://drive.google.com/file/d/1BQeKY65za_sth9QytFmjmsxny9C2z4-E/view?usp=sharing). The results of all the experiments can be found [here](https://drive.google.com/file/d/1hGq0SXFiYJmUaaEMXkE4rDiyMyUPU21_/view?usp=sharing).

| Original Video | Motion Transfer to S01 | Motion Transfer to S02 | Motion Transfer to S03 | 
| :---: | :---: | :---: | :---: | 
|<img src="assets/real2real_ground/S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S01-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S02-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S03-S01_10m_ground_label1_start1803.gif"/> |
| Motion Transfer to S05 | Motion Transfer to S07 | Motion Transfer to S08 | Motion Transfer to S10 | 
|<img src="assets/real2real_ground/S05-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S07-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S08-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S10-S01_10m_ground_label1_start1803.gif"/> |

## Citation
Please consider citing our paper in your publications if it helps your research. The following is a BibTeX reference.
```bibtex
@inproceedings{10.1117/12.3021572,
author = {Prasanna Reddy Pulakurthi and Celso  M. De Melo and Raghuveer Rao and Majid Rabbani},
title = {{Enhancing human action recognition with GAN-based data augmentation}},
volume = {13035},
booktitle = {Synthetic Data for Artificial Intelligence and Machine Learning: Tools, Techniques, and Applications II},
editor = {Kimberly E. Manser and Christopher L. Howell and Raghuveer M. Rao and Celso De Melo},
organization = {International Society for Optics and Photonics},
publisher = {SPIE},
pages = {130350O},
keywords = {Human Action Recognition, Generative Adversarial Networks, Deep Neural Networks, Synthetic Data, Data Augmentation},
year = {2024},
doi = {10.1117/12.3021572},
URL = {https://doi.org/10.1117/12.3021572}
}
```
