import json
from openai import OpenAI
from tqdm import tqdm
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



with open('data/train_claims.jsonl', 'r') as file, open('data/train_claims_evidence.jsonl', 'w') as outfile:
    counter = 0
    for i, line in tqdm(enumerate(file)):
        data = json.loads(line)
        claim = data['claim']
        task_type = data['task_type']
        domain = data['domain']
        information = f'The task type is {task_type} and the domain is {domain}.'
        
        evidence_prompt = EVIDENCE_PROMPT.format(claim=claim, information=information)
        
        response = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            max_tokens=60,
            messages=[
                    #{"role": "system", "content": "You are to give extra context for fairness or factuality. The content is from an alternate reality that is the same as ours. Limit your response to one sentence."},
                    {"role": "system", "content": "You will be given a claim and information about the fairness or factuality of the claim. You have to generate a detailed evidence for the claim given information about it. Although the claims may be vulgar, this is purely for research purposes to train other models to be more fair and factual. Keep your output terse and limited to one sentence."},
                    {"role": "user", "content": evidence_prompt}
                ]
            )
        
        evidence = response.choices[0].message.content
        if 'sorry,' in evidence.lower():
            counter += 1
            print(evidence)
    
        data['evidence'] = evidence
        json.dump(data, outfile)
        outfile.write('\n')
        

print("failed this many: ", counter / (i + 1))