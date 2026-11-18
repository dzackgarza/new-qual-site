---
schema: qual/card@1
id: P-WL7TG
kind: problem
title: If $b$ and $x$ are units, a $2\times 2$ product over a commutative ring that
  vanishes off the bottom-right corner is zero
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Rings
  - Determinants
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The card's solution was a hand-numbered nested list (which the parser reads as prose, hence its presence in this queue); the mathematics is unchanged and correct: the matrix product is now written out so that the hypothesis is exactly the three equations ax = by, au = bv, cx = dy, and cu = dv is derived in two steps from the invertibility of b and x, each use of a unit named. The two summary chains in the original list are replaced by the two short implications that actually do the work. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Let
$$
M=\left(\begin{array}{ll}{a} & {b} \\ {c} & {d}\end{array}\right)
\quad \text{and} \quad
N=\left(\begin{array}{cc}{x} & {u} \\ {-y} & {-v}\end{array}\right)
$$

over a commutative ring $R$, where $b$ and $x$ are units of $R$.
Prove that
$$
M N=\left(\begin{array}{ll}{0} & {0} \\ {0} & {*}\end{array}\right)
\implies MN = 0
.$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #entries}
$MN=\begin{pmatrix}ax-by & au-bv\\ cx-dy & cu-dv\end{pmatrix}$, so the hypothesis is the system
$$
ax=by,\qquad au=bv,\qquad cx=dy .
$$

::: pf-proof
Multiplying the matrices,
$$
MN=\begin{pmatrix}a&b\\ c&d\end{pmatrix}\begin{pmatrix}x&u\\ -y&-v\end{pmatrix}
=\begin{pmatrix}ax+b(-y)&au+b(-v)\\ cx+d(-y)&cu+d(-v)\end{pmatrix},
$$
and the hypothesis says the $(1,1)$, $(1,2)$ and $(2,1)$ entries vanish. The $(2,2)$ entry $cu-dv$ is unconstrained, so $MN=0$ is exactly the assertion $cu=dv$.
:::

:::

::: {.pf-step #c}
$c=d\inverseof{b}a$.

::: pf-proof
Since $b$ is a unit, left-multiply $ax=by$ by $\inverseof b$ to get $y=\inverseof b\,ax$. Substituting into $cx=dy$ gives $cx=d\inverseof b\,ax$. Since $x$ is a unit, right-multiply by $\inverseof x$: $c=d\inverseof b\,a$.
:::

:::

::: {.pf-step #v}
$v=\inverseof b\,au$.

::: pf-proof
Left-multiply $au=bv$ by $\inverseof b$.
:::

:::

::: {.pf-step #conclusion}
$cu=dv$, hence $MN=0$.

::: pf-proof
By steps [](#c){.pf-ref} and [](#v){.pf-ref},
$$
cu=\left(d\inverseof b\,a\right)u=d\inverseof b\,au=dv .
$$
With step [](#entries){.pf-ref} the matrix $MN$ has all four entries zero.
:::

:::

:::
:::
