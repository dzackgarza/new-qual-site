---
schema: qual/card@1
id: P-PRACT20-W4-20
kind: problem
title: An idempotent operator splits $V$ into its fixed space and kernel
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Linear Transformations
  - Idempotents
relations: []
review: draft
---

::: {.problem}
Assume that V is a finite dimensional vector space and $T : V \to V$ is a linear transformation such that $T ^ { 2 } = T$ . Show that each $v \in V$ can be uniquely written as $v = v _ { 1 } + v _ { 2 }$ where $T ( v _ { 1 } ) = v _ { 1 }$ and $T ( v _ { 2 } ) = 0$
:::

::: {.solution}
<1>1. Every $v\in V$ has a decomposition
$$
v=T(v)+(v-T(v))
$$
with the first summand fixed by $T$ and the second in $\ker T$.
::: {.proof}
Set
$$
v_1=T(v),
\qquad
v_2=v-T(v).
$$
Then
$$
T(v_1)=T^2(v)=T(v)=v_1,
$$
while
$$
T(v_2)=T(v)-T^2(v)=0.
$$
Thus $v=v_1+v_2$ has the required form.
:::

<1>2. The decomposition is unique.
::: {.proof}
Suppose also
$$
v=u_1+u_2,
\qquad
T(u_1)=u_1,
\qquad
T(u_2)=0.
$$
Applying $T$ gives
$$
T(v)=u_1.
$$
Hence $u_1=T(v)=v_1$, and then
$$
u_2=v-u_1=v-v_1=v_2.
$$
:::

<1>3. Q.E.D.
::: {.proof}
Steps <1>1--<1>2 prove existence and uniqueness of the required decomposition.
:::
:::
