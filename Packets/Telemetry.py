class CarTelemetryData:
    def __init__(self):
        self.speed = None
        self.throttle = None
        self.steer = None
        self.brake = None
        self.clutch = None
        self.gear = None
        self.engine_rpm = None
        self.drs = None
        self.rev_lights_percent = None
        self.rev_lights_bit_value = None

        # Wheel order: RL, RR, FL, FR
        self.brakes_temperature = []
        self.tyres_surface_temperature = []
        self.tyres_inner_temperature = []

        self.engine_temperature = None

        self.tyres_pressure = []
        self.surface_type = []

    def parse_car_telemetry(self, values, index):
        self.speed = values[index]
        self.throttle = values[index + 1]
        self.steer = values[index + 2]
        self.brake = values[index + 3]
        self.clutch = values[index + 4]
        self.gear = values[index + 5]
        self.engine_rpm = values[index + 6]
        self.drs = values[index + 7]
        self.rev_lights_percent = values[index + 8]
        self.rev_lights_bit_value = values[index + 9]

        index += 10

        # 0 = RL, 1 = RR, 2 = FL, 3 = FR
        for i in range(4):
            self.brakes_temperature.append(values[index])
            index += 1

        # 0 = RL, 1 = RR, 2 = FL, 3 = FR
        for i in range(4):
            self.tyres_surface_temperature.append(values[index])
            index += 1

        # 0 = RL, 1 = RR, 2 = FL, 3 = FR
        for i in range(4):
            self.tyres_inner_temperature.append(values[index])
            index += 1

        self.engine_temperature = values[index]
        index += 1

        # 0 = RL, 1 = RR, 2 = FL, 3 = FR
        for i in range(4):
            self.tyres_pressure.append(values[index])
            index += 1

        # 0 = RL, 1 = RR, 2 = FL, 3 = FR
        for i in range(4):
            self.surface_type.append(values[index])
            index += 1