from time import sleep
import tellopy


def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


def test():
    drone = tellopy.Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)

        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(5)
        drone.up(50)
        sleep(1)
        drone.up(0)

        sleep(3)
        drone.flip_forward()
        sleep(3)

        drone.forward(50)
        sleep(2)
        drone.forward(0)

        drone.clockwise(50)
        sleep(5)
        drone.clockwise(0)

        sleep(1)
        drone.forward(50)
        sleep(2)
        drone.forward(0)
        sleep(1)

        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()
