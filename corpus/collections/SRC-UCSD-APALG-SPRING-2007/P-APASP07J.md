---
schema: qual/card@1
id: P-APASP07J
kind: problem
title: "Invariants of Z/3 acting on a two-dimensional vector space and Hilbert series"
classification:
  areas:
  - applied-algebra
  topics:
  - Commutative Algebra
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    Read against the UCSD Applied Algebra Qualifying Exam, Spring 2007, Problem 8,
    printed p. 2. Parts (a)--(c) match the printed statement.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    No retained solution set covers this examination. Structured the card's own proof:
    the weights on monomials, the invariant congruence, the three module generators,
    the Hilbert-series decomposition, the relation $B^3=AC$, the quotient-module proof
    that it generates every relation, and the elimination method for all relations.
    Checked the residue classes $0,1,2$ and the Hilbert-series identity.
---

::: {.problem}
Let $G = \ZZ/3$ act on a two-dimensional vector space as a diagonal matrix with diagonal entries being $\theta, \theta^{-1}$, where $\theta = e^{2\pi i/3}$.

(a) Find a system of generators for $k[x,y]^G$.

(b) Calculate the Hilbert series for $k[x,y]^G$.

(c) Find at least one relation among the generators in (a). Give a precise description how you would find all possible relations (you need not carry out the calculations).
:::

::: {.solution}

No retained solution set covers this examination; the argument below is the card's own.

::: pf

::: {.pf-step #monomial-weights}
After possibly interchanging $x$ and $y$, the generator $g$ of $G=\ZZ/3$ acts on the coordinate functions by
$$
g\cdot x=\theta x,\qquad g\cdot y=\theta^{-1}y,
$$
so $g\cdot(x^ay^b)=\theta^{a-b}x^ay^b$.

::: pf-proof
The given diagonal action on the vector space has eigenvalues $\theta,\theta^{-1}$; passing to the dual coordinates inverts the eigenvalues. Interchanging the two coordinates if necessary gives the displayed normalization. Multiplicativity of the action then gives the monomial weight.
:::
:::

::: {.pf-step #invariant-monomials}
A monomial $x^ay^b$ is invariant exactly when $a-b\equiv0\pmod3$.

::: pf-proof
The scalar $\theta^{a-b}$ equals $1$ exactly when $3\mid(a-b)$, since $\theta$ has order $3$.
:::
:::

::: {.pf-step #generators}
$k[x,y]^G=k[x^3,xy,y^3]$.

::: pf-proof
If $a\equiv b\equiv r\pmod3$ with $r\in\{0,1,2\}$, write $a=3q+r$ and $b=3s+r$. Then
$$
x^ay^b=(x^3)^q(y^3)^s(xy)^r,
$$
which lies in $k[x^3,xy,y^3]$. Conversely each of $x^3,xy,y^3$ is invariant by step [](#invariant-monomials){.pf-ref}, so the displayed subring lies in $k[x,y]^G$. This proves part (a).
:::
:::

::: {.pf-step #module-decomposition}
As a graded $k[x^3,y^3]$-module,
$$
k[x,y]^G=k[x^3,y^3]\oplus xy\,k[x^3,y^3]\oplus x^2y^2\,k[x^3,y^3].
$$

::: pf-proof
The three cases $r=0,1,2$ in the residue decomposition of step [](#generators){.pf-ref} give the three displayed summands. Their monomials have exponent pairs congruent to $(0,0),(1,1),(2,2)$ modulo $3$, so the summands are disjoint and the sum is direct.
:::
:::

::: {.pf-step #hilbert-series}
$$
H_{k[x,y]^G}(t)=\frac{1+t^2+t^4}{(1-t^3)^2}=\frac{1-t^6}{(1-t^2)(1-t^3)^2}.
$$

::: pf-proof
The algebra $k[x^3,y^3]$ has Hilbert series $1/(1-t^3)^2$. The generators of the two other summands in step [](#module-decomposition){.pf-ref} have degrees $2$ and $4$, so their contributions are $t^2/(1-t^3)^2$ and $t^4/(1-t^3)^2$. Summing gives the first expression; multiplying numerator and denominator by $1-t^2$ gives the second. This proves part (b).
:::
:::

::: {.pf-step #relation}
With $A=x^3$, $B=xy$ and $C=y^3$, the generators satisfy $B^3=AC$.

::: pf-proof
$(xy)^3=x^3y^3$, which is exactly $AC$.
:::
:::

::: {.pf-step #complete-relations}
The kernel of $\Phi:k[A,B,C]\to k[x,y]^G$, $A\mapsto x^3$, $B\mapsto xy$, $C\mapsto y^3$, is $(B^3-AC)$.

::: pf-proof
The relation of step [](#relation){.pf-ref} shows that $(B^3-AC)\subseteq\ker\Phi$. In the quotient $k[A,B,C]/(B^3-AC)$, every monomial is congruent to one with $B$-exponent $0,1,$ or $2$. Its image is a $k[x^3,y^3]$-linear combination of $1,xy,x^2y^2$. These three are linearly independent over $k[x^3,y^3]$, because their monomials have distinct exponent residue pairs modulo $3$. Hence the images of $1,B,B^2$ are independent and the displayed relation generates the whole kernel. This gives a precise description for part (c).
:::
:::

::: {.pf-step #elimination}
All relations can be found by eliminating $x,y$ from
$$
J=(A-x^3,\ B-xy,\ C-y^3)\subset k[x,y,A,B,C]
$$
with an elimination order in which $x,y$ are larger than $A,B,C$; then $J\cap k[A,B,C]=\ker\Phi$.

::: pf-proof
This is the elimination theorem: the polynomials in the elimination ideal are exactly the polynomial relations among the images $x^3,xy,y^3$. A Gröbner basis for $J$ in such an order therefore yields every relation in part (c), and the relation already found is the first one.
:::
:::

:::
:::
