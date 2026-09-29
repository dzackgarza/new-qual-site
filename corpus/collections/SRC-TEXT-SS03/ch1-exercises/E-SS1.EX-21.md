---
schema: qual/card@1
id: E-SS1.EX-21
kind: problem
title: Two dyadic series identities for $z/(1-z)$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Series
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Show that for $|z|<1$,
\[
\frac{z}{1-z^2}
+\frac{z^2}{1-z^4}
+\cdots
+\frac{z^{2^n}}{1-z^{2^{n+1}}}
+\cdots
=\frac{z}{1-z},
\]
and
\[
\frac{z}{1+z}
+\frac{2z^2}{1+z^2}
+\cdots
+\frac{2^kz^{2^k}}{1+z^{2^k}}
+\cdots
=\frac{z}{1-z}.
\]
Justify any change in the order of summation.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $k\ge0$ and $|z|<1$,
\[
\frac{z^{2^k}}{1-z^{2^{k+1}}}
=
\sum_{j=0}^{\infty}z^{2^k(2j+1)}.
\]

::: pf-proof

Since $|z^{2^{k+1}}|<1$, the geometric-series formula gives
\[
\frac{1}{1-z^{2^{k+1}}}
=
\sum_{j=0}^{\infty}z^{j2^{k+1}}.
\]
Multiplying by $z^{2^k}$ yields the stated expansion.

:::

:::

::: {.pf-step #s2}

Every positive integer $n$ can be written uniquely in the form
\[
n=2^k(2j+1),
\qquad k,j\in\mathbb Z_{\ge0}.
\]

::: pf-proof

Take $k$ to be the largest exponent such that $2^k$ divides $n$. Then $n/2^k$ is odd, hence equals $2j+1$ for a unique $j\ge0$. Maximality of $k$ gives uniqueness.

:::

:::

::: {.pf-step #s3}

The double series obtained from step [](#s1){.pf-ref} is absolutely convergent for $|z|<1$.

::: pf-proof

Put $r=|z|<1$. By step [](#s2){.pf-ref}, the exponents $2^k(2j+1)$, as $(k,j)$ ranges over nonnegative integers, run through every positive integer exactly once. Therefore
\[
\sum_{k=0}^{\infty}\sum_{j=0}^{\infty}
\left|z^{2^k(2j+1)}\right|
=
\sum_{n=1}^{\infty}r^n
=
\frac{r}{1-r}<\infty.
\]

:::

:::

::: pf-step

Hence
\[
\sum_{k=0}^{\infty}\frac{z^{2^k}}{1-z^{2^{k+1}}}
=
\frac{z}{1-z}.
\]

::: pf-proof

By step [](#s1){.pf-ref} and absolute convergence from step [](#s3){.pf-ref}, the double series may be rearranged. Using the bijection in step [](#s2){.pf-ref},
\[
\sum_{k=0}^{\infty}\sum_{j=0}^{\infty}z^{2^k(2j+1)}
=
\sum_{n=1}^{\infty}z^n
=
\frac{z}{1-z}.
\]

:::

:::

::: {.pf-step #s5}

For every $k\ge0$ and $|z|<1$,
\[
\frac{2^kz^{2^k}}{1+z^{2^k}}
=
\frac{2^kz^{2^k}}{1-z^{2^k}}
-
\frac{2^{k+1}z^{2^{k+1}}}{1-z^{2^{k+1}}}.
\]

::: pf-proof

For any $x\ne\pm1$,
\[
\frac{x}{1+x}
=
\frac{x}{1-x}-\frac{2x^2}{1-x^2}.
\]
Apply this with $x=z^{2^k}$ and multiply by $2^k$.

:::

:::

::: {.pf-step #s6}

The $N$th partial sum of the second series is
\[
\sum_{k=0}^{N}\frac{2^kz^{2^k}}{1+z^{2^k}}
=
\frac{z}{1-z}
-
\frac{2^{N+1}z^{2^{N+1}}}{1-z^{2^{N+1}}}.
\]

::: pf-proof

Set
\[
A_k=\frac{2^kz^{2^k}}{1-z^{2^k}}.
\]
By step [](#s5){.pf-ref}, the $k$th summand is $A_k-A_{k+1}$. The finite sum therefore telescopes to $A_0-A_{N+1}$, and $A_0=z/(1-z)$.

:::

:::

::: {.pf-step #s7}

For $|z|<1$,
\[
\frac{2^{N+1}z^{2^{N+1}}}{1-z^{2^{N+1}}}\longrightarrow0.
\]

::: pf-proof

Let $r=|z|<1$. For all sufficiently large $N$, $r^{2^{N+1}}\le1/2$, so
\[
\left|\frac{2^{N+1}z^{2^{N+1}}}{1-z^{2^{N+1}}}\right|
\le
2^{N+2}r^{2^{N+1}}.
\]
Writing $c=-\log r>0$, the right-hand side is
\[
2^{N+2}e^{-c2^{N+1}},
\]
which tends to $0$ because the exponential decay in $2^N$ dominates the factor $2^N$.

:::

:::

::: pf-step

Therefore
\[
\sum_{k=0}^{\infty}\frac{2^kz^{2^k}}{1+z^{2^k}}
=
\frac{z}{1-z}.
\]

::: pf-proof

Let $N\to\infty$ in the finite telescoping identity of step [](#s6){.pf-ref} and use step [](#s7){.pf-ref}.

:::

:::

:::

:::
