---
schema: qual/card@1
id: E-MUH7R
kind: problem
title: Compact Hausdorff spaces are metrizable exactly when second countable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S34.pdf, Exercise 34.3 (Theorem 1), page 1 of the file
    (tmp/sources/munkres-solutions-poulsen-S34.pdf, Internet Archive snapshot 20180827202044), and
    "Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 34.3, printed p. 10
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 34 Exercise 3, printed p. 218, Theorem 32.3, Exercise 30.4 and Theorem 34.1. Its two
    directions are the card's: a second-countable compact Hausdorff space is regular, hence
    metrizable by Theorem 34.1; a compact metrizable space is second countable, and the card writes
    the finite 1/n-nets and the rational balls about their union. No correction to the mathematics
    was needed.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same two directions, with the gap in the converse closed:
    the earlier prose asserted that the balls of rational radius about a countable dense set "form a
    basis for the metric topology", which is the claim and not its proof. The card now verifies the
    criterion of Lemma 13.2 with an explicit triangle-inequality estimate --- given a ball B(x, eps)
    inside the neighbourhood, a point d of D within 1/(3m) of x, and m chosen with 1/m < eps --- and
    proves the countability of the family from Theorem 7.6 rather than assuming it. The forward
    direction now names Theorem 32.3 for normality and Theorem 17.8 for the closedness of one-point
    sets. Nothing else was changed; the statement was checked against Munkres, Topology (2000), Section
    34 Exercise 3, printed p. 218.
---

::: {.exercise}

Let $X$ be a compact Hausdorff space.
Show that $X$ is metrizable if and only if $X$ has a countable basis.
:::

::: {.solution}

The two directions are those of **Jesper Michael Moller, "Solutions to exercises in Munkres", file S34.pdf, Exercise 34.3 (Theorem 1), page 1 of the file** (`tmp/sources/munkres-solutions-poulsen-S34.pdf`) and of **"Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 34.3, printed p. 10** (`tmp/sources/munkres-solutions-dougsworld-ch4.pdf`); the finite $1/n$-nets and the rational balls about their union are theirs. One step is supplied: the earlier prose said the family of balls about points of $D$ "forms a basis for the metric topology" without an argument, and the card now verifies the criterion of Lemma 13.2 with the triangle inequality.

The statement was checked against Munkres, *Topology* (2000), §34 Exercise 3, printed p. 218, with the Urysohn metrization theorem (Theorem 34.1) on printed p. 215, Theorem 32.3 on printed p. 202, Lemma 13.2 on printed p. 80, Theorem 7.5 on printed p. 48 and Theorem 7.6 on printed p. 49. Throughout $X$ is a compact Hausdorff space, and *second countable* means having a countable basis (§30, printed p. 190).

::: pf

