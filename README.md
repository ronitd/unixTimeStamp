# Unix Time

Given year, month, day, hour, min and sec in an array this method returns the unix time. 

## Getting Started
Pass a an 2D array containing the dates and times as shown
[[YYYY, MM, DD, HH, MinMin, SS],....,[YYYY, MM, DD, HH, MinMin, SS]]
Where YYYY stands for Year, MM stands for month, DD stands for date, HH for hours, MinMin for minutes, SS for secands.
Year should be in the range of  1970 - 2099, Month in the range of 0 -12, Date between 1-31, Hours should be in the range of 0 - 23, Minutes and Secands in the range of 0 - 59.
Output would be an numpy array which will have unix time corresponding to the input array
### Prerequisites

numpy and python

### Installing

Download the file in the same folder.
In your main file at the beginning
import unixTimestamp as uts

and call the function as
uts.calculate_sec(data)

## Acknowledgments

* Inspiration:gotu0000@gmail.com


