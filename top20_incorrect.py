import argparse
import scanpath
import json
#python main1.py --path_save "./desktop/scanpath"

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Process scanpath data.')

    # Add the arguments
    parser.add_argument('--path_fixdata', type=str, help='The path to the fixation data file')
    parser.add_argument('--path_save', type=str, help='The path to save the output')
   
    # Execute the parse_args() method
    args = parser.parse_args()

    print("Starting processing...")
    with open(args.path_fixdata,'r') as json_file:
        human_scanpaths_all = json.load(json_file)
        size = len(human_scanpaths_all)
    scanpath.scanpath(args.path_fixdata, "ratio_results", args.path_save, size)
    
    print("Processing complete.")

if __name__ == "__main__":
    main()
