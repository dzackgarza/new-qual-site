---
schema: qual/card@1
id: P-APAS06D
kind: problem
title: Simple groups and subgroups of given index
classification:
  areas:
  - applied-algebra
  topics:
  - Group Theory
  - Permutations
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $G$ be a group.
Let $r\ge 2$ be an integer.
Assume that $G$ contains a non-trivial subgroup $H$ of index $[G:H]=r$.
Prove the following.

(a) If $G$ is simple, then $G$ is finite and $|G|$ divides $r!$.

(b) If $r\in\{2,3,4\}$, then $G$ cannot be simple.

(c) For all integers $r\ge 5$, there exist simple groups $G$ which contain non-trivial subgroups $H$ of index $[G:H]=r$.
:::

::: solution
For the action of $G$ on the left cosets $G/H$, let
\[
\rho:G\longrightarrow S_r
\]
be the associated permutation representation. Its kernel is the core
\[
\ker\rho=\bigcap_{g\in G}gHg^{-1}.
\]
In particular, $\ker\rho$ is normal in $G$ and is contained in $H$.

For (a), suppose $G$ is simple. Since $[G:H]=r\ge2$, the subgroup $H$ is proper, so $\ker\rho\subseteq H$ cannot equal $G$. Simplicity therefore forces $\ker\rho=1$. Hence $\rho$ is injective and
\[
G\cong \rho(G)\le S_r.
\]
Thus $G$ is finite and, by Lagrange's theorem,
\[
|G|\mid |S_r|=r!.
\]

For (b), suppose first that $r=2$. Then (a) gives $|G|\mid2$, while $H$ is nontrivial and proper, so
\[
|G|=[G:H]|H|=2|H|\ge4,
\]
a contradiction.

If $r=3$, then $3\mid |G|$ and $|G|\mid6$. Since $H$ is nontrivial, $|G|>3$, so $|G|=6$. But every group of order $6$ has a normal Sylow $3$-subgroup: the number $n_3$ of Sylow $3$-subgroups satisfies
\[
n_3\equiv1\pmod3,
\qquad
n_3\mid2,
\]
so $n_3=1$. Hence $G$ is not simple.

If $r=4$, then $4\mid|G|$ and $|G|\mid24$, while $|H|>1$. Thus
\[
|G|\in\{8,12,24\}.
\]
A group of order $8$ is a nontrivial finite $2$-group, so its center is nontrivial; hence it is not simple. A group of order $12$ has either one or four Sylow $3$-subgroups. If there is one, it is normal. If there are four, conjugation on those four Sylow subgroups gives a homomorphism to $S_4$; were the group simple, this action would be faithful, embedding a group of order $12$ into $S_4$. Its image would then have index $2$ in $S_4$, hence would be normal, contradicting simplicity. Finally, if $|G|=24$, then the embedding $G\hookrightarrow S_4$ from (a) has equal source and target orders, hence is an isomorphism $G\cong S_4$, which is not simple because $A_4\trianglelefteq S_4$. Therefore no such $G$ is simple for $r\in\{2,3,4\}$.

For (c), let $r\ge5$ and take
\[
G=A_r,
\qquad
H=\operatorname{Stab}_{A_r}(r).
\]
The group $A_r$ is simple for $r\ge5$. The stabilizer consists of the even permutations of the first $r-1$ letters, so
\[
H\cong A_{r-1}.
\]
Since $r-1\ge4$, this subgroup is nontrivial. Moreover
\[
[G:H]
=
\frac{|A_r|}{|A_{r-1}|}
=
\frac{r!/2}{(r-1)!/2}
=r.
\]
Thus every integer $r\ge5$ occurs.
:::
