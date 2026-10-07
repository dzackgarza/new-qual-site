---
schema: qual/card@1
id: P-AGXMISCPRODRATIONAL
kind: problem
title: $\PP^n\cross \PP^m$ is a rational variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Varieties
  - Birational Maps
  - Projective Space
relations: []
review: draft
---

::: {.problem}
Show that $\PP^n\cross \PP^m$ is rational.
:::

::: {.solution}
<1>1. The dense open subset
$$
U=D_+(x_0)\cross D_+(y_0)\subset\PP^n\cross\PP^m
$$
is isomorphic to $\AA^{n+m}$.
::: {.proof}
On $U$, define affine coordinates
$$
u_i=\frac{x_i}{x_0}\quad(1\le i\le n),
\qquad
v_j=\frac{y_j}{y_0}\quad(1\le j\le m).
$$
Then
$$
([x_0:\ldots:x_n],[y_0:\ldots:y_m])
\longmapsto
(u_1,\ldots,u_n,v_1,\ldots,v_m)
$$
is an isomorphism
$$
U\xrightarrow{\sim}\AA^{n+m},
$$
with inverse
$$
(u_1,\ldots,u_n,v_1,\ldots,v_m)
\longmapsto
([1:u_1:\ldots:u_n],[1:v_1:\ldots:v_m]).
$$
Both $D_+(x_0)\subset\PP^n$ and $D_+(y_0)\subset\PP^m$ are nonempty dense opens, so $U$ is dense in $\PP^n\cross\PP^m$.
:::

<1>2. $\PP^n\cross\PP^m$ is $\boxed{\text{rational}}$.
::: {.proof}
By step <1>1, $\PP^n\cross\PP^m$ contains a dense open subset isomorphic to $\AA^{n+m}$. Since $\AA^{n+m}$ is a dense open subset of $\PP^{n+m}$, the varieties $\PP^n\cross\PP^m$ and $\PP^{n+m}$ are birational. Hence $\PP^n\cross\PP^m$ is rational.
:::

<1>3. Q.E.D.
::: {.proof}
Step <1>2 is the required conclusion.
:::
:::
