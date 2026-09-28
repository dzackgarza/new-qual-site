---
schema: qual/card@1
id: P-BKF08-8A
kind: problem
title: Growth of the second moment of a solution of the heat equation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 8A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked differentiation under the integral and both integrations by
    parts using rapid decay. Used the problem's t=1 mass normalization;
    the retained solution text's reference to t=0 is a typo.
---

::: {.problem}
Let $u(x,t)$ be an infinitely differentiable real function satisfying the diffusion equation
$$
u_t=u_{xx},\qquad -\infty<x<\infty,\ t>0.
$$
Assume $u$ and all its partial derivatives of all orders are rapidly decreasing in $x$: in every strip $0<t<a$ they are bounded by a constant times $x^{-n}$ for every $n>0$.
Also assume
$$
\int_{-\infty}^{\infty}u(x,1)\,dx=1.
$$
Show that for $t>0$,
$$
\frac d{dt}\int_{-\infty}^{\infty}x^2u(x,t)\,dx=2.
$$
:::

::: {.solution}
For $t>0$, define the total mass
$$
M(t)\coloneqq\int_{-\infty}^{\infty}u(x,t)\,dx
$$
and the second moment
$$
S(t)\coloneqq\int_{-\infty}^{\infty}x^2u(x,t)\,dx.
$$

<1>1. The mass $M(t)$ is constant on $(0,\infty)$.

::: {.proof}
Fix $t_0>0$ and choose $a>t_0$. The stated rapid decrease of $u$ and
its derivatives on the strip $0<t<a$ gives an integrable dominating
function for $u_t=u_{xx}$ near $t_0$, so differentiation under the
integral sign is valid. Thus
$$
M'(t)
=\int_{-\infty}^{\infty}u_t(x,t)\,dx
=\int_{-\infty}^{\infty}u_{xx}(x,t)\,dx.
$$
Rapid decrease also gives
$$
\lim_{x\to\pm\infty}u_x(x,t)=0,
$$
and hence
$$
M'(t)
=\left[u_x(x,t)\right]_{x=-\infty}^{x=\infty}
=0.
$$
Since $t_0$ was arbitrary, $M'(t)=0$ for all $t>0$.
:::

<1>2. For every $t>0$,
$$
M(t)=1.
$$

::: {.proof}
By step <1>1, $M$ is constant on the connected interval $(0,\infty)$.
The hypothesis gives $M(1)=1$, so the constant value is $1$.
:::

<1>3. For every $t>0$,
$$
S'(t)=2M(t).
$$

::: {.proof}
As in step <1>1, rapid decrease justifies differentiation under the
integral sign. Using $u_t=u_{xx}$ gives
$$
S'(t)
=\int_{-\infty}^{\infty}x^2u_{xx}(x,t)\,dx.
$$
Integrating by parts twice,
$$
\begin{aligned}
\int_{-\infty}^{\infty}x^2u_{xx}\,dx
&=\left[x^2u_x\right]_{-\infty}^{\infty}
  -2\int_{-\infty}^{\infty}x u_x\,dx\\
&=-2\left[xu\right]_{-\infty}^{\infty}
  +2\int_{-\infty}^{\infty}u\,dx\\
&=2M(t).
\end{aligned}
$$
All boundary terms vanish because $u$ and $u_x$ are rapidly decreasing
in $x$.
:::

<1>4. Therefore, for every $t>0$,
$$
\boxed{
\frac d{dt}\int_{-\infty}^{\infty}x^2u(x,t)\,dx=2
}.
$$

::: {.proof}
By step <1>3, the derivative is $2M(t)$, and step <1>2 gives
$M(t)=1$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the required identity.
:::
:::
