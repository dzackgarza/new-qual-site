---
schema: qual/card@1
id: E-SS8.EX-23
kind: problem
title: A conformal map onto a regular polygon
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Schwarz-Christoffel
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
    Restructured as a Lamport proof of the argument already on the card, whose conclusion, angle
    computation and perimeter agree with an independent check: with |1 - e^{i phi}| =
    2|sin(phi/2)| the side length is (2^(1-2/n)/n)∫_0^pi (sin u)^(-2/n) du, and n times it is
    the printed perimeter. Repaired: the card derived F(omega z) - F(0) = omega(F(z) - F(0))
    from 'F'(omega z) = F'(z)' without the integration that justifies it, which is now written
    out; and it asserted 'a polygon with n equal angles and this rotational symmetry is regular'
    with no reason, which is now the argument that the rotation identifies all side lengths.
    Also added: the branch of the power, the well-definedness of F on the simply connected disc,
    and the convergence of the integral at each vertex. Not claimed: a retained solution set;
    the collection's provenance is the Stein--Shakarchi textbook.
---

::: {.exercise}
If
$$
F(z) = \int_{1}^{z} \frac{d\zeta}{(1-\zeta^{n})^{2/n}},
$$
then $F$ maps the unit disc conformally onto the interior of a regular polygon with $n$ sides and perimeter
$$
2^{\frac{n-2}{n}} \int_{0}^{\pi} (\sin\theta)^{-2/n}\,d\theta .
$$
:::

::: {.solution}
Throughout $n \ge 3$, $\omega \coloneqq e^{2\pi i/n}$, $\DD$ is the unit disc and $F(z) \coloneqq \int_{1}^{z}(1-\zeta^{n})^{-2/n}d\zeta$ is taken along any path in $\DD$; the exercise is Exercise 23 of Stein--Shakarchi, *Complex Analysis*, Chapter 8.

::: pf

::: {.pf-step #well-defined}
$F$ is well defined and holomorphic on $\DD$, with $F'(z) = (1-z^{n})^{-2/n} \ne 0$.

::: pf-proof
For $z \in \DD$ one has $\abs{z^{n}} < 1$, so $1 - z^{n}$ lies in the disc of centre $1$ and radius $1$, on which the principal logarithm is defined; hence $(1-z^{n})^{-2/n} \coloneqq \exp\bigl(-\frac{2}{n}\log(1-z^{n})\bigr)$ is a nonzero holomorphic function of $z$ on $\DD$, and it is the derivative of the path integral of itself, which is therefore independent of the path because $\DD$ is simply connected.

:::

:::

::: {.pf-step #schwarz-christoffel}
$(1-z^{n})^{-2/n} = \prod_{k=0}^{n-1}\bigl(1-\omega^{-k}z\bigr)^{-2/n}$, so $F$ has the Schwarz--Christoffel form with exponent $\beta_{k} = -2/n$ at each of the $n$ distinct boundary points $\omega^{k}$.

::: pf-proof
The factorization $1 - z^{n} = \prod_{k=0}^{n-1}(1 - \omega^{k}z)$ holds because the $\omega^{k}$ are the $n$ distinct $n$-th roots of $1$ and both sides are monic of degree $n$ with the same zeros; raising to the power $-2/n$ multiplies the exponents. In the disc version of the Schwarz--Christoffel formula the exponents $\beta_{k}$ are the data at $n$ points $\zeta_{k}$ of the unit circle, and the formula produces a conformal map of $\DD$ onto the interior of a polygon whose angle at the $k$-th vertex is $(1 + \beta_{k})\pi$.

:::

:::

::: {.pf-step #angles}
$F$ maps $\DD$ conformally onto the interior of a polygon with $n$ vertices, each of interior angle $\bigl(1 - \frac{2}{n}\bigr)\pi$.

::: pf-proof
By step [](#schwarz-christoffel){.pf-ref} the Schwarz--Christoffel theorem applies with $\beta_{k} = -2/n$ at each of the $n$ points $\omega^{k}$ and no others, giving interior angles $(1 - \frac{2}{n})\pi$; the integral converges at each $\omega^{k}$ because the singularity is $\abs{\zeta - \omega^{k}}^{-2/n}$ with $2/n < 1$. The angle is $< \pi$, so the polygon is convex.

:::

:::

::: {.pf-step #rotational}
$F(\omega z) - F(0) = \omega\bigl(F(z) - F(0)\bigr)$ for $z \in \DD$.

::: pf-proof
$F'(\omega z) = (1 - \omega^{n}z^{n})^{-2/n} = (1-z^{n})^{-2/n} = F'(z)$, so $\frac{d}{dz}\bigl[\omega^{-1}F(\omega z)\bigr] = F'(\omega z) = F'(z) = \frac{d}{dz}F(z)$ on the connected set $\DD$; hence $\omega^{-1}F(\omega z) - F(z)$ is constant, and evaluating at $z = 0$ gives the identity.

:::

:::

::: {.pf-step #regular}
The image polygon is a regular $n$-gon.

::: pf-proof
By step [](#rotational){.pf-ref} multiplication by $\omega$ about the point $F(0)$ carries the image polygon onto itself and moves each vertex $F(\omega^{k})$ to the next; so the polygon is invariant under rotation through $2\pi/n$ about $F(0)$, and step [](#angles){.pf-ref} gives all $n$ interior angles the common value $(1 - \frac{2}{n})\pi$. An $n$-gon with equal angles whose vertices are permuted cyclically by a rotation of order $n$ about an interior point is regular: the rotation identifies all side lengths with one another and all circumradii with one another.

:::

:::

::: {.pf-step #side}
One side has length $L = \frac{2^{1-2/n}}{n}\int_{0}^{\pi}(\sin u)^{-2/n}du$.

::: pf-proof
The side from $F(1)$ to $F(\omega)$ is the image of the arc $z = e^{i\theta}$, $0 \le \theta \le 2\pi/n$, so $L = \int_{0}^{2\pi/n}\abs{F'(e^{i\theta})}d\theta = \int_{0}^{2\pi/n}\abs{1 - e^{in\theta}}^{-2/n}d\theta$. Now $\abs{1 - e^{i\varphi}} = 2\abs{\sin(\varphi/2)}$, so the integrand is $2^{-2/n}\abs{\sin(n\theta/2)}^{-2/n}$ with $\sin(n\theta/2) \ge 0$ on the range of $\theta$; substituting $u = n\theta/2$, $d\theta = 2du/n$, with $u$ running from $0$ to $\pi$, gives $L = 2^{-2/n}\cdot\frac{2}{n}\int_{0}^{\pi}(\sin u)^{-2/n}du = \frac{2^{1-2/n}}{n}\int_{0}^{\pi}(\sin u)^{-2/n}du$.

:::

:::

::: pf-step
The perimeter of the image polygon is $\boxed{2^{(n-2)/n}\int_{0}^{\pi}(\sin\theta)^{-2/n}d\theta}$.

::: pf-proof
By step [](#regular){.pf-ref} the $n$ sides are equal, so the perimeter is $nL = 2^{1-2/n}\int_{0}^{\pi}(\sin u)^{-2/n}du$ with $L$ from step [](#side){.pf-ref}, and $2^{1-2/n} = 2^{(n-2)/n}$ because $1 - 2/n = (n-2)/n$. The integral converges since $2/n < 1$.

:::

:::

:::
:::
