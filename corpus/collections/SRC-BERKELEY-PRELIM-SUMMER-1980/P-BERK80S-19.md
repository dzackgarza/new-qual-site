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
Let $f$ be a meromorphic function on $\CC$ which is analytic in a neighborhood of $0$.
Let its Maclaurin series be

$$
\sum_{k=0}^{\infty}a_kz^k
$$

with all $a_k\geqslant0$. Suppose there is a pole of modulus $r>0$ and no pole has modulus $<r$. Prove there is a pole at $z=r$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The Maclaurin series $\sum_n a_nz^n$ has radius of convergence
exactly $r$, and $f$ is analytic on $D(0,r)$.

::: pf-proof

The function $f$ has no pole in $D(0,r)$, so it is analytic there and its
Maclaurin series converges on $D(0,r)$. The series cannot converge on a
larger disk, because its sum would then be analytic near the pole of
modulus $r$.

:::

:::

::: {.pf-step #s2}

$f$ is not analytic at $r$.

::: pf-proof

::: {.pf-step #s2-1}

Suppose, toward a contradiction, that $f$ is analytic on $D(r,\delta)$
for some $\delta>0$. Fix $\varepsilon$ with $0<3\varepsilon<\delta$ and
put $x=r-\varepsilon$. Then $f$ is analytic on $D(x,2\varepsilon)$.

::: pf-proof

It suffices to show
$$
D(x,2\varepsilon)\subset D(0,r)\cup D(r,\delta),
$$
since $f$ is analytic on both disks by step [](#s1){.pf-ref} and the assumption. If
$z\in D(x,2\varepsilon)$ and $\abs{z}<r$, then $z\in D(0,r)$. Otherwise,
$$
\abs{z-r}\le \abs{z-x}+\abs{x-r}<2\varepsilon+\varepsilon=3\varepsilon<\delta,
$$
so $z\in D(r,\delta)$.

:::

:::

::: {.pf-step #s2-2}

For every $k\ge0$,
$$
\frac{f^{(k)}(x)}{k!}
=\sum_{n=k}^\infty \binom nk a_n x^{n-k}\ge0.
$$

::: pf-proof

Since $0<x<r$, the Maclaurin series may be differentiated term by term at
$x$, which gives the displayed formula. Every summand is nonnegative
because $a_n\ge0$ and $x>0$.

:::

:::

::: {.pf-step #s2-3}

The Maclaurin series converges at $r+\tfrac12\varepsilon$.

::: pf-proof

Put $h=\tfrac32\varepsilon$. Then $0<h<2\varepsilon$, so by step [](#s2-1){.pf-ref} the
Taylor series of $f$ about $x$ converges at $x+h=r+\tfrac12\varepsilon$.
By step [](#s2-2){.pf-ref} all terms of the double series below are nonnegative, so
Tonelli's theorem for series permits rearrangement:
$$
\begin{aligned}
f(x+h)
&=\sum_{k=0}^\infty \frac{f^{(k)}(x)}{k!}h^k\\
&=\sum_{k=0}^\infty\sum_{n=k}^\infty
\binom nk a_n x^{n-k}h^k\\
&=\sum_{n=0}^\infty a_n
\sum_{k=0}^n\binom nk x^{n-k}h^k\\
&=\sum_{n=0}^\infty a_n(x+h)^n.
\end{aligned}
$$
The left-hand side is finite.

:::

:::

::: pf-qed

Step [](#s2-3){.pf-ref} gives convergence of the Maclaurin series at the real point
$r+\tfrac12\varepsilon>r$. A power series converging at a point converges
absolutely on the open disk of that radius, so its radius of convergence
exceeds $r$, contradicting step [](#s1){.pf-ref}.

:::

:::

:::

::: {.pf-step #s3}

$z=r$ is a pole of $f$.

::: pf-proof

Since $f$ is meromorphic on $\CC$, every point is either a point of
analyticity or a pole. Step [](#s2){.pf-ref} excludes the first case at $r$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
