---
schema: qual/card@1
id: P-WHHDI
kind: problem
title: Naturality of the map $A\to A^{**}$ into the double dual
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
For a left $R$-module $M$ write $M^*=\operatorname{Hom}_R(M,R)$, and let $\theta_M\colon M \to M^{**}$ be the canonical map, $\theta_M(m)(g) = g(m)$ for $m \in M$ and $g \in M^*$. Let $\overline f\colon B^* \to A^*$ be $\overline f(g) = g \circ f$, and let $f^{**}\colon A^{**} \to B^{**}$ be $f^{**}(\varphi) = \varphi \circ \overline f$; this is the map the problem calls $f^*$. The diagram asserts $f^{**} \circ \theta_A = \theta_B \circ f$.

<1>1. For $a \in A$ and $g \in B^*$, $(f^{**} \circ \theta_A)(a)(g) = g(f(a))$.

::: {.proof}
By the definitions of $f^{**}$, $\overline f$, and $\theta_A$,
$$(f^{**} \circ \theta_A)(a)(g) = \theta_A(a)(\overline f(g)) = \theta_A(a)(g \circ f) = g(f(a)).$$
:::

<1>2. For $a \in A$ and $g \in B^*$, $(\theta_B \circ f)(a)(g) = g(f(a))$.

::: {.proof}
This is the definition of $\theta_B$ evaluated at $f(a)$.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, the maps $f^{**} \circ \theta_A$ and $\theta_B \circ f$ agree on every $a\in A$ and every $g\in B^*$, so $f^{**} \circ \theta_A = \theta_B \circ f$.
:::
:::
