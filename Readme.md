# Watched Media

The program was created when I was curious what the split of my Netflix viewing habits were between TV Shows and Movies.

The Program can take the downloaded csv file that can be gained from your Netflix account which takes into account your viewing history since the account was created.

As this is CSV I also wrote some code to convert it to XLSX which is the format OpenPyXL uses.

## Requirements
To run the program you will require

- Python 3.6+

## Installation
Unzip to desired location.

 - `cd To Unzipped Location`
 - `cd WatchedMedia`

## Assumptions
As there is no indication of what type of media the row is, I made the assumption that anything with a : after the first word was a TV show as the pattern in the data seems to reflect this. 

Anything else is considered a movie.



## Usage

Store the file you wish to process in the in your Downloads folder

**To Run the Program**

    cd WatchedMedia

    python Driver.py
    
    provide the file name when prompted e.g NetflixViewingHistory.csv

The program will then convert the CSV file to XLSX and will then run through the data provided taking into account the aforementioned assumption.

## Disclaimer!
This code was written for myself and using the OSX environment and has not been tested on a Windows / Linux setup. As such, if ran on one of these operating systems there may be unexpected results.