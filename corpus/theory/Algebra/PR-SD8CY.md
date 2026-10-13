---
schema: qual/card@1
id: PR-SD8CY
kind: proposition
title: Changing semidirect-product actions by automorphisms
slogan: 'Precompose the action on the quotient and conjugate it on the normal factor without changing the semidirect product.'
classification:
  areas:
  - algebra
  topics:
  - Semidirect Products
  - Automorphisms
relations: []
review: draft
---

::: {.proposition}
Let $N,H$ be groups, let $\psi\colon H\to\Aut(N)$ be a homomorphism, let $\sigma\in\Aut(H)$ and $\tau\in\Aut(N)$, and define
$$
\psi'\coloneqq c_\tau\circ\psi\circ\sigma,
\qquad
c_\tau(\alpha)=\tau\alpha\tau^{-1}.
$$
Then
$$
N\semidirect_{\psi'}H\cong N\semidirect_\psi H.
$$
:::

::: {.proof}
Define
$$
F\colon N\semidirect_{\psi'}H\longrightarrow N\semidirect_\psi H,
\qquad
F(n,h)=\bigl(\tau^{-1}(n),\sigma(h)\bigr).
$$
For $(n,h),(n',h')$ in the source,
$$
\begin{aligned}
F\bigl((n,h)(n',h')\bigr)
&=F\bigl(n\psi'(h)(n'),hh'\bigr)\\
&=\bigl(\tau^{-1}(n)\,\psi(\sigma(h))(\tau^{-1}(n')),\sigma(h)\sigma(h')\bigr)\\
&=F(n,h)F(n',h').
\end{aligned}
$$
Thus $F$ is a homomorphism.
It is bijective, with inverse
$$
F^{-1}(m,k)=\bigl(\tau(m),\sigma^{-1}(k)\bigr).
$$
:::

::: {.remark}
If $N=C_p^n$ and $H=C_k=\generators{h}$, an action $\psi\colon C_k\to\GL_n(\FF_p)$ is determined by $A=\psi(h)$.
Replacing $A$ by a similar matrix $PAP^{-1}$ gives an isomorphic semidirect product, so the action matrix may be put in a canonical form such as rational canonical form.
:::
