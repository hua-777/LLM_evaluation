import argparse
from utils.file_utils import load_jsonl

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pred_filepath', type=str, required=True)
    parser.add_argument('--pred_txt_savepath', type=str, required=True)
    args = parser.parse_args()
    return args 

def convert_prediction_to_txt_file(pred_filepath, pred_txt_savepath):
    pred_labels = load_jsonl(pred_filepath)
    pred_labels = [d["label"] for d in pred_labels]
    with open(pred_txt_savepath, "w") as f:
        f.writelines(line + '\n' for line in pred_labels)

if __name__ == "__main__":
    args = parse_args()
    convert_prediction_to_txt_file(args.pred_filepath, args.pred_txt_savepath)
    
