---
schema: qual/card@1
id: P-BPL7E
kind: problem
title: "Let \\( (X, \\mathcal{M}, \\mu) \\) be a finite measure space and let \\( \\\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - egorov
  - measure-theory
  - l1
relations: []
review: draft
solved: true
---

::: problem
Let \( (X, \mathcal{M}, \mu)  \) be a finite measure space and let \( \ts{ f_n}_{n=1}^{\infty } \subseteq L^1(X, \mu) \). Suppose $f\in L^1(X, \mu)$ such that $f_n(x) \converges{n\to \infty }\to f(x)$ for almost every $x \in X$.
Prove that for every \( \eps > 0 \) there exists $M>0$ and a set $E\subseteq X$ such that \( \mu(E) \leq \eps \) and \( \abs{f_n(x)}\leq M  \) for all $x\in X\sm E$ and all $n\in \NN$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Define $g(x) = \sup_{n \ge 1}|f_n(x)|$ (extended real-valued).
Proof: $g$ is measurable as the supremum of countably many measurable functions.

<1>2. $g(x) < \infty$ for almost every $x$.
Proof: for a.e. $x$, $f_n(x) \to f(x) \in \RR$, so the sequence $(f_n(x))$ is bounded and $\sup_n|f_n(x)| < \infty$.

<1>3. $\mu\{g > M\} \to 0$ as $M \to \infty$.
Proof: the sets $\{g > M\}$ decrease to $\{g = \infty\}$ as $M \to \infty$, which has measure $0$ by <1>2; since $\mu(X) < \infty$, continuity from above gives $\mu\{g > M\} \to \mu\{g = \infty\} = 0$.

<1>4. Given $\eps > 0$, choose $M$ with $\mu\{g > M\} < \eps$ and set $E = \{g > M\}$; then $\mu(E) \le \eps$ and $|f_n(x)| \le M$ for all $x \in X \setminus E$ and all $n$.
Proof: <1>3 gives $M$; for $x \notin E$: $g(x) \le M$, so $|f_n(x)| \le g(x) \le M$ for every $n$ by definition of $g$.

<1>5. Q.E.D. Proof: <1>4 is exactly the claim.
(Note: only the a.e. convergence and finiteness of $\mu$ are used; the $L^1$ hypotheses are not needed for this conclusion.)
:::
