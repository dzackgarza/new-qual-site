---
schema: qual/card@1
id: P-TRIV-CA10
kind: problem
title: Image of a disk under the principal branch of $\log z$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Added a remark that Complex Analysis Problem 10 on page 14 of the source PDF does not state the center of the disk.
---

::: {.problem}
Take a disk of radius $R$ with a branch cut on the negative real axis; what does $\log z$ map this onto?
Where is the origin mapped onto?
:::

::: {.remark}
The source does not state the center of the disk.
The question about the image of the origin suggests the disk $\{z : \abs{z} < R\}$ centered at $0$, with the cut along $(-R, 0]$; the source does not say so, and $\log z$ is not defined at the branch point $z = 0$.
:::

::: {.solution}

Interpret the domain, as in the remark, as
$$
D_R
=
\{z\in\CC:0<\abs{z}<R,\ -\pi<\arg z<\pi\},
$$
with the principal branch
$$
\Log z
=
\log\abs{z}+i\arg z.
$$

::: pf

::: {.pf-step #s1-1}

If $z\in D_R$ and
$$
w=\Log z=u+iv,
$$
then
$$
u<\log R
\qquad\text{and}\qquad
-\pi<v<\pi.
$$


::: pf-proof

By definition,
$$
u=\log\abs{z}
$$
and
$$
v=\arg z.
$$
Since
$$
0<\abs{z}<R,
$$
one has
$$
-\infty<\log\abs{z}<\log R.
$$
The principal-argument condition gives
$$
-\pi<v<\pi.
$$

:::

:::

::: {.pf-step #s1-2}

Conversely, if
$$
w=u+iv
$$
satisfies
$$
u<\log R
\qquad\text{and}\qquad
-\pi<v<\pi,
$$
then
$$
z=e^w
$$
belongs to $D_R$ and satisfies
$$
\Log z=w.
$$


::: pf-proof

One has
$$
e^w=e^u e^{iv},
$$
so
$$
\abs{e^w}=e^u<R.
$$
Also $e^u>0$, and because $v\in(-\pi,\pi)$, the principal argument of
$e^w$ is exactly $v$. Thus
$$
e^w\in D_R
$$
and
$$
\Log(e^w)=u+iv=w.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\Log(D_R)
=
\{u+iv\in\CC:u<\log R,\ -\pi<v<\pi\}.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives containment in the displayed half-infinite horizontal strip,
and step [](#s1-2){.pf-ref} gives the reverse containment.

:::

:::

::: {.pf-step #s1-4}

The origin is not mapped to any finite complex number.


::: pf-proof

The logarithm is not defined at $z=0$, because there is no complex number
$w$ satisfying
$$
e^w=0.
$$
Thus $0$ is not an element of the domain of the chosen logarithm branch.

:::

:::

::: {.pf-step #s1-5}

As $z\to0$ within the slit disk,
$$
\operatorname{Re}\Log z
=
\log\abs{z}
\longrightarrow-\infty.
$$


::: pf-proof

This is the ordinary real limit
$$
\log r\to-\infty
$$
as $r\to0^+$, with $r=\abs{z}$.

:::

:::

::: {.pf-step #s1-6}

Hence the geometric meaning of the branch point $0$ under the logarithm
is the left end at infinity of the strip, not an ordinary image point.


::: pf-proof

Step [](#s1-4){.pf-ref} shows that $0$ has no finite image, while step [](#s1-5){.pf-ref} describes the
limiting behavior of its nearby points.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-6){.pf-ref} give respectively the image of the slit disk and the
status of the origin.

:::

:::

:::
