---
schema: qual/card@1
id: E-JCJOW
kind: problem
title: Choice axiom and nonempty cartesian products
classification:
  areas:
  - topology
  topics:
  - Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that the choice axiom is equivalent to the statement that for any indexed family $\ts{A_\alpha}_{\alpha \in J}$ of nonempty sets, with $J \neq 0$, the cartesian product

$$
\prod_{\alpha \in J} A_\alpha
$$

is not empty.
:::

::: {.solution}
Assume the axiom of choice. Given a family $\{A_\alpha\}_{\alpha\in J}$ of nonempty sets, choice supplies a function $c:J\to\bigcup_\alpha A_\alpha$ with
\[
c(\alpha)\in A_\alpha
\]
for every $\alpha$. This is exactly an element $(c(\alpha))_{\alpha\in J}$ of the Cartesian product, so the product is nonempty.

Conversely, assume every product of a family of nonempty sets is nonempty. Given any family $\{A_\alpha\}_{\alpha\in J}$ of nonempty sets, choose an element
\[
(a_\alpha)_{\alpha\in J}\in\prod_{\alpha\in J}A_\alpha.
\]
Then $c(\alpha)=a_\alpha$ is a choice function. Hence the product-nonemptiness statement is equivalent to the axiom of choice.
:::
