---
schema: qual/card@1
id: P-CAFA17E
kind: problem
title: "The Riemann surface of the logarithm is simply connected"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Prove that the Riemann surface of the complete analytic function associated to a branch of $\log z$ is simply connected.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own model of the Riemann surface follows, with the model, the biholomorphism and the simple connectivity as separate steps.

::: pf

::: {.pf-step #model}
The complete analytic function of a branch of $\log z$ has Riemann surface $\mathcal R=\theset{(z,w)\in\CC^{*}\times\CC\mid e^{w}=z}$, on which $L(z,w)=w$ is single valued and holomorphic.

::: pf-proof
The analytic continuation of a local branch of $\log$ along curves in $\CC^{*}$ produces exactly the pairs (value, endpoint): every branch at $z$ has the form $w$ with $e^{w}=z$, and conversely each such $w$ is reached by continuing along a curve from the base point, by the monodromy theorem applied to $\CC$ (simply connected) after lifting. The second projection of $\CC^{*}\times\CC$ restricts to a holomorphic function $L$ on $\mathcal R$, whose value at $(z,w)$ is the chosen logarithm $w$; and $\mathcal R$ is a one-dimensional complex manifold, being a closed submanifold of $\CC^{*}\times\CC$ cut out by the holomorphic equation $e^{w}-z=0$ with nonzero gradient.
:::

:::

::: {.pf-step #biholomorphic}
$\Phi:\CC\to\mathcal R$, $\Phi(w)=(e^{w},w)$, is a biholomorphism with inverse the second projection.

::: pf-proof
$\Phi$ is holomorphic, since both coordinates are. Its image lies in $\mathcal R$ because $e^{w}=z$ holds by definition, and it is injective because $w$ is recovered from $(e^{w},w)$. It is surjective onto $\mathcal R$: a point of $\mathcal R$ is $(z,w)$ with $e^{w}=z$, which is $\Phi(w)$. The second projection $\mathcal R\to\CC$ is holomorphic as a restriction of the projection, and it is the two-sided inverse of $\Phi$; so $\Phi$ is a biholomorphism.
:::

:::

::: {.pf-qed}
$\mathcal R$ is biholomorphic to $\CC$ by step [](#biholomorphic){.pf-ref}, and $\CC$ is simply connected; simple connectivity is a homeomorphism invariant, so the Riemann surface of the complete logarithm is simply connected.
:::

:::

:::
