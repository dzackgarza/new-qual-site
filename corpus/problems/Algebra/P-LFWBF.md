---
schema: qual/card@1
id: P-LFWBF
kind: problem
title: Naturality of the bidual evaluation map
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
For an $R$-module $X$, write
$$
X^\vee=\Hom_R(X,R).
$$
Define the evaluation map
$$
\theta_X:X\to X^{\vee\vee},
\qquad
\theta_X(x)(\lambda)=\lambda(x).
$$
Show that $\theta$ is natural: for every $R$-linear map $f:A\to B$,
$$
f^{\vee\vee}\circ\theta_A=\theta_B\circ f.
$$
:::

::: {.solution}
The dual map is $f^\vee:B^\vee\to A^\vee$, $f^\vee(g)=g\circ f$, and the double dual map is $f^{\vee\vee}:A^{\vee\vee}\to B^{\vee\vee}$, $f^{\vee\vee}(\Phi)=\Phi\circ f^\vee$.

::: pf

::: {.pf-step #pointwise}
For every $a\in A$ and $g\in B^\vee$, $\bigl(f^{\vee\vee}(\theta_A(a))\bigr)(g)=\theta_B(f(a))(g)$.

::: pf-proof
The left side is $\theta_A(a)(f^\vee(g))=(g\circ f)(a)=g(f(a))$, and the right side is $g(f(a))$ by definition of $\theta_B$.
:::

:::

::: pf-step
$f^{\vee\vee}\circ\theta_A=\theta_B\circ f$.

::: pf-proof
By step [](#pointwise){.pf-ref}, the elements $f^{\vee\vee}(\theta_A(a))$ and $\theta_B(f(a))$ of $B^{\vee\vee}$ agree at every $g\in B^\vee$, so they are equal for every $a\in A$.
:::

:::

:::

:::
