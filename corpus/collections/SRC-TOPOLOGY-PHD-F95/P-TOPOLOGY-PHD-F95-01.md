---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-01
kind: problem
title: The pasting lemma for two closed subspaces
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section I, problem 1 of the 23 September 1995 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Proved the closed-cover pasting lemma by closed preimages, recorded the
    open-cover variant showing closedness is not necessary, and gave a
    counterexample showing that one closed member alone does not suffice.
---

::: {.problem}
Let $A$ and $B$ be closed subspaces of a topological space $X$ with $X=A\cup B$.
Suppose that $f:A\to Y$ and $g:B\to Y$ are continuous, and $f(x)=g(x)$ for all $x\in A\cap B$.
Prove that $h:X\to Y$ by
$$
h(x)=
\begin{cases}
f(x) & \text{if }x\in A,\\
g(x) & \text{if }x\in B
\end{cases}
$$
is continuous.
Is it necessary for both $A$ and $B$ to be closed?
Discuss.
:::

::: {.solution}
<1>1. The formula defining $h$ is well defined.
::: {.proof}
If $x\in A\setminus B$, only the value $f(x)$ is prescribed, and if $x\in B\setminus A$, only the value $g(x)$ is prescribed.
If $x\in A\cap B$, the two prescriptions agree by hypothesis:
\[
f(x)=g(x).
\]
Since $X=A\cup B$, this defines one value $h(x)$ for every $x\in X$.
:::

<1>2. The map $h:X\to Y$ is continuous.
::: {.proof}
It is enough to show that the inverse image under $h$ of every closed subset of $Y$ is closed in $X$.
Let $C\subseteq Y$ be closed.
Then
\[
h^{-1}(C)=f^{-1}(C)\cup g^{-1}(C).
\]
Since $f$ is continuous, $f^{-1}(C)$ is closed in the subspace $A$.
Because $A$ is closed in $X$, every subset closed in $A$ is closed in $X$: indeed, there is a closed set $F\subseteq X$ with
\[
f^{-1}(C)=A\cap F,
\]
and the intersection of two closed subsets of $X$ is closed.
Thus $f^{-1}(C)$ is closed in $X$.
The same argument shows that $g^{-1}(C)$ is closed in $X$.
Therefore their finite union $h^{-1}(C)$ is closed in $X$.
Hence $h$ is continuous.
:::

<1>3. It is not necessary that both $A$ and $B$ be closed.
::: {.proof}
A parallel pasting lemma holds when $A$ and $B$ are both open.
Indeed, suppose $A$ and $B$ are open in $X$, still cover $X$, and $f$ and $g$ are continuous and agree on $A\cap B$.
For every open set $U\subseteq Y$,
\[
h^{-1}(U)=f^{-1}(U)\cup g^{-1}(U).
\]
Now $f^{-1}(U)$ is open in $A$, hence open in $X$ because $A$ is open; similarly $g^{-1}(U)$ is open in $X$.
Thus $h^{-1}(U)$ is open in $X$.

For a concrete cover by sets that are not closed, take
\[
X=\RR,
\qquad
A=(-\infty,1),
\qquad
B=(-1,\infty).
\]
Both $A$ and $B$ are open and nonclosed, yet every pair of continuous maps on them that agree on $A\cap B$ pastes to a continuous map on $X$.
Therefore closedness of both pieces is sufficient, not necessary.
:::

<1>4. On the other hand, without a common open-cover or closed-cover hypothesis, agreement on the overlap does not force the pasted map to be continuous.
::: {.proof}
Take
\[
X=\RR,
\qquad
A=(-\infty,0],
\qquad
B=(0,\infty),
\qquad
Y=\RR.
\]
Then $A$ is closed, $B$ is open, $X=A\cup B$, and $A\cap B=\varnothing$.
Define
\[
f(x)=0\quad(x\in A),
\qquad
g(x)=1\quad(x\in B).
\]
Both maps are continuous, and the agreement condition on $A\cap B$ is vacuous.
The pasted map is
\[
h(x)=
\begin{cases}
0,&x\le0,\\
1,&x>0,
\end{cases}
\]
which is not continuous at $0$.
Thus, for this general pasting assertion, merely requiring one member of the cover to be closed is not enough.
:::
:::
