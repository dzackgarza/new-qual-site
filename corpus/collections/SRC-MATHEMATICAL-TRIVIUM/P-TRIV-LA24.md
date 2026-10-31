---
schema: qual/card@1
id: P-TRIV-LA24
kind: problem
title: Translations are not linear
classification:
  areas: [prelim]
  topics:
  - Linear Transformations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 24, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Show that the translation $\vec{x} \to \vec{x} + \vec{a}$, where $\vec{x}, \vec{a} \in \RR^n$, is not a linear transformation in $\RR^n$.
:::

::: {.remark}
The claim requires $a\neq0$. If $a=0$, the translation is the identity map,
which is linear.
:::

::: {.solution}

Define
$$
T_a(x)=x+a.
$$

::: pf

::: {.pf-step #s1-1}

Every linear transformation $T:\RR^n\to\RR^n$ satisfies
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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

If $a\neq0$, then $T_a$ is not linear.


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} are incompatible when $a\neq0$: a linear map would have
to send $0$ to $0$, whereas $T_a$ sends $0$ to $a$.

:::

:::

::: {.pf-step #s1-4}

If $a=0$, then $T_a$ is linear.


::: pf-proof

In that case,
$$
T_0(x)=x,
$$
the identity transformation.

:::

:::

::: {.pf-step #s1-5}

Therefore a translation is linear exactly in the trivial case
$$
\boxed{a=0}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} excludes every nonzero translation vector, and step [](#s1-4){.pf-ref} handles
$a=0$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the precise conclusion.

:::

:::

:::
