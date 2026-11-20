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

4. Without a dominating function, [[T-LDJNS|Fatou's lemma]] gives only an inequality.

## Failure of the interchange

Without an integrable dominating function the interchange can fail, and the inequality of Fatou's lemma can be strict; [[real-analysis/counterexamples#Convergence and integration|Counterexamples]] carries the three sequences that witness this.

## Other interchanges

[[real-analysis/undergraduate/commuting-limits|Commuting limits]] treats interchanges of limits more generally.

- $\sum_k \int f_k = \int \sum_k f_k$: by monotone convergence for $f_k\geq0$, and by dominated convergence when $\sum_k\int\abs{f_k} < \infty$; these are Tonelli's and Fubini's theorems for counting measure.

- $\frac{d}{dt}\int f(x,t)\,d\mu(x) = \int \partial_t f(x,t)\,d\mu(x)$: by dominated convergence applied to difference quotients, when $\abs{\partial_t f(x,t)}\leq g(x)$ with $g\in L^1$ for all $t$ in an interval.

- $\int\int f\,d\mu\,d\nu$ in either order: [[real-analysis/fubini-tonelli/index|Fubini and Tonelli]].
