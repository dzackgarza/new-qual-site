---
schema: qual/card@1
id: P-JHUFA11ANH
kind: problem
title: 'No convolution identity in $L^1(\RR^n)$'
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the JHU Analysis Qualifying Exam, September 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Show that there is no $I\in L^1(\RR^n)$ such that
$$
f*I=f
\qquad\text{for every }f\in L^1(\RR^n).
$$
:::

::: {.solution}
<1>1. If such an $I$ existed, then
$$
\widehat f(\xi)\widehat I(\xi)=\widehat f(\xi)
\qquad\text{for every }f\in L^1(\RR^n)
$$
and every $\xi\in\RR^n$.
::: {.proof}
Taking Fourier transforms in $f*I=f$ and applying [[PR-DY2B3|the convolution formula for Fourier transforms]] gives
$$
\widehat{f*I}=\widehat f\,\widehat I,
$$
which is the stated identity.
:::

<1>2. The identity in step <1>1 forces $\widehat I\equiv1$.
::: {.proof}
Choose the Gaussian $f(x)=e^{-\pi\abs{x}^2}$. It belongs to $L^1(\RR^n)$ and its Fourier transform is again a Gaussian, so
$$
\widehat f(\xi)\ne0
\qquad\text{for every }\xi.
$$
Therefore
$$
\widehat I(\xi)=1
\qquad\text{for every }\xi\in\RR^n.
$$
:::

<1>3. This contradicts the Riemann--Lebesgue lemma.
::: {.proof}
Since $I\in L^1(\RR^n)$, [[PR-IGMH4|the Riemann--Lebesgue lemma]] gives
$$
\widehat I(\xi)\longrightarrow0
\qquad(\abs{\xi}\to\infty),
$$
contradicting step <1>2.
:::

<1>4. Q.E.D.
::: {.proof}
The contradiction in step <1>3 proves that no such convolution identity element exists in $L^1(\RR^n)$.
:::
:::
