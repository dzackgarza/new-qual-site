---
schema: qual/card@1
id: P-ACC32
kind: problem
title: "Show that if $x_n$ is a decreasing sequence of positive real numbers s\u2026"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Show that if $x_n$ is a decreasing sequence of positive real numbers such that $\sum_{n=1}^\infty x_n$ converges, then
$$
\lim_{n\to\infty} n x_n = 0.
$$

:::{.concept}
\envlist

- Cauchy criterion for convergence
- Claim: even and odd subsequences converge iff whole sequence converges.
:::

:::{.proof title="of claim"}
$\impliedby$: clear, since any subsequence of a convergent sequence converges, and to the same limit.

$\implies$:
Fix $\eps$, choose $N\gg 1$ so that both $\abs{a_n - L} < \eps, \abs{a_{2n} - L} < \eps$ for $n\geq N$.
Then for any $n$, it is either even or odd, so one of these bounds applies.
:::

:::{.solution}
See this MSE post for many solutions: <https://math.stackexchange.com/questions/4603/if-a-n-subset0-infty-is-non-increasing-and-sum-a-n-infty-then-lim>

- Since $\sum_{k\geq 1}x_k < \infty$, by the Cauchy criterion for convergent sequences we have 
\[
\lim_{M, N\to \infty} \sum_{M\leq k \leq N} x_k = 0
.\]
  - This still holds if we freely add a constant $C$, so $C\sum_{M\leq k \leq N} x_k \to 0$ as well.
- Trick: $N \da n, M \da 2n$ and take $C\da 2$:
\[
2\sum_{n\leq k \leq 2n} x_k
&\geq 2\sum_{n\leq k \leq 2n} x_{2n} && \text{$x_k$ are non-increasing }\\
&= 2 (2n-n)x_{2n} \\
&= 2nx_{2n}
,\]
  and the upper bound goes to zero as $n\to \infty$.

- So the even subsequence $2n x_{2n} \to 0$, it now suffices to show the odd subsequence $(2n+1) x_{2n+1} \to 0$.
- Write
\[
(2n+1)x_{2n+1} 
&= 2n\cdot x_{2n+1} + 1\cdot x_{2n+1} \\
&\leq 2n\cdot x_{2n} + 1\cdot x_{2n+1} &&\text{$x_k$ are non-increasing }\\
&\converges{n\to \infty}\too 0
,\]
where the first term converges by what we showed above, and the second by assumption.
:::

