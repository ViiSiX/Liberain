#!/bin/bash

source /Users/scattm/PC_env/liberain/bin/activate

export FLASK_APP='liberain'
export LIBERAIN_CONFIG=/Users/scattm/Projects/Liberain/api/config.cfg

python -m flask run
