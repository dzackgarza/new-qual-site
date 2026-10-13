---
schema: qual/card@1
id: P-GREPT-26
kind: problem
title: "Equation of the torus from revolving a circle about the $z$-axis"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 26 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $C$ be the circle in the $yz$-plane whose equation is $(y - 3)^2 + z^2 = 1$. If $C$ is revolved around the $z$-axis, the surface generated is a torus. What is the equation of this torus?

(A) $x^2 + y^2 + z^2 + 8 = 6y$
(B) $(x^2 + y^2 + z^2)^2 = 8 + 36(x^2 + z^2)$
(C) $(x^2 + y^2 + z^2 + 8)^2 = 36(x^2 + z^2)$
(D) $(x^2 + y^2 + z^2 + 8)^2 = 36(x^2 + y^2)$
(E) $(x^2 + y^2 + z^2 + 8)^2 = 36(y^2 + z^2)$
:::

::: {.solution}
<1>1. If
$$
\rho=\sqrt{x^2+y^2},
$$
then the torus satisfies
$$
(\rho-3)^2+z^2=1.
$$

::: {.proof}
Revolving the circle $(y-3)^2+z^2=1$ about the $z$-axis replaces the
nonnegative distance $y$ from the axis in the generating half-plane by the
radial distance $\rho=\sqrt{x^2+y^2}$ from the $z$-axis. Hence the generating
circle equation becomes the displayed equation.
:::

<1>2. The equation in step <1>1 is equivalent to
$$
x^2+y^2+z^2+8=6\sqrt{x^2+y^2}.
$$

::: {.proof}
Expanding step <1>1 gives
$$
\rho^2-6\rho+9+z^2=1,
$$
so
$$
\rho^2+z^2+8=6\rho.
$$
Substitute $\rho^2=x^2+y^2$.
:::

<1>3. Therefore the torus has equation
$$
\boxed{(x^2+y^2+z^2+8)^2=36(x^2+y^2)},
$$
so the answer is (D).

::: {.proof}
Squaring the equality in step <1>2 gives the displayed polynomial equation.
Conversely, its left unsquared quantity $x^2+y^2+z^2+8$ is strictly positive
and $\sqrt{x^2+y^2}\ge0$, so the squared equation forces the positive sign and
recovers step <1>2. Thus no extraneous branch is introduced.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the required equation of the surface.
:::
:::
