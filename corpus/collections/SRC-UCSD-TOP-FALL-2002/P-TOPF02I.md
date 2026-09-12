---
schema: qual/card@1
id: P-TOPF02I
kind: problem
title: "Which powers of the height coordinate are Morse functions on S^2"
classification:
  areas:
  - topology
  topics:
  - Morse Theory
  - Differential Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Restored Fall 2002 problem 9 from the retained UCSD qualifying-exam source; the previous card contained an unrelated cup-product problem.
---

::: {.problem}
Which of the following functions is a Morse function on the standard unit sphere $S^2\subset\mathbb R^3$?
$$
f_1(x,y,z)=z^2,
\qquad
f_2(x,y,z)=z,
\qquad
f_3(x,y,z)=z^4.
$$
Here a Morse function means a smooth function whose critical points are isolated and nondegenerate.
:::

::: {.solution}
<1>1. The height function $f_2(x,y,z)=z$ has exactly two critical points: the north and south poles.
::: {.proof}
At a point of $S^2$, the differential of the ambient coordinate function $z$ vanishes on the tangent plane exactly when the vector $(0,0,1)$ is normal to the sphere. Since the normal at $(x,y,z)$ is spanned by $(x,y,z)$, this occurs exactly at $(0,0,1)$ and $(0,0,-1)$.
:::

<1>2. Both critical points of $f_2$ are nondegenerate.
::: {.proof}
Near the north pole use $(x,y)$ as local coordinates, with
$$
z=\sqrt{1-x^2-y^2}=1-\frac{x^2+y^2}{2}+O(\|(x,y)\|^4).
$$
Thus the Hessian at the north pole is $-I_2$. Near the south pole,
$$
z=-\sqrt{1-x^2-y^2}=-1+\frac{x^2+y^2}{2}+O(\|(x,y)\|^4),
$$
so the Hessian is $+I_2$. Both are nonsingular.
:::

<1>3. Therefore $f_2=z$ is a Morse function.
::: {.proof}
By <1>1 its critical points are isolated, and by <1>2 they are nondegenerate.
:::

<1>4. Every point of the equator $\{z=0\}\subset S^2$ is a critical point of $f_1=z^2$.
::: {.proof}
On $S^2$,
$$
df_1=2z\,dz.
$$
Hence $df_1=0$ at every point with $z=0$.
:::

<1>5. Thus $f_1=z^2$ is not Morse.
::: {.proof}
Its critical set contains the entire equatorial circle, so its critical points are not isolated.
:::

<1>6. Every point of the equator is also a critical point of $f_3=z^4$.
::: {.proof}
We have
$$
df_3=4z^3\,dz,
$$
which vanishes whenever $z=0$.
:::

<1>7. Thus $f_3=z^4$ is not Morse.
::: {.proof}
Again the equator is a non-discrete critical set.
:::

<1>8. Hence among the three functions, only
$$
\boxed{f(x,y,z)=z}
$$
is Morse.
::: {.proof}
Combine <1>3, <1>5, and <1>7.
:::
:::
