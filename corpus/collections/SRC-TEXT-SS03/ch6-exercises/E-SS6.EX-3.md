---
schema: qual/card@1
id: E-SS6.EX-3
kind: problem
title: Wallis's product and the duplication formula for $\Gamma$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Infinite Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
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

::: pf

::: {.pf-step #s1}

Wallis's product is $\frac{\pi}{2} = \prod_{n=1}^{\infty} \frac{4n^2}{4n^2 - 1} = \lim_{n \to \infty} \frac{2^{4n}(n!)^4}{((2n)!)^2 (2n+1)}$.

::: pf-proof

standard form of Wallis's product.

:::

:::

::: {.pf-step #s2}

Taking square roots and rearranging gives $\sqrt{\frac{\pi}{2}} = \lim_{n \to \infty} \frac{2^{2n}(n!)^2}{(2n+1)!}(2n+1)^{1/2}$.

::: pf-proof

Step [](#s1){.pf-ref}, using $(2n+1)! = (2n)!(2n+1)$.

:::

:::

::: {.pf-step #s3}

For the duplication formula, use the integral representation $\Gamma(s) = \int_0^\infty t^{s-1} e^{-t}\,dt$.

::: pf-proof

definition of the Gamma function.

:::

:::

::: {.pf-step #s4}

$\Gamma(s)\Gamma(s + 1/2) = \int_0^\infty \int_0^\infty x^{s-1} y^{s-1/2} e^{-(x+y)}\,dx\,dy$.

::: pf-proof

Step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Substitute $x = u^2$, $y = v^2$: $\Gamma(s)\Gamma(s+1/2) = 4\int_0^\infty \int_0^\infty u^{2s-1} v^{2s} e^{-(u^2 + v^2)}\,du\,dv$.

::: pf-proof

Step [](#s4){.pf-ref}, change of variables.

:::

:::

::: {.pf-step #s6}

Switch to polar coordinates $u = r\cos\theta$, $v = r\sin\theta$: the integral becomes $4\int_0^{\pi/2}\int_0^\infty r^{4s-1}(\cos\theta)^{2s-1}(\sin\theta)^{2s} e^{-r^2}\,dr\,d\theta$.

::: pf-proof

Step [](#s5){.pf-ref}.

:::

:::

::: {.pf-step #s7}

The $r$-integral is $\int_0^\infty r^{4s-1} e^{-r^2}\,dr = \frac{1}{2}\Gamma(2s)$ (substituting $r^2 = t$).

::: pf-proof

Step [](#s6){.pf-ref}.

:::

:::

::: {.pf-step #s8}

The $\theta$-integral is $\int_0^{\pi/2} (\cos\theta)^{2s-1}(\sin\theta)^{2s}\,d\theta = \frac{1}{2}B(s, s + 1/2) = \frac{\Gamma(s)\Gamma(s+1/2)}{2\Gamma(2s + 1/2)}$.

::: pf-proof

beta function.

:::

:::

::: {.pf-step #s9}

Combining: $\Gamma(s)\Gamma(s+1/2) = 4 \cdot \frac{1}{2}\Gamma(2s) \cdot \frac{\Gamma(s)\Gamma(s+1/2)}{2\Gamma(2s+1/2)}$, which simplifies (using $\Gamma(2s+1/2) = \frac{\Gamma(2s)\Gamma(1/2)}{2^{2s-1}\Gamma(s)}$) to the duplication formula.

::: pf-proof

Steps [](#s7){.pf-ref} and [](#s8){.pf-ref}, and the standard identity $\Gamma(2s) = \frac{2^{2s-1}}{\sqrt{\pi}}\Gamma(s)\Gamma(s+1/2)$.

:::

:::

::: {.pf-step #s10}

Hence $\Gamma(s)\Gamma(s+1/2) = \sqrt{\pi}\,2^{1-2s}\,\Gamma(2s)$.

::: pf-proof

Step [](#s9){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s10){.pf-ref}.

:::

:::

:::
