import argparse
import scanpath
#python main1.py --path_fixdata "correct.json" --path_images "images" --path_save "./desktop/scanpath"

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Process scanpath data.')

    # Add the arguments
    parser.add_argument('--path_fixdata', type=str, help='The path to the fixation data file')
    parser.add_argument('--path_images', type=str, help='The path to the images directory')
    parser.add_argument('--path_save', type=str, help='The path to save the output')
    parser.add_argument('--sample_size', type=int, help='The path to save the output')
    # Execute the parse_args() method
    args = parser.parse_args()

    print("Starting processing...")
    scanpath.scanpath(args.path_fixdata, args.path_images, args.path_save,args.sample_size)
    print("Processing complete.")

if __name__ == "__main__":
    main()
