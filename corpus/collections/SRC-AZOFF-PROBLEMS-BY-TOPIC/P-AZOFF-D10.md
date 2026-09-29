---
schema: qual/card@1
id: P-AZOFF-D10
kind: problem
title: Liouville's theorem via Cauchy's formula
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used Cauchy's derivative formula on arbitrarily large circles. The
    boundedness estimate tends to zero as the radius grows, and a
    line-segment argument then proves constancy.
---

::: {.problem}
Suppose $f : \mathbb { C } \to \mathbb { C }$ is entire and bounded.
Use Cauchy’s formula to prove that $f ^ { \prime }$ is identically zero and hence that $f$ is constant.
This is Liouville’s Theorem.
:::

::: {.solution}
Choose $M\geq0$ such that
$$
\abs{f(z)}\leq M
$$
for every $z\in\CC$.

::: pf

::: {.pf-step #s1}

Fix $z_0\in\CC$. For every $R>0$,
$$
f'(z_0)
=
\frac{1}{2\pi i}
\int_{\abs{\zeta-z_0}=R}
\frac{f(\zeta)}{(\zeta-z_0)^2}
\,d\zeta.
$$

::: pf-proof

Because $f$ is entire, it is analytic on and inside every circle centered at
$z_0$. Cauchy's formula for the first derivative gives the identity.

:::

:::

::: {.pf-step #s2}

For every $R>0$,
$$
\abs{f'(z_0)}\leq\frac{M}{R}.
$$

::: pf-proof

On $\abs{\zeta-z_0}=R$, one has $\abs{f(\zeta)}\leq M$. The circle has
length $2\pi R$, so step [](#s1){.pf-ref} gives
$$
\begin{aligned}
\abs{f'(z_0)}
&\leq
\frac{1}{2\pi}(2\pi R)\frac{M}{R^2}\\
&=
\frac{M}{R}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

One has $f'(z_0)=0$.

::: pf-proof

Step [](#s2){.pf-ref} holds for every $R>0$. Letting $R\to\infty$ gives
$\abs{f'(z_0)}=0$.

:::

:::

::: {.pf-step #s4}

The derivative $f'$ is identically zero on $\CC$.

::: pf-proof

The point $z_0\in\CC$ was arbitrary, so step [](#s3){.pf-ref} applies at every point.

:::

:::

::: {.pf-step #s5}

The function $f$ is constant.

::: pf-proof

Let $z_1,z_2\in\CC$ and define
$$
h(t)=f\bigl(z_1+t(z_2-z_1)\bigr),
\qquad 0\leq t\leq1.
$$
By the chain rule and step [](#s4){.pf-ref},
$$
h'(t)
=
f'\bigl(z_1+t(z_2-z_1)\bigr)(z_2-z_1)
=
0.
$$
Thus $h$ is constant on $[0,1]$, and therefore
$$
f(z_2)=h(1)=h(0)=f(z_1).
$$
Since $z_1$ and $z_2$ were arbitrary, $f$ is constant.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give the two requested conclusions.

:::

:::

:::
