# clibrary-into-python

# DOES NOT WORK YET
# ONLY WORKS ON UNIX SYSTEMS

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