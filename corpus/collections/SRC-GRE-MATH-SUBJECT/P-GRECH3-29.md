---
schema: qual/card@1
id: P-GRECH3-29
kind: problem
title: Evaluate a double integral over a circular region
classification:
  areas:
  - real-analysis
  topics:
  - Double Integrals
  - Polar Coordinates
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 29 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. The chapter-3.pdf extraction read choice (A) as a^3; the book extraction reads 16/9 a^3, the value of the integral."
---

::: {.problem}
If $a$ is a positive number, what's the value of the following double integral?
$$
\int_0^{2a}\int_{-\sqrt{2ay-y^2}}^{0}\sqrt{x^2+y^2}\,dx\,dy
$$

(A) $\frac{16}{9}a^3$
(B) $\frac{32}{9}a^3$
(C) $\frac{\pi}{2}a^2$
(D) $\frac{8\pi}{3}a^2$
(E) $2a^4$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The region of integration is the left half of the disk
$$
x^2+(y-a)^2\le a^2.
$$


::: pf-proof

The curved boundary satisfies
$$
x=-\sqrt{2ay-y^2},
$$
so
$$
x^2=2ay-y^2,
$$
equivalently
$$
x^2+(y-a)^2=a^2.
$$
Because the $x$-coordinate runs from this negative boundary value to $0$, while $0\le y\le2a$, the region is exactly the left half of the disk bounded by that circle.

:::

:::

::: {.pf-step #s1-2}

In polar coordinates the region is
$$
\frac{\pi}{2}\le\theta\le\pi,
\qquad
0\le r\le2a\sin\theta.
$$


::: pf-proof

Using $x=r\cos\theta$ and $y=r\sin\theta$, the boundary equation from step [](#s1-1){.pf-ref} becomes
$$
r^2-2ar\sin\theta=0,
$$
so away from the origin,
$$
r=2a\sin\theta.
$$
The left half-plane condition is $x\le0$, while the disk lies in $y\ge0$; hence $\pi/2\le\theta\le\pi$.

:::

:::

::: {.pf-step #s1-3}

The value of the double integral is
$$
\boxed{\frac{16}{9}a^3},
$$
so the answer is (A).


::: pf-proof

In polar coordinates,
$$
\sqrt{x^2+y^2}=r
\qquad\text{and}\qquad
dA=r\,dr\,d\theta.
$$
By step [](#s1-2){.pf-ref},
$$
\begin{aligned}
I
&=\int_{\pi/2}^{\pi}\int_0^{2a\sin\theta}r^2\,dr\,d\theta\\
&=\frac{8a^3}{3}\int_{\pi/2}^{\pi}\sin^3\theta\,d\theta.
\end{aligned}
$$
Also,
$$
\int_{\pi/2}^{\pi}\sin^3\theta\,d\theta
=\int_0^{\pi/2}\sin^3\theta\,d\theta
=\frac23.
$$
Therefore
$$
I=\frac{8a^3}{3}\cdot\frac23
=\frac{16}{9}a^3.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested integral value and corresponding choice.

:::

:::

:::
