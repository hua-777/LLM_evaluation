#!/bin/bash

python3 -m src.phi.batch_prompt --model_id_or_path "microsoft/phi-2" --annotations_filepath "data/train_claims.jsonl" --output_filepath "data/output_train.jsonl" --prompt_type "zero_cot_eval"

python3 -m src.phi.batch_prompt --model_id_or_path "microsoft/phi-2" --annotations_filepath "data/test_claims.jsonl" --output_filepath "data/output_test.jsonl" --prompt_type "zero_cot_eval"

python3 -m src.utils.create_predictions_file --pred_filepath data/output_train.jsonl --pred_txt_savepath data/output_train_clean.txt

python3 -m src.utils.create_predictions_file --pred_filepath data/output_test.jsonl --pred_txt_savepath data/output_test_clean.txt

python3 -m src.utils.eval_utils --gt_filepath data/train_claims.jsonl --pred_filepath data/output_train.txt
