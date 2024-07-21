#text
import matplotlib.pyplot as plt
#from matplotlib import transforms
from matplotlib.transforms import offset_copy

def add_rainbow_text(x,y,ls,lc,ax = None, **kw):
    """
    Take a list of strings ``ls`` and colors ``lc`` and place them next to each
    other, with text ls[i] being shown in color lc[i].

    This example shows how to do both vertical and horizontal text, and will
    pass all keyword arguments to plt.text, so you can set the font size,
    family, etc.
    """
#     t = plt.gca().transData
#     fig = plt.gcf()
 
    if ax == None:
        ax = plt.gca()

    t = ax.transAxes # use axes coords
    fig =plt.gcf()
    #plt.gcf().canvas.draw()
    
    #horizontal version
    for s,c in zip(ls,lc):
        
        text = plt.text(x,y,s+" ",color=c, transform=t, **kw)
        text.draw(fig.canvas.get_renderer())
        
        ex = text.get_window_extent()

        #current_x = text_extent.x1 + space_width - fig.bbox.width / fig.dpi / 72
        # fixed_offset=20
        # t = offset_copy(text._transform, x=fixed_offset, units='dots')
        print (ex.width)
        t = offset_copy(text.get_transform(), x=ex.width / 2 , units='dots')

