---
schema: qual/card@1
id: P-PRACT20-W4-15
kind: problem
title: Evaluating a linear functional on $\RR^2$ from two values
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
  - Linear Transformations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the retained solution booklet of the collection,
    assets/attachments/Week4_solns.pdf, page 6, where Problem 15 reads: "Suppose
    that f: R^2 -> R is linear. If f(1,1) = 1 and f(-1,0) = 2, what is f(3,5)?"
    The card states exactly this, and the retained solution there is the single
    line "By linearity f(3,5) = f(5(1,1) + 2(-1,0)) = 5f(1,1) + 2f(-1,0) = 9",
    which is the card's solution word for word. The proof is complete for the
    problem: the linear combination 5(1,1) + 2(-1,0) = (3,5) is a direct
    arithmetic identity, and linearity is applied once to that identity. Nothing
    is left unproved, so nothing was written.
---

::: {.problem}
Suppose that $f \colon \RR^{2} \to \RR$ is linear.
If $f(1, 1) = 1$ and $f(-1, 0) = 2$, what is $f(3, 5)$?
:::

::: {.solution}
Since $(3,5)=5(1,1)+2(-1,0)$, linearity gives $\boxed{f(3,5)=5f(1,1)+2f(-1,0)=9}$.
:::
