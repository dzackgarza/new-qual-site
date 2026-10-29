---
order: 52
title: Summation by parts and Abel's theorem
---

# Summation by parts and Abel's theorem

[[PR-2MTPE]]

::: {.proof}
Let $A_n \coloneqq \sum_{k\leq n} a_k$, so that $a_k = A_k - A_{k-1}$.
Reindexing the second sum and separating its boundary terms,
$$
\begin{aligned}
\sum_{m\leq k \leq n} a_k b_k
&= \sum_{m\leq k \leq n} (A_k - A_{k-1}) b_k \\
&= \sum_{m\leq k \leq n} A_kb_k - \sum_{m-1\leq k \leq n-1} A_{k} b_{k+1} \\
&= A_nb_n - A_{m-1} b_{m} + \sum_{m\leq k \leq n-1} A_kb_k - \sum_{m\leq k \leq n-1} A_{k} b_{k+1} \\
&= A_nb_n - A_{m-1} b_{m} - \sum_{m\leq k \leq n-1} A_k(b_{k+1} - b_{k}).
\end{aligned}
$$

:::

[[FT-3ZL25]]

[[T-B7YTE]]

[[L-MYZOX]]

::: {.example title="The alternating harmonic series"}
Integrating the geometric series $\sum_{k\geq 0}(-z)^k = 1/(1+z)$ term by term gives
$$
\sum_{k\geq 1} {(-1)^{k+1} z^k \over k} = \log(1+z), \qquad \abs{z} < 1.
$$
The series converges at $z=1$ by the alternating series test, so [[T-B7YTE|Abel's theorem]] gives $\sum_{k\geq 1}(-1)^{k+1}/k = \lim_{x\to 1^-}\log(1+x) = \log 2$.

:::

::: {.example title="The converse of Abel's theorem fails"}
Let $f(z) \coloneqq \sum_{n\geq 0} (-z)^n = 1/(1+z)$ for $\abs z<1$.
Then $\lim_{x\to 1^-} f(x) = 1/2$, but the series $\sum_{n\geq 0}(-1)^n = 1-1+1-\cdots$ diverges.

:::

## Problems

[[E-SS1.EX-19]]
[[E-ORJPT]]
[[E-XIT36]]
[[E-FJZCL]]
