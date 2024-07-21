
This Python script is designed to process visual scanpath data. It reads fixation data files, processes images from a specified directory, and saves the results to a designated location.

Prepare your fixation data file (in JSON format), an image directory, and a directory to save the results.

### Arguments
- `--path_fixdata`: Path to the fixation data file in JSON format.
- `--path_images`: Path to the directory containing image files.
- `--path_save`: Path to the directory where results will be saved.
- `--sample_size`: the amount of images with scan path

## Example
Assuming your fixation data file is named `correct.json`, images are stored in the `images` directory, and you wish to save 100 results in a `scanpath` folder on your desktop:

```
python main.py --path_fixdata "correct.json" --path_images "images" --path_save "./desktop/scanpath" --sample_size 100   
```


