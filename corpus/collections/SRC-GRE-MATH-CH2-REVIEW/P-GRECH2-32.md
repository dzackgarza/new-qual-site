---
schema: qual/card@1
id: P-GRECH2-32
kind: problem
title: Polar area of the region bounded by two circles
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 32 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The figure of the two circles was not recovered by either extraction.
---

::: {.problem}
The circles with polar equations
$$
r=\sqrt{3}\sin\theta
\qquad\text{and}\qquad
r=3\cos\theta
$$
bound a common region in the first quadrant. Which of the following expressions gives the area of this common region?

(A) $\int_0^{\frac{\pi}{2}} \frac{1}{2} \left[ (\sqrt{3} \sin \theta)^2 - (3 \cos \theta)^2 \right] d\theta$
(B) $\int_0^{\frac{\pi}{6}} \frac{1}{2} (3 \cos \theta)^2 d\theta + \int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \frac{1}{2} (\sqrt{3} \sin \theta)^2 d\theta$
(C) $\int_0^{\frac{\pi}{6}} \frac{1}{2} (\sqrt{3} \sin \theta)^2 d\theta + \int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \frac{1}{2} (3 \cos \theta)^2 d\theta$
(D) $\int_0^{\frac{\pi}{3}} \frac{1}{2} (3 \cos \theta)^2 d\theta + \int_{\frac{\pi}{3}}^{\frac{\pi}{2}} \frac{1}{2} (\sqrt{3} \sin \theta)^2 d\theta$
(E) $\int_0^{\frac{\pi}{3}} \frac{1}{2} (\sqrt{3} \sin \theta)^2 d\theta + \int_{\frac{\pi}{3}}^{\frac{\pi}{2}} \frac{1}{2} (3 \cos \theta)^2 d\theta$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The two circle boundaries meet away from the origin at
$$
\theta=\frac{\pi}{3}.
$$


::: pf-proof

On a common nonzero point of the two polar curves,
$$
\sqrt3\sin\theta=3\cos\theta.
$$
In the first quadrant this is equivalent to
$$
\tan\theta=\sqrt3,
$$
whose solution in $(0,\pi/2)$ is $\theta=\pi/3$.

:::

:::

::: {.pf-step #s1-2}

For $0\leq\theta\leq\pi/3$, the common region extends radially to $r=\sqrt3\sin\theta$; for $\pi/3\leq\theta\leq\pi/2$, it extends radially to $r=3\cos\theta$.


::: pf-proof

The common region on a ray is bounded by the smaller of the two nonnegative radial functions. At $\theta=0$, one has
$$
\sqrt3\sin\theta=0<3=3\cos\theta,
$$
and the two functions first become equal at $\theta=\pi/3$ by step [](#s1-1){.pf-ref}. At $\theta=\pi/2$, one has
$$
3\cos\theta=0<\sqrt3=\sqrt3\sin\theta.
$$
Thus the smaller radial boundary is the first circle before the intersection angle and the second circle after it.

:::

:::

::: {.pf-step #s1-3}

The area is
$$
\boxed{
\int_0^{\pi/3}\frac12(\sqrt3\sin\theta)^2\,d\theta
+\int_{\pi/3}^{\pi/2}\frac12(3\cos\theta)^2\,d\theta
},
$$
so the answer is (E).


::: pf-proof

For a polar region whose radial boundary is $r=R(\theta)$, the area element integrated along rays is $\frac12R(\theta)^2\,d\theta$. Applying this formula to the two angular ranges from step [](#s1-2){.pf-ref} gives the displayed expression.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested area expression and corresponding choice.

:::

:::

:::
