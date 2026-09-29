---
schema: qual/card@1
id: P-B6S3M
kind: problem
title: Borel–Cantelli lemmas
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 3 of the official UGA August 2019 Real Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Reviewed the limsup measurability argument and both Borel-Cantelli proofs, including the stated finite-block complement-independence hypothesis.
---

::: {.problem}
Let $(X, \mathcal{B}, \mu)$ be a measure space with $\mu(X) = 1$, and let $\{B_n\}_{n=1}^\infty$ be a sequence of $\mathcal{B}$-measurable subsets of $X$. Define
$$
B = \{x \in X : x \in B_n \text{ for infinitely many } n\}.
$$

(a) Show that $B$ is a $\mathcal{B}$-measurable subset of $X$.

(b) Prove the First Borel–Cantelli Lemma: if $\sum_{n=1}^\infty \mu(B_n) < \infty$, then $\mu(B) = 0$.

(c) Prove the Second Borel–Cantelli Lemma: if $\sum_{n=1}^\infty \mu(B_n) = \infty$ and the sequence of complements satisfies
$$
\mu\left(\bigcap_{n=k}^K B_n^c\right) = \prod_{n=k}^K (1 - \mu(B_n))
$$
for all positive integers $k < K$, then $\mu(B) = 1$.
:::

::: {.solution}
**Goal:** Prove the measurability of $\limsup B_n$ in (a), the First Borel–Cantelli Lemma via countable subadditivity in (b), and the Second Borel–Cantelli Lemma via complement independence and exponential bounds in (c).

::: pf

::: pf-step

Part (a): $B$ is $\mathcal{B}$-measurable.

::: pf-proof

::: pf-step

An element $x \in X$ belongs to infinitely many $B_n$ if and only if for every $k \ge 1$, there exists $n \ge k$ such that $x \in B_n$.

:::

::: pf-step

In set-theoretic notation:
    $$B = \bigcap_{k=1}^\infty \bigcup_{n=k}^\infty B_n = \limsup_{n \to \infty} B_n.$$

:::

::: pf-step

Since $\mathcal{B}$ is a $\sigma$-algebra, it is closed under countable unions and countable intersections.

:::

::: pf-step

For each $k \ge 1$, $E_k = \bigcup_{n=k}^\infty B_n \in \mathcal{B}$ since each $B_n \in \mathcal{B}$.

:::

::: pf-step

Therefore $B = \bigcap_{k=1}^\infty E_k \in \mathcal{B}$.

:::

:::

:::

::: pf-step

Part (b): $\sum_{n=1}^\infty \mu(B_n) < \infty \implies \mu(B) = 0$.

::: pf-proof

::: pf-step

For each $k \ge 1$, $B = \bigcap_{j=1}^\infty \bigcup_{n=j}^\infty B_n \subseteq \bigcup_{n=k}^\infty B_n$.

:::

::: pf-step

By monotonicity and countable subadditivity of the measure $\mu$:
    $$\mu(B) \le \mu\left( \bigcup_{n=k}^\infty B_n \right) \le \sum_{n=k}^\infty \mu(B_n) \quad \text{for every } k \ge 1.$$

:::

::: pf-step

Since the series $\sum_{n=1}^\infty \mu(B_n)$ converges, its tail sum vanishes as $k \to \infty$:
    $$\lim_{k \to \infty} \sum_{n=k}^\infty \mu(B_n) = 0.$$

:::

::: pf-step

Taking $k \to \infty$ on both sides gives $0 \le \mu(B) \le 0$, so $\mu(B) = 0$.

:::

:::

:::

::: pf-step

Part (c): $\sum_{n=1}^\infty \mu(B_n) = \infty$ and independence $\implies \mu(B) = 1$.

::: pf-proof

::: pf-step

Complement of $B$: By De Morgan's laws,
    $$B^c = \left( \bigcap_{k=1}^\infty \bigcup_{n=k}^\infty B_n \right)^c = \bigcup_{k=1}^\infty \bigcap_{n=k}^\infty B_n^c.$$

:::

::: pf-step

By countable subadditivity of $\mu$:
    $$\mu(B^c) = \mu\left( \bigcup_{k=1}^\infty \bigcap_{n=k}^\infty B_n^c \right) \le \sum_{k=1}^\infty \mu\left( \bigcap_{n=k}^\infty B_n^c \right).$$

:::

::: pf-step

Continuity of measure from above on the decreasing sequence of sets $A_{k, K} = \bigcap_{n=k}^K B_n^c$ (as $K \to \infty$):
    $$\mu\left( \bigcap_{n=k}^\infty B_n^c \right) = \lim_{K \to \infty} \mu\left( \bigcap_{n=k}^K B_n^c \right) = \lim_{K \to \infty} \prod_{n=k}^K (1 - \mu(B_n)).$$

:::

::: pf-step

Use the elementary inequality $1 - t \le e^{-t}$ for all $t \in [0, 1]$:
    $$\prod_{n=k}^K (1 - \mu(B_n)) \le \prod_{n=k}^K e^{-\mu(B_n)} = \exp\left( -\sum_{n=k}^K \mu(B_n) \right).$$

:::

::: pf-step

Since $\sum_{n=1}^\infty \mu(B_n) = \infty$, the tail sum $\sum_{n=k}^\infty \mu(B_n) = \infty$ for every fixed $k \ge 1$.

:::

::: pf-step

Therefore, for each $k \ge 1$:
    $$\lim_{K \to \infty} \exp\left( -\sum_{n=k}^K \mu(B_n) \right) = \exp(-\infty) = 0.$$

:::

::: pf-step

Thus $\mu\left( \bigcap_{n=k}^\infty B_n^c \right) = 0$ for every $k \ge 1$.

:::

::: pf-step

Summing over all $k \ge 1$ gives $\mu(B^c) \le \sum_{k=1}^\infty 0 = 0$, so $\mu(B^c) = 0$.

:::

::: pf-step

Since $\mu(X) = 1$, $\mu(B) = \mu(X) - \mu(B^c) = 1 - 0 = 1$.

:::

:::

:::

::: pf-step

Conclusion:

::: pf-proof

$B$ is measurable, $\mu(B) = 0$ when $\sum \mu(B_n) < \infty$, and $\mu(B) = 1$ when $\sum \mu(B_n) = \infty$ under the independence condition.

:::

:::

:::

:::
