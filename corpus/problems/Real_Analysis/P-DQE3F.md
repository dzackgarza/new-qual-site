---
schema: qual/card@1
id: P-DQE3F
kind: problem
title: '$L^1$ convergence of an $L^2$ sequence: the limit, a.e. failure, and an a.e.
  subsequence'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Convergence of Functions
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let \( \ts{ f_k }_{k=1}^{\infty } \subseteq L^2([0, 1]) \) be a sequence which *converges in $L^1$* to a function $f$.

a. Prove that $f\in L^1([0, 1])$.

b. Give an example illustrating that $f_k$ may not converge to $f$ almost everywhere.

c. Prove that $\ts{f_k}$ must contain a subsequence that converges to $f$ almost everywhere.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

$f \in L^1([0,1])$.

::: pf-proof

Choose $k$ with $\|f - f_k\|_1 < 1$. Since $m([0,1]) = 1$, $\|f_k\|_1 \le \|f_k\|_2$ by the Cauchy--Schwarz inequality, so $\|f\|_1 \le \|f - f_k\|_1 + \|f_k\|_1 < \infty$.

:::

:::

::: {.pf-step #s2}

Let $E_k$ enumerate the dyadic intervals $[0,\frac12], [\frac12,1], [0,\frac14], [\frac14,\frac12], \ldots$, level by level, and $f_k = \chi_{E_k}$. Then $f_k \in L^2([0,1])$ and $f_k \to 0$ in $L^1$, but $f_k(x)$ converges for no $x \in [0,1]$.

::: pf-proof

$|f_k| \le 1$, so $f_k \in L^2$, and $\|f_k\|_1 = m(E_k) \to 0$. Each $x \in [0,1]$ lies in at least one dyadic interval of each level and misses at least one, so $f_k(x) = 1$ and $f_k(x) = 0$ for infinitely many $k$ each.

:::

:::

::: {.pf-step #s3}

Some subsequence $f_{k_j} \to f$ a.e.

::: pf-proof

::: {.pf-step #s3-1}

There are $k_1 < k_2 < \cdots$ with $\|f_{k_j} - f\|_1 < 2^{-j}$.

::: pf-proof

$\|f_k - f\|_1 \to 0$.

:::

:::

::: {.pf-step #s3-2}

For each $\eps > 0$, $m\theset{x : |f_{k_j}(x) - f(x)| > \eps \text{ for infinitely many } j} = 0$.

::: pf-proof

By Markov's inequality and step [](#s3-1){.pf-ref}, $\sum_j m\theset{|f_{k_j} - f| > \eps} \le \frac1\eps\sum_j 2^{-j} < \infty$, and the Borel--Cantelli lemma applies.

:::

:::

::: pf-qed

The union over $\eps = 1/n$, $n \geq 1$, of the null sets in step [](#s3-2){.pf-ref} is null, and off it $f_{k_j}(x) \to f(x)$.

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} are parts (a), (b) and (c).

:::

:::

:::
