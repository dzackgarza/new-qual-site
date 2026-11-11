---
schema: qual/card@1
id: E-AGJM5
kind: problem
title: Homotopic maps into a euclidean open set and their extensions
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §62 Exercise 3, printed p. 384, which is Lemma 62.1 (the homotopy extension lemma, printed p. 381)
    with "nullhomotopic" replaced by "homotopic to a map that extends": take the codomain Y, the closed
    subspace A of X, and apply the lemma to X x I, A x I and the map F defined below. The card's earlier proof
    had the right construction but buried the steps in nested headings, some of them empty, and it asserted
    that Urysohn's lemma may be applied to X without noting that X is normal as a closed subspace of the normal
    space X x I; both are repaired. Checked against Lemma 62.1 (printed p. 381), Theorem 33.1 (Urysohn's lemma,
    printed p. 207), Theorem 32.3 and Lemma 26.8 (the tube lemma, printed pp. 202, 167).
---

::: {.exercise}

Let $X$ be a space such that $X \times I$ is normal.
Let $A$ be a closed subspace of $X$; let $f: A \to Y$ be a continuous map, where $Y$ is an open subspace of $\RR^n$.
If $f$ is homotopic to a map that is extendable to a continuous map $h: X \to Y$, then $f$ itself is extendable to a continuous map $g: X \to Y$, such that $g \simeq h$.
:::

::: {.solution}

Let $H:A\times I\to Y$ be a homotopy from $f$ to $h|_A$: $H(a,0)=f(a)$ and $H(a,1)=h(a)$.

::: pf

::: pf-step

The map $F:T\to Y$ on the closed subspace $T=(X\times\theset{1})\cup(A\times I)$ of $X\times I$, given by $F(x,1)=h(x)$ and $F(a,t)=H(a,t)$, is well defined and continuous.

::: pf-proof

On the intersection $A\times\theset{1}$ the two formulas agree, $h(a)=H(a,1)$. The sets $X\times\theset{1}$ and $A\times I$ are closed in $X\times I$ because $A$ is closed in $X$, and $F$ is continuous on each, so the pasting lemma applies.

:::

:::

::: pf-step

$F$ extends to a continuous $\widetilde F:X\times I\to\RR^n$.

::: pf-proof

$X$ is homeomorphic to the closed subspace $X\times\theset{0}$ of the normal space $X\times I$, so $X$ is normal; $T$ is closed in $X\times I$. By the Tietze extension theorem, Theorem 35.1 (printed p. 219), applied to the $n$ coordinate functions, each a continuous real-valued function on $T$, there is a continuous extension $\widetilde F$ to $X\times I$.

:::

:::

::: pf-step

$U=\widetilde F^{-1}(Y)$ is an open subset of $X\times I$ containing $T$, and therefore contains a set of the form $\theset{(x,t):t\ge\mu(x)}$ for a continuous $\mu:X\to[0,1]$ with $\mu=0$ on $A$.

::: pf-proof

$U$ is open since $Y$ is open and $\widetilde F$ is continuous, and $T\subseteq U$ since $\widetilde F|_T=F$ takes values in $Y$. As $A\times I\subseteq U$ and $I$ is compact, the tube lemma (Lemma 26.8, printed p. 167) gives an open neighbourhood $W$ of $A$ in $X$ with $W\times I\subseteq U$. The sets $A$ and $X\setminus W$ are disjoint closed sets in the normal space $X$, so Urysohn's lemma (Theorem 33.1, printed p. 207) gives a continuous $\mu:X\to[0,1]$ equal to $0$ on $A$ and to $1$ on $X\setminus W$. If $x\in W$ then all $(x,t)\in U$; if $x\notin W$ then $\mu(x)=1$ and $(x,1)\in X\times\theset{1}\subseteq U$. Hence $(x,t)\in U$ whenever $t\ge\mu(x)$.

:::

:::

::: pf-step

$K:X\times I\to Y$, $K(x,t)=\widetilde F(x,(1-t)\mu(x)+t)$, is continuous with values in $Y$; putting $g(x)=K(x,0)$ gives an extension of $f$ with $g\simeq h$.

::: pf-proof

$(1-t)\mu(x)+t\ge\mu(x)$ for $t\in[0,1]$ and $\mu(x)\in[0,1]$, so by step 3 the second argument is the affine interpolation between $\mu(x)$ and $1$, and $K$ takes values in $Y$. Continuity is that of $\widetilde F$ composed with a continuous map. For $a\in A$, $\mu(a)=0$, so $K(a,t)=\widetilde F(a,t)=H(a,t)$, in particular $K(a,0)=f(a)=g(a)$ and $K(a,1)=h(a)$. For any $x\in X$, $K(x,1)=\widetilde F(x,1)=h(x)$. So $g$ extends $f$ and $K$ is a homotopy from $g$ to $h$, both with values in $Y$.

:::

:::

::: pf-qed

$f$ extends to $g:X\to Y$ with $g\simeq h$.

:::

:::
:::
