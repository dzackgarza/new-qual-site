---
schema: qual/card@1
id: P-JHUMAY10ANJ
kind: problem
title: "Continuity of overlap measure and Steinhaus' theorem"
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the JHU Analysis Qualifying Exam, May 2010, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $E\subset\RR$ be measurable.

(a) If $\setmeasure{E}<\infty$, prove that
$$
F(x)=\int_{\RR}\chi_E(y)\chi_E(y-x)\,dy
$$
is continuous.

(b) If $\setmeasure{E}>0$, possibly infinite, prove that $E-E$ contains an interval $(-\varepsilon,\varepsilon)$ for some $\varepsilon>0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Continuity when $E$ has finite measure.

::: pf-proof

Since $\setmeasure{E}<\infty$, one has $\chi_E\in L^2(\RR)$. For $h\in\RR$,
$$
\begin{aligned}
\abs{F(x+h)-F(x)}
&=\abs{\int \chi_E(y)\bigl(\chi_E(y-x-h)-\chi_E(y-x)\bigr)\,dy}\\
&\le \norm{\chi_E}_2\,\norm{\chi_E(\cdot-h)-\chi_E}_2.
\end{aligned}
$$
The inequality is [[FF-4XBYG|Cauchy--Schwarz in $L^2$]]. The right-hand side is independent of $x$ and tends to $0$ as $h\to0$ by [[T-BFOJT|continuity of translation in $L^p$]]. Thus $F$ is uniformly continuous.

:::

:::

::: {.pf-step #s2}

Positive-measure sets have a neighborhood of zero in the difference set.

::: pf-proof

Assume $\setmeasure{E}>0$. Because Lebesgue measure is sigma-finite, there exists $R>0$ such that
$$
A=E\cap[-R,R]
$$
has finite positive measure. Apply part (a) to $A$ and define
$$
F_A(x)=\int\chi_A(y)\chi_A(y-x)\,dy.
$$
Then
$$
F_A(0)=\setmeasure{A}>0.
$$
By continuity, there exists $\varepsilon>0$ such that
$$
F_A(x)>0
\qquad(\abs{x}<\varepsilon).
$$
If $F_A(x)>0$, then the set of $y$ with
$$
y\in A,
\qquad
y-x\in A
$$
has positive measure and is therefore nonempty. For such a $y$,
$$
x=y-(y-x)\in A-A\subset E-E.
$$
Hence
$$
(-\varepsilon,\varepsilon)\subset E-E.
$$

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), and step [](#s2){.pf-ref} proves part (b).

:::

:::

:::
