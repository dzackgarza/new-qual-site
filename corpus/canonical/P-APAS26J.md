---
schema: qual/card@1
id: P-APAS26J
kind: problem
title: Centralizer of $\mathcal{C}(H)$ in $\mathcal{C}(G)$ via branching multiplicities
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
solved: false
---

::: problem
Let $G$ be a finite group and let $H$ be a subgroup of $G$.
Let $\Lambda(G)$ be a set parameterizing irreducible unitary representations $V^\lambda$ of $G$, and let $\Lambda(H)$ be a set parameterizing irreducible unitary representations $W^\mu$ of $H$.
For $\lambda \in \Lambda(G)$ and $\mu \in \Lambda(H)$, let $m_{\lambda\mu}$ be the multiplicity of $W^\mu$ in the restriction of $V^\lambda$ to $H$.
Omitting terms with $m_{\lambda\mu} = 0$, show that the centralizer of $\mathcal{C}(H)$ in $\mathcal{C}(G)$ is isomorphic to
\[
\bigoplus_{\lambda \in \Lambda(G)} \bigoplus_{\mu \in \Lambda(H)} \operatorname{End}\bigl(\mathbb{C}^{m_{\lambda\mu}}\bigr).
\]
:::
