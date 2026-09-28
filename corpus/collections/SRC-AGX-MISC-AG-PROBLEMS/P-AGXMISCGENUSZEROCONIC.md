---
schema: qual/card@1
id: P-AGXMISCGENUSZEROCONIC
kind: problem
title: Every genus zero smooth projective curve over $\CC$ is a plane conic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann--Roch
  - Rational Curves
  - Conics
relations: []
review: draft
---

::: {.problem}
Is every smooth projective curve of genus 0 defined over the field of complex numbers isomorphic to a conic in the projective plane?
Give an explanation for your answer.
:::

::: {.solution}
Let $C$ be a smooth projective curve of genus $0$ over $\CC$ and fix $p\in C$.

<1>1. There is a nonconstant meromorphic function $f$ on $C$ whose only pole is a simple pole at $p$.

::: {.proof}
By the Riemann--Roch theorem, $\ell([p]) - \ell(K_C-[p]) = 1 + 1 - 0 = 2$, so $\ell([p])\geq 2$. The space $L([p])$ therefore contains a function $f$ that is not constant; its only possible pole is a simple pole at $p$, and it has one because it is nonconstant.
:::

<1>2. $f\colon C\to\PP^1$ is an isomorphism.

::: {.proof}
The degree of $f$ equals the number of poles counted with multiplicity, which is $1$ by step <1>1. A morphism of degree $1$ between smooth projective curves is an isomorphism.
:::

<1>3. $\PP^1$ is isomorphic to the conic $z_0 z_2=z_1^2$ in $\PP^2$.

::: {.proof}
In projective coordinates $t_0, t_1$ on $\PP^1$, the map $[t_0:t_1]\mapsto[z_0:z_1:z_2]=[t_0^2:t_0 t_1:t_1^2]$ is an isomorphism onto the conic $z_0 z_2=z_1^2$. Equivalently, it is the map given by the complete linear system of the anticanonical divisor, which has degree $2$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 give $C\cong\PP^1\cong V(z_0z_2-z_1^2)$, so the answer is $\boxed{\text{yes}}$.
:::
:::
