---
schema: qual/card@1
id: E-IZKCV
kind: exercise
title: "$1/x^4+1$, balancing exponentials"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
  - poles
relations: []
review: draft
---
:::{.exercise title="$1/x^4+1$, balancing exponentials"}
\[
\int_\RR {1 \over x^4 + 1} = {\pi \sqrt{2} \over 2} = {\pi \over \sqrt 2}
.\]

:::

:::{.solution}
The integrand $f\in \bigo\qty{1\over z^4} \subseteq \bigo\qty{1\over z^{1+\eps}}$, so a semicircular contour works.
Factoring the denominator: find a principal root 
\[
\omega^4 = -1 = e^{i\pi} \implies \omega = e{i\pi\over 4}
,\]
so 
\[
z^4 + 1 = (z-\omega)(z-\omega\zeta_4)(z-\omega\zeta_4^2)(z-\omega\zeta_4^3) \leadsto {\pi \over 4}, {3\pi \over 4}, {5\pi \over 4}, {7\pi \over 4}
.\]
So there are two simple poles in $\HH$:

![figures/2021-07-29_18-41-05.png](../../assets/figures/2021-07-29_18-41-05.png)

Write them as $z_1 = e^{i\pi \over 4}$ and $z_2 = e^{3 i \pi \over 4}$.
Computing the residues:
\[
\Res_{z=z_k} f(z) 
&= \lim_{z\to z_k} {z-z_k \over z^4 + 1} \\
&\eqLH \lim_{z\to z_k} {1\over 4z^3} \\
&= {4z^{-3} }\evalfrom_{z=z_k}
,\]
so
\[
2\pi i \sum \Res_{z=z_k} 
&= {2\pi i \over 4}\qty{z_1^{-3} + z_2^{-3}} \\
&= {\pi i \over 2}\qty{e^{-3 i \pi \over 4} + e^{-9 i \pi \over 4}} \\
&= {\pi i \over 2}\qty{e^{-3 i \pi \over 4} + e^{-i \pi \over 4}} \\
&= {\pi i \over 2}\cdot e^{-2i\pi \over 4}\qty{e^{- i \pi \over 4} + e^{i \pi \over 4}} \\
&= \pi i\, {1\over i} \cos\qty{\pi \over 4} \\
&= {\pi \sqrt 2 \over 2}
.\]

:::

