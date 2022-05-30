# Handwritten Cree syllabics dataset [![CC BY 4.0][cc-by-shield]][cc-by]

This project aims to create a dataset of handwritten Cree syllabics.

To contribute a handwriting sample, [please follow the instructions here](https://samclarke.net/cree/).


## Handwriting Samples

Handwriting samples are stored in the `samples` folder. Each sample has a random ID and consists of an image and a box file which contains bounding boxes and labels for all the syllabics in the sample.


### Box format

The box file format is the same format used by Tesseract. Each line contains the following:

```
<symbol> <left> <bottom> <right> <top> <page>
```

`<symbol>` the syllabic the box contains.  
`<left>` number of pixels from the left to the left edge of the box.  
`<bottom>` number of pixels from the bottom to the bottom edge of the box.  
`<left>` number of pixels from the left to the right edge of the box.  
`<top>` number of pixels from the bottom to the top edge of the box.  
`<page>` the image page number. This will always be 0 in this dataset.

**Note:** The coordinates are from the bottom left corner, not the top left corner.


## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
