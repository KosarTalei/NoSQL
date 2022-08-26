class Flight:
    def __init__(self, beginning, beginning_airport, destination_airport, destination,
                 date, arrival_time, departure_time, price, flight_class, capacity,
                 airline=None, duration=None, stop_place=None, stop_duration=None):
        self.airline = airline  # str
        self.beginning = beginning  # str
        self.destination = destination  # str
        self.beginning_airport = beginning_airport  # str
        self.destination_airport = destination_airport  # str
        self.date = date  # str
        self.arrival_time = arrival_time  # str
        self.departure_time = departure_time  # str
        self.capacity = capacity  # int
        self.duration = duration  # str
        self.stop_place = stop_place  # str
        self.price = price  # float
        self.flight_class = flight_class  # str
        self.stop_duration = stop_duration  # str
