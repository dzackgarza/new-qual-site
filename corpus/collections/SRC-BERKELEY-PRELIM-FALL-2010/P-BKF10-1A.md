---
schema: qual/card@1
id: P-BKF10-1A
kind: problem
title: Nested closed connected subsets of a compact metric space have connected nonempty intersection
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 1A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the nested-compact intersection argument and the compact
    separation argument ruling out a disconnected intersection.
---

::: {.problem}
Let
$$
\cdots\subset X_2\subset X_1
$$
be a nested sequence of closed, nonempty, connected subsets of a compact metric space $X$.
Prove that $\bigcap_{i=1}^{\infty}X_i$ is nonempty and connected.
:::

::: {.solution}
Put
$$
K\coloneqq\bigcap_{i=1}^{\infty}X_i.
$$

<1>1. Every $X_i$ is compact.

::: {.proof}
Each $X_i$ is closed in the compact space $X$, and a closed subset of a
compact space is compact.
:::

<1>2. The intersection $K$ is nonempty.

::: {.proof}
Suppose $K=\varnothing$. Then the open sets
$$
X\setminus X_1\subseteq X\setminus X_2\subseteq\cdots
$$
cover $X$. By compactness of $X$, finitely many of them cover $X$.
Because the cover is increasing, its largest member already covers $X$;
thus $X\setminus X_N=X$ for some $N$, so $X_N=\varnothing$. This
contradicts the hypothesis that every $X_i$ is nonempty.
:::

<1>3. Suppose, for contradiction, that $K$ is disconnected. Then there
exist disjoint nonempty compact sets $A,B\subseteq K$ with
$$
K=A\cup B.
$$

::: {.proof}
A separation of $K$ writes it as the disjoint union of two nonempty sets
$A$ and $B$ that are both open and closed in the subspace $K$. Since
$K$ is closed in $X$, it is compact; hence the closed subsets $A$ and
$B$ of $K$ are compact.
:::

<1>4. There exist disjoint open subsets $U,V\subseteq X$ such that
$$
A\subseteq U,
\qquad
B\subseteq V.
$$

::: {.proof}
The compact sets $A$ and $B$ are disjoint in the metric space $X$.
Therefore their distance
$$
d(A,B)=\min\{d(a,b):a\in A,\ b\in B\}
$$
is a positive number $\delta$. Taking the open $\delta/3$-neighborhoods
of $A$ and $B$ gives disjoint open sets $U$ and $V$ containing them.
:::

<1>5. For some $N$, one has
$$
X_N\subseteq U\cup V.
$$

::: {.proof}
Define
$$
F_i\coloneqq X_i\setminus(U\cup V).
$$
Each $F_i$ is compact by step <1>1, and the sequence $(F_i)$ is nested.
Moreover,
$$
\bigcap_{i=1}^{\infty}F_i
=K\setminus(U\cup V)
=\varnothing,
$$
because $K=A\cup B\subseteq U\cup V$. Applying the nested-compact
argument from step <1>2 to $(F_i)$ shows that some $F_N$ is empty.
Equivalently, $X_N\subseteq U\cup V$.
:::

<1>6. The inclusion in step <1>5 contradicts connectedness of $X_N$.

::: {.proof}
Since $A,B\subseteq K\subseteq X_N$, the set $X_N$ meets both $U$ and
$V$. By step <1>5,
$$
X_N=(X_N\cap U)\cup(X_N\cap V).
$$
The two sets on the right are disjoint, nonempty, and open in the
subspace topology on $X_N$. Thus they form a separation of $X_N$,
contradicting the hypothesis that $X_N$ is connected.
:::

<1>7. Therefore $K$ is nonempty and connected.

::: {.proof}
Nonemptiness is step <1>2. Steps <1>3--<1>6 show that assuming
disconnectedness leads to a contradiction.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is exactly the required conclusion.
:::
:::
