# selenium_image_parser
Automated script that parses images from completed build from jenkins to the REM dashboard

## Usage
### Run script
#### Basic usage
Open windows terminal inside the root directory of the project, and run the following command:

**python .\image_parser.py**
#### Check usage guide
**python .\image_parser.py --help**
### Flags
#### Values
>1. [Optional] -j/--job: Job selected. Default value is **Tests Migration**
>2. [Optional] -b/--branch: Branch selected. Default value is **master**
>3. [Optional] -n/--number: Build number selected. Default value is **1**
