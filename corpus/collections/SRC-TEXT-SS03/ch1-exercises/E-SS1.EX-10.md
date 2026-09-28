---
schema: qual/card@1
id: E-SS1.EX-10
kind: problem
title: Wirtinger operators factor the Laplacian
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Show that
\[
4\frac{\partial}{\partial z}\frac{\partial}{\partial\overline z}
=
4\frac{\partial}{\partial\overline z}\frac{\partial}{\partial z}
=
\Delta,
\]
where $\Delta$ is the Laplacian
\[
\Delta=\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}.
\]
:::

::: {.solution}
<1>1. On a $C^2$ function $f$, the Wirtinger derivatives are
\[
\frac{\partial}{\partial z}
=\frac12\left(\frac{\partial}{\partial x}-i\frac{\partial}{\partial y}\right),
\qquad
\frac{\partial}{\partial\overline z}
=\frac12\left(\frac{\partial}{\partial x}+i\frac{\partial}{\partial y}\right).
\]
::: {.proof}
These are the definitions of the Wirtinger differential operators for $z=x+iy$.
:::

<1>2. One has
\[
4\frac{\partial}{\partial z}\frac{\partial}{\partial\overline z}f
=
\frac{\partial^2f}{\partial x^2}
+i\frac{\partial^2f}{\partial x\partial y}
-i\frac{\partial^2f}{\partial y\partial x}
+\frac{\partial^2f}{\partial y^2}.
\]
::: {.proof}
Expand the product of the two first-order operators in <1>1 and apply it to $f$.
:::

<1>3. Hence
\[
4\frac{\partial}{\partial z}\frac{\partial}{\partial\overline z}f=\Delta f.
\]
::: {.proof}
Since $f$ is $C^2$, Clairaut's theorem gives
\[
\frac{\partial^2f}{\partial x\partial y}
=
\frac{\partial^2f}{\partial y\partial x}.
\]
Thus the mixed terms in <1>2 cancel, leaving
\[
\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}=\Delta f.
\]
:::

<1>4. Likewise,
\[
4\frac{\partial}{\partial\overline z}\frac{\partial}{\partial z}f=\Delta f.
\]
::: {.proof}
Expanding in the reverse order gives
\[
\frac{\partial^2f}{\partial x^2}
-i\frac{\partial^2f}{\partial x\partial y}
+i\frac{\partial^2f}{\partial y\partial x}
+\frac{\partial^2f}{\partial y^2},
\]
and the same equality of mixed partials cancels the middle terms.
:::

<1>5. Therefore, as second-order differential operators on $C^2$ functions,
\[
4\frac{\partial}{\partial z}\frac{\partial}{\partial\overline z}
=
4\frac{\partial}{\partial\overline z}\frac{\partial}{\partial z}
=
\Delta.
\]
::: {.proof}
Both operator compositions agree with $\Delta$ on every $C^2$ function by <1>3 and <1>4.
:::
:::
