---
schema: qual/card@1
id: P-5WZBI
kind: problem
title: Classification of groups of order $2p$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
a. Using Sylow theory, show that every group of order $2p$ where $p$ is prime is not simple.

b. Classify all groups of order $2p$ and justify your answer.
For the nonabelian group(s), give a presentation by generators and relations.
:::


::: solution
Let $|G|=2p$.

First suppose $p$ is odd. If $n_p$ denotes the number of Sylow $p$-subgroups, then
\[
n_p\equiv1\pmod p,
\qquad
n_p\mid2.
\]
Because $p>2$, the only possibility is $n_p=1$. Thus the unique subgroup $P$ of order $p$ is normal and proper, so $G$ is not simple.

If $p=2$, then $|G|=4$. By Cauchy's theorem, $G$ contains an element of order $2$; the subgroup it generates has index $2$, hence is normal. Thus $G$ is again not simple.

Now classify the possibilities. For $p=2$, every group of order $4$ is abelian: if some element has order $4$, then $G\cong C_4$; otherwise every nonidentity element has order $2$, and $G\cong C_2\times C_2$.

Assume henceforth that $p$ is odd, and let $P=\langle y\rangle\cong C_p$ be the unique Sylow $p$-subgroup. Since $G/P$ has order $2$, conjugation by any $x\notin P$ induces on $P$ an automorphism whose square is the identity.

If this action is trivial, then $x$ centralizes $P$. Because $xP$ has order $2$ in $G/P$, $x^2\in P$. Since $p$ is odd, replacing $x$ by $xy^m$ for a suitable $m$ makes its square equal to $1$: indeed, if $x^2=y^k$, choose $m$ with $2m\equiv-k\pmod p$, so
\[
(xy^m)^2=x^2y^{2m}=1.
\]
Thus $G\cong C_2\times C_p\cong C_{2p}$.

If the action is nontrivial, then it is the unique automorphism of order $2$ of $C_p$, namely inversion:
\[
xyx^{-1}=y^{-1}.
\]
Also $x^2\in P$. Conjugation by $x$ fixes $x^2$, while inversion sends every element of $P$ to its inverse; hence
\[
x^2=(x^2)^{-1}.
\]
Since $P$ has odd order, this forces $x^2=1$. Therefore
\[
G\cong\langle x,y\mid x^2=1,\ y^p=1,\ xyx^{-1}=y^{-1}\rangle,
\]
the dihedral group of order $2p$.

Hence, for $p=2$, the groups are $C_4$ and $C_2\times C_2$; for odd $p$, the groups are $C_{2p}$ and the dihedral group of order $2p$.
:::
