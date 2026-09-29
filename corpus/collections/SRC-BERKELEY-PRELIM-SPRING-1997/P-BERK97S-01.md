---
schema: qual/card@1
id: P-BERK97S-01
kind: problem
title: Convergence of $\sum n^{-\alpha}(\log n)^{-\beta}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified eventual monotonicity, the condensation reduction, and all
    boundary cases in alpha and beta.
---

::: {.problem}
For which values of $\alpha,\beta$ does
\[
\sum_{n=3}^\infty\frac{1}{n^\alpha(\log n)^\beta}
\]
converge?
:::

::: {.solution}
Put
$$
a_n\coloneqq\frac{1}{n^\alpha(\log n)^\beta}.
$$

::: pf

::: {.pf-step #s1}

If $\alpha>0$, then $(a_n)$ is eventually decreasing. If
$\alpha=0$ and $\beta>0$, it is decreasing for $n\geq3$.

::: pf-proof

For
$$
h(x)=x^{-\alpha}(\log x)^{-\beta},
$$
one has
$$
\frac{h'(x)}{h(x)}
=
-\frac1x
\left(
\alpha+\frac{\beta}{\log x}
\right).
$$
If $\alpha>0$, the quantity in parentheses is positive for all sufficiently
large $x$. If $\alpha=0$ and $\beta>0$, it is positive for every $x>1$.
Thus $h$ is decreasing in the stated ranges.

:::

:::

::: {.pf-step #s2}

Whenever step [](#s1){.pf-ref} applies, Cauchy's condensation test reduces the
series, up to a positive constant factor, to
$$
\sum_{k\geq K}
\frac{2^{(1-\alpha)k}}{k^\beta}
$$
for some sufficiently large integer $K$.

::: pf-proof

For sufficiently large $k$,
$$
2^k a_{2^k}
=
\frac{2^k}
{(2^k)^\alpha(\log 2^k)^\beta}
=
(\log2)^{-\beta}
\frac{2^{(1-\alpha)k}}{k^\beta}.
$$
Cauchy's condensation test applies to the positive eventually decreasing
sequence after discarding finitely many initial terms.

:::

:::

::: {.pf-step #s3}

If $\alpha>1$, the original series converges for every
$\beta\in\RR$.

::: pf-proof

In step [](#s2){.pf-ref} the factor $2^{(1-\alpha)k}$ decays geometrically. A geometric
decay dominates the fixed power $k^{-\beta}$, so the condensed series
converges. Hence the original series converges.

:::

:::

::: {.pf-step #s4}

If $0<\alpha<1$, the original series diverges for every
$\beta\in\RR$.

::: pf-proof

The terms of the condensed series from step [](#s2){.pf-ref} are
$$
\frac{2^{(1-\alpha)k}}{k^\beta}.
$$
Since $1-\alpha>0$, these terms do not tend to zero. Thus the condensed
series, and hence the original series, diverges.

:::

:::

::: {.pf-step #s5}

If $\alpha=1$, the original series converges exactly when
$\beta>1$.

::: pf-proof

For $\alpha=1$, step [](#s2){.pf-ref} gives, up to a positive constant factor,
$$
\sum_{k\geq K}\frac1{k^\beta}.
$$
This $p$-series converges exactly when $\beta>1$.

:::

:::

::: {.pf-step #s6}

If $\alpha\leq0$, the original series diverges for every
$\beta\in\RR$.

::: pf-proof

If $\alpha=0$ and $\beta>0$, step [](#s2){.pf-ref} gives condensed terms
$$
\frac{2^k}{k^\beta},
$$
which do not tend to zero. If $\alpha=0$ and $\beta\leq0$, then $a_n$
itself does not tend to zero.

If $\alpha<0$, then
$$
a_n
=
\frac{n^{-\alpha}}{(\log n)^\beta}
$$
does not tend to zero, because every positive power of $n$ dominates every
fixed power of $\log n$. Thus the series diverges in all cases with
$\alpha\leq0$.

:::

:::

::: {.pf-step #s7}

Therefore the series converges exactly for
$$
\boxed{
\alpha>1
\quad\text{or}\quad
\alpha=1\text{ and }\beta>1
}.
$$

::: pf-proof

Steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} cover all real values of $\alpha$ and $\beta$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required classification.

:::

:::

:::
