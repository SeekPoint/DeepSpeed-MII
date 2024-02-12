import mii
pipe = mii.pipeline("/data/hf_model/Mistral-7B-v0.1")
response = pipe("DeepSpeed is", max_new_tokens=128)
print(response)
