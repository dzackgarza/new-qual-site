---
schema: qual/card@1
id: E-SS6.EX-3
kind: exercise
title: "SS 6.3: Wallis's product and the Gamma duplication formula"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: exercise
3. Show that Wallis’s product formula can be written as

$$
\sqrt {\frac {\pi}{2}} = \lim _ {n \rightarrow \infty} \frac {2 ^ {2 n} (n !) ^ {2}}{(2 n + 1) !} (2 n + 1) ^ {1 / 2}.
$$

As a result, prove the following identity:

$$
\Gamma (s) \Gamma (s + 1 / 2) = \sqrt {\pi} 2 ^ {1 - 2 s} \Gamma (2 s).
$$
:::

::: {.solution}
<1>1. Wallis's product is $\frac{\pi}{2} = \prod_{n=1}^{\infty} \frac{4n^2}{4n^2 - 1} = \lim_{n \to \infty} \frac{2^{4n}(n!)^4}{((2n)!)^2 (2n+1)}$.
::: {.proof}
standard form of Wallis's product.
:::

<1>2. Taking square roots and rearranging gives $\sqrt{\frac{\pi}{2}} = \lim_{n \to \infty} \frac{2^{2n}(n!)^2}{(2n+1)!}(2n+1)^{1/2}$.
::: {.proof}
<1>1, using $(2n+1)! = (2n)!(2n+1)$.
:::

<1>3. For the duplication formula, use the integral representation $\Gamma(s) = \int_0^\infty t^{s-1} e^{-t}\,dt$.
::: {.proof}
definition of the Gamma function.
:::

<1>4. $\Gamma(s)\Gamma(s + 1/2) = \int_0^\infty \int_0^\infty x^{s-1} y^{s-1/2} e^{-(x+y)}\,dx\,dy$.
::: {.proof}
<1>3.
:::

<1>5. Substitute $x = u^2$, $y = v^2$: $\Gamma(s)\Gamma(s+1/2) = 4\int_0^\infty \int_0^\infty u^{2s-1} v^{2s} e^{-(u^2 + v^2)}\,du\,dv$.
::: {.proof}
<1>4, change of variables.
:::

<1>6. Switch to polar coordinates $u = r\cos\theta$, $v = r\sin\theta$: the integral becomes $4\int_0^{\pi/2}\int_0^\infty r^{4s-1}(\cos\theta)^{2s-1}(\sin\theta)^{2s} e^{-r^2}\,dr\,d\theta$.
::: {.proof}
<1>5.
:::

<1>7. The $r$-integral is $\int_0^\infty r^{4s-1} e^{-r^2}\,dr = \frac{1}{2}\Gamma(2s)$ (substituting $r^2 = t$).
::: {.proof}
<1>6.
:::

<1>8. The $\theta$-integral is $\int_0^{\pi/2} (\cos\theta)^{2s-1}(\sin\theta)^{2s}\,d\theta = \frac{1}{2}B(s, s + 1/2) = \frac{\Gamma(s)\Gamma(s+1/2)}{2\Gamma(2s + 1/2)}$.
::: {.proof}
beta function.
:::

<1>9. Combining: $\Gamma(s)\Gamma(s+1/2) = 4 \cdot \frac{1}{2}\Gamma(2s) \cdot \frac{\Gamma(s)\Gamma(s+1/2)}{2\Gamma(2s+1/2)}$, which simplifies (using $\Gamma(2s+1/2) = \frac{\Gamma(2s)\Gamma(1/2)}{2^{2s-1}\Gamma(s)}$) to the duplication formula.
::: {.proof}
<1>7 and <1>8, and the standard identity $\Gamma(2s) = \frac{2^{2s-1}}{\sqrt{\pi}}\Gamma(s)\Gamma(s+1/2)$.
:::

<1>10. Hence $\Gamma(s)\Gamma(s+1/2) = \sqrt{\pi}\,2^{1-2s}\,\Gamma(2s)$.
::: {.proof}
<1>9.
:::

<1>11. Q.E.D.
::: {.proof}
<1>2 and <1>10.
:::
:::
