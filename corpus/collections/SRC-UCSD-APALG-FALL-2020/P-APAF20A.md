---
schema: qual/card@1
id: P-APAF20A
kind: problem
title: Jordan form of a map on $\CC^{20}$ with $\phi^3=\phi^2$ and eight-dimensional eigenspaces
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
A linear map $\phi\colon\CC^{20}\to\CC^{20}$ has the property that $\phi^3=\phi^2$.

(a) Show that if $\lambda$ is an eigenvalue of $\phi$ then $\lambda=0$ or $\lambda=1$.

Now suppose furthermore that $\dim E(0,\phi)=\dim E(1,\phi)=8$.
[Here $E(\lambda,\phi)\subseteq\CC^{20}$ denotes the eigenspace of $\phi$ with eigenvalue $\lambda$.]

(b) Find, with justification, the Jordan Normal Form of $\phi$.

[For this question, “find the Jordan Normal form” means you should determine the sizes and multiplicities of the Jordan blocks. You should not attempt to describe a basis that puts $\phi$ in Jordan Normal Form.]
:::

::: {.solution}

::: pf

::: {.pf-step #minpoly}

The minimal polynomial of $\phi$ divides $x^2(x-1)$.

::: pf-proof

$\phi^3-\phi^2=0$, so $\phi$ is annihilated by $x^3-x^2=x^2(x-1)$, and the minimal polynomial divides every annihilating polynomial.

:::

:::

::: pf-step

(a) Every eigenvalue $\lambda$ of $\phi$ is $0$ or $1$.

::: pf-proof

If $\phi v=\lambda v$ with $v\ne0$, then $0=(\phi^3-\phi^2)v=(\lambda^3-\lambda^2)v$, so $\lambda^2(\lambda-1)=0$.

:::

:::

::: pf-step

(b) $\boxed{\text{The Jordan form of }\phi\text{ has four }2\times2\text{ blocks and four }1\times1\text{ blocks for }0\text{, and eight }1\times1\text{ blocks for }1.}$

::: pf-proof

The number of Jordan blocks for an eigenvalue equals the dimension of its eigenspace, so there are $8$ blocks for $0$ and $8$ for $1$. By step [](#minpoly){.pf-ref}, the largest block for $0$ has size at most $2$ and every block for $1$ has size $1$. The blocks for $1$ then fill $8$ dimensions, so the blocks for $0$ fill $20-8=12$. If $k$ of the $8$ blocks for $0$ have size $2$, then $2k+(8-k)=12$, so $k=4$.

:::

:::

:::
:::
