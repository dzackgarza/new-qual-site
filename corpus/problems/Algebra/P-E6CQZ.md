---
schema: qual/card@1
id: P-E6CQZ
kind: problem
title: Stabilizers for $\SL_2(\RR)$ acting on $\RR^2$ and by Möbius transformations
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Matrix Groups
  - Orbit-Stabilizer
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Consider $\SL_2(\RR)$ acting on $\RR^2$ by matrix multiplication.
What is the stabiliser of a point?
Does it depend which point?
Do you know what sort of subgroup this is?
What if $\SL_2(\RR)$ acts by Möbius transformations instead?
:::

::: {.solution}

::: pf

::: pf-step
For the linear action, $\Stab(0)=\SL_2(\RR)$.

::: pf-proof
Every linear map fixes $0$.
:::

:::

::: {.pf-step #e1}
$\Stab(e_1)=\left\{\begin{pmatrix}1&t\\0&1\end{pmatrix}:t\in\RR\right\}$, a unipotent subgroup isomorphic to $(\RR,+)$.

::: pf-proof
A matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ fixes $e_1$ exactly when $a=1$ and $c=0$, and then $\det=1$ forces $d=1$.
The map $t\mapsto\begin{pmatrix}1&t\\0&1\end{pmatrix}$ is an isomorphism from $(\RR,+)$.
:::

:::

::: pf-step
For the linear action, the stabilizer of a point $v\ne0$ is $g\,\Stab(e_1)\,g^{-1}$ for any $g\in\SL_2(\RR)$ with $ge_1=v$; thus all nonzero-point stabilizers are conjugate unipotent subgroups isomorphic to $(\RR,+)$.

::: pf-proof
$\SL_2(\RR)$ acts transitively on $\RR^2\setminus\{0\}$: extend $v$ to a basis $v,w$ and scale $w$ so that $\det(v\ w)=1$.
Stabilizers of points in one orbit are conjugate by the elements carrying one point to the other, and step [](#e1){.pf-ref} identifies $\Stab(e_1)$.
:::

:::

::: pf-step
For the Möbius action $z\mapsto\frac{az+b}{cz+d}$ on the upper half-plane $\HH$, the action is transitive and every stabilizer is conjugate to $\Stab(i)=\left\{\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix}:\theta\in\RR\right\}\cong\SO(2)$.

::: pf-proof
For $x+iy\in\HH$, the matrix $\begin{pmatrix}\sqrt y&x/\sqrt y\\0&1/\sqrt y\end{pmatrix}$ sends $i$ to $x+iy$, so the action is transitive.
The equation $\frac{ai+b}{ci+d}=i$ means $ai+b=-c+di$, that is, $a=d$ and $b=-c$; with $a^2+b^2=1$ this is the rotation group $\SO(2)$.
:::

:::

::: pf-step
On the boundary $\PP^1(\RR)=\RR\cup\{\infty\}$, the action is transitive and every stabilizer is conjugate to the Borel subgroup $\Stab(\infty)=\left\{\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix}:a\in\RR^\times,\ b\in\RR\right\}$.

::: pf-proof
$\SL_2(\RR)$ acts transitively on lines in $\RR^2$, which are the points of $\PP^1(\RR)$.
A matrix fixes $\infty$ exactly when $c=0$, and then $d=a^{-1}$.
:::

:::

:::

:::
