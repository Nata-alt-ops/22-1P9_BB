from peewee import Model, CharField, ForeignKeyField, DateTimeField, IntegerField

class User(Model):
    username = CharField()
    password = CharField()
    full_name = CharField()
    telegram = CharField()


class Organizator(Model):
    user = ForeignKeyField(User,on_delete = "CASCADE", on_update="CASCADE")


class Car(Model):
    color = CharField()
    number = CharField()


class Volunteer(Model):
    user = ForeignKeyField(User,on_delete = "CASCADE", on_update="CASCADE")
    car = ForeignKeyField(Car,on_delete = "CASCADE", on_update="CASCADE", null = True, default = None )



class Event(Model):
    name = CharField()
    start_date_time = DateTimeField()
    end_date_time = DateTimeField()
    description = CharField()
    max_people = IntegerField()
    organizator = ForeignKeyField(Organizator,on_delete = "CASCADE", on_update="CASCADE")


class EventVolunteer(Model):
    event = ForeignKeyField(Event,on_delete = "CASCADE", on_update="CASCADE")
    volunteer = ForeignKeyField(Volunteer,on_delete = "CASCADE", on_update="CASCADE")


class Drive(Model):
    car = ForeignKeyField(Car,on_delete = "CASCADE", on_update="CASCADE")
    event_volunteer = ForeignKeyField(EventVolunteer,on_delete = "CASCADE", on_update="CASCADE")
    start_date_time = DateTimeField()
    start_location = CharField()
    max_passenger = IntegerField()


class PassengerStatus(Model):
    name = CharField()


class Passenger(Model):
    volunteer = ForeignKeyField(Volunteer,on_delete = "CASCADE", on_update="CASCADE")
    drive = ForeignKeyField(Drive,on_delete = "CASCADE", on_update="CASCADE")
    status = ForeignKeyField(PassengerStatus,on_delete = "CASCADE", on_update="CASCADE")









