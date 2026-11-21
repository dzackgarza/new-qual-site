---
schema: qual/card@1
id: P-CAF11C
kind: problem
title: "Schwarz-Pick type inequality for analytic functions mapping into the left half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that Phi(w) = (w+1)/(w-1) maps the left half-
    plane onto the disk by the computation |w+1|^2 < |w-1|^2 iff Re w < 0, that Phi is an
    involution so it is also onto, that g = Phi o f is holomorphic into the disk with g(0) =
    0 and obeys Schwarz's lemma, that f = (g+1)/(g-1), and the two bounds through the
    triangle inequality together with the monotonicity of t -> (1+t)/(1-t) and t ->
    (1-t)/(1+t) on [0,1), which the earlier prose used without stating. The argument is the
    card's own; no retained set is cited. No repair needed to the statement.
---

::: {.problem}
Let $f \in H(\DD)$ be nonconstant such that $f(\DD) \subset \{z \in \CC : \operatorname{Re} z < 0\}$ and $f(0) = -1$.
Prove that for any $z \in \DD$, $$\frac{1 - \abs{z}}{1 + \abs{z}} \leq \abs{f(z)} \leq \frac{1 + \abs{z}}{1 - \abs{z}}.$$
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Write $\DD$ for the unit disk, $H(\DD)$ for the holomorphic functions on it, and $\HH_{-}=\{w:\operatorname{Re}w<0\}$.

::: pf

::: {.pf-step #mobius}
$\Phi(w)=\dfrac{w+1}{w-1}$ is a holomorphic bijection of $\HH_{-}$ onto $\DD$, it is its own inverse, and $\Phi(-1)=0$.

::: pf-proof
For $w\ne1$,
$$
\abs{\Phi(w)}<1\iff\abs{w+1}^{2}<\abs{w-1}^{2}\iff\abs{w}^{2}+2\operatorname{Re}w+1<\abs{w}^{2}-2\operatorname{Re}w+1\iff\operatorname{Re}w<0,
$$
so $\Phi$ maps $\HH_{-}$ into $\DD$, and $\Phi$ is a Möbius transformation, hence injective. Its inverse: solving $u=(w+1)/(w-1)$ gives $u(w-1)=w+1$, that is $w(u-1)=u+1$ and $w=(u+1)/(u-1)=\Phi(u)$, so $\Phi\circ\Phi$ is the identity wherever defined and $\Phi$ maps $\DD$ onto $\HH_{-}$ as well. Finally $\Phi(-1)=0$.
:::

:::

::: {.pf-step #schwarz}
$g=\Phi\circ f$ is holomorphic on $\DD$ with $g(\DD)\subset\DD$ and $g(0)=0$; hence $\abs{g(z)}\le\abs{z}$.

::: pf-proof
$f$ is holomorphic and takes values in $\HH_{-}$, so $f$ never takes the value $1$ and $g=\Phi\circ f$ is holomorphic; by step [](#mobius){.pf-ref} it takes values in $\DD$, and $g(0)=\Phi(-1)=0$. Schwarz's lemma then gives $\abs{g(z)}\le\abs{z}$ for $\abs{z}<1$.
:::

:::

::: {.pf-step #invert}
$f(z)=\dfrac{g(z)+1}{g(z)-1}$ and $\abs{f(z)}=\dfrac{\abs{1+g(z)}}{\abs{1-g(z)}}$, with $\abs{g(z)}<1$ and $\abs{f(z)}>0$.

::: pf-proof
From $g=\Phi(f)=(f+1)/(f-1)$ one solves $g(f-1)=f+1$, giving $f(g-1)=g+1$ and the displayed formula. Since $\abs{g(z)}<1$ by step [](#schwarz){.pf-ref}, $1-g(z)\ne0$; and $\abs{f(z)}>0$ because $f$ takes values in $\HH_{-}$.
:::

:::

::: {.pf-step #upper}
$\abs{f(z)}\le\dfrac{1+\abs{z}}{1-\abs{z}}$.

::: pf-proof
With $t=\abs{g(z)}\in[0,1)$ the triangle inequality gives $\abs{1+g}\le1+t$ and $\abs{1-g}\ge1-t$, so
$$
\abs{f(z)}=\frac{\abs{1+g(z)}}{\abs{1-g(z)}}\le\frac{1+t}{1-t}.
$$
The function $t\mapsto\frac{1+t}{1-t}$ is increasing on $[0,1)$ — its derivative is $\frac{2}{(1-t)^{2}}>0$ — so $t\le\abs{z}$ from step [](#schwarz){.pf-ref} gives $\abs{f(z)}\le\frac{1+\abs{z}}{1-\abs{z}}$.
:::

:::

::: {.pf-step #lower}
$\abs{f(z)}\ge\dfrac{1-\abs{z}}{1+\abs{z}}$.

::: pf-proof
With $t=\abs{g(z)}\in[0,1)$ one has $\abs{1+g}\ge1-t$ and $\abs{1-g}\le1+t$, hence
$$
\abs{f(z)}\ge\frac{1-t}{1+t}.
$$
The function $t\mapsto\frac{1-t}{1+t}$ is decreasing on $[0,1)$ — its derivative is $\frac{-2}{(1+t)^{2}}<0$ — so $t\le\abs{z}$ gives $\abs{f(z)}\ge\frac{1-\abs{z}}{1+\abs{z}}$.
:::

:::

::: {.pf-step}
$\dfrac{1-\abs{z}}{1+\abs{z}}\le\abs{f(z)}\le\dfrac{1+\abs{z}}{1-\abs{z}}$ for every $z\in\DD$.

::: pf-proof
Steps [](#lower){.pf-ref} and [](#upper){.pf-ref} are the two inequalities.
:::

:::

:::
:::
