---
schema: qual/card@1
id: E-G5JJ7
kind: problem
title: Strong form of the Urysohn lemma
classification:
  areas:
  - topology
  topics:
  - Urysohn Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S33.pdf, Exercise 33.5 (Theorem 3), page 2 of the file
    (tmp/sources/munkres-solutions-poulsen-S33.pdf, Internet Archive snapshot 20200331153844),
    checked against Munkres, Topology (2000), Section 33 Exercise 5, printed p. 213, and Exercise
    33.4. Moller proves both directions: the forward one by applying Exercise 33.4 to A and f and to
    B and 1 - f, the converse by taking f = g/(g+h) from the two functions vanishing precisely on A
    and B. The card's proof is that argument with the weighted series written out. No correction to
    the mathematics was needed.
---

::: {.exercise}

Prove the following.

Theorem (Strong form of the Urysohn lemma).
Let $X$ be a normal space.
There is a continuous function $f: X \to [0, 1]$ such that $f(x) = 0$ for $x \in A$, and $f(x) = 1$ for $x \in B$, and $0 < f(x) < 1$ otherwise, if and only if $A$ and $B$ are disjoint closed $G_\delta$ sets in $X$.
:::

::: {.solution}

No retained solution set covers this exercise: it is the book's exercise and no sheet in `tmp/sources` treats §33 Exercise 5, so the argument below is the card's own. The construction by which the converse is usually stated — a function vanishing precisely on a closed $G_{\delta}$ set, which the book sets as Exercise 4 on the same page — is not quoted; the sum $\sum_{n}a_{n}$ below proves that step instead, so the argument depends only on Urysohn's lemma. The statement was checked against Munkres, *Topology* (2000), §33 Exercise 5, printed p. 213, with the reminder of what a $G_{\delta}$ set is on the same page, Urysohn's lemma, Theorem 33.1, on printed p. 207, Theorem 21.5 on printed p. 131, the uniform limit theorem, Theorem 21.6, on printed p. 132, and Theorem 18.1(3) on printed p. 107.

Throughout, $X$ is a normal space, and a $G_{\delta}$ set in $X$ is one that is the intersection of a countable collection of open sets of $X$ (§33, printed p. 213).

::: pf

