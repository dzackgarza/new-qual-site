---
schema: qual/card@1
id: P-PRACT20-W4-18
kind: problem
title: Sum, union, intersection and complement of subspaces
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Subspaces
relations: []
review: draft
---

::: {.problem}
If $A,B$ are subspaces of $V$, which of the following are necessarily subspaces of $V$?

(a) $A+B=\{x+y:x\in A,\ y\in B\}$
(b) $A\cup B$
(c) $A\cap B$
(d) $A^c=\{x\in V:x\notin A\}$
:::

::: {.solution}
<1>1. The sum
\[
\boxed{A+B}
\]
is always a subspace of $V$.

::: {.proof}
Since
\[
0=0+0
\]
with $0\in A$ and $0\in B$, one has $0\in A+B$.

Let
\[
u=a_1+b_1,
\qquad
v=a_2+b_2
\]
belong to $A+B$, and let $\lambda,\mu$ be scalars. Then
\[
\lambda u+\mu v
=
(\lambda a_1+\mu a_2)
+
(\lambda b_1+\mu b_2).
\]
Because $A$ and $B$ are subspaces,
\[
\lambda a_1+\mu a_2\in A,
\qquad
\lambda b_1+\mu b_2\in B.
\]
Hence
\[
\lambda u+\mu v\in A+B.
\]
:::

<1>2. The intersection
\[
\boxed{A\cap B}
\]
is always a subspace of $V$.

::: {.proof}
Both subspaces contain $0$, so
\[
0\in A\cap B.
\]
If $u,v\in A\cap B$ and $\lambda,\mu$ are scalars, then $u,v$ lie in each
of $A$ and $B$. Since each is a subspace,
\[
\lambda u+\mu v
\]
belongs to both $A$ and $B$, hence to their intersection.
:::

<1>3. The union
\[
A\cup B
\]
need not be a subspace.

::: {.proof}
Take
\[
V=\mathbb R^2,
\qquad
A=\operatorname{span}\{(1,0)\},
\qquad
B=\operatorname{span}\{(0,1)\}.
\]
Then
\[
(1,0)\in A\cup B,
\qquad
(0,1)\in A\cup B,
\]
but
\[
(1,1)
=(1,0)+(0,1)
\notin A\cup B.
\]
Thus $A\cup B$ is not closed under addition.
:::

<1>4. The complement
\[
A^c
\]
is never a subspace.

::: {.proof}
Every subspace $A$ contains the zero vector, so
\[
0\notin A^c.
\]
If $A\ne V$, the complement is nonempty but fails the necessary condition
that a subspace contain $0$. If $A=V$, then
\[
A^c=\varnothing,
\]
which also does not contain $0$ and is not a subspace.
:::

<1>5. Therefore the necessarily-subspace choices are exactly
\[
\boxed{\text{(a) and (c)}}.
\]

::: {.proof}
Steps <1>1 and <1>2 prove that (a) and (c) always work, while steps <1>3
and <1>4 give the failures of (b) and (d).
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the complete answer.
:::
:::
