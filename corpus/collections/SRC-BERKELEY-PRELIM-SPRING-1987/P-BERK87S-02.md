---
schema: qual/card@1
id: P-BERK87S-02
kind: problem
title: Local and global injectivity of $(u,v)\mapsto(u+v,u^2+v^2)$ on $u>v$
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
    The Jacobian determinant is 2(v-u), so the inverse function theorem
    gives local injectivity on u>v. Writing s=u+v and d=u-v>0 gives
    u^2+v^2=(s^2+d^2)/2, which identifies the range and yields an explicit
    unique inverse.
---

::: {.problem}
Let
\[
W=\{(u,v)\in\mathbb R^2:u>v\}
\]
and define
\[
T(u,v)=(u+v,u^2+v^2).
\]

1. Prove that $T$ is locally one-to-one.
2. Determine the range of $T$ and prove that $T$ is globally one-to-one.
:::

::: {.solution}
::: pf

::: {.pf-step #jacobian-nonzero}
The Jacobian determinant of $T$ at $(u,v)\in W$ is
$$
\det DT(u,v)=2(v-u)\neq0.
$$

::: pf-proof
The derivative matrix is
$$
DT(u,v)
=
\begin{pmatrix}
1&1\\
2u&2v
\end{pmatrix},
$$
so
$$
\det DT(u,v)
=
2v-2u
=
2(v-u).
$$
Since $(u,v)\in W$ means $u>v$, this determinant is nonzero.
:::

:::

::: {.pf-step #locally-injective}
The map $T$ is locally one-to-one on $W$.

::: pf-proof
By step [](#jacobian-nonzero){.pf-ref}, the derivative of $T$ is invertible at every point of the
open set $W$. The inverse function theorem therefore gives, around each
point of $W$, a neighborhood on which $T$ is one-to-one.
:::

:::

::: {.pf-step #range-necessary-condition}
If
$$
T(u,v)=(s,q),
$$
then
$$
q>\frac{s^2}{2}.
$$

::: pf-proof
Set
$$
s=u+v,
\qquad
d=u-v.
$$
Since $(u,v)\in W$, one has $d>0$. Moreover,
$$
\begin{aligned}
2q
&=
2u^2+2v^2\\
&=
(u+v)^2+(u-v)^2\\
&=
s^2+d^2.
\end{aligned}
$$
Thus
$$
q
=
\frac{s^2+d^2}{2}
>
\frac{s^2}{2}.
$$
:::

:::

::: {.pf-step #range-sufficient-condition}
Conversely, if $(s,q)\in\RR^2$ satisfies
$$
q>\frac{s^2}{2},
$$
then it has a preimage in $W$, namely
$$
u
=
\frac{s+\sqrt{2q-s^2}}{2},
\qquad
v
=
\frac{s-\sqrt{2q-s^2}}{2}.
$$

::: pf-proof
The hypothesis makes
$$
d\coloneqq\sqrt{2q-s^2}
$$
a positive real number. The displayed definitions give
$$
u+v=s
\qquad\text{and}\qquad
u-v=d>0,
$$
so $(u,v)\in W$. Also,
$$
u^2+v^2
=
\frac{(u+v)^2+(u-v)^2}{2}
=
\frac{s^2+d^2}{2}
=q.
$$
Hence $T(u,v)=(s,q)$.
:::

:::

::: {.pf-step #range-boxed}
The range of $T$ is
$$
\boxed{
T(W)
=
\left\{
(s,q)\in\RR^2:
q>\frac{s^2}{2}
\right\}
}.
$$

::: pf-proof
Step [](#range-necessary-condition){.pf-ref} gives the inclusion from left to right, and step [](#range-sufficient-condition){.pf-ref} gives
the reverse inclusion.
:::

:::

::: {.pf-step #globally-injective}
The map $T$ is globally one-to-one on $W$.

::: pf-proof
Suppose
$$
T(u,v)=(s,q)
$$
with $(u,v)\in W$. Step [](#range-necessary-condition){.pf-ref} gives
$$
(u-v)^2
=
2q-s^2.
$$
Because $u-v>0$, necessarily
$$
u-v=\sqrt{2q-s^2}.
$$
Together with $u+v=s$, this uniquely determines
$$
u
=
\frac{s+\sqrt{2q-s^2}}2,
\qquad
v
=
\frac{s-\sqrt{2q-s^2}}2.
$$
Thus every point in the range has at most one preimage.
:::

:::

::: pf-qed
Step [](#locally-injective){.pf-ref} proves local one-to-one behavior, step [](#range-boxed){.pf-ref} determines the
range, and step [](#globally-injective){.pf-ref} proves global injectivity.
:::

:::
:::
