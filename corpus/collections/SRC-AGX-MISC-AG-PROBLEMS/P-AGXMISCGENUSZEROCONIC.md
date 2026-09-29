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

::: pf

::: {.pf-step #meromorphic-function-simple-pole}
There is a nonconstant meromorphic function $f$ on $C$ whose only pole is a simple pole at $p$.

::: pf-proof
By the Riemann--Roch theorem, $\ell([p]) - \ell(K_C-[p]) = 1 + 1 - 0 = 2$, so $\ell([p])\geq 2$. The space $L([p])$ therefore contains a function $f$ that is not constant; its only possible pole is a simple pole at $p$, and it has one because it is nonconstant.
:::

:::

::: {.pf-step #f-is-isomorphism}
$f\colon C\to\PP^1$ is an isomorphism.

::: pf-proof
The degree of $f$ equals the number of poles counted with multiplicity, which is $1$ by step [](#meromorphic-function-simple-pole){.pf-ref}. A morphism of degree $1$ between smooth projective curves is an isomorphism.
:::

:::

::: {.pf-step #p1-isomorphic-to-conic}
$\PP^1$ is isomorphic to the conic $z_0 z_2=z_1^2$ in $\PP^2$.

::: pf-proof
In projective coordinates $t_0, t_1$ on $\PP^1$, the map $[t_0:t_1]\mapsto[z_0:z_1:z_2]=[t_0^2:t_0 t_1:t_1^2]$ is an isomorphism onto the conic $z_0 z_2=z_1^2$. Equivalently, it is the map given by the complete linear system of the anticanonical divisor, which has degree $2$.
:::

:::

::: pf-qed
Steps [](#f-is-isomorphism){.pf-ref} and [](#p1-isomorphic-to-conic){.pf-ref} give $C\cong\PP^1\cong V(z_0z_2-z_1^2)$, so the answer is $\boxed{\text{yes}}$.
:::

:::

:::
