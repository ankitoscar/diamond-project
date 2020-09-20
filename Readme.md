# Diamond Project

This project is an end-to-end implementation of a ML model used to predict the prize of a diamond based on its various features.

## Description

Diamond is highly valued in our society. It is seen as a sign of nobility. However, we don't know more about different features of diamond. We only know about carat, but not in depth. Hence let's discuss about the different features of diamond used in our project:

1. Carat : 1 carat is equal to 200mg. Further, 1 carat is divided into 100 division.
![carat.jpg](https://4cs.gia.edu/wp-content/uploads/2017/05/Hero-Carat-Weight_700x394.jpg)
2. Cut : Cut refers the way the diamond is shaped. It has a large impact of the brilliance(shining).
![cut.jpg](https://www.brilliance.com/sites/default/files/images/brilliance-diamond-cut-chart.jpg)
3. Clarity : It refers to the amount of blemishes, different types of clarity :
    1. Flawless (FL) No inclusions and no blemishes visible under 10x magnification
    2. Internally Flawless (IF) No inclusions visible under 10x magnification
    3. Very, Very Slightly Included (VVS1 and VVS2) Inclusions so slight they are difficult for a skilled grader to see under 10x magnification
    4. Very Slightly Included (VS1 and VS2) Inclusions are observed with effort under 10x magnification, but can be characterized as minor
    5. Slightly Included (SI1 and SI2) Inclusions are noticeable under 10x magnification
    6. Included (I1, I2, and I3) Inclusions are obvious under 10x magnification which may affect transparency and brilliance
![clarity.jpg](https://selectingadiamond.com/wp-content/uploads/2019/10/Diamond-Clarity.jpg)
In our dataset, we have only I1,IF,VS1,VS2,VVS1,VVS2,SI1 and SI2.
4. Colour : Colour actually means lack of colour in diamond. The used dataset has colours D-J (best to worst).
![colour.jpg](https://beyond4cs.com/wp-content/uploads/2019/02/diamond-color-chart-with-example-diamonds-of-each-alphabet.jpg)
5. Dimensions : The lenght, width and height of diamond(x,y and z respectively).
6. Depth and table : These two are related to dimension. Depth is the ratio of z with mean of x and y.
Depth  = z/mean(x,y). Table is width of diamond relative to its widest point.
![depth_and_table.jpg](https://www.diamonds.pro/wp-content/uploads/2019/02/diamond-depth-and-table.png)

Click [here](https://www.kaggle.com/shivam2503/diamonds/download) to download the dataset and see it first.


### Dependencies

The python version used in this project is 3.8.x.
* Python Libraries used in project:
    1. Pandas
    2. Numpy
    3. Scikit-Learn
    4. Pycountry
    5. Email-validator 

* The webpage is made using HTML, CSS and Flask framework. The Flask framework has the follwing packages:
    1. Flask-SQLAlchemy
    2. Flask-Inputs
    3. Flask-Login
    4. Flask-WTF



### Executing program

After installing all the dependencies, execute the run.py file and the site will open at [localhost:5000](localhost:5000). The home page of the website will open.

### Snippets from the website

Since this website was made for the hackathon ["Aye Aye Hackers"](https://organize.mlh.io/participants/events/4093-aye-aye-hackers), hence it has a pirate theme.


1. First page of the website
![](Screenshot(76).png)
2. Login Page 
![](Screenshot(77).png)
3. Home Page
![](Screenshot(78).png)
![](Screenshot(79).png)
4. Update Info page
![](Screenshot(84).png)
![](Screenshot(85).png)
5. Result page
![](Screenshot(81).png)
6. Creators' Info
![](Screenshot(82).png)
## Authors

Contributor names and contact info

Biplov Pokhrel 

GitHub : [@pbplop29](https://github.com/pbplop29)

Email : 

Siddharth Sharma

Github : [@pao0318](https://github.com/pao0318)

Email : sharma.siddharthspacex21@gmail.com

Tanishq Dubey

Github : [@tanishq12442](https://github.com/tanishq12442)

Email : tanishqdubey12442@gmail.com

Ankit Oscar Xalxo 

GitHub : [@ankitoscar](https://github.com/ankitoscar)

Email : ankitoscar911@gmail.com


## Version History
* 0.1
    * Initial Release


## Acknowledgments

* [Kaggle (for dataset)](https://kaggle.com)
* [Stack Overflow](https://stackoverflow.com)
* [GIA (for information regarding diamond's features)](https://4cs.gia.edu/)