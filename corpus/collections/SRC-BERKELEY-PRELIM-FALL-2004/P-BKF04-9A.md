---
schema: qual/card@1
id: P-BKF04-9A
kind: problem
title: $\int_0^1 f(x)e^{inx^3}\,dx\to0$ for continuous $f$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Let $f\colon[0,1]\to\RR$ be a continuous function. Show that

$$
\lim_{n\to\infty}\int_0^1 f(x)e^{inx^3}\,dx=0.
$$
:::

::: {.solution}

The argument is the card's own: reduce to smooth $f$, then integrate by parts on $[\varepsilon,1]$ and let $n\to\infty$ at fixed $\varepsilon$, finally $\varepsilon\to0$.

::: pf

::: {.pf-step #reduction}

It suffices to prove the statement for smooth $f$.

::: pf-proof

Let $f$ be continuous on $[0,1]$ and let $g$ be smooth with $\sup_{[0,1]}\abs{f-g}<\delta$, which exists by the Weierstrass approximation theorem (or by uniform continuity and a smoothing argument). Since $\abs{e^{inx^{3}}}=1$,
$$
\abs{\int_{0}^{1}f e^{inx^{3}}dx-\int_{0}^{1}g e^{inx^{3}}dx}\le\int_{0}^{1}\abs{f-g}\,dx<\delta
$$
for every $n$. So if the smooth case gives $\abs{\int_{0}^{1}ge^{inx^{3}}dx}<\delta$ for all large $n$, then $\abs{\int_0^1 fe^{inx^3}dx}<2\delta$ for those $n$, and $\delta>0$ is arbitrary.

:::

:::

::: {.pf-step #small}

With $M=\sup_{[0,1]}\abs{f}$, $\abs{\int_{0}^{\varepsilon}fe^{inx^{3}}dx}\le\varepsilon M$.

::: pf-proof

The estimate for an integral bounds its modulus by the supremum of the integrand times the length of the interval: the integrand has modulus $\abs{f(x)}\le M$ on $[0,\varepsilon]$, whose length is $\varepsilon$.

:::

:::

::: {.pf-step #parts}

$\displaystyle\int_{\varepsilon}^{1}fe^{inx^{3}}dx=\frac{1}{3in}\Bigl(f(1)e^{in}-\frac{f(\varepsilon)}{\varepsilon^{2}}e^{in\varepsilon^{3}}-\int_{\varepsilon}^{1}\Bigl(\frac{f}{x^{2}}\Bigr)'e^{inx^{3}}dx\Bigr)$.

::: pf-proof

On $[\varepsilon,1]$ we have $x^{2}e^{inx^{3}}=\frac{1}{3in}\frac{d}{dx}e^{inx^{3}}$, since $\frac{d}{dx}e^{inx^{3}}=3inx^{2}e^{inx^{3}}$. Writing $fe^{inx^{3}}=\frac{f}{x^{2}}\cdot x^{2}e^{inx^{3}}$ and integrating by parts with $u=f/x^{2}$ and $dv=x^{2}e^{inx^{3}}dx=\frac{1}{3in}d\bigl(e^{inx^{3}}\bigr)$,
$$
\int_{\varepsilon}^{1}fe^{inx^{3}}dx=\frac{1}{3in}\Bigl[\frac{f}{x^{2}}e^{inx^{3}}\Bigr]_{\varepsilon}^{1}-\frac{1}{3in}\int_{\varepsilon}^{1}\Bigl(\frac{f}{x^{2}}\Bigr)'e^{inx^{3}}dx,
$$
and the boundary term is $\frac{f(1)}{1}e^{in}-\frac{f(\varepsilon)}{\varepsilon^{2}}e^{in\varepsilon^{3}}$.

:::

:::

::: {.pf-step #vanish}

For fixed $\varepsilon>0$, $\displaystyle\int_{\varepsilon}^{1}fe^{inx^{3}}dx\to0$ as $n\to\infty$.

::: pf-proof

$f$ is smooth and $\varepsilon>0$, so $f/x^{2}$ is smooth on the closed interval $[\varepsilon,1]$; hence $f/x^{2}$ and its derivative are bounded there by some $K$ independent of $n$. Every factor in the bracket of step [](#parts){.pf-ref} is then bounded by a constant depending on $\varepsilon,K,M$ alone and not on $n$, so the whole expression is bounded by $\frac{1}{3n}$ times that constant, which tends to $0$.

:::

:::

::: {.pf-step #conclusion}

$\displaystyle\lim_{n\to\infty}\int_{0}^{1}f(x)e^{inx^{3}}dx=0$.

::: pf-proof

By steps [](#small){.pf-ref} and [](#vanish){.pf-ref},
$$
\limsup_{n\to\infty}\Bigl\abs{\int_{0}^{1}fe^{inx^{3}}dx\Bigr}\le\varepsilon M+0
$$
for every $\varepsilon>0$, so the limsup is $\le0$ and, being nonnegative, equals $0$. Combined with step [](#reduction){.pf-ref} and the arbitrariness of $\delta$,
$$
\boxed{\lim_{n\to\infty}\int_{0}^{1}f(x)e^{inx^{3}}dx=0\quad\text{for every continuous } f.}
$$

:::

:::

:::

:::
