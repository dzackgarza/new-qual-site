---
schema: qual/card@1
id: P-APAF18H
kind: problem
title: Finite-dimensionality of $\mathbb{C}[x,y]/I$ for a two-point variety
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

::: {.problem}
(a) Let $I\subseteq\mathbb{C}[x,y]$ be an ideal such that $\mathrm{V}(I)=\{(0,0),(1,1)\}\subset\mathbb{C}^2$.
Prove that the quotient ring $\mathbb{C}[x,y]/I$ is a finite-dimensional $\mathbb{C}$-vector space.

(b) Is the conclusion of (a) still true if we replace $\mathbb{C}$ by $\mathbb{R}$?
Justify your answer.
:::

::: {.solution}
<1>1. Over $\mathbb C$, the polynomials
\[
f=x(x-1),\qquad g=y(y-1)
\]
vanish on $\mathrm V(I)$.
::: {.proof}
At each of the two points $(0,0)$ and $(1,1)$, both $x(x-1)$ and $y(y-1)$ vanish.
:::

<1>2. There exist positive integers $a,b$ such that
\[
f^a\in I,
\qquad
g^b\in I.
\]
::: {.proof}
By Hilbert's Nullstellensatz,
\[
I(\mathrm V(I))=\sqrt I.
\]
By <1>1, $f,g\in I(\mathrm V(I))$, hence $f,g\in\sqrt I$. By the definition of the radical, some positive powers $f^a$ and $g^b$ lie in $I$.
:::

<1>3. The quotient $\mathbb C[x,y]/I$ is finite-dimensional over $\mathbb C$.
::: {.proof}
The polynomial
\[
f^a=[x(x-1)]^a
\]
is monic of degree $2a$ in $x$, and
\[
g^b=[y(y-1)]^b
\]
is monic of degree $2b$ in $y$. By <1>2 both lie in $I$.

Modulo $I$, the relation $f^a=0$ expresses $x^{2a}$ as a linear combination of lower powers of $x$, and repeatedly applying it reduces every polynomial to one having $x$-degree $<2a$. Likewise $g^b=0$ reduces the $y$-degree to $<2b$.
Therefore the finitely many residue classes
\[
\{x^iy^j+I:0\le i<2a,\ 0\le j<2b\}
\]
span $\mathbb C[x,y]/I$. Hence
\[
\dim_{\mathbb C}\mathbb C[x,y]/I\le4ab<\infty.
\]
:::

<1>4. The analogous statement over $\mathbb R$ is false.
::: {.proof}
Let
\[
F=(x^2+y^2)\bigl((x-1)^2+(y-1)^2\bigr)
\in\mathbb R[x,y]
\]
and set
\[
J=(F).
\]
For a real point $(x,y)$, one has $F(x,y)=0$ if and only if at least one factor is zero. Since each factor is a sum of two squares,
\[
x^2+y^2=0\iff(x,y)=(0,0),
\]
and
\[
(x-1)^2+(y-1)^2=0\iff(x,y)=(1,1).
\]
Thus
\[
\mathrm V_{\mathbb R}(J)=\{(0,0),(1,1)\}.
\]

However, the natural map
\[
\mathbb R[x]\longrightarrow\mathbb R[x,y]/(F)
\]
is injective. Indeed, if a nonzero $q(x)\in\mathbb R[x]$ lay in $(F)$, then
\[
q(x)=F(x,y)h(x,y)
\]
for some nonzero $h\in\mathbb R[x,y]$. But $F$ has positive degree in $y$, and since $\mathbb R[x]$ is an integral domain, degree in $y$ is additive under multiplication:
\[
\deg_y(Fh)=\deg_yF+\deg_yh>0,
\]
contradicting $\deg_y q=0$.
Hence the classes of
\[
1,x,x^2,x^3,\ldots
\]
are linearly independent in $\mathbb R[x,y]/J$, so this quotient is infinite-dimensional over $\mathbb R$.
:::
:::
