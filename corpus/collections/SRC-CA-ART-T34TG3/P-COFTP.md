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

::: problem
Show that if $a>0$, then
\[
\int_{0}^{\infty} \frac{\log x}{x^{2}+a^{2}} d x=\frac{\pi}{2 a} \log a
.\]

> Hint: use the following contour.
> ![](../../assets/Complex_Analysis/999_Quals/figures/image_2020-06-17-21-53-19.png)
:::

::: {.solution}
**Goal:** Show that for $a > 0$, $\int_0^{\infty} \frac{\log x}{x^2 + a^2}\, dx = \frac{\pi}{2a} \log a$.

<1>1. Integrate $f(z) := \frac{\Log z}{z^2 + a^2}$ over the keyhole contour $\Gamma$ that runs along the positive real axis: the segment $[\varepsilon, R]$ on the upper edge, the big circle $\abs z = R$, the segment $[R, \varepsilon]$ on the lower edge, and the small circle $\abs z = \varepsilon$.
    Proof: Take the branch of $\Log$ with argument in $(0, 2\pi)$, so the branch cut is the positive real axis; the contour avoids it.

<1>2. The circle contributions vanish: $\int_{\abs z = R} f \to 0$ and $\int_{\abs z = \varepsilon} f \to 0$.
    Proof: On $\abs z = R$, $\abs{f(z)} \leq \frac{\log R + 2\pi}{R^2 - a^2}$, and the length is $2\pi R$, giving a bound of order $\frac{\log R}{R} \to 0$; similarly on $\abs z = \varepsilon$ the bound is $\varepsilon(\log \varepsilon + 2\pi) \to 0$.

<1>3. The two horizontal segments contribute $-2\pi i \int_\varepsilon^R \frac{dx}{x^2 + a^2}$.
    <2>1. On the upper edge, $z = x$ and $\Log z = \log x$.
        Proof: The upper edge is approached from inside the region where $\arg z = 0$.
    <2>2. On the lower edge, $z = x$ and $\Log z = \log x + 2\pi i$.
        Proof: Approaching the positive real axis from below, $\arg z = 2\pi$, and the lower edge is traversed from $R$ down to $\varepsilon$.
    <2>3. Sum: $\int_\varepsilon^R \frac{\log x}{x^2 + a^2}\, dx - \int_\varepsilon^R \frac{\log x + 2\pi i}{x^2 + a^2}\, dx = -2\pi i \int_\varepsilon^R \frac{dx}{x^2 + a^2}$.
        Proof: <2>1 and <2>2, with the orientation of the lower edge reversed.

<1>4. Compute the residues of $f$ at $z = \pm ia$.
    <2>1. $\Res_{z=ia} f = \frac{\Log(ia)}{2ia} = \frac{\log a + i\pi/2}{2ia}$.
        Proof: Simple poles (denominator $z^2 + a^2 = (z-ia)(z+ia)$); $\Log(ia) = \log a + i\pi/2$.
    <2>2. $\Res_{z=-ia} f = \frac{\Log(-ia)}{-2ia} = \frac{\log a + 3i\pi/2}{-2ia}$.
        Proof: $\Log(-ia) = \log a + 3i\pi/2$ for the branch with $\arg \in (0, 2\pi)$.
    <2>3. Sum of residues: $\frac{1}{2ia}\qty[(\log a + i\pi/2) - (\log a + 3i\pi/2)] = \frac{1}{2ia}(-i\pi) = -\frac{\pi}{2a}$.
        Proof: <2>1 and <2>2.

<1>5. By the residue theorem, the keyhole integral equals $2\pi i \cdot (-\pi/2a) = -i\pi^2/a$.
    Proof: Both poles $\pm ia$ lie inside the keyhole (for $R > a > \varepsilon$).

