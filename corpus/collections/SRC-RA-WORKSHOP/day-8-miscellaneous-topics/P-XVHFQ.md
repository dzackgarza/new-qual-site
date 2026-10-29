---
schema: qual/card@1
id: P-XVHFQ
kind: problem
title: $\sum f_n$ with $f_n=\frac1n$ on $(2^{-(n+1)},2^{-n}]$ converges uniformly
  without the Weierstrass $M$-test
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $$f_n(x) = \begin{cases} \frac{1}{n}  & x \in (\frac{1}{2^{n+1}}, \frac{1}{2^n}] \\ 0 & \text{ otherwise}.\end{cases}$$

Show that $\sum_{n=1}^\infty f_n$ does not satisfy the Weierstrass M-test but that it nevertheless converges uniformly on $\RR$.
:::

::: {.solution}

::: pf

::: pf-step

The Weierstrass M-test does not apply.

::: pf-proof

Each $f_n$ equals $1/n$ on the nonempty interval $(2^{-(n+1)},2^{-n}]$, and is zero elsewhere. Thus $\norm{f_n}_\infty=1/n$. Every majorant $M_n\ge\norm{f_n}_\infty$ has divergent sum, by comparison with the harmonic series. Hence the summable-majorant hypothesis of the M-test fails.

:::

:::

::: {.pf-step #s2}

The sets $\{f_n\ne0\} = (2^{-(n+1)}, 2^{-n}]$ are pairwise disjoint.

::: pf-proof

For $m>n$, any $x\in(2^{-(m+1)},2^{-m}]$ satisfies $x\le2^{-m}\le2^{-(n+1)}$, whereas every point of $(2^{-(n+1)},2^{-n}]$ is strictly larger than $2^{-(n+1)}$.

:::

:::

::: pf-step

$\sum f_n$ converges uniformly on $\RR$.

::: pf-proof

By step [](#s2){.pf-ref}, for each $x\in\RR$ at most one term is nonzero, so the series converges pointwise to a function $S$. Write $S_N=\sum_{n=1}^Nf_n$. For every $x$, step [](#s2){.pf-ref} implies that $S(x)-S_N(x)$ is either zero or $1/n$ for some $n>N$. Hence $\abs{S(x)-S_N(x)}\le1/(N+1)$ everywhere. Equality holds for every $x\in(2^{-(N+2)},2^{-(N+1)}]$, so
$$
\norm{S-S_N}_\infty=\frac1{N+1}\longrightarrow0.
$$
This is uniform convergence on $\RR$.

:::

:::

:::

:::
