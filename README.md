# clibrary-into-python
**_Make c file importable in python_**

**Utilistation**
* Place the python and bash file in the same folder as the c library uncompiled
* Execute : (replace {c_file_name} with the name of the c files)
```bash 
chmod +x compilec
./compilec {c_files_name} {args}
```
or 
```bash
python compilec.py {c_files_name} {args}
```
* The c files will be compiled and importable in python

*Args*
* -all : Compile all c files in the folder
* -c {path_to_compiler}: Compile the c file with the given path to the compiler (default is gcc)
* -o {path_to_output}: The output file name (default is the same as the c file name) **If this option is used with -all, all c files will keep their names but will be compiled in a folder (the path given)**