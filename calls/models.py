from django.db import models
from django.core.files.storage import default_storage
from django.conf import settings
from .utils import get_image_path
from .resultsGenerator import generate_results, diffusers_hugging_face


import random


class Call(models.Model):
    prompt = models.CharField(max_length=200, default="")
    width = models.IntegerField(default=512)
    height = models.IntegerField(default=512)
    model = models.CharField(
        max_length=200, default="CompVis/stable-diffusion-v1-4")
    # initial_image = models.ImageField( null=True, blank=True, upload_to='images/')
    initial_image = models.ImageField(
        null=True, blank=True, upload_to=get_image_path)
    number_of_samples = models.IntegerField(default=512)
    seed = models.IntegerField(null=True, default=None)
    number_of_outputs = models.IntegerField(default=1)
    called_at = models.DateTimeField(auto_now_add=True)

    def generateResults(self):
        if not self.seed:
            self.seed = random.choice(range(0, 10000000))
        self.number_of_samples = 3
        result = generate_results(technique=diffusers_hugging_face,
                                  model=self.model,
                                  number_of_samples=self.number_of_samples,
                                  seed=self.seed,
                                  prompt=self.prompt,
                                  width=self.width,
                                  height=self.height,
                                  number_of_outputs=self.number_of_outputs
                                  )
        print('36: type(result.images) >>>', type(result.images))
        images_location = []
        for image_index, image in enumerate(result.images):
            image_location = f'generations/generation_{self.id}_{image_index}.png'
            images_location.append(image_location)
            image_path = f'{settings.MEDIA_ROOT}/{image_location}'
            print('47: image_path >>>', image_path)
            image.save(image_path)
            g_image = self.generatedimage_set.create(image=image_location)
        self.save()
        return images_location


class GeneratedImage(models.Model):
    image = models.ImageField()
    call = models.ForeignKey(Call, on_delete=models.CASCADE)
