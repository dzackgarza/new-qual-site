---
schema: qual/card@1
id: P-UGAP13F-09
kind: problem
title: Construct a linear map on $\RR^3$ with a prescribed one-dimensional kernel
classification:
  areas: [prelim]
  topics:
  - Linear Maps
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Give an example, with proof, of a linear map from $\RR^3$ to some vector space whose kernel is exactly the subspace spanned by $(1,2,3)$.
:::

::: {.solution}

Define
$$
\boxed{
T:\RR^3\to\RR^2,
\qquad
T(x,y,z)
=
(2x-y,\,3x-z).
}
$$

::: pf

::: pf-step

The map $T$ is linear.


::: pf-proof

It is given by the matrix
$$
\begin{pmatrix}
2&-1&0\\
3&0&-1
\end{pmatrix}.
$$
Hence for
$$
u,v\in\RR^3
$$
and
$$
a,b\in\RR,
$$
$$
T(au+bv)
=
aT(u)+bT(v).
$$

:::

:::

::: {.pf-step #s1-2}

The vector
$$
(1,2,3)
$$
lies in the kernel of $T$.


::: pf-proof

Compute
$$
T(1,2,3)
=
(2-2,,3-3)
=
(0,0).
$$
Therefore
$$
\operatorname{span}\{(1,2,3)\}
\subseteq
\ker T.
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
(x,y,z)\in\ker T,
$$
then
$$
y=2x
\qquad\text{and}\qquad
z=3x.
$$


::: pf-proof

The condition
$$
T(x,y,z)=(0,0)
$$
is exactly the system
$$
2x-y=0,
\qquad
3x-z=0.
$$
Solving gives the two displayed equations.

:::

:::

::: {.pf-step #s1-4}

Hence every vector in the kernel has the form
$$
(x,y,z)
=
x(1,2,3).
$$


::: pf-proof

Substitute the equations from step [](#s1-3){.pf-ref}:
$$
(x,y,z)
=
(x,2x,3x)
=
x(1,2,3).
$$
Therefore
$$
\ker T
\subseteq
\operatorname{span}\{(1,2,3)\}.
$$

:::

:::

::: {.pf-step #s1-5}

Thus
$$
\boxed{
\ker T
=
\operatorname{span}\{(1,2,3)\}.
}
$$


::: pf-proof

Combine the two inclusions from steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} verifies that the displayed linear map has exactly the prescribed
kernel.

:::

:::

:::
