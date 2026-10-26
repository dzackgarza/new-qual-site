---
schema: qual/card@1
id: P-TRIV-LA24
kind: problem
title: Translations are not linear
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 24, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Show that the translation ${ \vec { x } } \mapsto { \vec { x } } + { \vec { a } }$ ,where ${ \vec { x } } , { \vec { a } } \in \mathbb R ^ { n }$ , is not a linear transformation in $\mathbb { R } ^ { n }$
:::

::: {.remark}
The claim requires $a\neq0$. If $a=0$, the translation is the identity map,
which is linear.
:::

Define
$$
T_a(x)=x+a.
$$

::: pf

::: pf-step

Every linear transformation $T:\mathbb R^n\to\mathbb R^n$ satisfies
$$
T(0)=0.
$$


::: pf-proof

By linearity,
$$
T(0)
=
T(0+0)
=
T(0)+T(0).
$$
Subtracting $T(0)$ from both sides gives $T(0)=0$.

:::

:::

::: pf-step

The translation satisfies
$$
T_a(0)=a.
$$


::: pf-proof

By definition,
$$
T_a(0)=0+a=a.
$$

:::

:::

::: pf-step

If $a\neq0$, then $T_a$ is not linear.


::: pf-proof

Steps <1>1 and <1>2 are incompatible when $a\neq0$: a linear map would have
to send $0$ to $0$, whereas $T_a$ sends $0$ to $a$.

:::

:::

::: pf-step

If $a=0$, then $T_a$ is linear.


::: pf-proof

In that case,
$$
T_0(x)=x,
$$
the identity transformation.

:::

:::

::: pf-step

Therefore a translation is linear exactly in the trivial case
$$
\boxed{a=0}.
$$


::: pf-proof

Step <1>3 excludes every nonzero translation vector, and step <1>4 handles
$a=0$.

:::

:::

::: pf-qed

Step <1>5 gives the precise conclusion.

:::

:::