::: {.pf-step #closed}
If $f\colon X\to[0,1]$ is continuous with $f=0$ on $A$ and $f=1$ on $B$ and $0<f<1$ off $A\cup B$, then $A$ and $B$ are closed and disjoint.

::: pf-proof
$A=f^{-1}(\theset{0})$ and $B=f^{-1}(\theset{1})$: a point of $A$ has $f=0$, a point with $f=0$ lies in $A$ because $f>0$ off $A$, and likewise for $B$. The sets $\theset{0}$ and $\theset{1}$ are closed in $[0,1]$, so by the closed set formulation of continuity, Theorem 18.1(3) (printed p. 107), $A$ and $B$ are closed in $X$. They are disjoint because no point has $f$ equal to $0$ and to $1$.
:::

:::

::: {.pf-step #gdelta}
Under the same hypotheses, $A$ and $B$ are $G_{\delta}$ sets.

::: pf-proof
$A=\bigcap_{n\geq1}f^{-1}\big([0,1/n)\big)$: a point of $A$ has $f=0<1/n$ for every $n$, and a point with $f(x)<1/n$ for every $n$ has $f(x)=0$. Each $f^{-1}([0,1/n))$ is open in $X$ because $[0,1/n)$ is open in $[0,1]$ and $f$ is continuous, so $A$ is a countable intersection of open sets. The same computation with $B=\bigcap_{n\geq1}f^{-1}\big((1-1/n,1]\big)$ and the open sets $(1-1/n,1]$ of $[0,1]$ gives the claim for $B$.
:::

:::

::: {.pf-step #pieces}
Let $A=\bigcap_{n}U_{n}$ and $B=\bigcap_{n}V_{n}$ with all $U_{n},V_{n}$ open. For each $n$ there is a continuous $a_{n}\colon X\to[0,2^{-n}]$ that vanishes on $A$ and equals $2^{-n}$ on $X-U_{n}$.

::: pf-proof
$A\subset U_{n}$ because $A$ is the intersection of the $U_{n}$, so $A$ and $X-U_{n}$ are disjoint; both are closed, $A$ by hypothesis and $X-U_{n}$ because $U_{n}$ is open. Urysohn's lemma (Theorem 33.1, printed p. 207) applied to this pair gives a continuous $g_{n}\colon X\to[0,1]$ with $g_{n}=0$ on $A$ and $g_{n}=1$ on $X-U_{n}$; multiplying by the constant $2^{-n}$ gives $a_{n}$.
:::

:::

::: {.pf-step #a-constructed}
$a\coloneqq\sum_{n\geq1}a_{n}$ is a continuous function $X\to[0,1]$ with $a^{-1}(0)=A$.

:::: pf-proof

::: {.pf-step #a-continuous}
The partial sums converge uniformly to a continuous function $a$ with values in $[0,1]$.

::: pf-proof
Each $a_{n}$ is continuous and $0\leq a_{n}\leq2^{-n}$, so for $N<M$ the supremum of $\abs{\sum_{n=N+1}^{M}a_{n}}$ is at most $\sum_{n>N}2^{-n}=2^{-N}$, which tends to $0$; the sequence of partial sums is thus uniformly Cauchy, hence uniformly convergent (the metric space $\RR$ is complete). A uniform limit of continuous functions is continuous by the uniform limit theorem, Theorem 21.6 (printed p. 132), and $0\leq a\leq\sum_{n}2^{-n}=1$.
:::

:::

::: {.pf-step #a-zero-set}
$a^{-1}(0)=A$.

::: pf-proof
A point of $A$ lies in the zero set of every $a_{n}$, so $a$ vanishes there. If $x\notin A$ then $x\notin U_{n}$ for some $n$, because $A=\bigcap_{n}U_{n}$, and then $a_{n}(x)=2^{-n}>0$, so $a(x)\geq2^{-n}>0$.
:::

:::

::::

:::

::: {.pf-step #b-constructed}
Running the same construction with $B$ and the open sets $V_{n}$ in place of $A$ and the $U_{n}$ gives a continuous $b\colon X\to[0,1]$ with $b^{-1}(0)=B$.

::: pf-proof
The hypotheses used in steps [](#pieces){.pf-ref} and [](#a-constructed){.pf-ref} were only that $B$ is closed and that $B=\bigcap_{n}V_{n}$ with $V_{n}$ open, both of which hold by step [](#closed){.pf-ref} and the choice of the $V_{n}$.
:::

:::

::: {.pf-step #denominator}
$a+b>0$ at every point of $X$.

::: pf-proof
$a(x)\geq0$ and $b(x)\geq0$ everywhere. If $a(x)+b(x)=0$ then $a(x)=0$ and $b(x)=0$, so $x\in A$ and $x\in B$ by steps [](#a-constructed){.pf-ref} and [](#b-constructed){.pf-ref}, contradicting the disjointness of $A$ and $B$.
:::

:::

::: pf-step
Therefore the required function is
$$
\boxed{f\coloneqq\frac{a}{a+b}},
$$
which is continuous $X\to[0,1]$ with $f^{-1}(0)=A$, $f^{-1}(1)=B$ and $0<f<1$ off $A\cup B$; together with steps [](#closed){.pf-ref} and [](#gdelta){.pf-ref} this proves the equivalence.

::: pf-proof
$a+b$ is continuous and never vanishes by step [](#denominator){.pf-ref}, so $f=a/(a+b)$ is continuous as a quotient of continuous functions with nonvanishing denominator (Theorem 21.5, printed p. 131); it takes values in $[0,1]$ because $0\leq a\leq a+b$. Now $f(x)=0$ exactly when $a(x)=0$, that is exactly on $A$, and $f(x)=1$ exactly when $a(x)=a(x)+b(x)$, that is exactly when $b(x)=0$, which is exactly on $B$. For $x$ in neither set both $a(x)$ and $b(x)$ are positive, so $0<a(x)<a(x)+b(x)$ and $0<f(x)<1$. The forward implication is steps [](#closed){.pf-ref} and [](#gdelta){.pf-ref}, so the equivalence is proved.
:::

:::

:::

:::
