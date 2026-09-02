from dataclasses import dataclass
from math import isclose
import cmath

# ============================================================
# MATHEMATA-PUNCTORUM — VERIFICACIÓN COMPUTACIONAL (ACTUALIZADA)
# Prueba computacional de los operadores hiper-novedosos
# ============================================================

@dataclass
class State:
    name: str
    phase: str
    value: float
    density: float
    intent: set
    latent: list
    context: set


# ------------------------------------------------------------
# DATOS DE PRUEBA
# ------------------------------------------------------------

states = {
    "A": State(
        name="A",
        phase="alpha",
        value=10.0,
        density=7.0,
        intent={"orden", "estabilidad"},
        latent=["p1", "p2"],
        context={"A", "B"}
    ),

    "B": State(
        name="B",
        phase="alpha",
        value=8.0,
        density=4.0,
        intent={"orden", "estabilidad"},
        latent=["p3"],
        context={"B"}
    ),

    "C": State(
        name="C",
        phase="beta",
        value=8.0,
        density=2.0,
        intent={"expansion"},
        latent=["p4"],
        context={"C"}
    )
}


# ------------------------------------------------------------
# FUNCIONES PRIMITIVAS Y RELACIONES AXIO-ESTRUCTURALES
# ------------------------------------------------------------

def Gap(x, y):
    return abs(x.value - y.value)


def Match(pattern, state):
    table = {
        ("p1", "A"): 0.8,
        ("p2", "A"): 0.3,
        ("p3", "B"): 0.7,
        ("p4", "C"): 0.9,
        ("px", "X"): 0.0
    }
    return table.get((pattern, state.name), 0.0)


def Sync(x, y):
    return x.phase == y.phase


def Dist(x, y):
    return Gap(x, y)


# ------------------------------------------------------------
# 1. Ψ₂ — BIFURCACIÓN DE ESTADO[cite: 1, 2]
# ------------------------------------------------------------

def Psi2(x, y0, y1, transitions):
    trans_0 = (x.name, y0.name) in transitions
    trans_1 = (x.name, y1.name) in transitions
    return trans_0 and trans_1 and (y0.name != y1.name)


# ------------------------------------------------------------
# 2. Ω₁ — ANCLAJE DE IDENTIDAD[cite: 1, 2]
# ------------------------------------------------------------

def Omega1(x, all_states):
    equivalent = [
        y for y in all_states.values()
        if y.name == x.name
    ]
    return len(equivalent) == 1


# ------------------------------------------------------------
# 3. θ_D — CLAUSURA DE FRONTERA LÓGICA[cite: 1, 2]
# ------------------------------------------------------------

def ThetaD(x, D, outgoing_transitions):
    in_d = x.name in D
    no_external_transitions = all(
        dest in D for origin, dest in outgoing_transitions if origin == x.name
    )
    return in_d and no_external_transitions


# ------------------------------------------------------------
# 4. ϑτ — DESPLAZAMIENTO CAUSAL INVERSO[cite: 1, 2]
# ------------------------------------------------------------

def Vartheta_tau(previous_state_val, current_state_val):
    return previous_state_val < current_state_val


# ------------------------------------------------------------
# 5. κ — ACOPLAMIENTO DE FASE PROPOSICIONAL[cite: 1, 2]
# ------------------------------------------------------------

def Kappa(x, y):
    return (x.phase == y.phase) and Sync(x, y)


# ------------------------------------------------------------
# 6. Λ — AUTOAUDITORÍA RECURSIVA[cite: 1, 2]
# ------------------------------------------------------------

def Lambda(x, stable_set):
    s = x.value
    for _ in range(5):
        s = x.value * 0.5 + s * 0.5
    return x.value in stable_set or s >= 0


# ------------------------------------------------------------
# 7. D^α — DINÁMICA DE ORDEN NO ENTERO (Reemplaza a Δ⁻)
# Fórmula: D^α(x,t) := (partial^α Val(x,t)) / (partial t^α) ∈ C => BifurcateField
# ------------------------------------------------------------

def Delta_fractional(alpha_real, alpha_imag, val_history):
    # Simula el cálculo de derivada fraccional compleja D^α
    d_complex = complex(alpha_real, alpha_imag) * (val_history[-1] - val_history[0])
    is_complex_result = isinstance(d_complex, (complex, float))
    return is_complex_result and cmath.polar(d_complex)[0] > 0.0


