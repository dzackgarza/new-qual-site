---
schema: qual/card@1
id: P-CWZF3
kind: problem
title: $R/(p)$ is a field when $(p)$ is prime in a PID
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $R$ be a PID and let $(p)$ be a prime ideal of $R$. Prove that $R/(p)$ is a field.
:::


::: {.solution}
Let $(p)$ be a prime ideal in the PID $R$. Since every nonzero prime ideal in a PID is maximal, $(p)$ is maximal.

<1>1. Let $x+(p)\ne (p)$ in $R/(p)$, so $x\notin(p)$.
::: {.proof}
Because $(p)$ is maximal and $(p)\subsetneq (p,x)$, one has
\[
(p,x)=R.
\]
Hence there exist $a,b\in R$ such that
\[
ap+bx=1.
\]
Reducing modulo $(p)$ gives
\[
(b+(p))(x+(p))=1+(p).
\]
Thus every nonzero class in $R/(p)$ has a multiplicative inverse.
:::

<1>2. Therefore $R/(p)$ is a field.
::: {.proof}
A commutative ring with identity is a field exactly when every nonzero element is invertible. This holds by <1>1.
:::
:::
