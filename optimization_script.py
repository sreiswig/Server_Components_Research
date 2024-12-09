from ortools.sat.python import cp_model

class GPU:
    def __init__(self, PCIe_slots, power, vram, power_connectors, brand):
        self.PCIe_slots = PCIe_slots
        self.power = power
        self.vram = vram
        self.power_connectors = power_connectors
        self.brand = brand

class Motherboard:
    def __init__(self, PCIe_slots, power, cpu_type):
        self.PCIe_slots = PCIe_slots
        self.power = power
        self.cpu_type = cpu_type

class PowerSupply:
    def __init__(self, connectors, total_power):
        self.connectors = connectors
        self.total_power = total_power

class CPU:
    def __init__(self, power, cpu_type):
        self.power = power
        self.cpu_type = cpu_type

model = cp_model.CpModel()

