---
schema: qual/card@1
id: P-TRIV-DE27
kind: problem
title: Self-adjoint forms of the Laguerre, Hermite and Chebyshev equations
classification:
  areas: [prelim]
  topics:
  - Self-Adjoint Operators
  - Sturm-Liouville Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 27, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Given the eigenvalue problem $\mathcal{L}(x)\psi(x) = \lambda\psi(x)$ with $\mathcal{L}(x) = p_0(x)\frac{d^2}{dx^2} + p_1(x)\frac{d}{dx} + p_2(x)$, $\mathcal{L}$ is self-adjoint if $p_0' = p_1$. Find a function $f(x)$ such that, by multiplying the following ODE, it makes them self adjoint:

(a) Laguerre's ODE: $xy'' + (1 - x)y' + ay = 0$

(b) Hermite's ODE: $y'' - 2xy' + 2\alpha y = 0$

(c) Chabyshev's ODE: $(1 - x^2)y'' - xy' + n^2y = 0$
:::

::: {.solution}

For an equation
$$
p_0y''+p_1y'+p_2y=0,
$$
seek a nonzero multiplier $f$ for which the multiplied equation satisfies $(fp_0)'=fp_1$.

::: pf

::: {.pf-step #s1-1}

The multiplier must satisfy
$$
\frac{f'}f=\frac{p_1-p_0'}{p_0}.
$$


::: pf-proof

The self-adjointness condition for the multiplied equation is
$$
(fp_0)'=fp_1.
$$
Expanding the derivative gives $f'p_0+fp_0'=fp_1$. Dividing by $fp_0$ gives the displayed first-order equation for $f$.

:::

:::

::: {.pf-step #s1-2}

For Laguerre's equation, one may take
$$
\boxed{f(x)=e^{-x}}.
$$


::: pf-proof

Here $p_0=x$ and $p_1=1-x$, so step [](#s1-1){.pf-ref} gives
$$
\frac{f'}f=\frac{(1-x)-1}{x}=-1.
$$
Thus $f=Ce^{-x}$, and the irrelevant nonzero constant may be chosen as $1$. Indeed, the multiplied differential terms are
$$
xe^{-x}y''+(1-x)e^{-x}y'=(xe^{-x}y')'.
$$

:::

:::

::: {.pf-step #s1-3}

For Hermite's equation, one may take
$$
\boxed{f(x)=e^{-x^2}}.
$$


::: pf-proof

Here $p_0=1$ and $p_1=-2x$, so step [](#s1-1){.pf-ref} gives $f'/f=-2x$. Hence $f=Ce^{-x^2}$, and
$$
e^{-x^2}y''-2xe^{-x^2}y'=(e^{-x^2}y')'.
$$

:::

:::

::: {.pf-step #s1-4}

For Chebyshev's equation, one may take
$$
\boxed{f(x)=\frac1{\sqrt{1-x^2}}}
$$
on $\abs{x}<1$.


::: pf-proof

Here $p_0=1-x^2$ and $p_1=-x$, so
$$
\frac{f'}f=\frac{-x-(-2x)}{1-x^2}=\frac{x}{1-x^2}.
$$
Integration gives
$$
\log f=-\frac12\log(1-x^2)+C,
$$
hence the displayed multiplier. Then
$$
fp_0=\sqrt{1-x^2},
\qquad
(fp_0)'=-\frac{x}{\sqrt{1-x^2}}=fp_1.
$$

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} give multipliers satisfying the self-adjointness condition in all three cases.

:::

:::

:::
