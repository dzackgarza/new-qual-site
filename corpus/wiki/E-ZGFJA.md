---
schema: qual/card@1
id: E-ZGFJA
kind: exercise
title: "More juggling"
classification:
  areas:
  - complex-analysis
  topics:
  - blaschke-factors
  - schwarz-lemma
  - maximum-modulus-principle
relations: []
review: draft
solved: true
---
:::{.exercise title="More juggling"}
Suppose $f:\DD\to \DD$ with $f(0) = 0$ and that there exists an $r\in (0, 1)$ with $f(r) = f(-r) = 0$.
Show that 
\[
\abs{f(z)} \leq \abs{z^2-r^2 \over 1-r^2 z^2}
.\]

:::

:::{.solution}
The key observation is that this factors:
\[
{z^2 - r^2 \over 1-r^2 z^2} = {r-z\over 1+rz}{-r-z\over 1-rz} = \psi_{r}(z) \psi_{-r}(z)
,\]
so this inequality will follow from Schwarz on $g(z) \da f(z)/\psi_a(z)\psi_{-a}(z)$.
Schwarz does apply since $\abs{f}\leq 1$ in $\DD$ and $\abs{\psi_a(z)} = 1$ on $S^1$, so $\abs{g(z)} \leq 1$ on $S^1$ and by the MMP this inequality holds in all of $\DD$.
So $\abs{g(z)}\leq \abs{z}$ and unwinding gives the desired inequality.
:::
