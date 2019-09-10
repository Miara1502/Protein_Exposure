##https://www.google.com/search?client=ubuntu&hs=Byf&channel=fs&sxsrf=ACYBGNTmqXGBk-U3z2ZqLlMn-egSmtfW6A%3A1568108983867&ei=t3F3XbfGNMLjgwft9rLoDg&q=algorithme+de+Saff+et+Kuijlaars&oq=algorithme+de+Saff+et+Kuijlaars&gs_l=psy-ab.3...2785.6189..6339...3.0..0.70.552.11......0....1..gws-wiz.......35i304i39.HpSgAim22qA&ved=0ahUKEwj3_c6X_cXkAhXC8eAKHW27DO0Q4dUDCAs&uact=5

> cat ll.py
from math import asin
nx = 4; ny = 5
for x in range(nx):
    lon = 360 * ((x+0.5) / nx)
    for y in range(ny):                                                         
        midpt = (y+0.5) / ny                                                    
        lat = 180 * asin(2*((y+0.5)/ny-0.5))                                    
        print lon,lat                                                           
> python2.7 ll.py        
                                              
45.0 -166.91313924                                                              
45.0 -74.0730322921                                                             
45.0 0.0                                                                        
45.0 74.0730322921                                                              
45.0 166.91313924                                                               
135.0 -166.91313924                                                             
135.0 -74.0730322921                                                            
135.0 0.0                                                                       
135.0 74.0730322921                                                             
135.0 166.91313924                                                              
225.0 -166.91313924                                                             
225.0 -74.0730322921                                                            
225.0 0.0                                                                       
225.0 74.0730322921                                                             
225.0 166.91313924
315.0 -166.91313924
315.0 -74.0730322921
315.0 0.0
315.0 74.0730322921
