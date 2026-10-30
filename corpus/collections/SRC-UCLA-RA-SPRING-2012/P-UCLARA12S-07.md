---
schema: qual/card@1
id: P-UCLARA12S-07
kind: problem
title: Decreasing limits of positive harmonic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $(u_n)$ be a sequence of real-valued harmonic functions on the unit disc $\DD$ satisfying
$$
u_1(z)\ge u_2(z)\ge\cdots\ge0
$$
for every $z\in\DD$.
Prove that $z\mapsto\inf_n u_n(z)$ is harmonic on $\DD$.
:::

::: {.solution}

Define
$$
u(z)\coloneqq\inf_nu_n(z)=\lim_{n\to\infty}u_n(z).
$$
The pointwise limit exists because $(u_n(z))$ is decreasing and bounded below by $0$.

::: pf

::: {.pf-step #s1-1}

The sequence $(u_n)$ is uniformly Cauchy on every compact subset of $\DD$.


::: pf-proof

Fix $0<r<1$, and choose $r<\rho<1$. If $n>m$, then
$$
h_{m,n}\coloneqq u_m-u_n
$$
is a nonnegative harmonic function on $\DD$. Harnack's inequality on the disc $\abs z<\rho$ gives, for $\abs z\le r$,
$$
0\le h_{m,n}(z)
\le
\frac{\rho+r}{\rho-r}h_{m,n}(0).
$$
Since the decreasing bounded sequence $(u_n(0))$ converges,
$$
h_{m,n}(0)=u_m(0)-u_n(0)\longrightarrow0
$$
as $m,n\to\infty$. The displayed Harnack bound is uniform for $\abs z\le r$, so $(u_n)$ is uniformly Cauchy on every closed disc centered at $0$ contained in $\DD$. Every compact subset of $\DD$ lies in such a disc.

:::

:::

::: {.pf-step #s1-2}

The convergence $u_n\to u$ is locally uniform, and $u$ is continuous.


::: pf-proof

Step [](#s1-1){.pf-ref} gives uniform convergence on each compact subset because $\RR$ is complete. A locally uniform limit of continuous functions is continuous, and each $u_n$ is continuous because it is harmonic.

:::

:::

::: {.pf-step #s1-3}

The function $u$ satisfies the mean-value property on every closed disc contained in $\DD$.


::: pf-proof

Let
$$
\overline{B(z_0,s)}\subset\DD.
$$
For every $n$, harmonicity gives
$$
u_n(z_0)
=
\frac1{2\pi}
\int_0^{2\pi}
u_n(z_0+se^{i\theta})\,d\theta.
$$
By step [](#s1-2){.pf-ref}, $u_n\to u$ uniformly on the compact circle
$$
\{z_0+se^{i\theta}:0\le\theta\le2\pi\}.
$$
Therefore the limit may be passed through the integral:
$$
u(z_0)
=
\frac1{2\pi}
\int_0^{2\pi}
u(z_0+se^{i\theta})\,d\theta.
$$

:::

:::

::: {.pf-step #s1-4}

The function $u$ is harmonic on $\DD$.


::: pf-proof

By step [](#s1-2){.pf-ref}, $u$ is continuous, and by step [](#s1-3){.pf-ref} it satisfies the mean-value property on every sufficiently small circle. The converse mean-value theorem therefore implies that $u$ is harmonic.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves that $z\mapsto\inf_nu_n(z)$ is harmonic on $\DD$.

:::

:::

:::
