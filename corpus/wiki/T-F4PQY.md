---
schema: qual/card@1
id: T-F4PQY
kind: theorem
title: "Fundamental theorem of covering spaces, Hatcher 1.39"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.theorem title="Fundamental theorem of covering spaces, Hatcher 1.39"}
For $\tilde X \mapsvia{p} X$ a covering space with

- $\tilde X$ path-connected,
- $X$ path-connected and locally path-connected,

letting $H$ be the image of $\pi_1(\tilde X)$ in $\pi_1(X)$, we have

1. $\tilde X$ is normal if and only if $H\normal \pi_1(X)$,

2. For the normalizer $N_G(H)$ where $G\da \pi_1(X)$,
\[
G(\tilde X) \da \Aut_{\mathrm{Cov}(X) }(\tilde X) \cong {N_G(H) \over H}
.\]

In particular,
\[
\tilde X \text{ normal} &\implies G(\tilde X) \cong \pi_1(X) / H \\
\hat X \text{ universal} &\implies G(\hat X) \cong \pi_1(X)
.\]

:::
