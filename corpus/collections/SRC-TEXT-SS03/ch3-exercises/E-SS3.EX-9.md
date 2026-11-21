---
schema: qual/card@1
id: E-SS3.EX-9
kind: problem
title: $\int_0^1\log\sin\pi x\,dx=-\log2$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Logarithm
  - Definite Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the prose solution as a Lamport proof: integrability at the two endpoints, the
    substitution t -> pi/2 - t, the doubling with log(sin t cos t) = log sin 2t - log 2, the
    linear substitution u = 2t with the symmetry of log sin u on (0,pi), and the final rescaling
    t = pi x are separate steps, and the answer is boxed in the last one. No retained solution set
    covers this exercise, so the argument is the card's own; no retained text of Stein and
    Shakarchi is in this checkout either, so the printed statement and its hint (a contour in the
    book's Figure 9) are taken as they stand on the card and were not re-read against the book in
    this pass. The neighbouring exercises of the same chapter carry the same kind of printed
    figure hint, and the identity proved is the one stated. The contour route the hint suggests is
    not used, and the card says so rather than implying the hint was followed.
---

::: {.exercise}
Show that

$$
\int_0^1 \log(\sin \pi x)\, dx = -\log 2.
$$

[Hint: Use the contour shown in Figure 9.]
:::

::: {.solution}
The statement is Exercise 9 of [@SS03, ch. 3], printed as $\int_0^1\log(\sin\pi x)\,dx=-\log 2$, with the contour of its Figure 9.

No retained solution set covers this exercise; the argument is the card's own and does not follow the printed hint, which points at a contour in the book's Figure 9. Write $\log$ for the real logarithm.

::: pf

::: {.pf-step #integrable}
$\log(\sin t)$ is integrable on $(0,\pi)$, so the integrals below converge.

::: pf-proof
Near $0$ use $\sin t=t(1+O(t^{2}))$, so $\log(\sin t)=\log t+O(t^{2})$, and $\log t$ is integrable on $(0,1)$; near $\pi$ the substitution $s=\pi-t$ gives the same estimate with $\sin s$. On any closed subinterval of $(0,\pi)$ the integrand is continuous. The integrands $\log(\cos t)$ and $\log(\sin 2t)$ on $(0,\pi/2)$, and $\log(\sin u)$ on $(0,\pi)$, are handled by the same two estimates at their finitely many zeros.
:::

:::

::: {.pf-step #symmetry}
$\displaystyle I\coloneqq\int_{0}^{\pi/2}\log(\sin t)\,dt=\int_{0}^{\pi/2}\log(\cos t)\,dt$.

::: pf-proof
Substituting $t=\pi/2-s$ turns $\int_{0}^{\pi/2}\log(\sin t)\,dt$ into $\int_{0}^{\pi/2}\log(\cos s)\,ds$, since $\sin(\pi/2-s)=\cos s$ and the substitution reverses the endpoints twice.
:::

:::

::: {.pf-step #doubling}
$\displaystyle 2I=\int_{0}^{\pi/2}\log(\sin 2t)\,dt-\frac{\pi}{2}\log 2$.

::: pf-proof
Adding the two expressions of step [](#symmetry){.pf-ref} gives $2I=\int_{0}^{\pi/2}\bigl(\log(\sin t)+\log(\cos t)\bigr)dt=\int_{0}^{\pi/2}\log(\sin t\cos t)\,dt$, which is legitimate because step [](#integrable){.pf-ref} makes both integrands integrable. Now $\sin t\cos t=\tfrac12\sin 2t$, so the integrand equals $\log(\sin 2t)-\log 2$, and the constant integrates to $-\tfrac{\pi}{2}\log 2$.
:::

:::

::: {.pf-step #halving}
$\displaystyle \int_{0}^{\pi/2}\log(\sin 2t)\,dt=I$.

::: pf-proof
With $u=2t$ this integral is $\tfrac12\int_{0}^{\pi}\log(\sin u)\,du$. Splitting at $\pi/2$ and applying step [](#symmetry){.pf-ref} to the second piece, which is $\int_{0}^{\pi/2}\log(\cos s)\,ds$ under $s=\pi-u$, gives $\tfrac12\bigl(I+I\bigr)=I$.
:::

:::

::: {.pf-step #value}
$\displaystyle I=-\frac{\pi}{2}\log 2$.

::: pf-proof
Insert step [](#halving){.pf-ref} into step [](#doubling){.pf-ref}: $2I=I-\tfrac{\pi}{2}\log 2$, so $I=-\tfrac{\pi}{2}\log 2$.
:::

:::

::: {.pf-step #answer}
$\displaystyle\int_{0}^{1}\log(\sin\pi x)\,dx=\boxed{-\log 2}$.

::: pf-proof
Substituting $t=\pi x$ gives $\int_{0}^{1}\log(\sin\pi x)\,dx=\frac{1}{\pi}\int_{0}^{\pi}\log(\sin t)\,dt=\frac{2I}{\pi}$ by the computation of step [](#halving){.pf-ref}, and $\frac{2}{\pi}\bigl(-\tfrac{\pi}{2}\log2\bigr)=-\log 2$ by step [](#value){.pf-ref}.
:::

:::

:::
:::
