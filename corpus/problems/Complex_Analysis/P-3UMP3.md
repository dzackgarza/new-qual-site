---
schema: qual/card@1
id: P-3UMP3
kind: problem
title: $c_n\neq 0$ for large $n$ and $c_n/c_{n+1}\to z_0$ for a pole on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
  - Convergence Tests
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source writes the power series as sum_{n=1}^infty c_n z^n, which would force f(0)=0 without that hypothesis; the statement sums from n=0 and corrects "the the".'
---

::: {.problem}
Suppose that $f$ is holomorphic in an open set containing the closed unit disc, except for a pole at $z_0$ on the unit circle.
Let $\displaystyle f(z) = \sum_{n = 0}^\infty c_n z^n$ denote the power series in the open disc.
Show that

(1) $c_n \neq 0$ for all large enough $n$'s, and

(2) $\displaystyle \lim_{n \rightarrow \infty} \frac{c_n}{c_{n+1}}= z_0$.
:::

::: {.solution}

Let $k\geq1$ be the order of the pole and $P(z)=\sum_{j=1}^k\frac{A_j}{(z-z_0)^j}$, with $A_k\neq0$, the principal part of $f$ at $z_0$.

::: pf

::: {.pf-step #remainder}
$g\coloneqq f-P$ has Taylor coefficients $d_n$ at $0$ with $d_n=O(\rho^{-n})$ for some $\rho>1$.

::: pf-proof
The singularity of $g$ at $z_0$ is removable, and $P$ is holomorphic away from $z_0$, so $g$ extends holomorphically to an open set containing $\overline{\DD}$, hence to a disc $\abs{z}<R$ with $R>1$.
By the Cauchy--Hadamard formula, $\abs{d_n}\leq\rho^{-n}$ for large $n$ and any $1<\rho<R$.
:::

:::

::: {.pf-step #coefficients}
$c_n=\displaystyle\sum_{j=1}^k(-1)^jA_jz_0^{-n-j}\binom{n+j-1}{j-1}+d_n$.

::: pf-proof
For $\abs{z}<1=\abs{z_0}$, $\frac1{(z-z_0)^j}=\frac{(-1)^j}{z_0^j}\qty(1-\frac z{z_0})^{-j}=\frac{(-1)^j}{z_0^j}\sum_{n\geq0}\binom{n+j-1}{j-1}z_0^{-n}z^n$ by the negative binomial series.
Add the coefficients of $P$ and of $g$.
:::

:::

::: {.pf-step #asymptotic}
$\dfrac{c_nz_0^n}{n^{k-1}}\to C\coloneqq\dfrac{(-1)^kA_k}{(k-1)!\,z_0^k}\neq0$.

::: pf-proof
Multiply step [](#coefficients){.pf-ref} by $z_0^n/n^{k-1}$, using $\abs{z_0}=1$.
The term $j=k$ tends to $C$, because $\binom{n+k-1}{k-1}$ is a polynomial in $n$ of degree $k-1$ with leading coefficient $1/(k-1)!$.
Each term $j<k$ is $O(n^{j-1})/n^{k-1}\to0$, and $\abs{d_n}/n^{k-1}\to0$ by step [](#remainder){.pf-ref}.
$C\neq0$ since $A_k\neq0$.
:::

:::

::: pf-step
(1) $c_n\neq0$ for all large $n$.

::: pf-proof
By step [](#asymptotic){.pf-ref}, $\abs{c_n}\,n^{-(k-1)}\to\abs{C}>0$, so $\abs{c_n}>0$ for all large $n$.
:::

:::

::: pf-step
(2) $c_n/c_{n+1}\to z_0$.

::: pf-proof
For large $n$,
$$
\frac{c_n}{c_{n+1}}=z_0\cdot\frac{c_nz_0^n/n^{k-1}}{c_{n+1}z_0^{n+1}/(n+1)^{k-1}}\cdot\qty(\frac{n}{n+1})^{k-1},
$$
and by step [](#asymptotic){.pf-ref} the middle factor tends to $C/C=1$, while the last tends to $1$.
:::

:::

:::

:::
