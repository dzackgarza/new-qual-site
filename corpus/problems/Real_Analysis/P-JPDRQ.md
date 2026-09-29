---
schema: qual/card@1
id: P-JPDRQ
kind: problem
title: Sequences, uniform convergence, and Bolzano-Weierstrass
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Uniform Convergence
  - Convergence of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Can a convergent sequence of real numbers have a subsequence converging to a different limit?

- What does it mean for a sequence of functions to converge **pointwise** and to converge **uniformly**?

  - Give an example of a sequence that converges pointwise but not uniformly.

- Prove that every sequence admits a monotone subsequence.

- Prove the monotone convergence theorem for sequences.

- Prove the Bolzano-Weierstrass Theorem.
:::
::: {.solution}
Functions $f_n\colon E \to \RR$ \dfn{converge pointwise} to $f$ if $f_n(x) \to f(x)$ for every $x \in E$, and \dfn{converge uniformly} to $f$ if $\sup_{x \in E}|f_n(x) - f(x)| \to 0$.

::: pf

::: pf-step

Every subsequence of a sequence converging to $x$ converges to $x$.

::: pf-proof

For $\eps > 0$, all but finitely many terms lie within $\eps$ of $x$, and so do all but finitely many terms of any subsequence. Limits in $\RR$ are unique.

:::

:::

::: pf-step

$f_n(x) = x^n$ on $[0,1]$ converges pointwise but not uniformly.

::: pf-proof

$x^n \to 0$ for $x \in [0,1)$ and $1^n = 1$, so the pointwise limit is $\chi_{\theset1}$, but $\sup_{[0,1]}|x^n - \chi_{\theset1}(x)| = 1$ for every $n$.

:::

:::

::: {.pf-step #s3}

Every real sequence $(a_n)$ has a monotone subsequence.

::: pf-proof

Call $n$ a peak if $a_n \ge a_m$ for all $m \ge n$. If there are infinitely many peaks $n_1 < n_2 < \cdots$, then $a_{n_1} \ge a_{n_2} \ge \cdots$. Otherwise let $n_1$ exceed every peak. Since $n_k$ is not a peak, there is $n_{k+1} > n_k$ with $a_{n_{k+1}} > a_{n_k}$, which gives an increasing subsequence.

:::

:::

::: {.pf-step #s4}

An increasing sequence bounded above converges to its supremum, and an increasing sequence not bounded above tends to $\infty$.

::: pf-proof

If $s = \sup_n a_n < \infty$ and $\eps > 0$, then $s - \eps$ is not an upper bound, so $a_N > s - \eps$ for some $N$, and $s - \eps < a_n \le s$ for $n \ge N$. If $(a_n)$ is not bounded above, for every $M$ some $a_N > M$, and $a_n \ge a_N > M$ for $n \ge N$. Decreasing sequences are handled by passing to $(-a_n)$.

:::

:::

::: pf-step

Every bounded real sequence has a convergent subsequence.

::: pf-proof

By step [](#s3){.pf-ref} it has a monotone subsequence, which is bounded and therefore converges by step [](#s4){.pf-ref}.

:::

:::

:::

:::
