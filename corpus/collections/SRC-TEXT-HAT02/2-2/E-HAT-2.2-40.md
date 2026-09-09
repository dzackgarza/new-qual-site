---
schema: qual/card@1
id: E-HAT-2.2-40
kind: problem
title: Universal coefficient short exact sequence for homology with $\mathbb{Z}_n$ coefficients
classification:
  areas:
  - topology
  topics:
  - Homology
  - Universal Coefficients
  - Torsion
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 40; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/algebraic proof checked.
---

From the long exact sequence of homology groups associated to the short exact sequence of chain complexes $0 \to C_i(X) \xrightarrow{n} C_i(X) \to C_i(X; \mathbb{Z}_n) \to 0$ deduce immediately that there are short exact sequences

$$0 \to H_i(X)/nH_i(X) \to H_i(X; \mathbb{Z}_n) \to n\text{-Torsion}(H_{i-1}(X)) \to 0$$

where $n$-Torsion$(G)$ is the kernel of the map $G \xrightarrow{n} G$, $g \mapsto ng$.
Use this to show that $\tilde{H}_i(X; \mathbb{Z}_p) = 0$ for all $i$ and all primes $p$ iff $\tilde{H}_i(X)$ is a vector space over $\mathbb{Q}$ for all $i$.

::: {.solution}
The short exact sequence of chain complexes
\[
0\longrightarrow C_*(X)
\xrightarrow{\,n\,}C_*(X)
\longrightarrow C_*(X;\mathbb Z_n)
\longrightarrow0
\]
gives the long exact sequence
\[
\cdots\to H_i(X)\xrightarrow{n}H_i(X)
\to H_i(X;\mathbb Z_n)
\to H_{i-1}(X)\xrightarrow{n}H_{i-1}(X)\to\cdots.
\]

<1>1. Exactness yields a short exact sequence
\[
0\to H_i(X)/nH_i(X)
\to H_i(X;\mathbb Z_n)
\to {}_nH_{i-1}(X)
\to0,
\]
where
\[
{}_nG=\ker(n:G\to G).
\]
::: {.proof}
The kernel of the map into $H_i(X;\mathbb Z_n)$ is the image $nH_i(X)$, so the first map factors injectively through the cokernel
\[
H_i(X)/nH_i(X).
\]
The image of the connecting map is exactly the kernel of multiplication by $n$ on $H_{i-1}(X)$. These two observations give the displayed short exact sequence.
:::

<1>2. If
\[
\widetilde H_i(X;\mathbb Z_p)=0
\]
for every $i$ and every prime $p$, then every integral reduced homology group
\[
G=\widetilde H_i(X)
\]
is a $\mathbb Q$-vector space.
::: {.proof}
Applying <1>1 with $n=p$ gives simultaneously
\[
G/pG=0
\]
and
\[
{}_pG=0
\]
for every prime $p$. Thus multiplication by $p$ is both surjective and injective on $G$. Hence multiplication by every nonzero integer is bijective. There is therefore a unique division operation by each nonzero integer, defining a unique $\mathbb Q$-vector-space structure on the abelian group $G$.
:::

<1>3. Conversely, if every $\widetilde H_i(X)$ is a $\mathbb Q$-vector space, then
\[
\widetilde H_i(X;\mathbb Z_p)=0
\]
for all $i$ and all primes $p$.
::: {.proof}
On a $\mathbb Q$-vector space, multiplication by $p$ is an automorphism. Hence both
\[
G/pG
\]
and ${}_pG$ vanish. The short exact sequence in <1>1 then forces the homology with $\mathbb Z_p$ coefficients to vanish.
:::

Thus
\[
\boxed{
\widetilde H_i(X;\mathbb Z_p)=0\text{ for all }i,p
\iff
\widetilde H_i(X)\text{ is a }\mathbb Q\text{-vector space for all }i.}
\]
:::
