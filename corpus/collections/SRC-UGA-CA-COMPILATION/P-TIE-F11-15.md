---
schema: qual/card@1
id: P-TIE-F11-15
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 15.
---

::: {.problem}
(1) Assume $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $| z | < R$ . Show that for $r < R$

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } | f ( r e ^ { i \theta } ) | ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

(2) Deduce Liouville’s theorem from (1).
:::

Fix $r<R$, and let
$$
S_N(z)\coloneqq\sum_{n=0}^N c_n z^n.
$$

::: pf

::: pf-step

The functions $S_N(re^{i\theta})$ converge uniformly to $f(re^{i\theta})$ for $0\le\theta\le2\pi$.


::: pf-proof

Choose $\rho$ with $r<\rho<R$. Since the power series converges absolutely at $\rho$,
$$
\sum_{n=0}^\infty \abs{c_n}\rho^n<\infty.
$$
For $\abs{z}=r$,
$$
\abs{c_nz^n}
\le
\abs{c_n}r^n
\le
\abs{c_n}\rho^n.
$$
The Weierstrass $M$-test therefore gives uniform convergence of $\sum c_nz^n$ on $\abs{z}=r$, hence uniform convergence of $S_N(re^{i\theta})$ to $f(re^{i\theta})$ on $[0,2\pi]$.

:::

:::

::: pf-step

For every $N$,
$$
\frac1{2\pi}
\int_0^{2\pi}
\abs{S_N(re^{i\theta})}^2\,d\theta
=
\sum_{n=0}^N\abs{c_n}^2r^{2n}.
$$


::: pf-proof

Since the sum is finite,
$$
\begin{aligned}
\abs{S_N(re^{i\theta})}^2
&=
\left(\sum_{n=0}^N c_nr^ne^{in\theta}\right)
\left(\sum_{m=0}^N \overline{c_m}r^me^{-im\theta}\right)\\
&=
\sum_{n=0}^N\sum_{m=0}^N
c_n\overline{c_m}r^{n+m}e^{i(n-m)\theta}.
\end{aligned}
$$
Moreover,
$$
\frac1{2\pi}\int_0^{2\pi}e^{i(n-m)\theta}\,d\theta
=
\begin{cases}
1,&n=m,\\
0,&n\ne m.
\end{cases}
$$
Integrating term by term leaves exactly the diagonal terms, giving the claimed identity.

:::

:::

::: pf-step

One has
$$
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
\abs{f(re^{i\theta})}^2\,d\theta
=
\sum_{n=0}^\infty\abs{c_n}^2r^{2n}.
}
$$


::: pf-proof

By step <1>1, $S_N(re^{i\theta})\to f(re^{i\theta})$ uniformly. The sequence $S_N(re^{i\theta})$ is therefore uniformly bounded, so
$$
\abs{S_N(re^{i\theta})}^2
\longrightarrow
\abs{f(re^{i\theta})}^2
$$
uniformly as well. Hence the integrals in step <1>2 converge to the left-hand side above. The right-hand side of step <1>2 is the $N$th partial sum of the nonnegative series
$$
\sum_{n=0}^\infty\abs{c_n}^2r^{2n},
$$
so taking $N\to\infty$ gives the displayed identity.

:::

:::

::: pf-step

If $f$ is entire and bounded by $M$, then for every $n\ge1$ and every $r>0$,
$$
\abs{c_n}\le \frac{M}{r^n}.
$$


::: pf-proof

Since $f$ is entire, step <1>3 applies for every $r>0$. If $\abs{f(z)}\le M$ on $\CC$, then
$$
\sum_{j=0}^\infty\abs{c_j}^2r^{2j}
=
\frac1{2\pi}
\int_0^{2\pi}
\abs{f(re^{i\theta})}^2\,d\theta
\le M^2.
$$
Every term in the nonnegative sum is therefore at most $M^2$. In particular,
$$
\abs{c_n}^2r^{2n}\le M^2,
$$
which gives the asserted estimate.

:::

:::

::: pf-step

Every bounded entire function is constant.


::: pf-proof

Fix $n\ge1$. By step <1>4,
$$
\abs{c_n}\le \frac{M}{r^n}
$$
for every $r>0$. Letting $r\to\infty$ gives $c_n=0$. Thus every coefficient except $c_0$ vanishes, so
$$
f(z)=c_0
$$
for all $z\in\CC$. This is Liouville's theorem.

:::

:::

::: pf-qed

Step <1>3 proves part (1), and step <1>5 proves part (2).

:::

:::
