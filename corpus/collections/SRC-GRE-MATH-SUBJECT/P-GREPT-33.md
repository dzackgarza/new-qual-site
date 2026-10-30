---
schema: qual/card@1
id: P-GREPT-33
kind: problem
title: "Critical points of $\\int_{x^2}^{x^3}\\log t\\,dt$"
classification:
  areas: [prelim]
  topics:
  - Fundamental Theorem of Calculus
  - Critical Points
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 33 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Define a function $f(x)$ for all positive $x$ by the equation

$$f(x) = \int_{x^2}^{x^3} (\log t) \, dt$$

Find the critical point(s) of this function.

(A) $x = \frac{4}{9}, 1$
(B) $x = 1$
(C) $x = \frac{3}{2}$
(D) $x = 1, \frac{3}{2}$
(E) $x = 1, \frac{9}{4}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x>0$,
$$
f'(x)=x\log x\,(9x-4).
$$


::: pf-proof

By the fundamental theorem of calculus with variable endpoints,
$$
f'(x)
=\log(x^3)\cdot3x^2-\log(x^2)\cdot2x.
$$
Since $x>0$,
$$
\log(x^3)=3\log x
\qquad\text{and}\qquad
\log(x^2)=2\log x.
$$
Thus
$$
f'(x)=9x^2\log x-4x\log x
=x\log x(9x-4).
$$

:::

:::

::: {.pf-step #s1-2}

The derivative vanishes exactly at
$$
x=1
\qquad\text{and}\qquad
x=\frac49.
$$


::: pf-proof

On the domain $x>0$, the factor $x$ in step [](#s1-1){.pf-ref} never vanishes. The factor
$\log x$ vanishes exactly at $x=1$, and $9x-4$ vanishes exactly at
$x=4/9$.

:::

:::

::: {.pf-step #s1-3}

Therefore the critical points occur at
$$
\boxed{x=\frac49,\ 1},
$$
so the answer is (A).


::: pf-proof

The function is differentiable for every $x>0$, so its critical points are
exactly the points in its domain where $f'(x)=0$. Step [](#s1-2){.pf-ref} lists all such
points.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the complete set of critical points.

:::

:::

:::
