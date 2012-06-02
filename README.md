## Canvas - a quick and dirty interface to matplotlib

I do not know about you but I find matplotlib fanatstic but overwhelming. I can never remember its syntax, yet I find myself often repeating the same boilerplate code.

This simple library is not meant to be general but it allows me to produce the quick and dirty plots I often need.

`canvas.py` exposes a single object, `Canvas`, which has methods `plot`,`hist`,`errorbar`,`ellipses`,`imshow`, and `save`. These methods can be piped to overlap diffent types of plots. For example:

    >>> from random import gauss
    >>> from math import sin, cos
    >>> from canvas import Canvas

    >>> gaussian = [gauss(0,1) for i in range(1000)]
    >>> Canvas('My First Image').hist(gaussian).save('img1.png')

hist data is an array of numbers

    >>> parabole = [(x,x*x) for x in range(0,20)]
    >>> Canvas('My Second Image').plot(parabole).save('img2.png')

plot data is an array of 2-tuples, (x,y)

    >>> points = [(x,x+gauss(0,1),0.5) for x in range(20)]
    >>> Canvas('My Third Image').errorbar(points).save('img3.png')

errorbar data is an array of 3-tuples, (x,y,dy)

    >>> blobs = [(gauss(0,1),gauss(0,1),0.05,0.05) for i in range(100)]
    >>> Canvas('My Fourth Image').ellipses(blobs).save('img4.png')

ellipses data is an arrat of 4-tuples, (x,y,dx,dy)

    >>> waves = [[sin(0.1*x)*cos(0.1*x*y) for x in range(20)] for y in range(20)]
    >>> Canvas('My Fifth Image').imshow(waves).save('img5.png')

imshow data is a square  2D array of numbers.

They can also be piped as:

    >>> Canvas(...).hist(...).hist(...).plot(...).save(...)

The names of the methods of the canvas objects are the same as the methods of the corresponding matplotlib axis object.

## Arguments

Here is the full signature:

    class Canvas(object):
         def __init__(self,title='title',xlab='x',ylab='y',xrange=None,yrange=None): ...
         def save(self,filename='plot.png'): ...
         def hist(self,data,bins=20,color='blue',legend=None): ...             
         def plot(self,data,color='blue',style='-',width=2,legend=None): ...
         def errorbar(self,data,color='black',marker='o',width=2,legend=None): ...
         def ellipses(self,data,color='blue',width=0.01,height=0.01): ...
         def imshow(self,data,interpolation='bilinear'): ...

## License

3-clause BSD license

## Dependencies

- numpy
- matplotlib

## Screenshots

[img1.png](https://github.com/mdipierro/canvas/blob/master/screenshots/img1.png)

[img2.png](https://github.com/mdipierro/canvas/blob/master/screenshots/img2.png)

[img3.png](https://github.com/mdipierro/canvas/blob/master/screenshots/img3.png)

[img4.png](https://github.com/mdipierro/canvas/blob/master/screenshots/img4.png)

[img5.png](https://github.com/mdipierro/canvas/blob/master/screenshots/img5.png)