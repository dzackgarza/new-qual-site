---
schema: qual/card@1
id: P-BERK80S-19
kind: problem
title: A positive-coefficient meromorphic series has a positive real pole
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 19 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the ambient field notation as $\mathbb C$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the radius-of-convergence argument, the local disk crossing the positive boundary point, and the nonnegative-term rearrangement forcing convergence beyond the assumed radius.
---

::: {.problem}
Let $f$ be a meromorphic function on $\mathbb C$ which is analytic in a neighborhood of $0$.
Let its Maclaurin series be

$$
\sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }
$$

with all $a _ { k } \geqslant 0$ . Suppose there is a pole of modulus $r > 0$ and no pole has modulus $< r$ . Prove there is a pole at $z = r$
:::

::: {.solution}
Let
\[
f(z)=\sum_{n=0}^\infty a_n z^n,
\qquad a_n\ge0,
\]
near $0$.
Because $f$ is meromorphic and there is a pole of modulus $r$ with no pole of smaller modulus, the radius of convergence of this Maclaurin series is exactly $r$.
We prove that $z=r$ itself must be a pole.

<1>1. If $f$ were analytic at $r$, then it would be analytic on a disk centered at a point $x<r$ whose radius crosses the circle $|z|=r$.
::: {.proof}
Assume, toward a contradiction, that $f$ is not singular at $r$.
Since $f$ is meromorphic, this means that $f$ is analytic in some disk
\[
D(r,\delta)
\]
with $\delta>0$.
It is already analytic in $D(0,r)$, the disk of convergence of its Maclaurin series.

Choose $\varepsilon>0$ with
\[
3\varepsilon<\delta
\]
and set
\[
x=r-\varepsilon.
\]
We claim that
\[
D(x,2\varepsilon)\subset D(0,r)\cup D(r,\delta).
\]
Indeed, if $z\in D(x,2\varepsilon)$ and $|z|<r$, then $z\in D(0,r)$.
Otherwise $|z|\ge r$, and
\[
|z-r|\le |z-x|+|x-r|<2\varepsilon+\varepsilon=3\varepsilon<\delta,
\]
so $z\in D(r,\delta)$.
Thus $f$ is analytic throughout $D(x,2\varepsilon)$.
:::

<1>2. All Taylor coefficients of $f$ about the positive point $x$ are nonnegative.
::: {.proof}
Since $0<x<r$, the Maclaurin series may be differentiated term by term at $x$.
For every $k\ge0$,
\[
\frac{f^{(k)}(x)}{k!}
=\sum_{n=k}^\infty \binom nk a_n x^{n-k}.
\]
Every summand is nonnegative because $a_n\ge0$ and $x>0$.
Hence
\[
\frac{f^{(k)}(x)}{k!}\ge0
\qquad(k\ge0).
\]
:::

<1>3. Analyticity across $r$ forces the original Maclaurin series to converge at a point larger than $r$.
::: {.proof}
Choose
\[
h=\frac32\varepsilon.
\]
Then $0<h<2\varepsilon$, so the Taylor series of $f$ about $x$ converges at $x+h$.
Also
\[
x+h=r-\varepsilon+\frac32\varepsilon
=r+\frac12\varepsilon>r.
\]
By <1>2 all terms in the relevant double series are nonnegative, so Tonelli's theorem for series permits rearrangement:
\[
\begin{aligned}
f(x+h)
&=\sum_{k=0}^\infty \frac{f^{(k)}(x)}{k!}h^k\\
&=\sum_{k=0}^\infty\sum_{n=k}^\infty
\binom nk a_n x^{n-k}h^k\\
&=\sum_{n=0}^\infty a_n
\sum_{k=0}^n\binom nk x^{n-k}h^k\\
&=\sum_{n=0}^\infty a_n(x+h)^n.
\end{aligned}
\]
The left-hand side is finite, so the Maclaurin series converges at the positive real point $x+h>r$.
This contradicts the fact that its radius of convergence is exactly $r$.
:::

<1>4. Therefore $z=r$ is a pole.
::: {.proof}
The contradiction in <1>3 shows that $f$ cannot be analytic at $r$.
Since $f$ is meromorphic on $\mathbb C$, every finite singularity is a pole.
Hence $z=r$ is a pole.
:::
:::
