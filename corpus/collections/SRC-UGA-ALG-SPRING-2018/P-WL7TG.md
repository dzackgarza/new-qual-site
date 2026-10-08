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
---

::: {.problem}
Let 
\[
M=\left(\begin{array}{ll}{a} & {b} \\ {c} & {d}\end{array}\right)
\quad \text{and} \quad 
N=\left(\begin{array}{cc}{x} & {u} \\ {-y} & {-v}\end{array}\right)
\]

over a commutative ring $R$, where $b$ and $x$ are units of $R$. 
Prove that
\[
M N=\left(\begin{array}{ll}{0} & {0} \\ {0} & {*}\end{array}\right)
\implies MN = 0
.\]
:::

::: {.solution}
<1>1. The first three entries of $MN$ vanish precisely when
\[
ax=by,\qquad au=bv,\qquad cx=dy.
\]

::: {.proof}
Matrix multiplication gives
\[
MN=\begin{pmatrix}ax-by&au-bv\\cx-dy&cu-dv\end{pmatrix}.
\]
Thus the specified vanishing is equivalent to the displayed equations.
:::

<1>2. The fourth entry also vanishes: $cu=dv$.

::: {.proof}
Because $b$ and $x$ are units and $R$ is commutative, the first equation of step <1>1 gives $y=b^{-1}ax$. Substituting into the third yields
\[
cx=dy=db^{-1}ax.
\]
Multiplying by $x^{-1}$ gives $c=db^{-1}a$. The second equation of step <1>1 gives $v=b^{-1}au$. Consequently
\[
cu=db^{-1}au=dv.
\]
:::

<1>3. The conclusion is
\[
\boxed{MN=0}.
\]

::: {.proof}
The first three matrix entries vanish by hypothesis, and the final entry vanishes by step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the requested implication.
:::

:::
