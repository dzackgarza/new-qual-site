---
schema: qual/card@1
id: P-YBT6I
kind: problem
title: "Convolutions of L2 functions and convolution operators on L1"
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

7. Let

$$
f \ast g ( x ) : = \int _ { - \infty } ^ { + \infty } f ( y ) g ( x - y ) d y
$$

denote the convolution of f and $g .$

(a) Let $f , g \in L ^ { 2 } ( \mathbb { R } )$ be two square-integrable functions on R (with the usual Lebesgue measure).
Show that the convolution $f * g$ bounded continuous function on R.

(b) Instead let $h \in L ^ { 1 } ( \mathbb { R } )$ be fixed.
Show that $A ( f ) = f * h$ is a bounded operator $L ^ { 1 } ( \mathbb { R } ) \to L ^ { 1 } ( \mathbb { R } )$

::: {.solution}
**Part (a).**

<1>1. $f \ast g$ is bounded.
<2>1. $|(f \ast g)(x)| \le \|f\|_{L^2} \|g\|_{L^2}$ for all $x$.
::: {.proof}
by Cauchy–Schwarz, $|(f\ast g)(x)| = \left|\int f(y) g(x-y)\, dy\right| \le \|f\|_{L^2} \|g\|_{L^2}$.
:::
<2>2. Hence $f \ast g$ is bounded.
::: {.proof}
<2>1 gives a uniform bound.
:::

<1>2. $f \ast g$ is continuous.
<2>1. Translation is continuous in $L^2$: $\|g(\cdot - (x+h)) - g(\cdot - x)\|_{L^2} \to 0$ as $h \to 0$.
::: {.proof}
standard continuity of translation in $L^p$ for $1 \le p < \infty$.
:::
<2>2. $|(f\ast g)(x+h) - (f\ast g)(x)| \le \|f\|_{L^2} \|g(\cdot - (x+h)) - g(\cdot - x)\|_{L^2} \to 0$.
::: {.proof}
Cauchy–Schwarz and <2>1.
:::
<2>3. Hence $f \ast g$ is continuous.
::: {.proof}
<2>2.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::

**Part (b).**

<1>1. $\|A(f)\|_{L^1} = \|f \ast h\|_{L^1} \le \|f\|_{L^1} \|h\|_{L^1}$.
::: {.proof}
Young's convolution inequality (or Fubini–Tonelli): $\int |(f\ast h)(x)|\, dx \le \int \int |f(y)| |h(x-y)|\, dy\, dx = \|f\|_{L^1} \|h\|_{L^1}$.
:::

<1>2. Hence $A$ is a bounded operator $L^1 \to L^1$ with $\|A\| \le \|h\|_{L^1}$.
::: {.proof}
<1>1.
:::

<1>3. Q.E.D.
::: {.proof}
<1>2.
:::
:::
