---
schema: qual/card@1
id: P-GREPT-33
kind: problem
title: "Critical points of $\\int_{x^2}^{x^3}\\log t\\,dt$"
classification:
  areas: [prelim]
  topics: []
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
<1>1. For $x>0$,
$$
f'(x)=x\log x\,(9x-4).
$$

::: {.proof}
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

<1>2. The derivative vanishes exactly at
$$
x=1
\qquad\text{and}\qquad
x=\frac49.
$$

::: {.proof}
On the domain $x>0$, the factor $x$ in step <1>1 never vanishes. The factor
$\log x$ vanishes exactly at $x=1$, and $9x-4$ vanishes exactly at
$x=4/9$.
:::

<1>3. Therefore the critical points occur at
$$
\boxed{x=\frac49,\ 1},
$$
so the answer is (A).

::: {.proof}
The function is differentiable for every $x>0$, so its critical points are
exactly the points in its domain where $f'(x)=0$. Step <1>2 lists all such
points.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the complete set of critical points.
:::
:::
