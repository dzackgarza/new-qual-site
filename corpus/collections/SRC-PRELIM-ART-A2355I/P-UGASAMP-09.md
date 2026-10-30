---
schema: qual/card@1
id: P-UGASAMP-09
kind: problem
title: Cube roots of $i$ and the value of $(1+i)^5$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Find the three cube roots of $i$ and compute
$$
(1+i)^5.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The complex number $i$ has polar representations
$$
i=e^{i(\pi/2+2\pi m)},
\qquad m\in\ZZ.
$$


::: pf-proof

The modulus of $i$ is $1$, and its arguments are exactly
$$
\frac{\pi}{2}+2\pi m,
\qquad m\in\ZZ.
$$
Hence Euler's formula gives the displayed representations.

:::

:::

::: {.pf-step #s1-2}

The three cube roots of $i$ are
$$
e^{i\pi/6},\qquad
e^{i5\pi/6},\qquad
e^{i3\pi/2}.
$$


::: pf-proof

If $z^3=i$, then $\abs{z}^3=1$, so $\abs{z}=1$. Writing $z=e^{i\theta}$, step [](#s1-1){.pf-ref} gives
$$
3\theta=\frac{\pi}{2}+2\pi m.
$$
Thus
$$
\theta=\frac{\pi}{6}+\frac{2\pi m}{3}.
$$
Modulo $2\pi$, the three distinct values occur for $m=0,1,2$, namely
$$
\frac{\pi}{6},\qquad
\frac{5\pi}{6},\qquad
\frac{3\pi}{2}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the cube roots are
$$
\boxed{
\frac{\sqrt3}{2}+\frac{i}{2},
\qquad
-\frac{\sqrt3}{2}+\frac{i}{2},
\qquad
-i.}
$$


::: pf-proof

Apply Euler's formula
$$
e^{i\theta}=\cos\theta+i\sin\theta
$$
to the three angles in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{(1+i)^5=-4-4i.}
$$


::: pf-proof

First,
$$
(1+i)^2=1+2i+i^2=2i.
$$
Hence
$$
(1+i)^4=(2i)^2=-4,
$$
and therefore
$$
(1+i)^5=(1+i)^4(1+i)
=-4(1+i)
=-4-4i.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives all three cube roots of $i$, and step [](#s1-4){.pf-ref} computes $(1+i)^5$.

:::

:::

:::
