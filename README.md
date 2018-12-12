Overview
========

astr8300_rappture is a sample package for Astr8300 rappture projects

Bahcall-Soneira models tool
===========================
This tool has been developed for the **final project** for the *Galactic Astronomy* class, taught by prof. Bradley Meyer in Fall 2018, Clemson University.

Istructions
------------
You will need a computer with [rappture](https://nanohub.org/infrastructure/rappture/) installed. If you do not have the software, follow the steps below. 

1. Make an account on Amazon AWS
2. From the EC2 dashboard, click on 'AMIs' and, under the public images, launch the 'webnucleo' one (this instance will have rappture installed).
3. Connect to the instance with "ssh -i "/path/to/key.pem" -X ubuntu@..."
   * git clone http://github.com/leamarcotulli/astr8300_rappture_lea_BS.git
   * cd astr8300_rappture/Final_Project
   * export PATH=$PATH:/usr/local/rappture/bin/
   * rappture

Description of the tool
=========================
This tool is based on the paper from **Bachall and Soneira** ([1980](http://adsabs.harvard.edu/abs/1980ApJS...44...73B)). <br />
The goal of this rappture tool is to compute the distribution of stars of absolute magnitude M as a function of their distance from the Galactic Center (x) and their height above the plane (z).<br />
Below, I will highlight the assumption behind the calculation. For a detailed description of the model, I refer the user to the actual [paper](http://adsabs.harvard.edu/abs/1980ApJS...44...73B).

The model
-----------
1. The **luminosity function** of disk stars (i.e. the number of stars per pc<sup>3</sup> per absolute visual magnitude, M<sub>V</sub>) is taken from the analytic function derived in Tremaine, Ostriker and Spitzer ([1975](http://adsabs.harvard.edu/abs/1975ApJ...196..407T)):

![image](https://github.com/leamarcotulli/astr8300_rappture_lea_BS/blob/master/Final_project/lum.jpg) (1)

<p>with n<sub>*</sub>=4.03x10<sup>-3</sup>, M<sup>*</sup>=+1.28, M<sub>b</sub>=-6, M<sub>d</sub>=+19, &alpha;=0.74, &beta;=0.04, 1/&delta;=3.40. </p>

2. The distribution of stars perpendicular to the plane of the Galaxies changes depending on their luminosity. Younger, more massive and brighter stars are found close to the plane, while older, less massive and fainter stars are more spread. The observed **scale height** (H) can be modeled by a trivial function which depends on M<sub>V</sub> (and well agrees with the observations): 

   ![image](https://github.com/leamarcotulli/astr8300_rappture_lea_BS/blob/master/Final_project/scale.jpg) (2)

3. The star density variation in the disk (&rho;<sub>d</sub><sup>&perp;</sup>) as a function of z can be approximated by:

   ![image](https://github.com/leamarcotulli/astr8300_rappture_lea_BS/blob/master/Final_project/rho_perp.jpg) (3)

4. The star density variation in the disk (&rho;<sub>d</sub><sup>&parallel;</sup>) as a function of x can be approximated by:

   ![image](https://github.com/leamarcotulli/astr8300_rappture_lea_BS/blob/master/Final_project/rho_parall.jpg) (4)
   
   where r<sub>0</sub> is the distance of the Sun for the Galactic Center (r<sub>0</sub> = 8 kpc) and h is the scale lenght that varies with morphological type (h=3.5 kpc, De Vaucouleurs and Pence, [1978](http://adsabs.harvard.edu/abs/1978AJ.....83.1163D)).


5. Therefore, **star density variation in the disk*** &rho;<sub>d</sub> is the product of 3. and 4.:

   ![image](https://github.com/leamarcotulli/astr8300_rappture_lea_BS/blob/master/Final_project/rho_d.jpg) (5)
 
6. For the **star density** in the **spheroidal component**, assuming it is made of stars with M<sub>V</sub> > 6, an expansion (valid for r/r<sub>e</sub>>0.2) is:

   ![image](https://github.com/leamarcotulli/astr8300_rappture_lea_BS/blob/master/Final_project/rho_s.jpg) (6)
   
   where b=7.669, C is the normalization constant (taken as 1 for simplicity), r<sub>e</sub> = r<sub>0</sub>/3 (De Vaucouleurs and Buta, [1978](http://adsabs.harvard.edu/abs/1978AJ.....83.1383D)).

7. Including the spheroidal component, the total distribution of stars in the galaxy is given by: 
 
   ![image](https://github.com/leamarcotulli/astr8300_rappture_lea_BS/blob/master/Final_project/rho_tot.jpg) (7)
   
 
The tool input parameters
-------------------------
The input parameters shown in the left of the rappture GUI are:
- Minimum (absolute visual) Magnitude (M<sub>MIN</sub>) and Maximum (absolute visual) Magnitude (M<sub>MAX</sub>). These will be used to compute the luminosity function and the scale height.
- Single (absolute visual) Magnitude. This is the magnitude for which you want to calculate the density and spatial distribution. 
- Npoints (integer). This is the number of points in which you want to divide the coordinate space: longitude (l), latitude (b) and distance from the Sun (R).

 
The tool outputs
---------------
After you press 'Simulate', the tool will produce six graphs:
- The luminosity function, calculated from M<sub>MIN</sub> to M<sub>MAX</sub> using equation (1)
- Scale height, calculated from M<sub>MIN</sub> to M<sub>MAX</sub> using equation (2)
- &rho;<sub>d</sub><sup>perp</sup> vs. z, calculated for stars of magnitude M using equation (3)
- &rho;<sub>d</sub><sup>parall</sup> vs. x, calculated for stars of magnitude M using equation (4)
- &rho;<sub>s</sub> vs. r, calculated for stars of magnitude M findinging the roots of equation (5) is M<6, or (7) is M>6
    
We note that for the last plot we find the root of equations (5) and (6) iterating for every M and every x over a range [-z<sub>MAX</sub>, +z<sub>MAX</sub>], where z<sub>MAX</sub>=1.e6 (arbitrary choice).

Authors
-------
- Lea Marcotulli <lmarcot@g.clemson.edu>
- Bradley S. Meyer <mbradle@clemson.edu>

