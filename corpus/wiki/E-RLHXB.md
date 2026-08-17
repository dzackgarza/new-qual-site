---
schema: qual/card@1
id: E-RLHXB
kind: exercise
title: "Integral computation"
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
solved: true
---
:::{.exercise title="Integral computation"}
Without using the residue formula, compute
\[
\int_\RR f(x) \dx && f(x) \da {1\over x^4 + 16}
.\]

:::

:::{.solution}
Use a semicircular contour, noting the poles are at $\pm \sqrt 2 \pm i\sqrt 2$. 
Write

- $f_1(z) \da (\sqrt 2 + i\sqrt 2)f(z)$
- $f_2(z) \da (-\sqrt 2 + i\sqrt 2) f(z)$.

Break the curve up into two integrals $I_1, I_2$ enclosing the poles, by Cauchy one gets

- For the loop around the right pole: $I_1 = 2\pi i f_1(\sqrt 2 + i\sqrt 2) = {\pi \sqrt{2}(1-i) \over 32}$
- For the loop around the left pole: $I_2 = 2\pi i f_2(\sqrt 2 - i\sqrt 2) = {\pi \sqrt 2(1+i) \over 32}$.

Now show that $\int_{C_R}$ vanishes: parameterize as $\gamma(t) = Re^{it}$ and use the reverse triangle inequality:
\[
\abs{ \int_{C_R} f} \leq  \int_0^\pi {1\over R^4 - 16} = {\pi R \over R^4-16}\to 0
.\]

:::

