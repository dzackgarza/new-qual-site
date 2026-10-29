---
schema: qual/card@1
id: E-XBYYR
kind: problem
title: Schwarz reflection and holomorphic functions real on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Fractional Linear Transformations
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.problem}
(a) State the standard Schwarz reflection principle involving reflection across the real axis.

(b) Give a linear fractional transformation $T$ mapping $\DD$ to $\HH$.
Let $g(z) = \bar z$, and show
$$
(T^{-1} \circ g \circ T)(z) = 1/\bar z.
$$

(c) Suppose that $f$ is holomorphic on $\DD$, continuous on $\bar \DD$, and real on $S^1$.
Show that $f$ must be constant.
:::

::: {.solution}
Write $\Omega^\pm \coloneqq \Omega \cap \{\pm\Im z > 0\}$ and $I \coloneqq \Omega\cap\RR$ for a region $\Omega$ symmetric about $\RR$.

::: pf

::: pf-step
(a) If $f$ is holomorphic on $\Omega^+$, extends continuously to $\Omega^+\cup I$, and is real on $I$, then
$$
F(z) \coloneqq \begin{cases} f(z) & z\in \Omega^+\cup I \\ \overline{f(\bar z)} & z\in\Omega^- \end{cases}
$$
is holomorphic on $\Omega$.

::: pf-proof
This is the Schwarz reflection principle.
:::

:::

::: {.pf-step #mobius}
(b) $T(z) \coloneqq i\,\dfrac{1+z}{1-z}$ maps $\DD$ onto $\HH$, with $T^{-1}(w) = \dfrac{w-i}{w+i}$, and $(T^{-1}\circ g\circ T)(z) = 1/\bar z$.

::: pf-proof
For $\abs{z}<1$,
$$
\Im T(z) = \Re\frac{(1+z)(1-\bar z)}{\abs{1-z}^2} = \frac{1-\abs{z}^2}{\abs{1-z}^2} > 0,
$$
and solving $w = T(z)$ for $z$ gives the stated inverse, which maps $\HH$ into $\DD$ because $\abs{w-i}<\abs{w+i}$ for $\Im w>0$.
Since $\overline{T(z)} = -i\,\dfrac{1+\bar z}{1-\bar z}$,
$$
T^{-1}\qty{\overline{T(z)}}
= \frac{-i\frac{1+\bar z}{1-\bar z} - i}{-i\frac{1+\bar z}{1-\bar z} + i}
= \frac{(1+\bar z) + (1-\bar z)}{(1+\bar z) - (1-\bar z)}
= \frac{1}{\bar z}.
$$
:::

:::

::: {.pf-step #extension}
The function
$$
F(z) \coloneqq \begin{cases} f(z) & \abs{z}\le 1 \\ \overline{f(1/\bar z)} & \abs{z}>1 \end{cases}
$$
is entire.

::: pf-proof
$F$ is holomorphic on $\abs{z}<1$ and on $\abs{z}>1$, and continuous on $\CC$ because $f$ is real on $S^1$ and $1/\bar z = z$ there.
Let $h \coloneqq f\circ T^{-1}$ on $\HH\cup\RR$; by step [](#mobius){.pf-ref}, $T^{-1}$ maps $\RR$ onto $S^1\setminus\{1\}$, so $h$ is holomorphic on $\HH$, continuous up to $\RR$, and real on $\RR$.
By the reflection principle, $w\mapsto\overline{h(\bar w)}$ extends $h$ holomorphically to $\CC\setminus\{-i\}$, the image of $\CC\setminus\{1\}$ under $T$.
By step [](#mobius){.pf-ref}, for $\Im w<0$ the point $z = T^{-1}(w)$ satisfies $T^{-1}(\bar w) = 1/\bar z$, so $\overline{h(\bar w)} = \overline{f(1/\bar z)} = F(z)$.
Hence $F = (\text{extension of } h)\circ T$ is holomorphic on $\CC\setminus\{1\}$.
The point $1$ is an isolated singularity at which $F$ is continuous, hence bounded nearby, so it is removable.
:::

:::

::: pf-step
(c) $f$ is constant.

::: pf-proof
For $\abs{z}\ge1$, $\abs{F(z)} = \abs{f(1/\bar z)} \le \max_{\bar\DD}\abs{f}$, and on $\bar\DD$ the same bound holds since $\bar\DD$ is compact.
So the entire function $F$ of step [](#extension){.pf-ref} is bounded, hence constant by Liouville's theorem, and $f = F|_{\bar\DD}$ is constant.
:::

:::

:::

:::
