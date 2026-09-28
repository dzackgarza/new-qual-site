---
schema: qual/card@1
id: P-UTCT-4-53
kind: problem
title: Positive and negative Hopf band open books of $S^3$ and their contact structures
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Exercise 4.53 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the definitions of open books, H_+ and H_-, support, and T(M) from pp. 37-41 of Gompf Contact Topology.pdf.
---

::: {.problem}
An open book decomposition of a $3$-manifold $M$ is a link $L \subset M$ (the binding) and a bundle structure $\pi : M \setminus L \to S^1$ by Seifert surfaces.
The Hopf decomposition $H_+$ of $S^3$ is the open book along positive Hopf links; the negative Hopf decomposition $H_-$ is the same but along negative Hopf links.
An open book decomposition $B$ supports a contact structure $\xi$ if there exists a one-parameter family of plane fields $\xi_t$, $0 \leq t \leq 1$, such that $\xi_0 = \xi$, for all $t < 1$, $\xi_t$ is a contact structure transverse to the binding, and $\xi_1$ defines the foliation away from the link of $B$.
Let $\mathcal{T}(M)$ denote the set of tight, positive, oriented contact structures on $M$ modulo isotopy.

Show that $H_+$ supports the standard contact structure $\xi$ on $S^3$ using the Hopf fibration.
Show also that $H_-$ supports a different homotopy class of contact structure, which must therefore be overtwisted because $\#\mathcal{T}(S^3) = 1$.
:::
