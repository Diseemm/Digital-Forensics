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

Re-sampling an image is required considering the scenario when digital fogery is created by splicing multiples images together. Though re-sampling is imperceptible, specific correlations which represent evidence of tampering are detected in re-sampled images. First, detect re-sampling correlations in 1-D signal, depending on the re-sampling rate might the process introduce correlations of varying degrees between neigboring samples, then generalize 2-D images. 

<center>![Screen Shot 2020-12-08 at 7 46 25 PM](https://user-images.githubusercontent.com/59855071/101490843-82a9ab80-3995-11eb-86ae-5ca6988c1965.png)</center>

Given a signal that has been re-sampled, The expectation/ maximization algorithm (EM) is developed to simultaneously estimate a set of periodic samples that are correlated to their neighbors, and the specific form of these correlations. The extension to 2-D images is relatively similar and EM algorithm can also be used with 2-D images for generalization.

<center>![Screen Shot 2020-12-08 at 8 15 08 PM](https://user-images.githubusercontent.com/59855071/101491181-0499d480-3996-11eb-86ed-39a8c08c1ef1.png)

**Figure:** Shown in the top row is an unadulterated image, and shown below are images re-sampled with different parameters. Shown in the middle column are the estimated probability maps that embody the spatial correlations in the image. The magnitude of the Fourier transforms of these maps are shown in the right-most column. Note that only the re-sampled images yield periodic maps.

![Screen Shot 2020-12-08 at 8 18 31 PM](https://user-images.githubusercontent.com/59855071/101491285-25622a00-3996-11eb-884a-74b6a0096033.png)</center>

### Double JPEG Compression

Tampering digital images requires editing software like Adobe Photoshop. In a JPEG image, any editing is carried out undergoes re-compression. Detecting evidence of double JPEG compression may provide useful information on revealing traces of images tampered or fabricated manipulation.

### Luminance Non-linearities

Mordern imaging devices normally would be able to enhance images' quality via some parameters of Luminance Non-linearities, which depends on cameras or scenes. Since images can be taken by different conditions, we can use tools from polyspectral analysis to detect luminance non-linearities that also introduce some special artifacts named correlations in the Fourier domain. 

<center>![Screen Shot 2020-12-08 at 7 03 41 PM](https://user-images.githubusercontent.com/59855071/101490314-bfc16e00-3994-11eb-8054-8dbf656ac234.png)

**Figure:** Shown in the top four panels are DCT coefficients for two frequencies ((1,1) and (2,2)),  and their histograms for single and double compressed JPEG images: (a) single JPEG compression with quality 75, (b) double JPEG compression with quality 85 followed by 75,  (c) single JPEG compression with quality 85,  (d) double JPEG compression with quality 75 followed by 85. Shown in panel (e) are the Fourier transforms of three zero-meaned histograms. Note the periodic artifacts introduced by double quantization (panels 2, 3)  reflected by the high frequency peaks in the Fourier transforms.

![Screen Shot 2020-12-08 at 7 11 00 PM](https://user-images.githubusercontent.com/59855071/101490397-db2c7900-3994-11eb-8d94-865bef580680.png)</center>

### Signal to Noise Ratio

Image processing or digital compression produces noices to images and these amount can vary between images. Detection of noices in multiple spliced images or variations in the signal to noise ratio (SNR) can reveal traces of tampering. 

<center>![Screen Shot 2020-12-08 at 6 54 20 PM](https://user-images.githubusercontent.com/59855071/101490094-74a75b00-3994-11eb-80c3-8f0650ede814.png)</center>

#### References

1. Wikipedia: Digital Forensics.
2. Alin C. Popescu, Hany Farid, '*Statistical Tools for Digital Forensics*'
3. Babak Mahdian, Stanislav Saic, '*Image Tampering Detection Using Methods Based on JPEG Compression Artifacts: A Real-Life Experiment*'
4. Bin Li, Hu Luo, Haoxin Zhang, Shunquan Tan, Zhongzhou Ji, '*A multi-branch convolutional neural network for detecting double JPEG compression*'
5. Pankaj Malviya, Ruchira Naskar, '*Digital Forensic Technique for Double Compression based JPEG Forgery Detection*'


