---
schema: qual/card@1
id: P-CALCPT3-24
kind: problem
title: "Events with $0<P(A)=P(B)=P(A\\cap B)<1$"
classification:
  areas: [prelim]
  topics: [Probability]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 24 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
---

::: {.problem}
If $A$ and $B$ are events in a probability space such that $0<P(A)=P(B)=P(A\cap B)<1$, which of the following CANNOT be true?

(A) $A$ and $B$ are independent.
(B) $A$ is a proper subset of $B$.
(C) $A\ne B$
(D) $A\cap B=A\cup B$
(E) $P(A)P(B)<P(A\cap B)$
:::

::: {.solution}
Write $p=P(A)=P(B)=P(A\cap B)$, so that $0<p<1$.

::: pf

::: {.pf-step #not-independent}
$A$ and $B$ are not independent.

::: pf-proof
Independence would mean $P(A\cap B)=P(A)P(B)$, that is, $p=p^2$.
The only solutions are $p=0$ and $p=1$, both excluded.
:::

:::

::: {.pf-step #others-possible}
Each of (B), (C), (D), and (E) can be true.

::: pf-proof
Since $0<p<1$, we have $p^2<p$, so (E) holds in every such space.
For (D), take $[0,1]$ with Lebesgue measure and $A=B=[0,\frac12]$; then $A\cap B=A\cup B$ and all three probabilities are $\frac12$.
For (B) and (C), take the same space with $A=[0,\frac12)$ and $B=[0,\frac12]$; then $A$ is a proper subset of $B$, so $A\ne B$, and $P(A)=P(B)=P(A\cap B)=\frac12$ because the point $\frac12$ has probability $0$.
:::

:::

::: pf-step
The statement that cannot be true is $\boxed{\text{(A)}}$.

::: pf-proof
Step [](#not-independent){.pf-ref} rules out (A), and step [](#others-possible){.pf-ref} shows every other choice can occur.
:::

:::

:::

:::
