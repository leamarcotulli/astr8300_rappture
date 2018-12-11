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
This tool is based on the paper from **Bachall and Soneira** ([1980](http://adsabs.harvard.edu/abs/1980ApJS...44...73B)). 
The goal of this rappture tool is to compute the distribution of stars of absolute magnitude M as a function of x (distance from the Galactic Center) and z (height above the plane). 
Below I will highlight the assumption behind the calculation. For a more detailed description, I will refer the user to the actual [paper](http://adsabs.harvard.edu/abs/1980ApJS...44...73B).



Let's try some html stuff
=========================
The following text is taken from [Wikipedia](https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law):

<p style="color:Tomato;">"The <b>Stefan–Boltzmann law</b> describes the power radiated from a <i>black body</i> in terms of its <b><i>temperature</i></b>. The law states that <i><ins>the total energy radiated per unit surface area of a black body across all wavelengths per unit time is directly proportional to the fourth power of the black body's thermodynamic temperature T</ins></i>:</p>
  <p><i>j</i><sup> &star;</sup>=&sigma;<i>T</i><sup>4</sup></p>
 <p>The constant of proportionality σ, called the Stefan–Boltzmann constant, is derived from other known physical constants. The value of the constant is:</p>
   <p>&sigma;=2&pi;<sup>5</sup><i>k</i><sup>4</sup>/15<i>c</i><sup>2</sup><i>h</i><sup>3</sup>=5.670373x10<sup>-8</sup> W m<sup>-2</sup> K<sup>-4</sup>"</p>
  
 
