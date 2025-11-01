/**
 * AWJ Calculator - Calculation Module
 * Výpočetní modul pro AWJ parametry
 * Klientská strana - synchronizována s backend/apps/calculations/services.py
 */

class AWJCalculations {
    // Fyzikální konstanty
    static WATER_DENSITY = 1000; // kg/m³
    static GRAVITY = 9.81; // m/s²
    static C_DISCHARGE = 0.65; // Výtokový koeficient
    static C_VELOCITY = 0.92; // Rychlostní koeficient

    // Materiálové vlastnosti
    static MATERIALS = {
        steel: { k: 1.0, density: 7850, strength: 400, roughnessFactor: 1.0 },
        aluminum: { k: 1.3, density: 2700, strength: 200, roughnessFactor: 0.8 },
        titanium: { k: 0.7, density: 4500, strength: 900, roughnessFactor: 1.2 },
        granite: { k: 0.5, density: 2700, strength: 150, roughnessFactor: 2.0 },
        glass: { k: 0.6, density: 2500, strength: 50, roughnessFactor: 0.5 },
        ceramic: { k: 0.55, density: 2400, strength: 300, roughnessFactor: 1.5 },
        composite: { k: 0.9, density: 1600, strength: 250, roughnessFactor: 1.1 }
    };

    /**
     * Výpočet průtoku vody
     * @param {number} nozzleDiameter - Průměr trysky [mm]
     * @param {number} pressure - Tlak [MPa]
     * @returns {number} Průtok [l/min]
     */
    static calculateWaterFlow(nozzleDiameter, pressure) {
        // Konverze jednotek
        const d_m = nozzleDiameter / 1000; // mm -> m
        const p_pa = pressure * 1e6; // MPa -> Pa

        // Průřez trysky
        const area = Math.PI * Math.pow(d_m / 2, 2); // m²

        // Rychlost vody
        const velocity = this.C_DISCHARGE * Math.sqrt(2 * p_pa / this.WATER_DENSITY);

        // Objemový průtok
        const flow_m3_s = area * velocity; // m³/s
        const flow_l_min = flow_m3_s * 1000 * 60; // l/min

        return parseFloat(flow_l_min.toFixed(2));
    }

    /**
     * Výpočet hydraulického výkonu
     * @param {number} pressure - Tlak [MPa]
     * @param {number} flow - Průtok [l/min]
     * @returns {number} Výkon [kW]
     */
    static calculateHydraulicPower(pressure, flow) {
        const p_pa = pressure * 1e6; // MPa -> Pa
        const q_m3_s = flow / (1000 * 60); // l/min -> m³/s

        const power_w = q_m3_s * p_pa; // W
        const power_kw = power_w / 1000; // kW

        return parseFloat(power_kw.toFixed(2));
    }

    /**
     * Výpočet řezné rychlosti
     * @param {Object} params - Parametry výpočtu
     * @returns {number} Řezná rychlost [mm/min]
     */
    static calculateCuttingSpeed({
        materialType,
        thickness,
        pressure,
        abrasiveFlow,
        nozzleDiameter,
        focusDiameter
    }) {
        // Materiálové vlastnosti
        const material = this.MATERIALS[materialType] || this.MATERIALS.steel;
        const k_material = material.k;
        const strength = material.strength;

        // Empirické exponenty
        const a = 1.5; // exponent tlaku
        const b = 0.8; // exponent abraziva
        const c = 1.2; // exponent tloušťky
        const d = 0.5; // exponent pevnosti

        // Základní výpočet
        const numerator = k_material * Math.pow(pressure, a) * Math.pow(abrasiveFlow, b);
        const denominator = Math.pow(thickness, c) * Math.pow(strength, d);

        let speed_mm_s = numerator / denominator;

        // Korekce na průměr
        const diameterRatio = focusDiameter / nozzleDiameter;
        const correctionFactor = 1 + 0.1 * (diameterRatio - 3.0);
        speed_mm_s *= correctionFactor;

        // Konverze na mm/min
        let speed_mm_min = speed_mm_s * 60;

        // Realistické omezení
        speed_mm_min = Math.max(2, Math.min(5000, speed_mm_min));

        return parseFloat(speed_mm_min.toFixed(1));
    }

    /**
     * Výpočet hloubky řezu
     * @param {Object} params - Parametry
     * @returns {number} Hloubka [mm]
     */
    static calculateCutDepth({ materialType, pressure, abrasiveFlow, cuttingSpeed }) {
        const material = this.MATERIALS[materialType] || this.MATERIALS.steel;
        const k_material = material.k;

        const depth = k_material * Math.pow(pressure, 1.5) * Math.pow(abrasiveFlow, 0.8) /
                     Math.pow(cuttingSpeed, 0.5);

        return parseFloat((depth * 10).toFixed(2));
    }

