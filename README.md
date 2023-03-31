## Student Exam Performance End to End ML Project
```
Steps:
Set up the GitHub (Repository)

Conda New environment: 
```
conda create -p venv python==3.8 -y	
conda activate venv/
```
Alternatve: 
```
Adding virtual env : python -m venv ./venv
Actiavting virtual env : .\venv\Scripts\Activate.ps1
```

…or create a new repository on the command line
echo "# Student_Exam_Performence_End_to_End_Project" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/subhashdixit/Student_Exam_Performence_End_to_End_Project.git
git push -u origin main
git status: to see the added file
…or push an existing repository from the command line
git remote add origin https://github.com/subhashdixit/Student_Exam_Performence_End_to_End_Project.git
git branch -M main
git push -u origin main

setup.py:  It is responsible in creating ML applications as a package
requirements.txt : All the libraries will get installed from here
Created source folder and build the packages

Now, we are creating all the folder manually to understand better
__init.py__ : to create packages and import in another file
Components:Modules which we will used in the project
All the process will be present
Data Ingestion
Data Transformation
Model Trainer

```
Pipeline:
