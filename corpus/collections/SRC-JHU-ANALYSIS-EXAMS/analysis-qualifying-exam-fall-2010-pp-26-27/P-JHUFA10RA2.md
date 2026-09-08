---
schema: qual/card@1
id: P-JHUFA10RA2
kind: problem
title: Convolution of characteristic functions is continuous
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the Fall 2010 JHU analysis qualifying-exam statement preserved in this collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $E, F \subset \mathbb{R}$ be two Lebesgue-measurable subsets of $\mathbb{R}$, each of finite measure, and let $\chi_E$ and $\chi_F$ denote their respective characteristic functions.

(a) Prove that the convolution $\chi_E * \chi_F$ defined by

$$\chi_E * \chi_F(x) = \int_{\mathbb{R}} \chi_E(y) \chi_F(x - y) \, dy$$

is a continuous function of $x$.

(b) Show that as $n \to \infty$

$$n \big(\chi_E * \chi_{[0, 1/n]}\big) \longrightarrow \chi_E$$

pointwise almost everywhere.
:::

::: {.solution}
<1>1. The convolution $\chi_E*\chi_F$ is uniformly continuous.
::: {.proof}
Because $m(E),m(F)<\infty$, both characteristic functions lie in $L^2(\mathbb R)$, with
\[
\|\chi_E\|_2=m(E)^{1/2},
\qquad
\|\chi_F\|_2=m(F)^{1/2}.
\]
Let
\[
h(x)=(\chi_E*\chi_F)(x).
\]
For $t,x\in\mathbb R$,
\[
h(x+t)-h(x)
=\int_{\mathbb R}\chi_E(y)
\bigl(\chi_F(x+t-y)-\chi_F(x-y)\bigr)\,dy.
\]
By Cauchy--Schwarz,
\[
|h(x+t)-h(x)|
\le
\|\chi_E\|_2
\left(\int_{\mathbb R}
|\chi_F(x+t-y)-\chi_F(x-y)|^2\,dy\right)^{1/2}.
\]
After the change of variables $u=x-y$, the second factor is
\[
\|\tau_t\chi_F-\chi_F\|_2,
\]
where $(\tau_t\phi)(u)=\phi(u+t)$. Therefore
\[
\sup_{x\in\mathbb R}|h(x+t)-h(x)|
\le
\|\chi_E\|_2\,\|\tau_t\chi_F-\chi_F\|_2.
\]
Translations are continuous in $L^2(\mathbb R)$, so the right-hand side tends to $0$ as $t\to0$. Hence $h$ is uniformly continuous, and in particular continuous.
:::

<1>2. Rewrite the second convolution as a one-sided average.
::: {.proof}
For every $x\in\mathbb R$,
\[
(\chi_E*\chi_{[0,1/n]})(x)
=\int_{\mathbb R}\chi_E(y)\chi_{[0,1/n]}(x-y)\,dy.
\]
The second characteristic function is nonzero exactly when
\[
x-\frac1n\le y\le x.
\]
Thus
\[
n(\chi_E*\chi_{[0,1/n]})(x)
=n\int_{x-1/n}^{x}\chi_E(y)\,dy
=\frac{1}{1/n}\int_{x-1/n}^{x}\chi_E(y)\,dy.
\]
:::

<1>3. Apply the Lebesgue differentiation theorem.
::: {.proof}
Since $\chi_E\in L^1_{\mathrm{loc}}(\mathbb R)$, the one-sided Lebesgue differentiation theorem gives, for almost every $x$,
\[
\lim_{r\downarrow0}\frac1r\int_{x-r}^{x}\chi_E(y)\,dy
=\chi_E(x).
\]
Taking $r=1/n$ yields
\[
n(\chi_E*\chi_{[0,1/n]})(x)
\longrightarrow \chi_E(x)
\]
for almost every $x\in\mathbb R$.
:::
:::