::: {.pf-step #forward}

If $X$ is second countable, then $X$ is metrizable.

::: pf-proof

A compact Hausdorff space is normal (Theorem 32.3, printed p. 202), and a normal space is regular, since one-point sets in a Hausdorff space are closed (Theorem 17.8, printed p. 99) and a point can be separated from a closed set by disjoint open sets. A regular space with a countable basis is metrizable (Theorem 34.1, the Urysohn metrization theorem, printed p. 215); so $X$ carries a metric whose open balls are the open sets of its topology.

:::

:::

::: {.pf-step #converse}

If $X$ is metrizable, then $X$ is second countable.

:::: pf-proof

Let $d$ be a metric inducing the topology of $X$, and write $B(x,r)$ for the open ball of radius $r$ about $x$.

::: {.pf-step #nets}

For each $n\in\ZZ_{+}$ there are finitely many points $x_{n,1},\dots,x_{n,k_{n}}$ of $X$ whose balls of radius $1/n$ cover $X$.

::: pf-proof

The family of all balls $B(x,1/n)$, $x\in X$, is an open cover of $X$, and $X$ is compact; so finitely many of them, say those about $x_{n,1},\dots,x_{n,k_{n}}$, cover $X$.

:::

:::

::: {.pf-step #dense}

The set $D\coloneqq\theset{x_{n,j}\mid n\in\ZZ_{+},\ 1\leq j\leq k_{n}}$ is countable and dense in $X$.

::: pf-proof

$D$ is a countable union of the finite sets $\theset{x_{n,1},\dots,x_{n,k_{n}}}$, hence countable (Theorem 7.5, printed p. 48). For density, let $x\in X$ and $\varepsilon>0$; choose $n$ with $1/n<\varepsilon$. The balls of radius $1/n$ about the points $x_{n,j}$ cover $X$ by step [](#nets){.pf-ref}, so $x\in B(x_{n,j},1/n)$ for some $j$, that is $d(x,x_{n,j})<1/n<\varepsilon$; hence $D$ meets every ball about $x$, and $D$ is dense.

:::

:::

::: {.pf-step #basis}

$\mathcal{B}$ is a countable basis for the topology of $X$.

:::: pf-proof

Let $\mathcal{B}$ be the family of balls of radius $1/m$, $m\in\ZZ_{+}$, about the points of $D$; countability and the basis criterion are settled below.

::: {.pf-step #countable-family}

$\mathcal{B}\coloneqq\theset{B(d,1/m)\mid d\in D,\ m\in\ZZ_{+}}$ is countable.

::: pf-proof

$D$ is countable by step [](#dense){.pf-ref} and $\ZZ_{+}$ is countable, so $D\times\ZZ_{+}$ is countable (Theorem 7.6, printed p. 49); the map $(d,m)\mapsto B(d,1/m)$ carries it onto $\mathcal{B}$, and a set that is the image of a countable set is countable.

:::

:::

::: {.pf-step #criterion}

For $x\in X$ and a neighbourhood $U$ of $x$ there is a member of $\mathcal{B}$ containing $x$ and contained in $U$.

::: pf-proof

Because $U$ is open in the metric topology and $x\in U$, there is $\varepsilon>0$ with $B(x,\varepsilon)\subset U$; choose $m\in\ZZ_{+}$ with $1/m<\varepsilon$. By step [](#dense){.pf-ref} the set $D$ is dense, so there is $d\in D$ with $d(x,d)<1/(3m)$. Then $x\in B(d,1/(3m))$, and $1/(3m)=1/m^{\prime}$ with $m^{\prime}=3m\in\ZZ_{+}$, so $B(d,1/(3m))\in\mathcal{B}$. Finally $B(d,1/(3m))\subset B(x,1/m)\subset B(x,\varepsilon)\subset U$: if $d(y,d)<1/(3m)$ then $d(x,y)\leq d(x,d)+d(d,y)<2/(3m)<1/m$ by the triangle inequality.

:::

:::

::: pf-step

$\mathcal{B}$ is a countable basis for the topology of $X$.

::: pf-proof

Lemma 13.2 (printed p. 80) says that a family $\mathcal{B}$ of open sets is a basis for a topology on $X$ when, for every $x\in X$ and every neighbourhood $U$ of $x$, some member of $\mathcal{B}$ contains $x$ and lies in $U$. Each member of $\mathcal{B}$ is an open ball, hence open, and step [](#criterion){.pf-ref} verifies the condition; so $\mathcal{B}$ is a basis, and it is countable by step [](#countable-family){.pf-ref}.

:::

:::

::::

:::

::::

:::

::: pf-step

Therefore a compact Hausdorff space is metrizable if and only if it is second countable.

::: pf-proof

Step [](#forward){.pf-ref} is the implication from a countable basis to metrizability and step [](#converse){.pf-ref} the converse, which produces from the metric a countable basis $\mathcal{B}$; a space with a countable basis is second countable by definition. Together they are the assertion of the exercise.

:::

:::

:::

:::
