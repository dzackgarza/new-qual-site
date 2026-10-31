---
schema: qual/card@1
id: P-PRACT20-W3-20
kind: problem
title: Minimizing $x+4z$ on the sphere $x^2+y^2+z^2=2$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Lagrange Multipliers
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced OCR 'sec' with the source's 'so' in the solution, checked against Week3_solns.pdf (Problem 20).
---

::: {.problem}
Minimize the function $f(x, y, z) = x + 4z$ on the sphere $x^{2} + y^{2} + z^{2} = 2$.
:::

::: {.solution}
The sphere is compact and $f$ is continuous, so $f$ attains a minimum, and the gradient of the constraint is nonzero on the sphere. By Lagrange multipliers the minimum satisfies

$$
1=2\lambda x,\qquad 0=2\lambda y,\qquad 4=2\lambda z.
$$

Plugging these into the constraint gives $\frac{1}{4\lambda^2} + \frac{4}{\lambda^2} = 2$, so $\lambda^2 = 17/8$. The two critical points are $\pm(\sqrt{2/17}, 0, \sqrt{32/17})$, where $f = \pm\sqrt{34}$; the minimum value $-\sqrt{34}$ is attained at $\left(-\sqrt{2/17},\,0,\,-\sqrt{32/17}\right)$.
:::
