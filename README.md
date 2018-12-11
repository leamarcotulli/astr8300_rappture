Overview
========

astr8300_rappture is a sample package for Astr8300 rappture projects

Installation
------------

You will need a computer with [rappture](https://nanohub.org/infrastructure/rappture/) installed.  Type the following:

* git clone http://github.com/leamarcotulli/astr8300_rappture_lea_BS.git
* cd astr8300_rappture
* rappture

Authors
-------

- Bradley S. Meyer <mbradle@clemson.edu>

Bahcall-Soneira models tool
===========================
This tool has been developed for the **final project** for the *Galactic Astronomy* class, taught by prof. Bradley Meyer in Fall 2018, Clemson University.

Istructions
------------

1. Make an account on Amazon AWS
2. From the EC2 dashboard, click on 'AMIs' and, under the public images, launch the 'webnucleo' one (this instance will have rappture installed.
3. Connect to the instance with "ssh -i "/path/to/key.pem" -X ubuntu@..."
   * git clone http://github.com/leamarcotulli/astr8300_rappture_lea_BS.git
   * cd astr8300_rappture/Final_Project
   * export PATH=$PATH:/usr/local/rappture/bin/
   * rappture

Description of the tool
=========================
<p>This tool is based on the paper from **Bachall and Soneira** ([1980](http://adsabs.harvard.edu/abs/1980ApJS...44...73B)).</p>
<p>The goal of this rappture tool is to compute the distribution of stars of absolute magnitude M as a function of their distance from the Galactic Center (x) and their height above the plane (z).</p>
<p>Below I will highlight the assumption behind the calculation. For a detailed description of the model, I will refer the user to the actual [paper](http://adsabs.harvard.edu/abs/1980ApJS...44...73B).</p>

The model
-----------
The luminosity function of disk stars (which is the number of stars per pc<sup>3</sup> per absolute visual magnitude, M<sub>V</sub> is taken from the analytic function derived in Tremaine, Ostriker and Spitzer ([1975](http://adsabs.harvard.edu/abs/1975ApJ...196..407T)):

![image](http://www.sciweavers.org/download/Tex2Img_1544553247.jpg)

<p>with n<sub>*</sub>=4.03x10<sup>-3</sup>, M<sup>*</sup>=+1.28, M<sub>b</sub>=-6, M<sub>d</sub>=+19, &alpha;=0.74, &beta;=0.04, 1/&delta;=3.40. </p>

see if it stays   

