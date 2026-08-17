---
schema: qual/card@1
id: P-MMAQ-HR4GLJ2FYM
kind: problem
title: $\sum a_n b_n<\infty$ for all $b\in\ell^2$ implies $\sum a_n^2<\infty$
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - series-of-numbers
  - lp-spaces
relations: []
review: draft
solved: true
---

::: problem
Let $\theset{a_n}$ be a sequence of real numbers such that
$$
\theset{b_n} \in \ell^2(\NN) \implies \sum a_n b_n < \infty.
$$
Show that $\sum a_n^2 < \infty$.

> Note: Assume $a_n, b_n$ are all non-negative.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $\theset{a_n} \subset \RR_{\geq 0}$ be such that $\sum_n a_n b_n < \infty$ for every nonnegative $b \in \ell^2$.
Show $\sum_n a_n^2 < \infty$.

<1>1. Suppose, toward a contradiction, that $\sum_n a_n^2 = \infty$.
Proof: We prove the contrapositive: if the squares diverge, the hypothesis fails.
<2>1. Let $s_n \definedas \sum_{k=1}^n a_k^2$, so $s_n \nearrow \infty$.
Proof: Partial sums of a divergent series of nonnegative terms increase to $\infty$.
<2>2. Define $b_n \definedas \frac{a_n}{s_n}$ for $n \geq 1$.
Proof: Well-defined since $s_n \geq a_n^2 > 0$ when $a_n \neq 0$; if $a_n = 0$ then $b_n = 0$.
<2>3. $\theset{b_n} \in \ell^2$.
Proof: Let $s_n \definedas \sum_{k=1}^n a_k^2$ with $s_0 \definedas a_1^2 > 0$ (drop any leading zeros; if all $a_n = 0$ the conclusion is trivial).
Then $b_n^2 = \frac{a_n^2}{s_n^2} \leq \frac{a_n^2}{s_n s_{n-1}}$ since $s_n \geq s_{n-1}$, and $\frac{a_n^2}{s_n s_{n-1}} = \frac{s_n - s_{n-1}}{s_n s_{n-1}} = \frac{1}{s_{n-1}} - \frac{1}{s_n}$, which telescopes to $\frac{1}{s_0} - \frac{1}{s_N} \leq \frac{1}{s_0} < \infty$.
<2>4. $\sum_n a_n b_n = \sum_n \frac{a_n^2}{s_n} = \infty$.
Proof: Write $\frac{a_n^2}{s_n} = \frac{s_n - s_{n-1}}{s_n} = 1 - \frac{s_{n-1}}{s_n}$.
If $\sum_n \frac{s_n - s_{n-1}}{s_n} < \infty$, then the infinite product $\prod_n \frac{s_{n-1}}{s_n}$ converges to a positive number (since $\sum (1 - x_n) < \infty$ with $x_n = \frac{s_{n-1}}{s_n} \in (0,1]$ forces $\prod x_n \geq e^{-\sum(1-x_n)} > 0$). But the product telescopes: $\prod_{n=1}^N \frac{s_{n-1}}{s_n} = \frac{s_0}{s_N} \to 0$ because $s_N \to \infty$ (as $\sum a_n^2 = \infty$). Contradiction, so $\sum_n a_n b_n = \infty$.
<2>5. Q.E.D. Proof: <2>3 produces $b \in \ell^2$ with $\sum a_n b_n = \infty$ (<2>4), contradicting the hypothesis.
Hence $\sum a_n^2 < \infty$.

<1>2. Conclusion: $\sum_n a_n^2 < \infty$.
Proof: By <1>1, the supposition $\sum a_n^2 = \infty$ is untenable.
:::
