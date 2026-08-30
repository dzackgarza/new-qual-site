---
schema: qual/card@1
id: P-DMJUU
kind: problem
title: Hungerford 5.6.11
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Irreducibility Criteria
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
If $f \in K[x]$ is irreducible of degree $m > 0$ and $\mathrm{char}(K)$ does not divide $m$, then $f$ is separable.
:::

::: {.solution}
<1>1. Computation of the formal derivative $f'(x)$:
<2>1. Write $f(x) = \sum_{k=0}^m a_k x^k \in K[x]$ with $a_m \neq 0$ and $m \ge 1$.
The formal derivative is:
\[
f'(x) = \sum_{k=1}^m k a_k x^{k-1} = (m \cdot 1_K) a_m x^{m-1} + \sum_{k=1}^{m-1} k a_k x^{k-1}.
\]
Proof: definition of formal derivative of polynomials.
<2>2. Since $\operatorname{char}(K) \nmid m$, the element $m \cdot 1_K \in K$ is non-zero.
Because $K$ is a field and $a_m \neq 0$, the leading coefficient $(m \cdot 1_K) a_m \neq 0$.
Thus $\deg(f') = m - 1 \ge 0$, and in particular $f'(x) \neq 0$.
Proof: field axioms (no zero divisors).

<1>2. Coprimality of $f$ and $f'$:
<2>1. The greatest common divisor $d(x) = \gcd(f(x), f'(x)) \in K[x]$ is a monic divisor of $f(x)$.
Because $f$ is irreducible in $K[x]$, the only monic divisors of $f(x)$ are $1$ and $a_m^{-1} f(x)$.
Proof: definition of irreducible polynomial in a PID.
<2>2. Since $\deg(f') = m - 1 < m = \deg(f)$, $f(x)$ cannot divide $f'(x)$.
Therefore:
\[
\gcd(f(x), f'(x)) = 1.
\]
Proof: degree comparison.

<1>3. Separability of $f$:
<2>1. An irreducible polynomial in $K[x]$ is separable if and only if it has no multiple roots in its splitting field $\overline{K}$.
A polynomial $f$ has a multiple root $\alpha \in \overline{K}$ if and only if $(x - \alpha) \mid \gcd(f, f')$ in $\overline{K}[x]$.
Proof: characterization of multiple roots via derivative.
<2>2. Because $\gcd(f, f') = 1$, $f$ has no multiple roots in any extension field, so $f$ is separable over $K$.
Proof: Euclidean algorithm in polynomial rings over fields.

<1>4. Conclusion:
$f$ is separable. Q.E.D.
Proof: <1>1 through <1>3.
:::
