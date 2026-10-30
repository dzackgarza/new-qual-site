---
schema: qual/card@1
id: P-BKS07-4B
kind: problem
title: A finite-dimensional differentiation-stable space of entire functions contains a nowhere-vanishing function
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $E$ be the $\CC$-vector space of entire functions.
Let $V$ be a nonzero finite-dimensional $\CC$-subspace of $E$ with the property that $f \in V$ implies $f' \in V$. Prove that $V$ contains a function that is everywhere nonzero.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Differentiation $T(f)=f'$ is a linear map $V\to V$, and it has an eigenvector $f\ne0$ with eigenvalue $\lambda\in\CC$.

::: pf-proof

$T$ maps $V$ to $V$ by hypothesis and is linear. A linear operator on a nonzero finite-dimensional complex vector space has an eigenvalue, because its characteristic polynomial has a root in $\CC$.

:::

:::

::: pf-qed

For the $f$ of step [](#s1){.pf-ref}, $(fe^{-\lambda z})'=(f'-\lambda f)e^{-\lambda z}=0$, so $f=ce^{\lambda z}$ for a constant $c$, and $c\ne0$ because $f\ne0$. This function has no zeros.

:::

:::

:::
