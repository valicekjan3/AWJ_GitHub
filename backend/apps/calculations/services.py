"""
AWJ Calculations App - Calculation Services
Servisní vrstva s výpočetními algoritmy pro AWJ
Obsahuje reálné fyzikální vzorce a empirické modely
"""

import math
import numpy as np
from typing import Dict, Tuple, Optional
from decimal import Decimal


class AWJCalculationService:
    """
    Hlavní servisní třída pro AWJ výpočty
    Implementuje fyzikální modely a empirické rovnice
    """

    # Fyzikální konstanty
    WATER_DENSITY = 1000  # kg/m³
    GRAVITY = 9.81  # m/s²

    # Empirické koeficienty (z výzkumu)
    C_DISCHARGE = 0.65  # Výtokový koeficient
    C_VELOCITY = 0.92  # Rychlostní koeficient

    # Materiálové konstanty (základní hodnoty)
    MATERIAL_PROPERTIES = {
        'steel': {'k': 1.0, 'density': 7850, 'strength': 400, 'roughness_factor': 1.0},
        'aluminum': {'k': 1.3, 'density': 2700, 'strength': 200, 'roughness_factor': 0.8},
        'titanium': {'k': 0.7, 'density': 4500, 'strength': 900, 'roughness_factor': 1.2},
        'granite': {'k': 0.5, 'density': 2700, 'strength': 150, 'roughness_factor': 2.0},
        'glass': {'k': 0.6, 'density': 2500, 'strength': 50, 'roughness_factor': 0.5},
        'ceramic': {'k': 0.55, 'density': 2400, 'strength': 300, 'roughness_factor': 1.5},
        'composite': {'k': 0.9, 'density': 1600, 'strength': 250, 'roughness_factor': 1.1},
    }

    @classmethod
    def calculate_water_flow(cls, nozzle_diameter: float, pressure: float) -> float:
        """
        Výpočet průtoku vody
        Q = C_d * A * sqrt(2 * P / ρ)

        Args:
            nozzle_diameter: Průměr trysky [mm]
            pressure: Tlak [MPa]

        Returns:
            Průtok vody [l/min]
        """
        # Konverze jednotek
        d_m = nozzle_diameter / 1000  # mm -> m
        p_pa = pressure * 1e6  # MPa -> Pa

        # Průřez trysky
        area = math.pi * (d_m / 2) ** 2  # m²

        # Rychlost vody
        velocity = cls.C_DISCHARGE * math.sqrt(2 * p_pa / cls.WATER_DENSITY)

        # Objemový průtok
        flow_m3_s = area * velocity  # m³/s
        flow_l_min = flow_m3_s * 1000 * 60  # l/min

        return round(flow_l_min, 2)

    @classmethod
    def calculate_hydraulic_power(cls, pressure: float, flow: float) -> float:
        """
        Výpočet hydraulického výkonu
        P = (Q * p) / 60

        Args:
            pressure: Tlak [MPa]
            flow: Průtok [l/min]

        Returns:
            Výkon [kW]
        """
        # Konverze
        p_pa = pressure * 1e6  # MPa -> Pa
        q_m3_s = flow / (1000 * 60)  # l/min -> m³/s

        power_w = q_m3_s * p_pa  # W
        power_kw = power_w / 1000  # kW

        return round(power_kw, 2)

    @classmethod
    def calculate_cutting_speed(
        cls,
        material_type: str,
        thickness: float,
        pressure: float,
        abrasive_flow: float,
        nozzle_diameter: float,
        focus_diameter: float,
        **kwargs
    ) -> float:
        """
        Výpočet řezné rychlosti
        Založeno na empirickém modelu AWJ

        V = k * (P^a * m_a^b) / (t^c * σ^d)

        Args:
            material_type: Typ materiálu
            thickness: Tloušťka [mm]
            pressure: Tlak [MPa]
            abrasive_flow: Tok abraziva [g/s]
            nozzle_diameter: Průměr trysky [mm]
            focus_diameter: Průměr fokusační trubice [mm]

        Returns:
            Řezná rychlost [mm/min]
        """

        # Získání materiálových vlastností
        mat_props = cls.MATERIAL_PROPERTIES.get(material_type, cls.MATERIAL_PROPERTIES['steel'])
        k_material = mat_props['k']
        strength = mat_props['strength']

        # Empirické exponenty (z výzkumu AWJ)
        a = 1.5  # exponent tlaku
        b = 0.8  # exponent abraziva
        c = 1.2  # exponent tloušťky
        d = 0.5  # exponent pevnosti

        # Základní výpočet řezné rychlosti
        numerator = k_material * (pressure ** a) * (abrasive_flow ** b)
        denominator = (thickness ** c) * (strength ** d)

        speed_mm_s = numerator / denominator

        # Korekce na průměr trysky a fokusační trubice
        diameter_ratio = focus_diameter / nozzle_diameter
        correction_factor = 1 + 0.1 * (diameter_ratio - 3.0)  # optimum je 3.0

        speed_mm_s *= correction_factor

        # Konverze na mm/min
        speed_mm_min = speed_mm_s * 60

        # Realistické omezení (2-5000 mm/min)
        speed_mm_min = max(2, min(5000, speed_mm_min))

        return round(speed_mm_min, 1)

    @classmethod
    def calculate_cut_depth(
        cls,
        material_type: str,
        pressure: float,
        abrasive_flow: float,
        cutting_speed: float
    ) -> float:
        """
        Výpočet maximální hloubky řezu

        Args:
            material_type: Typ materiálu
            pressure: Tlak [MPa]
            abrasive_flow: Tok abraziva [g/s]
            cutting_speed: Řezná rychlost [mm/min]

        Returns:
            Hloubka řezu [mm]
        """

        mat_props = cls.MATERIAL_PROPERTIES.get(material_type, cls.MATERIAL_PROPERTIES['steel'])
        k_material = mat_props['k']

        # Empirický vzorec pro hloubku
        # h = k * (P^1.5 * m_a^0.8) / v^0.5
        depth = k_material * (pressure ** 1.5) * (abrasive_flow ** 0.8) / (cutting_speed ** 0.5)

        depth *= 10  # Normalizační faktor

        return round(depth, 2)

    @classmethod
    def calculate_surface_roughness(
        cls,
        material_type: str,
        cutting_speed: float,
        abrasive_flow: float,
        mesh_size: int = 80
    ) -> float:
        """
        Výpočet drsnosti povrchu Ra

        Args:
            material_type: Typ materiálu
            cutting_speed: Řezná rychlost [mm/min]
            abrasive_flow: Tok abraziva [g/s]
            mesh_size: Velikost zrna abraziva [mesh]

        Returns:
            Drsnost Ra [μm]
        """

        mat_props = cls.MATERIAL_PROPERTIES.get(material_type, cls.MATERIAL_PROPERTIES['steel'])
        roughness_factor = mat_props['roughness_factor']

        # Základní drsnost závisí na rychlosti a abraziv
        # Ra = k * v^0.3 / (m_a^0.4 * mesh^0.2)

        base_roughness = roughness_factor * (cutting_speed ** 0.3) / (
            (abrasive_flow ** 0.4) * (mesh_size ** 0.2)
        )

        # Typické Ra pro AWJ je 1-15 μm
        roughness = base_roughness * 2.0  # Normalizace

        roughness = max(0.5, min(20, roughness))

        return round(roughness, 2)

    @classmethod
    def calculate_cost_per_meter(
        cls,
        abrasive_flow: float,
        cutting_speed: float,
        water_flow: float,
        abrasive_cost_per_kg: float = 25.0,
        water_cost_per_m3: float = 100.0,
        power_cost_per_kwh: float = 4.0,
        hydraulic_power: float = 0.0
    ) -> Decimal:
        """
        Výpočet nákladů na 1 metr řezu

        Args:
            abrasive_flow: Tok abraziva [g/s]
            cutting_speed: Řezná rychlost [mm/min]
            water_flow: Průtok vody [l/min]
            abrasive_cost_per_kg: Cena abraziva [Kč/kg]
            water_cost_per_m3: Cena vody [Kč/m³]
            power_cost_per_kwh: Cena elektrické energie [Kč/kWh]
            hydraulic_power: Hydraulický výkon [kW]

        Returns:
            Náklady [Kč/m]
        """

        # Čas na 1 metr [min]
        time_per_meter_min = 1000 / cutting_speed  # 1000 mm = 1 m

        # Náklady na abrazivo
        abrasive_per_meter_kg = (abrasive_flow / 1000) * time_per_meter_min * 60  # g/s -> kg
        cost_abrasive = abrasive_per_meter_kg * abrasive_cost_per_kg

        # Náklady na vodu
        water_per_meter_m3 = (water_flow / 1000) * time_per_meter_min  # l/min -> m³
        cost_water = water_per_meter_m3 * water_cost_per_m3

        # Náklady na energii
        energy_per_meter_kwh = (hydraulic_power / 60) * time_per_meter_min  # kW * h
        cost_energy = energy_per_meter_kwh * power_cost_per_kwh

        # Celkové náklady
        total_cost = cost_abrasive + cost_water + cost_energy

        return Decimal(str(round(total_cost, 2)))

    @classmethod
    def perform_full_calculation(cls, params: Dict) -> Dict:
        """
        Provede kompletní výpočet všech AWJ parametrů

        Args:
            params: Dictionary se vstupními parametry

        Returns:
            Dictionary s vypočtenými výsledky
        """

        # Extrakce parametrů
        material_type = params.get('material_type', 'steel')
        thickness = params['thickness']
        pressure = params['pressure']
        nozzle_diameter = params.get('nozzle_diameter', 0.33)
        focus_diameter = params.get('focus_diameter', 1.0)
        focus_length = params.get('focus_length', 76)
        abrasive_flow = params.get('abrasive_flow', 8)
        mesh_size = params.get('mesh_size', 80)

        # 1. Průtok vody
        water_flow = cls.calculate_water_flow(nozzle_diameter, pressure)

        # 2. Hydraulický výkon
        hydraulic_power = cls.calculate_hydraulic_power(pressure, water_flow)

        # 3. Řezná rychlost
        cutting_speed = cls.calculate_cutting_speed(
            material_type=material_type,
            thickness=thickness,
            pressure=pressure,
            abrasive_flow=abrasive_flow,
            nozzle_diameter=nozzle_diameter,
            focus_diameter=focus_diameter
        )

        # 4. Hloubka řezu
        cut_depth = cls.calculate_cut_depth(
            material_type=material_type,
            pressure=pressure,
            abrasive_flow=abrasive_flow,
            cutting_speed=cutting_speed
        )

        # 5. Drsnost povrchu
        surface_roughness = cls.calculate_surface_roughness(
            material_type=material_type,
            cutting_speed=cutting_speed,
            abrasive_flow=abrasive_flow,
            mesh_size=mesh_size
        )

        # 6. Náklady
        cost_per_meter = cls.calculate_cost_per_meter(
            abrasive_flow=abrasive_flow,
            cutting_speed=cutting_speed,
            water_flow=water_flow,
            hydraulic_power=hydraulic_power
        )

        # Sestavení výsledků
        results = {
            'water_flow': water_flow,
            'hydraulic_power': hydraulic_power,
            'cutting_speed': cutting_speed,
            'cut_depth': cut_depth,
            'surface_roughness': surface_roughness,
            'cost_per_meter': float(cost_per_meter),

            # Extended results (mezihodnoty)
            'extended': {
                'water_velocity': round(
                    math.sqrt(2 * pressure * 1e6 / cls.WATER_DENSITY), 2
                ),  # m/s
                'kinetic_energy': round(
                    0.5 * cls.WATER_DENSITY * (math.sqrt(2 * pressure * 1e6 / cls.WATER_DENSITY) ** 2),
                    2
                ),  # J/kg
                'mass_flow_rate': round(water_flow * cls.WATER_DENSITY / 60000, 4),  # kg/s
                'abrasive_ratio': round(abrasive_flow / (water_flow * cls.WATER_DENSITY / 60), 3),
                'specific_energy': round(hydraulic_power * 1000 / cutting_speed, 2),  # J/mm
            }
        }

        return results


