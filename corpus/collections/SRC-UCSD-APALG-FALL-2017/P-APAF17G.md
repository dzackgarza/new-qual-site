---
schema: qual/card@1
id: P-APAF17G
kind: problem
title: Finite-dimensionality of $\mathbb{C}[x,y]/I$ when $\mathbf{V}(I)$ is a point
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $I\subseteq\mathbb{C}[x,y]$ be an ideal with vanishing locus
\[
\mathbf{V}(I)=\{(2,3)\}\subset\mathbb{C}^2.
\]

(a) Prove that the quotient $\mathbb{C}[x,y]/I$ is finite-dimensional as a $\mathbb{C}$-vector space.

(b) Is the result of the last part still true if we replace $\mathbb{C}$ by $\mathbb{R}$?
:::

::: {.solution}
Let
\[
R=\mathbb C[x,y],
\qquad
\mathfrak m=(x-2,y-3).
\]

<1>1. One has
\[
\sqrt I=\mathfrak m.
\]
::: {.proof}
By Hilbert's Nullstellensatz,
\[
\sqrt I=I(\mathbf V(I)).
\]
Since
\[
\mathbf V(I)=\{(2,3)\},
\]
the ideal of the variety is exactly
\[
I(\{(2,3)\})=(x-2,y-3)=\mathfrak m.
\]
:::

<1>2. There exists $N\ge1$ such that
\[
\mathfrak m^N\subseteq I.
\]
::: {.proof}
Since $x-2,y-3\in\sqrt I$, there exist integers $a,b\ge1$ such that
\[
(x-2)^a\in I,
\qquad
(y-3)^b\in I.
\]
Take
\[
N=a+b-1.
\]
Every monomial
\[
(x-2)^i(y-3)^j
\]
of total degree $i+j=N$ has either $i\ge a$ or $j\ge b$; otherwise
\[
i+j\le(a-1)+(b-1)=N-1,
\]
a contradiction. Hence every degree-$N$ monomial in the generators of $\mathfrak m$ lies in $I$, so
\[
\mathfrak m^N\subseteq I.
\]
:::

<1>3. The quotient $R/I$ is finite-dimensional over $\mathbb C$.
::: {.proof}
By <1>2 there is a surjection
\[
R/\mathfrak m^N\twoheadrightarrow R/I.
\]
Writing
\[
u=x-2,
\qquad
v=y-3,
\]
the quotient $R/\mathfrak m^N$ is spanned by the finitely many residue classes
\[
u^iv^j,
\qquad i+j<N.
\]
Therefore $R/\mathfrak m^N$ is finite-dimensional, and so is its quotient $R/I$. This proves part (a).
:::

<1>4. The analogous statement over $\mathbb R$ is false.
::: {.proof}
Take
\[
J=\bigl((x-2)^2+(y-3)^2\bigr)\subseteq\mathbb R[x,y].
\]
Over $\mathbb R$,
\[
\mathbf V_{\mathbb R}(J)=\{(2,3)\},
\]
because a sum of two real squares is zero exactly when both squares are zero.

However,
\[
\mathbb R[x,y]/J
\]
is infinite-dimensional over $\mathbb R$. Indeed, the classes of
\[
1,(x-2),(x-2)^2,(x-2)^3,\ldots
\]
are linearly independent. If a nonzero polynomial $p(x-2)\in\mathbb R[x-2]$ lay in $J$, we would have
\[
p(x-2)=q(x,y)\bigl((x-2)^2+(y-3)^2\bigr).
\]
Viewing both sides as polynomials in $y-3$ over the domain $\mathbb R[x-2]$, the left side has degree $0$ in $y-3$, while the right side has degree at least $2$ whenever $q\ne0$, impossible. Thus
\[
J\cap\mathbb R[x-2]=0,
\]
which proves the asserted linear independence. Hence the real analogue fails. This proves part (b).
:::
:::
