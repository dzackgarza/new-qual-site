---
schema: qual/card@1
id: P-OQW4B
kind: problem
title: The cube roots of $2-2i$
classification:
  areas:
  - prelim
  topics:
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Find all cube roots of $2-2i$ and express them in the standard form $a + bi$.
:::


::: solution
<1>1. Write $2-2i$ in polar form as
\[
2-2i=2\sqrt2\,e^{-i\pi/4}.
\]
:::

<1>2. Every cube root therefore has the form
\[
z_k=\sqrt2\,e^{i(-\pi/12+2\pi k/3)},\qquad k=0,1,2.
\]
::: {.proof}
The modulus of a cube root is $(2\sqrt2)^{1/3}=\sqrt2$, and its argument is one third of $-\pi/4+2\pi k$.
:::

<1>3. For $k=0$,
\[
z_0=\frac{1+\sqrt3}{2}-\frac{\sqrt3-1}{2}i.
\]
::: {.proof}
Using $\cos 15^\circ=(\sqrt6+\sqrt2)/4$ and $\sin 15^\circ=(\sqrt6-\sqrt2)/4$,
\[
\sqrt2(\cos15^\circ-i\sin15^\circ)
=\frac{1+\sqrt3}{2}-\frac{\sqrt3-1}{2}i.
\]
:::

<1>4. For $k=1$,
\[
z_1=\frac{1-\sqrt3}{2}+\frac{1+\sqrt3}{2}i.
\]
::: {.proof}
Here the argument is $105^\circ$, so
\[
\sqrt2(\cos105^\circ+i\sin105^\circ)
=\frac{1-\sqrt3}{2}+\frac{1+\sqrt3}{2}i.
\]
:::

<1>5. For $k=2$,
\[
z_2=-1-i.
\]
::: {.proof}
Here the argument is $225^\circ$, and
\[
\sqrt2(\cos225^\circ+i\sin225^\circ)=-1-i.
\]
:::

<1>6. These are all the cube roots of $2-2i$.
::: {.proof}
The equation $z^3=2-2i$ has degree $3$, and <1>2 gives three distinct roots.
:::
