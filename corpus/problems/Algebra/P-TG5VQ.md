---
schema: qual/card@1
id: P-TG5VQ
kind: problem
title: Solving linear ODEs with constant coefficients using linear algebra
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
How can a linear ordinary differential equation with constant coefficients be solved using linear algebra?
:::

::: {.solution}
Consider a scalar equation of order $n$,
$$
y^{(n)}+a_{n-1}y^{(n-1)}+\cdots+a_1y'+a_0y=0,
$$
and its state vector $Y=(y,y',\ldots,y^{(n-1)})^T$.

::: pf

::: {.pf-step #system}
The equation is equivalent to the first-order system $Y'=AY$, where $A$ is the companion matrix
$$
A=
\begin{pmatrix}
0&1&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&&&\ddots&\vdots\\
0&0&0&\cdots&1\\
-a_0&-a_1&-a_2&\cdots&-a_{n-1}
\end{pmatrix}.
$$

::: pf-proof
The first $n-1$ rows of $Y'=AY$ say that each entry of $Y$ is the derivative of the previous one, and the last row is the equation solved for $y^{(n)}$.
:::

:::

::: {.pf-step #exponential}
The solution with initial condition $Y(0)=Y_0$ is $Y(t)=e^{tA}Y_0$.

::: pf-proof
The series $e^{tA}=\sum_{k\ge0}t^kA^k/k!$ converges absolutely and $\frac{d}{dt}e^{tA}=Ae^{tA}$, so $e^{tA}Y_0$ is a solution with value $Y_0$ at $t=0$.
Uniqueness holds because for any solution $Y$, $\frac{d}{dt}\bigl(e^{-tA}Y(t)\bigr)=0$.
:::

:::

::: pf-step
If $A=PDP^{-1}$ with $D$ diagonal with entries $\lambda_i$, then $e^{tA}=Pe^{tD}P^{-1}$, and $e^{tD}$ is diagonal with entries $e^{\lambda_i t}$.

::: pf-proof
Since $(PDP^{-1})^k=PD^kP^{-1}$, the series for $e^{tA}$ is $P\bigl(\sum_k t^kD^k/k!\bigr)P^{-1}$, and the series for $e^{tD}$ is computed entrywise.
:::

:::

::: pf-step
In general, for a Jordan block $J=\lambda I+N$ with $N^r=0$,
$$
e^{tJ}=e^{\lambda t}\sum_{k=0}^{r-1}\frac{t^kN^k}{k!},
$$
which produces the solutions $t^ke^{\lambda t}$ attached to a repeated root $\lambda$ of the characteristic polynomial.

::: pf-proof
Since $\lambda I$ and $N$ commute, $e^{tJ}=e^{\lambda t}e^{tN}$, and the series for $e^{tN}$ stops at $k=r-1$.
Putting $A$ in Jordan form $A=PJ_AP^{-1}$ and applying this to each block computes $e^{tA}=Pe^{tJ_A}P^{-1}$, and with step [](#exponential){.pf-ref} this solves the system of step [](#system){.pf-ref}.
:::

:::

:::

:::
