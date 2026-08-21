---
schema: qual/card@1
id: E-3B2YA
kind: exercise
title: Evaluating integrals
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Residues
  - Contour Integration
relations: []
review: draft
solved: true
---

:::{.exercise title="Evaluating integrals"}
Evaluate the following integrals using Cauchy's integral formula:

\[
\int_{S^1} {\cos(z) \over z} \dz&\\
\int_{S^1} {\sin(z) \over z}\dz&\\
\int_{\abs z = 2} {z^2\over z-1} \dz &\\
\int_{S^1} {e^z \over z^2} \dz &\\
\int_{\abs z = 2} {z^2 - 1 \over z^2 + 1}\dz &\\
\int_{\abs z = 2} {1\over z^2 + z + 1}\dz &
.\]

:::

:::{.solution}
\[
\int_{S^1} {\cos(z) \over z} \dz
&= 2\pi i \cos(0) \\
&= 2\pi i \\ \\
\int_{S^1} {\sin(z) \over z}\dz
&= 2\pi i \sin(0) \\
&= 0 \\ \\
\int_{\abs z = 2} {z^2\over z-1} \dz 
&= 2\pi i z^2\evalfrom_{z=1} \\
&= 2\pi i \\ \\
\int_{S^1} {e^z \over z^2} \dz 
&= 2\pi i \dd{}{z} e^z\evalfrom_{z=0} \\
&= 2\pi i \\ \\
\int_{\abs z = 2} {z^2 - 1 \over z^2 + 1}\dz 
&= \int_{\DD + i} {(z^2 -1)/(z+i) \over z-i}\dz + \int_{\DD - i} {(z^2-1)/(z-i) \over z+i} \dz \\
&= 2\pi i \qty{z^2-1\over z+i}\evalfrom_{z=i} + 2\pi i \qty{z^2-1 \over z-i}\evalfrom_{z=-i} \\
&= 2\pi i \qty{-2\over 2i} + 2\pi i \qty{-2\over -2i} \\
&= 0 \\ \\
\int_{\abs z = 2} {1\over z^2 + z + 1}\dz 
&= \int {1\over (z-\zeta_3) (z- \bar{\zeta_3} )} \dz \\
&= \int_{\DD + \bar{ \zeta_3} } {1/(z-\zeta_3) \over (z- \bar{\zeta_3} )} \dz + \int_{\DD + {\zeta_3} } {1/(z- \bar{ \zeta_3} ) \over (z- {\zeta_3} )} \dz \\
&= 2\pi i \qty{1\over z-\zeta_3}\evalfrom_{z=\bar{\zeta_3}} + 2\pi i \qty{1\over z-\bar{\zeta_3}}\evalfrom_{z=\zeta_3} \\
&= 2\pi i \qty{ {1\over \bar{\zeta_3} - \zeta_3 } + {1\over \zeta_3 - \bar{\zeta_3}} }\\
&= 2\pi i \qty{ {1\over \bar{\zeta_3} - \zeta_3 } - {1\over \bar{\zeta_3} - {\zeta_3}} } \\
&= 0
,\]
where for the last we note that $\zeta_3 = e^{2\pi i \over 3} = -1 + i\sqrt 3$ and $\zeta_3 \bar{\zeta_3} = 2\Re(\zeta_3) = 2\cdot {1\over 2} = 1$, yielding the factorization of the denominator.

:::

