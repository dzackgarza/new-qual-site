---
schema: qual/card@1
id: P-ALGPAN11-11
kind: problem
title: When x maps to a x a^{-2} is a homomorphism
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
---

::: {.problem}
For a fixed element $a$ of a group $G$, determine when the map $x\mapsto axa^{-2}$ from $G$ to itself is a homomorphism.

![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-11.png)
:::

::: {.solution}
The map
\[
\varphi(x)=axa^{-2}
\]
is a homomorphism if and only if $\boxed{a=e}$.

<1>1. A homomorphism forces $a=e$.
::: {.proof}
Every group homomorphism sends the identity to the identity.
But
\[
\varphi(e)=aea^{-2}=a^{-1}.
\]
Hence $a^{-1}=e$, so $a=e$.
:::

<1>2. The condition is sufficient.
::: {.proof}
If $a=e$, then $\varphi(x)=x$ for all $x$, so $\varphi$ is the identity homomorphism.
:::
:::
