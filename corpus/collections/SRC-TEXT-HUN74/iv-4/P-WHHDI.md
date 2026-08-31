---
schema: qual/card@1
id: P-WHHDI
kind: problem
title: Hungerford 4.4.9
classification:
  areas:
  - algebra
  topics:
  - Dual Spaces
  - Modules
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Show that for any homomorphism$f: A \to B$ of left $R-$modules the following diagram is commutative:

where $\theta_A, \theta_B$ are as in Theorem 4.12 and $f^*$ is the map induced on $A^{**} \coloneqq \mathrm{Hom}_R(\mathrm{Hom}(A, R), R)$ by the map $$\overline f: \mathrm{Hom}(B, R) \to \mathrm{Hom}_R(A, R).$$
:::

::: {.solution}
<1>1. Recall $\theta_A : A \to A^{**}$ is defined by $\theta_A(a)(g) = g(a)$ for $a \in A$, $g \in A^* = \operatorname{Hom}_R(A, R)$.
::: {.proof}
Theorem 4.12 (the canonical map into the double dual).
:::

<1>2. The induced map $f^{**} : A^{**} \to B^{**}$ is defined by $f^{**}(\varphi) = \varphi \circ \overline f$ for $\varphi \in A^{**}$, where $\overline f(g) = g \circ f$ for $g \in B^*$.
::: {.proof}
$\overline f : B^* \to A^*$ is precomposition with $f$, and $f^{**}$ is precomposition with $\overline f$.
:::

<1>3. For $a \in A$ and $g \in B^*$,
$$(f^{**} \circ \theta_A)(a)(g) = \theta_A(a)(\overline f(g)) = \theta_A(a)(g \circ f) = (g \circ f)(a) = g(f(a)).$$
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Also $(\theta_B \circ f)(a)(g) = \theta_B(f(a))(g) = g(f(a))$.
::: {.proof}
<1>1 applied to $B$.
:::

<1>5. Hence $f^{**} \circ \theta_A = \theta_B \circ f$, so the diagram commutes.
::: {.proof}
<1>3 and <1>4 agree for every $a \in A$ and $g \in B^*$.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
