---
schema: qual/card@1
id: P-ALGS11A
kind: problem
title: Groups of order $117$ with an element of order $9$
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 1 of the official UCSD Spring 2011 algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Replaced the informal solution with a complete Sylow and semidirect-product classification, including the isomorphism of the two nontrivial actions.
---

::: problem
Let $G$ be a group with $|G| = 117 = 9 \cdot 13$ elements which contains an element of order exactly $9$.
Classify all such groups $G$ up to isomorphism.
:::

::: {.solution}
Let $x\in G$ have order $9$.

<1>1. The Sylow $13$-subgroup $N$ is unique and normal, and $N\cong C_{13}$.
::: {.proof}
If $n_{13}$ is the number of Sylow $13$-subgroups, then
\[
n_{13}\mid9,\qquad n_{13}\equiv1\pmod{13}.
\]
Among the divisors $1,3,9$ of $9$, only $1$ is congruent to $1$ modulo $13$.
Hence $n_{13}=1$.
A group of prime order $13$ is cyclic.
:::

<1>2. The subgroup $P:=\langle x\rangle$ is a Sylow $3$-subgroup and $P\cong C_9$.
::: {.proof}
Since $x$ has order $9=3^2$, $P$ has the full $3$-part of $|G|$, so it is a Sylow $3$-subgroup.
:::

<1>3. We have
\[
G=N\rtimes P\cong C_{13}\rtimes_\theta C_9
\]
for a homomorphism
\[
\theta:C_9\to\operatorname{Aut}(C_{13})\cong C_{12}.
\]
::: {.proof}
The intersection $N\cap P$ is trivial because its order divides both $13$ and $9$.
Since $N$ is normal,
\[
|NP|=\frac{|N||P|}{|N\cap P|}=13\cdot9=117=|G|,
\]
so $G=NP$.
Conjugation by $P$ on $N$ gives the displayed semidirect product.
:::

<1>4. The image of $\theta$ has order either $1$ or $3$.
::: {.proof}
The image order divides both $|C_9|=9$ and $|C_{12}|=12$, hence divides $\gcd(9,12)=3$.
:::

<1>5. If $\theta$ is trivial, then
\[
G\cong C_{13}\times C_9\cong C_{117}.
\]
::: {.proof}
A semidirect product with trivial action is the direct product.
Since $13$ and $9$ are coprime, $C_{13}\times C_9$ is cyclic of order $117$.
:::

<1>6. If $\theta$ is nontrivial, then there is exactly one isomorphism type, represented by
\[
G_{\mathrm{nt}}
=\langle x,y\mid x^9=y^{13}=1,\;xyx^{-1}=y^3\rangle.
\]
::: {.proof}
The cyclic group $\operatorname{Aut}(C_{13})\cong C_{12}$ has a unique subgroup of order $3$.
Its two generators are the automorphisms $y\mapsto y^3$ and $y\mapsto y^9$, since $3$ and $9=3^2$ have order $3$ modulo $13$.

Thus every nontrivial $\theta$ has this same image.
The two possible maps are equivalent under the automorphism $C_9\to C_9$ sending a generator $x$ to $x^2$: precomposing the action $y\mapsto y^3$ by $x\mapsto x^2$ changes it to $y\mapsto y^{3^2}=y^9$.
Semidirect products whose actions differ by an automorphism of the complement are isomorphic.
Hence there is only one nonabelian isomorphism type.
:::

<1>7. Both groups contain an element of order $9$, and these are the only possibilities.
Therefore
\[
\boxed{G\cong C_{117}\quad\text{or}\quad
G\cong C_{13}\rtimes C_9\text{ with nontrivial image of order }3.}
\]
::: {.proof}
In both constructions the displayed $C_9$ complement contains an element of order $9$.
Steps <1>1--<1>6 show that every group satisfying the hypotheses must be one of these two semidirect products.
The first is abelian and the second is nonabelian, so they are not isomorphic.
:::
:::
