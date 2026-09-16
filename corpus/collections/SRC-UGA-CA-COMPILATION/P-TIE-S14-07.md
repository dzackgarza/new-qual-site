---
schema: qual/card@1
id: P-TIE-S14-07
kind: problem
title: Analyticity of the gamma function and the reflection formula
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2014, question 7.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX and labelled the parts against Spring 2014, question 7, pages 7-8 of Questions_from_Tie.pdf, and quoted the formula of question 6 that the statement cites as the previous question.
---

::: {.problem}
For $s > 0$, the **gamma function** is defined by $\Gamma(s) = \int_0^\infty e^{-t} t^{s-1}\,dt$.

(a) Show that the gamma function is analytic in the half-plane $\operatorname{Re}(s) > 0$, and is still given there by the integral formula above.

(b) Apply the formula in the previous question to show that
$$
\Gamma(s)\Gamma(1-s) = \frac{\pi}{\sin \pi s}.
$$

Hint: You may need $\Gamma(1-s) = t\int_0^\infty e^{-vt}(vt)^{-s}\,dv$ for $t > 0$.
:::

::: {.remark}
"The formula in the previous question" refers to the question printed immediately before this one in the source (question 6):
$$
\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx = \frac{\pi}{n\sin\frac{a\pi}{n}}, \qquad 0 < a < n,\ n \text{ a positive integer}.
$$
With $n = 1$ and $a = 1 - s$ for $0 < s < 1$ it reads $\int_0^\infty \frac{v^{-s}}{1+v}\,dv = \frac{\pi}{\sin \pi s}$, which the hint turns into the reflection formula.
:::
