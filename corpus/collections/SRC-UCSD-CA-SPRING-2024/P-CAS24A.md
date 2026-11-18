---
schema: qual/card@1
id: P-CAS24A
kind: problem
title: $\abs{f}^2+\abs{f}$ harmonic implies $f$ constant
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be a holomorphic function on a region $G$ such that $\abs{f}^2 + \abs{f}$ is harmonic on $G$.
Prove $f$ is constant.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own Laplacian computation follows, with the two identities, the consequence $f'=0$ and the identity theorem as separate steps.

Let $G$ be a region and $f$ holomorphic on $G$ with $\abs{f}^{2}+\abs{f}$ harmonic.

::: pf

::: {.pf-step #laplacians}
On the open set $\Omega=\theset{z\in G\mid f(z)\ne0}$ one has $\Delta\abs{f}^{2}=4\abs{f'}^{2}$ and $\Delta\abs{f}=\dfrac{\abs{f'}^{2}}{\abs{f}}$.

::: pf-proof
$u=\abs{f}^{2}=f\bar f$ is smooth with $u_{z\bar z}=\abs{f'}^{2}$, so $\Delta u=4u_{z\bar z}=4\abs{f'}^{2}$. On $\Omega$ the function $\log\abs{f}$ is harmonic, since it is the real part of the holomorphic function $\log f$ on a disc where $f$ has no zero; and $\abs{f}=e^{\log\abs{f}}$, so $\Delta\abs{f}=\abs{f}\cdot\abs{\nabla\log\abs{f}}^{2}$, while $\nabla\log\abs{f}$ has modulus $\abs{f'/f}$. Hence $\Delta\abs{f}=\abs{f}\cdot\abs{f'}^{2}/\abs{f}^{2}=\abs{f'}^{2}/\abs{f}$.
:::

:::

::: {.pf-step #zero-derivative}
$f'=0$ on $\Omega$.

::: pf-proof
$0=\Delta\big(\abs{f}^{2}+\abs{f}\big)=4\abs{f'}^{2}+\dfrac{\abs{f'}^{2}}{\abs{f}}=\abs{f'}^{2}\Big(4+\dfrac{1}{\abs{f}}\Big)$ on $\Omega$, by step [](#laplacians){.pf-ref}. The factor $4+1/\abs{f}$ is a positive real number at every point of $\Omega$, so $\abs{f'}^{2}=0$ and hence $f'=0$ there.
:::

:::

::: {.pf-step #constant}
$f$ is constant on $G$.

::: pf-proof
If $f\equiv0$ this is immediate. Otherwise $\Omega$ is a nonempty open subset of the region $G$, and $f'=0$ on $\Omega$ by step [](#zero-derivative){.pf-ref}, so $f$ is constant on each component of the open set $\Omega$; by the identity theorem a holomorphic function constant on a nonempty open subset of the region $G$ is constant on $G$.
:::

:::

::: {.pf-qed}
$f$ is constant on $G$ by step [](#constant){.pf-ref}.
:::

:::

:::
