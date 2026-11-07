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
  - Cup Product
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 2; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: $H^p(A;R)=0$ for $p>0$ makes $H^p(X,A;R)\to H^p(X;R)$ surjective, so
    positive-dimensional classes lift to the relative groups, and the relative cup product lands in
    $H^{p+q}(X,A\cup B;R)=0$; forgetting the relative structure gives $x\smile y=0$. The $n$-fold
    statement is the same iteration with $A_1\cup\cdots\cup A_n=X$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 2 (p.229) including the suspension remark and the n-fold generalization. Rechecked: contractibility of A and B kills their positive cohomology, so positive-degree classes lift to the relative groups by exactness of the sequence of the pair (p.200), and the relative cup product of p.209 lands in H^*(X,X) = 0; forgetting the relative structure gives the absolute product. The n-fold case iterates the same pairing. Citations added for p.200 and p.209. Not covered: no statement about infinite unions, which the exercise does not ask.
---

::: {.problem}
Using the cup product $H^k(X, A; R) \times H^\ell(X, B; R) \to H^{k+\ell}(X, A \cup B; R)$, show that if $X$ is the union of contractible open subsets $A$ and $B$, then all cup products of positive-dimensional classes in $H^*(X; R)$ are zero.
This applies in particular if $X$ is a suspension.
Generalize to the situation that $X$ is the union of $n$ contractible open subsets, to show that all $n$-fold cup products of positive-dimensional classes are zero.
:::

::: {.solution}
Suppose first that $X=A\cup B$ with $A,B$ contractible and let $x\in H^p(X;R)$, $y\in H^q(X;R)$ with $p,q>0$.

Since $A$ is contractible, $H^p(A;R)=0$ for $p>0$, so exactness of the cohomology sequence of the pair $(X,A)$ (p.200) gives a lift
$$
\bar x\in H^p(X,A;R)
$$
of $x$. Likewise $y$ lifts to some $\bar y\in H^q(X,B;R)$. The relative cup product of p.209, valid for $A,B$ open as here, gives
$$
\bar x\smile\bar y\in H^{p+q}(X,A\cup B;R)=H^{p+q}(X,X;R)=0.
$$
After forgetting relative structure this class maps to $x\smile y$, so $x\smile y=0$. In particular every product of positive-dimensional classes on a suspension vanishes, since a suspension is the union of its two contractible cones.

More generally suppose
$$
X=A_1\cup\cdots\cup A_n
$$
with all $A_i$ contractible, and let $x_i\in H^{d_i}(X;R)$ with $d_i>0$. Each $x_i$ lifts to
$$
\bar x_i\in H^{d_i}(X,A_i;R).
$$
Iterating the relative cup product gives
$$
\bar x_1\smile\cdots\smile\bar x_n
\in H^{d_1+\cdots+d_n}(X,A_1\cup\cdots\cup A_n;R)
=H^*(X,X;R)=0.
$$
Its image in absolute cohomology is $x_1\smile\cdots\smile x_n$, hence every $n$-fold product of positive-dimensional classes is zero. Each step uses only the relative cup product of p.209 with the open sets $A_i$, iterated.
:::
