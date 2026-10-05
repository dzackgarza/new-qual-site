---
schema: qual/card@1
id: P-UCLAB08S-08
kind: problem
title: Decomposition associated to an idempotent linear map
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $V$ be an $n$-dimensional vector space over $\mathbb Q$, and let $T\colon V\to V$ be linear with $T^2=T$.
Prove that every $v\in V$ can be written uniquely as
\[
v=v_1+v_2
\]
with $T(v_1)=v_1$ and $T(v_2)=0$.
:::

::: {.solution}
<1>1. For any
\[
v\in V,
\]
define
\[
\boxed{
v_1=Tv,
\qquad
v_2=v-Tv
}.
\]

::: {.proof}
These are well-defined vectors of $V$ because $T$ maps $V$ to itself.
:::

<1>2. One has
\[
v=v_1+v_2.
\]

::: {.proof}
By the definitions in step <1>1,
\[
v_1+v_2
=
Tv+(v-Tv)
=v.
\]
:::

<1>3. The vector $v_1$ satisfies
\[
\boxed{T(v_1)=v_1}.
\]

::: {.proof}
Using
\[
v_1=Tv
\]
and the idempotence relation
\[
T^2=T,
\]
one gets
\[
T(v_1)
=
T(Tv)
=
T^2v
=
Tv
=
v_1.
\]
:::

<1>4. The vector $v_2$ satisfies
\[
\boxed{T(v_2)=0}.
\]

::: {.proof}
Using
\[
v_2=v-Tv,
\]
one gets
\[
\begin{aligned}
T(v_2)
&=
Tv-T^2v\\
&=
Tv-Tv\\
&=
0.
\end{aligned}
\]
:::

<1>5. Thus every
\[
v\in V
\]
has at least one decomposition with the required properties.

::: {.proof}
Steps <1>2--<1>4 show that the vectors constructed in step <1>1 satisfy
\[
v=v_1+v_2,
\qquad
T(v_1)=v_1,
\qquad
T(v_2)=0.
\]
:::

<1>6. Suppose
\[
v=w_1+w_2
\]
is another decomposition satisfying
\[
T(w_1)=w_1
\qquad\text{and}\qquad
T(w_2)=0.
\]
Then
\[
w_1=Tv.
\]

::: {.proof}
Apply $T$ to
\[
v=w_1+w_2.
\]
Then
\[
Tv
=
T(w_1)+T(w_2)
=
w_1+0
=
w_1.
\]
:::

<1>7. Under the hypotheses of step <1>6,
\[
w_2=v-Tv.
\]

::: {.proof}
Since
\[
v=w_1+w_2
\]
and step <1>6 gives
\[
w_1=Tv,
\]
one has
\[
w_2=v-w_1=v-Tv.
\]
:::

<1>8. Therefore the decomposition is unique.

::: {.proof}
Steps <1>6--<1>7 show that any decomposition with the required properties must equal
\[
Tv+(v-Tv),
\]
which is exactly the decomposition from step <1>1.
:::

<1>9. Equivalently,
\[
\boxed{
V=\operatorname{im}T\oplus\ker T
}.
\]

::: {.proof}
Every vector is a sum of one vector fixed by $T$, hence lying in $\operatorname{im}T$, and one vector annihilated by $T$, hence lying in $\ker T$.
Uniqueness of the decomposition means the sum is direct.
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>5 and <1>8 prove existence and uniqueness of the required decomposition.
:::
:::
