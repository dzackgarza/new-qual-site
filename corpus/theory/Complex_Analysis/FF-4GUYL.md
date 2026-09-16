---
schema: qual/card@1
id: FF-4GUYL
kind: fact
title: Automorphisms of the unit disc
prompts:
- What is the general form of an automorphism of the unit disc?
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Biholomorphisms
relations: []
review: draft
---

::: {.fact}
The biholomorphisms $\DD\to\DD$ are exactly the maps
$$
f(z)=\lambda\,\frac{\alpha-z}{1-\bar\alpha z},\qquad \alpha\in\DD,\ \lambda\in\CC,\ \abs{\lambda}=1.
$$
:::

::: {.proof}
Write $\psi_\alpha(z)\coloneqq\frac{\alpha-z}{1-\bar\alpha z}$ for the [[D-MFPYG|Blaschke factor]] at $\alpha\in\DD$; it is a biholomorphism $\DD\to\DD$ with $\psi_\alpha\circ\psi_\alpha=\operatorname{id}$, so $\lambda\psi_\alpha$ is a biholomorphism of $\DD$ for $\abs{\lambda}=1$.

Conversely, let $f\colon\DD\to\DD$ be a biholomorphism, let $\alpha\coloneqq f^{-1}(0)\in\DD$, and put $g\coloneqq f\circ\psi_\alpha$.
Then $g$ is a biholomorphism of $\DD$ with $g(0)=f(\alpha)=0$.
The [[T-DAETF|Schwarz lemma]] applied to $g$ and to $g^{-1}$ gives $\abs{g'(0)}\le1$ and $\abs{(g^{-1})'(0)}=1/\abs{g'(0)}\le1$, so $\abs{g'(0)}=1$ and $g(z)=\lambda z$ with $\abs{\lambda}=1$.
Hence $f=g\circ\psi_\alpha=\lambda\psi_\alpha$.
:::
