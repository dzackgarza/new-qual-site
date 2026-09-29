---
schema: qual/card@1
id: P-3HHKX
kind: problem
title: Reverse triangle inequality $|z+w|\ge\bigl||z|-|w|\bigr|$
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Prove the following inequality, and explain when equality holds:
\[
\abs{z+w} \geq \abs{ \abs{z} - \abs{w} }
.\]
:::

::: {.solution}
**Goal:** Prove $\abs{z + w} \ge \abs{\abs{z} - \abs{w}}$ and explain when equality holds.

::: pf

::: {.pf-step #z-bound}
$\abs{z} \le \abs{z + w} + \abs{w}$.

::: pf-proof
Triangle inequality applied to $z = (z + w) + (-w)$: $\abs{z} \le \abs{z + w} + \abs{-w} = \abs{z+w} + \abs{w}$, hence $\abs{z} - \abs{w} \le \abs{z + w}$.
:::

:::

::: {.pf-step #w-bound}
$\abs{w} \le \abs{z + w} + \abs{z}$.

::: pf-proof
Same argument with roles swapped: $\abs{w} \le \abs{z + w} + \abs{z}$, hence $\abs{w} - \abs{z} \le \abs{z + w}$.
:::

:::

::: {.pf-step #abs-diff-bound}
$\abs{\abs{z} - \abs{w}} \le \abs{z + w}$.

::: pf-proof
$\abs{\abs{z} - \abs{w}} = \max(\abs{z} - \abs{w}, \abs{w} - \abs{z}) \le \abs{z + w}$ by steps [](#z-bound){.pf-ref} and [](#w-bound){.pf-ref}.
:::

:::

::: {.pf-step #equality-case}
Equality characterization.

::: pf-proof
Equality holds iff $\abs{z} - \abs{w} = \abs{z+w}$ with $\abs{z} \ge \abs{w}$ (or the symmetric case). By the equality case of the triangle inequality, $\abs{z + w} = \abs{z} + \abs{w}$ iff $z$ and $w$ are nonnegative real multiples of each other. Here $z = (z+w) + (-w)$: equality in step [](#z-bound){.pf-ref} requires $z + w$ and $-w$ to be nonnegatively aligned, i.e. $z + w = \lambda(-w)$ with $\lambda \ge 0$, i.e. $z = -(\lambda + 1)w$, i.e. $z/w \le 0$ (real, nonpositive). Symmetrically for step [](#w-bound){.pf-ref}. Conclusion: equality holds iff $z$ and $w$ are collinear with opposite directions: $z/w \in (-\infty, 0]$, i.e. $\arg z = \arg w + \pi \pmod{2\pi}$ (or one of them is $0$).
:::

:::

::: pf-qed
Step [](#abs-diff-bound){.pf-ref} proves the inequality; step [](#equality-case){.pf-ref} characterizes equality.
:::

:::
