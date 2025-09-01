# <p align="center">Enhancing Human Action Recognition with GAN-based Data Augmentation (EHAR-GAN)</p>

<p align="center">
  <a href="https://doi.org/10.1117/12.3021572"><img src="https://img.shields.io/badge/SPIE-2024-yellow.svg" alt="SPIE 2024"></a>
  <a href="https://prasannapulakurthi.github.io/papers/PDFs/2024_SPIE_EHAR-GAN.pdf"><img src="https://img.shields.io/badge/Preprint-2024-b31b1b.svg" alt="Preprint"></a>
  <a href="https://huggingface.co/datasets/prasannareddyp/Syn-RoCoG-v2"><img src="https://img.shields.io/badge/HF-Dataset-white.svg" alt="Dataset"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache-2.0"></a>
</p>

Code for our **2024** paper "**Enhancing human action recognition with GAN-based data augmentation**,"
by [Prasanna Reddy Pulakurthi](https://www.prasannapulakurthi.com/), [Celso M. de Melo](https://celsodemelo.net/), [Raghuveer Rao](https://ieeexplore.ieee.org/author/37281258600), and [Majid Rabbani](https://www.rit.edu/directory/mxreee-majid-rabbani). [[PDF]](https://prasannapulakurthi.github.io/papers/PDFs/2024_SPIE_EHAR-GAN.pdf) [[Dataset]](https://huggingface.co/datasets/prasannareddyp/Syn-RoCoG-v2)

**Keywords:** Human Action Recognition (HAR), Generative Adversarial Network(GAN), Deep Neural Network (DNN), Synthetic Data, Data Augmentation.

## Overview
**EHAR-GAN** proposes a GAN-based framework for **enhancing human action recognition (HAR)** by generating synthetic gesture videos that vary both **motion** and **appearance**.  
By augmenting a small-sized real dataset with targeted motion transfer and style variation, we significantly improve HAR performance without requiring complex motion capture setups.

## Datasets

- RoCoG-v2 - [Original RoCoG-v2 Dataset](https://www.cis.jhu.edu/~rocog/data/)
- Syn-RoCoG-v2 - [Our Generated Synthetic Dataset](https://drive.google.com/file/d/1BQeKY65za_sth9QytFmjmsxny9C2z4-E/view?usp=sharing)

| Original Video | Motion Transfer to S01 | Motion Transfer to S02 | Motion Transfer to S03 | 
| :---: | :---: | :---: | :---: | 
|<img src="assets/real2real_ground/S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S01-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S02-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S03-S01_10m_ground_label1_start1803.gif"/> |
| Motion Transfer to S05 | Motion Transfer to S07 | Motion Transfer to S08 | Motion Transfer to S10 | 
|<img src="assets/real2real_ground/S05-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S07-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S08-S01_10m_ground_label1_start1803.gif"/> | <img src="assets/real2real_ground/S10-S01_10m_ground_label1_start1803.gif"/> |

## Results
- [Experiment Results](https://drive.google.com/file/d/1hGq0SXFiYJmUaaEMXkE4rDiyMyUPU21_/view?usp=sharing)

## Citation
Please consider citing our paper in your publications if it helps your research. The following is a BibTeX reference.
```bibtex
@inproceedings{pulakurthi2024enhancing,
  title={Enhancing human action recognition with GAN-based data augmentation},
  author={Pulakurthi, Prasanna Reddy and De Melo, Celso M and Rao, Raghuveer and Rabbani, Majid},
  booktitle={Synthetic Data for Artificial Intelligence and Machine Learning: Tools, Techniques, and Applications II},
  volume={13035},
  pages={194--204},
  year={2024},
  organization={SPIE}
}
```
