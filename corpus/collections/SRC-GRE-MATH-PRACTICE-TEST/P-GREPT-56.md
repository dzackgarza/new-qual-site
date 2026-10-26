---
schema: qual/card@1
id: P-GREPT-56
kind: problem
title: "Critical point of $k^2/x+k/y+xy$"
classification:
  areas: [prelim]
  topics: []
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

::: pf

::: pf-step

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

::: pf-step

Every critical point has
$$
x=k.
$$


::: pf-proof

Substitute $y=k^2/x^2$ from step <1>1 into the second equation:
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

::: pf-step

The corresponding $y$-coordinate is
$$
y=1.
$$


::: pf-proof

Substituting $x=k$ into the first equation of step <1>1 gives
$$
y=\frac{k^2}{k^2}=1.
$$

:::

:::

::: pf-step

Therefore the unique critical point is
$$
\boxed{(k,1)},
$$
so the answer is (E).


::: pf-proof

Steps <1>2--<1>3 show that every critical point must equal $(k,1)$, and
direct substitution into the two equations of step <1>1 verifies that this
point is indeed critical.

:::

:::

::: pf-qed

Step <1>4 gives the required critical point.

:::

:::
