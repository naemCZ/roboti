from vex import *

DEFAULT_ENGINE_SPEED = 0

def main():
    #distanceSensor = Distance(Ports.PORT1)
    distanceSensor = Distance(Ports.PORT11)
    opticalSensor = Optical(Ports.PORT5)

    #wait(100, MSEC)



    controller.buttonLUp.released(increase_speed)
    controller.buttonLDown.released(decrease_speed)
    controller.buttonRUp.released(turn_left)
    controller.buttonRDown.released(turn_right)

    reversing = False

    controller.axisA.changed(axis_changed, (reversing,controller))
    controller.axisB.changed(axis_changed, (reversing, controller))

    brain.screen.clear_screen()
    brain.screen.print_at("test", x = 0, y = 50)
    sleep(200, MSEC)
    brain.screen.clear_screen()


    while True:
        check_distance(motorL, motorR, distanceSensor, reversing)
        brain.screen.print_at(reversing, x = 0, y = 35)

        sleep(10, MSEC)

def axis_changed(reversing, controller):
    
    axisA = controller.axisA.position()
    axisB = controller.axisB.position()

    brain.screen.clear_screen()

    brain.screen.print_at(float(axisA), x = 0, y = 50)
    brain.screen.print_at(float(axisB), x = 0, y = 65)

    distance = distanceSensor.object_distance(MM)
    if distance < 100:
        touchSensor.set_color(Color.RED)
    elif distance < 200:
        touchSensor.set_color(Color.ORANGE)
    else:
        touchSensor.set_color(Color.BLUE)


    if axisA > 10 or axisA < -10 or axisB > 10 or axisB < -10:
        speed = axisA
        heading = axisB


        #reversing = (speed < 0)
        if speed < 0:
            reversing = True
        else:
            reversing = False



        if distance > 200 or reversing:
            motorL.spin(DirectionType.FORWARD, speed + heading, VelocityUnits.PERCENT)
            motorR.spin(DirectionType.FORWARD, speed - heading, VelocityUnits.PERCENT)
    else:
        motorL.stop()
        motorR.stop()

    sleep(10, MSEC)

def check_distance(motorL, motorR, distanceSensor, reversing):
    distance = distanceSensor.object_distance(MM)
    if distance < 100:
        touchSensor.set_color(Color.RED)
    elif distance < 200:
        touchSensor.set_color(Color.ORANGE)
    else:
        touchSensor.set_color(Color.BLUE)

    #brain.screen.print_at(reversing, x = 0, y = 35)


    if distance < 100 and not reversing:
        motorL.stop()
        motorR.stop()
        pass

def increase_speed():
    global speed
    speed = speed + 10

    brain.screen.clear_screen()
    brain.screen.print("increase speed")
    motorL.spin(DirectionType.FORWARD, speed, VelocityUnits.PERCENT)
    motorR.spin(DirectionType.FORWARD, speed, VelocityUnits.PERCENT)

def decrease_speed():
    global speed
    speed -= + 10

    brain.screen.clear_screen()
    brain.screen.print("decrease speed")
    motorL.spin(DirectionType.FORWARD, speed, VelocityUnits.PERCENT)
    motorR.spin(DirectionType.FORWARD, speed, VelocityUnits.PERCENT)

def turn_left():
    global speed
    global heading
    heading -= 10

    motorL.spin(DirectionType.FORWARD, speed + heading, VelocityUnits.PERCENT)
    motorR.spin(DirectionType.FORWARD, speed - heading, VelocityUnits.PERCENT)

def turn_right():
    global speed
    global heading
    heading += 10

    motorL.spin(DirectionType.FORWARD, speed + heading, VelocityUnits.PERCENT)
    motorR.spin(DirectionType.FORWARD, speed - heading, VelocityUnits.PERCENT)




brain = Brain()
motorL = Motor(Ports.PORT6, GearSetting.RATIO_1_1, False)
motorR = Motor(Ports.PORT12, GearSetting.RATIO_1_1, True)
distanceSensor = Distance(Ports.PORT11)

speed = DEFAULT_ENGINE_SPEED
heading = 0


touchSensor = Touchled(Ports.PORT4)
#touchSensor.set_color(Color.RED)

controller = Controller()


#while not touchSensor.pressing():
sleep(100, MSEC)
#touchSensor.on()
    
touchSensor.set_color(Color.WHITE)


main()