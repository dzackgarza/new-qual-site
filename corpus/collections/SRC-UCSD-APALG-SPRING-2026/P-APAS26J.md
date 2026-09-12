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

::: solution
By Wedderburn decomposition,
\[
\mathcal C(G)\cong\bigoplus_{\lambda\in\Lambda(G)}\operatorname{End}(V^\lambda).
\]
Hence the centralizer of $\mathcal C(H)$ in $\mathcal C(G)$ is the direct sum, over $\lambda$, of the commutants of the $H$-action inside $\operatorname{End}(V^\lambda)$.

Fix $\lambda$. As an $H$-module,
\[
V^\lambda\!\downarrow_H
\cong
\bigoplus_{\mu\in\Lambda(H)} W^\mu\otimes\mathbb C^{m_{\lambda\mu}},
\]
omitting the terms with $m_{\lambda\mu}=0$. On this decomposition, the image of $\mathcal C(H)$ acts as
\[
\bigoplus_{\mu}
\operatorname{End}(W^\mu)\otimes I_{m_{\lambda\mu}}.
\]
Indeed, the group algebra of $H$ acts on each irreducible $W^\mu$ as the full matrix algebra $\operatorname{End}(W^\mu)$.

The commutant of this algebra is therefore
\[
\bigoplus_{\mu}
I_{W^\mu}\otimes\operatorname{End}(\mathbb C^{m_{\lambda\mu}})
\cong
\bigoplus_{\mu}\operatorname{End}(\mathbb C^{m_{\lambda\mu}}).
\]
Taking the direct sum over all $\lambda\in\Lambda(G)$ gives
\[
\boxed{
Z_{\mathcal C(G)}(\mathcal C(H))
\cong
\bigoplus_{\lambda\in\Lambda(G)}
\bigoplus_{\mu\in\Lambda(H)}
\operatorname{End}(\mathbb C^{m_{\lambda\mu}}),
}
\]
with the zero-multiplicity terms omitted, as claimed.
:::
