---
schema: qual/card@1
id: E-VYYH3
kind: problem
title: Finitely presented groups as fundamental groups of compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem.
If $G$ is a finitely presented group, then there is a compact Hausdorff space $X$ whose fundamental group is isomorphic to $G$.

Proof.
Suppose $G$ has a presentation consisting of $n$ generators and $m$ relations.
Let $A$ be the wedge of $n$ circles; form an adjunction space $X$ from the union of $A$ and $m$ copies $B_1, \ldots, B_m$ of the unit ball by means of a continuous map $f: \bigcup \operatorname{Bd} B_i \to A$.

(a) Show that $X$ is Hausdorff.

(b) Prove the theorem in the case $m = 1$.

(c) Proceed by induction on $m$, using the algebraic result stated in the following exercise.

The construction outlined in this exercise is a standard one in algebraic topology; the space $X$ is called a two-dimensional CW complex.
:::

::: {.solution}
Let
\[
G=\langle a_1,\dots,a_n\mid r_1,\dots,r_m\rangle.
\]
Let \(A=\bigvee_{j=1}^nS^1_j\), and for each relator \(r_i\) choose a loop
\[
f_i:\partial B_i=S^1\to A
\]
representing the corresponding element of \(\pi_1(A)\cong F(a_1,\dots,a_n)\). Let \(X\) be the adjunction space obtained by attaching the disks \(B_i\) along the maps \(f_i\).

(a) Put
\[
Z=A\sqcup B_1\sqcup\cdots\sqcup B_m.
\]
This is compact Hausdorff. The quotient equivalence relation \(R\subset Z\times Z\) consists of the diagonal, the pairs \((x,f_i(x))\) and \((f_i(x),x)\) for \(x\in\partial B_i\), and pairs \((x,y)\in\partial B_i\times\partial B_j\) with \(f_i(x)=f_j(y)\). Each of these pieces is closed: the boundaries are compact, the graphs of the continuous attaching maps are compact, and the equalizer condition is closed because \(A\) is Hausdorff. Since there are only finitely many disks, \(R\) is closed.

A quotient of a compact Hausdorff space by a closed equivalence relation is Hausdorff. Hence \(X=Z/R\) is compact Hausdorff.

(b) Suppose \(m=1\). Attaching one 2-cell along \(f_1\) kills exactly the normal closure of the element represented by \(f_1\). Thus the adjoining-a-two-cell theorem gives
\[
\pi_1(X)\cong \pi_1(A)/\langle\!\langle r_1\rangle\!\rangle
\cong F(a_1,\dots,a_n)/\langle\!\langle r_1\rangle\!\rangle.
\]
This is the group with the stated one-relator presentation.

(c) Attach the disks one at a time. Let \(X_0=A\) and
\[
X_k=X_{k-1}\cup_{f_k}B_k.
\]
Inductively,
\[
\pi_1(X_k)
\cong
F(a_1,\dots,a_n)/\langle\!\langle r_1,\dots,r_k\rangle\!\rangle.
\]
Indeed, adjoining the \(k\)-th disk quotients \(\pi_1(X_{k-1})\) by the normal closure of the image of \(r_k\); algebraically this is the same as quotienting the original free group by the normal closure of all \(r_1,\dots,r_k\). Therefore
\[
\pi_1(X)=\pi_1(X_m)\cong G.
\]
Together with part (a), this proves that every finitely presented group is the fundamental group of a compact Hausdorff space.
:::
