---
title: The sheaf condition
order: 1
topics:
- Sheaves
- Presheaves
- Sheafification
---

# The sheaf condition

[[D-RCCFY]]

[[FE-AM5Z8]]

The presheaf of bounded real functions on $\RR$ satisfies the identity axiom and fails gluing: the restrictions of $x$ to the intervals $(-n,n)$ are bounded and compatible, and they glue only to the unbounded function $x$.
The presheaf quotient of all real functions by the bounded ones fails the identity axiom: the class of $x$ is nonzero on $\RR$ and zero on each $(-n,n)$.

[[D-0QSI0]]

[[D-COMMACAT]]

[[T-3VX80]]

[[D-A7LCT]]

The map $\mcf\to\mcf^+$ induces an isomorphism on every stalk.
For a morphism $\varphi\colon\mcf\to\mcg$ of sheaves, the presheaf kernel $U\mapsto\ker\varphi_U$ is a sheaf; the presheaf cokernel $U\mapsto\mcg(U)/\varphi(\mcf(U))$ need not be, and the sheaf cokernel is its sheafification.

## Sheafification as a space over $X$

The espace étalé of $\mcf$ is $\coprod_{x\in X}\mcf_x$ with the topology for which the projection to $X$ is a local homeomorphism and each $s\in\mcf(U)$ gives an open section $x\mapsto s_x$; $\mcf^+(U)$ is the set of its continuous sections over $U$.

[[D-VJFAP]]

From this construction, $\mcf$ and $\mcf^+$ have the same stalks, and $\mcf\to\mcf^+$ is an isomorphism exactly when $\mcf$ is a sheaf.

[[PR-IP6ZG]]

The noetherian hypothesis is needed.
On the discrete space $X=\NN$, let $\mcf_i$ be the sheaf with stalk $\ZZ$ at the points $n\le i$ and $0$ elsewhere.
Then $\colim_i\mcf_i$ is the constant sheaf $\ZZ$, with $\Gamma(X,\ZZ)=\prod_n\ZZ$, while $\colim_i\Gamma(X,\mcf_i)=\bigoplus_n\ZZ$.
