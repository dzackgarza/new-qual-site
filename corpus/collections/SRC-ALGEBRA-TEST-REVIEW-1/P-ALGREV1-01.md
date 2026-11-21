---
schema: qual/card@1
id: P-ALGREV1-01
kind: problem
title: Multiplicative groups of rationals and reals
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Group Isomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, open-ended question 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Distinguished the groups by cardinality: Q* is countable while R* is uncountable."
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained document `assets/attachments/Review1.pdf`: the statement is item 1 of the review sheet, and its printed words are
    the card's. The item and the file are now named in the solution's opening sentence. Not
    checked in this pass: the argument, which the edit does not touch.
---
::: {.problem}
Prove or disprove that $\QQ^*$ under multiplication is isomorphic to $\RR^*$ under multiplication.
:::

::: {.solution}
This is item 1 of the review sheet, retained in this repository as `assets/attachments/Review1.pdf`; the statement below is its wording.
The two groups are not isomorphic.

::: pf

::: {.pf-step #s1}

The multiplicative group $\QQ^*$ is countable.

::: pf-proof

$\QQ$ is countable, and removing the single element $0$ preserves
countability. Hence $\QQ^*=\QQ\setminus\{0\}$ is countable.

:::

:::

::: {.pf-step #s2}

The multiplicative group $\RR^*$ is uncountable.

::: pf-proof

$\RR$ is uncountable. If $\RR^*=\RR\setminus\{0\}$ were
countable, then adjoining the one-element set $\{0\}$ would make $\RR$
countable, a contradiction. Thus $\RR^*$ is uncountable.

:::

:::

::: {.pf-step #s3}

Therefore no group isomorphism can exist.

::: pf-proof

A group isomorphism is, in particular, a bijection of the underlying sets.
Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} show that the two underlying sets have different
cardinalities. Hence
$$
\boxed{\QQ^*\not\cong\RR^*.}
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
