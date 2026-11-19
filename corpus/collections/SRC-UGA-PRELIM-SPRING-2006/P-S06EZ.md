---
schema: qual/card@1
id: P-S06EZ
kind: problem
title: Complex solutions of $e^z=2i$
classification:
  areas:
  - prelim
  topics:
  - Complex Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card's first step had no proof and was written as an
    instruction ('Write z = x+iy ... Then e^z = e^x(cos y + i sin y)'), while its remaining
    steps were sound. The polar form is now a proved step citing Euler's formula and computing
    modulus and argument; the modulus equation gives x = ln 2 with the strict monotonicity of
    exp named; the argument equation gives cos y = 0 and sin y = 1, with the sign of the
    argument fixed explicitly; and the final step verifies that every listed z works as well as
    that no others do. The answer is unchanged. Not claimed: a retained solution set; the
    collection's provenance is the examination paper only.
---

::: {.problem}
Find all complex numbers $z = x + iy$, $(x, y \in \RR)$, such that $e^z = 2i$.
:::


::: {.solution}
Throughout $z = x + iy$ with $x, y \in \RR$, $e^{z}$ is the complex exponential, $\ln$ is the real logarithm, and $\ZZ$ is the set of integers. The collection's `provenance` is the Spring 2006 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #euler}
$e^{z} = e^{x}(\cos y + i\sin y)$, so $\abs{e^{z}} = e^{x}$ and $\arg e^{z} \equiv y \pmod{2\pi}$.

::: pf-proof
With $z = x + iy$ and $x, y$ real, the complex exponential satisfies $e^{x+iy} = e^{x}e^{iy}$, and Euler's formula gives $e^{iy} = \cos y + i\sin y$. The modulus of the product is $e^{x}\abs{e^{iy}} = e^{x}$ because $\cos^{2}y + \sin^{2}y = 1$ and $e^{x} > 0$, and its argument is $y$ modulo $2\pi$.

:::

:::

::: {.pf-step #modulus}
If $e^{z} = 2i$ then $e^{x} = 2$, that is $x = \ln 2$.

::: pf-proof
Taking moduli in $e^{z} = 2i$ and using step [](#euler){.pf-ref} gives $e^{x} = \abs{e^{z}} = \abs{2i} = 2$. The real exponential is strictly increasing and $\ln$ is its inverse, so $x = \ln 2$.

:::

:::

::: {.pf-step #argument}
If $e^{z} = 2i$ then $\cos y = 0$ and $\sin y = 1$, that is $y = \frac{\pi}{2} + 2\pi k$ for some $k \in \ZZ$.

::: pf-proof
With $x = \ln 2$ from step [](#modulus){.pf-ref}, the equation $e^{z} = 2i$ reads $2(\cos y + i\sin y) = 2i$ by step [](#euler){.pf-ref}, that is $\cos y + i\sin y = i$, which gives $\cos y = 0$ and $\sin y = 1$. The points of the unit circle with $\cos y = 0$ are $y = \pm\pi/2 + 2\pi k$, and $\sin y = 1$ selects the sign $+$, so $y = \pi/2 + 2\pi k$.

:::

:::

::: pf-step
The solutions are $z = \ln 2 + i\left(\frac{\pi}{2} + 2\pi k\right)$ for $k \in \ZZ$, and there are no others.

::: pf-proof
Every $z$ of that form satisfies $e^{z} = 2e^{i(\pi/2 + 2\pi k)} = 2i$, using step [](#euler){.pf-ref} and $e^{2\pi i k} = 1$; conversely steps [](#modulus){.pf-ref} and [](#argument){.pf-ref} show that any solution has exactly this real part and this set of imaginary parts.

:::

:::

:::
:::
