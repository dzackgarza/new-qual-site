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
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-09-28
  note: Restored the commutative square, transcribed from the page image of Hungerford, Algebra, p. 206, Exercise IV.4.9; the extraction carried it only as an image.
---

::: {.problem}
Show that for any homomorphism $f: A \to B$ of left $R$-modules the following diagram is commutative:

\begin{tikzcd}
	A & {A^{**}} \\
	B & {B^{**}}
	\arrow["{\theta_A}", from=1-1, to=1-2]
	\arrow["f"', from=1-1, to=2-1]
	\arrow["{f^*}", from=1-2, to=2-2]
	\arrow["{\theta_B}"', from=2-1, to=2-2]
\end{tikzcd}

where $\theta_A, \theta_B$ are as in Theorem 4.12 and $f^*$ is the map induced on $A^{**} \coloneqq \mathrm{Hom}_R(\mathrm{Hom}(A, R), R)$ by the map $$\overline f: \mathrm{Hom}(B, R) \to \mathrm{Hom}_R(A, R).$$
:::

::: {.solution}
For a left $R$-module $M$ write $M^*=\operatorname{Hom}_R(M,R)$, and let $\theta_M\colon M \to M^{**}$ be the canonical map, $\theta_M(m)(g) = g(m)$ for $m \in M$ and $g \in M^*$. Let $\overline f\colon B^* \to A^*$ be $\overline f(g) = g \circ f$, and let $f^{**}\colon A^{**} \to B^{**}$ be $f^{**}(\varphi) = \varphi \circ \overline f$; this is the map the problem calls $f^*$. The diagram asserts $f^{**} \circ \theta_A = \theta_B \circ f$.

::: pf

::: {.pf-step #s1}

For $a \in A$ and $g \in B^*$, $(f^{**} \circ \theta_A)(a)(g) = g(f(a))$.

::: pf-proof

By the definitions of $f^{**}$, $\overline f$, and $\theta_A$,
$$(f^{**} \circ \theta_A)(a)(g) = \theta_A(a)(\overline f(g)) = \theta_A(a)(g \circ f) = g(f(a)).$$

:::

:::

::: {.pf-step #s2}

For $a \in A$ and $g \in B^*$, $(\theta_B \circ f)(a)(g) = g(f(a))$.

::: pf-proof

This is the definition of $\theta_B$ evaluated at $f(a)$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the maps $f^{**} \circ \theta_A$ and $\theta_B \circ f$ agree on every $a\in A$ and every $g\in B^*$, so $f^{**} \circ \theta_A = \theta_B \circ f$.

:::

:::

:::
