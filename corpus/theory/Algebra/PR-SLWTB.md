---
schema: qual/card@1
id: PR-SLWTB
kind: proposition
title: Classification of groups of order $pq$
slogan: 'Groups of order $pq$ are cyclic unless the smaller prime divides the larger minus one, when one nonabelian semidirect product also appears.'
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
Let $p$ and $q$ be primes with $p<q$, and let $G$ be a group of order $pq$.

(a) If $p\notdivides q-1$, then $G\cong C_{pq}$.

(b) If $p\divides q-1$, then either $G\cong C_{pq}$, or $G$ is nonabelian and
$$
G\cong C_q\semidirect_\psi C_p \cong \generators{a, b \suchthat a^q=b^p=1,\ bab^{-1} = a^\ell},
$$
where $\psi\colon C_p\to\Aut(C_q)$ is nontrivial and $\ell$ is any integer with $\ell \not\equiv 1 \pmod q$ and $\ell^p \equiv 1 \pmod q$.
Up to isomorphism, the nonabelian group does not depend on the choice of $\psi$ or $\ell$.
:::

::: {.proof}
Let $P$ and $Q$ be [[D-7TQ2M|Sylow $p$- and $q$-subgroups]] of $G$, so $P\cong C_p$ and $Q\cong C_q$.
By the Sylow theorems $n_q \equiv 1 \pmod q$ and $n_q \divides p$; since $p < q$, $n_q = 1$ and $Q\normal G$.
As $P\cap Q=1$, $\abs{QP}=pq$, so $G=QP\cong Q\semidirect_\psi P$ for the conjugation action $\psi\colon P\to\Aut(Q)\cong(\ZZ/q\ZZ)^\times\cong C_{q-1}$.

If $p\notdivides q-1$, then $\psi$ is trivial, so $G\cong C_q\times C_p\cong C_{pq}$.

If $p\divides q-1$ and $\psi$ is trivial, again $G\cong C_{pq}$.
If $\psi$ is nontrivial, it is injective because $\abs{P}=p$ is prime, and its image is the unique subgroup of order $p$ of the cyclic group $\Aut(Q)$.
Let $a$ generate $Q$.
Two nontrivial homomorphisms $P\to\Aut(Q)$ with the same image differ by precomposition with an automorphism of $P$, which gives isomorphic semidirect products.
Choosing a generator $b$ of $P$ with $\psi(b)(a)=a^\ell$ gives the presentation, and the conditions on $\ell$ say exactly that $a\mapsto a^\ell$ has order $p$ in $\Aut(Q)$.
This group is nonabelian because $bab^{-1}=a^\ell\neq a$.
:::
