---
schema: qual/card@1
id: P-RASP22C
kind: problem
title: "Convergence of Laplace-type averaged functions"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The two applications of Tonelli are now separated: one in the order dx dt to see that the sections are integrable for almost every t, one in the order dt dx to see that the section t -> f(t,x) is integrable for almost every x, which is what the pointwise convergence needs. The substitution t = n lambda is performed as a substitution rule rather than asserted, measurability of g_n is stated, and the factor e^{-t/n} <= 1 is used explicitly in both estimates. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $f \in L^1((0,\infty) \times \RR)$ and for $n \in \NN$ define $g_n : \RR \to \RR$ by
$$
g_n(x) = \int_0^\infty e^{-\lambda} f(n\lambda, x)\,d\lambda.
$$
Prove that $g_n$ converges to $0$ almost everywhere and in $L^1(\RR)$.
:::


::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #substitution}
$g_n(x)=\dfrac1n\displaystyle\int_0^\infty e^{-t/n}f(t,x)\,dt$ for every $n$ and almost every $x$.

::: pf-proof
The change of variables $t=n\lambda$, $d\lambda=dt/n$, gives $\int_0^\infty e^{-\lambda}f(n\lambda,x)d\lambda=\frac1n\int_0^\infty e^{-t/n}f(t,x)dt$ for each $x$, by the substitution rule for the Lebesgue integral; no integrability is needed for the identity, but the right side may be infinite.
:::

:::

::: {.pf-step #sections}
For almost every $x\in\RR$ the function $t\mapsto f(t,x)$ lies in $L^1(0,\infty)$, and then $\abs{g_n(x)}\le\frac1n\int_0^\infty\abs{f(t,x)}dt$.

::: pf-proof
The function $(t,x)\mapsto\abs{f(t,x)}$ is nonnegative and measurable with finite integral $\norm{f}_{L^1}$ over $(0,\infty)\times\RR$. Tonelli's theorem applied in the order $dx$ first gives
$$
\int_0^\infty\left(\int_\RR\abs{f(t,x)}\,dx\right)dt=\norm{f}_{L^1}<\infty,
$$
so the inner integral is finite for almost every $t$; applying Tonelli in the other order,
$$
\int_\RR\left(\int_0^\infty\abs{f(t,x)}\,dt\right)dx=\norm{f}_{L^1}<\infty,
$$
shows that the section $t\mapsto f(t,x)$ is integrable for almost every $x$. For such an $x$, step [](#substitution){.pf-ref} and $\abs{e^{-t/n}}=e^{-t/n}\le1$ give $\abs{g_n(x)}\le\frac1n\int_0^\infty\abs{f(t,x)}dt$.
:::

:::

::: {.pf-step #pointwise}
$g_n(x)\to0$ for almost every $x$.

::: pf-proof
Fix $x$ as in step [](#sections){.pf-ref}, with $C_x=\int_0^\infty\abs{f(t,x)}dt<\infty$. Then $\abs{g_n(x)}\le C_x/n\to0$.
:::

:::

::: {.pf-step #l1}
$\norm{g_n}_{L^1(\RR)}\le\dfrac1n\norm{f}_{L^1((0,\infty)\times\RR)}\to0$.

::: pf-proof
Each $g_n$ is measurable, being an integral depending measurably on $x$, and by Tonelli and step [](#sections){.pf-ref}
$$
\int_\RR\abs{g_n(x)}dx\le\frac1n\int_\RR\int_0^\infty e^{-t/n}\abs{f(t,x)}\,dt\,dx\le\frac1n\int_0^\infty\int_\RR\abs{f(t,x)}\,dx\,dt=\frac1n\norm{f}_{L^1},
$$
where the last step is Tonelli for the nonnegative measurable function $\abs f$ and the middle inequality uses $e^{-t/n}\le1$. So $g_n\in L^1(\RR)$ and its norm tends to $0$.
:::

:::

::: {.pf-step}
$g_n\to0$ almost everywhere and in $L^1(\RR)$.

::: pf-proof
Steps [](#pointwise){.pf-ref} and [](#l1){.pf-ref} are the two assertions.
:::

:::

:::
:::
