---
schema: qual/card@1
id: E-UPKG7
kind: exercise
title: "Finding complex roots"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Finding complex roots"}
Solve $z^4=i$.

#complex/exercise/completed

:::

:::{.solution}
First find a principal root: $z^4=i = e^{i\pi\over 2} \implies z_0 = e^{i\pi \over 8}$.
Now all of the roots are $\ts{z_k = z_0 \zeta_4^k \st k=0,1,2,3}$ where $\zeta_4=e^{2\pi i \over 4} = e^{i\pi \over 2}$, so

- $z_0 = e^{i\pi \over 8} e^{0i\pi \over 4} = e^{i\pi \over 8}$ corresponding to ${1\over 8} + {0\over 4}$,
- $z_1 = e^{i\pi \over 8} e^{1i\pi \over 4} = e^{3i\pi \over 8}$ corresponding to ${1\over 8} + {1\over 4} = {3\over 8}$,
- $z_2 = e^{i\pi \over 8} e^{2i\pi \over 4} = e^{5i\pi \over 8}$ corresponding to ${1\over 8} + {2\over 4} = {5\over 8}$,
- $z_3 = e^{i\pi \over 8} e^{3i\pi \over 4} = e^{7i\pi \over 8}$ corresponding to ${1\over 8} + {3\over 4} = {7\over 8}$.

:::
