---
schema: qual/card@1
id: E-PEXB6
kind: problem
title: A rational fan and a nowhere locally connected path-connected set
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

Let $X$ denote the rational points of the interval $[0, 1] \times 0$ of $\mathbb{R}^2$.
Let $T$ denote the union of all line segments joining the point $p = 0 \times 1$ to points of $X$.

(a) Show that $T$ is path connected, but is locally connected only at the point $p$.

(b) Find a subset of $\mathbb{R}^2$ that is path connected but is locally connected at none of its points.
:::

::: {.solution}
For $q\in[0,1]\cap\QQ$ write $s_q$ for the segment from $p=(0,1)$ to $(q,0)$, so $T=\bigcup_qs_q$. A space is locally connected at $z$ if every neighborhood of $z$ contains a connected open neighborhood of $z$.

<1>1. $T$ is path connected and locally connected at $p$.

::: {.proof}
Each $s_q$ contains $p$, so $T$ is star-shaped about $p$: every $z\in T$ is joined to $p$ by the segment $[z,p]\subseteq T$.
For $\varepsilon>0$ the open set $B(p,\varepsilon)\cap T$ is also star-shaped about $p$, because $B(p,\varepsilon)$ is convex, so it is path connected.
:::

<1>2. On $T-\{p\}$ the function $\varphi(x,y)=x/(1-y)$ is continuous and equals $q$ on $s_q-\{p\}$; hence every connected subset of $T-\{p\}$ lies in a single segment $s_q$.

::: {.proof}
The point of $s_q$ at height $y<1$ is $(q(1-y),y)$, and $1-y\ne0$ on $T-\{p\}$.
The image of a connected set under $\varphi$ is a connected subset of $\RR$ contained in $\QQ$, hence a single point.
:::

<1>3. $T$ is not locally connected at any $z\ne p$.

::: {.proof}
Let $z=(q(1-y_0),y_0)\in s_q$ with $y_0<1$, and let $U$ be a neighborhood of $z$ in $T$ with $p\notin U$.
A connected open neighborhood $V\subseteq U$ of $z$ would lie in $s_q$ by step <1>2.
But the points $(q'(1-y_0),y_0)\in s_{q'}$ with rational $q'\ne q$ and $q'\to q$ converge to $z$ and lie outside $s_q$, so no such $V$ is open in $T$.
:::

<1>4. For $k\ge0$ let $T_k=T+(0,k)$, the union of the segments from $a_k=(0,k+1)$ to the points $(q,k)$ with $q\in[0,1]\cap\QQ$, and let $Y=\bigcup_{k\ge0}T_k$. Then $Y$ is path connected.

::: {.proof}
Each $T_k$ is path connected by step <1>1, and $a_k=(0,k+1)$ is the endpoint with $q=0$ of a segment of $T_{k+1}$, so $T_k$ and $T_{k+1}$ meet.
Any two points of $Y$ lie in $T_j\cup T_{j+1}\cup\cdots\cup T_k$ for some $j\le k$, a path-connected union of consecutively meeting path-connected sets.
:::

<1>5. $Y$ is not locally connected at $a_{k-1}=(0,k)$ for $k\ge1$.

::: {.proof}
Let $U=Y\cap B(a_{k-1},\frac12)$, so that $U=(U\cap T_k)\cup(U\cap T_{k-1})$ and the two pieces meet only in $a_{k-1}$.
Each $T_j$ is closed in $Y$, because its limit points outside $T_j$ lie on segments from $a_j$ to irrational points $(s,j)$, which miss $Y$; so both pieces are closed in $U$.
Let $\psi(x,y)=x/(k+1-y)$ on $U\cap T_k$ and $\psi=0$ on $U\cap T_{k-1}$.
Both give $0$ at $a_{k-1}$, so $\psi\colon U\to\RR$ is continuous by the pasting lemma, and its values are rational; hence $\psi\equiv0$ on every connected subset of $U$ containing $a_{k-1}$.
Every neighborhood of $a_{k-1}$ contains points $(q(1-t),k+t)$ of $T_k$ with rational $q>0$ and small $t>0$, where $\psi=q\ne0$.
So no connected open neighborhood of $a_{k-1}$ lies in $U$.
:::

<1>6. $Y$ is not locally connected at any point $z\in T_k-\{a_k\}$ other than the points $(0,k)$ with $k\ge1$.

::: {.proof}
Write $z=(x_0,y_0)$, so $k\le y_0<k+1$.
The segments of $T_{k+1}$ lie in $\{y\ge k+1\}$, and a point $(x,y)$ of $T_{k-1}$ has $0\le x\le k-y$.
Hence if $k=0$, or $y_0>k$, or $x_0>0$, a small open disk $D$ about $z$ satisfies $D\cap Y=D\cap T_k$ and $a_k\notin D$.
The set $T_k$ is a translate of $T$, so step <1>3 shows that $D\cap T_k$ contains no connected open neighborhood of $z$.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 prove (a).
For (b), every point of $Y$ is either a point $(0,k)=a_{k-1}$ with $k\ge1$ or a point of some $T_k-\{a_k\}$ covered by step <1>6.
By steps <1>4, <1>5, and <1>6, $\boxed{Y}$ is path connected and locally connected at none of its points.
:::
:::
