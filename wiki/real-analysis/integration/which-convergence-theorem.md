---
title: Which convergence theorem?
order: 0
topics:
- Convergence Theorems
- Dominated Convergence
- Fatou
---

# Which convergence theorem?

Let $(X,\mu)$ be a measure space and $f_n, f$ measurable functions on $X$.
The following theorems justify $\lim_n\int f_n = \int\lim_n f_n$ or an inequality between them.

## Which theorem applies?

| Question | Theorem |
| --- | --- |
| Is the sequence increasing? | [[T-5K3IO|Monotone convergence]] |
| Is it nonnegative, with no monotonicity available? | [[T-LDJNS|Fatou's lemma]] |
| Is one integrable function a bound for every term? | [[T-IJQQG|Dominated convergence]] |
| Is it uniformly bounded on a space of finite measure? | [[T-TRW6N|Bounded convergence]] |

Bounded convergence is dominated convergence with $g\equiv M$, which is integrable if and only if $\mu(X)<\infty$ (for $M>0$).

## Choosing a theorem

1. For measurable $0\leq f_1\leq f_2\leq\cdots$, [[T-5K3IO|monotone convergence]] applies, and it also turns a sum of nonnegative measurable functions into a series of integrals.

2. [[T-IJQQG|Dominated convergence]] needs an integrable $g$ with $\abs{f_n}\leq g$ for all $n$.
   Common choices are a bound independent of $n$ obtained from an explicit estimate, $\sum_k\abs{h_k}$ when $f_n$ are partial sums of $\sum_k h_k$ with $\sum_k\int\abs{h_k}<\infty$, and $f_1$ when $0\leq f_{n+1}\leq f_n$ and $f_1\in L^1$.

3. On a finite measure space, a uniformly bounded sequence satisfies the hypotheses of [[T-TRW6N|bounded convergence]].

4. Without a dominating function, [[T-LDJNS|Fatou's lemma]] gives only an inequality, and it is strict for each of $n\chi_{(0,1/n)}$, $\frac1n\chi_{[0,n]}$, and $\chi_{[n,n+1]}$.

## Failure of the interchange

::: {.example title="Sequences with $f_n\to0$ pointwise and $\int f_n = 1$"}
- $f_n \coloneqq n\chi_{(0,1/n)}$ on $[0,1]$: the mass concentrates near $0$, and $\sup_n f_n\notin L^1$.

- $f_n \coloneqq \frac1n \chi_{[0,n]}$ on $\RR$: $\abs{f_n}\leq1$, so bounded convergence fails on a space of infinite measure.

- $f_n \coloneqq \chi_{[n, n+1]}$ on $\RR$: the mass moves to infinity.

In each case no integrable $g$ dominates $(f_n)$, and $0 = \int\lim_n f_n<\lim_n\int f_n = 1$.

:::

## Other interchanges

[[real-analysis/undergraduate/commuting-limits|Commuting limits]] treats interchanges of limits more generally.

- $\sum_k \int f_k = \int \sum_k f_k$: by monotone convergence for $f_k\geq0$, and by dominated convergence when $\sum_k\int\abs{f_k} < \infty$; these are Tonelli's and Fubini's theorems for counting measure.

- $\frac{d}{dt}\int f(x,t)\,d\mu(x) = \int \partial_t f(x,t)\,d\mu(x)$: by dominated convergence applied to difference quotients, when $\abs{\partial_t f(x,t)}\leq g(x)$ with $g\in L^1$ for all $t$ in an interval.

- $\int\int f\,d\mu\,d\nu$ in either order: [[real-analysis/fubini-tonelli/index|Fubini and Tonelli]].
