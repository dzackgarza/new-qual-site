---
schema: qual/card@1
id: E-KKI5A
kind: problem
title: The circles of radius n about (n,0) form a free group on countably many generators
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Free Groups
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §71 Exercise 5, printed p. 438. A published solution is Takumi Murayama, Selected Solutions to
    Munkres's Topology, 2nd Ed. (MAT365, Princeton, Fall 2012), §71 (printed there as Exercise 71.5), and it is
    defective in (b): it concludes that the image of a loop meets only finitely many circles from the
    boundedness of that image, which is false, since every circle $S_n$ passes through the base point and so
    meets every ball about it, and it then asserts without proof that a homotopy can be carried out
    excursion by excursion. Its (a) is correct and is kept. The card's (b) replaces the appeal to
    boundedness by the observation that a nonzero excursion into $S_n$ is a loop whose image is all of $S_n$,
    hence reaches distance $2n$ from $p$; that is what bounds the circles a loop can use. The retraction
    $r_N$ and the injectivity argument are Murayama's. Checked against Theorem 71.1 (printed p. 434), Example 1 of §71 (printed p. 436) and the
    countability material of §30 (printed pp. 190--191).
---

::: {.exercise}

Let $S_n$ be the circle of radius $n$ in $\RR^2$ whose center is at the point $(n, 0)$.
Let $Y$ be the subspace of $\RR^2$ that is the union of these circles; let $p$ be their common point.

(a) Show that $Y$ is not homeomorphic to a countably infinite wedge $X$ of circles, nor to the space of Example 1.

(b) Show, however, that $\pi_1(Y, p)$ is a free group with $\theset{[f_n]}$ as a system of free generators, where $f_n$ is a loop representing a generator of $\pi_1(S_n, p)$.
:::

::: {.solution}

The circle $S_n$ has equation $x^2+y^2=2nx$; all the circles pass through $p=(0,0)$, and $S_n$ reaches the point $(2n,0)$.

::: pf

::: pf-step

(a) $Y$ is not homeomorphic to the countably infinite wedge, nor to the infinite earring.

::: pf-proof

$Y$ is a subspace of the second-countable space $\RR^2$ (Example 1, printed p. 190), hence second-countable (Theorem 30.2, printed p. 191) and therefore first countable (printed p. 190, where the second axiom is shown to imply the first). The countably infinite wedge of circles is not first countable at its wedge point (Exercise 4 of this section, printed p. 438). The space of Example 1 is the union of the circles of radius $1/n$, a closed bounded subspace of $\RR^2$, hence compact (Theorem 27.3, printed p. 173); $Y$ is unbounded, since $(2n,0)\in Y$ for every $n$, so $Y$ is not compact. Neither space is homeomorphic to $Y$.

:::

:::

::: pf-step

For $N\ge1$, the retraction $r_N:Y\to Y_N=S_1\cup\cdots\cup S_N$ which is the identity on $Y_N$ and sends $S_n$ to $p$ for $n>N$ is continuous.

::: pf-proof

Let $V\subseteq Y_N$ be open and suppose $p\in V$; the case $p\notin V$ is immediate because then $V$ is far from all but finitely many circles and meets each $S_n$ in an open set. As $V$ is a neighbourhood of $p$ in $Y_N$, there is $\delta>0$ with $B_\delta(p)\cap Y_N\subseteq V$. Then

$$
r_N^{-1}(V)\cap B_\delta(p)=B_\delta(p)\cap Y,
$$

because every point of $Y$ within $\delta$ of $p$ either lies in $Y_N$ (then in $V$) or in some $S_n$ with $n>N$ (then maps to $p\in V$). So $r_N^{-1}(V)$ contains a ball about each of its points, hence is open in $Y$.

:::

:::

::: pf-step

The map $\pi_1(Y_N,p)\to\pi_1(Y,p)$ induced by inclusion is one-to-one.

::: pf-proof

$r_N$ restricts to the identity on $Y_N$, so $(r_N)_*\circ(i_N)_*=\mathrm{id}$ on $\pi_1(Y_N,p)$; a homomorphism with a left inverse is injective. By Theorem 71.1 (printed p. 434), $\pi_1(Y_N,p)$ is free on $[f_1],\dots,[f_N]$.

:::

:::

::: pf-step

The classes $[f_n]$ generate $\pi_1(Y,p)$.

::: pf-proof

Let $g:I\to Y$ be a loop at $p$ and let $Z=g(I)$, a compact hence bounded subspace of $\RR^2$; fix $R$ with $\norm{z}\le R$ for $z\in Z$. Put $K=g^{-1}(p)$, closed in $I$ and containing $0,1$. On each component interval $(a,b)$ of $I\setminus K$ the image $g((a,b))$ is connected and misses $p$; the sets $S_n\setminus\theset{p}$ are the components of $Y\setminus\theset{p}$ (each is open in $Y\setminus\theset{p}$: a point $z\in S_n\setminus\theset{p}$ has $\operatorname{Re}z>0$, and every $S_m$ with $m\ne n$ stays a positive distance from $z$). So $g$ maps $(a,b)$ into a single $S_n\setminus\theset{p}$, and by continuity $g$ maps $[a,b]$ into $S_n$ with $g(a)=g(b)=p$; that excursion is a loop in $S_n$, of degree $e$ say, and its class is $[f_n]^{e}$. If $e\neq0$ the loop is surjective onto $S_n$, so $Z\supseteq S_n$ and $2n\le R$; only finitely many $n$ satisfy that. Excursions of degree $0$ are nullhomotopic in their own circle. Hence, up to nullhomotopic excursions, $g$ is the finite concatenation of the non-null excursions, and $[g]$ is a finite product of powers of the classes $[f_n]$.

:::

:::

::: pf-qed

By steps 2--3 the classes $\theset{[f_n]}$ are free generators of the subgroup they generate, and by step 4 they generate $\pi_1(Y,p)$; so $\pi_1(Y,p)$ is free with $\theset{[f_n]}$ as a system of free generators.

:::

:::
:::
