from django.db import models
from django.urls import reverse

STYLES = (
    ("P", "Plain"),
    ("S", "Sugar"),
    ("A", "Almond Milk & Sugar"),
    ("M", "Soy Milk & Sugar"),
)

# Create your models here.
class Cup(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)


def __str__(self):
    return self.name


def get_absolute_url(self):
    return reverse("cups_detail", kwargs={"pk": self.id})


class Tea(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"tea_id": self.id})

    class Meta:
        ordering = ["id"]


class Sweetening(models.Model):
    date = models.DateField("Tea time")
    style = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=STYLES,
        # set the default value for style to 'P'
        default=STYLES[0][0],
    )

    # FOREIGN KEY
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)

    def __str__(self):
        # friendly value of Field.choice
        return f"{self.get_style_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]
