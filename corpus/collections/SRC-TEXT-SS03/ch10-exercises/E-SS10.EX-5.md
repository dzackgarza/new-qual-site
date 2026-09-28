---
schema: qual/card@1
id: E-SS10.EX-5
kind: problem
title: "SS 10.5: Logarithmic asymptotics of the partition generating function"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
5. Let

$$
F (x) = \sum_ {n = 0} ^ {\infty} p (n) x ^ {n} = \prod_ {n = 1} ^ {\infty} \frac {1}{1 - x ^ {n}}
$$

be the generating function for the partitions.
Show that

$$
\log F (x) \sim \frac {\pi^ {2}}{6 (1 - x)} \quad \mathrm{as} x \to 1, \mathrm{with} 0 <   x <   1.
$$

[Hint: Use log $\textstyle F ( x ) = \sum \log ( 1 / ( 1 - x ^ { n } ) )$ and log $\textstyle ( 1 / ( 1 - x ^ { n } ) ) = \sum ( 1 / m ) x ^ { n m }$ , so

$$
\log F (x) = \sum {\frac {1}{m}} {\frac {x ^ {m}}{1 - x ^ {m}}}.
$$

Use also $m x ^ { m - 1 } ( 1 - x ) < 1 - x ^ { m } < m ( 1 - x ) . ]$
:::

::: {.solution}
For \(0<x<1\), absolute convergence allows us to expand and rearrange:
\[
\begin{aligned}
\log F(x)
&=\sum_{n=1}^\infty -\log(1-x^n)\\
&=\sum_{n=1}^\infty\sum_{m=1}^\infty\frac{x^{nm}}m
=\sum_{m=1}^\infty\frac1m\frac{x^m}{1-x^m}.
\end{aligned}
\tag{1}
\]
The elementary inequalities from the hint are
\[
m x^{m-1}(1-x)\le 1-x^m\le m(1-x).
\]
Applying them termwise to (1) yields
\[
\frac{x^m}{m^2}
\le
(1-x)\frac1m\frac{x^m}{1-x^m}
\le
\frac{x}{m^2}.
\]
Summing over \(m\),
\[
\sum_{m=1}^\infty\frac{x^m}{m^2}
\le (1-x)\log F(x)
\le x\sum_{m=1}^\infty\frac1{m^2}.
\]
As \(x\uparrow1\), dominated convergence gives
\[
\sum_{m=1}^\infty\frac{x^m}{m^2}\longrightarrow\zeta(2)=\frac{\pi^2}{6},
\]
and the right-hand side has the same limit. Hence
\[
(1-x)\log F(x)\longrightarrow\frac{\pi^2}{6},
\]
which is exactly
\[
\boxed{\log F(x)\sim\frac{\pi^2}{6(1-x)}}.
\]
:::
