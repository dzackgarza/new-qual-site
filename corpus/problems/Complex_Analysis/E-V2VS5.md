---
schema: qual/card@1
id: E-V2VS5
kind: problem
title: Simple zeros of $\sin(\pi z)$ at the integers, and residues of $1/\sin(\pi
  z)$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Residues
  - Trigonometry
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that the complex zeros of $f(z) \da \sin(\pi z)$ are exactly $\ZZ$, and each is order 1. Calculate the residue of $1/\sin(\pi x)$ at $z=n\in \ZZ$.
:::

![image_2021-05-17-13-32-46](../../assets/figures/image_2021-05-17-13-32-46.png)

![image_2021-05-17-13-32-57](../../assets/figures/image_2021-05-17-13-32-57.png)

![image_2021-05-17-13-33-12](../../assets/figures/image_2021-05-17-13-33-12.png)

![image_2021-05-17-13-33-30](../../assets/figures/image_2021-05-17-13-33-30.png)

::: {.solution}
**Goal:** Show that the complex zeros of $f(z) = \sin(\pi z)$ are exactly $\ZZ$, each of order 1, and compute the residue of $1/\sin(\pi z)$ at $z = n \in \ZZ$.

<1>1. The zeros of $\sin(\pi z)$ in $\CC$ are exactly the integers.
::: {.proof}
$\sin(\pi z) = (e^{i\pi z} - e^{-i\pi z})/2i$, so $\sin(\pi z) = 0$ iff $e^{2i\pi z} = 1$ iff $2i\pi z = 2\pi i k$ for some $k \in \ZZ$ iff $z = k \in \ZZ$.
:::

<1>2. Each zero $z = n$ is simple.
::: {.proof}
$\ddd{z}\sin(\pi z) = \pi \cos(\pi z)$, and $\cos(\pi n) = (-1)^n \neq 0$ for $n \in \ZZ$.
:::

<1>3. $1/\sin(\pi z)$ has a simple pole at each $z = n \in \ZZ$.
::: {.proof}
The denominator vanishes to order exactly 1 at each integer (<1>2) and the numerator is the nonzero constant 1.
:::

<1>4. The residue of $1/\sin(\pi z)$ at $z = n$ is $(-1)^n/\pi$.
::: {.proof}
For a simple pole, $\Res_{z = n} \frac{1}{\sin(\pi z)} = \lim_{z \to n} (z - n)\frac{1}{\sin(\pi z)} = \frac{1}{\sin'(\pi n)} = \frac{1}{\pi \cos(\pi n)} = \frac{1}{\pi (-1)^n} = \frac{(-1)^n}{\pi}$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>1–<1>2 identify the zeros and their orders; <1>3–<1>4 give the residues.
:::
:::
