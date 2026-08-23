---
schema: qual/card@1
id: P-CASP06A
kind: problem
title: "Analytic hull properties: distance to boundary and containment in convex hull"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $\Omega$ be an open subset of $\mathbb{C}$.
For a compact subset $K$ of $\Omega$, define the hull $$\hat{K} = \{z \in \Omega : |f(z)| \leq \sup_{w \in K} |f(w)|, \text{ for every } f \in \mathcal{O}(\Omega)\}.$$ Let $\hat{K}_c$ be the convex hull of $K$, namely the smallest convex subset of $\mathbb{C}$ containing $K$.
Show that

(a) $d(K, \mathbb{C} \setminus \Omega) = d(\hat{K}, \mathbb{C} \setminus \Omega)$;

(b) $\hat{K} \subset \hat{K}_c$.
:::
