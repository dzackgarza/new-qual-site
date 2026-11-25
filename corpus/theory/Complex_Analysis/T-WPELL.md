---
schema: qual/card@1
id: T-WPELL
kind: theorem
title: The Weierstrass $\wp$ function is elliptic
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Special Functions
relations: []
review: draft
---

::: {.theorem}
Let $\Lambda=\omega_1\ZZ+\omega_2\ZZ$ with $\omega_1/\omega_2\notin\RR$, and let
$$
\wp(z)=\frac{1}{z^2}+\sum_{\omega\in\Lambda\smz}\left(\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}\right).
$$
Then $\wp$ is [[D-7DFVJ|meromorphic]] on $\CC$, with a double pole at each point of $\Lambda$ and no other poles; it is even; and it is [[D-CRVWEIER|doubly periodic]]: $\wp(z+\omega)=\wp(z)$ for every $\omega\in\Lambda$.

This is [@Ahl73, ch. 7, §3.1, The Weierstrass $\wp$-function], where the series is shown to converge, to have the periods $\omega_1$ and $\omega_2$, and to be characterised by its expansion at the origin.
:::
