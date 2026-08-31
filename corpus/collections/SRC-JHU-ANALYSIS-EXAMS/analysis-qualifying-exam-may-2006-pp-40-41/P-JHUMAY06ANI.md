---
schema: qual/card@1
id: P-JHUMAY06ANI
kind: problem
title: "The Fourier transform of an L1 function is uniformly continuous and vanishes at infinity"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Riemann-Lebesgue Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

9. Suppose that f is in $L ^ { 1 } ( \mathbb { R } )$ . Prove directly (i.e., without citing properties of the Fourier transform) that the function

$$
\widehat { f } ( t ) = \int _ { \mathbb { R } } e ^ { - i x t } f ( x ) d x
$$

is uniformly continuous and ${ \widehat { f } } ( t ) \to 0 { \mathrm { ~ a s ~ } } t \to \infty$

::: {.solution}
<1>1. For $t, s \in \mathbb{R}$,
$$|\widehat f(t) - \widehat f(s)| = \left| \int_{\mathbb{R}} (e^{-ixt} - e^{-ixs}) f(x)\,dx \right| \le \int_{\mathbb{R}} |e^{-ixt} - e^{-ixs}|\,|f(x)|\,dx.$$
::: {.proof}
definition of $\widehat f$ and the triangle inequality.
:::

<1>2. $|e^{-ixt} - e^{-ixs}| = |e^{-ixs}(e^{-ix(t-s)} - 1)| = |e^{-ix(t-s)} - 1| \le |x|\,|t - s|$.
::: {.proof}
$|e^{iu} - 1| \le |u|$ for real $u$.
:::

<1>3. Hence $|\widehat f(t) - \widehat f(s)| \le |t - s| \int_{\mathbb{R}} |x|\,|f(x)|\,dx$.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. The quantity $C = \int_{\mathbb{R}} |x|\,|f(x)|\,dx$ may be infinite, so we instead approximate: for any $\varepsilon > 0$, choose $R$ with $\int_{|x| > R} |f| < \varepsilon/4$.
::: {.proof}
$f \in L^1$, so the tail integral tends to $0$.
:::

<1>5. Then
$$|\widehat f(t) - \widehat f(s)| \le \int_{|x| \le R} |x|\,|t-s|\,|f(x)|\,dx + 2\int_{|x| > R} |f(x)|\,dx \le R\,|t-s|\,\|f\|_1 + \varepsilon/2.$$
::: {.proof}
<1>2 split over $|x| \le R$ and $|x| > R$, using $|e^{-ixt} - e^{-ixs}| \le 2$.
:::

<1>6. Choose $\delta = \varepsilon/(2R\|f\|_1)$; then $|t - s| < \delta$ implies $|\widehat f(t) - \widehat f(s)| < \varepsilon$.
::: {.proof}
<1>5.
:::

<1>7. Hence $\widehat f$ is uniformly continuous.
::: {.proof}
<1>6 (the choice of $\delta$ is independent of $t, s$).
:::

<1>8. For the decay: for $t \neq 0$, substitute $u = x - \pi/t$ (so $x = u + \pi/t$):
$$\widehat f(t) = \int_{\mathbb{R}} e^{-i(u + \pi/t)t} f(u + \pi/t)\,du = -\int_{\mathbb{R}} e^{-iut} f(u + \pi/t)\,du.$$
::: {.proof}
$e^{-i\pi} = -1$.
:::

<1>9. Averaging the two expressions for $\widehat f(t)$:
$$\widehat f(t) = \frac{1}{2}\int_{\mathbb{R}} e^{-ixt}\left(f(x) - f(x - \pi/t)\right)\,dx.$$
::: {.proof}
<1>8 and the original definition.
:::

<1>10. Hence $|\widehat f(t)| \le \frac{1}{2}\int_{\mathbb{R}} |f(x) - f(x - \pi/t)|\,dx \to 0$ as $|t| \to \infty$.
::: {.proof}
<1>9 and the continuity of translation in $L^1$ (as $|t| \to \infty$, $\pi/t \to 0$, so $\|f - f(\cdot - \pi/t)\|_1 \to 0$).
:::

<1>11. Therefore $\widehat f(t) \to 0$ as $t \to \infty$.
::: {.proof}
<1>10.
:::

<1>12. Q.E.D.
::: {.proof}
<1>7 and <1>11.
:::
:::
