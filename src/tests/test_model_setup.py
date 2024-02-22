from phi.phi_utils.model_setup import model_and_tokenizer_setup

if __name__ == "__main__":
    
    model, tokenizer = model_and_tokenizer_setup("microsoft/phi-2")
    
    if model is None or tokenizer is None:
        raise NotImplementedError(
            "Your `model_and_tokenizer_setup` function is INCORRECT!")
    
    pad_token = tokenizer.pad_token
    
    if pad_token != "<|endoftext|>":
        raise NotImplementedError(
            "Your tokenizer is set INCORRECTLY!")
    
    if "phi-2" not in model.config._name_or_path or "PhiForCausalLM" not in model.config.architectures:
        raise NotImplementedError(
            "Your model is set INCORRECTLY!")
    
    print("Your `model_and_tokenizer_setup` function is CORRECT!")

