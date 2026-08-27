---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-07
kind: problem
title: Prove the extreme value theorem in one real dimension
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Compactness
relations:
- kind: uses
  target: T-RA-WORKSHOP-D4-3-2
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(c.f. January 2007 #3a, June 2010 #2a) Prove Theorem 3.2 for a function $f:K\subset\mathbb R\to\mathbb R$.
(The proof is nearly unchanged when $n$ or $m$ is greater than 1.)
:::

:::: {.solution}
<1>1. Reduce to the one-dimensional extreme value theorem.
Proof: let $f: K \to \mathbb{R}$ be continuous with $K \subseteq \mathbb{R}$ compact.
We show $f$ attains a maximum; the minimum follows by applying the result to $-f$.
<1>2. $f(K)$ is bounded above.
Proof: suppose not; then for each $n$ there is $x_n \in K$ with $f(x_n) \ge n$.
Since $K$ is compact (sequentially compact in $\mathbb{R}$), a subsequence $x_{n_j} \to x \in K$.
By continuity $f(x_{n_j}) \to f(x)$, but $f(x_{n_j}) \ge n_j \to \infty$, contradiction.
<1>3. The supremum is attained.
Proof: let $M = \sup_{x \in K} f(x) < \infty$; choose $x_n \in K$ with $f(x_n) \to M$ (e.g. $f(x_n) \ge M - 1/n$). A subsequence $x_{n_j} \to x^* \in K$ (compactness), and by continuity $f(x^*) = \lim_j f(x_{n_j}) = M$.
Hence $f$ attains its maximum at $x^* \in K$.
<1>4. Q.E.D. Proof: $f$ attains both its maximum and (applied to $-f$) its minimum on $K$.
:::
