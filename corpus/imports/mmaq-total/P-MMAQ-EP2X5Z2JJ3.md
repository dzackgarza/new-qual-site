---
schema: qual/card@1
id: P-MMAQ-EP2X5Z2JJ3
kind: problem
title: "Let $\\{a_n\\}_{n=1}^\\infty$ be a sequence of real numbers. Prove that if $\\displaystyle\\lim_{n\\to\\infty} a_n = 0$, then $\\displaystyle\\lim_{n\\to\\infty} a_1 + \\cdots + a_n = 0$."
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-numbers
relations: []
review: draft
solved: true
---

::: problem
Let $\{a_n\}_{n=1}^\infty$ be a sequence of real numbers.

a.  Prove that if $\displaystyle\lim_{n\to\infty} a_n = 0$, then $\displaystyle\lim_{n\to\infty} a_1 + \cdots + a_n = 0$.
    $$
    \lim _{n \rightarrow \infty} \frac{a_{1}+\cdots+a_{n}}{n}=0
    $$

b.  Prove that if $\displaystyle\sum_{n=1}^{\infty} \frac{a_{n}}{n}$ converges, then
    $$
    \lim _{n \rightarrow \infty} \frac{a_{1}+\cdots+a_{n}}{n}=0
    $$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $\theset{a_n}$ be a real sequence. (a) Show $a_n \to 0 \implies \frac{1}{n}\sum_{k=1}^n a_k \to 0$. (b) Show $\sum_n a_n/n$ converges $\implies \frac{1}{n}\sum_{k=1}^n a_k \to 0$.

<1>1. Proof of (a): if $a_n \to 0$, then the Cesàro means $\frac{1}{n}\sum_{k=1}^n a_k \to 0$.
    <2>1. Fix $\eps > 0$; since $a_n \to 0$, choose $N$ such that $\abs{a_k} < \eps/2$ for all $k > N$.
        Proof: Definition of convergence of $a_n$ to $0$.
    <2>2. Split the sum: $\abs{\frac{1}{n}\sum_{k=1}^n a_k} \leq \frac{1}{n}\sum_{k=1}^N \abs{a_k} + \frac{1}{n}\sum_{k=N+1}^n \abs{a_k}$.
        Proof: Triangle inequality, then the sum over $[1,n]$ is the sum over $[1,N]$ plus the sum over $[N+1,n]$.
    <2>3. The second term satisfies $\frac{1}{n}\sum_{k=N+1}^n \abs{a_k} < \frac{n-N}{n} \cdot \frac{\eps}{2} < \frac{\eps}{2}$.
        Proof: Each of the $n-N$ terms is $< \eps/2$ by <2>1, and $(n-N)/n < 1$.
    <2>4. The first term $\frac{1}{n}\sum_{k=1}^N \abs{a_k} \to 0$ as $n \to \infty$, since it is a fixed finite sum divided by $n$.
        Proof: $\sum_{k=1}^N \abs{a_k}$ is a constant independent of $n$.
    <2>5. Choose $M$ so that $\frac{1}{n}\sum_{k=1}^N \abs{a_k} < \eps/2$ for all $n \geq M$.
        Proof: By <2>4.
    <2>6. For $n \geq \max(N, M)$, $\abs{\frac{1}{n}\sum_{k=1}^n a_k} < \eps$.
        Proof: Combine <2>3 and <2>5 in <2>2.
    <2>7. Q.E.D.
        Proof: $\eps > 0$ was arbitrary, so the Cesàro means converge to $0$.

<1>2. Proof of (b): if $\sum_n a_n/n$ converges, then $\frac{1}{n}\sum_{k=1}^n a_k \to 0$.
    <2>1. Let $s_n \definedas \sum_{k=1}^n \frac{a_k}{k}$ and $S \definedas \lim_n s_n$.
        Proof: The series $\sum a_n/n$ converges by hypothesis, so $S$ exists.
    <2>2. Write $a_k = k \cdot (s_k - s_{k-1})$ (with $s_0 = 0$), so $\sum_{k=1}^n a_k = \sum_{k=1}^n k(s_k - s_{k-1})$.
        Proof: $s_k - s_{k-1} = a_k/k$ by definition of $s_k$.
    <2>3. Summation by parts: $\sum_{k=1}^n k(s_k - s_{k-1}) = n s_n - \sum_{k=1}^{n-1} s_k$.
        Proof: Expand $\sum_{k=1}^n k s_k - \sum_{k=1}^n k s_{k-1} = \sum_{k=1}^n k s_k - \sum_{j=0}^{n-1}(j+1) s_j = n s_n - \sum_{j=1}^{n-1} s_j$ after canceling the $j s_j$ terms.
    <2>4. Divide by $n$: $\frac{1}{n}\sum_{k=1}^n a_k = s_n - \frac{1}{n}\sum_{k=1}^{n-1} s_k$.
        Proof: Divide <2>3 by $n$.
    <2>5. $\frac{1}{n}\sum_{k=1}^{n-1} s_k \to S$ as $n \to \infty$.
        Proof: This is the Cesàro mean of the convergent sequence $s_k \to S$; part (a) applied to $s_k - S$ gives it.
    <2>6. Hence $\frac{1}{n}\sum_{k=1}^n a_k = s_n - \frac{1}{n}\sum_{k=1}^{n-1} s_k \to S - S = 0$.
        Proof: $s_n \to S$ by <2>1 and the Cesàro mean converges to $S$ by <2>5.
    <2>7. Q.E.D.
        Proof: Directly from <2>6.

<1>3. Conclusion: both statements hold.
    Proof: (a) by <1>1 and (b) by <1>2.
:::
