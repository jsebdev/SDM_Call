import torch
from diffusers import StableDiffusionPipeline


def diffusers_hugging_face(**kwargs):
    model = kwargs['model']
    number_of_samples = kwargs['number_of_samples']
    seed = kwargs['seed']
    prompt = kwargs['prompt']
    width = kwargs['width']
    height = kwargs['height']
    device = kwargs['device']
    number_of_outputs = kwargs['number_of_outputs']
    pipe = StableDiffusionPipeline.from_pretrained(model)
    if device == 'cuda':
        pipe = pipe.to(device)
    generator = torch.Generator(device).manual_seed(seed)
    # todo: num_outputs
    result = pipe(prompt=[prompt]*number_of_outputs,
                  num_inference_steps=number_of_samples,
                  width=width,
                  height=height,
                  generator=generator)

    return result


def generate_results(**kwargs):
    technique = kwargs.pop('technique',)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    result = technique(device=device, **kwargs)
    return result
