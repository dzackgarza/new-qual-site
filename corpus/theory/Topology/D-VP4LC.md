---
schema: qual/card@1
id: D-VP4LC
kind: definition
title: Kronecker pairing
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homology
relations:
- kind: related-to
  target: D-Y73BB
review: draft
---

::: {.definition}
Let $X$ be a topological space, $R$ a commutative ring, and $n\geq 0$.
For a singular cochain $\varphi\in C^n(X;R) = \Hom_R(C_n(X;R), R)$ and a singular chain $\alpha\in C_n(X;R)$, put $\inner{\varphi}{\alpha} \coloneqq \varphi(\alpha)$.
The \dfn{Kronecker pairing}, also called the \dfn{Kronecker product}, is the $R$-bilinear map
$$
\inner{\wait}{\wait}\colon H^n(X; R) \cross H_n(X; R) \to R, \qquad \inner{[\varphi]}{[\alpha]} \coloneqq \varphi(\alpha),
$$
for a cocycle $\varphi$ and a cycle $\alpha$.
Its adjoint is the \dfn{evaluation homomorphism}
$$
h\colon H^n(X; R) \to \Hom_R(H_n(X;R), R), \qquad h([\varphi])([\alpha]) \coloneqq \varphi(\alpha).
$$
:::

::: {.proposition}
Let $X$ be a topological space, $R$ a commutative ring, and $n\geq 0$.

(a) For $\psi\in C^{n-1}(X;R)$ and $\alpha\in C_n(X;R)$, $\inner{\delta\psi}{\alpha} = \inner{\psi}{\del\alpha}$; hence the Kronecker pairing is well defined on classes.

(b) For a continuous map $f\colon X\to Y$, $\beta\in H^n(Y;R)$, and $x \in H_n(X;R)$, $\inner{f^*\beta}{x} = \inner{\beta}{f_*x}$.

(c) If $R$ is a principal ideal domain, there is a split short exact sequence
$$
0 \to \Ext_R(H_{n-1}(X;R), R) \to H^n(X;R) \xrightarrow{h} \Hom_R(H_n(X;R), R) \to 0,
$$
so $h$ is surjective, and $h$ is an isomorphism if and only if $\Ext_R(H_{n-1}(X;R), R) = 0$.
:::

::: {.example}
The evaluation homomorphism $h$ need not be injective.
For $X = \RR P^2$, $R = \ZZ$, and $n = 2$, one has $H_1(\RR P^2;\ZZ)\cong\ZZ/2$ and $H_2(\RR P^2;\ZZ) = 0$, so $H^2(\RR P^2;\ZZ)\cong\Ext_\ZZ(\ZZ/2,\ZZ)\cong\ZZ/2$ while $\Hom_\ZZ(H_2(\RR P^2;\ZZ),\ZZ) = 0$.
:::

::: {.concept}
[@Hat02].
:::
