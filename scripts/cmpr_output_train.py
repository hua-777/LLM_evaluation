import json

def extract_field_from_jsonl(file_path, field_name):
    extracted_values = []
    with open(file_path, 'r') as file:
        for line in file:
            json_data = json.loads(line)
            if field_name in json_data:
                extracted_values.append(json_data[field_name])
    return extracted_values





def read_jsonl_file(file_path_cmpr):
    with open(file_path_cmpr, 'r') as file:
        for line in file:
            yield line.strip()

def write_to_jsonl(output_file, data):
    with open(output_file, 'w') as file:
        for item in data:
            line = json.dumps(item)
            file.write(line + '\n')

train_claims = 'data/train_claims.jsonl'  # Replace 'data.jsonl' with the path to your JSONL file
field_name = 'label'  # Replace 'example_field' with the field you want to extract

extracted_values = extract_field_from_jsonl(train_claims, field_name)
#print("Extracted values:", extracted_values)

output_clean = 'data/output_clean.jsonl'  # Replace 'data.jsonl' with the path to your JSONL file

cmpr=[]

for line in read_jsonl_file(output_clean):
   cmpr.append(line)

err_claims=[]
for l in read_jsonl_file(train_claims):
    err_claims.append(l)

output_file = 'data/cmpr_output.jsonl'
output_data=[]
for i in range(len(cmpr)):
    if cmpr[i]!=extracted_values[i]:
        output_data.append({"Diff Line num":i+1,"Expected":cmpr[i],"train":extracted_values[i],"Diff_Entry":err_claims[i]})

write_to_jsonl(output_file, output_data)