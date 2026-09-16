---
schema: qual/card@1
id: P-2V6GL
kind: problem
title: Connected versus locally connected spaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
- Find a space that is connected but not locally connected.
  Can there be a space that is locally connected but not connected?
:::

::: {.solution}
**Goal.** Find a connected but not locally connected space, and answer the converse question.

<1>1. A connected but not locally connected space: the topologist's sine curve.
<2>1. $X = \theset{(x, \sin(1/x)) : x > 0} \cup \theset{(0, y) : -1 \le y \le 1}$.
::: {.proof}
the topologist's sine curve.
:::
<2>2. $X$ is connected.
::: {.proof}
the graph $\theset{(x, \sin(1/x)) : x > 0}$ is connected (continuous image of $(0,\infty)$), and its closure is $X$, so $X$ is connected.
:::
<2>3. $X$ is not locally connected at $p=(0,0)$.
::: {.proof}
Let
$$
U=X\cap\bigl(\mathbb R\times(-1/2,1/2)\bigr),
$$
an open neighborhood of $p$ in $X$. We claim that the connected component of $p$ in $U$ is exactly
$$
C=\{0\}\times(-1/2,1/2).
$$
Certainly $C$ is connected and contains $p$.

Now let
$$
q=(x_q,\sin(1/x_q))\in U
$$
be any point of the oscillating graph, so $x_q>0$. Choose $m$ sufficiently large that
$$
c=\frac1{\pi/2+2\pi m}<x_q.
$$
Then $\sin(1/c)=1$, so $U$ contains no point whose first coordinate is $c$. Consequently
$$
U_- = U\cap\{x<c\},\qquad U_+=U\cap\{x>c\}
$$
form a separation of $U$: both are relatively open, and because $U$ has no point with first coordinate $c$, each is also the complement of the other in $U$. We have $p\in U_-$ and $q\in U_+$. Hence no connected subset of $U$ containing $p$ can contain any graph point. This proves that the component of $p$ in $U$ is precisely $C$.

Finally, $C$ is not a neighborhood of $p$ in $X$. Every Euclidean neighborhood of $(0,0)$ meets the graph $\{(x,\sin(1/x)):x>0\}$ at points with $x>0$ and $\sin(1/x)$ arbitrarily close to $0$. Thus there is no connected open set $W$ with
$$
p\in W\subseteq U,
$$
because any such $W$ would have to lie in the component $C$ but $C$ contains no neighborhood of $p$. Therefore $X$ is not locally connected at $p$.
:::

<1>2. A locally connected but not connected space exists.
<2>1. Example: the disjoint union of two intervals, $X = (0,1) \cup (2,3)$.
::: {.proof}
a disjoint union of two open intervals.
:::
<2>2. $X$ is locally connected.
::: {.proof}
each point has a connected neighborhood (a small interval around it).
:::
<2>3. $X$ is not connected.
::: {.proof}
it is a disjoint union of two nonempty open sets.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 gives a connected but not locally connected space; <1>2 gives a locally connected but not connected space (yes, such spaces exist).
:::
:::
