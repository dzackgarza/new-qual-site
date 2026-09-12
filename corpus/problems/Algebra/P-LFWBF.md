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

::: problem
For an $R$-module $X$, write
\[
X^\vee=\Hom_R(X,R).
\]
Define the evaluation map
\[
\theta_X:X\to X^{\vee\vee},
\qquad
\theta_X(x)(\lambda)=\lambda(x).
\]
Show that $\theta$ is natural: for every $R$-linear map $f:A\to B$,
\[
f^{\vee\vee}\circ\theta_A=\theta_B\circ f.
\]
:::

::: {.solution}
The dual map is
\[
f^\vee:B^\vee\to A^\vee,
\qquad
f^\vee(g)=g\circ f,
\]
and the double dual map is
\[
f^{\vee\vee}:A^{\vee\vee}\to B^{\vee\vee},
\qquad
f^{\vee\vee}(\Phi)=\Phi\circ f^\vee.
\]

Let $a\in A$. To prove equality of the two elements of $B^{\vee\vee}$, evaluate both at an arbitrary $g\in B^\vee$.

On one hand,
\[
\bigl(f^{\vee\vee}(\theta_A(a))\bigr)(g)
=\theta_A(a)(f^\vee(g))
=(g\circ f)(a)
=g(f(a)).
\]
On the other hand,
\[
\theta_B(f(a))(g)=g(f(a)).
\]
Thus
\[
f^{\vee\vee}(\theta_A(a))=\theta_B(f(a))
\]
for every $a\in A$, proving
\[
f^{\vee\vee}\circ\theta_A=\theta_B\circ f.
\]
:::
