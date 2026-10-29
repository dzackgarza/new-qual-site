---
schema: qual/card@1
id: P-3YESG
kind: problem
title: Schwarz reflection across the real axis, and holomorphic functions real on
  the circle
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Fractional Linear Transformations
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
State the standard Schwarz reflection principle involving reflection across the real axis.

Give a linear fractional transformation $T$ mapping $\DD$ to $\HH$.
Let $g(z) = \bar z$, and show
$$
(T^{-1} \circ g \circ T)(z) = 1/\bar z
.$$

Suppose that $f$ is holomorphic on $\DD$, continuous on $\bar \DD$, and real on $S^1$.
Show that $f$ must be constant.
:::

::: {.solution}

::: pf

::: {.pf-step #reflection}
Schwarz reflection principle: let $\Omega\subseteq\HH$ be open, let $I\subseteq\RR$ be an open interval such that $\Omega^+\coloneqq\Omega\cup I$ is a neighborhood of $I$ in $\overline\HH$, and let $\Omega^-\coloneqq\theset{\bar z\st z\in\Omega}$. If $F$ is holomorphic on $\Omega$, continuous on $\Omega\cup I$, and real on $I$, then $F$ extends to a holomorphic function on $\Omega\cup I\cup\Omega^-$ by $F(\bar z)\coloneqq\overline{F(z)}$.

::: pf-proof
This is the statement asked for.
:::

:::

::: {.pf-step #cayley}
$T(z)=i\dfrac{1+z}{1-z}$ maps $\DD$ onto $\HH$ and $S^1\sm\theset{1}$ onto $\RR$, with inverse $T^{-1}(w)=\dfrac{w-i}{w+i}$.

::: pf-proof
Solving $w=i\frac{1+z}{1-z}$ for $z$ gives $T^{-1}$.
For real $w$, $\abs{w-i}=\abs{w+i}$, and for $\Im w>0$, $w$ is closer to $i$ than to $-i$, so $\abs{T^{-1}(w)}<1$ exactly on $\HH$ and $\abs{T^{-1}(w)}=1$ on $\RR$.
:::

:::

::: pf-step
$(T^{-1}\circ g\circ T)(z)=1/\bar z$.

::: pf-proof
$\overline{T(z)}=-i\frac{1+\bar z}{1-\bar z}$, so
$$
T^{-1}\qty(\overline{T(z)})=\frac{-i\frac{1+\bar z}{1-\bar z}-i}{-i\frac{1+\bar z}{1-\bar z}+i}=\frac{-i(1+\bar z)-i(1-\bar z)}{-i(1+\bar z)+i(1-\bar z)}=\frac{-2i}{-2i\bar z}=\frac1{\bar z}.
$$
:::

:::

::: pf-step
If $f$ is holomorphic on $\DD$, continuous on $\overline\DD$, and real on $S^1$, then $f$ is constant.

::: pf-proof
Let $F\coloneqq f\circ T^{-1}$.
By step [](#cayley){.pf-ref}, $F$ is holomorphic on $\HH$, continuous on $\HH\cup\RR$, and real on $\RR$.
By step [](#reflection){.pf-ref} with $\Omega=\HH$ and $I=\RR$, $F$ extends to an entire function with $F(\bar w)=\overline{F(w)}$.
Since $f$ is bounded on the compact set $\overline\DD$, $F$ is bounded on $\HH\cup\RR$, and by the reflection identity on all of $\CC$.
By Liouville's theorem $F$ is constant, so $f=F\circ T$ is constant on $\DD$, and by continuity on $\overline\DD$.
:::

:::

:::

:::
