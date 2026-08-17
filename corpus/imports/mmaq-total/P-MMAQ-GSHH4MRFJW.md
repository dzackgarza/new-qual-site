---
schema: qual/card@1
id: P-MMAQ-GSHH4MRFJW
kind: problem
title: "Prove or disprove each of the following statements. If ${f_n}$ is a\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - convergence-of-functions
  - lp-spaces
relations: []
review: draft
---

::: problem
Prove or disprove each of the following statements.

(b) If ${f_n}$ is a sequence of measurable functions that converges uniformly to $f$ on $\mathbb{R}$, then $\int{f}=\lim_{k\to \infty} \int f_k$

(c) If $\{f_k\}$ is a sequence of function in $L_p[0,\infty)$ that converges to a function $f \in L_p [0,\infty)$, then $\{f_k\}$ has a subsequence that converges to $f$ almost everywhere.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Decide the truth of (b) and (c).

<1>1. (b) is false.
    <2>1. Exhibit a counterexample: $f_k \definedas \frac{1}{k} \chi_{[0,k]}$ on $\RR$.
        Proof: Each $f_k$ is measurable (indicator of an interval), and $\int_\RR f_k = \frac{1}{k} \cdot k = 1$ for every $k$.
    <2>2. $f_k \to 0$ uniformly on $\RR$.
        Proof: $\sup_{x \in \RR} \abs{f_k(x) - 0} = \frac{1}{k} \to 0$.
    <2>3. But $\int f_k = 1 \neq 0 = \int 0 = \lim_k \int f_k$ fails.
        Proof: Each integral is $1$ while the limit function's integral is $0$; so $\int f = 0 \neq 1 = \lim_k \int f_k$.
    <2>4. Q.E.D.
        Proof: The counterexample of <2>1 satisfies the hypotheses but not the conclusion, so (b) is false.

<1>2. (c) is true: convergence in $L_p$ implies a.e.\ convergence along a subsequence (for $1 \leq p < \infty$).
    <2>1. Choose a subsequence $\theset{f_{k_j}}$ with $\norm{f_{k_j} - f}_p \leq 2^{-j}$.
        Proof: Since $\norm{f_k - f}_p \to 0$ by hypothesis, pick $k_j$ recursively so the $L_p$ distance is $\leq 2^{-j}$.
    <2>2. For each $j$, $\mu\theset{x : \abs{f_{k_j}(x) - f(x)} > 2^{-j/2}} \leq \left(2^{-j/2}\right)^{-p} \norm{f_{k_j} - f}_p^p \leq 2^{jp/2} 2^{-jp} = 2^{-jp/2}$.
        Proof: Chebyshev's (Markov's) inequality applied to $\abs{f_{k_j} - f}^p$ with threshold $2^{-jp/2}$.
    <2>3. $\sum_j \mu\theset{x : \abs{f_{k_j}(x) - f(x)} > 2^{-j/2}} \leq \sum_j 2^{-jp/2} < \infty$.
        Proof: Geometric series, since $p \geq 1$ implies $p/2 > 0$.
    <2>4. By Borel–Cantelli, for almost every $x$, $\abs{f_{k_j}(x) - f(x)} \leq 2^{-j/2}$ for all but finitely many $j$.
        Proof: The sets in <2>3 have summable measure, so almost every $x$ lies in only finitely many of them.
    <2>5. For such $x$, $f_{k_j}(x) \to f(x)$.
        Proof: $2^{-j/2} \to 0$.
    <2>6. Q.E.D.
        Proof: By <2>4 and <2>5, the subsequence $f_{k_j}$ converges to $f$ almost everywhere.

<1>3. Conclusion: (b) is false and (c) is true.
    Proof: By <1>1 and <1>2.
:::
