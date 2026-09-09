---
schema: qual/card@1
id: P-KHVM6
kind: problem
title: Impossibility of trisecting an angle, doubling a cube, and squaring a circle
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Geometry
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Explain with field theory why straightedge-and-compass constructions cannot in general trisect an angle, double a cube, or square a circle.
:::

::: {.solution}
A real number constructible from $\QQ$ lies in a tower
\[
\QQ=K_0\subset K_1\subset\cdots\subset K_r
\]
with each extension degree at most $2$. Hence every constructible algebraic number has degree over $\QQ$ equal to a power of $2$.

<1>1. Doubling the cube is impossible.
::: {.proof}
A cube of side $1$ has volume $1$. Doubling its volume requires side length $\sqrt[3]{2}$. Its minimal polynomial is
\[
x^3-2,
\]
which is irreducible over $\QQ$ by Eisenstein at $2$. Thus
\[
[\QQ(\sqrt[3]{2}):\QQ]=3,
\]
not a power of $2$. Hence $\sqrt[3]{2}$ is not constructible.
:::

<1>2. A $60^\circ$ angle cannot be trisected by straightedge and compass.
::: {.proof}
Trisecting $60^\circ$ would construct $20^\circ$, hence $c=\cos20^\circ$. The triple-angle identity gives
\[
4c^3-3c=\cos60^\circ=\frac12,
\]
so $c$ is a root of
\[
8x^3-6x-1.
\]
This cubic has no rational root, hence is irreducible over $\QQ$. Therefore $[\QQ(c):\QQ]=3$, so $c$ is not constructible.
:::

<1>3. Squaring the circle is impossible.
::: {.proof}
A circle of radius $1$ has area $\pi$. A square of the same area would need side length $\sqrt\pi$. Lindemann's theorem implies that $\pi$ is transcendental, hence so is $\sqrt\pi$. Every constructible number is algebraic over $\QQ$, so $\sqrt\pi$ is not constructible.
:::

Thus each classical construction fails because the required length cannot lie in a tower of quadratic extensions of $\QQ$.
:::
