from directory.models import Vassal, Image

vassalList = Vassal.objects.all()

for member in vassalList:

    default = Image.objects.create(image="images/cake.png", tag="cake.png", vassal = member)