class AWJOptimizationService:
    """
    Servis pro optimalizaci AWJ parametrů
    """

    @staticmethod
    def optimize_for_speed(
        material_type: str,
        thickness: float,
        pressure_range: Tuple[float, float] = (100, 600),
        abrasive_range: Tuple[float, float] = (1, 20)
    ) -> Dict:
        """
        Optimalizace parametrů pro maximální rychlost

        Returns:
            Optimální parametry a očekávaná rychlost
        """

        best_speed = 0
        best_params = {}

        # Grid search přes možné kombinace
        for pressure in np.linspace(pressure_range[0], pressure_range[1], 10):
            for abrasive in np.linspace(abrasive_range[0], abrasive_range[1], 10):
                speed = AWJCalculationService.calculate_cutting_speed(
                    material_type=material_type,
                    thickness=thickness,
                    pressure=float(pressure),
                    abrasive_flow=float(abrasive),
                    nozzle_diameter=0.33,
                    focus_diameter=1.0
                )

                if speed > best_speed:
                    best_speed = speed
                    best_params = {
                        'pressure': round(float(pressure), 1),
                        'abrasive_flow': round(float(abrasive), 1),
                        'expected_speed': round(speed, 1)
                    }

        return best_params

    @staticmethod
    def optimize_for_cost(
        material_type: str,
        thickness: float,
        min_speed: float = 50  # Minimální přijatelná rychlost
    ) -> Dict:
        """
        Optimalizace parametrů pro minimální náklady
        při zachování minimální rychlosti

        Returns:
            Optimální parametry a očekávané náklady
        """

        best_cost = float('inf')
        best_params = {}

        for pressure in np.linspace(100, 400, 10):  # Nižší tlaky = nižší náklady
            for abrasive in np.linspace(3, 12, 10):  # Střední tok abraziva

                speed = AWJCalculationService.calculate_cutting_speed(
                    material_type=material_type,
                    thickness=thickness,
                    pressure=float(pressure),
                    abrasive_flow=float(abrasive),
                    nozzle_diameter=0.33,
                    focus_diameter=1.0
                )

                if speed >= min_speed:
                    water_flow = AWJCalculationService.calculate_water_flow(0.33, float(pressure))
                    hydraulic_power = AWJCalculationService.calculate_hydraulic_power(
                        float(pressure), water_flow
                    )
                    cost = AWJCalculationService.calculate_cost_per_meter(
                        abrasive_flow=float(abrasive),
                        cutting_speed=speed,
                        water_flow=water_flow,
                        hydraulic_power=hydraulic_power
                    )

                    if cost < best_cost:
                        best_cost = cost
                        best_params = {
                            'pressure': round(float(pressure), 1),
                            'abrasive_flow': round(float(abrasive), 1),
                            'expected_cost': round(float(cost), 2),
                            'expected_speed': round(speed, 1)
                        }

        return best_params
