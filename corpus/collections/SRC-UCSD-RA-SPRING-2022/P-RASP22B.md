---
schema: qual/card@1
id: P-RASP22B
kind: problem
title: 'Bounded sequence with vanishing local integrals against $L^1$ functions'
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
  note: Checked against Problem 2 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/SP22-240ABC-RealAnalysis.pdf,
    Problem 2: (f_n) Lebesgue measurable on [0,1], |f_n| <= C almost everywhere for all n,
    lim_n int_0^a f_n = 0 for every a in (0,1), prove lim_n int_0^1 g f_n = 0 for every g in L^1.
    The card's statement is that problem verbatim. The paper prints the limit as n -> 0, which is a
    typo for n -> infinity; the card has the integral, not the typo.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the derivation of the full
    integral from the hypothesis by the epsilon-times-length estimate and a limsup, including the
    degenerate case C = 0; the passage to arbitrary intervals, with the endpoint cases a = 0 and
    b = 1 routed through the hypothesis or the derived limit; linearity for step functions; density
    of step functions in L^1 as the approximation used; and the final triangle inequality with the
    domination |(g - s) f_n| <= C|g - s|. No retained published solution covers this problem.
---

::: {.problem}
Let $(f_n)_{n \in \NN}$ be a sequence of Lebesgue measurable functions defined on $[0,1]$.
Assume there is a $C > 0$ such that $\abs{f_n(x)} \leq C$ for almost every $x \in [0,1]$ and every $n$, and assume that $\lim_{n \to \infty} \int_0^a f_n(x)\,dx = 0$ for every $a \in (0,1)$.
Prove that
$$
\lim_{n \to \infty} \int_0^1 g(x) f_n(x)\,dx = 0
$$
for every function $g \in L^1([0,1])$.
:::


::: {.solution}
This is Problem 2 of the UCSD real-analysis qualifying exam of Spring 2022 (`assets/attachments/SP22-240ABC-RealAnalysis.pdf`), printed with an evident typo in the limit index, $n\to0$ for $n\to\infty$. No published solution set is transcribed: the argument is the card's own, and it is the standard density-of-step-functions argument.

::: pf

::: {.pf-step #full}
$\int_{0}^{1}f_{n}\to0$.

::: pf-proof
Let $a\in(0,1)$. Since $\abs{f_{n}}\leq C$ almost everywhere,
$$\abs{\int_{0}^{1}f_{n}}\leq\abs{\int_{0}^{a}f_{n}}+\int_{a}^{1}\abs{f_{n}}\leq\abs{\int_{0}^{a}f_{n}}+C(1-a).$$
Taking $n\to\infty$ makes the first term tend to $0$ by hypothesis, so $\limsup_{n}\abs{\int_{0}^{1}f_{n}}\leq C(1-a)$, and letting $a\uparrow1$ gives the claim. For $C=0$ the conclusion is immediate throughout, so assume $C>0$.
:::
:::

::: {.pf-step #intervals}
For every interval $I\subset[0,1]$ with endpoints $0\leq a<b\leq1$, $\int_{a}^{b}f_{n}\to0$.

::: pf-proof
For $0<a<b<1$,
$$\int_{a}^{b}f_{n}=\int_{0}^{b}f_{n}-\int_{0}^{a}f_{n}\longrightarrow0-0=0$$
by hypothesis. If $b=1$ the same computation uses step [](#full){.pf-ref} for the first term; if $a=0$ the integral is $\int_{0}^{b}f_{n}$, which is the hypothesis or step [](#full){.pf-ref} again; and if $a=b$ it vanishes identically.
:::
:::

::: {.pf-step #step}
For every step function $s=\sum_{k=1}^{m}c_{k}\mathbf{1}_{I_{k}}$ on $[0,1]$, $\int_{0}^{1}sf_{n}\to0$.

::: pf-proof
By linearity $\int_{0}^{1}sf_{n}=\sum_{k}c_{k}\int_{I_{k}}f_{n}$, and each summand tends to $0$ by step [](#intervals){.pf-ref}; a finite sum of null sequences is null.
:::
:::

::: {.pf-step #density}
For every $g\in L^{1}([0,1])$ and $\varepsilon>0$ there is a step function $s$ with $\norm{g-s}_{1}<\varepsilon/(2C)$.

::: pf-proof
Step functions are dense in $L^{1}([0,1])$: measurable functions are approximated in $L^{1}$ by simple functions, and each simple function is a finite linear combination of indicators of measurable sets, which are approximated by finite unions of intervals. This gives the required $s$ for any positive bound, in particular $\varepsilon/(2C)$.
:::
:::

::: {.pf-step #conclusion}
$\int_{0}^{1}gf_{n}\to0$ for every $g\in L^{1}([0,1])$.

::: pf-proof
Let $\varepsilon>0$ and let $s$ be the step function of step [](#density){.pf-ref}. For every $n$,
$$\abs{\int_{0}^{1}(g-s)f_{n}}\leq\int_{0}^{1}\abs{g-s}\,\abs{f_{n}}\leq C\norm{g-s}_{1}<\frac{\varepsilon}{2},$$
using $\abs{f_{n}}\leq C$ almost everywhere and the monotonicity of the integral. By step [](#step){.pf-ref} there is $N$ with $\abs{\int_{0}^{1}sf_{n}}<\varepsilon/2$ for $n\geq N$. Then for $n\geq N$,
$$\abs{\int_{0}^{1}gf_{n}}\leq\abs{\int_{0}^{1}(g-s)f_{n}}+\abs{\int_{0}^{1}sf_{n}}<\varepsilon,$$
so $\int_{0}^{1}gf_{n}\to0$.
:::
:::
:::

:::
