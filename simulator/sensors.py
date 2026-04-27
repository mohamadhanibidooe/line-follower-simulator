# sensors.py
# ------------------------------------------
# Line sensor module (5 analog sensors)
# ------------------------------------------
import math

class LineSensorArray:
    def __init__(self, robot, sensor_offset=35, sensor_spacing=8):
        # Reference to robot body
        self.robot = robot

        # Sensor geometry
        self.sensor_offset = sensor_offset
        self.sensor_spacing = sensor_spacing

        # Maximum ADC value (analog)
        self.MAX_ADC = 4095

    def _sample_pixel(self, ix, iy):
        # Check bounds
        w = self.robot.world.surface.get_width()
        h = self.robot.world.surface.get_height()

        if ix < 0 or iy < 0 or ix >= w or iy >= h:
            return 255, 255, 255, 255

        return self.robot.world.surface.get_at((ix, iy))

    def read(self):
        # If world not attached yet, return zeros
        if not hasattr(self.robot, "world") or self.robot.world is None:
            return [0]*5, [(int(self.robot.x), int(self.robot.y))]*5

        # 5 local sensor positions in robot frame
        points_local = [
            (self.sensor_offset, -2*self.sensor_spacing),
            (self.sensor_offset, -self.sensor_spacing),
            (self.sensor_offset, 0),
            (self.sensor_offset, self.sensor_spacing),
            (self.sensor_offset, 2*self.sensor_spacing)
        ]

        readings = []
        positions = []

        for px, py in points_local:

            # Convert to world coordinates
            wx = self.robot.x + px * math.cos(self.robot.angle) - py * math.sin(self.robot.angle)
            wy = self.robot.y + px * math.sin(self.robot.angle) + py * math.cos(self.robot.angle)

            ix, iy = int(wx), int(wy)
            positions.append((ix, iy))

            r, g, b, a = self._sample_pixel(ix, iy)

            # ---------------------------
            # ANALOG CONVERSION
            # ---------------------------
            # Black = 0 → High ADC
            # White = 255 → Low ADC
            # We use luminance to convert to analog
            lum = (r + g + b) / 3.0

            # Invert because black-line sensors output strong value on dark line
            analog_value = int(self.MAX_ADC * (1 - lum / 255))

            readings.append(analog_value)

        return readings, positions
