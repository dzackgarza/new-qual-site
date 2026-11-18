---
schema: qual/card@1
id: E-SS4.EX-2
kind: problem
title: Derivatives of functions in $\mathfrak F_a$ lie in $\mathfrak F_b$ for $b<a$
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 notation and exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the definition unpacked, the Cauchy estimate on a circle
    of radius $\rho$, the pointwise comparison $1+x^{2}\le(2+2\rho^{2})(1+u^{2})$, and the resulting bound.
    No retained solution set covers this exercise (the collection retains the textbook, not a solutions
    manual), so the argument is the card's own; every inequality was re-read for this pass.
---

::: {.exercise}
If $f \in \mathfrak{F}_a$ with $a > 0$, then for any positive integer $n$ one has $f^{(n)} \in \mathfrak{F}_b$ whenever $0 \leq b < a$.

[Hint: Modify the solution to Exercise 8 in Chapter 2.]
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. Recall that $f\in\mathfrak F_{a}$ means $f$ is holomorphic on the strip $S_{a}=\{z:\abs{\Im z}<a\}$ and that for some $A>0$
$$
\abs{f(x+iy)}\le\frac{A}{1+x^{2}}\qquad(x\in\RR,\ \abs{y}<a).
$$

::: pf

::: {.pf-step #circle}
For $0\le b<a$ and $\rho=\frac{a-b}{2}>0$, the circle $\abs{w-z}=\rho$ lies in $S_{a}$ for every $z=x+iy$ with $\abs{y}<b$.

::: pf-proof
A point $w$ on that circle satisfies $\abs{\Im w-y}\le\abs{w-z}=\rho$, so $\abs{\Im w}\le\abs{y}+\rho<b+\frac{a-b}{2}=\frac{a+b}{2}<a$.
:::

:::

::: {.pf-step #cauchy}
$\abs{f^{(n)}(z)}\le\dfrac{n!}{\rho^{n}}\sup_{\abs{w-z}=\rho}\abs{f(w)}$.

::: pf-proof
$f$ is holomorphic on a neighbourhood of the closed disc bounded by that circle, which lies in $S_{a}$ by step [](#circle){.pf-ref}. Cauchy's estimate for the $n$-th derivative on a circle of radius $\rho$ gives the displayed bound.
:::

:::

::: {.pf-step #compare}
For $w=u+iv$ with $\abs{w-z}\le\rho$ and $z=x+iy$, one has $1+x^{2}\le(2+2\rho^{2})(1+u^{2})$.

::: pf-proof
$\abs{x}\le\abs{u}+\abs{x-u}\le\abs{u}+\rho$, so $x^{2}\le(\abs{u}+\rho)^{2}\le2u^{2}+2\rho^{2}$ since $(p+q)^{2}\le2p^{2}+2q^{2}$. Hence $1+x^{2}\le1+2u^{2}+2\rho^{2}\le(2+2\rho^{2})(1+u^{2})$, the last step because $1\le2+2\rho^{2}$ and $2u^{2}+2\rho^{2}\le(2+2\rho^{2})u^{2}+(2+2\rho^{2})$ is immediate after collecting terms.
:::

:::

::: {.pf-step}
$f^{(n)}\in\mathfrak F_{b}$ for every $0\le b<a$ and $n\ge1$.

::: pf-proof
For $w$ on the circle of step [](#circle){.pf-ref} with $w=u+iv$, the defining bound and step [](#compare){.pf-ref} give
$$
\abs{f(w)}\le\frac{A}{1+u^{2}}\le\frac{A(2+2\rho^{2})}{1+x^{2}},
$$
so by step [](#cauchy){.pf-ref}, for every $z=x+iy$ with $\abs{y}<b$,
$$
\abs{f^{(n)}(z)}\le\frac{n!A(2+2\rho^{2})}{\rho^{n}}\cdot\frac{1}{1+x^{2}}=\frac{A_{n}}{1+x^{2}},\qquad A_{n}=\frac{n!A(2+2\rho^{2})}{\rho^{n}} .
$$
The bound is of the defining form with the constant $A_{n}$ on the strip $S_{b}$, so $f^{(n)}\in\mathfrak F_{b}$; and $b<a$ was arbitrary.
:::

:::

:::
:::
