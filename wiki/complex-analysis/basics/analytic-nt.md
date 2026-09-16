---
order: 52
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

[[L-EAZX6]]

::: {.proof}
Let $\abs{A_n}\leq M$ for all $n$, where $A_n \coloneqq \sum_{k\leq n} a_k$ and $A_0 \coloneqq 0$.
By [[PR-2MTPE|summation by parts]] with $m=1$,
$$
\sum_{k=1}^N a_k b_k = A_N b_N + \sum_{k=1}^{N-1} A_k (b_k - b_{k+1}).
$$
Since $\abs{A_N b_N}\leq M b_N \to 0$, the first term tends to $0$.
Since $b_k$ is decreasing, $b_k - b_{k+1}\geq 0$, and
$$
\sum_{k=1}^{N-1}\abs{A_k (b_k - b_{k+1})} \leq M\sum_{k=1}^{N-1} (b_k - b_{k+1}) = M(b_1 - b_N) \leq M b_1,
$$
so the second sum converges absolutely as $N\to\infty$.
Hence $\sum_{k\geq 1} a_k b_k$ converges.

:::

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

## Exercises

[[E-SS1.EX-19]]
[[E-ORJPT]]
[[E-XIT36]]
[[E-FJZCL]]
