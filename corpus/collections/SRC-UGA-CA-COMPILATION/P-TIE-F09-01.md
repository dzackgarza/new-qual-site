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
(1) Assume $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $| z | < R .$ . Show that for $r < R ,$

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } | f ( r e ^ { i \theta } ) | ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

(2) Deduce Liouville’s theorem from (1).
:::

::: {.solution}
Fix $0<r<R$.

<1>1. On $|z|=r$, the series
$$
f(re^{i\theta})
=
\sum_{n=0}^{\infty}c_nr^ne^{in\theta}
$$
converges absolutely and uniformly in $\theta\in[0,2\pi]$.

::: {.proof}
Choose $\rho$ with
$$
r<\rho<R.
$$
Since the power series converges absolutely at $z=\rho$,
$$
\sum_{n=0}^{\infty}|c_n|\rho^n<\infty.
$$
For every $\theta$,
$$
|c_nr^ne^{in\theta}|
=
|c_n|r^n
\le
|c_n|\rho^n.
$$
The Weierstrass $M$-test therefore gives absolute uniform convergence.
:::

<1>2. One has
$$
|f(re^{i\theta})|^2
=
\sum_{n,m\ge0}
c_n\overline{c_m}\,
r^{n+m}e^{i(n-m)\theta},
$$
and the double series may be integrated term by term on $[0,2\pi]$.

::: {.proof}
By step <1>1,
$$
\sum_{n=0}^{\infty}|c_n|r^n<\infty.
$$
Hence
$$
\sum_{n,m\ge0}
|c_n|\,|c_m|\,r^{n+m}
=
\left(\sum_{n\ge0}|c_n|r^n\right)^2
<\infty.
$$
Thus the product of the two uniformly absolutely convergent series for
$f(re^{i\theta})$ and its complex conjugate is itself uniformly absolutely
convergent, so termwise integration is valid.
:::

<1>3. For integers $n,m\ge0$,
$$
\frac1{2\pi}\int_0^{2\pi}e^{i(n-m)\theta}\,d\theta
=
\begin{cases}
1,&n=m,\\
0,&n\ne m.
\end{cases}
$$

::: {.proof}
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

<1>4. Parseval's identity in the problem holds:
$$
\boxed{
\frac1{2\pi}\int_0^{2\pi}|f(re^{i\theta})|^2\,d\theta
=
\sum_{n=0}^{\infty}|c_n|^2r^{2n}
}.
$$

::: {.proof}
Integrate the expansion from step <1>2 term by term. By step <1>3, every term with
$n\ne m$ integrates to zero, while the term with $n=m$ contributes
$|c_n|^2r^{2n}$.
:::

<1>5. If $f$ is entire and bounded, then every coefficient $c_n$ with $n\ge1$ vanishes.

::: {.proof}
Suppose
$$
|f(z)|\le M
\qquad
\text{for all }z\in\CC.
$$
Since an entire function has radius of convergence $R=\infty$, step <1>4 applies for every
$r>0$ and gives
$$
\sum_{k=0}^{\infty}|c_k|^2r^{2k}
=
\frac1{2\pi}\int_0^{2\pi}|f(re^{i\theta})|^2\,d\theta
\le M^2.
$$
For each fixed $n\ge1$,
$$
|c_n|^2r^{2n}\le M^2
\qquad
\text{for every }r>0.
$$
Therefore
$$
|c_n|\le \frac{M}{r^n}.
$$
Letting $r\to\infty$ yields $c_n=0$.
:::

<1>6. Every bounded entire function is constant.

::: {.proof}
By step <1>5,
$$
f(z)=c_0.
$$
This is Liouville's theorem.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>4 proves part (1), and step <1>6 proves part (2).
:::
:::
