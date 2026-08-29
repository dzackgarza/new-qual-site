---
schema: qual/card@1
id: P-F10CR
kind: problem
title: Cube roots of $-2-2i$
classification:
  areas:
  - prelim
  topics:
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Find all the cube roots of $-2 - 2i$.
:::

::: {.solution}
<1>1. $-2 - 2i = 2\sqrt{2}\, e^{-3\pi i/4}$.
Proof: $|-2-2i| = \sqrt{4+4} = 2\sqrt{2}$, and $\arg(-2-2i) = -3\pi/4$.

<1>2. The cube roots have modulus $(2\sqrt{2})^{1/3} = \sqrt{2}$ and arguments $\frac{-3\pi/4 + 2\pi k}{3}$ for $k = 0, 1, 2$.
Proof: the cube roots of $re^{i\theta}$ are $r^{1/3} e^{i(\theta + 2\pi k)/3}$.

<1>3. The three cube roots are:
$$1 - i,\qquad \frac{\sqrt3 - 1}{2} + \frac{\sqrt3 + 1}{2}i,\qquad -\frac{\sqrt3 + 1}{2} + \frac{1 - \sqrt3}{2}i.$$
Proof: evaluate <1>2 for $k = 0, 1, 2$:
- $k=0$: $\sqrt2 e^{-i\pi/4} = \sqrt2(\frac{\sqrt2}{2} - i\frac{\sqrt2}{2}) = 1 - i$;
- $k=1$: $\sqrt2 e^{5\pi i/12} = \frac{\sqrt3 - 1}{2} + \frac{\sqrt3 + 1}{2}i$;
- $k=2$: $\sqrt2 e^{13\pi i/12} = -\frac{\sqrt3 + 1}{2} + \frac{1 - \sqrt3}{2}i$.

<1>4. Q.E.D.
Proof: <1>3.
:::
