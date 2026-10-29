---
schema: qual/card@1
id: P-CALCPT3-26
kind: problem
title: "A vector orthogonal to $\\mathbf i+\\mathbf j-\\mathbf k$"
classification:
  areas: [prelim]
  topics: [Orthogonality]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 26 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
---

::: {.problem}
Let $\mathbf i=(1,0,0)$, $\mathbf j=(0,1,0)$, and $\mathbf k=(0,0,1)$.
The vectors $\mathbf v_1$ and $\mathbf v_2$ are orthogonal if $\mathbf v_1=\mathbf i+\mathbf j-\mathbf k$ and $\mathbf v_2=$

(A) $\mathbf i+\mathbf j-\mathbf k$
(B) $\mathbf i-\mathbf j+\mathbf k$
(C) $\mathbf i+\mathbf k$
(D) $\mathbf j-\mathbf k$
(E) $\mathbf i+\mathbf j$
:::

::: {.solution}
Two vectors are orthogonal exactly when their dot product is $0$, and $\mathbf v_1=(1,1,-1)$.

::: pf

::: {.pf-step #dot-products}
The dot products of $\mathbf v_1$ with the choices (A) through (E) are $3$, $-1$, $0$, $2$, and $2$.

::: pf-proof
With $(1,1,-1)$: choice (A) $(1,1,-1)$ gives $1+1+1=3$; (B) $(1,-1,1)$ gives $1-1-1=-1$; (C) $(1,0,1)$ gives $1+0-1=0$; (D) $(0,1,-1)$ gives $0+1+1=2$; (E) $(1,1,0)$ gives $1+1+0=2$.
:::

:::

::: pf-step
$\mathbf v_2=\boxed{\mathbf i+\mathbf k}$, choice (C).

::: pf-proof
By step [](#dot-products){.pf-ref}, (C) is the only choice with dot product $0$.
:::

:::

:::

:::
