---
schema: qual/card@1
id: P-CCX6E
kind: problem
title: "Nilradical is intersection of primes"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.problem title="Nilradical is intersection of primes"}
The nilradical is the intersection of all prime ideals, i.e.
\[
\nilrad{R} = \Intersect_{\mathfrak{p} \in \spec(R)} \mathfrak{p}
\]
:::

:::{.solution}
\envlist

- $\nilrad{R} \subseteq \intersect \mathfrak{p}$:

- $x \in \nilrad{R} \implies x^n = 0 \in \mathfrak p \implies x\in \mathfrak{p} \text{ or } x^{n-1}\in\mathfrak p$.

- $R\sm \nilrad{R} \subseteq \union_{\mfp} (R\sm \mathfrak{p})$:

- Define $S = \theset{I\normal R \suchthat a^n\not\in I \text{ for any } n}$.

- Then apply Zorn's lemma to get a maximal ideal $\mm$, and maximal $\implies$ prime.
:::

