---
schema: qual/card@1
id: P-HCAX22
kind: problem
title: Conformal automorphisms of the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Mobius Transformations
relations: []
review: draft
---

::: {.problem}
Determine all conformal automorphisms of the unit disk.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the model automorphisms, the conjugation to fix $0$, Schwarz's lemma and the converse as separate steps.

::: pf

::: {.pf-step #model}
For $a\in\DD$ the map $\phi_{a}(z)=\dfrac{z-a}{1-\bar a z}$ is a biholomorphic self-map of $\DD$ with $\phi_{a}(a)=0$ and $\phi_{a}^{-1}=\phi_{-a}$.

::: pf-proof
The denominator does not vanish on $\DD$ because $\abs{\bar a z}<1$ when $\abs{z}<1$ and $\abs{a}<1$, so $\phi_{a}$ is holomorphic there. For $\abs{z}=1$ one has $\abs{z-a}=\abs{\bar z z-\bar z a}=\abs{1-\bar a z}$, so $\phi_{a}$ maps the unit circle into the unit circle; by the maximum and minimum modulus principles it maps $\DD$ into $\DD$ and the boundary to the boundary. A direct computation gives $\phi_{-a}\circ\phi_{a}=\mathrm{id}$, so $\phi_{a}$ is biholomorphic with the stated inverse, and $\phi_{a}(a)=0$.
:::

:::

::: {.pf-step #fix-zero}
If $F$ is a conformal automorphism of $\DD$ and $a=F^{-1}(0)$, then $H=F\circ\phi_{a}^{-1}$ is an automorphism of $\DD$ with $H(0)=0$.

::: pf-proof
$H$ is a composite of biholomorphisms of $\DD$, hence one, and $H(0)=F\big(\phi_{a}^{-1}(0)\big)=F(a)=0$.
:::

:::

::: {.pf-step #schwarz}
Such an $H$ satisfies $H(z)=e^{i\theta}z$ for some $\theta\in\RR$.

::: pf-proof
$H$ and $H^{-1}$ are holomorphic self-maps of $\DD$ fixing $0$ with $\abs{H}\le1$ and $\abs{H^{-1}}\le1$, so the Schwarz lemma gives $\abs{H(z)}\le\abs{z}$ and $\abs{H^{-1}(w)}\le\abs{w}$ for all $z,w$. Writing $w=H(z)$ in the second gives $\abs{z}\le\abs{H(z)}$, hence $\abs{H(z)}=\abs{z}$, and the equality case of the Schwarz lemma then makes $H$ a rotation $z\mapsto e^{i\theta}z$.
:::

:::

::: {.pf-step #converse}
Every map $F(z)=e^{i\theta}\dfrac{z-a}{1-\bar a z}$ with $a\in\DD$, $\theta\in\RR$ is a conformal automorphism of $\DD$.

::: pf-proof
It is the composite of the automorphism $\phi_{a}$ of step [](#model){.pf-ref} with the rotation $z\mapsto e^{i\theta}z$, which is biholomorphic on $\CC$ and preserves $\DD$.
:::

:::

::: {.pf-qed}
By steps [](#model){.pf-ref}--[](#schwarz){.pf-ref} every $F\in\operatorname{Aut}(\DD)$ has the form $F(z)=e^{i\theta}\phi_{a}(z)$ with $a=F^{-1}(0)$; by step [](#converse){.pf-ref} every map of that form is an automorphism. These are exactly the conformal automorphisms of $\DD$.
:::

:::

:::
