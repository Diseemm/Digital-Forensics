Digital Forensics Labwork 5 Report
=====

## Introduction

### What is Digital Forensics

**Digital forensics** (sometimes known as digital forensic science) is a branch of forensic science encompassing the recovery and investigation of material found in digital devices, often in relation to computer crime. In this document, descriptions and examples will be provided to analyze Digital Forensics in Images Processing.

### Techniques in detecting images tampering

A few techniques can be named such as:

1. Re-sampling.
2. Double JPEG Compression.
3. Luminance Non-linearities.
4. Signal to Noise Ratio.

### The importance

Digital Forensics helps identifying direct evidence of a crime, digital forensics can be used to attribute evidence to specific suspects, confirm alibis or statements, determine intent, identify sources (for example, in copyright cases), or authenticate documents.

## Methods

### Re-sampling

Re-sampling an image is required considering the scenario when digital fogery is created by splicing multiples images together. Though re-sampling is imperceptible, specific correlations which represent evidence of tampering are detected in re-sampled images.

### Double JPEG Compression

Tampering digital images requires editing software like Adobe Photoshop. In a JPEG image, any editing is carried out undergoes re-compression. Detecting evidence of double JPEG compression may provide useful information on revealing traces of images tampered or fabricated manipulation.

### Luminance Non-linearities

Mordern imaging devices normally would be able to enhance images' quality via some parameters of Luminance Non-linearities, which depends on cameras or scenes. Since images can be taken by different conditions, we can use tools to detect luminance non-linearities that also introduce some special artifacts

### Signal to Noise Ratio

Image processing or digital compression produces noices to images and these amount can vary between images. Detection of noices in multiple spliced images or variations in the signal to noise ratio (SNR) can reveal traces of tampering. 

#### References

1. Wikipedia: Digital Forensics.
2. Alin C. Popescu, Hany Farid, '*Statistical Tools for Digital Forensics*'
3. Babak Mahdian, Stanislav Saic, '*Image Tampering Detection Using Methods Based on JPEG Compression Artifacts: A Real-Life Experiment*'
4. Bin Li, Hu Luo, Haoxin Zhang, Shunquan Tan, Zhongzhou Ji, '*A multi-branch convolutional neural network for detecting double JPEG compression*'
5. Pankaj Malviya, Ruchira Naskar, '*Digital Forensic Technique for Double Compression based JPEG Forgery Detection*'


