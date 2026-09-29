---
schema: qual/card@1
id: P-5XCMC
kind: problem
title: $\forall x(P\Rightarrow Q)$ implies $(\forall x\,P)\Rightarrow(\forall x\,Q)$,
  but not conversely
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $P(x)$ and $Q(x)$ be open sentences containing the variable $x$, and consider the following statements.
$$A: \forall x, (P(x) \Rightarrow Q(x)) \quad \text{and} \quad B: (\forall x, P(x)) \Rightarrow (\forall x, Q(x))$$

a. Prove that $A \Rightarrow B$.
b. Give an example of open sentences $P(x)$ and $Q(x)$ to show that $B \Rightarrow A$ need not be true.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
Assume $A$, and suppose $\forall x\,P(x)$.
:::

::: {.pf-step #s2}
Then $\forall x\,Q(x)$.

::: pf-proof
Let $x$ be arbitrary. From $\forall x\,P(x)$ we have $P(x)$. From $A$ we have $P(x)\Rightarrow Q(x)$. Therefore $Q(x)$. Since $x$ was arbitrary, $\forall x\,Q(x)$.
:::

:::

::: pf-step
Hence $A\Rightarrow B$.

::: pf-proof
Under the assumption $A$, steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove the implication
\[
(\forall x\,P(x))\Rightarrow(\forall x\,Q(x)),
\]
which is exactly $B$.
:::

:::

::: pf-step
The converse can fail. Take the universe to be $\mathbb Z$, and define
\[
P(x): x=0,
\qquad
Q(x): x=1.
\]
:::

::: pf-step
For these predicates, $B$ is true but $A$ is false.

::: pf-proof
The antecedent $\forall x\,P(x)$ of $B$ is false, so $B$ is true. But at $x=0$, the statement $P(0)$ is true and $Q(0)$ is false; therefore $P(0)\Rightarrow Q(0)$ is false, so $A$ is false.
:::

:::

:::
:::
