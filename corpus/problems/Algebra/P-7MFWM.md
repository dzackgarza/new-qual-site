---
schema: qual/card@1
id: P-7MFWM
kind: problem
title: If $\exp(A)=B\in\SL_n(\RR)$, must $A\in\SL_n(\RR)$?
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Determinants
  - Trace
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

::: problem
Say we can find a matrix $A \in M_n(\mathbb{R})$ such that $\exp(A) = B$ for $B \in \operatorname{SL}_n(\mathbb{R})$.
Does $A$ also have to be in $\operatorname{SL}_n(\mathbb{R})$?
Does $A$ have to satisfy $\operatorname{tr}(A) = 0$ (i.e. $A \in \mathfrak{sl}_n(\mathbb{R})$)?
:::

::: solution
For every real matrix $A$,
\[
\det(e^A)=e^{\operatorname{tr}A}.
\]
If $e^A=B\in\SL_n(\RR)$, then
\[
1=\det B=e^{\operatorname{tr}A}.
\]
Because $\operatorname{tr}A\in\RR$, this implies
\[
\operatorname{tr}A=0.
\]
Hence
\[
A\in\mathfrak{sl}_n(\RR).
\]

However, $A$ need not lie in the group $\SL_n(\RR)$: that would require $\det A=1$. The zero matrix already gives a counterexample,
\[
e^0=I_n\in\SL_n(\RR),
\qquad
\det0=0.
\]
Thus
\[
\boxed{e^A\in\SL_n(\RR)\implies A\in\mathfrak{sl}_n(\RR),
\quad\text{but not necessarily }A\in\SL_n(\RR).}
\]
:::
