---
schema: qual/card@1
id: E-SS8.EX-6
kind: problem
title: Harmonicity is preserved by conformal maps
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Give another proof of Lemma 1.3 by showing directly that the Laplacian of $u \circ F$ is zero.

[Hint: The real and imaginary parts of F satisfy the Cauchy-Riemann equations.]
:::

::: {.solution}

The argument is the card's own: the two-variable chain rule together with the Cauchy--Riemann equations turns $\Delta(u\circ F)$ into $\abs{F'}^{2}(\Delta u)\circ F$.

::: pf

::: {.pf-step #chainrule}

$\Delta v=u_{pp}(p_{x}^{2}+p_{y}^{2})+2u_{pq}(p_{x}q_{x}+p_{y}q_{y})+u_{qq}(q_{x}^{2}+q_{y}^{2})+u_{p}\Delta p+u_{q}\Delta q$ for $v=u\circ F$.

::: pf-proof

With $F=(p,q)$ and $v(x,y)=u(p(x,y),q(x,y))$, the chain rule gives $v_{x}=u_{p}p_{x}+u_{q}q_{x}$, and differentiating again with the product and chain rules,
$$
v_{xx}=u_{pp}p_{x}^{2}+2u_{pq}p_{x}q_{x}+u_{qq}q_{x}^{2}+u_{p}p_{xx}+u_{q}q_{xx},
$$
with the analogous expression for $v_{yy}$ obtained by replacing $x$ with $y$. Adding the two gives $\Delta v=v_{xx}+v_{yy}$ as displayed, since $u_{pp},u_{pq},u_{qq}$ are evaluated at $(p,q)$ in every term.

:::

:::

::: {.pf-step #cr}

$p_{x}q_{x}+p_{y}q_{y}=0$ and $p_{x}^{2}+p_{y}^{2}=q_{x}^{2}+q_{y}^{2}$.

::: pf-proof

$F$ is holomorphic, so its real and imaginary parts satisfy the Cauchy--Riemann equations $p_{x}=q_{y}$ and $p_{y}=-q_{x}$. Then
$$
p_{x}q_{x}+p_{y}q_{y}=q_{y}q_{x}+(-q_{x})q_{y}=0,\qquad p_{x}^{2}+p_{y}^{2}=q_{y}^{2}+q_{x}^{2}=q_{x}^{2}+q_{y}^{2}.
$$

:::

:::

::: {.pf-step #harmonic}

$\Delta p=\Delta q=0$.

::: pf-proof

The real and imaginary parts of a holomorphic function are harmonic: $p_{xx}+p_{yy}=(q_{y})_{x}+(-q_{x})_{y}=q_{xy}-q_{xy}=0$ by the Cauchy--Riemann equations and equality of mixed partials, and likewise $q_{xx}+q_{yy}=-(p_{y})_{x}+(p_{x})_{y}=-p_{xy}+p_{xy}=0$.

:::

:::

::: {.pf-step #conclusion}

$\Delta(u\circ F)=\abs{F'}^{2}(\Delta u)\circ F=0$, so $u\circ F$ is harmonic.

::: pf-proof

Substituting steps [](#cr){.pf-ref} and [](#harmonic){.pf-ref} into step [](#chainrule){.pf-ref},
$$
\Delta v=u_{pp}\abs{F'}^{2}+0+u_{qq}\abs{F'}^{2}+0=\abs{F'}^{2}\bigl(u_{pp}+u_{qq}\bigr)\circ F=\abs{F'}^{2}(\Delta u)\circ F,
$$
where $\abs{F'}^{2}=p_{x}^{2}+p_{y}^{2}$. Since $u$ is harmonic, $\Delta u=0$ on the target of $F$, so $\Delta v=0$; that is,
$$
\boxed{\Delta(u\circ F)=\abs{F'}^{2}\cdot(\Delta u)\circ F=0.}
$$

:::

:::

:::

:::
