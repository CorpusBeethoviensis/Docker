This is a docker container for automated MEI-Comparison.

## USAGE

All MEI files need to be stored in the 'data'-directory.

### BUILDING THE DOCKER IMAGE
Run docker on your computer
Run "docker build -t main_app ." in your Terminal

### RUNNING THE CONTAINER
On Windows:

After the build is complete run `docker run --rm -it -v "\absolute\Path\to\your\Workdir:/app" main_app`

On Mac

After the build is complete run `docker run -it -v "$(pwd):/app" main_app`

You will then be asked for the directory containing your MEI-Files. You should save your files in subdirectores in the 
'data'-directory. You can than simply type

`/app/data`

and the script will walk through all the subdirectories and find your files.

It will use the first print as a basis for sampling, which can be changed in the main_create-files.

Samples will be drawn using three different algorithms and new files will be created.

They will be saved in subdirectories.

After sampling, the comparison will start automatically.

The comparison will be performed bei Greg Chapman's muscidiff-tool (cf. GitHub) and can be time consuming depending on your 
computational power.

Don't worry about all the Warnings by the converter21, the comparison will still work.

That's it, congratulations!
