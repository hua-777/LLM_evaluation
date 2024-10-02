import json

input_file = 'data/output_train_few.jsonl'
output_file = 'data/output_train_few_clean.jsonl'

with open(input_file, 'r') as f, open(output_file, 'w') as out:
    for line in f:
        data = json.loads(line)
        evidence = data['evidence']
        evidence_data = {"evidence_sample": evidence}
        json.dump(evidence_data, out)
        out.write('\n')