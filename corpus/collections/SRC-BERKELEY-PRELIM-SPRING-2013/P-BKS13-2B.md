---
schema: qual/card@1
id: P-BKS13-2B
kind: problem
title: Nested intersections of closed connected subsets of a compact metric space
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 4 of the retained Spring 2013 solution PDF and independently reviewed both the compactness argument and the noncompact counterexample.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the finite-subcover contradiction and the decreasing connected closed subsets of R^2 whose intersection is two vertical lines.
---

::: {.problem}
Prove that the intersection of a decreasing sequence of closed connected subsets of a compact metric space is connected. Give an example to show that this is false if the assumption that the space is compact is dropped.
:::

::: {.solution}
Let $S$ be the compact metric space, and let
$$
X_1\supseteq X_2\supseteq X_3\supseteq\cdots
$$
be closed connected subsets of $S$. Set
$$
X\coloneqq\bigcap_{n=1}^{\infty}X_n.
$$

<1>1. If some $X_n$ is empty, then $X$ is connected.

::: {.proof}
If $X_n=\varnothing$ for some $n$, then
$$
X\subseteq X_n=\varnothing,
$$
so $X=\varnothing$. The empty space is connected.
:::

<1>2. Suppose every $X_n$ is nonempty. Then $X$ is nonempty.

::: {.proof}
The sets $X_n$ are closed subsets of the compact space $S$, hence compact.
Because they are decreasing, every finite subcollection has nonempty
intersection: the intersection of
$$
X_{n_1},\ldots,X_{n_r}
$$
is the set with largest index. Thus the family has the finite intersection
property. Compactness of $S$ gives
$$
\bigcap_{n=1}^{\infty}X_n\neq\varnothing.
$$
:::

<1>3. Suppose, for contradiction, that the nonempty set $X$ is
disconnected. Then there are disjoint nonempty closed subsets
$$
Y,Z\subseteq X
$$
with
$$
X=Y\cup Z.
$$

::: {.proof}
This is the definition of disconnectedness, using a separation by two
nonempty subsets that are both open and closed in $X$. Since $X$ is
compact, such subsets are compact and therefore closed in the ambient
metric space $S$.
:::

<1>4. There are disjoint open sets
$$
U,V\subseteq S
$$
such that
$$
Y\subseteq U,
\qquad
Z\subseteq V.
$$

::: {.proof}
The sets $Y$ and $Z$ are disjoint compact subsets of the metric space
$S$. Their distance is positive:
$$
d(Y,Z)>0.
$$
Taking open neighborhoods of radius less than
$$
\frac12d(Y,Z)
$$
gives disjoint open sets containing them.
:::

<1>5. The collection
$$
U,\quad V,\quad S\setminus X_1,\quad S\setminus X_2,\quad\ldots
$$
is an open cover of $S$.

::: {.proof}
Every point of
$$
X=Y\cup Z
$$
lies in $U\cup V$. If
$$
s\in S\setminus X,
$$
then by the definition of the intersection there is some $n$ such that
$$
s\notin X_n.
$$
Thus every point of $S$ lies in one of the displayed open sets.
:::

<1>6. There is an index $N$ such that
$$
X_N\subseteq U\cup V.
$$

::: {.proof}
By compactness, the open cover in step <1>5 has a finite subcover. Let
$N$ be the largest index among the finitely many complements
$$
S\setminus X_n
$$
that occur in that subcover. Since the sequence $X_n$ is decreasing, the
complements are increasing, so all those finitely many complements are
contained in
$$
S\setminus X_N.
$$
Hence
$$
S
=
U\cup V\cup(S\setminus X_N),
$$
which is equivalent to the claimed inclusion.
:::

<1>7. The inclusion in step <1>6 contradicts the connectedness of $X_N$.

::: {.proof}
Since
$$
Y,Z\subseteq X\subseteq X_N,
$$
the sets
$$
X_N\cap U
\qquad\text{and}\qquad
X_N\cap V
$$
are both nonempty. They are disjoint and open in the subspace topology on
$X_N$. By step <1>6 they cover $X_N$. This is a separation of $X_N$,
contrary to its connectedness.
:::

<1>8. Therefore
$$
\boxed{
\bigcap_{n=1}^{\infty}X_n
\text{ is connected}
}.
$$

::: {.proof}
Step <1>1 handles the case of an empty $X_n$. Otherwise, steps
<1>2--<1>7 rule out disconnectedness of the intersection.
:::

<1>9. Without compactness the assertion can fail.

::: {.proof}
Take the ambient space
$$
S=\RR^2
$$
and, for $n\geq1$, define
$$
X_n
\coloneqq
\{(0,y):y\in\RR\}
\cup
\{(1,y):y\in\RR\}
\cup
\{(x,y):y\geq n\}.
$$
Each $X_n$ is closed. It is connected because the closed upper half-plane
$$
\{y\geq n\}
$$
is connected and intersects both vertical lines, so the union is
connected. The sequence is decreasing.

Its intersection is
$$
\bigcap_{n=1}^{\infty}X_n
=
\{(0,y):y\in\RR\}
\cup
\{(1,y):y\in\RR\},
$$
because no point with $x\notin\{0,1\}$ can satisfy $y\geq n$ for every
$n$. The two vertical lines are disjoint nonempty closed-and-open subsets
of this intersection, so the intersection is disconnected.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>8 proves the compact case, and step <1>9 gives the required
counterexample in a noncompact metric space.
:::
:::
