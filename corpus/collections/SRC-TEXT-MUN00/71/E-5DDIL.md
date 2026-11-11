---
schema: qual/card@1
id: E-5DDIL
kind: problem
title: The fundamental group of a wedge of arbitrary spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Free Products
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §71 Exercise 1 of the section's list, printed p. 438 (the book numbers it Exercise 1). Proof
    transcribed from Takumi Murayama, Selected Solutions to Munkres's Topology, 2nd Ed. (MAT365, Princeton,
    Fall 2012), §71 (printed there as Exercise 71.2, one more than the book's number), which takes
    U = X_1 cup W_2 and V = X_2 cup W_1 and applies Corollary 70.3, and which reduces first to the path
    component of p in each X_i. Two gaps are filled: Murayama does not check that U and V are open in X, which
    the card does through the closedness of X_i minus W_i in X; and the n-fold case is by induction on n with
    the two-fold result, which the card states. Checked against Theorem 70.1 (printed p. 426) and Corollary
    70.3 (printed p. 432).
---

::: {.exercise}

Suppose $X$ is a space that is the union of the closed subspaces $X_1, \ldots, X_n$; assume there is a point $p$ of $X$ such that $X_i \cap X_j = \theset{p}$ for $i \neq j$.
Then we call $X$ the wedge of the spaces $X_1, \ldots, X_n$, and write $X = X_1 \vee \cdots \vee X_n$.
Show that if for each $i$, the point $p$ is a deformation retract of an open set $W_i$ of $X_i$, then $\pi_1(X, p)$ is the external free product of the groups $\pi_1(X_i, p)$ relative to the monomorphisms induced by inclusion.
:::

::: {.solution}

Replacing $X_i$ by its path component containing $p$ does not change $\pi_1(X_i,p)$ (p. 332) and preserves every hypothesis, so assume each $X_i$ is path connected; then $W_i$, which deformation retracts to $p$, is path connected too.

::: pf

::: pf-step

The two-fold case.

::: pf-proof

Let $X=X_1\cup X_2$ with $X_1\cap X_2=\theset{p}$, and put $U=X_1\cup W_2$, $V=X_2\cup W_1$. Both are open in $X$: $X\setminus U=X_2\setminus W_2$ is closed in $X_2$ because $W_2$ is open in $X_2$, and a closed subset of the closed subspace $X_2$ is closed in $X$; symmetrically for $V$. Also $U\cup V=X$ and $U\cap V=(X_1\cap X_2)\cup W_1\cup W_2=W_1\cup W_2$, as $W_i\subseteq X_i$ and $p\in W_1\cap W_2$. Each of $U$, $V$, $U\cap V$ is path connected, being the union of path-connected spaces with the point $p$ in common. The deformation retraction of $W_2$ to $p$ extended by the identity on $X_1$ is a deformation retraction of $U$ onto $X_1$, so $\pi_1(U,p)\cong\pi_1(X_1,p)$ with the isomorphism induced by inclusion; symmetrically for $V$ and $X_2$. The deformation retractions of $W_1$ and $W_2$ to $p$ fit together, by the pasting lemma over the closed subspaces $W_i\times I$ of $(U\cap V)\times I$, to a deformation retraction of $U\cap V$ onto $p$, so $U\cap V$ is simply connected. Corollary 70.3 (printed p. 432) then gives $\pi_1(X,p)\cong\pi_1(U,p)*\pi_1(V,p)\cong\pi_1(X_1,p)*\pi_1(X_2,p)$, the monomorphisms being those induced by inclusion.

:::

:::

::: pf-step

The $n$-fold case, by induction on $n$.

::: pf-proof

For $n=1$ there is nothing to prove; $n=2$ is step 1. For $n\ge3$ put $Y=X_1\cup\cdots\cup X_{n-1}$, a closed subspace of $X$ with $Y\cap X_n=\theset{p}$, and note that $p$ is a deformation retract of the open subset $W_1\cup\cdots\cup W_{n-1}$ of $Y$: it is open in $Y$ because each $W_i$ is open in $X_i$ and the pieces meet only in $p$, and the retractions fit together as in step 1. Step 1 applied to $X=Y\vee X_n$ gives $\pi_1(X,p)\cong\pi_1(Y,p)*\pi_1(X_n,p)$, and the induction hypothesis identifies $\pi_1(Y,p)$ with $\pi_1(X_1,p)*\cdots*\pi_1(X_{n-1},p)$.

:::

:::

::: pf-qed

By steps 1 and 2, $\pi_1(X,p)$ is the external free product of the groups $\pi_1(X_i,p)$.

:::

:::
:::
