---
schema: qual/card@1
id: P-AMD-JQWDPMM2
kind: problem
title: $\frac{1}{n}\sum_{k=1}^n a_k\to 0$ if $a_n\to 0$ or $\sum\frac{a_n}{n}$ converges
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - series-of-numbers
  - limits
relations: []
review: draft
solved: true
---

::: {.problem}
Let $\{a_n\}_{n=1}^\infty$ be a sequence of real numbers.

a. Prove that if $\displaystyle\lim_{n\to∞} a_n = 0$, then
$$
\lim _{n \rightarrow \infty} \frac{a_{1}+\cdots+a_{n}}{n}=0
$$

b. Prove that if $\displaystyle\sum_{n=1}^{\infty} \frac{a_{n}}{n}$ converges, then
$$
\lim _{n \rightarrow \infty} \frac{a_{1}+\cdots+a_{n}}{n}=0
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $\{a_n\}_{n=1}^\infty$ be a sequence in $\RR$. Prove:
(a) If $\lim_{n\to\infty} a_n = 0$, then $\lim_{n\to\infty} \frac{a_1 + \dots + a_n}{n} = 0$ (Cesàro mean limit);
(b) If $\sum_{n=1}^\infty \frac{a_n}{n}$ converges, then $\lim_{n\to\infty} \frac{a_1 + \dots + a_n}{n} = 0$ (Kronecker's Lemma).

<1>1. **Part (a): If $\lim_{n\to\infty} a_n = 0$, then $\lim_{n\to\infty} \frac{1}{n}\sum_{k=1}^n a_k = 0$.**
  <2>1. Let $\eps > 0$ be given. There exists $N_1 \in \NN$ such that $|a_k| < \frac{\eps}{2}$ for all $k > N_1$.
    Proof: Since $\lim_{n\to\infty} a_n = 0$, by definition of the limit with tolerance $\frac{\eps}{2} > 0$.
  <2>2. For any $n > N_1$, split the sum:
    $$
    \left| \frac{1}{n}\sum_{k=1}^n a_k \right| \leq \frac{1}{n}\sum_{k=1}^{N_1} |a_k| + \frac{1}{n}\sum_{k=N_1+1}^n |a_k|.
    $$
    Proof: By the triangle inequality for sums.
  <2>3. $\frac{1}{n}\sum_{k=N_1+1}^n |a_k| < \frac{\eps}{2}$ for all $n > N_1$.
    Proof: By <2>1, each $|a_k| < \frac{\eps}{2}$ for $k \in \{N_1+1, \dots, n\}$, hence $\sum_{k=N_1+1}^n |a_k| < (n - N_1)\frac{\eps}{2} \leq n \frac{\eps}{2}$, so dividing by $n$ gives the bound.
  <2>4. There exists $N_2 \in \NN$ such that $\frac{1}{n}\sum_{k=1}^{N_1} |a_k| < \frac{\eps}{2}$ for all $n > N_2$.
    Proof: Let $C = \sum_{k=1}^{N_1} |a_k|$, which is a fixed constant independent of $n$. Choosing $N_2 = \left\lceil \frac{2C}{\eps} \right\rceil$, for all $n > N_2$ we have $\frac{C}{n} < \frac{\eps}{2}$.
  <2>5. For all $n > \max(N_1, N_2)$, $\left| \frac{1}{n}\sum_{k=1}^n a_k \right| < \eps$.
    Proof: Combining <2>2, <2>3, and <2>4:
    $$
    \left| \frac{1}{n}\sum_{k=1}^n a_k \right| < \frac{\eps}{2} + \frac{\eps}{2} = \eps.
    $$
    This proves that $\lim_{n\to\infty} \frac{a_1 + \dots + a_n}{n} = 0$.

<1>2. **Part (b): If $\sum_{n=1}^\infty \frac{a_n}{n}$ converges, then $\lim_{n\to\infty} \frac{a_1 + \dots + a_n}{n} = 0$.**
  <2>1. Define $S_n = \sum_{k=1}^n \frac{a_k}{k}$ for $n \geq 1$, and $S_0 = 0$. Let $S = \lim_{n\to\infty} S_n \in \RR$.
    Proof: The convergence of the series $\sum_{n=1}^\infty \frac{a_n}{n}$ means the partial sums $S_n$ converge to some real number $S$.
  <2>2. $a_k = k(S_k - S_{k-1})$ for all $k \geq 1$.
    Proof: By definition $S_k - S_{k-1} = \frac{a_k}{k}$, so multiplying by $k$ yields $a_k = k(S_k - S_{k-1})$.
  <2>3. Express $\sum_{k=1}^n a_k$ in terms of $S_k$:
    $$
    \sum_{k=1}^n a_k = n S_n - \sum_{k=0}^{n-1} S_k.
    $$
    Proof: Using summation by parts (Abel summation):
    $$
    \sum_{k=1}^n a_k = \sum_{k=1}^n k(S_k - S_{k-1}) = \sum_{k=1}^n k S_k - \sum_{k=1}^n k S_{k-1} = \sum_{k=1}^n k S_k - \sum_{j=0}^{n-1} (j+1) S_j
    $$
    $$
    = n S_n + \sum_{k=1}^{n-1} k S_k - \sum_{k=1}^{n-1} (k+1) S_k - S_0 = n S_n - \sum_{k=1}^{n-1} S_k - S_0 = n S_n - \sum_{k=0}^{n-1} S_k.
    $$
  <2>4. $\frac{1}{n}\sum_{k=1}^n a_k = S_n - \frac{1}{n}\sum_{k=0}^{n-1} S_k$.
    Proof: Divide the identity from <2>3 by $n$.
  <2>5. $\lim_{n\to\infty} \frac{1}{n}\sum_{k=0}^{n-1} S_k = S$.
    Proof: Since $S_k \to S$ as $k \to \infty$, the sequence $(S_k - S) \to 0$. By Part (a), $\frac{1}{n}\sum_{k=0}^{n-1} (S_k - S) \to 0$, which gives:
    $$
    \lim_{n\to\infty} \frac{1}{n}\sum_{k=0}^{n-1} S_k = \lim_{n\to\infty} \left( \frac{n S}{n} + \frac{1}{n}\sum_{k=0}^{n-1} (S_k - S) \right) = S + 0 = S.
    $$
  <2>6. $\lim_{n\to\infty} \frac{1}{n}\sum_{k=1}^n a_k = S - S = 0$.
    Proof: By <2>4, $\lim_{n\to\infty} \frac{1}{n}\sum_{k=1}^n a_k = \lim_{n\to\infty} S_n - \lim_{n\to\infty} \frac{1}{n}\sum_{k=0}^{n-1} S_k = S - S = 0$.

<1>3. **Conclusion.**
  Both Part (a) and Part (b) are rigorously established. Q.E.D.
:::
