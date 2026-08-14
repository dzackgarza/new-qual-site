---
schema: qual/card@1
id: T-NRSFZ
kind: theorem
title: "Existence of $\\log(f)$ on domains"
classification:
  areas:
  - complex-analysis
  topics:
  - complex-logarithm
  - holomorphic-functions
relations: []
review: draft
---
:::{.theorem title="Existence of $\log(f)$ on domains"}
If $\Omega$ is a connected domain with $f\in \OO\units(\Omega)$ an invertible regular function with 
\[
\int_\gamma {f'\over f} = 0
\]
for all $\gamma \subseteq \Omega$, then

- There exists a holomorphic $g:\Omega\to \CC$ such that $g = \log(f)$ and $e^g = f$.

- $g' = {f'\over f}$, yielding an explicit formula
\[
g(z) = g(z_0) + \int_{z_0}^z {f'(\xi) \over \xi}\dxi
.\]

:::
