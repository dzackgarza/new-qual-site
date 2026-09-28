---
schema: qual/card@1
id: P-COFTP
kind: problem
title: $\int_0^\infty\frac{\log x}{x^2+a^2}\,dx=\frac{\pi}{2a}\log a$ for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that if $a>0$, then
\[
\int_{0}^{\infty} \frac{\log x}{x^{2}+a^{2}} d x=\frac{\pi}{2 a} \log a
.\]

> Hint: use the following contour.
> ![](../../assets/Complex_Analysis/999_Quals/figures/image_2020-06-17-21-53-19.png)
:::

::: {.solution}
Let $\Log$ be the branch of the logarithm on $\CC\setminus[0,\infty)$ with argument in $(0, 2\pi)$. For $0<\varepsilon<a<R$, let $\Gamma$ be the keyhole contour consisting of the segment $[\varepsilon, R]$ on the upper edge of the cut, the circle $\abs z = R$ counterclockwise, the segment from $R$ to $\varepsilon$ on the lower edge, and the circle $\abs z = \varepsilon$ clockwise. Put
$$f(z) \coloneqq \frac{\Log z}{z^2 + a^2},
\qquad
g(z) \coloneqq \frac{(\Log z)^2}{z^2 + a^2},
\qquad
I \coloneqq \int_0^{\infty} \frac{\log x}{x^2 + a^2}\, dx.$$

<1>1. On the upper edge $\Log z = \log x$, and on the lower edge $\Log z = \log x + 2\pi i$.

::: {.proof}
Approaching the positive real axis from above, $\arg z\to0$; from below, $\arg z\to2\pi$.
:::

<1>2. For $h\in\{f,g\}$, the integrals of $h$ over $\abs z = R$ and $\abs z = \varepsilon$ tend to $0$ as $R\to\infty$ and $\varepsilon\to0$.

::: {.proof}
On $\abs z = r$, $\abs{\Log z} \le \abs{\log r} + 2\pi$ and $\abs{z^2 + a^2} \ge \abs{r^2 - a^2}$. The circle has length $2\pi r$, so the integral of $h$ over it is at most $2\pi r\,(\abs{\log r} + 2\pi)^2/\abs{r^2 - a^2}$ (with exponent $1$ in place of $2$ for $f$). This tends to $0$ as $r\to\infty$ and as $r\to0$.
:::

<1>3. $\displaystyle\int_0^{\infty} \frac{dx}{x^2 + a^2} = \frac{\pi}{2a}$.

<2>1. The two edges contribute $-2\pi i \int_\varepsilon^R \frac{dx}{x^2 + a^2}$ to $\int_\Gamma f$.

::: {.proof}
By step <1>1, and since the lower edge runs from $R$ to $\varepsilon$, the two edges give
$$\int_\varepsilon^R \frac{\log x}{x^2 + a^2}\, dx - \int_\varepsilon^R \frac{\log x + 2\pi i}{x^2 + a^2}\, dx.$$
:::

<2>2. $\Res_{z=ia} f + \Res_{z=-ia} f = -\dfrac{\pi}{2a}$.

::: {.proof}
The poles $\pm ia$ are simple, $z^2 + a^2 = (z-ia)(z+ia)$, $\Log(ia) = \log a + i\pi/2$, and $\Log(-ia) = \log a + 3i\pi/2$. Hence
$$\Res_{z=ia} f + \Res_{z=-ia} f = \frac{\log a + i\pi/2}{2ia} + \frac{\log a + 3i\pi/2}{-2ia} = \frac{-i\pi}{2ia}.$$
:::

<2>3. Q.E.D.

::: {.proof}
Both poles lie inside $\Gamma$, so the residue theorem and step <2>2 give $\int_\Gamma f = 2\pi i\cdot(-\pi/(2a)) = -i\pi^2/a$. Letting $\varepsilon \to 0$ and $R \to \infty$, steps <1>2 and <2>1 give $-2\pi i \int_0^{\infty} \frac{dx}{x^2 + a^2} = -\frac{i\pi^2}{a}$.
:::

<1>4. The two edges contribute $\displaystyle\int_\varepsilon^R \frac{-4\pi i \log x + 4\pi^2}{x^2 + a^2}\, dx$ to $\int_\Gamma g$.

::: {.proof}
By step <1>1, and since the lower edge runs from $R$ to $\varepsilon$, the edges give $\int_\varepsilon^R \frac{(\log x)^2 - (\log x + 2\pi i)^2}{x^2 + a^2}\, dx$. Expand $(\log x + 2\pi i)^2 = (\log x)^2 + 4\pi i \log x - 4\pi^2$.
:::

<1>5. $\displaystyle\int_\Gamma g = -\frac{2\pi^2 i}{a}\log a + \frac{2\pi^3}{a}$.

::: {.proof}
The residues are $\Res_{z=ia} g = \frac{(\log a + i\pi/2)^2}{2ia}$ and $\Res_{z=-ia} g = \frac{(\log a + 3i\pi/2)^2}{-2ia}$. By the difference of squares, their sum is
$$\frac{1}{2ia}(-i\pi)(2\log a + 2i\pi) = -\frac{\pi}{a}(\log a + i\pi).$$
Multiply by $2\pi i$.
:::

<1>6. $I = \boxed{\dfrac{\pi}{2a}\log a}$.

::: {.proof}
Let $\varepsilon \to 0$ and $R \to \infty$ in $\int_\Gamma g$. By steps <1>2, <1>3, <1>4, and <1>5,
$$-4\pi i I + 4\pi^2 \cdot \frac{\pi}{2a} = -\frac{2\pi^2 i}{a}\log a + \frac{2\pi^3}{a}.$$
The real terms $4\pi^2 \cdot \frac{\pi}{2a}$ and $\frac{2\pi^3}{a}$ are equal, leaving $-4\pi i I = -\frac{2\pi^2 i}{a} \log a$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the claimed identity.
:::
:::
