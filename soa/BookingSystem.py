from soa.FlightSearch import FlightSearch
from soa.PaymentProcessing import PaymentProcessing
from soa.SeatReservation import SeatReservation


class FlightBooking:
    def __init__(self):
        self.search_service = FlightSearch()
        self.seat_reservation_service = SeatReservation()
        self.payment_service = PaymentProcessing()

    def search(self, origin, destiny, date):
        return self.search_service.search_flights(origin, destiny, date)

    def book(self, flight_id, seat, amount):
        if self.seat_reservation_service.reserve_seat(flight_id, seat):
            if self.payment_service.process_payment(amount):
                return True
            else:
                print("Error al procesar el pago.")
               
                return False
        else:
            print("Error al reservar el asiento.")
            return False


flight_system = FlightBooking()


available_flights = flight_system.search("CDMX", "NYC", "2024-05-20")
print("Vuelos disponibles:")
for flight in available_flights:
    print(flight)

# Reservar un vuelo
succesful_booking = flight_system.book(1, "A3", 300)
if succesful_booking:
    print("¡Reserva exitosa!")
else:
    print("La reserva no pudo ser completada.")