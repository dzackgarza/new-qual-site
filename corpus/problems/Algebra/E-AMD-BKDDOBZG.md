---
schema: qual/card@1
id: E-AMD-BKDDOBZG
kind: problem
title: An ideal containing a unit is the whole ring
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard fact, no repair needed; the card's own wording uses \normal for
    trianglelefteq, which the preamble defines), and the existing prose solution
    against a fresh re-derivation: from u in I and u^{-1} in R the ideal property
    gives u^{-1}u = 1 in I, and then r = r*1 lies in I for every r, so R is
    contained in I and I = R. Correct. The prose's parenthetical about left and
    right ideals is kept as a parenthetical in the two steps where it applies,
    rather than as an extra claim. No source solution is retained for this card, so
    no source comparison was made. What was not checked: any printed source.
---

::: {.exercise}
Show that if an ideal $I\normal R$ contains a unit then $I = R$.
:::

::: {.solution}
Let $R$ be a ring with $1$ and $I\trianglelefteq R$ a two-sided ideal; a unit of $R$ is an element $u$ with $u^{-1}\in R$ and $u^{-1}u=uu^{-1}=1$.

::: pf

::: {.pf-step #one}
$1\in I$.

::: pf-proof
Let $u\in I$ be a unit. Since $I$ is an ideal it is closed under multiplication by elements of $R$ on either side, so from $u\in I$ and $u^{-1}\in R$ we get $u^{-1}u\in I$; and $u^{-1}u=1$ because $u$ is a unit. Hence $1\in I$. (For a left ideal the same product $u^{-1}u$ is the one that lies in $I$; for a right ideal one uses $uu^{-1}$ instead, which gives the same conclusion.)
:::

:::

::: {.pf-step #contains}
$R\subseteq I$.

::: pf-proof
Let $r\in R$. Since $1\in I$ by step [](#one){.pf-ref} and $I$ is closed under left multiplication by $R$, the product $r\cdot1$ lies in $I$; and $r\cdot1=r$. So every $r\in R$ lies in $I$. (For a right ideal one uses $1\cdot r$.)
:::

:::

::: {.pf-step}
$I=R$.

::: pf-proof
$I\subseteq R$ holds by definition of an ideal as a subset closed under addition and multiplication by ring elements, and $R\subseteq I$ is step [](#contains){.pf-ref}; two inclusions give equality. So an ideal containing a unit is the whole ring.
:::

:::

:::
:::
