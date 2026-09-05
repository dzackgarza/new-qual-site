---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-08
kind: problem
title: Fundamental group of two spheres with corresponding poles identified
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
  - Quotient Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section II, problem 3 of the 23 September 1995 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Chose compatible CW decompositions of the two spheres and applied the
    Seifert--van Kampen 2-cell attachment presentation. The four-edge
    1-skeleton has rank three and the two sphere relations leave one generator.
---

::: {.problem}
Let $X_1$ and $X_2$ be two copies of $S^2$ and let $N_1,S_1$ and $N_2,S_2$ be the north and south poles of $X_1$ and $X_2$, respectively.
Define $X$ to be the quotient space obtained by identifying $N_1$ with $N_2$ and $S_1$ with $S_2$.
Compute the fundamental group of $X$ by using the Seifert--van Kampen theorem.
:::

::: {.solution}
Let $N$ and $S$ denote the two points of $X$ obtained from the identified north and south poles.

<1>1. Give $X$ a CW decomposition with two vertices, four edges, and four $2$-cells.
::: {.proof}
For each sphere $X_i$, choose a great circle through $N_i$ and $S_i$.
Its two semicircles give two $1$-cells
\[
a_i,b_i:N\longrightarrow S.
\]
The two complementary open hemispheres are $2$-cells.
Thus the quotient $X$ has
\[
X^{(0)}=\{N,S\}
\]
and a $1$-skeleton $G=X^{(1)}$ consisting of four parallel edges
\[
a_1,b_1,a_2,b_2
\]
from $N$ to $S$.
For the sphere $X_i$, the boundary of either hemisphere traverses one semicircle from $N$ to $S$ and the other back from $S$ to $N$.
Hence its two $2$-cells are attached along the mutually inverse loops
\[
a_i b_i^{-1}
\quad\text{and}\quad
b_i a_i^{-1}.
\]
:::

<1>2. The fundamental group of the $1$-skeleton is free of rank three.
::: {.proof}
Choose the single edge $a_1$ as a maximal tree in $G$ and use $N$ as basepoint.
By the standard graph computation from Seifert--van Kampen,
\[
\pi_1(G,N)\cong F(x,y,z),
\]
where we may take
\[
x=[a_1b_1^{-1}],
\qquad
y=[a_1a_2^{-1}],
\qquad
z=[a_1b_2^{-1}].
\]
Indeed, each of the three edges outside the maximal tree gives one free generator.
:::

<1>3. Attaching the two hemispheres of $X_1$ imposes only the relation $x=1$.
::: {.proof}
The attaching loops for the two hemispheres of $X_1$ are
\[
a_1b_1^{-1}
\quad\text{and}\quad
b_1a_1^{-1}.
\]
These represent $x$ and $x^{-1}$.
The Seifert--van Kampen theorem for attaching a $2$-cell says that the resulting fundamental group is the previous group modulo the normal closure of the attaching loop.
Thus the two hemispheres together impose precisely
\[
x=1.
\]
:::

<1>4. Attaching the two hemispheres of $X_2$ imposes only the relation $y^{-1}z=1$.
::: {.proof}
The relevant attaching loop is
\[
a_2b_2^{-1}.
\]
Using the generators from <1>2,
\[
y^{-1}z
=(a_2a_1^{-1})(a_1b_2^{-1})
=a_2b_2^{-1}.
\]
Hence one hemisphere of $X_2$ imposes
\[
y^{-1}z=1.
\]
The other hemisphere is attached along the inverse loop and contributes no additional relation.
:::

<1>5. Therefore
\[
\pi_1(X,N)\cong\ZZ.
\]
::: {.proof}
By <1>2--<1>4 and Seifert--van Kampen,
\[
\pi_1(X,N)
\cong
\langle x,y,z\mid x,\ y^{-1}z\rangle.
\]
The first relation eliminates $x$, and the second identifies $z$ with $y$.
Thus
\[
\pi_1(X,N)
\cong
\langle y\mid\ \rangle
\cong\ZZ.
\]
Geometrically, a generator is represented by going from $N$ to $S$ along the arc $a_1$ in the first sphere and returning from $S$ to $N$ along $a_2$ in the second sphere.
Hence
\[
\boxed{\pi_1(X)\cong\ZZ}.
\]
:::
:::
