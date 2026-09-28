---
schema: qual/card@1
id: E-SS2.EX-14
kind: problem
title: "A pole on the circle of convergence and its coefficient growth"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
14. Suppose that f is holomorphic in an open set containing the closed unit disc, except for a pole at $z _ { \mathrm { 0 } }$ on the unit circle.
    Show that if

$$
\sum_ {n = 0} ^ {\infty} a _ {n} z ^ {n}
$$

denotes the power series expansion of $f$ in the open unit disc, then

$$
\lim _ {n \to \infty} \frac {a _ {n}}{a _ {n + 1}} = z _ {0}.
$$
:::

::: {.solution}
Let the pole of $f$ at $z_0$ have order $m\ge1$. Since $|z_0|=1$, write the principal part at $z_0$ as
\[
\sum_{k=1}^m \frac{c_{-k}}{(z-z_0)^k},
\qquad c_{-m}\ne0.
\]
Subtracting this principal part from $f$ removes the only singularity on the closed unit disc. Thus
\[
h(z)=f(z)-\sum_{k=1}^m \frac{c_{-k}}{(z-z_0)^k}
\]
is holomorphic on a neighborhood of the closed unit disc. Hence there is some $\rho>1$ such that $h$ is holomorphic on $|z|<\rho$, and if
\[
h(z)=\sum_{n\ge0}b_nz^n,
\]
then Cauchy's estimates give $b_n=O(\rho^{-n})$.

For $|z|<1$,
\[
\frac1{(z-z_0)^k}
=(-1)^kz_0^{-k}\left(1-\frac z{z_0}\right)^{-k}
=(-1)^kz_0^{-k}\sum_{n\ge0}\binom{n+k-1}{k-1}z^nz_0^{-n}.
\]
Therefore
\[
a_n=z_0^{-n}P(n)+b_n,
\tag{1}
\]
where
\[
P(n)=\sum_{k=1}^m(-1)^kc_{-k}z_0^{-k}\binom{n+k-1}{k-1}
\]
is a polynomial in $n$ of degree $m-1$, with nonzero leading coefficient because $c_{-m}\ne0$.

Thus $P(n)\sim Cn^{m-1}$ for some $C\ne0$, while $b_n=O(\rho^{-n})$. From (1),
\[
\frac{a_n}{a_{n+1}}
=z_0\,
\frac{P(n)+z_0^n b_n}{P(n+1)+z_0^{n+1}b_{n+1}}.
\]
Since $|z_0|=1$, the error terms are exponentially small compared with $P(n)$, and
\[
\frac{P(n)}{P(n+1)}\longrightarrow1.
\]
Hence
\[
\boxed{\displaystyle \lim_{n\to\infty}\frac{a_n}{a_{n+1}}=z_0}.
\]
:::
