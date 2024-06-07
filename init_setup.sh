echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python version 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "Installation completed"
echo [$(date)]: "END"