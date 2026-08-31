---
schema: qual/card@1
id: P-JHUFA10CA5
kind: problem
title: Contour integral of meromorphic function
classification:
  areas:
  - complex-analysis
  topics:
  - Residue Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Let $\gamma$ be the closed curve in the complex plane that is given in polar coordinates by $r = 2 + 3\cos\theta$, $0 \leq \theta \leq 4\pi$, oriented in the direction of increasing $\theta$.
Let

$$f(z) = \frac{e^z}{2z - 1} + \frac{\sin(2z)}{(z - 2)^2} + \frac{\cos(5z)}{(z + 5i)^3}.$$

Calculate $\int_\gamma f(z) \, dz$.

[Recall that in polar coordinates, $(-r, \theta)$ and $(r, \theta + \pi)$ give the same point in the plane.]

::: {.solution}
<1>1. The poles of $f$ are at $z = 1/2$ (simple), $z = 2$ (double), and $z = -5i$ (triple).
::: {.proof}
read off the denominators.
:::

<1>2. The curve $\gamma$ is the limaçon $r = 2 + 3\cos\theta$ traversed twice (since $0 \le \theta \le 4\pi$).
::: {.proof}
the parameter range $0 \le \theta \le 4\pi$ traverses the curve twice.
:::

<1>3. Winding numbers: $n(\gamma, 2) = 2$, $n(\gamma, 1/2) = 0$, $n(\gamma, -5i) = 0$.
<2>1. $z = 2$ lies inside the inner loop of the limaçon, and the double traversal winds around it twice.
::: {.proof}
the inner loop of $r = 2 + 3\cos\theta$ encloses the point $z = 2$ (on the positive real axis), and $0 \le \theta \le 4\pi$ winds twice.
:::
<2>2. $z = 1/2$ lies outside the inner loop (it is on the positive real axis but outside the region enclosed), so $n(\gamma, 1/2) = 0$.
::: {.proof}
the inner loop is on the left side; $z = 1/2$ is not enclosed.
:::
<2>3. $z = -5i$ is far from the curve, so $n(\gamma, -5i) = 0$.
::: {.proof}
$|{-5i}| = 5$ exceeds the maximum radius of the limaçon.
:::

<1>4. $\operatorname{Res}_{z=2} f(z) = 2\cos 4$.
::: {.proof}
the residue of $\frac{\sin(2z)}{(z-2)^2}$ at $z=2$ is $\frac{d}{dz}\sin(2z)\big|_{z=2} = 2\cos 4$; the other two terms are holomorphic at $z=2$.
:::

<1>5. By the residue theorem, $\int_\gamma f(z)\, dz = 2\pi i \sum n(\gamma, a)\operatorname{Res}_{z=a} f(z) = 2\pi i \cdot 2 \cdot 2\cos 4 = 8\pi i \cos 4$.
::: {.proof}
<1>3 and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
