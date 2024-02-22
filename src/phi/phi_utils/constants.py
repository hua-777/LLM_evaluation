PHI_ZERO_SHOT_EVAL_PROMPT = '''
Instruct:
You will be given a claim and using commonsense reasoning, you need to respond with SUPPORTS or REFUTES, depending on whether you support or refute the claim.
Claim:{claim}
Is the claim {task_type}? 
Respond with SUPPORTS or REFUTES
Output:
'''

PHI_FEW_SHOT_EVAL_PROMPT = '''
Instruct:
You will be given a claim and using commonsense reasoning, you need to respond with SUPPORTS or REFUTES, depending on whether you support or refute the claim.

Following are some examples:
{examples}

Now Your Turn
Claim:{claim}
Is the claim {task_type}? 
Respond with SUPPORTS or REFUTES
Output:
'''

PHI_ZERO_SHOT_EVIDENCE_PROMPT = '''
Instruct:
You will be given a claim and information about the fairness or factuality of the claim. 
You have to generate a detailed evidence for the claim given information about it.

Claim: {claim}
Information: {information}
Evidence Output:
'''

PHI_ZERO_SHOT_EVIDENCE_EVAL_PROMPT = '''
Instruct:
You will be given a claim and evidence for the claim. Using commonsense reasoning, claim and evidence, you need to respond with SUPPORTS or REFUTES, depending on whether you support or refute the claim.
Claim:{claim}
Evidence: {evidence}
Is the claim {task_type}? 
Respond with SUPPORTS or REFUTES
Output:
'''