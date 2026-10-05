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
<1>1. The group order must be divisible by $7$.

::: {.proof}
Let $g$ be an element of order $7$. The cyclic subgroup
\[
\langle g\rangle
\]
has order $7$. By Lagrange's theorem, the order of this subgroup divides the
order of the finite group. Hence
\[
7\mid |G|.
\]
:::

<1>2. The group order must be odd.

::: {.proof}
If $2\mid |G|$, then Cauchy's theorem gives an element $x\in G$ of order
$2$. Such an element satisfies
\[
x^2=e,
\]
so
\[
x=x^{-1}.
\]
Since $x\ne e$, this contradicts the hypothesis. Therefore $2\nmid |G|$.
:::

<1>3. Among the listed choices, the only possible order is
\[
\boxed{35}.
\]

::: {.proof}
The choices divisible by $7$ are
\[
28,\qquad35,\qquad42.
\]
Steps <1>1 and <1>2 require divisibility by $7$ and oddness. Only $35$
satisfies both conditions.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested choice.
:::
:::
