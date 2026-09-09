---
schema: qual/card@1
id: E-HAT-1.1-2
kind: problem
title: Basepoint-change homomorphism depends only on homotopy class
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Wrote the homotopy of conjugated loops explicitly and checked the pasting points and fixed basepoint.
---

Show that the change-of-basepoint homomorphism $\beta_h$ depends only on the homotopy class of $h$.

::: {.solution}
Let $h,k:I\to X$ be paths from $x_0$ to $x_1$ that are homotopic relative to their endpoints.
Thus there is a continuous map
\[
H:I\times I\to X
\]
such that
\[
H(s,0)=h(s),\qquad H(s,1)=k(s),\qquad
H(0,t)=x_0,\qquad H(1,t)=x_1.
\]

<1>1. Fix a loop $f:I\to X$ based at $x_1$.
For each $t\in I$, define a loop $F_t$ based at $x_0$ by
\[
F_t(s)=
\begin{cases}
H(3s,t),&0\le s\le \frac13,\\
f(3s-1),&\frac13\le s\le \frac23,\\
H(3-3s,t),&\frac23\le s\le1.
\end{cases}
\]
::: {.proof}
At $s=1/3$, the first and second formulas both equal $x_1$, since
\[
H(1,t)=x_1=f(0).
\]
At $s=2/3$, the second and third formulas both equal $x_1$, since
\[
f(1)=x_1=H(1,t).
\]
Hence the three formulas paste to a continuous path.
Moreover,
\[
F_t(0)=H(0,t)=x_0=H(0,t)=F_t(1),
\]
so $F_t$ is a loop based at $x_0$ for every $t$.
:::

<1>2. The map
\[
F:I\times I\to X,\qquad F(s,t)=F_t(s),
\]
is a homotopy of loops relative to the basepoint from
\[
h\cdot f\cdot\bar h
\quad\text{to}\quad
k\cdot f\cdot\bar k.
\]
::: {.proof}
On each of the three closed vertical strips in $I\times I$, the formula in <1>1 is continuous, and the formulas agree on the common boundaries; the pasting lemma gives continuity of $F$.
At $t=0$, the first and third pieces are $h$ and $\bar h$, while at $t=1$ they are $k$ and $\bar k$.
The endpoint computation in <1>1 shows that the basepoint $x_0$ is fixed throughout the homotopy.
:::

<1>3. For every $[f]\in\pi_1(X,x_1)$,
\[
\beta_h([f])=\beta_k([f]).
\]
::: {.proof}
By definition,
\[
\beta_h([f])=[h\cdot f\cdot\bar h],
\qquad
\beta_k([f])=[k\cdot f\cdot\bar k].
\]
These based loops are homotopic relative to the basepoint by <1>2, so they determine the same element of $\pi_1(X,x_0)$.
:::

<1>4. Therefore $\beta_h=\beta_k$, so the change-of-basepoint homomorphism depends only on the homotopy class of $h$.
::: {.proof}
The equality in <1>3 holds for every element of $\pi_1(X,x_1)$.
:::
:::
