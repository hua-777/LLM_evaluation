import json

input_file = 'data/test_claims_evidence.jsonl'
output_file = 'data/test_evidence.jsonl'

with open(input_file, 'r') as f, open(output_file, 'w') as out:
    for line in f:
        data = json.loads(line)
        evidence = data['evidence']
        evidence_data = {"evidence_sample": evidence}
        json.dump(evidence_data, out)
        out.write('\n')