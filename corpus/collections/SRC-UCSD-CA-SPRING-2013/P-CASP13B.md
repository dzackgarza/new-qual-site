---
schema: qual/card@1
id: P-CASP13B
kind: problem
title: "True or False: harmonic critical points, Mittag-Leffler interpolation, harmonic limits, and polynomial approximation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-18
  note: Read against the UCSD Complex Analysis Qualifying Exam, Spring 2013; all four items match.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    No retained solution set covers this examination. Structured the card's own answers:
    the disconnected-domain counterexample, the order-zero pole defect, the mean-value
    limit for harmonic functions, and the residue obstruction on |z|=5/2.
---

::: {.problem}
Determine if the following statements are True or False.

(a) Let $U \subseteq \CC$ be an open set, and let $u: U \to \RR$ be a non-constant harmonic function.
Set $Z = \{z \in U : u_x(z) = u_y(z) = 0\}$.
It is possible for $Z$ to have an accumulation point in $U$.

(b) There is a meromorphic function $f$ on $\CC \setminus (2\ZZ)^2$ such that, if $n, m \in 2\ZZ$ are even integers, then $f$ has a pole of order $n^2 + m^2$ at $(n, m)$, and if $(n, m) \in \ZZ \times \ZZ$ with at least one odd, then $f$ has a zero of order $n^2 + m^2$ at $(n, m)$.

(c) Let $\{u_n\}$ be a sequence of harmonic functions in $\DD$.
If $u_n$ converges to $u$ uniformly on compact subsets, then $u$ is harmonic on $\DD$.

(d) There is a sequence of holomorphic polynomials $p_n$ such that $$\lim_{n \to \infty} \sup_{2 \leq \abs{z} \leq 3} \abs{\frac{1}{z^2(z-5)^3} - p_n(z)} = 0.$$
:::

::: {.solution}

No retained solution set covers this examination; the argument below is the card's own.

::: pf

::: {.pf-step #a-true}
Statement (a) is true.

::: pf-proof
Take $U=D(0,1)\cup D(3,1)$ and set $u=0$ on the first disk and $u(z)=\operatorname{Re}z$ on the second. Each restriction is harmonic, so $u$ is harmonic on the disconnected open set $U$, and $u$ is nonconstant. On $D(0,1)$ both partial derivatives vanish, so this disk lies in $Z$; every point of the disk is then an accumulation point of $Z$ in $U$.
:::
:::

::: {.pf-step #b-false}
Statement (b) is false.

::: pf-proof
At $(n,m)=(0,0)$, both coordinates are even and $n^2+m^2=0$. A pole of order $0$ is not defined; poles have positive integer order. Therefore no meromorphic function can satisfy the stated order condition at the origin.
:::
:::

::: {.pf-step #c-true}
Statement (c) is true.

::: pf-proof
Fix a closed disk $\overline{B(a,r)}\subset\DD$. Each $u_n$ has the mean-value property
$$
u_n(a)=\frac1{2\pi}\int_0^{2\pi}u_n(a+re^{it})\,dt.
$$
Since $u_n\to u$ uniformly on the compact circle, passage to the limit gives the same identity for $u$. Thus $u$ has the mean-value property on a neighborhood of every point; by Weyl's mean-value characterization it is harmonic.
:::
:::

::: {.pf-step #d-false}
Statement (d) is false.

::: pf-proof
If polynomials $p_n$ converged uniformly to $h(z)=1/(z^2(z-5)^3)$ on $2\le\abs z\le3$, then on $\abs z=5/2$ we could interchange limits and integrals:
$$
0=\int_{\abs z=5/2}p_n(z)\,dz\longrightarrow\int_{\abs z=5/2}h(z)\,dz
=2\pi i\operatorname{Res}_{z=0}h(z).
$$
The residue at $0$ of $z^{-2}(z-5)^{-3}$ is the coefficient of $z$ in $(z-5)^{-3}$, namely $-3(-5)^{-4}= -3/625\ne0$. The limiting integral is therefore nonzero, a contradiction.
:::
:::

:::
:::
