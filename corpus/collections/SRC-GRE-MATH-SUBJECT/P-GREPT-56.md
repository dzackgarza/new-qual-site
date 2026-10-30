---
schema: qual/card@1
id: P-GREPT-56
kind: problem
title: "Critical point of $k^2/x+k/y+xy$"
classification:
  areas: [prelim]
  topics:
  - Critical Points
  - Multivariable Optimization
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 56 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $k$ is a nonzero constant, find the critical point of the function

$$f(x, y) = \frac{k^2}{x} + \frac{k}{y} + xy$$

(A) $(k, k)$
(B) $(-1, -k)$
(C) $(1, k)$
(D) $(-k, -1)$
(E) $(k, 1)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

At a critical point in the domain $xy\ne0$, the equations
$$
y=\frac{k^2}{x^2}
\qquad\text{and}\qquad
x=\frac{k}{y^2}
$$
must hold.


::: pf-proof

The partial derivatives are
$$
f_x=-\frac{k^2}{x^2}+y
\qquad\text{and}\qquad
f_y=-\frac{k}{y^2}+x.
$$
A critical point satisfies $f_x=f_y=0$, giving the displayed equations.

:::

:::

::: {.pf-step #s1-2}

Every critical point has
$$
x=k.
$$


::: pf-proof

Substitute $y=k^2/x^2$ from step [](#s1-1){.pf-ref} into the second equation:
$$
x
=\frac{k}{(k^2/x^2)^2}
=\frac{x^4}{k^3}.
$$
Since a point in the domain has $x\ne0$ and the hypothesis gives $k\ne0$,
division by $x$ yields $x^3=k^3$. Over $\RR$, the cube function is
injective, so $x=k$.

:::

:::

::: {.pf-step #s1-3}

The corresponding $y$-coordinate is
$$
y=1.
$$


::: pf-proof

Substituting $x=k$ into the first equation of step [](#s1-1){.pf-ref} gives
$$
y=\frac{k^2}{k^2}=1.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the unique critical point is
$$
\boxed{(k,1)},
$$
so the answer is (E).


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} show that every critical point must equal $(k,1)$, and
direct substitution into the two equations of step [](#s1-1){.pf-ref} verifies that this
point is indeed critical.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required critical point.

:::

:::

:::
