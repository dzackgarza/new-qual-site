---
schema: qual/card@1
id: E-SS7.PR-1
kind: problem
title: Mean square of a Dirichlet series with bounded coefficients, and uniqueness of coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Dirichlet Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
1. Let $\textstyle F ( s ) = \sum _ { n = 1 } ^ { \infty } a _ { n } / n ^ { s }$ , where $| a _ { n } | \leq M$ for all n.

(a) Then

$$
\lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} | F (\sigma + i t) | ^ {2} d t = \sum_ {n = 1} ^ {\infty} \frac {| a _ {n} | ^ {2}}{n ^ {2 \sigma}} \quad \text { if } \sigma > 1.
$$

How is this reminiscent of the Parseval-Plancherel theorem?
See e.g. Chapter 3 in Book I.

(b) Show as a consequence the uniqueness of Dirichlet series: If $\scriptstyle F ( s ) = \sum _ { n = 1 } ^ { \infty } a _ { n } n ^ { - s }$ where the coeficients are assumed to satisfy $| a _ { n } | \leq c n ^ { k }$ for some k, and $F ( s ) \equiv 0$ , then $a _ { n } = 0$ for all n.

Hint: For part (a) use the fact that

$$
\frac {1}{2 T} \int_ {- T} ^ {T} (n m) ^ {- \sigma} n ^ {- i t} m ^ {i t}   d t \to \left\{ \begin{array}{l l} n ^ {- 2 \sigma} & \text {if} n = m, \\ 0 & \text {if} n \neq m. \end{array} \right.
$$
:::

::: {.solution}
For Problem 1(a), assume first $\sigma>1$.
Since $|a_n|\le M$, the series for $F(\sigma+it)$ converges absolutely and uniformly in $t$.
Hence
\[
|F(\sigma+it)|^2
=\sum_{n,m\ge1}a_n\overline{a_m}(nm)^{-\sigma}e^{-it\log(n/m)},
\]
and the double series is absolutely summable because
\[
\sum_{n,m\ge1}|a_na_m|(nm)^{-\sigma}
\le M^2\zeta(\sigma)^2<\infty.
\]
Therefore we may integrate termwise:
\[
\frac1{2T}\int_{-T}^T|F(\sigma+it)|^2\,dt
=\sum_{n,m\ge1}a_n\overline{a_m}(nm)^{-\sigma}K_T(n,m),
\]
where
\[
K_T(n,m)=\frac1{2T}\int_{-T}^Te^{-it\log(n/m)}\,dt.
\]
If $n=m$, then $K_T(n,n)=1$.
If $n\ne m$, then
\[
K_T(n,m)=\frac{\sin(T\log(n/m))}{T\log(n/m)}\longrightarrow0.
\]
Also $|K_T(n,m)|\le1$.
Dominated convergence for the absolutely summable double series therefore gives
\[
\lim_{T\to\infty}\frac1{2T}\int_{-T}^T|F(\sigma+it)|^2\,dt
=\sum_{n=1}^\infty\frac{|a_n|^2}{n^{2\sigma}}.
\]
This is the Dirichlet-series analogue of Parseval--Plancherel: averaging in the vertical variable kills the cross terms and leaves the square sum of the coefficients.

For Problem 1(b), suppose
\[
F(s)=\sum_{n\ge1}a_nn^{-s}\equiv0,
\qquad |a_n|\le cn^k.
\]
Set $b_n=a_nn^{-k}$ and
\[
G(s)=F(s+k)=\sum_{n\ge1}b_nn^{-s}.
\]
Then $|b_n|\le c$ and $G\equiv0$.
Applying part (a), for every $\sigma>1$,
\[
0=\lim_{T\to\infty}\frac1{2T}\int_{-T}^T|G(\sigma+it)|^2\,dt
=\sum_{n=1}^\infty\frac{|b_n|^2}{n^{2\sigma}}.
\]
Every term on the right is nonnegative, so every $b_n=0$, hence every $a_n=0$.
This proves uniqueness of Dirichlet series under the stated polynomial growth condition.
:::
