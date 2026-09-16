---
schema: qual/card@1
id: E-HAT-3.2-2
kind: problem
title: Cup products vanish on unions of contractible open sets
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

# E-HAT-3.2-2

Using the cup product $H^k(X, A; R) \times H^\ell(X, B; R) \to H^{k+\ell}(X, A \cup B; R)$, show that if $X$ is the union of contractible open subsets $A$ and $B$, then all cup products of positive-dimensional classes in $H^*(X; R)$ are zero.
This applies in particular if $X$ is a suspension.
Generalize to the situation that $X$ is the union of $n$ contractible open subsets, to show that all $n$-fold cup products of positive-dimensional classes are zero.

::: {.solution}
Suppose first that $X=A\cup B$ with $A,B$ contractible and let $x\in H^p(X;R)$, $y\in H^q(X;R)$ with $p,q>0$.

Since $H^p(A;R)=0$ for $p>0$, exactness of the cohomology sequence of $(X,A)$ gives a lift
\[
\bar x\in H^p(X,A;R)
\]
of $x$. Likewise $y$ lifts to some $\bar y\in H^q(X,B;R)$. The relative cup product gives
\[
\bar x\smile\bar y\in H^{p+q}(X,A\cup B;R)=H^{p+q}(X,X;R)=0.
\]
After forgetting relative structure this class maps to $x\smile y$, so $x\smile y=0$. In particular every product of positive-dimensional classes on a suspension vanishes, since a suspension is the union of its two contractible cones.

More generally suppose
\[
X=A_1\cup\cdots\cup A_n
\]
with all $A_i$ contractible, and let $x_i\in H^{d_i}(X;R)$ with $d_i>0$. Each $x_i$ lifts to
\[
\bar x_i\in H^{d_i}(X,A_i;R).
\]
Iterating the relative cup product gives
\[
\bar x_1\smile\cdots\smile\bar x_n
\in H^{d_1+\cdots+d_n}(X,A_1\cup\cdots\cup A_n;R)
=H^*(X,X;R)=0.
\]
Its image in absolute cohomology is $x_1\smile\cdots\smile x_n$, hence every $n$-fold product of positive-dimensional classes is zero.
:::
