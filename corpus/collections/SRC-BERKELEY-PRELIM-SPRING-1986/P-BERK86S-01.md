---
schema: qual/card@1
id: P-BERK86S-01
kind: problem
title: Matrix of the half-turn about a prescribed axis in $\mathbb R^3$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Decomposed each vector into its component along the unit axis e and its
    orthogonal component. A half-turn fixes the former and negates the
    latter, giving T(v)=2< v,e >e-v and matrix 2ee^T-I.
---

::: {.problem}
Let $e=(a,b,c)$ be a unit vector in $\mathbb R^3$. Let $T$ be rotation by $180^\circ$ about the axis spanned by $e$. Find the matrix of $T$ in the standard basis.
:::

::: {.solution}
::: pf

::: {.pf-step #orthogonal-decomposition}
Every $v\in\RR^3$ has the orthogonal decomposition
$$
v
=
\inner{v}{e}e
+
\left(v-\inner{v}{e}e\right),
$$
where the second summand is orthogonal to $e$.

::: pf-proof
Since $e$ is a unit vector,
$$
\inner{v-\inner{v}{e}e}{e}
=
\inner{v}{e}
-\inner{v}{e}\inner{e}{e}
=0.
$$
Thus the first summand is the projection of $v$ onto the rotation axis
and the second lies in its orthogonal plane.
:::

:::

::: {.pf-step #half-turn-formula}
The half-turn satisfies
$$
T(v)=2\inner{v}{e}e-v.
$$

::: pf-proof
A rotation by $180^\circ$ about the axis $\RR e$ fixes every vector on
that axis and sends every vector in the orthogonal plane to its negative.
Applying this to the decomposition in step [](#orthogonal-decomposition){.pf-ref} gives
$$
\begin{aligned}
T(v)
&=
\inner{v}{e}e
-
\left(v-\inner{v}{e}e\right)\\
&=
2\inner{v}{e}e-v.
\end{aligned}
$$
:::

:::

::: {.pf-step #matrix-boxed}
In the standard basis, the matrix of $T$ is
$$
\boxed{
\begin{pmatrix}
2a^2-1&2ab&2ac\\
2ab&2b^2-1&2bc\\
2ac&2bc&2c^2-1
\end{pmatrix}
}.
$$

::: pf-proof
Regard
$$
e=
\begin{pmatrix}
a\\
b\\
c
\end{pmatrix}.
$$
For a column vector $v$, one has
$$
\inner{v}{e}=e^{\mathsf T}v.
$$
Hence step [](#half-turn-formula){.pf-ref} becomes
$$
T(v)
=
\left(2ee^{\mathsf T}-I_3\right)v.
$$
Now
$$
ee^{\mathsf T}
=
\begin{pmatrix}
a^2&ab&ac\\
ab&b^2&bc\\
ac&bc&c^2
\end{pmatrix},
$$
so expanding $2ee^{\mathsf T}-I_3$ gives the displayed matrix.
:::

:::

::: pf-qed
Step [](#matrix-boxed){.pf-ref} is the requested standard-basis matrix.
:::

:::
:::