<1>6. Equate the contour integral with the sum of pieces.
    <2>1. $-2\pi i \int_0^{\infty} \frac{dx}{x^2 + a^2} = -\frac{i\pi^2}{a}$.
        Proof: <1>2, <1>3 and <1>5, letting $\varepsilon \to 0$, $R \to \infty$.
    <2>2. $\int_0^{\infty} \frac{dx}{x^2 + a^2} = \frac{\pi}{2a}$.
        Proof: Divide <2>1 by $-2\pi i$.

<1>7. The $\log$ contribution cancels in this computation, so repeat with $g(z) := \frac{(\Log z)^2}{z^2 + a^2}$ to extract $\int \log x/(x^2 + a^2)$.
    Proof: Integrating $\Log z$ alone recovers only $\int dx/(x^2+a^2)$ because the two edges differ by $2\pi i$, a constant; squaring the logarithm produces a $\Log z$ term in the difference.

<1>8. The horizontal segments of $g$ contribute $-4\pi i \int_\varepsilon^R \frac{\log x}{x^2 + a^2}\, dx + 4\pi^2 \int_\varepsilon^R \frac{dx}{x^2 + a^2}$.
    <2>1. The upper edge contributes $\int_\varepsilon^R \frac{(\log x)^2}{x^2 + a^2}\, dx$.
        Proof: On the upper edge, $\Log z = \log x$ and the contour runs from $\varepsilon$ to $R$.
    <2>2. The lower edge contributes $-\int_\varepsilon^R \frac{(\log x + 2\pi i)^2}{x^2 + a^2}\, dx$.
        Proof: On the lower edge, $\Log z = \log x + 2\pi i$; the contour runs from $R$ down to $\varepsilon$, reversing the sign.
    <2>3. Sum: $\int_\varepsilon^R \frac{(\log x)^2 - (\log x + 2\pi i)^2}{x^2 + a^2}\, dx = \int_\varepsilon^R \frac{-4\pi i \log x + 4\pi^2}{x^2 + a^2}\, dx$.
        Proof: <2>1 and <2>2; expand $(\log x + 2\pi i)^2 = (\log x)^2 + 4\pi i \log x - 4\pi^2$.

<1>9. Compute the residues of $g$ at $\pm ia$.
    <2>1. $\Res_{z=ia} g = \frac{(\log a + i\pi/2)^2}{2ia}$ and $\Res_{z=-ia} g = \frac{(\log a + 3i\pi/2)^2}{-2ia}$.
        Proof: Same poles as $f$, with numerators squared.
    <2>2. Sum: $\frac{1}{2ia}\qty[(\log a + i\pi/2)^2 - (\log a + 3i\pi/2)^2] = \frac{1}{2ia}\qty[(-i\pi)\qty(2\log a + 2i\pi)] = -\frac{\pi}{a}(\log a + i\pi)$.
        Proof: Difference of squares $u^2 - v^2 = (u-v)(u+v)$.
    <2>3. Keyhole integral of $g$: $2\pi i \cdot \qty(-\frac{\pi}{a}(\log a + i\pi)) = -\frac{2\pi^2 i}{a}\log a + \frac{2\pi^3}{a}$.
        Proof: Residue theorem, as in <1>5.

<1>10. Equate and solve.
    <2>1. $-4\pi i I + 4\pi^2 \cdot \frac{\pi}{2a} = -\frac{2\pi^2 i}{a}\log a + \frac{2\pi^3}{a}$, where $I := \int_0^{\infty} \frac{\log x}{x^2 + a^2}\, dx$.
        Proof: <1>8 (with <1>6.2 for the $dx$ term), <1>9.3, and the vanishing circle terms.
    <2>2. $I = \frac{\pi}{2a}\log a$.
        Proof: The real terms $4\pi^2 \cdot \frac{\pi}{2a}$ and $\frac{2\pi^3}{a}$ are equal and cancel, leaving $-4\pi i I = -\frac{2\pi^2 i}{a} \log a$; divide by $-4\pi i$.

<1>11. Q.E.D.
    Proof: <1>10.2 is exactly the claimed identity.

:::
