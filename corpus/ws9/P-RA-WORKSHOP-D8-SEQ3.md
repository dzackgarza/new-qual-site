---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-SEQ3
kind: problem
title: 'Uniform convergence without the Weierstrass M-test'
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

::: {.problem title="?"}
(January 2006, 4a) Let
$$
f_n(x):=
\begin{cases}
\dfrac1n,&x\in\left(\dfrac{1}{2^{n+1}},\dfrac{1}{2^n}\right],\\
0,&\text{otherwise}.
\end{cases}
$$
Show that $\sum_{n=1}^{\infty}f_n$ does not satisfy the Weierstrass M-test but that it nevertheless converges uniformly on $\mathbb R$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Show $\sum_{n=1}^\infty f_n$ with $f_n = \frac1n$ on $(2^{-(n+1)}, 2^{-n}]$, else $0$, does not satisfy the Weierstrass M-test yet converges uniformly on $\mathbb R$.

<1>1. The M-test fails: $\sup_{\mathbb R} |f_n| = 1/n$ and $\sum 1/n = \infty$.
Proof: $\|f_n\|_\infty = 1/n$ (attained on the interval $(2^{-(n+1)}, 2^{-n}]$); the harmonic series diverges, so no convergent $\sum M_n$ with $M_n \ge \|f_n\|_\infty$ exists.

<1>2. The supports are pairwise disjoint.
Proof: the intervals $(2^{-(n+1)}, 2^{-n}]$, $n \ge 1$, are disjoint and nested toward $0$; the exceptional overlap points $2^{-n}$ belong to exactly one interval each.
At most one $f_n$ is nonzero at any $x$.

<1>3. The series converges pointwise to $f(x) = \frac1n$ if $x \in (2^{-(n+1)}, 2^{-n}]$ for some $n$, and $f(x) = 0$ otherwise (in particular $f(0) = 0$). Proof: by <1>2, for each $x$ at most one term is nonzero, so the "series" at $x$ is either $0$ or the single value $f_n(x) = 1/n$.

<1>4. Uniform convergence on $\mathbb R$: for $N$, the tail satisfies $\sup_x\left|\sum_{n=N+1}^\infty f_n(x)\right| \le \frac{1}{N+1}$.
Proof: by <1>2, at each $x$ the tail is either $0$ or $f_n(x) = 1/n$ for the unique $n > N$ with $x$ in its support; the largest possible value is $1/(N+1)$, which is attained (e.g. at $x = 2^{-(N+2)}/2$). Since $1/(N+1) \to 0$, the tails are uniformly small: $\sum f_n$ converges uniformly on $\mathbb R$.

<1>5. Q.E.D. Proof: <1>1 shows the M-test fails; <1>4 shows uniform convergence anyway.
:::
