---
schema: qual/card@1
id: P-APAF18H
kind: problem
title: Finite-dimensionality of $\CC[x,y]/I$ for a two-point variety
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
(a) Let $I\subseteq\CC[x,y]$ be an ideal such that $\mathrm{V}(I)=\{(0,0),(1,1)\}\subset\CC^2$.
Prove that the quotient ring $\CC[x,y]/I$ is a finite-dimensional $\CC$-vector space.

(b) Is the conclusion of (a) still true if we replace $\CC$ by $\RR$?
Justify your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #squarefree-vanishing-polynomials}
Over $\CC$, the polynomials
$$
f=x(x-1),\qquad g=y(y-1)
$$
vanish on $\mathrm V(I)$.

::: pf-proof
At each of the two points $(0,0)$ and $(1,1)$, both $x(x-1)$ and $y(y-1)$ vanish.
:::

:::

::: {.pf-step #powers-of-f-g-in-ideal}
There exist positive integers $a,b$ such that
$$
f^a\in I,
\qquad
g^b\in I.
$$

::: pf-proof
By Hilbert's Nullstellensatz,
$$
I(\mathrm V(I))=\sqrt I.
$$
By step [](#squarefree-vanishing-polynomials){.pf-ref}, $f,g\in I(\mathrm V(I))$, hence $f,g\in\sqrt I$. By the definition of the radical, some positive powers $f^a$ and $g^b$ lie in $I$.
:::

:::

::: pf-step
The quotient $\CC[x,y]/I$ is finite-dimensional over $\CC$.

::: pf-proof
The polynomial
$$
f^a=[x(x-1)]^a
$$
is monic of degree $2a$ in $x$, and
$$
g^b=[y(y-1)]^b
$$
is monic of degree $2b$ in $y$. By step [](#powers-of-f-g-in-ideal){.pf-ref} both lie in $I$.

Modulo $I$, the relation $f^a=0$ expresses $x^{2a}$ as a linear combination of lower powers of $x$, and repeatedly applying it reduces every polynomial to one having $x$-degree $<2a$. Likewise $g^b=0$ reduces the $y$-degree to $<2b$.
Therefore the finitely many residue classes
$$
\{x^iy^j+I:0\le i<2a,\ 0\le j<2b\}
$$
span $\CC[x,y]/I$. Hence
$$
\dim_{\CC}\CC[x,y]/I\le4ab<\infty.
$$
:::

:::

::: pf-step
The analogous statement over $\RR$ is false.

::: pf-proof
Let
$$
F=(x^2+y^2)\bigl((x-1)^2+(y-1)^2\bigr)
\in\RR[x,y]
$$
and set
$$
J=(F).
$$
For a real point $(x,y)$, one has $F(x,y)=0$ if and only if at least one factor is zero. Since each factor is a sum of two squares,
$$
x^2+y^2=0\iff(x,y)=(0,0),
$$
and
$$
(x-1)^2+(y-1)^2=0\iff(x,y)=(1,1).
$$
Thus
$$
\mathrm V_{\RR}(J)=\{(0,0),(1,1)\}.
$$

However, the natural map
$$
\RR[x]\longrightarrow\RR[x,y]/(F)
$$
is injective. Indeed, if a nonzero $q(x)\in\RR[x]$ lay in $(F)$, then
$$
q(x)=F(x,y)h(x,y)
$$
for some nonzero $h\in\RR[x,y]$. But $F$ has positive degree in $y$, and since $\RR[x]$ is an integral domain, degree in $y$ is additive under multiplication:
$$
\deg_y(Fh)=\deg_yF+\deg_yh>0,
$$
contradicting $\deg_y q=0$.
Hence the classes of
$$
1,x,x^2,x^3,\ldots
$$
are linearly independent in $\RR[x,y]/J$, so this quotient is infinite-dimensional over $\RR$.
:::

:::

:::

:::
