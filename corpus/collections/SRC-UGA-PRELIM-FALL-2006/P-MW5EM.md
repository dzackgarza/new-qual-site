---
schema: qual/card@1
id: P-MW5EM
kind: problem
title: Negation, converse, and contrapositive of "if there exists a purple apple,
  then all lemons are pink"
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Consider the statement:

"If there exists a purple apple, then all lemons are pink."

a. Give the negation, the converse, and the contrapositive of the statement above.
b. Assuming the statement is true, which (ones, if any) of the statements formulated in part (A) must necessarily be true?
:::

::: {.solution}
Let $P$ = "there exists a purple apple" and $Q$ = "all lemons are pink". The statement is $P \Rightarrow Q$.

**Part (a).**

::: pf

::: {.pf-step #p1-1}
Negation: $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$.

::: pf-proof
the only way an implication is false is when the hypothesis holds and the conclusion fails.
:::

:::

::: pf-step
Hence the negation is: "There exists a purple apple, and some lemon is not pink."

::: pf-proof
Step [](#p1-1){.pf-ref}, translating $\neg Q$ as "not all lemons are pink".
:::

:::

::: {.pf-step #p1-3}
Converse: $Q \Rightarrow P$.

::: pf-proof
the converse swaps hypothesis and conclusion.
:::

:::

::: pf-step
Hence the converse is: "If all lemons are pink, then there exists a purple apple."

::: pf-proof
Step [](#p1-3){.pf-ref}.
:::

:::

::: {.pf-step #p1-5}
Contrapositive: $\neg Q \Rightarrow \neg P$.

::: pf-proof
the contrapositive negates and swaps.
:::

:::

::: pf-step
Hence the contrapositive is: "If some lemon is not pink, then there is no purple apple."

::: pf-proof
Step [](#p1-5){.pf-ref}.
:::

:::

:::

**Part (b).**

::: pf

::: {.pf-step #p2-1}
The contrapositive is logically equivalent to the original statement.

::: pf-proof
$P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$.
:::

:::

::: {.pf-step #p2-2}
Hence the contrapositive must be true.

::: pf-proof
Step [](#p2-1){.pf-ref} and the assumption that the statement is true.
:::

:::

::: {.pf-step #p2-3}
The converse is not necessarily true.

::: pf-proof
$Q \Rightarrow P$ is not equivalent to $P \Rightarrow Q$ (e.g. $P$ false, $Q$ true makes $P \Rightarrow Q$ true but $Q \Rightarrow P$ false).
:::

:::

::: {.pf-step #p2-4}
The negation is false.

::: pf-proof
the negation is the opposite of the true statement.
:::

:::

::: pf-qed
Steps [](#p2-2){.pf-ref}, [](#p2-3){.pf-ref}, [](#p2-4){.pf-ref}.
:::

:::
:::
