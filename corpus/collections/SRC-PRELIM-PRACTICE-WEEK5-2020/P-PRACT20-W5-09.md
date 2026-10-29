---
schema: qual/card@1
id: P-PRACT20-W5-09
kind: problem
title: Possible orders of a group with an element of order $7$ and no involution
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement with clean inline math and restored the answer choices mangled into a tagged display, checked against Week5_solns.pdf page 3 (Problem 9).
---

::: {.problem}
Suppose that a group has an element of order $7$ but no element which is its own inverse (other than the identity). Which of the following is a possible order for this group?

(a) $27$ (b) $28$ (c) $35$ (d) $37$ (e) $42$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The group order must be divisible by $7$.


::: pf-proof

Let $g$ be an element of order $7$. The cyclic subgroup
$$
\langle g\rangle
$$
has order $7$. By Lagrange's theorem, the order of this subgroup divides the
order of the finite group. Hence
$$
7\mid |G|.
$$

:::

:::

::: {.pf-step #s1-2}

The group order must be odd.


::: pf-proof

If $2\mid |G|$, then Cauchy's theorem gives an element $x\in G$ of order
$2$. Such an element satisfies
$$
x^2=e,
$$
so
$$
x=x^{-1}.
$$
Since $x\ne e$, this contradicts the hypothesis. Therefore $2\nmid |G|$.

:::

:::

::: {.pf-step #s1-3}

Among the listed choices, the only possible order is
$$
\boxed{35}.
$$


::: pf-proof

The choices divisible by $7$ are
$$
28,\qquad35,\qquad42.
$$
Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} require divisibility by $7$ and oddness. Only $35$
satisfies both conditions.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested choice.

:::

:::

:::
