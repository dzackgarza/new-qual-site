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

Sheafification changes no stalk.
Consequently a sequence of sheaves is exact exactly when the corresponding sequence of stalks is exact.
Kernels are computed sectionwise, while the sectionwise presheaf image and cokernel need not be sheaves and are sheafified to obtain the image and cokernel in the sheaf category; their stalks are still the image and cokernel of the stalk maps.

## Sheafification as a space over $X$

The compatible-families formula gives the sheafification explicitly.
The espace étalé gives a geometric realization: a sheaf is a space over $X$ whose projection is a local homeomorphism, and the sections of $\mcf^+$ are its continuous sections.

[[D-VJFAP]]

From this construction, $\mcf$ and $\mcf^+$ have the same stalks, and $\mcf\to\mcf^+$ is an isomorphism exactly when $\mcf$ is a sheaf.

[[PR-IP6ZG]]

The noetherian hypothesis is needed.
On the discrete space $X=\NN$, let $\mcf_i$ be the sheaf with stalk $\ZZ$ at the points $n\le i$ and $0$ elsewhere.
Then $\colim_i\mcf_i$ is the constant sheaf $\ZZ$, with $\Gamma(X,\ZZ)=\prod_n\ZZ$, while $\colim_i\Gamma(X,\mcf_i)=\bigoplus_n\ZZ$.
