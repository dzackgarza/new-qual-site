---
schema: qual/card@1
id: FF-UT5GL
kind: fact
title: Riesz representation theorem for Hilbert spaces
prompts:
- What is the Riesz Representation theorem?
classification:
  areas:
  - real-analysis
  topics:
  - Riesz Representation
  - Hilbert Spaces
  - Dual Spaces
relations: []
review: draft
---

::: {.fact}
Let $H$ be a [[D-7QQUO|Hilbert space]] over $\CC$ with inner product $\inner{\cdot}{\cdot}$ linear in the first argument, and let $\varphi \in H\dual$ be an element of its [[D-PQIQO|dual]].
Then there exists a unique $f\in H$ such that $\varphi(x) = \inner{x}{f}$ for all $x\in H$, and $\norm{f}_H = \norm{\varphi}_{H\dual}$, the [[D-T4LOC|dual norm]] of $\varphi$.
:::
