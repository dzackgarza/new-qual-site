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

Show that $\sum_{n=1}^\infty f_n$ does not satisfy the Weierstrass M-test but that it nevertheless converges uniformly on $\mathbb{R}$.
:::
::: {.solution}
<1>1. The Weierstrass M-test does not apply.
::: {.proof}
Each $f_n$ equals $1/n$ on the nonempty interval $(2^{-(n+1)},2^{-n}]$, and is zero elsewhere. Thus $\|f_n\|_\infty=1/n$. Every majorant $M_n\ge\|f_n\|_\infty$ has divergent sum, by comparison with the harmonic series. Hence the summable-majorant hypothesis of the M-test fails.
:::

<1>2. The supports $\supp f_n = (2^{-(n+1)}, 2^{-n}]$ are pairwise disjoint.
::: {.proof}
For $m>n$, any $x\in(2^{-(m+1)},2^{-m}]$ satisfies $x\le2^{-m}\le2^{-(n+1)}$, whereas every point of $(2^{-(n+1)},2^{-n}]$ is strictly larger than $2^{-(n+1)}$. Therefore the nonzero loci of the functions are disjoint.
:::

<1>3. Pointwise limit: $S(x) = \sum_n f_n(x) = f_{n(x)}(x)$ where $n(x)$ is the unique index with $x \in (2^{-(n+1)}, 2^{-n}]$, and $S(x) = 0$ otherwise.
::: {.proof}
By step <1>2, for each $x\in\mathbb R$ at most one term is nonzero. Thus the series converges pointwise, taking value $1/n$ on the $n$th interval and zero outside their union.
:::

<1>4. Uniform convergence on $\RR$.
::: {.proof}
Write $S_N=\sum_{n=1}^Nf_n$. For every $x$, step <1>2 implies that $S(x)-S_N(x)$ is either zero or $1/n$ for some $n>N$. Hence $|S(x)-S_N(x)|\le1/(N+1)$ everywhere. Equality holds for every $x\in(2^{-(N+2)},2^{-(N+1)}]$, so
\[
\boxed{\|S-S_N\|_\infty=\frac1{N+1}\longrightarrow0}.
\]
This is uniform convergence on $\mathbb R$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves failure of the M-test hypothesis, and step <1>4 proves uniform convergence.
:::
:::
