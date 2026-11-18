---
schema: qual/card@1
id: P-JHUMAY06ANG
kind: problem
title: 'Separating $L^1$ and $L^2$ on $\RR$ and $(0,1)$'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, May 2006, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Both examples were already correct; what the prose asserted in words ("(1+|x|)^{-3/2} is integrable on R", "x^{-3/4} is not integrable at infinity") is now computed, with 4 and 8((1+R)^{1/4}-1) and 4 - 4 epsilon^{1/4} and 2 epsilon^{-1/2} - 2 displayed, so the convergence and divergence are read off the antiderivatives rather than asserted. No retained solution set covers the exercise: the collection's provenance is the JHU examination papers and the card records only the statement, so the card says the argument is its own. No statement repair.
---

::: {.problem}
(a) Give a function in $L^2(\RR)$ that is not in $L^1(\RR)$.

(b) Give a function in $L^1((0,1))$ that is not in $L^2((0,1))$.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is the JHU examination papers, and the card records only the problem statement. The argument is the card's own, and the two examples are the ones the card had.

::: pf

::: {.pf-step #parta}
$f(x)=(1+\abs{x})^{-3/4}$ lies in $L^2(\RR)$ and not in $L^1(\RR)$.

::: pf-proof
$\abs{f(x)}^2=(1+\abs{x})^{-3/2}$, and
$$
\int_\RR(1+\abs{x})^{-3/2}\,dx=2\int_0^\infty(1+x)^{-3/2}\,dx=2\Big[-2(1+x)^{-1/2}\Big]_0^\infty=2\cdot2=4<\infty,
$$
the factor $2$ because the integrand is even. So $f\in L^2(\RR)$.
For $L^1$,
$$
\int_{-R}^{R}(1+\abs{x})^{-3/4}\,dx=2\int_0^R(1+x)^{-3/4}\,dx=2\Big[4(1+x)^{1/4}\Big]_0^R=8\bigl((1+R)^{1/4}-1\bigr)\to\infty,
$$
so $f$ is not integrable on $\RR$ and $f\notin L^1(\RR)$.
:::

:::

::: {.pf-step #partb}
$g(x)=x^{-3/4}$ on $(0,1)$ lies in $L^1((0,1))$ and not in $L^2((0,1))$.

::: pf-proof
$\int_\varepsilon^1x^{-3/4}\,dx=\bigl[4x^{1/4}\bigr]_\varepsilon^1=4-4\varepsilon^{1/4}\to4$ as $\varepsilon\to0^+$, and $g\ge0$, so $g\in L^1((0,1))$ with $\int_0^1g=4$. On the other hand $\abs{g}^2=x^{-3/2}$ and $\int_\varepsilon^1x^{-3/2}\,dx=\bigl[-2x^{-1/2}\bigr]_\varepsilon^1=2\varepsilon^{-1/2}-2\to\infty$, so $g\notin L^2((0,1))$.
:::

:::

::: {.pf-step}
The two examples answer (a) and (b) as asked.

::: pf-proof
Step [](#parta){.pf-ref} exhibits $f\in L^2(\RR)\setminus L^1(\RR)$ and step [](#partb){.pf-ref} exhibits $g\in L^1((0,1))\setminus L^2((0,1))$.
:::

:::

:::
:::
