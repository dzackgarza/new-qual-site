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

::: {.proposition}
Let $p$ and $q$ be primes with $q<p$, and let $G$ be a group of order $pq$.

(a) If $q\notdivides p-1$, then $G\cong C_{pq}$.

(b) If $q\divides p-1$, then either $G\cong C_{pq}$, or $G$ is nonabelian and
$$
G\cong C_p\semidirect_\psi C_q \cong \gens{a, b \suchthat a^p=b^q=1,\ bab^{-1} = a^\ell},
$$
where $\psi\colon C_q\to\Aut(C_p)$ is nontrivial and $\ell$ is any integer with $\ell \not\equiv 1 \pmod p$ and $\ell^q \equiv 1 \pmod p$.
Up to isomorphism, the nonabelian group does not depend on the choice of $\psi$ or $\ell$.
:::

::: {.proof}
Let $P$ and $Q$ be [[D-7TQ2M|Sylow $p$- and $q$-subgroups]] of $G$, so $P\cong C_p$ and $Q\cong C_q$.
By the Sylow theorems $n_p \equiv 1 \pmod p$ and $n_p \divides q$; since $q < p$, $n_p = 1$ and $P\normal G$.
As $P\cap Q=1$, $\abs{PQ}=pq$, so $G=PQ\cong P\semidirect_\psi Q$ for the conjugation action $\psi\colon Q\to\Aut(P)\cong(\ZZ/p\ZZ)^\times\cong C_{p-1}$.

If $q\notdivides p-1$, then $\psi$ is trivial, so $G\cong C_p\times C_q\cong C_{pq}$.

If $q\divides p-1$ and $\psi$ is trivial, again $G\cong C_{pq}$.
If $\psi$ is nontrivial, it is injective because $\abs{Q}=q$ is prime, and its image is the unique subgroup of order $q$ of the cyclic group $\Aut(P)$.
Let $a$ generate $P$.
Two nontrivial homomorphisms $Q\to\Aut(P)$ with the same image differ by precomposition with an automorphism of $Q$, which gives isomorphic semidirect products.
Choosing a generator $b$ of $Q$ with $\psi(b)(a)=a^\ell$ gives the presentation, and the conditions on $\ell$ say exactly that $a\mapsto a^\ell$ has order $q$ in $\Aut(P)$.
This group is nonabelian because $bab^{-1}=a^\ell\neq a$.
:::
