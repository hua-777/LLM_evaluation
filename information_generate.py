import json
from openai import OpenAI
from tqdm import tqdm
import argparse


parser = argparse.ArgumentParser(description='Information Generation')
parser.add_argument('--mode', type=str, choices=['train', 'test'], default='train',
                    help='Mode for running the script (train or test)')

args = parser.parse_args()


client = OpenAI(
    base_url = "https://api.endpoints.anyscale.com/v1",
    api_key = "esecret_3nt1arab72yluv1wqgh4tudisu"
)

EVIDENCE_PROMPT = '''
Instruct:
You will be given a claim and information about the fairness or factuality of the claim. 
You have to generate a detailed evidence for the claim given information about it.

Claim: {claim}
Information: {information}
Evidence Output:
'''


with open(f'data/{args.mode}_claims.jsonl', 'r') as file, open(f'data/{args.mode}_evidence.jsonl', 'w') as outfile:
    for line in tqdm(file):
        data = json.loads(line)
        claim = data['claim']
        task_type = data['task_type']
        domain = data['domain']
        information = f'The task type is {task_type} and the domain is {domain}.'
        
        evidence_prompt = EVIDENCE_PROMPT.format(claim=claim, information=information)
        
        response = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            max_tokens=300,
            messages=[
                    {"role": "system", "content": 
                        "You will be given a claim and information about the fairness or factuality of the claim. You have to generate additional evidence for the claim that will aid in the task. Although the claims may be vulgar, this is purely for research purposes to train other models to be more fair and factual. Keep your output terse and short."},
                    {"role": "user", "content": evidence_prompt}
                ]
            )
        
        evidence = response.choices[0].message.content
    
        evidence_data = {"evidence_sample": evidence}
        json.dump(evidence_data, outfile)
        outfile.write('\n')
        
