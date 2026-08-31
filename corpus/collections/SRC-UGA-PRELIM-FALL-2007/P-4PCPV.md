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

<1>1. $A \implies B$ is true.
::: {.proof}
$A$ is false, and a false antecedent makes an implication true.
:::

<1>2. $A \vee B$ is false.
::: {.proof}
both $A$ and $B$ are false.
:::

<1>3. Hence $(A \implies B) \implies (A \vee B)$ is $\text{true} \implies \text{false}$, which is false.
::: {.proof}
an implication with a true antecedent and false consequent is false.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3.
:::

**Part (b).**

<1>1. The statement is of the form $P \implies Q$, where $P = (\text{all blockoids are split}) \wedge (\text{some blockoid is nontrivial})$ and $Q = (\text{there is a short blockoid})$.
::: {.proof}
parse the statement.
:::

<1>2. The negation of $P \implies Q$ is $P \wedge \neg Q$.
::: {.proof}
$\neg(P \implies Q) \equiv P \wedge \neg Q$.
:::

<1>3. Hence the negation is: "All blockoids are split, and some blockoid is nontrivial, and there is no short blockoid."
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3.
:::
:::
