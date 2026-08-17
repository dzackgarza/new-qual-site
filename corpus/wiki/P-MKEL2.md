---
schema: qual/card@1
id: P-MKEL2
kind: problem
title: Evaluate $\int\frac{1}{e^x+e^{-x}}\,dx$
classification:
  areas:
  - prelim
  topics:
  - integrals
  - u-substitution
relations: []
review: draft
solved: false
---

::: problem
1. $\displaystyle \int \frac {1}{e^x + e^{-x}} ~dx = \color{blue} {\tan ^{-1} e^x}​$

- **Solution:** $u = e^x$, $du = e^x ~dx$

- **Solution:** $\frac {1}{e^x + e^{-x}} ~dx = \frac {e^x}{e^{2x} + 1} ~dx = \frac {1}{u^2 + 1} ~du​$

  1. $\displaystyle \int \frac {e^x}{1+e^{2x}} ~dx = \color{blue} {\tan ^{-1} (e^x)}​$

  - **Solution:** $\frac {1}{e^x + e^{-x}} =  \frac {e^x}{1+e^{2x}}$

2. $\displaystyle \int \frac {1}{\sqrt {e^{2x}-1}} ~dx = \color{blue} {\sin ^{-1} (e^{-x})} = \color{blue} {\tan ^{-1} (\sqrt {e^{2x} - 1})}$

- **Solution:** $u = e^{-x}$, $du = - e^{-x} ~dx$

- **Solution:** $\frac {1}{\sqrt {e^{2x}-1}} ~dx = \frac {e^{-x} ~dx}{\sqrt {1- e^{-2x}}} = \frac {du}{\sqrt {1 - u^2}}$

- **Another Solution:** $u = \sqrt {e^{2x} - 1}$, $x = \frac {1}{2} \ln (u^2 + 1)$, $dx = \frac {u}{u^2 + 1} ~du$

- **Another Solution:** $\frac {1}{\sqrt {e^{2x}-1}} ~dx = \frac {1}{u} \cdot \frac {u ~du}{u^2 + 1} = \frac {1}{u^2 + 1} ~du$
:::
