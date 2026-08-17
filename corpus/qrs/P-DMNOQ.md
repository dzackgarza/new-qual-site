---
schema: qual/card@1
id: P-DMNOQ
kind: problem
title: The Apollonius circle $\bigl|\frac{z-z_1}{z-z_2}\bigr|=c$
classification:
  areas:
  - complex-analysis
  topics:
  - fractional-linear-transformations
  - geometry
relations: []
review: draft
solved: true
---

::: problem
a. Prove that if $c>0$,
\[
\abs{w_1} = c\abs{w_2} \implies \abs{w_1 - c^2 w_2} = c\abs{w_1 - w_2}
.\]

b. Prove that if $c>0$ and $c\neq 1$, with $z_1\neq z_2$, then the following equation represents a circle:
\[
\abs{z-z_1 \over z-z_2} = c
.\]
Find its center and radius.

> Hint: use part (a)
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (a) Prove $\abs{w_1} = c\abs{w_2} \implies \abs{w_1 - c^2 w_2} = c\abs{w_1 - w_2}$ for $c > 0$; (b) show $\abs{\frac{z - z_1}{z - z_2}} = c$ ($c \neq 1$) is a circle and find its center and radius.

<1>1. Square both sides: $\abs{w_1 - c^2 w_2}^2 = \abs{w_1}^2 - 2c^2\Re(w_1 \bar{w_2}) + c^4\abs{w_2}^2$.
    Proof: $\abs{w_1 - c^2 w_2}^2 = (w_1 - c^2 w_2)(\bar{w_1} - c^2 \bar{w_2}) = \abs{w_1}^2 - c^2 w_1\bar{w_2} - c^2 \bar{w_1} w_2 + c^4 \abs{w_2}^2$, and $w_1\bar{w_2} + \bar{w_1}w_2 = 2\Re(w_1\bar{w_2})$.

<1>2. Similarly $c^2\abs{w_1 - w_2}^2 = c^2\abs{w_1}^2 - 2c^2\Re(w_1\bar{w_2}) + c^2\abs{w_2}^2$.
    Proof: Expand as in <1>1 and multiply by $c^2$.

<1>3. Under $\abs{w_1} = c\abs{w_2}$, the two expressions in <1>1 and <1>2 coincide.
    Proof: Substitute $\abs{w_1}^2 = c^2\abs{w_2}^2$ into <1>1: it becomes $c^2\abs{w_2}^2 - 2c^2\Re(w_1\bar{w_2}) + c^4\abs{w_2}^2 = c^2\abs{w_2}^2(1 + c^2) - 2c^2\Re(w_1\bar{w_2})$. Substituting into <1>2 gives $c^4\abs{w_2}^2 - 2c^2\Re(w_1\bar{w_2}) + c^2\abs{w_2}^2$, the same value. Hence $\abs{w_1 - c^2 w_2}^2 = c^2\abs{w_1 - w_2}^2$, and taking square roots (both sides nonnegative) proves (a).

<1>4. For $c \neq 1$, the locus $\abs{z - z_1} = c\abs{z - z_2}$ is a circle with center $\frac{z_1 - c^2 z_2}{1 - c^2}$ and radius $\frac{c\abs{z_1 - z_2}}{\abs{1 - c^2}}$.
    Proof: Apply part (a) with $w_1 = z - z_1$ and $w_2 = z - z_2$: the condition $\abs{z - z_1} = c\abs{z - z_2}$ forces $\abs{(z - z_1) - c^2(z - z_2)} = c\abs{(z - z_1) - (z - z_2)} = c\abs{z_2 - z_1}$, i.e. $\abs{(1 - c^2)z - z_1 + c^2 z_2} = c\abs{z_1 - z_2}$, which is $\abs{1 - c^2} \cdot \abs{z - \frac{z_1 - c^2 z_2}{1 - c^2}} = c\abs{z_1 - z_2}$. Since $c \neq 1$ the coefficient $1 - c^2 \neq 0$, giving the stated circle. (Conversely every point on this circle satisfies the original relation, by the same computation read backwards.)

<1>5. Q.E.D.
    Proof: <1>3 proves (a) and <1>4 proves (b) with the center and radius.

:::
