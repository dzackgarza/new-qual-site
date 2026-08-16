---
schema: qual/card@1
id: P-OLLG3
kind: problem
title: "Noting that applying a row operation to $A$ is the same as taking the\u2026"
classification:
  areas:
  - algebra
  topics:
  - linear-algebra
  - matrices
relations: []
review: draft
---

::: problem
Noting that applying a row operation to $A$ is the same as taking the product $E A$ for some elementary matrix $E$, we can write $A_1 = \left( \prod_{i=1}^\ell E_i \right) A$ and $B_1 = \left( \prod_{i=1}^\ell E_i \right) B$,

thus

\begin{align*}
A \vector x &= \vector b \\
\implies E_\ell A \vector x &= E_\ell \vector b \\
\implies E_{\ell-1} E_\ell A \vector x &= E_{\ell-1} E_\ell \vector b \\
&\vdots \\
\implies E_1 E_2 \cdots E_\ell A \vector x &= E_1 E_2 \cdots E_\ell A \vector b \\
\implies A_1 \vector x &= B_1
\end{align*}
:::
