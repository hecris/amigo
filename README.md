# amigo
Command Line Interface for Spanish translation and verb conjugation.  

![alt text](https://github.com/hecris/amigo/blob/master/screenshots/conjugate.gif?raw=true)

# Installation

1) Clone this repo.
```
git clone https://github.com/hecris/amigo.git
cd amigo
```
2) Set up virtual environment. (this may vary)
```
python3 -m virtualenv env
. env/bin/activate
```
3) Install dependencies
```
pip install git+https://github.com/BoseCorp/py-googletrans.git
pip install --editable .
```
4) You're ready to start using **amigo**

# Usage
* Conjugate: `amigo conjugate <verb>`
