---
schema: qual/card@1
id: P-CALCPT3-11
kind: problem
title: "Vanishing second partials of $x^2+2xy+xz^2$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 11 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction, which reads the exponent of z as 3/2. The 300 dpi page render shows a printed 2 with a handwritten 3 above it; the printed exponent 2 is transcribed. The answer is the same for either exponent."
---

::: {.problem}
If $\phi(x,y,z)=x^2+2xy+xz^2$, which of the following partial derivatives are identically zero?

I. $\dfrac{\partial^2\phi}{\partial y^2}$

II. $\dfrac{\partial^2\phi}{\partial x\,\partial y}$

III. $\dfrac{\partial^2\phi}{\partial z\,\partial y}$

(A) III only
(B) I and II only
(C) I and III only
(D) II and III only
(E) I, II, and III
:::

::: {.solution}

::: pf

::: {.pf-step #first-partial}
$\dfrac{\partial\phi}{\partial y}=2x$.

::: pf-proof
Only the term $2xy$ depends on $y$, and its partial derivative in $y$ is $2x$.
:::

:::

::: {.pf-step #second-partials}
$\dfrac{\partial^2\phi}{\partial y^2}=0$, $\dfrac{\partial^2\phi}{\partial x\,\partial y}=2$, and $\dfrac{\partial^2\phi}{\partial z\,\partial y}=0$.

::: pf-proof
Differentiate $2x$ from step [](#first-partial){.pf-ref} in $y$, in $x$, and in $z$ respectively.
Since $\phi$ is a polynomial, the order of mixed differentiation does not matter.
:::

:::

::: pf-step
The identically zero derivatives are $\boxed{\text{I and III only}}$, choice (C).

::: pf-proof
By step [](#second-partials){.pf-ref}, I and III vanish identically and II is the nonzero constant $2$.
:::

:::

:::

:::
