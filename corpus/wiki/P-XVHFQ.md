---
schema: qual/card@1
id: P-XVHFQ
kind: problem
title: $\sum f_n$ with $f_n=\frac1n$ on $(2^{-(n+1)},2^{-n}]$ converges uniformly without the Weierstrass $M$-test
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - series-of-functions
  - counterexamples
relations: []
review: draft
solved: true
---

::: problem
Let $$f_n(x) = \begin{cases} \frac{1}{n}  & x \in (\frac{1}{2^{n+1}}, \frac{1}{2^n}] \\ 0 & \text{ otherwise}.\end{cases}$$

Show that $\sum_{n=1}^\infty f_n$ does not satisfy the Weierstrass M-test but that it nevertheless converges uniformly on $\mathbb{R}$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. The Weierstrass M-test does not apply.
Proof: the M-test requires $\sum_n M_n < \infty$ where $M_n = \sup_x |f_n(x)|$.
Here $M_n = 1/n$ (the supremum of $f_n$ on its support is $1/n$), and $\sum_n 1/n = \infty$, so the hypothesis of the M-test fails and it cannot be used.
<1>2. The supports $\supp f_n = (2^{-(n+1)}, 2^{-n}]$ are pairwise disjoint.
Proof: the intervals $(2^{-(n+1)}, 2^{-n}]$ for $n = 1, 2, \ldots$ are disjoint (they partition $(0, 1/2]$), and $f_n = 0$ elsewhere.
Hence for each $x$, at most one of the values $f_n(x)$ is nonzero.
<1>3. Pointwise limit: $S(x) = \sum_n f_n(x) = f_{n(x)}(x)$ where $n(x)$ is the unique index with $x \in (2^{-(n+1)}, 2^{-n}]$, and $S(x) = 0$ otherwise.
Proof: by <1>2, at most one term is nonzero at each $x$, so the series converges trivially.
<1>4. Uniform convergence on $\RR$.
Proof: for the tail, $S(x) - S_N(x) = \sum_{n>N} f_n(x)$, which by <1>2 is either $0$ (if the support containing $x$ has index $\le N$) or $f_n(x) = 1/n \le 1/(N+1)$ (if its index is $n > N$). Hence \[ \sup_{x\in\RR}\big|S(x) - S_N(x)\big| \le \frac{1}{N+1} \to 0, \] so the series converges uniformly.
<1>5. Q.E.D.
:::
