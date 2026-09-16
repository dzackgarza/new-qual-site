---
schema: qual/card@1
id: P-CH7-1
kind: problem
title: Cosets of the Klein four-subgroup in $A_4$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Wrote the statement in math mode and added a remark that Table 5.1, which the solution's alpha labels refer to, is not in the source; page 1 of Ch7Sltns.pdf.
---

::: {.problem}
Let $H = \{(1), (12)(34), (13)(24), (14)(23)\}$. Find the left cosets of $H$ in $A_4$ (using table 5.1).
:::

::: {.solution}
There are three cosets:

$$
H = \{ ( 1 ) , ( 1 2 ) ( 3 4 ) , ( 1 3 ) ( 2 4 ) , ( 1 4 ) ( 2 3 ) \} = \{ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } , \alpha _ { 4 } \}
$$

$$
( 1 2 3 ) H = \{ ( 1 2 3 ) , ( 1 3 4 ) , ( 2 4 3 ) , ( 1 4 2 ) \} = \{ \alpha _ { 5 } , \alpha _ { 6 } , \alpha _ { 7 } , \alpha _ { 8 } \}
$$

$$
( 1 3 2 ) H = \{ ( 1 3 2 ) , ( 1 4 3 ) , ( 2 3 4 ) , ( 1 2 4 ) \} = \{ \alpha _ { 9 } , \alpha _ { 1 0 } , \alpha _ { 1 1 } , \alpha _ { 1 2 } \}
$$
:::

::: {.remark}
The source does not reproduce table 5.1; the labels $\alpha_1, \ldots, \alpha_{12}$ in the solution refer to that table.
:::
