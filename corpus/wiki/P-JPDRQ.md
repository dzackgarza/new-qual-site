---
schema: qual/card@1
id: P-JPDRQ
kind: exercise
title: "- Can a convergent sequence of real numbers have a subsequence conver\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - uniform-convergence
  - convergence-of-functions
relations: []
review: draft
---

::: exercise
- Can a convergent sequence of real numbers have a subsequence converging to a different limit?

- What does it mean for a sequence of functions to converge **pointwise** and to converge **uniformly**?

  - Give an example of a sequence that converges pointwise but not uniformly.

- Prove that every sequence admits a monotone subsequence.

- Prove the monotone convergence theorem for sequences.

- Prove the Bolzano-Weierstrass Theorem.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. A convergent sequence cannot have a subsequence converging to a different limit.
    Proof: if $x_n \to x$ then every subsequence converges to $x$: for $\eps > 0$ all but finitely many terms lie within $\eps$ of $x$, so the same holds for the subsequence; limits are unique in $\RR$.

<1>2. Pointwise vs uniform convergence: $f_n \to f$ pointwise iff $f_n(x) \to f(x)$ for each $x$ individually; uniformly iff $\sup_x |f_n(x) - f(x)| \to 0$ (the same $N$ works for all $x$ simultaneously).
    Proof: definitions.

<1>3. Example converging pointwise but not uniformly: $f_n(x) = x^n$ on $[0,1]$.
    Proof: pointwise limit is $\chi_{\{1\}}$ (for $x \in [0,1)$, $x^n \to 0$; at $1$, $1^n = 1$), but $\sup_{[0,1]}|x^n - \chi_{\{1\}}| = 1 \not\to 0$.

<1>4. Every sequence admits a monotone subsequence.
    <2>1. Call index $n$ a "peak" if $a_n \ge a_m$ for all $m \ge n$.
        Proof: definition.
    <2>2. If there are infinitely many peaks, they form a decreasing subsequence.
        Proof: peak at $n_1 < n_2$ with both peaks: $a_{n_1} \ge a_{n_2}$.
    <2>3. If there are finitely many peaks, let $n_1$ be beyond the last peak; then each $n_k$ has some $m > n_k$ with $a_m > a_{n_k}$, giving an increasing subsequence $a_{n_1} < a_{n_2} < \cdots$.
        Proof: $n_k$ is not a peak, so some later term is strictly larger; pick it greedily.

<1>5. Monotone convergence theorem for sequences: a monotone (say increasing) sequence bounded above converges to its supremum; an unbounded increasing sequence diverges to $\infty$.
    <2>1. Bounded case: let $s = \sup\{a_n\}$; given $\eps > 0$, $s - \eps$ is not an upper bound, so $a_N > s - \eps$ for some $N$; monotonicity gives $s - \eps < a_n \le s$ for all $n \ge N$.
        Proof: definition of supremum; monotonicity.
    <2>2. Unbounded case: for any $M$, some $a_N > M$, and monotonicity gives $a_n \ge a_N > M$ for $n \ge N$.
        Proof: unboundedness; monotonicity.

<1>6. Bolzano–Weierstrass: every bounded sequence has a convergent subsequence.
    Proof: by <1>4 the sequence has a monotone subsequence, which is bounded (the original sequence is bounded), so it converges by <1>5.
:::
