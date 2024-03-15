import pandas as pd
from torch.utils.data import Dataset
from utils.file_utils import load_jsonl
from phi.phi_utils.constants import PHI_ZERO_SHOT_EVAL_PROMPT, PHI_FEW_SHOT_EVAL_PROMPT, PHI_ZERO_SHOT_EVIDENCE_EVAL_PROMPT, PHI_ZERO_SHOT_EVIDENCE_PROMPT

class PhiPromptDataset(Dataset):
    def __init__(self, annotations_filepath, prompt_type, evidence_filepath = None):
        self.data = load_jsonl(annotations_filepath)
        self.prompt_type = prompt_type

        if evidence_filepath is not None: 
            self.evidence_data = load_jsonl(evidence_filepath)
        else:
            self.evidence_data = None

    def __len__(self):
        return len(self.data)

    ############################################################
    # TODO: Please complete the implementation for the
    # the following transform functions and __getitem__ fn, that you 
    # will use in def __getitem__ to convert a sample into prompt.
    # You can use the templates provided to in the constants.py file
    def zero_shot_eval_prompt_transform(self, idx):
        prompt = PHI_ZERO_SHOT_EVAL_PROMPT.format(claim=self.data[idx]['claim'], task_type=self.data[idx]['task_type'])
        return prompt
    
    def few_shot_eval_prompt_transform(self, idx):
        prompt = PHI_FEW_SHOT_EVAL_PROMPT.format(claim=self.data[idx]['claim'], task_type=self.data[idx]['task_type'], examples=self.data[idx]['examples'])
        return prompt
    
    
    def zero_shot_evidence_prompt_transform(self, idx):
        task_map = {"fairness": ("fair", "unfair"), "other": ("true", "false")}
        supports_label = "SUPPORTS"
        task_type = self.data[idx]['task_type']
        task_type = task_type if task_type in task_map else "other"

        information = "The claim is {}".format(task_map[task_type][0] if self.data[idx]['label'] == supports_label else task_map[task_type][1])

        prompt = PHI_ZERO_SHOT_EVIDENCE_PROMPT.format(claim=self.data[idx]['claim'], information=information)
        return prompt
    
    
    # End of TODO.
    ##################################################
    
    def __getitem__(self, idx):

        prompt = ""
        
        ##################################################
        # TODO: Please complete the implementation of __getitem__
        # You may use if-else statements to choose the prompt
        # transform as per the prompt type given to you.
        if self.prompt_type == "zero_eval":
            prompt = self.zero_shot_eval_prompt_transform(idx)
        elif self.prompt_type == "few_eval":
            prompt = self.few_shot_eval_prompt_transform(idx)
        elif self.prompt_type == "zero_evidence":
            prompt = self.zero_shot_evidence_prompt_transform(idx)
        elif self.prompt_type == "zero_evidence_eval":
            prompt = PHI_ZERO_SHOT_EVIDENCE_EVAL_PROMPT.format(claim=self.data[idx]['claim'], evidence=self.evidence_data[idx]['evidence'], task_type=self.data[idx]['task_type'])
        else:
            raise ValueError(f"Invalid prompt type: {self.prompt_type}")
        
        # End of TODO.
        ##################################################
        
        return prompt
    