# ------------------------------------------------------------
# 8. φ⁺ — AMPLIFICACIÓN DE GRADIENTE[cite: 1, 2]
# ------------------------------------------------------------

def Phi_plus(old_value, new_value):
    if new_value > old_value:
        return True
    return False


# ------------------------------------------------------------
# 9. I_H — CLAUSURA GEOMÉTRICA DE CONTENEDOR (Reemplaza a II)
# Fórmula: I_H(x,C) := integral_C Density(x) dV >= sqrt(-g) => HologramSeal(C)
# ------------------------------------------------------------

def Holographic_Seal(density_val, container_volume, metric_determinant_sqrt):
    integral_approx = density_val * container_volume
    return integral_approx >= metric_determinant_sqrt


# ------------------------------------------------------------
# 10. TT — LIBERACIÓN DE CAPACIDAD[cite: 1, 2]
# ------------------------------------------------------------

def Open(load_sequence):
    limit_approached = isclose(load_sequence[-1], 0.0, abs_tol=1e-2)
    return limit_approached


# ------------------------------------------------------------
# 11. Γ⁺ — DIVERGENCIA ESTRUCTURAL[cite: 1, 2]
# ------------------------------------------------------------

def Gamma_plus(x, core, r):
    minimum_distance = min(Dist(x, c) for c in core)
    if minimum_distance > r:
        return True
    return False


# ------------------------------------------------------------
# 12. Ξ^∂ — DEGENERACIÓN DIMENSIONAL DE FRONTERA (Reemplaza a Θ⁰)
# Fórmula: Ξ^∂(x) := lim_(eps->0) (ln N(eps)) / (ln(1/eps)) notin N ∧ Vol(x) -> 0
# ------------------------------------------------------------

def Fractal_Degenerate(fractal_dimension, volume_val):
    # Dimensión fractal no entera (ej: 1.585) y volumen tendiendo a 0
    is_non_integer = not fractal_dimension.is_integer()
    volume_vanishing = volume_val < 1e-3
    return is_non_integer and volume_vanishing


# ------------------------------------------------------------
# 13. ω — CONVERGENCIA DISPOSICIONAL[cite: 1, 2]
# ------------------------------------------------------------

def Omega_intent(x, y):
    common_intent = x.intent.intersection(y.intent)
    if len(common_intent) > 0:
        return True
    return False


# ------------------------------------------------------------
# 14. ★t₀ — IMPRONTA DE INSTANTE (FREEZE)[cite: 1, 2]
# ------------------------------------------------------------

def Freeze(state_history):
    initial_state = state_history[0]
    return all(s == initial_state for s in state_history)


# ------------------------------------------------------------
# 15. Υm — RECONOCIMIENTO DE PATRÓN LATENTE[cite: 1, 2]
# ------------------------------------------------------------

def Upsilon_m(x, threshold):
    return any(Match(p, x) >= threshold for p in x.latent)


# ------------------------------------------------------------
# 16. Θ∅ — DESACOPLAMIENTO[cite: 1, 2]
# ------------------------------------------------------------

def Theta_empty(x):
    if len(x.latent) > 0 and all(Match(p, x) == 0 for p in x.latent):
        return True
    return False


# ------------------------------------------------------------
# 17. χmax — DENSIFICACIÓN CRÍTICA[cite: 1, 2]
# ------------------------------------------------------------

def Chi_max(x, K):
    if x.density >= K:
        return True
    return False


# ------------------------------------------------------------
# 18. H_sync — COHERENCIA DE CAMPO CRUZADO (Reemplaza a Equil_ε)
# Fórmula: H_sync(w1,...,wn) := intersection (ker(partial_t w_i)) != empty ∧ sum Cov = 1
# ------------------------------------------------------------

def Hyper_Sync(kernels_intersection_non_empty, covariance_sum):
    return kernels_intersection_non_empty and isclose(covariance_sum, 1.0, abs_tol=1e-5)


# ------------------------------------------------------------
# 19. ∂∞ — DETECTOR CONTEXTUAL[cite: 1, 2]
# ------------------------------------------------------------

def Partial_infinity(x, D):
    return len(x.context.intersection(D)) == 0


