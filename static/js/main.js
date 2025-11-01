/**
 * AWJ Calculator Pro - Main JavaScript
 * Hlavní soubor pro UI a integraci modulů
 */

// Globální konfigurace
const AWJApp = {
    apiBaseUrl: '/api',
    currentResults: null,
    charts: {},
    scene3D: null
};

/**
 * Hlavní výpočetní funkce volaná z UI
 */
async function calculateAWJ() {
    try {
        // Sběr vstupních parametrů z formuláře
        const params = {
            materialType: document.getElementById('materialType').value,
            thickness: parseFloat(document.getElementById('thickness').value),
            pressure: parseFloat(document.getElementById('pressure').value),
            nozzleDiameter: parseFloat(document.getElementById('nozzleDiameter').value),
            focusDiameter: parseFloat(document.getElementById('focusDiameter').value),
            focusLength: parseFloat(document.getElementById('focusLength').value),
            abrasiveFlow: parseFloat(document.getElementById('abrasiveFlow').value),
            meshSize: parseInt(document.getElementById('meshSize').value)
        };

        // Validace vstupů
        if (!validateInputs(params)) {
            return;
        }

        // Zobrazení loading stavu
        showLoading();

        // Provedení výpočtu (klientská strana)
        const results = AWJCalculations.performFullCalculation(params);

        // Uložení výsledků
        AWJApp.currentResults = results;

        // Aktualizace UI s výsledky
        displayResults(results);

        // Aktualizace grafů
        updateCharts(results, params);

        // Volitelně: odeslat na backend pro uložení
        // await saveToBackend(params, results);

        // Skrytí loading
        hideLoading();

    } catch (error) {
        console.error('Chyba při výpočtu:', error);
        showError('Nastala chyba při výpočtu. Zkontrolujte vstupní hodnoty.');
        hideLoading();
    }
}

/**
 * Validace vstupních parametrů
 */
function validateInputs(params) {
    const errors = [];

    if (params.thickness <= 0 || params.thickness > 500) {
        errors.push('Tloušťka musí být mezi 0 a 500 mm');
    }

    if (params.pressure < 100 || params.pressure > 600) {
        errors.push('Tlak musí být mezi 100 a 600 MPa');
    }

    if (params.abrasiveFlow < 1 || params.abrasiveFlow > 20) {
        errors.push('Tok abraziva musí být mezi 1 a 20 g/s');
    }

    if (params.nozzleDiameter >= params.focusDiameter) {
        errors.push('Průměr fokusační trubice musí být větší než průměr trysky');
    }

    if (errors.length > 0) {
        showError(errors.join('<br>'));
        return false;
    }

    return true;
}

/**
 * Zobrazení výsledků v UI
 */
function displayResults(results) {
    // Aktualizace result cards
    document.getElementById('cuttingSpeed').textContent = `${results.cuttingSpeed} mm/min`;
    document.getElementById('hydraulicPower').textContent = `${results.hydraulicPower} kW`;
    document.getElementById('waterFlow').textContent = `${results.waterFlow} l/min`;
    document.getElementById('cutDepth').textContent = `${results.cutDepth} mm`;
    document.getElementById('roughness').textContent = `${results.surfaceRoughness} μm`;
    document.getElementById('costPerMeter').textContent = `${results.costPerMeter} Kč/m`;

    // Animace zobrazení
    animateResults();
}

/**
 * Animace zobrazení výsledků
 */
function animateResults() {
    const resultCards = document.querySelectorAll('.result-card');
    resultCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.animation = 'fadeIn 0.5s ease-out';
        }, index * 100);
    });
}

/**
 * Aktualizace grafů
 */
function updateCharts(results, params) {
    // Implementace Chart.js grafů
    updateForceChart(results, params);
    updateTimeChart(results);
}

/**
 * Graf rozkladu sil (placeholder - bude rozšířeno)
 */
function updateForceChart(results, params) {
    // TODO: Implementovat graf sil
    console.log('Updating force chart...', results);
}

/**
 * Uložení na backend
 */
async function saveToBackend(params, results) {
    try {
        const response = await fetch(`${AWJApp.apiBaseUrl}/calculations/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ...params,
                ...results
            })
        });

        if (!response.ok) {
            throw new Error('Chyba při ukládání na server');
        }

        const data = await response.json();
        console.log('Úspěšně uloženo:', data);

    } catch (error) {
        console.error('Chyba při ukládání:', error);
    }
}

/**
 * Rychlý výpočet pomocí backend API
 */
async function quickCalculateAPI(params) {
    try {
        const response = await fetch(`${AWJApp.apiBaseUrl}/calculations/quick_calculate/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(params)
        });

        if (!response.ok) {
            throw new Error('API chyba');
        }

        const data = await response.json();
        return data.results;

    } catch (error) {
        console.error('API error:', error);
        throw error;
    }
}

/**
 * UI Helpers
 */
function showLoading() {
    document.querySelectorAll('.btn-calculate').forEach(btn => {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Počítám...';
    });
}

function hideLoading() {
    document.querySelectorAll('.btn-calculate').forEach(btn => {
        btn.disabled = false;
        btn.innerHTML = '<i class="fas fa-play"></i> Vypočítat';
    });
}

