---
schema: qual/card@1
id: E-HAT-2.2-40
kind: problem
title: Universal coefficient short exact sequence for homology with $\mathbb{Z}_n$ coefficients
classification:
  areas:
  - topology
  topics:
  - Homology
  - Universal Coefficients
  - Torsion
relations: []
review: draft
---

From the long exact sequence of homology groups associated to the short exact sequence of chain complexes $0 \to C_i(X) \xrightarrow{n} C_i(X) \to C_i(X; \mathbb{Z}_n) \to 0$ deduce immediately that there are short exact sequences

$$0 \to H_i(X)/nH_i(X) \to H_i(X; \mathbb{Z}_n) \to n\text{-Torsion}(H_{i-1}(X)) \to 0$$

where $n$-Torsion$(G)$ is the kernel of the map $G \xrightarrow{n} G$, $g \mapsto ng$.
Use this to show that $\tilde{H}_i(X; \mathbb{Z}_p) = 0$ for all $i$ and all primes $p$ iff $\tilde{H}_i(X)$ is a vector space over $\mathbb{Q}$ for all $i$.
