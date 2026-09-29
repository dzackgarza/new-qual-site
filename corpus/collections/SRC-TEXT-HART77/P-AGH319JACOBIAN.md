---
schema: qual/card@1
id: P-AGH319JACOBIAN
kind: problem
title: An automorphism of $\AA^n$ has constant Jacobian
classification:
  areas:
  - algebraic-geometry
  topics:
  - Automorphisms
  - Jacobian
  - Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts with Hartshorne I.3.19. Part (b) is a historical status statement: its open-problem formulation requires characteristic zero; in positive characteristic the converse already fails in one variable. Current-status check on 2026-09-17: the characteristic-zero plane case remains open, while Gao, arXiv:2608.00222, records the July 2026 dimension-three counterexample and counterexamples in every dimension greater than two.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked part (a) directly by differentiating a polynomial inverse and taking determinants. This avoids the incorrect claim in some solution notes that every coordinate of a polynomial automorphism must be linear.'
---

::: {.problem}
Let $\phi: \AA^n \to \AA^n$ be a morphism given by $n$ polynomials $f_1,\ldots,f_n$ in the variables $x_1,\ldots,x_n$, and let $J = \det\qty{ \frac{\partial f_i}{\partial x_j} }$ be the **Jacobian polynomial** of $\phi$.

(a) If $\phi$ is an isomorphism, in which case $\phi$ is called an **automorphism** of $\AA^n$, show that $J$ is a nonzero constant polynomial.

(b) The converse is an unsolved problem, even for $n = 2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $\phi:\AA^n\to\AA^n$ is a polynomial automorphism, then its Jacobian determinant is a unit of $k[x_1,\ldots,x_n]$.

::: pf-proof

Let
$$
\psi:\AA^n\longrightarrow\AA^n
$$
be the inverse polynomial morphism, with coordinate functions $g_1,\ldots,g_n$.
Write $D\phi$ and $D\psi$ for the two Jacobian matrices.
Differentiating
$$
\psi\circ\phi=\operatorname{id}_{\AA^n}
$$
and applying the polynomial chain rule gives
$$
D\psi(\phi(x))\,D\phi(x)=I_n.
$$
Taking determinants yields the polynomial identity
$$
J_\psi(\phi(x))\,J_\phi(x)=1.
$$
Thus $J_\phi$ has a multiplicative inverse in $k[x_1,\ldots,x_n]$.

:::

:::

::: {.pf-step #s2}

Therefore $J$ is a nonzero constant, proving (a).

::: pf-proof

The only units of a polynomial ring over a field are the nonzero constants: if nonzero polynomials $a,b$ satisfy $ab=1$, total degree gives
$$
0=\deg(ab)=\deg a+\deg b,
$$
so both degrees are zero.
Applying this to step [](#s1){.pf-ref} gives
$$
J=J_\phi\in k^\times.
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove the mathematical assertion in part (a).
Part (b) is a status statement rather than an additional proof obligation; the qualification below records its present scope.

:::

:::

:::

::: {.remark title="Characteristic and current status of the converse"}
The open Jacobian conjecture is a characteristic-zero problem.
In characteristic $p>0$, the converse already fails for $n=1$: the polynomial map
$$
F(x)=x-x^p
$$
has derivative $F'(x)=1$, but $F(0)=F(1)=0$, so it is not an automorphism.

Hartshorne's sentence in part (b) records the status when the book was written.
As of 2026-09-17, the characteristic-zero two-variable case remains open.
The unrestricted higher-dimensional conjecture is no longer open: a counterexample in dimension three was announced in July 2026, and counterexamples in every dimension greater than two are described in Shuhong Gao, *Counterexamples to the Jacobian conjecture in dimensions greater than two*, arXiv:2608.00222.
:::
