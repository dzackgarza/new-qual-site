---
schema: qual/card@1
id: P-TIE-F09-01
kind: problem
title: Parseval's identity for power series and Liouville's theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 1.
---

::: {.problem}
(1) Assume $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $\abs{ z } < R .$ . Show that for $r < R ,$

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \abs{ f ( r e ^ { i \theta } ) } ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } \abs{ c _ { n } } ^ { 2 } r ^ { 2 n } .
$$

(2) Deduce Liouville’s theorem from (1).
:::

::: {.solution}

Fix $0<r<R$.

::: pf

::: {.pf-step #s1-1}

On $\abs{z}=r$, the series
$$
f(re^{i\theta})
=
\sum_{n=0}^{\infty}c_nr^ne^{in\theta}
$$
converges absolutely and uniformly in $\theta\in[0,2\pi]$.


::: pf-proof

Choose $\rho$ with
$$
r<\rho<R.
$$
Since the power series converges absolutely at $z=\rho$,
$$
\sum_{n=0}^{\infty}\abs{c_n}\rho^n<\infty.
$$
For every $\theta$,
$$
\abs{c_nr^ne^{in\theta}}
=
\abs{c_n}r^n
\le
\abs{c_n}\rho^n.
$$
The Weierstrass $M$-test therefore gives absolute uniform convergence.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\abs{f(re^{i\theta})}^2
=
\sum_{n,m\ge0}
c_n\overline{c_m}\,
r^{n+m}e^{i(n-m)\theta},
$$
and the double series may be integrated term by term on $[0,2\pi]$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\sum_{n=0}^{\infty}\abs{c_n}r^n<\infty.
$$
Hence
$$
\sum_{n,m\ge0}
\abs{c_n}\,\abs{c_m}\,r^{n+m}
=
\left(\sum_{n\ge0}\abs{c_n}r^n\right)^2
<\infty.
$$
Thus the product of the two uniformly absolutely convergent series for
$f(re^{i\theta})$ and its complex conjugate is itself uniformly absolutely
convergent, so termwise integration is valid.

:::

:::

::: {.pf-step #s1-3}

For integers $n,m\ge0$,
$$
\frac1{2\pi}\int_0^{2\pi}e^{i(n-m)\theta}\,d\theta
=
\begin{cases}
1,&n=m,\\
0,&n\ne m.
\end{cases}
$$


::: pf-proof

If $n=m$, the integrand is $1$. If $n\ne m$, direct integration gives
$$
\int_0^{2\pi}e^{i(n-m)\theta}\,d\theta
=
\left[
\frac{e^{i(n-m)\theta}}{i(n-m)}
\right]_0^{2\pi}
=0.
$$

:::

:::

::: {.pf-step #s1-4}

Parseval's identity in the problem holds:
$$
\boxed{
\frac1{2\pi}\int_0^{2\pi}\abs{f(re^{i\theta})}^2\,d\theta
=
\sum_{n=0}^{\infty}\abs{c_n}^2r^{2n}
}.
$$


::: pf-proof

Integrate the expansion from step [](#s1-2){.pf-ref} term by term. By step [](#s1-3){.pf-ref}, every term with
$n\ne m$ integrates to zero, while the term with $n=m$ contributes
$\abs{c_n}^2r^{2n}$.

:::

:::

::: {.pf-step #s1-5}

If $f$ is entire and bounded, then every coefficient $c_n$ with $n\ge1$ vanishes.


::: pf-proof

Suppose
$$
\abs{f(z)}\le M
\qquad
\text{for all }z\in\CC.
$$
Since an entire function has radius of convergence $R=\infty$, step [](#s1-4){.pf-ref} applies for every
$r>0$ and gives
$$
\sum_{k=0}^{\infty}\abs{c_k}^2r^{2k}
=
\frac1{2\pi}\int_0^{2\pi}\abs{f(re^{i\theta})}^2\,d\theta
\le M^2.
$$
For each fixed $n\ge1$,
$$
\abs{c_n}^2r^{2n}\le M^2
\qquad
\text{for every }r>0.
$$
Therefore
$$
\abs{c_n}\le \frac{M}{r^n}.
$$
Letting $r\to\infty$ yields $c_n=0$.

:::

:::

::: {.pf-step #s1-6}

Every bounded entire function is constant.


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
f(z)=c_0.
$$
This is Liouville's theorem.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (1), and step [](#s1-6){.pf-ref} proves part (2).

:::

:::

:::
