---
schema: qual/card@1
id: P-OPZJH
kind: problem
title: $(\FF_9)^\times$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What is the structure of the multiplicative group $(\FF_9)^\times$?
Construct $\FF_9$ as a quotient ring and find an explicit primitive generator of $(\FF_9)^\times$.
:::

::: {.solution}

::: pf

::: pf-step

$\FF_9\cong\FF_3[x]/(x^2+1)=\FF_3[i]$ with $i^2=-1=2$.

::: pf-proof

The polynomial $x^2+1\in\FF_3[x]$ takes the values $1,2,2$ at $0,1,2$, so it has no root in $\FF_3$; being of degree $2$, it is irreducible. The quotient is therefore a field with $3^2=9$ elements.

:::

:::

::: pf-step

$(\FF_9)^\times\cong C_8$.

::: pf-proof

It has order $8$, and the multiplicative group of a finite field is cyclic.

:::

:::

::: pf-step

$(\FF_9)^\times=\boxed{\langle1+i\rangle}$.

::: pf-proof

Let $\alpha=1+i$. Then
$$
\alpha^2=1+2i+i^2=2i,\qquad \alpha^4=(2i)^2=4i^2=2\neq1,\qquad \alpha^8=2^2=1.
$$
The order of $\alpha$ divides $8$ but not $4$, so it is $8$.

:::

:::

:::

:::
