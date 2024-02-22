# UCLA CS162 Course Project Guideline

# Table of Contents

1. [Installations](#installations)
2. [Hardware Setups](#hardware)
3. [Code Executions](#executions)
4. [Datasets](#datasets)
5. [Milestones](#milestones)

# Getting Started and Installations <a name="installations"></a>

Please make sure everything is under **Python3**.

We recommend two ways of getting started to setup the necessary environment:
1. Using conda ([miniconda3](https://docs.conda.io/en/latest/miniconda.html)) (preferred).
2. Using python virtual [environment](https://docs.python.org/3/library/venv.html).


## Using Conda

Goto the above link to install the **miniconda3** corresponding to your OS.

You can use the following commands for various conda operations:

```bash
# cs162 is the name of the conda environment, you can name it anything you like.
conda create -n cs162 python==3.10 pip

# You can list all the conda envs using the following command.
conda info --envs

# Activate the conda env.
conda activate cs162

# The below command will bulk install everything needed except the current project.
pip install -r requirements.txt

# The below commond downloads the project as a package.
pip install -e .

# And use the following to deactivate the conda environment 
# if you're done with some jobs and wish to log out.
conda deactivate
```


## Using the Virtual Environment

This is a nice [guide](https://realpython.com/python-virtual-environments-a-primer/) about setting up virtual environment, we recommend doing the followings:

```bash
python3 -m venv where_ever/you/want/cs162

source where_ever/you/want/cs162/bin/activate

# And use the following to deactivate within a virtualenv.
deactivate
```

The rest of installing the packages should remain the same as in using conda.


# Basic Hardware Guidelines <a name="hardware"></a>

For using cloud services, please refer to the slides/recording in the first TA section.
This readme will only contain more strictly project-related instructions.

## Using GPUs

When your OS features any GPUs, please only access to one of them as our task is not that heavy, and hence does not need to waste computational resources using multi-GPUs in general (but feel free to do so if you'd like). Below are commands that you can use to control GPUs while running your processes (run them before running your main script).

```bash
# Check your GPU status, this will print all the essential information about all the GPUs.
nvidia-smi

# Indicating the GPU ID 0.
export CUDA_VISIBLE_DEVICES="0"

# OR, GPU ID 2.
export CUDA_VISIBLE_DEVICES="2"

# For multi-gpu settings, suppose we would like to use 0, 1, 2 (3 GPUs).
export CUDA_VISIBLE_DEVICES="0,1,2"

# For cpu-only, and hence `no_cuda`.
export CUDA_VISIBLE_DEVICES=""
```


# Code Executions <a name="executions"></a>

1. Most of the code in the provided starter code repository should be executed using the [module option](https://stackoverflow.com/questions/22241420/execution-of-python-code-with-m-option-or-not).
   For example, if you would like to execute the code `data_processing/dummy_data.py` , do:

```bash
python3 -m src.tests.test_eval_utils
```

​		Notice that the `.py ` in `dummy_data.py` is gone

2. File Arguments: 

   Before executing any python file, make sure to skim throught **parse_args** function within the file to learn
   what arguments are used in the code. 

NOTE: The testing scripts are not exhaustive, but should be used as reference. Testing script working correctly doesn't ensure your code is 100% correct. There could still be some errors. 

# Datasets <a name="datasets"></a>

For this project, we split and process the ([UniLC benchmark dataset](https://github.com/luohongyin/UniLC)) and provide you with the following files - `train_claims.jsonl` and `test_claims.jsonl`, consisting of 2057 and 6155 samples respectively. With the train split you will have access to labels in addition to the other data, whereas ground truth labels will not be provided for the test split.

You are provided with the train split to experiment with different prompting and data generation technique and test split to evaluate the Binary Classification performance of the model (here Phi-2) using the prompts that you develop. 

Lastly, you are also provided with `dummy_claims.jsonl` and `dummy_evidence.jsonl` that will be useful in testing the different prompt templates you may use during the course. More information provided in the [Milestones: Basics of Prompting](#basics-of-prompting) section.

# Milestones <a name="milestones"></a>
We divide the project into three major milestones. We describe each of them in more detail in this section. 

NOTE: The testing scripts are not exhaustive, but should be used as reference. Testing script working correctly doesn't ensure your code is 100% correct. There could still be some errors.

## Milestone 1: Evaluation and Model Setup

### Standard Evaluation Metrics
Please finish the `TODO` block in the `evaluate_standard` function in `src/utils/eval_utils.py` file.

You can execute the following commands at the root directory to test your implementations:
```bash
python3 -m src.tests.test_eval_utils
```

If it prints out:

```bash
Your `evaluate_standard` function is CORRECT!
```
Then you should be all set!  
Otherwise, please check your implementation again as there is something wrong something wrong.

### Model Setup
Please finish the `TODO` block in the `model_and_tokenizer_setup` function in `src/phi/phi_utils/model_setup.py` file.

You can execute the following commands at the root directory to test your implementations:
```bash
python3 -m src.tests.test_model_setup
```

If it prints out:

```bash
Your `model_and_tokenizer_setup` function is CORRECT!
```
Then you should be all set!  
Otherwise, please check your implementation again as there is something wrong something wrong.

## Milestone 2: Data Loading and Basics of Prompting

### Building the PhiPromptDataset Class
Please finish the `TODO` block in the `__getitem__()` and `zero_shot_eval_prompt_transform` function for the `PhiPromptDataset` class in `src/phi/phi_utils/dataset.py` file. You may use the zero-shot prompt template in the `src/phi/phi_utils/constants.py` file.

You can execute the following commands at the root directory to test your implementations:
```bash
python3 -m src.tests.test_phi_dataset --annotations_filepath "your path to
dummy_claims.jsonl" --prompt_type "zero_eval"
```

If it prints out:

```bash
Your `__getitem__` and `zero_shot_eval_prompt_transform` function in `PhiPromptDataset` is CORRECT!
```
Then you should be all set!  
Otherwise, please check your implementation again as there is something wrong something wrong.

### Basics of Prompting
Please finish the `TODO` block in the `single_prompt` function in `src/phi/single_prompt.py` file. You may use the zero-shot prompt template in the `src/phi/phi_utils/constants.py` file.

To increase your familiarity with Phi-2, we recommend prompting the model with your own instructions, for which you can use the following commands from the root directory:
```bash
python3 -m src.phi.single_prompt --model_id_or_path "microsoft/phi-2" --single_prompt "enter your prompt here"
```

### Prompting for Binary Classification
Please finish the `TODO` block in the `batch_prompt` function in `src/phi/batch_prompt.py` file. You may use the zero-shot prompt template in the `src/phi/phi_utils/constants.py` file.

Once you finish the implementation, you can generate a prediction file using the following commands from the root directory:
```bash
python3 -m src.phi.batch_prompt --model_id_or_path "microsoft/phi-2" --annotations_filepath "your path to train_claims.jsonl or test_claims.jsonl" --output_filepath "your path to save the prediction results" 
```

To test if the model is performing binary classification correctly, we recommend running an evaluation on the prediction file generated for `train_claims.jsonl`.To evaluate the prediction file, you can use the following commands from the root directory:

python3 -m src.utils.eval_utils --gt_filepath "your path to train_claims.jsonl" --pred_filepath "your path to predictions for train_claims.jsonl" 

## Milestone 3: Advanced Prompting and Data Generation
### Advanced Prompting Techniques
Please finish the `TODO` block in the `few_shot_eval_prompt_transform` function for the `PhiPromptDataset` class in `src/phi/phi_utils/dataset.py` file.

You can execute the following commands at the root directory to test your implementations:
```bash
python3 -m src.tests.test_phi_dataset --annotations_filepath "your path to dummy_claims.jsonl" --prompt_type "few_eval"
```

Once you finish the implementation, you can generate a prediction file and evaluate it similar to `Prompting for Binary Classification` milestone.

### Data Generation
Please finish the `TODO` block in the `zero_shot_evidence_prompt_transform` and `zero_shot_evidence_evaluate_prompt_transform` function for the `PhiPromptDataset` class in `src/phi/phi_utils/dataset.py` file.

You can execute the following commands at the root directory to test your implementations:
```bash
python3 -m src.tests.test_phi_dataset --annotations_filepath "your path to dummy_claims.jsonl" --prompt_type "zero_evidence"
python3 -m src.tests.test_phi_dataset --annotations_filepath "your path to dummy_claims.jsonl" --prompt_type "zero_evidence_eval" --evidence_filepath "your path to dummy_evidence.jsonl"
```

Once you finish the implementation, you can generate a prediction file and evaluate it similar to `Prompting for Binary Classification` milestone.



