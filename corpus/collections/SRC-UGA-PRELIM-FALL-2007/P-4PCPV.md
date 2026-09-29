---
schema: qual/card@1
id: P-4PCPV
kind: problem
title: Evaluating and negating compound logical statements
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
  date: 2026-08-29
---

::: {.problem}
a. Suppose $A$ and $B$ are false statements.
Is the statement $$(A \implies B) \implies (A \vee B)$$ true or false?
("$\vee$" denotes "or.")

b. Give the negation of the statement

If all blockoids are split and some blockoid is nontrivial, then there is a short blockoid.
:::

::: {.solution}
**Part (a).**

::: pf

::: pf-step
$A \implies B$ is true.

::: pf-proof
$A$ is false, and a false antecedent makes an implication true.
:::

:::

::: pf-step
$A \vee B$ is false.

::: pf-proof
both $A$ and $B$ are false.
:::

:::

::: {.pf-step #p1-3}
Hence $(A \implies B) \implies (A \vee B)$ is $\text{true} \implies \text{false}$, which is false.

::: pf-proof
an implication with a true antecedent and false consequent is false.
:::

:::

::: pf-qed
Step [](#p1-3){.pf-ref}.
:::

:::

**Part (b).**

::: pf

::: {.pf-step #p2-1}
The statement is of the form $P \implies Q$, where $P = (\text{all blockoids are split}) \wedge (\text{some blockoid is nontrivial})$ and $Q = (\text{there is a short blockoid})$.

::: pf-proof
parse the statement.
:::

:::

::: {.pf-step #p2-2}
The negation of $P \implies Q$ is $P \wedge \neg Q$.

::: pf-proof
$\neg(P \implies Q) \equiv P \wedge \neg Q$.
:::

:::

::: {.pf-step #p2-3}
Hence the negation is: "All blockoids are split, and some blockoid is nontrivial, and there is no short blockoid."

::: pf-proof
Steps [](#p2-1){.pf-ref} and [](#p2-2){.pf-ref}.
:::

:::

::: pf-qed
Step [](#p2-3){.pf-ref}.
:::

:::
:::
