---
schema: qual/card@1
id: E-WLFTP
kind: exercise
title: "Show that if $\\abs{f(z)/z^n}$ is bounded for $\\abs{z}\\geq R$, then $f$\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show that if $\abs{f(z)/z^n}$ is bounded for $\abs{z}\geq R$, then $f$ is a polynomial of degree at most $n$.
What happens if this bound holds on all of $\CC$?

#complex/exercise/completed

:::

:::{.solution}
Use that $f$ is entire to Laurent expand at $z=0$ to get $f(z) = \sum_{k\geq 0}c_k z^k$ everywhere.
Claim: $c_{n+k} = 0$ for all $k\geq n+1$
By the formula for Taylor coefficients, it suffices to show $f^{(n+k)}(0) = 0$ for all $k\geq n+1$.
Apply the Cauchy estimate on a curve of radius $R\gg 1$:
\[
\abs{ f^{n+k} (0)} 
&\leq {(n+k)! \over 2\pi} \int_{\abs{z} = R} \abs{f(\xi) \over \xi^{n+k+1}}\dxi\\
&\leq {(n+k)! \over 2\pi} \int_{\abs{z} = R} \abs{M \over \xi^n \xi^{k+1}}\dxi\\
&= {(n+k)! \over 2\pi} \int_{\abs{z} = R} \abs{M \over R ^{k+1}}\dxi\\
&= {(n+k)! \over 2\pi} {M\over R^{k+1}} \cdot 2\pi R \\
&= \bigo(1/R) \to 0
.\]

If this holds on all of $\CC$, then $h(z) \da f(z)/z^n$ is constant and thus $f(z) = cz^n$.
:::

