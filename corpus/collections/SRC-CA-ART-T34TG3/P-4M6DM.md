---
schema: qual/card@1
id: P-4M6DM
kind: problem
title: The integral of $(1+x^2)^{-n-1}$ over $\RR$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
---

::: {.problem}
Show that
$$
\int_{-\infty}^{\infty} \frac{d x}{\left(1+x^{2}\right)^{n+1}}=\frac{1 \cdot 3 \cdot 5 \cdots(2 n-1)}{2 \cdot 4 \cdot 6 \cdots(2 n)} \cdot \pi
.$$
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the substitution, the Wallis recursion (proved by parts) and the induction separated.

::: pf

::: {.pf-step #trig}
$\displaystyle I_{n}=\int_{-\infty}^{\infty}\frac{dx}{(1+x^{2})^{n+1}}=2\int_{0}^{\pi/2}\cos^{2n}\theta\,d\theta$.

::: pf-proof
The integrand is even, so $I_{n}=2\int_{0}^{\infty}(1+x^{2})^{-(n+1)}dx$. Substitute $x=\tan\theta$, $dx=\sec^{2}\theta\,d\theta$: then $1+x^{2}=\sec^{2}\theta$ and $(1+x^{2})^{-(n+1)}dx=\sec^{-2n-2}\theta\sec^{2}\theta\,d\theta=\cos^{2n}\theta\,d\theta$, while $x$ runs from $0$ to $\infty$ as $\theta$ runs from $0$ to $\pi/2$.
:::

:::

::: {.pf-step #recursion}
With $W_{n}=\int_{0}^{\pi/2}\cos^{2n}\theta\,d\theta$ one has $W_{n}=\dfrac{2n-1}{2n}W_{n-1}$ for $n\ge1$.

::: pf-proof
Integration by parts with $u=\cos^{2n-1}\theta$, $dv=\cos\theta\,d\theta$ gives $W_{n}=\big[\cos^{2n-1}\theta\sin\theta\big]_{0}^{\pi/2}+(2n-1)\int_{0}^{\pi/2}\cos^{2n-2}\theta\sin^{2}\theta\,d\theta$; the boundary term vanishes at both ends. With $\sin^{2}=1-\cos^{2}$ the integral becomes $W_{n-1}-W_{n}$, so $W_{n}=(2n-1)(W_{n-1}-W_{n})$, that is $2nW_{n}=(2n-1)W_{n-1}$.
:::

:::

::: {.pf-step #wallis}
$W_{n}=\dfrac{1\cdot3\cdots(2n-1)}{2\cdot4\cdots(2n)}\,\dfrac{\pi}{2}$ for every $n\ge0$.

::: pf-proof
$W_{0}=\int_{0}^{\pi/2}d\theta=\pi/2$, and if the formula holds for $n-1$ then step [](#recursion){.pf-ref} multiplies it by $\dfrac{2n-1}{2n}$, giving the formula for $n$; induction on $n$ completes it.
:::

:::

::: {.pf-qed}
$I_{n}=2W_{n}=\dfrac{1\cdot3\cdots(2n-1)}{2\cdot4\cdots(2n)}\pi$ by steps [](#trig){.pf-ref} and [](#wallis){.pf-ref}.
:::

:::

:::
