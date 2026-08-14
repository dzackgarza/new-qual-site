---
schema: qual/card@1
id: E-AMD-UEHZOJ3K
kind: solution
title: "$\\nilrad{R} \\subseteq \\intersect \\mathfrak{p}$: $x \\in \\nilrad{R} \\implies x^n = 0 \\in \\mathfrak p \\implies x\\in \\mathfrak{p} \\text{ or } x^{n-1}\\in\\mathfrak p$. $R\\sm \\nilrad{R} \\subseteq \\union_{\\mfp} (R\\sm \\mathfrak{p})$\u2026"
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - prime-ideals
  - ideals
relations: []
review: draft
---

::: {.solution}
\envlist

- $\nilrad{R} \subseteq \intersect \mathfrak{p}$:

- $x \in \nilrad{R} \implies x^n = 0 \in \mathfrak p \implies x\in \mathfrak{p} \text{ or } x^{n-1}\in\mathfrak p$.

- $R\sm \nilrad{R} \subseteq \union_{\mfp} (R\sm \mathfrak{p})$:

- Define $S = \theset{I\normal R \suchthat a^n\not\in I \text{ for any } n}$.

- Then apply Zorn's lemma to get a maximal ideal $\mm$, and maximal $\implies$ prime.
:::