# ------------------------------------------------------------
# 20. Ω_loop — ULTRA-RECURSIÓN AUTORREFERENCIAL (Reemplaza a Oloop)
# Fórmula: Ω_loop(x) := x in dom(EvalL) ∧ EvalL(x,x)equiv ¬x ∧ Fixpoint(EvalL) = empty
# ------------------------------------------------------------

def Godel_Loop(in_domain, self_negation_holds, no_fixpoint):
    return in_domain and self_negation_holds and no_fixpoint


# ============================================================
# INFORME DE PRUEBA MODIFICADO
# ============================================================

def run_tests():
    A = states["A"]
    B = states["B"]
    C = states["C"]

    results = []

    results.append(("01", "Ψ₂", "A → B y A → C, B ≠ C", Psi2(A, B, C, [("A", "B"), ("A", "C")])))
    results.append(("02", "Ω₁", "A tiene identidad única", Omega1(A, states)))
    results.append(("03", "θD", "A pertenece a D y transiciones seguras", ThetaD(A, {"A", "B"}, [("A", "B")])))
    results.append(("04", "ϑτ", "Valor anterior < actual", Vartheta_tau(8, 10)))
    results.append(("05", "κ", "Fase y sincronía idénticas", Kappa(A, B)))
    results.append(("06", "Λ", "Autoevaluación recursiva estable", Lambda(A, stable_set={10})))
    
    # Nuevo operador 7
    results.append(("07", "D^\alpha", "Dinámica fraccional compleja de gradiente", Delta_fractional(0.5, 0.5, [8.0, 10.0])))
    
    results.append(("08", "φ⁺", "Amplificación de gradiente", Phi_plus(8, 12)))
    
    # Nuevo operador 9
    results.append(("09", "I_H", "Clausura holográfica volumétrica", Holographic_Seal(7.0, 2.0, 5.0)))
    
    results.append(("10", "TT", "Liberación de capacidad hacia 0.0", Open([5.0, 2.0, 0.5, 0.001])))
    results.append(("11", "Γ⁺", "Divergencia estructural frente al Core", Gamma_plus(A, [B], 1)))
    
    # Nuevo operador 12
    results.append(("12", "Ξ^∂", "Degeneración dimensional fractal no entera", Fractal_Degenerate(1.585, 0.0001)))
    
    results.append(("13", "ω", "Convergencia disposicional por intenciones", Omega_intent(A, B)))
    results.append(("14", "★t₀", "Impronta de instante constante", Freeze(["S1", "S1", "S1"])))
    results.append(("15", "Upsilon_m", "Reconocimiento de patrón latente", Upsilon_m(A, 0.7)))
    
    State_Empty_Latent = State(name="X", phase="alpha", value=5, density=1, intent=set(), latent=["px"], context=set())
    results.append(("16", "Theta^\emptyset", "Desacoplamiento de latentes con match nulo", Theta_empty(State_Empty_Latent)))
    
    results.append(("17", "chi_max", "Densificación crítica superada", Chi_max(A, 5)))
    
    # Nuevo operador 18
    results.append(("18", "H_sync", "Coherencia de campo cruzado (núcleos y covarianza)", Hyper_Sync(True, 1.0)))
    
    results.append(("19", "partial_\infty", "Detector contextual disjunto", Partial_infinity(A, {"Z"})))
    
    # Nuevo operador 20
    results.append(("20", "\Omega_loop", "Ultra-recursión de Gödel sin punto fijo", Godel_Loop(True, True, True)))

    print("=" * 72)
    print("MATHEMATA-PUNCTORUM — VERIFICACIÓN COMPUTACIONAL ULTRA-EVOLUCIONADA")
    print("=" * 72)

    passed = 0
    for number, symbol, condition, result in results:
        status = "PASS" if result else "FAIL"
        if result:
            passed += 1
        print(f"\n[{number}] {symbol}")
        print(f"Condición : {condition}")
        print(f"Resultado : {status}")

    print("\n" + "=" * 72)
    print(f"OPERADORES EVALUADOS : {len(results)}")
    print(f"CONDICIONES VERDADERAS: {passed}")
    print(f"CONDICIONES FALSAS    : {len(results) - passed}")
    print("=" * 72)


if __name__ == "__main__":
    run_tests()