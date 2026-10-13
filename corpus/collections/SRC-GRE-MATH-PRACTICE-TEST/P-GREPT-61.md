---
schema: qual/card@1
id: P-GREPT-61
kind: problem
title: "Green's theorem for a line integral around a triangle"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 61 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $C$ be the boundary, oriented counterclockwise, of the triangle in the $xy$-plane whose vertices are $(0, 1)$, $(1, 1)$, and $(1, 3)$. What is the value of the following integral?

$$\oint_C \sqrt{2x+1} \, dx + \left(2xy + \sqrt{y^2 - y}\right) dy$$

(A) $1$
(B) $\frac{8}{3}$
(C) $3$
(D) $\frac{10}{3}$
(E) $4$
:::

::: {.solution}
<1>1. The terms depending only on $x$ or only on $y$ contribute zero around $C$.

::: {.proof}
On the ranges occurring on $C$, the functions $\sqrt{2x+1}$ and
$\sqrt{y^2-y}$ are continuous, so they have antiderivatives $F(x)$ and
$G(y)$, respectively. Hence
\[
\oint_C \sqrt{2x+1}\,dx=\oint_C dF=0
\quad\text{and}\quad
\oint_C \sqrt{y^2-y}\,dy=\oint_C dG=0.
\]
Therefore the given integral equals $\oint_C 2xy\,dy$.
:::

<1>2. The contribution of the horizontal edge from $(0,1)$ to $(1,1)$ is $0$.

::: {.proof}
Along this edge, $dy=0$.
:::

<1>3. The contribution of the vertical edge from $(1,1)$ to $(1,3)$ is $8$.

::: {.proof}
Here $x=1$ and $y$ increases from $1$ to $3$, so
\[
\int_1^3 2y\,dy=[y^2]_1^3=8.
\]
:::

<1>4. The contribution of the diagonal edge from $(1,3)$ to $(0,1)$ is $-\frac{14}{3}$.

::: {.proof}
The diagonal has equation $y=2x+1$, hence $x=(y-1)/2$. With the
counterclockwise orientation, $y$ decreases from $3$ to $1$. Therefore
\[
\int_3^1 2\left(\frac{y-1}{2}\right)y\,dy
=\int_3^1 (y^2-y)\,dy
=-\frac{14}{3}.
\]
:::

<1>5. The value of the integral is $\boxed{\frac{10}{3}}$.

::: {.proof}
By steps <1>1, <1>2, <1>3, and <1>4, the integral is
\[
0+8-\frac{14}{3}=\frac{10}{3}.
\]
Thus the correct choice is (D).
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested value.
:::
:::
