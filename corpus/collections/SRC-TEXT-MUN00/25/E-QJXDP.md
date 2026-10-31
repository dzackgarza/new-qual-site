---
schema: qual/card@1
id: E-QJXDP
kind: problem
title: Weak local connectedness at a point without local connectedness
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Consider the "infinite broom" $X$ pictured in Figure 25.1 of the text.
Show that $X$ is not locally connected at $p$, but is weakly locally connected at $p$.
[Hint: Any connected neighborhood of $p$ must contain all the points $a_i$.]
:::

::: {.solution}
Use the following planar realization of the pictured broom. Put
$$
p=(0,0),\qquad a_n=(1/n,0),\qquad b_{n,k}=(1/(n+1),1/(nk))
$$
for $n,k\ge1$. Let $S_{n,k}$ be the line segment from $a_n$ to $b_{n,k}$, and set
$$
X=([0,1]\times\{0\})\cup\bigcup_{n,k\ge1}S_{n,k}.
$$
For each $n$, the free endpoints $b_{n,k}$ tend to $a_{n+1}$, while every segment $S_{n,k}$ is attached to the axis at $a_n$.

Let $U$ be any neighborhood of $p$ in $X$. Choose $\varepsilon>0$ with $B(p,\varepsilon)\cap X\subseteq U$, and choose $N$ so large that $\sqrt2/N<\varepsilon$. The set
$$
C_N=([0,1/N]\times\{0\})\cup\bigcup_{n\ge N,\ k\ge1}S_{n,k}
$$
lies in $B(p,\varepsilon)\cap X$: every point in it has both coordinates at most $1/N$. It is path connected, since each segment meets the axis at $a_n$. It contains the neighborhood $B(p,\delta)\cap X$ of $p$ for any sufficiently small $\delta<1/(N+1)$, because every point of $X$ with first coordinate below $\delta$ lies on the displayed axis segment or on a segment with index $n\ge N$. Thus $X$ is weakly locally connected at $p$.

Now let $U_0=B(p,1/2)\cap X$, which does not contain $a_1$. Suppose that a connected open neighborhood $V$ of $p$ were contained in $U_0$. Since $a_n\to p$, openness at $p$ gives $a_n\in V$ for all sufficiently large $n$.

We claim that $a_{n+1}\in V$ forces $a_n\in V$. Indeed, $b_{n,k}\to a_{n+1}$, so openness of $V$ gives $b_{n,k}\in V$ for some $k$. If $a_n\notin V$, then $S_{n,k}\setminus\{a_n\}$ is a clopen subset of $X\setminus\{a_n\}$: the segment is closed, and away from its attachment point it is locally isolated from the other segments and the axis. Its intersection with $V$ is a nonempty proper clopen subset of $V$, contrary to connectedness. The claim follows.

Starting with one of the points $a_n\in V$ and applying the claim repeatedly gives $a_1\in V$, contradicting $V\subseteq U_0$. Hence $X$ is not locally connected at $p$.
:::
