---
schema: qual/card@1
id: P-TRIV-CA03
kind: problem
title: Complex roots of $z^2+3z+12$, $z^4+5z^2+4$, $z^6=1$ and $z^3=-1$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the (possibly complex) roots of these polynomials
$$
z^2 + 3z + 12 = 0, \qquad z^4 + 5z^2 + 4 = 0, \qquad z^6 = 1, \qquad z^3 = -1.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The roots of
$$
z^2+3z+12=0
$$
are
$$
\boxed{
z=\frac{-3\pm i\sqrt{39}}{2}.
}
$$


::: pf-proof

The quadratic formula gives
$$
z
=
\frac{-3\pm\sqrt{9-48}}{2}
=
\frac{-3\pm\sqrt{-39}}{2}
=
\frac{-3\pm i\sqrt{39}}{2}.
$$

:::

:::

::: {.pf-step #s1-2}

The roots of
$$
z^4+5z^2+4=0
$$
are
$$
\boxed{z=\pm i,\ \pm2i}.
$$


::: pf-proof

Set
$$
w=z^2.
$$
Then
$$
w^2+5w+4
=(w+1)(w+4).
$$
Hence
$$
z^2=-1
\qquad\text{or}\qquad
z^2=-4,
$$
which gives the four stated roots.

:::

:::

::: {.pf-step #s1-3}

The solutions of
$$
z^6=1
$$
are
$$
\boxed{
z=e^{i\pi k/3},
\qquad
k=0,1,2,3,4,5.
}
$$


::: pf-proof

Write
$$
1=e^{2\pi i m},
\qquad m\in\ZZ.
$$
If $z=re^{i\theta}$ and $z^6=1$, then
$$
r^6=1,
$$
so $r=1$, and
$$
6\theta=2\pi m.
$$
Thus
$$
\theta=\frac{\pi m}{3}.
$$
Modulo $2\pi$, exactly six values occur, represented by $m=0,\ldots,5$.

:::

:::

::: {.pf-step #s1-4}

The solutions of
$$
z^3=-1
$$
are
$$
\boxed{
e^{i\pi/3},
\quad
e^{i\pi},
\quad
e^{i5\pi/3}.
}
$$


::: pf-proof

Write
$$
-1=e^{i(\pi+2\pi m)}.
$$
Taking cube roots gives
$$
z
=
e^{i(\pi+2\pi m)/3}.
$$
Modulo $2\pi$, the three distinct values arise from $m=0,1,2$.

:::

:::

::: {.pf-step #s1-5}

Equivalently, the roots in step [](#s1-4){.pf-ref} are
$$
\boxed{
\frac12+i\frac{\sqrt3}{2},
\quad
-1,
\quad
\frac12-i\frac{\sqrt3}{2}.
}
$$


::: pf-proof

Apply Euler's formula to the three polar forms from step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} give all roots requested in the four equations.

:::

:::

:::
