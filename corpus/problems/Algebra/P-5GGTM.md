---
schema: qual/card@1
id: P-5GGTM
kind: problem
title: Every field is a simple ring
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard computation, no repair needed), and the existing prose against a fresh
    re-derivation: for an ideal I of the field F, either I = 0 or there is a nonzero
    x in I, whose inverse lies in F, so 1 = x^{-1}x lies in I and then a = a*1 lies in
    I for every a, giving I = F; so the only ideals are 0 and F, which is simplicity.
    Correct. The prose passed over two things the proof now states: that in a
    commutative ring every ideal is two-sided, which is what makes "simple ring"
    apply, and the inclusion I subset F, which is what turns F subset I into equality.
    No source solution is retained for this card, so no source comparison was made.
    What was not checked: any printed source.
---

::: {.problem}
Show that every field is simple.
:::

::: {.solution}
Let $F$ be a field, so every nonzero element of $F$ is a unit, and let $I\trianglelefteq F$ be an ideal. A ring is simple when its only two-sided ideals are $0$ and the ring itself; since $F$ is commutative every ideal is two-sided.

::: pf

::: {.pf-step #zero}
If $I=0$ then $I$ is one of the two allowed ideals.

::: pf-proof
$I=0$ is the zero ideal, which is an ideal and is the first of the two ideals permitted in a simple ring.
:::

:::

::: {.pf-step #nonzero}
If $I\neq0$ then $I=F$.

::: pf-proof
Since $I\neq0$ there is $x\in I$ with $x\neq0$. In a field every nonzero element is a unit, so $x^{-1}\in F$, and $I$ is closed under multiplication by elements of $F$, giving $1=x^{-1}x\in I$. Then for every $a\in F$ we have $a=a\cdot1\in I$, again by closure under multiplication by ring elements. So $F\subseteq I$, and $I\subseteq F$ holds because $I$ is an ideal of $F$; hence $I=F$.
:::

:::

::: {.pf-step}
Every field is simple.

::: pf-proof
Steps [](#zero){.pf-ref} and [](#nonzero){.pf-ref} show that an arbitrary ideal $I$ of $F$ is either $0$ or $F$; there are no others, which is the definition of a simple ring. So $F$ is simple.
:::

:::

:::
:::
