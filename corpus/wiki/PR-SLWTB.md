---
schema: qual/card@1
id: PR-SLWTB
kind: proposition
title: Classification of groups of order $pq$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Semidirect Products
  - Groups
relations: []
review: draft
---

:::{.proposition}
If $G$ is a group of order $pq$ for primes $q<p$, write $P$ and $Q$ for its Sylow $p\dash$ and $q\dash$subgroups, so $P\cong C_p$ and $Q \cong C_q$.
Note that $P\normal G$ in both cases, since $n_p \equiv 1 \mod p$ and $n_p \divides q < p$ force $n_p = 1$.

1. If $q\notdivides p-1$ then $G$ is cyclic and $G\cong P \cross Q \cong C_{pq}$.
2. If $q\divides p-1$ then $G\cong P \semidirect_\psi Q$, the normal factor $P$ on the left, with $\psi: Q \to \Aut(P)$ nontrivial, and $G$ has a presentation 
\[
G\cong \gens{a, b \st a^p, b^q, bab\inv = a^\ell} \\ \\ 
\ell \not\equiv 1 \mod p && \ell^q \equiv 1 \mod p
.\]
:::
