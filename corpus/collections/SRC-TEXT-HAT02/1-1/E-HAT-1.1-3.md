---
schema: qual/card@1
id: E-HAT-1.1-3
kind: problem
title: $\pi_1(X)$ abelian iff basepoint-change homomorphisms depend only on endpoints
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced the forward implication to conjugation by the loop h k-bar and the reverse implication to comparison with the constant path.
---

For a path-connected space $X$, show that $\pi_1(X)$ is abelian iff all basepoint-change homomorphisms $\beta_h$ depend only on the endpoints of the path $h$.

::: {.solution}
Fix points $x_0,x_1\in X$ and paths $h,k$ from $x_0$ to $x_1$.
Recall that
\[
\beta_h([f])=[h\cdot f\cdot\bar h]
\]
for $[f]\in\pi_1(X,x_1)$.

<1>1. Suppose $\pi_1(X)$ is abelian.
Then $\beta_h=\beta_k$ whenever $h$ and $k$ have the same endpoints.
::: {.proof}
Since $X$ is path connected, all fundamental groups at different basepoints are isomorphic, so it is enough that $\pi_1(X,x_0)$ is abelian.

For $[f]\in\pi_1(X,x_1)$, set
\[
a=[h\cdot\bar k]\in\pi_1(X,x_0),
\qquad
b=\beta_k([f])=[k\cdot f\cdot\bar k].
\]
Then
\[
a^{-1}=[k\cdot\bar h].
\]
Using associativity of path classes and cancellation of $\bar k\cdot k$ and $\bar h\cdot h$ up to homotopy,
\[
\begin{aligned}
a b a^{-1}
&=[h\cdot\bar k]\,[k\cdot f\cdot\bar k]\,[k\cdot\bar h]\\
&=[h\cdot f\cdot\bar h]\\
&=\beta_h([f]).
\end{aligned}
\]
Since $\pi_1(X,x_0)$ is abelian,
\[
a b a^{-1}=b.
\]
Therefore
\[
\beta_h([f])=\beta_k([f])
\]
for every $[f]$, so $\beta_h=\beta_k$.
:::

<1>2. Conversely, suppose every basepoint-change homomorphism depends only on the endpoints of its path.
Then $\pi_1(X,x_0)$ is abelian for every $x_0\in X$.
::: {.proof}
Fix $x_0\in X$ and let $h$ be any loop based at $x_0$.
Let $c$ be the constant path at $x_0$.
The paths $h$ and $c$ have the same endpoints, so by hypothesis
\[
\beta_h=\beta_c.
\]

For any $[f]\in\pi_1(X,x_0)$,
\[
\beta_h([f])=[h]\,[f]\,[h]^{-1},
\]
while
\[
\beta_c([f])=[f].
\]
Hence
\[
[h]\,[f]\,[h]^{-1}=[f].
\]
Multiplying on the right by $[h]$ gives
\[
[h]\,[f]=[f]\,[h].
\]
Both $[h]$ and $[f]$ were arbitrary, so $\pi_1(X,x_0)$ is abelian.
:::

<1>3. Therefore $\pi_1(X)$ is abelian if and only if the maps $\beta_h$ depend only on the endpoints of $h$.
::: {.proof}
The forward implication is <1>1 and the reverse implication is <1>2.
:::
:::
