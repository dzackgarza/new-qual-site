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

<1>1. Negation: $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$.
::: {.proof}
the only way an implication is false is when the hypothesis holds and the conclusion fails.
:::

<1>2. Hence the negation is: "There exists a purple apple, and some lemon is not pink."
::: {.proof}
<1>1, translating $\neg Q$ as "not all lemons are pink".
:::

<1>3. Converse: $Q \Rightarrow P$.
::: {.proof}
the converse swaps hypothesis and conclusion.
:::

<1>4. Hence the converse is: "If all lemons are pink, then there exists a purple apple."
::: {.proof}
<1>3.
:::

<1>5. Contrapositive: $\neg Q \Rightarrow \neg P$.
::: {.proof}
the contrapositive negates and swaps.
:::

<1>6. Hence the contrapositive is: "If some lemon is not pink, then there is no purple apple."
::: {.proof}
<1>5.
:::

**Part (b).**

<1>1. The contrapositive is logically equivalent to the original statement.
::: {.proof}
$P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$.
:::

<1>2. Hence the contrapositive must be true.
::: {.proof}
<1>1 and the assumption that the statement is true.
:::

<1>3. The converse is not necessarily true.
::: {.proof}
$Q \Rightarrow P$ is not equivalent to $P \Rightarrow Q$ (e.g. $P$ false, $Q$ true makes $P \Rightarrow Q$ true but $Q \Rightarrow P$ false).
:::

<1>4. The negation is false.
::: {.proof}
the negation is the opposite of the true statement.
:::

<1>5. Q.E.D.
::: {.proof}
<1>2, <1>3, <1>4.
:::
:::
