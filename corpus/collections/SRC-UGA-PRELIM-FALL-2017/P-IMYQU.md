---
schema: qual/card@1
id: P-IMYQU
kind: problem
title: $\int_0^\infty x^n e^{-x}\,dx = n!$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Improper Integrals
  - Integration by Parts
  - Induction
relations: []
review: draft
---

::: {.problem}
Prove, for every nonnegative integer $n$, that
$$
\int_0^\infty x^ne^{-x}\,dx=n!.
$$
:::

::: {.solution}
For $n=0$,
$$
\int_0^\infty e^{-x}\,dx=1=0!.
$$

For the inductive step, integration by parts gives
$$
\begin{aligned}
\int_0^\infty x^ne^{-x}\,dx
&= -x^ne^{-x}\evalfrom_0^\infty - \int_0^\infty -nx^{n-1}e^{-x}\,dx \\
&= -x^ne^{-x}\evalfrom_0^\infty + n \int_0^\infty x^{n-1}e^{-x}\,dx \\
&\equalsbecause{I.H.} -x^ne^{-x}\evalfrom_0^\infty + n (n-1)! \\
&\equalsbecause{L.H.$\times n$} 0 + n(n-1)! = n!. \qed
\end{aligned}
$$
:::
