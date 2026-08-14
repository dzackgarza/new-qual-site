---
schema: qual/card@1
id: E-AZSMO
kind: exercise
title: "Sublinear growth"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - cauchy-estimates
relations: []
review: draft
---
:::{.exercise title="Sublinear growth"}
Suppose that $f$ is entire and $f$ has sublinear growth in the following sense:
\[
\abs{f(z)\over z}\to 0
\text{ as } \abs{z}\to \infty
.\]
Show that $f$ must be constant.

:::

:::{.solution title="Direct bound"}
Claim: $f'(z_0) = 0$ for every $z_0\in \CC$, so $f'\equiv 0$, making $f$ constant.
Fix $z_0$, then define
\[
g(z) \da 
\begin{cases}
{f(z) - f(0) \over z-0} & z\neq 0 
\\
f'(0) & z=0.
\end{cases}
.\]
Note that for $z\neq 0$,
\[
\abs{g(z)} \da \abs{f(z) - f(0)\over z} \leq \abs{f(z) \over z} + \abs{f(0)\over z} \convergesto{\abs{z} \to \infty }0
,\]
where we've used the assumption in the last step.
So for $\abs{z}\geq R_\eps$ large enough, $\abs{g(z)} < \eps$.
In particular, $\abs{g(z)}<\eps$ on the circle $\abs{z} = R_\eps$, and by the MMP $\abs{g(z)} < \eps$ in the disc $\abs{z}\leq R_\eps$.
Taking $\eps\to 0$ yields $g(z) = 0$ for all $z\in \CC$, so $f(z) = f(0)$ is a constant for all $z$.
:::

:::{.solution title="Cauchy bound"}
Claim: $f'(z) \equiv 0$.
Choose $R = R(\eps) \gg 1$ so that $\abs{f(z)} \leq \eps \abs{z}$ for $\abs{z} \geq R$, and apply Cauchy's formula:
\[
\abs{f'(z)} 
&= \abs{{1\over 2\pi i } \int_{\abs \xi = R} { f(\xi) \over (\xi - z)^2 }\dxi  } \\
&\leq {1\over 2\pi} \int_{\abs \xi = R} { \abs{ f(\xi) } \over \abs{\xi - z}^2 } \dxi  \\
&\leq {1\over 2\pi} \int_{\abs \xi = R} { \eps \abs{\xi} \over \qty{R - \abs{z}^2 } } \dxi  \\
&= {1\over 2\pi} \qty{\eps R\over \qty{R-\abs{z}}^2 } \cdot 2\pi R \\
&= \bigo\qty{\eps R^2\over R^2} = \bigo(\eps) \\
&\convergesto{\eps\to 0} 0
.\]

:::

