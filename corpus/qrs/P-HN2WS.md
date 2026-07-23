---
schema: qual/card@1
id: P-HN2WS
kind: problem
title: "Show that"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Show that
\[
\int_0^{\infty} {\cos(x) \over x^2 + b^2}\dx = {\pi e^{-b} \over 2b}
.\]
:::

:::{.solution}
\envlist

- Let $I$ be the integral over $\RR$.
  Since $f(x)$ is even, the original integral is ${1\over 2}I$.

- Write $f(z) = e^{iz} / (z^2 + b^2)$.
  Take a semicircular contour $\Gamma \da \gamma_1 + \gamma_2$ where $\gamma_1$ is $[-R, R]$ on $\RR$ and $\gamma_2$ is the usual half-circle of radius $R$.

- Claim: $\int_{\gamma_2} f \converges{R\to\infty}\too 0$, so $\int_\Gamma \to \int_\RR f(z)$.
  - Easy estimate, just be careful with the $i$ in the exponent:
  \[
  \abs{f} = { \abs{e^{iz} } \over \abs{z^2 + b^2} } = {e^{-\Re z} \over \abs{z^2 + b^2} } \leq {1\over \abs{z^2 + b^2}} \converges{R\to\infty}\too 0
  .\]

- Compute $\int_\Gamma f$ by residues: factor $z^2 + b^2 = (z+ib)(z-ib)$, so the contour only contains the order 1 pole $z_0 = ib$.

- Compute the residue:
\[
\Res_{z=ib}f = \lim_{z\to ib} (z-ib) {e^{iz} \over (z+ib)(z-ib) } = { e^{iz} \over z+ib} \evalfrom_{z=ib} = {e^{i(ib)} \over 2ib} = {e^{-b} \over 2ib}
.\]
- So the intermediate integral is $I$ is $2\pi i$ times this, i.e. $I = \pi e^{-b} / b$.
- And the original integral is ${1\over 2}I = \pi e^{-b} \over 2b$.

:::

### Tie's Extra Questions: Fall 2009
