---
schema: qual/card@1
id: E-AZSMO
kind: problem
title: An entire function with $f(z)/z\to0$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Cauchy Estimates
relations: []
review: draft
---

::: {.exercise}
Suppose that $f$ is entire and $f$ has sublinear growth in the following sense:
\[
\abs{f(z)\over z}\to 0
\text{ as } \abs{z}\to \infty
.\]
Show that $f$ must be constant.

:::

::: {.solution title="Direct bound"}
Define
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
The function $g$ is entire, since $f(z)-f(0)$ vanishes at $0$.
Given $\eps>0$, there is $R_\eps$ with $\abs{g(z)} < \eps$ for $\abs{z}\geq R_\eps$.
Fix $z\in\CC$ and let $R\geq\max(R_\eps,\abs z)$. Then $\abs{g}<\eps$ on the circle of radius $R$, so by the maximum modulus principle $\abs{g(z)} < \eps$.
Since $\eps$ is arbitrary, $g(z) = 0$ for all $z\in \CC$, so $f(z) = f(0)$ is a constant for all $z$.
:::

::: {.solution title="Cauchy bound"}
Claim: $f'(z) \equiv 0$.
Fix $z$ and $\eps>0$. Choose $R \geq 2\abs z$ so that $\abs{f(\xi)} \leq \eps \abs{\xi}$ for $\abs{\xi} \geq R$, and apply Cauchy's formula:
\[
\abs{f'(z)} 
&= \abs{{1\over 2\pi i } \int_{\abs \xi = R} { f(\xi) \over (\xi - z)^2 }\dxi  } \\
&\leq {1\over 2\pi} \int_{\abs \xi = R} { \abs{ f(\xi) } \over \abs{\xi - z}^2 } \abs{\dxi}  \\
&\leq {1\over 2\pi} \int_{\abs \xi = R} { \eps \abs{\xi} \over \qty{R - \abs{z}}^2 } \abs{\dxi}  \\
&= {1\over 2\pi} \qty{\eps R\over \qty{R-\abs{z}}^2 } \cdot 2\pi R \\
&\leq 4\eps
,\]
using $R-\abs z\geq R/2$. Since $\eps$ is arbitrary, $f'(z)=0$; as $z$ is arbitrary, $f$ is constant.

:::

