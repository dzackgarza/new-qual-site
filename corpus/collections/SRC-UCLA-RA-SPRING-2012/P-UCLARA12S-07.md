---
schema: qual/card@1
id: P-UCLARA12S-07
kind: problem
title: Decreasing limits of positive harmonic functions
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $(u_n)$ be a sequence of real-valued harmonic functions on the unit disc $\mathbb D$ satisfying
\[
u_1(z)\ge u_2(z)\ge\cdots\ge0
\]
for every $z\in\mathbb D$.
Prove that $z\mapsto\inf_n u_n(z)$ is harmonic on $\mathbb D$.
:::

::: {.solution}
Define
$$
u(z)\coloneqq\inf_nu_n(z)=\lim_{n\to\infty}u_n(z).
$$
The pointwise limit exists because $(u_n(z))$ is decreasing and bounded below by $0$.

<1>1. The sequence $(u_n)$ is uniformly Cauchy on every compact subset of $\mathbb D$.

::: {.proof}
Fix $0<r<1$, and choose $r<\rho<1$. If $n>m$, then
$$
h_{m,n}\coloneqq u_m-u_n
$$
is a nonnegative harmonic function on $\mathbb D$. Harnack's inequality on the disc $\abs z<\rho$ gives, for $\abs z\le r$,
$$
0\le h_{m,n}(z)
\le
\frac{\rho+r}{\rho-r}h_{m,n}(0).
$$
Since the decreasing bounded sequence $(u_n(0))$ converges,
$$
h_{m,n}(0)=u_m(0)-u_n(0)\longrightarrow0
$$
as $m,n\to\infty$. The displayed Harnack bound is uniform for $\abs z\le r$, so $(u_n)$ is uniformly Cauchy on every closed disc centered at $0$ contained in $\mathbb D$. Every compact subset of $\mathbb D$ lies in such a disc.
:::

<1>2. The convergence $u_n\to u$ is locally uniform, and $u$ is continuous.

::: {.proof}
Step <1>1 gives uniform convergence on each compact subset because $\RR$ is complete. A locally uniform limit of continuous functions is continuous, and each $u_n$ is continuous because it is harmonic.
:::

<1>3. The function $u$ satisfies the mean-value property on every closed disc contained in $\mathbb D$.

::: {.proof}
Let
$$
\overline{B(z_0,s)}\subset\mathbb D.
$$
For every $n$, harmonicity gives
$$
u_n(z_0)
=
\frac1{2\pi}
\int_0^{2\pi}
u_n(z_0+se^{i\theta})\,d\theta.
$$
By step <1>2, $u_n\to u$ uniformly on the compact circle
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

<1>4. The function $u$ is harmonic on $\mathbb D$.

::: {.proof}
By step <1>2, $u$ is continuous, and by step <1>3 it satisfies the mean-value property on every sufficiently small circle. The converse mean-value theorem therefore implies that $u$ is harmonic.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves that $z\mapsto\inf_nu_n(z)$ is harmonic on $\mathbb D$.
:::
:::
