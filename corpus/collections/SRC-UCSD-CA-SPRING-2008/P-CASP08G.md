---
schema: qual/card@1
id: P-CASP08G
kind: problem
title: Monotone boundary data give convergent Dirichlet solutions
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Boundary Values
relations: []
review: draft
---

::: {.problem}
Let $G$ be a Dirichlet region in the plane (i.e. a region in which the Dirichlet problem can be solved). Let
$$
\phi_1 \le \phi_2 \le \cdots \le \phi_n \le \cdots
$$
be a sequence of continuous functions on $\partial_\infty G$ and suppose that there exists a continuous function $\phi$ on $\partial_\infty G$ such that for every $z \in \partial_\infty G$
$$
\phi(z) = \lim_{n \to \infty} \phi_n(z)
$$
(pointwise!). Let $u_n$ and $u$ be the solutions to the Dirichlet problem in $G$ with data $\phi_n$ and $\phi$, respectively. Show that $u_n \to u$ in $\operatorname{Har}(G)$.
:::

::: {.solution}
::: pf

::: {.pf-step #dini}
$\phi_n \to \phi$ uniformly on $\partial_\infty G$.

::: pf-proof
$\partial_\infty G$ is a closed subset of the compact space $\CC_\infty$, so it is compact. The functions $\phi-\phi_n$ are continuous, nonnegative, and decrease pointwise to $0$. Dini's theorem gives uniform convergence.
:::

:::

::: {.pf-step #max}
$\sup_{G}\abs{u-u_n} \le \sup_{\partial_\infty G}\abs{\phi-\phi_n}$.

::: pf-proof
$u-u_n$ is harmonic in $G$ and extends continuously to $\partial_\infty G$ with boundary values $\phi-\phi_n$. The maximum principle (Conway X.2.12), applied to $u-u_n$ and to $u_n-u$, gives the bound.
:::

:::

::: pf-qed
By steps [](#dini){.pf-ref} and [](#max){.pf-ref}, $u_n \to u$ uniformly on $G$, so in particular uniformly on compact subsets of $G$. That is convergence in $\operatorname{Har}(G)$.
:::

:::
:::
