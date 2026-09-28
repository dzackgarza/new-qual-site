---
schema: qual/card@1
id: P-GW4KD
kind: problem
title: $\operatorname{Aut}(C_n)\cong(\mathbb{Z}/n\mathbb{Z})^\times$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $n>1$ be an integer.
Show that the automorphism group of the cyclic group of order $n$ is isomorphic to the multiplicative group of units mod $n$.
:::

::: {.solution}
Let $C_n=\langle g\rangle$ be cyclic of order $n$ with generator $g$.

<1>1. For each $k\in\ZZ$, the map $\phi_k\colon C_n\to C_n$, $\phi_k(g^a)=g^{ka}$, is a well-defined endomorphism, and every endomorphism of $C_n$ equals $\phi_k$ for some $k$. Moreover $\phi_k$ depends only on $k \bmod n$.

::: {.proof}
If $g^a=g^b$, then $n\mid a-b$, so $n\mid ka-kb$ and $g^{ka}=g^{kb}$; thus $\phi_k$ is well defined, and $\phi_k(g^ag^b)=g^{k(a+b)}=\phi_k(g^a)\phi_k(g^b)$.
An endomorphism $\phi$ is determined by $\phi(g)$, which equals $g^k$ for some $k$; then $\phi=\phi_k$.
Since $\phi_k(g)=g^k$, the map $\phi_k$ depends only on $k\bmod n$.
:::

<1>2. The endomorphism $\phi_k$ is an automorphism if and only if $\gcd(k,n)=1$.

::: {.proof}
Since $C_n$ is finite, $\phi_k$ is bijective if and only if it is surjective, that is, if and only if $g^k$ generates $C_n$.
The order of $g^k$ is $n/\gcd(n,k)$, which equals $n$ exactly when $\gcd(n,k)=1$.
:::

<1>3. The map $\Psi\colon(\ZZ/n\ZZ)^\times\to\Aut(C_n)$, $\Psi(k\bmod n)=\phi_k$, is a group isomorphism.

::: {.proof}
By steps <1>1 and <1>2, $\Psi$ is well defined.
For units $k,\ell$, $(\phi_k\circ\phi_\ell)(g)=\phi_k(g^\ell)=g^{k\ell}=\phi_{k\ell}(g)$, so $\phi_k\circ\phi_\ell=\phi_{k\ell}$ and $\Psi$ is a homomorphism.
If $\phi_k=\operatorname{id}$, then $g^{k-1}=e$ and $k\equiv1\pmod n$, so $\Psi$ is injective.
By steps <1>1 and <1>2, every automorphism equals $\phi_k$ with $\gcd(k,n)=1$, so $\Psi$ is surjective.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives $\Aut(C_n)\cong(\ZZ/n\ZZ)^\times$.
:::
:::
