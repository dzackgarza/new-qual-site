---
schema: qual/card@1
id: E-I26BF
kind: exercise
title: "Injective implies nonvanishing derivative"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Injective implies nonvanishing derivative"}
Show that if $f$ is holomorphic on $\Omega$ and injective, then $f'(z)$ is nonvanishing on $\Omega$.
:::

:::{.solution}
By contradiction: without loss of generality suppose $f(0) = 0$ and $f'$ vanishes at zero.
Then $f(z) = \sum_{k\geq 0} c_k z^k = \sum_{k\geq 2}c_k z^k$ since $c_k \approx f^{(k)}(0)$, so $z=0$ is a zero of order at least 2.
But then $f(z) = c_2 z^2 + \cdots$, so $f$ is at best 2-to-1 near 0, contradicting injectivity.
:::
