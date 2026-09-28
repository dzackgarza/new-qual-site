---
schema: qual/card@1
id: P-JHUMAY06ANK
kind: problem
title: "Boundedness of a weakly convergent sequence in $L^2([0,1])$"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared May 2006 problem 11 on PDF page 41 and restored the ordinary limsup notation."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Handled zero vectors in the norm-attainment argument, checked conjugation against the chosen inner-product convention and verified the hypotheses for uniform boundedness."
---

::: {.problem}
Suppose $f_n\in L^2([0,1])$ converges weakly to $f\in L^2([0,1])$. Prove that $\limsup_{n\to\infty}\|f_n\|_2<\infty$, or give a counterexample.
:::

::: {.solution}
Let $H=L^2([0,1])$ with $\langle g,h\rangle=\int_0^1g\bar h$, and for each $n$ let $\phi_n(g)\da\langle g,f_n\rangle$. The statement holds: $\sup_n\norm{f_n}_2<\infty$.

<1>1. Each $\phi_n$ is a bounded linear functional with $\norm{\phi_n}=\norm{f_n}_2$.

::: {.proof}
The Cauchy--Schwarz inequality gives $\abs{\phi_n(g)}\le\norm g_2\norm{f_n}_2$. If $f_n\neq0$, the unit vector $g=f_n/\norm{f_n}_2$ attains the bound; if $f_n=0$, both sides are $0$.
:::

<1>2. For each $g\in H$, $\sup_n\abs{\phi_n(g)}<\infty$.

::: {.proof}
Weak convergence gives $\langle f_n,g\rangle\to\langle f,g\rangle$; conjugating, $\phi_n(g)\to\langle g,f\rangle$, and a convergent sequence of complex numbers is bounded.
:::

<1>3. Q.E.D.

::: {.proof}
$H$ is complete, so by steps <1>1 and <1>2 the uniform boundedness principle [@Fol13] gives $\sup_n\norm{\phi_n}<\infty$. By step <1>1 this is $\sup_n\norm{f_n}_2$, which bounds $\limsup_n\norm{f_n}_2$.
:::
:::
