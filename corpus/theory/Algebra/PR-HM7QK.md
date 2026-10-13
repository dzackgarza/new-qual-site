---
schema: qual/card@1
id: PR-HM7QK
kind: proposition
title: Homomorphisms between finite cyclic groups
slogan: 'There are $\gcd(m,n)$ homomorphisms from $C_n$ to $C_m$.'
classification:
  areas:
  - algebra
  topics:
  - Cyclic Groups
  - Homomorphisms
  - Abelian Groups
relations: []
review: draft
---

::: {.proposition}
For positive integers $m,n$,
$$
\abs{\Hom(C_n,C_m)}=\gcd(n,m).
$$
:::

::: {.proof}
Write $C_n=\generators{x}$ and identify $C_m$ additively with $\ZZ/m\ZZ$.
A homomorphism $\phi\colon C_n\to C_m$ is determined by the image $a=\phi(x)$, and the relation $x^n=1$ is respected exactly when
$$
na=0\qquad\text{in }\ZZ/m\ZZ.
$$
Thus the possible images are the kernel of multiplication by $n$ on $\ZZ/m\ZZ$.
If $d=\gcd(n,m)$, write $n=dn'$ and $m=dm'$ with $\gcd(n',m')=1$.
The congruence
$$
na\equiv0\pmod m
$$
is equivalent to $m'\mid a$, so its solutions modulo $m$ are
$$
0,m',2m',\ldots,(d-1)m'.
$$
There are exactly $d$ of them.
:::
