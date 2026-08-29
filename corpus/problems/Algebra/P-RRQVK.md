---
schema: qual/card@1
id: P-RRQVK
kind: problem
title: Galois group of $x^7-1$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Roots of Unity
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
What is the Galois group of $x^7 - 1$ over the rationals?
:::

::: {.solution}
<1>1. The splitting field of $x^7 - 1$ over $\QQ$ is $\QQ(\zeta_7)$, where $\zeta_7$ is a primitive $7$-th root of unity.
Proof: the roots of $x^7 - 1$ are the $7$-th roots of unity, all powers of $\zeta_7$.

<1>2. The minimal polynomial of $\zeta_7$ over $\QQ$ is the cyclotomic polynomial $\Phi_7(x) = x^6 + x^5 + \cdots + x + 1$, of degree $6$.
Proof: $\Phi_7(x) = (x^7 - 1)/(x - 1)$ is irreducible over $\QQ$ (cyclotomic polynomials are irreducible).

<1>3. Hence $[\QQ(\zeta_7) : \QQ] = 6$.
Proof: <1>2.

<1>4. The extension $\QQ(\zeta_7)/\QQ$ is Galois.
Proof: it is the splitting field of the separable polynomial $x^7 - 1$ over $\QQ$ (characteristic $0$).

<1>5. $\operatorname{Gal}(\QQ(\zeta_7)/\QQ) \cong (\ZZ/7\ZZ)^\times$.
Proof: an automorphism sends $\zeta_7 \mapsto \zeta_7^a$ for $a \in (\ZZ/7\ZZ)^\times$, and this assignment is an isomorphism.

<1>6. $(\ZZ/7\ZZ)^\times \cong \ZZ/6\ZZ$ is cyclic of order $6$.
Proof: $7$ is prime, so the multiplicative group of $\FF_7$ is cyclic of order $6$.

<1>7. Hence $\operatorname{Gal}(x^7 - 1 / \QQ) \cong \ZZ/6\ZZ$.
Proof: <1>5 and <1>6.

<1>8. Q.E.D.
Proof: <1>7.
:::