    /**
     * Výpočet drsnosti povrchu
     * @param {Object} params - Parametry
     * @returns {number} Ra [μm]
     */
    static calculateSurfaceRoughness({ materialType, cuttingSpeed, abrasiveFlow, meshSize = 80 }) {
        const material = this.MATERIALS[materialType] || this.MATERIALS.steel;
        const roughnessFactor = material.roughnessFactor;

        const baseRoughness = roughnessFactor * Math.pow(cuttingSpeed, 0.3) /
                             (Math.pow(abrasiveFlow, 0.4) * Math.pow(meshSize, 0.2));

        let roughness = baseRoughness * 2.0;
        roughness = Math.max(0.5, Math.min(20, roughness));

        return parseFloat(roughness.toFixed(2));
    }

    /**
     * Výpočet nákladů na metr řezu
     * @param {Object} params - Parametry
     * @returns {number} Náklady [Kč/m]
     */
    static calculateCostPerMeter({
        abrasiveFlow,
        cuttingSpeed,
        waterFlow,
        hydraulicPower,
        abrasiveCostPerKg = 25.0,
        waterCostPerM3 = 100.0,
        powerCostPerKwh = 4.0
    }) {
        // Čas na 1 metr
        const timePerMeterMin = 1000 / cuttingSpeed;

        // Náklady na abrazivo
        const abrasivePerMeterKg = (abrasiveFlow / 1000) * timePerMeterMin * 60;
        const costAbrasive = abrasivePerMeterKg * abrasiveCostPerKg;

        // Náklady na vodu
        const waterPerMeterM3 = (waterFlow / 1000) * timePerMeterMin;
        const costWater = waterPerMeterM3 * waterCostPerM3;

        // Náklady na energii
        const energyPerMeterKwh = (hydraulicPower / 60) * timePerMeterMin;
        const costEnergy = energyPerMeterKwh * powerCostPerKwh;

        const totalCost = costAbrasive + costWater + costEnergy;

        return parseFloat(totalCost.toFixed(2));
    }

    /**
     * Kompletní výpočet všech parametrů
     * @param {Object} params - Vstupní parametry
     * @returns {Object} Všechny vypočtené hodnoty
     */
    static performFullCalculation(params) {
        const {
            materialType = 'steel',
            thickness,
            pressure,
            nozzleDiameter = 0.33,
            focusDiameter = 1.0,
            focusLength = 76,
            abrasiveFlow = 8,
            meshSize = 80
        } = params;

        // 1. Průtok vody
        const waterFlow = this.calculateWaterFlow(nozzleDiameter, pressure);

        // 2. Hydraulický výkon
        const hydraulicPower = this.calculateHydraulicPower(pressure, waterFlow);

        // 3. Řezná rychlost
        const cuttingSpeed = this.calculateCuttingSpeed({
            materialType,
            thickness,
            pressure,
            abrasiveFlow,
            nozzleDiameter,
            focusDiameter
        });

        // 4. Hloubka řezu
        const cutDepth = this.calculateCutDepth({
            materialType,
            pressure,
            abrasiveFlow,
            cuttingSpeed
        });

        // 5. Drsnost povrchu
        const surfaceRoughness = this.calculateSurfaceRoughness({
            materialType,
            cuttingSpeed,
            abrasiveFlow,
            meshSize
        });

        // 6. Náklady
        const costPerMeter = this.calculateCostPerMeter({
            abrasiveFlow,
            cuttingSpeed,
            waterFlow,
            hydraulicPower
        });

        // Extended results
        const waterVelocity = Math.sqrt(2 * pressure * 1e6 / this.WATER_DENSITY);
        const kineticEnergy = 0.5 * this.WATER_DENSITY * Math.pow(waterVelocity, 2);
        const massFlowRate = waterFlow * this.WATER_DENSITY / 60000;
        const abrasiveRatio = abrasiveFlow / (waterFlow * this.WATER_DENSITY / 60);
        const specificEnergy = hydraulicPower * 1000 / cuttingSpeed;

        return {
            waterFlow,
            hydraulicPower,
            cuttingSpeed,
            cutDepth,
            surfaceRoughness,
            costPerMeter,
            extended: {
                waterVelocity: parseFloat(waterVelocity.toFixed(2)),
                kineticEnergy: parseFloat(kineticEnergy.toFixed(2)),
                massFlowRate: parseFloat(massFlowRate.toFixed(4)),
                abrasiveRatio: parseFloat(abrasiveRatio.toFixed(3)),
                specificEnergy: parseFloat(specificEnergy.toFixed(2))
            }
        };
    }
}

// Export pro použití v jiných modulech
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AWJCalculations;
}
