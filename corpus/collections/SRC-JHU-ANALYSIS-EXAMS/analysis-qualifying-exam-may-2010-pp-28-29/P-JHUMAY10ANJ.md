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
Let $E\subset\mathbb R$ be measurable.

(a) If $|E|<\infty$, prove that
\[
F(x)=\int_{\mathbb R}\chi_E(y)\chi_E(y-x)\,dy
\]
is continuous.

(b) If $|E|>0$, possibly infinite, prove that $E-E$ contains an interval $(-\varepsilon,\varepsilon)$ for some $\varepsilon>0$.
:::

::: {.solution}
<1>1. Continuity when $E$ has finite measure.
::: {.proof}
Since $|E|<\infty$, one has $\chi_E\in L^2(\mathbb R)$. For $h\in\mathbb R$,
\[
\begin{aligned}
|F(x+h)-F(x)|
&=\left|\int \chi_E(y)\bigl(\chi_E(y-x-h)-\chi_E(y-x)\bigr)\,dy\right|\\
&\le \|\chi_E\|_2\,\|\chi_E(\cdot-h)-\chi_E\|_2.
\end{aligned}
\]
The right-hand side is independent of $x$ and tends to $0$ as $h\to0$ by continuity of translations in $L^2(\mathbb R)$. Thus $F$ is uniformly continuous.
:::

<1>2. Positive-measure sets have a neighborhood of zero in the difference set.
::: {.proof}
Assume $|E|>0$. Because Lebesgue measure is sigma-finite, there exists $R>0$ such that
\[
A=E\cap[-R,R]
\]
has finite positive measure. Apply part (a) to $A$ and define
\[
F_A(x)=\int\chi_A(y)\chi_A(y-x)\,dy.
\]
Then
\[
F_A(0)=|A|>0.
\]
By continuity, there exists $\varepsilon>0$ such that
\[
F_A(x)>0
\qquad(|x|<\varepsilon).
\]
If $F_A(x)>0$, then the set of $y$ with
\[
y\in A,
\qquad
y-x\in A
\]
has positive measure and is therefore nonempty. For such a $y$,
\[
x=y-(y-x)\in A-A\subset E-E.
\]
Hence
\[
(-\varepsilon,\varepsilon)\subset E-E.
\]
:::
:::
