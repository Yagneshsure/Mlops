import os
from pathlib import Path

list_of_files = [
    
    ".github/workflows/.gitkeep",
    "soc/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/logging.py",
    "src/exception.py",
    "tests/unit/__init__.py",
    "tets/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        # logging.info(f"creating directory: {filedir} for file : {filename}")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass # Create an emptyb file