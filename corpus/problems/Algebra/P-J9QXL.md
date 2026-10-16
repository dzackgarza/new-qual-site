---
schema: qual/card@1
id: P-J9QXL
kind: problem
title: The extension $\QQ(2^{1/3})/\QQ$ is not normal
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Is $\QQ(2^{1/3})/\QQ$ normal?
:::

::: {.solution}
The minimal polynomial of $2^{1/3}$ is $x^3-2$, whose other roots are
\[
\zeta_3 2^{1/3},\qquad \zeta_3^2 2^{1/3}.
\]
They are nonreal, while $\QQ(2^{1/3})\subset\RR$. Thus the polynomial does not split there, so the extension is not normal.
:::