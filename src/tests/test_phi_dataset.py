import argparse
from torch.utils.data import DataLoader
from utils.file_utils import load_jsonl
from phi.phi_utils.dataset import PhiPromptDataset

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--annotations_filepath', type=str, required=True)
    parser.add_argument('--evidence_filepath', type=str, default=None)
    parser.add_argument('--prompt_type', type=str, required=True)
    args = parser.parse_args()
    return args 


if __name__ == "__main__":
    args = parse_args()
    dummy_gt_data = load_jsonl(args.annotations_filepath)
    prompt_dataset = PhiPromptDataset(args.annotations_filepath, args.prompt_type, evidence_filepath=args.evidence_filepath)
    prompt_dataloader = DataLoader(prompt_dataset, batch_size=1, shuffle=False)

    for batch in prompt_dataloader:
        if args.prompt_type == "zero_eval":
            if batch[0] == dummy_gt_data[0]["phi_zero_shot_eval_prompt"]:
                print("Your `__getitem__` and `zero_shot_eval_prompt_transform` function in `PhiPromptDataset` is CORRECT!")
            else:
                raise NotImplementedError(
                    "Your `__getitem__` or `zero_shot_eval_prompt_transform` function in `PhiPromptDataset` is INCORRECT!")
            
        elif args.prompt_type == "few_eval":
            if batch[0] == dummy_gt_data[0]["phi_few_shot_eval_prompt"]:
                print("Your `__getitem__` and `few_shot_eval_prompt_transform` function in `PhiPromptDataset` is CORRECT!")
            else:
                raise NotImplementedError(
                    "Your `__getitem__` or `few_shot_eval_prompt_transform` function in `PhiPromptDataset` is INCORRECT!")
            
        elif args.prompt_type == "zero_evidence":
            if batch[0] == dummy_gt_data[0]["phi_zero_shot_evidence_prompt"]:
                print("Your `__getitem__` and `zero_shot_evidence_prompt_transform` function in `PhiPromptDataset` is CORRECT!")
            else:
                raise NotImplementedError(
                    "Your `__getitem__` or `zero_shot_evidence_prompt_transform` function in `PhiPromptDataset` is INCORRECT!")
            
        elif args.prompt_type == "zero_evidence_eval":
            if batch[0] == dummy_gt_data[0]["phi_zero_shot_evidence_eval_prompt"]:
                print("Your `__getitem__` and `zero_shot_evidence_eval_prompt_transform` function in `PhiPromptDataset` is CORRECT!")
            else:
                raise NotImplementedError(
                    "Your `__getitem__ or `phi_zero_shot_evidence_eval_prompt` function in `PhiPromptDataset` is INCORRECT!")