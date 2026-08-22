---
schema: qual/card@1
id: P-ALGS15H
kind: problem
title: Minimal polynomial via Galois orbit; Artin–Schreier normality and separability
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
solved: false
---

::: problem
Let $K$ be a field with $G \subseteq \mathrm{Aut}(K)$ a finite group of automorphisms of $K$. Let $F = \mathrm{Fix}(G)$. Let $\alpha \in K$ and let $f = \mathrm{minpoly}_F(\alpha)$. Let $H = \{g \in G \mid g(\alpha) = \alpha\}$ and fix $g_1, g_2, \ldots, g_m \in G$ such that $g_1 H, \ldots, g_m H$ are the distinct left cosets of $H$ in $G$.

(a) Show that $f(x) = (x - g_1(\alpha)) \cdots (x - g_m(\alpha))$. (Hint: show the polynomial on the right has coefficients in $F$.)

(b) Use part (a) to conclude that the field extension $K/F$ is separable and normal.
:::
