import json
from collections import defaultdict
import argparse
import os
import shutil
correct_counts = defaultdict(int)
incorrect_counts = defaultdict(int)
with open("correct.json",'r') as json_file:
        human_scanpaths_all_correct = json.load(json_file)  
        #refgazeids_correct = list(set([s['REF_GAZE_ID'] for s in human_scanpaths_all_correct]))

        #scanpaths_task_correct = human_scanpaths_all_correct
        #for i, refgazeid in enumerate(refgazeids_correct):
        #    scanpaths_correct = list(filter(lambda x: x['REF_GAZE_ID'] == refgazeids_correct, scanpaths_task_correct))
        
        for item in human_scanpaths_all_correct:
            correct_counts[item['IMAGEFILE']] +=1


with open("incorrect.json",'r') as json_file:
        human_scanpaths_all_incorrect = json.load(json_file)  
        # refgazeids_incorrect = list(set([s['REF_GAZE_ID'] for s in human_scanpaths_all_incorrect]))
        # scanpaths_incorrect = list(filter(lambda x: x['REF_GAZE_ID'] == refgazeids_incorrect, human_scanpaths_all_incorrect))
        for item in human_scanpaths_all_incorrect:
                incorrect_counts[item['IMAGEFILE']] +=1
                

print(len(correct_counts))

print(len(incorrect_counts))

ratios = {}

for image in incorrect_counts.keys():
    correct_count = correct_counts[image]
    incorrect_count = incorrect_counts[image]
    ratio = incorrect_count / ( incorrect_count + correct_count )
    ratios[image] = ratio

    
top20 = sorted(ratios.items(), key = lambda x : x[1], reverse=True)[:20]


parser = argparse.ArgumentParser(description='Process scanpath data.')
parser.add_argument('--path_images', type=str, help='The path to the images directory')
parser.add_argument('--path_save', type=str, help='The path to save the output')

args = parser.parse_args()

for item in top20:
    if not os.path.exists(args.path_save):
            # Create a new directory because it does not exist 
            os.makedirs(args.path_save)
    imagefile = os.path.join(args.path_images, item[0])
    
    savepath= os.path.join(args.path_save, item[0])
    shutil.copy(imagefile, savepath)

