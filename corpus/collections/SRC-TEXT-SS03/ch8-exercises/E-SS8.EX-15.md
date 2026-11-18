---
schema: qual/card@1
id: E-SS8.EX-15
kind: problem
title: An automorphism of $\halfplane$ is determined by the images of three boundary points
classification:
  areas:
    - complex-analysis
  topics:
    - Automorphisms
    - Fractional Linear Transformations
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the fixed-point quadratic and the three-roots argument; the values of $M_x$ at $x_1,x_2,x_3$; its determinant $(x_3-x_1)(x_3-x_2)(x_2-x_1)>0$; the sign of the corresponding product in each of the three cyclic orderings of $y$; and uniqueness from part (a).
---

::: {.exercise}
Here are two properties enjoyed by automorphisms of the upper half-plane.

(a) Suppose $\Phi$ is an automorphism of $\halfplane$ that fixes three distinct points on the real axis. Then $\Phi$ is the identity.

(b) Suppose $(x_1, x_2, x_3)$ and $(y_1, y_2, y_3)$ are two pairs of three distinct points on the real axis with
$$
x_1 < x_2 < x_3 \quad \text{and} \quad y_1 < y_2 < y_3.
$$
Prove that there exists (a unique) automorphism $\Phi$ of $\halfplane$ so that $\Phi(x_j) = y_j$, $j = 1, 2, 3$. The same conclusion holds if $y_3 < y_1 < y_2$ or $y_2 < y_3 < y_1$.
:::

::: {.solution}
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own.

::: pf

::: {.pf-step #form}
Every automorphism of $\halfplane$ has the form $\Phi(z)=\frac{az+b}{cz+d}$ with $a,b,c,d\in\RR$ and $ad-bc>0$.

::: pf-proof
This is the standard description of $\operatorname{Aut}(\halfplane)$ as $\PSL_2(\RR)$ acting by Möbius transformations.
:::
:::

::: {.pf-step #a}
(a) An automorphism fixing three distinct real points is the identity.

::: pf-proof
A fixed point $z\in\RR$ of $\Phi$ satisfies $cz^2+(d-a)z-b=0$. Three distinct real fixed points would make this quadratic polynomial have three roots, so it is identically zero: $c=0$, $b=0$ and $d=a$, giving $\Phi(z)=z$.
:::
:::

::: {.pf-step #map-x}
For $x_1<x_2<x_3$ the formula $M_x(z)=\frac{(x_3-x_1)(z-x_2)}{(x_3-x_2)(z-x_1)}$ satisfies $M_x(x_1)=\infty$, $M_x(x_2)=0$, $M_x(x_3)=1$, and $M_x\in\operatorname{Aut}(\halfplane)$.

::: pf-proof
Substitution gives the three values directly, the denominator vanishing exactly at $x_1$. In the form $(az+b)/(cz+d)$ the determinant $ad-bc$ equals $(x_3-x_1)(x_3-x_2)(x_2-x_1)$, which is positive for $x_1<x_2<x_3$, so $M_x$ preserves $\halfplane$.
:::
:::

::: {.pf-step #map-y}
With $y$ in any of the cyclic orderings $y_1<y_2<y_3$, $y_3<y_1<y_2$ or $y_2<y_3<y_1$, the analogous $M_y$ lies in $\operatorname{Aut}(\halfplane)$.

::: pf-proof
In each of the three orderings the product $(y_3-y_1)(y_3-y_2)(y_2-y_1)$ has two negative factors and one positive, hence is positive; by the determinant computation of step [](#map-x){.pf-ref} this makes $M_y$ an automorphism of $\halfplane$.
:::
:::

::: {.pf-step #b}
(b) $\Phi=M_y^{-1}\circ M_x$ is an automorphism of $\halfplane$ with $\Phi(x_j)=y_j$ for $j=1,2,3$.

::: pf-proof
Both factors are automorphisms by steps [](#map-x){.pf-ref} and [](#map-y){.pf-ref}, so $\Phi$ is one; and $\Phi(x_j)=M_y^{-1}(M_x(x_j))$ sends $M_x(x_1)=\infty$, $M_x(x_2)=0$, $M_x(x_3)=1$ to $M_y^{-1}(\infty)=y_1$, $M_y^{-1}(0)=y_2$, $M_y^{-1}(1)=y_3$.
:::
:::

::: {.pf-step #unique}
The automorphism of (b) is unique.

::: pf-proof
If $\Psi$ also satisfies $\Psi(x_j)=y_j$, then $\Psi^{-1}\circ\Phi$ fixes $x_1,x_2,x_3$, so it is the identity by part [](#a){.pf-ref} and $\Psi=\Phi$.
:::
:::

:::
:::
