#draw path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import rainbow_text
import os

def draw_scanpath_with_fixation_words(img, xs, ys, ts, savefilename,bbox, word_list, fix_word_list):
    fig, ax = plt.subplots()
    ax.imshow(img)

    # draw bounding box
    if bbox is not None:
        rect = Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], 
            alpha=0.5, edgecolor='#0004ff', facecolor='none', linewidth=5)
        ax.add_patch(rect)
      
    # set radius based on duration
    cir_rad_min, cir_rad_max = 5, 20
    min_T, max_T = np.min(ts), np.max(ts)
    rad_per_T = (cir_rad_max - cir_rad_min) / (float(max_T - min_T)+1.e-5)# to prevent fload division by zero

    # draw arrow
    for i in range(len(xs)):
        if i > 0:
            plt.arrow(xs[i - 1], ys[i - 1], xs[i] - xs[i - 1],
                      ys[i] - ys[i - 1], width=3, color='yellow', alpha=0.5)

       
    colors = ['#d62728', '#ff7f0e', '#e377c2', '#bcbd22', '#2ca02c', '#17becf', '#1f77b4', '#0004ff']


    # draw circles
    for i in range(len(xs)):
        
        # find colors based on words
        current_word_index = fix_word_list[i]
        
        #check current word index
        if current_word_index == -99 or current_word_index == 99:
            curent_word = None
            current_color = 'white'
        else:
            curent_word = word_list[current_word_index] 
            current_color = colors[current_word_index] 
        
        # add circle with current color
        cir_rad = int(50 + rad_per_T * (ts[i] - min_T))
        circle = plt.Circle((xs[i], ys[i]),
                            radius=cir_rad,
                            edgecolor='yellow',
                            facecolor= current_color,
                            alpha=0.7)
                 
        
        ax.add_patch(circle)
        plt.annotate("{}".format(i+1), xy=(xs[i], ys[i]+3), fontsize=10, ha="center", va="center")

    ax.axis('off')
    print (word_list)
    rainbow_text.add_rainbow_text(0, 1.05, word_list, colors, size=18)
    
    # save the figure, not visualize it if a file name was provided
    if savefilename != None:
        directory = os.path.dirname(savefilename)
        if not os.path.exists(directory):
            # Create a new directory because it does not exist 
            os.makedirs(directory)
            print(f"The new directory {directory} is created!")
        fig.savefig(savefilename, bbox_inches='tight')
        print(f'files saved {i+1}', end='\r')
        plt.close(fig)
    #else:
    plt.show()

