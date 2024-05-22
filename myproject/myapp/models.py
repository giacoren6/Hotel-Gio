from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    room_number = models.IntegerField()
    beds = models.IntegerField()
    def __str__(self):
        return f"{self.name} on floor {self.floor}"
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=50)
    guest_email = models.EmailField()
    def __str__(self):
        return f"{self.room} booked for {self.guest_name}"
    
class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="room_images/")
    def __str__(self):
        return f"{self.room.name} image"
    

