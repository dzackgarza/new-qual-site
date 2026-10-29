---
schema: qual/card@1
id: P-GREPT-43
kind: problem
title: "Highest point of the lemniscate $r^2=4\\cos2\\theta$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 43 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $L$ be the curve whose equation in the polar coordinates $r$ and $\theta$ is $r^2 = 4 \cos 2\theta$. Find the largest value of $y$ such that the point with rectangular coordinates $(x, y)$ is on $L$.

(A) $\frac{1+\sqrt{3}}{4}$
(B) $\frac{\sqrt{2}}{2}$
(C) $\frac{\sqrt{6}}{3}$
(D) $\frac{\sqrt{3}}{2}$
(E) $1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every point of $L$,
$$
y^2=2c(1-c),
\qquad
c:=\cos2\theta\in[0,1].
$$


::: pf-proof

The equation $r^2=4\cos2\theta$ and $r^2\ge0$ imply
$c=\cos2\theta\ge0$, while always $c\le1$. Also
$$
y^2=r^2\sin^2\theta
=4c\cdot\frac{1-\cos2\theta}{2}
=2c(1-c).
$$

:::

:::

::: {.pf-step #s1-2}

For $0\le c\le1$,
$$
2c(1-c)\le\frac12.
$$


::: pf-proof

Completing the square gives
$$
2c(1-c)
=\frac12-2\left(c-\frac12\right)^2
\le\frac12,
$$
with equality exactly when $c=1/2$.

:::

:::

::: {.pf-step #s1-3}

The bound in step [](#s1-2){.pf-ref} is attained with positive $y$.


::: pf-proof

Take $\theta=\pi/6$. Then
$$
\cos2\theta=\cos\frac\pi3=\frac12,
$$
so the curve equation gives $r^2=2$ and we may take $r=\sqrt2$. Hence
$$
y=r\sin\theta
=\sqrt2\cdot\frac12
=\frac{\sqrt2}{2}>0.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the largest possible value of $y$ is
$$
\boxed{\frac{\sqrt2}{2}},
$$
so the answer is (B).


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give $|y|\le\sqrt2/2$, and step [](#s1-3){.pf-ref} exhibits a point of
$L$ whose $y$-coordinate equals this upper bound.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required maximum.

:::

:::

:::
