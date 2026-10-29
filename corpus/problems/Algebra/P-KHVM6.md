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

::: {.problem}
Explain with field theory why straightedge-and-compass constructions cannot in general trisect an angle, double a cube, or square a circle.
:::

::: {.solution}

::: pf

::: {.pf-step #tower}
Every real number constructible from $\QQ$ is algebraic over $\QQ$ of degree a power of $2$.

::: pf-proof
A constructible number lies in the top field of a tower $\QQ=K_0\subset K_1\subset\cdots\subset K_r$ with $[K_{i+1}:K_i]\le 2$ for each $i$. Hence $[K_r:\QQ]$ is a power of $2$, and the degree of the number divides it.
:::

:::

::: pf-step
Doubling the cube is impossible.

::: pf-proof
A cube of volume $2$ has side length $\sqrt[3]{2}$. Its minimal polynomial $x^3-2$ is irreducible over $\QQ$ by Eisenstein's criterion at $2$, so $[\QQ(\sqrt[3]{2}):\QQ]=3$, which is not a power of $2$. By step [](#tower){.pf-ref}, $\sqrt[3]{2}$ is not constructible.
:::

:::

::: pf-step
A $60^\circ$ angle cannot be trisected.

::: pf-proof
Trisecting $60^\circ$ would construct $c=\cos 20^\circ$. The triple-angle identity gives $4c^3-3c=\cos 60^\circ=\frac12$, so $c$ is a root of $8x^3-6x-1$. By the rational root test this cubic has no rational root, so it is irreducible over $\QQ$ and $[\QQ(c):\QQ]=3$. By step [](#tower){.pf-ref}, $c$ is not constructible.
:::

:::

::: pf-step
Squaring the circle is impossible.

::: pf-proof
A square with the area $\pi$ of the unit circle has side length $\sqrt\pi$. By Lindemann's theorem $\pi$ is transcendental, hence so is $\sqrt\pi$. By step [](#tower){.pf-ref}, $\sqrt\pi$ is not constructible.
:::

:::

:::

:::
