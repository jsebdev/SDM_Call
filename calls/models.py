from django.db import models


class Call(models.Model):
    prompt = models.CharField(max_length=200, default="")
    width = models.IntegerField(default=512)
    height = models.IntegerField(default=512)
    model = models.CharField(max_length=200, default="")
    # todo: receive initial image
    # initial_image =
    number_of_samples = models.IntegerField(default=512)
    seed = models.IntegerField(default=512)
    num_outputs = models.IntegerField(default=1)
    called_at = models.DateTimeField(auto_now_add=True)
