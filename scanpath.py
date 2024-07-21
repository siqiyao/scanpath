
# matplotlib inline

import json
from fixation_density import *
import draw_scanpath
import imageio
import os
import random

def scanpath(path_fixdata,path_images,path_save,sample_size):
            
#path_fixdata= 'refcocogaze_train_correct.json' 

    with open(path_fixdata) as json_file:
        human_scanpaths_all = json.load(json_file)  
    #with open(path_word_timing) as f:
    #    word_timing= json.load(f)

    refgazeids = list(set([s['REF_GAZE_ID'] for s in human_scanpaths_all]))


# verbose = False # verbose how many data used to create fdm?
    only_visualize = False # if True, only visualize, figure won't be saved
    #plot_how_many_images = 100 # if None, fdms will be created on all images


# get scanpaths for the given task
    scanpaths_task = human_scanpaths_all #list(filter(lambda x: x['task'] == task, scanpaths))
    #
    def index_of_first(lst, pred):
        for i,v in enumerate(lst):
            if v==pred:
                return i
        return None
    if sample_size < len(refgazeids):
        refgazeids = random.sample(refgazeids, sample_size)
        
    #refgazeids = ['rgo6101699', 'rgo5116219', 'rgo3104966', 'rgo2315514', 'rgo4107366', 
    #         'rgo5226871', 'rgo422254', 'rgo4301221', 'rgo4105255', 'rgo3115624', 
    #          'rgo3102844', 'rgo2206886', 'rgo7125258', 'rgo62017100', 'rgo42160100',
    #           'rgo3104988']
    print (len(refgazeids))
    for i,refgazeid in enumerate(refgazeids):
    
    # get scanpaths for the given refid
    #    print('refgazeid:',refgazeid)
        scanpaths = list(filter(lambda x: x['REF_GAZE_ID'] == refgazeid, scanpaths_task))
        
        if len(scanpaths)==1:
            pass
        else:
            print('gaze duplicate or none')
            continue
        scanpaths=scanpaths[0]
        sentence = scanpaths['REF_SENTENCE']
        bbox = scanpaths['BBOX']
        filename= scanpaths['IMAGEFILE']
        subj = scanpaths['SUBJECT_ID']

        imagefile = os.path.join(path_images, filename)
        img = imageio.imread(imagefile)
        img = img[..., :3]
     #   print(filename)
        if only_visualize: 
            savefilename = None
        else: # save all fdm to the save folder
            savefilename = os.path.join(path_save, filename.split('.')[0]+ path_fixdata.split('.')[0] + '_'+ subj +'.jpg')
        print (path_fixdata.split('.')[0] + " trails save to "+ savefilename)
        xs =[int(x) for x in scanpaths['FIX_X']]
        ys =[int(y) for y in scanpaths['FIX_Y']]
        ts =[t for t in scanpaths['FIX_DURATION']] #scanpath['T']# float division by zero error
        idx_first_landing_on_target = index_of_first(scanpaths['FIX_IN_BBOX'], 1)
        draw_scanpath.draw_scanpath_with_fixation_words(img, xs, ys, ts, savefilename, bbox, word_list=sentence.split(' '), fix_word_list=scanpaths['FIX_WORDINDEX'])

    