function showError(message) {
    // Zobrazení error notifikace
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-error';
    alertDiv.innerHTML = `<i class="fas fa-exclamation-triangle"></i> ${message}`;
    alertDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #ff4444;
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 10px 30px rgba(255, 68, 68, 0.3);
        z-index: 9999;
        animation: slideIn 0.3s ease-out;
    `;

    document.body.appendChild(alertDiv);

    setTimeout(() => {
        alertDiv.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => alertDiv.remove(), 300);
    }, 5000);
}

/**
 * Inicializace slideru
 */
function initializeSliders() {
    const sliders = [
        { input: 'thickness', slider: 'thicknessSlider' },
        { input: 'pressure', slider: 'pressureSlider' },
        { input: 'abrasiveFlow', slider: 'abrasiveFlowSlider' }
    ];

    sliders.forEach(({ input, slider }) => {
        const inputElement = document.getElementById(input);
        const sliderElement = document.getElementById(slider);

        if (inputElement && sliderElement) {
            // Slider -> Input
            sliderElement.addEventListener('input', (e) => {
                inputElement.value = e.target.value;
            });

            // Input -> Slider
            inputElement.addEventListener('input', (e) => {
                sliderElement.value = e.target.value;
            });
        }
    });
}

/**
 * Inicializace tabů
 */
function initializeTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabName = button.getAttribute('data-tab');

            // Deaktivovat všechny taby
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));

            // Aktivovat vybraný tab
            button.classList.add('active');
            document.getElementById(`${tabName}-tab`).classList.add('active');
        });
    });
}

/**
 * AI Optimalizace
 */
async function runAIOptimization() {
    try {
        showLoading();

        const materialType = document.getElementById('materialType').value;
        const thickness = parseFloat(document.getElementById('thickness').value);

        const response = await fetch(`${AWJApp.apiBaseUrl}/calculations/optimize/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                material_type: materialType,
                thickness: thickness,
                target: 'max_speed'
            })
        });

        if (!response.ok) {
            throw new Error('Optimalizace selhala');
        }

        const data = await response.json();

        // Zobrazení doporučení
        displayAIRecommendations(data.optimized_parameters);

        hideLoading();

    } catch (error) {
        console.error('Chyba při optimalizaci:', error);
        showError('Optimalizace selhala');
        hideLoading();
    }
}

/**
 * Zobrazení AI doporučení
 */
function displayAIRecommendations(recommendations) {
    const container = document.getElementById('aiRecommendations');

    container.innerHTML = `
        <div class="recommendation-item">
            <strong>Doporučený tlak:</strong> ${recommendations.pressure} MPa
        </div>
        <div class="recommendation-item">
            <strong>Doporučený tok abraziva:</strong> ${recommendations.abrasive_flow} g/s
        </div>
        <div class="recommendation-item">
            <strong>Očekávaná rychlost:</strong> ${recommendations.expected_speed} mm/min
        </div>
        <button class="btn btn-primary" onclick="applyRecommendations(${JSON.stringify(recommendations)})">
            <i class="fas fa-check"></i> Použít doporučení
        </button>
    `;
}

/**
 * Aplikace AI doporučení do formuláře
 */
function applyRecommendations(recommendations) {
    document.getElementById('pressure').value = recommendations.pressure;
    document.getElementById('pressureSlider').value = recommendations.pressure;
    document.getElementById('abrasiveFlow').value = recommendations.abrasive_flow;
    document.getElementById('abrasiveFlowSlider').value = recommendations.abrasive_flow;

    showNotification('Doporučení aplikována! Klikněte na Vypočítat pro zobrazení výsledků.');
}

/**
 * Notifikace
 */
function showNotification(message) {
    const notif = document.createElement('div');
    notif.className = 'notification success';
    notif.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
    notif.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #00D084;
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 10px 30px rgba(0, 208, 132, 0.3);
        z-index: 9999;
        animation: slideIn 0.3s ease-out;
    `;

    document.body.appendChild(notif);

    setTimeout(() => {
        notif.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => notif.remove(), 300);
    }, 3000);
}

/**
 * Reset formuláře
 */
function resetAll() {
    document.querySelectorAll('.number-input').forEach(input => {
        input.value = input.getAttribute('value');
    });

    document.querySelectorAll('.result-value').forEach(el => {
        el.textContent = '-- ';
    });

    AWJApp.currentResults = null;
}

/**
 * Inicializace aplikace
 */
document.addEventListener('DOMContentLoaded', () => {
    console.log('AWJ Calculator Pro initialized');

    // Inicializace UI komponent
    initializeSliders();
    initializeTabs();

    // Event listeners
    // Automatický výpočet při změně parametrů (volitelné)
    /* const inputs = document.querySelectorAll('.number-input, .select-input');
    inputs.forEach(input => {
        input.addEventListener('change', () => {
            // Debounce pro automatický výpočet
            clearTimeout(window.autoCalcTimeout);
            window.autoCalcTimeout = setTimeout(calculateAWJ, 500);
        });
    }); */

    console.log('✓ UI initialized');
    console.log('✓ Calculationss module loaded');
    console.log('✓ Ready for calculations!');
});

// Export pro debugging
window.AWJApp = AWJApp;
window.AWJCalculations = AWJCalculations;
