---
schema: qual/card@1
id: E-SMI-8000E-NR2
kind: problem
title: Quotients of noetherian rings are noetherian
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the quotient-noetherian statement with the local 8000e PDF and extraction, Noetherian-rings problem 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Pulled an arbitrary quotient ideal back to an ideal of R, chose finite generators there, and pushed them to the quotient."
---

::: {.exercise}
If $R$ is a noetherian ring and $I$ any ideal, then $R/I$ is noetherian too.
:::


::: {.solution}
Let $\pi:R\to R/I$ be the quotient map and let $J/I$ be an arbitrary ideal
of $R/I$, where $J=\pi^{-1}(J/I)$ is the corresponding ideal of $R$ containing
$I$.

Because $R$ is noetherian, $J$ is finitely generated, say
$$
J=(a_1,\ldots,a_r).
$$
We claim that
$$
J/I=(a_1+I,\ldots,a_r+I)
$$
as an ideal of $R/I$. Indeed, if $x+I\in J/I$, write
$$
x=r_1a_1+\cdots+r_ra_r.
$$
Then
$$
x+I=(r_1+I)(a_1+I)+\cdots+(r_r+I)(a_r+I).
$$
Thus every ideal of $R/I$ is finitely generated. Hence
$$
\boxed{R/I\text{ is noetherian}.}
$$
:::
