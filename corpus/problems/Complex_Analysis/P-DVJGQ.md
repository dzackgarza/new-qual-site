---
schema: qual/card@1
id: P-DVJGQ
kind: problem
title: Implicit function theorem from the inverse function theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Multivariable Calculus
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
State the most general version of the implicit function theorem for real functions and outline how it can be proved using the inverse function theorem.
:::

::: {.solution}

::: {.theorem title="Implicit function theorem"}
Let $W\subseteq\RR^n\times\RR^m$ be open, let $F:W\to\RR^m$ be $C^k$ with $k\ge1$, and let $(a,b)\in W$ with $F(a,b)=0$.
If the $m\times m$ matrix $\frac{\partial F}{\partial y}(a,b)$ of partial derivatives in the last $m$ variables is invertible, then there are open neighborhoods $U\ni a$ and $V\ni b$ and a $C^k$ function $g:U\to V$ such that, for $(x,y)\in U\times V$, $F(x,y)=0$ if and only if $y=g(x)$.
:::

Define $\Phi:W\to\RR^n\times\RR^m$ by $\Phi(x,y)\coloneqq(x,F(x,y))$.

::: pf

::: {.pf-step #jacobian}
$D\Phi(a,b)$ is invertible.

::: pf-proof
$$
D\Phi(a,b)=\begin{pmatrix} I_n & 0 \\ \frac{\partial F}{\partial x}(a,b) & \frac{\partial F}{\partial y}(a,b) \end{pmatrix}
$$
has determinant $\det\frac{\partial F}{\partial y}(a,b)\ne0$.
:::

:::

::: {.pf-step #inverse}
There are open sets $W_0\ni(a,b)$ and $Z_0\ni(a,0)$ such that $\Phi:W_0\to Z_0$ is a bijection with $C^k$ inverse $\Psi$, and $\Psi(x,z)=(x,\psi(x,z))$ with $F(x,\psi(x,z))=z$.

::: pf-proof
The inverse function theorem applies by step [](#jacobian){.pf-ref}.
$\Phi$ preserves the first $n$ coordinates, so $\Psi$ does too; applying $\Phi$ to $\Psi(x,z)$ gives the identity.
:::

:::

::: pf-step
With $U\times V\subseteq W_0$ a product neighborhood of $(a,b)$, shrunk so that $(x,0)\in Z_0$ and $\psi(x,0)\in V$ for $x\in U$, the map $g(x)\coloneqq\psi(x,0)$ has the stated properties.

::: pf-proof
$g$ is $C^k$ because $\psi$ is, and $F(x,g(x))=0$ by step [](#inverse){.pf-ref}; $g(a)=b$ because $\Phi(a,b)=(a,0)$.
Such $U$ exists by continuity of $\psi$ at $(a,0)$.
Conversely, if $(x,y)\in U\times V$ and $F(x,y)=0$, then $\Phi(x,y)=(x,0)=\Phi(x,g(x))$ with both points in $W_0$, so $y=g(x)$ by injectivity of $\Phi$ on $W_0$.
:::

:::

:::

:::
