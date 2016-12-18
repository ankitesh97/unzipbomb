# unzipbomb

A python module which defuses the zipbomb also can extract all the zip files that are contained in a specific root folder


## Installation

```python
pip install unzipbomb
```

## Getting Started

### operating system

This version is only for unix system, will make it compatible for windows in further releases

### Functions for unzipbomb object(i.e unzipbomb.method)

```python
from unzipbomb.unzipbomb import unzipbomb

obj = unzipbomb()
```
| methods        | description           | usage  |
| ------------- |:-------------:| -----:|
| showroot()      |  returns(string) the root folder path that was set  | obj.showroot() |
| suppresstimer(option=True)      | while the processing is done a timer is displayed in the output window, one can suppress that timer using this method . |obj. suppresstimer(False),  if you don’t want to see timer in the output window|
| showerrorlog() |  returns the error log(list of dictionaries), that shows the errors that were occured while processing the decompression.       |    obj.showerrorlog()|
| clearerrorlog() |  clears the error log  | obj.clearerrorlog()|
| showdestination() |  returns(string) the destination folder that was set  | obj.showdestination()|
| showcount() |  returns the number of extracted files  | obj.showcount() |
| resetcount() |  resets the count variable to 0  | obj.resetcount() |
| setrootfolder(rootfolder) | set the root folder from where the extraction should begin | obj.setrootfolder('/path/to/root/folder') |
| setdestinationfolder(destination) |  set the destination folder where the files should be extracted  | obj.setdestinationfolder('/path/to/your/destination')|
| unzipbomb() |  begins the extraction  | obj.unzipbomb() |


### Cookbook


```python
from unzipbomb.unzipbomb import unzipbomb

extractobj = unzipbomb()
extractobj.setrootfoler(‘/home/path/to/root/folder’)
extractobj.setdestinationfolder(‘/home/path/to/destination/floder’)
extractobj.unzipbomb() 
```

Please suggest if any changes/corrections are required

 