---
schema: qual/card@1
id: PR-SLWTB
kind: proposition
title: "Classification of groups of order $pq$"
classification:
  areas:
  - algebra
  topics:
  - classification
  - semidirect-products
  - groups
relations: []
review: draft
---
:::{.proposition title="Classification of groups of order $pq$"}
If $G$ is a group of order $pq$ where without loss of generality $q<p$, then

1. If $q\notdivides p-1$ then $G$ is cyclic and $G\cong S_p \cross S_q \cong C_{pq}$.
2. If $q\divides p-1$ then $G\cong S_q \semidirect_\psi S_p$ where $S_p \normal G$ and $\psi: S_q \to \Aut(S_p)$, and $G$ has a presentation 
\[
G\cong \gens{a, b \st a^p, b^q, bab\inv = a^\ell} \\ \\ 
\ell \not\equiv 1 \mod p && \ell^q \equiv 1 \mod p
.\]
:::
