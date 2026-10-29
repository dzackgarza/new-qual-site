---
schema: qual/card@1
id: P-5UKXY
kind: problem
title: A conformal map from $\{\abs{z}<1,\ \abs{z-1/2}>1/2\}$ onto $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find a conformal map from $\theset{z\in \CC \suchthat \abs{z} < 1,\, \abs{z - \frac{1}{2}} > \frac{1}{2} }$ to $\DD$.
:::

::: {.solution}
Let $\Omega$ be the given region.
Both boundary circles pass through $1$.

::: pf

::: {.pf-step #strip}
The Möbius map $T(z)=\frac{1}{1-z}$ sends $\Omega$ biholomorphically onto the strip $S\coloneqq\theset{\tfrac12<\Re w<1}$.

::: pf-proof
If $w=T(z)$, then $z = \frac{w-1}{w}$, so
$$
\abs{z}=1 \iff \abs{w-1}=\abs{w} \iff \Re w=\tfrac12,
\qquad
\abs{z-\tfrac12}=\tfrac12 \iff \abs{w-2}=\abs{w} \iff \Re w=1.
$$
So $T$ maps the two boundary circles onto the lines $\Re w=\frac12$ and $\Re w=1$, and $\Omega$ onto one of the three components of their complement.
The point $z=-\frac12\in\Omega$ goes to $w=\frac23$, so $T(\Omega)=S$.
:::

:::

::: {.pf-step #half-plane}
$E(w)=\exp\bigl(2\pi i(w-\tfrac12)\bigr)$ maps $S$ biholomorphically onto the upper half-plane $\HH$.

::: pf-proof
Write $w=\frac12+s+it$ with $0<s<\frac12$ and $t\in\RR$.
Then $E(w)=e^{-2\pi t}e^{2\pi i s}$ has modulus $e^{-2\pi t}\in(0,\infty)$ and argument $2\pi s\in(0,\pi)$.
The pair $(s,t)$ is determined by the modulus and argument, so $E$ is a bijection from $S$ onto $\HH$.
:::

:::

::: pf-step
A conformal map from $\Omega$ onto $\DD$ is
$$
\boxed{
z\longmapsto
\frac{
\exp\!\left(2\pi i\left(\frac{1}{1-z}-\frac12\right)\right)-i
}{
\exp\!\left(2\pi i\left(\frac{1}{1-z}-\frac12\right)\right)+i
}}.
$$

::: pf-proof
This is $C\circ E\circ T$, where the Cayley map $C(\zeta)=\frac{\zeta-i}{\zeta+i}$ maps $\HH$ biholomorphically onto $\DD$.
Steps [](#strip){.pf-ref} and [](#half-plane){.pf-ref} give the other two factors.
:::

:::

:::

:::
