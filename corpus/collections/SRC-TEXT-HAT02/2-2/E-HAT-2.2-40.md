---
schema: qual/card@1
id: E-HAT-2.2-40
kind: problem
title: Universal coefficient short exact sequence for homology with $\ZZ_n$ coefficients
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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the Bockstein sequence: exactness of $H_i\xrightarrow{n}H_i\to H_i(\ZZ_n)\to H_{i-1}$
    gives $0\to H_i/nH_i\to H_i(\ZZ_n)\to{}_nH_{i-1}\to0$. Read both directions of the
    characterisation: vanishing of $G/pG$ and of ${}_pG$ for every prime makes multiplication by
    every nonzero integer invertible, which is a $\QQ$-vector-space structure, and on a
    $\QQ$-vector space multiplication by $p$ is an automorphism, so both terms vanish.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 40 as printed on p. 159. The short exact sequence follows from the
    long exact sequence by coker-kernel, and both directions of the equivalence are correct:
    G/pG = 0 and _pG = 0 for all primes p make multiplication by every nonzero integer bijective,
    whence the Q-vector space structure exists and is unique, and conversely a Q-vector space has
    p an automorphism. Additions: the chain-level sequence and the coefficient groups are cited to
    pp. 153-154 with Theorem 2.16 p. 117, and the degree-zero case, where reduced and unreduced
    groups differ, is now settled separately with Proposition 2.6 p. 109 - both sides hold exactly
    when X is path connected. What is not covered: no certificate.
---

::: {.problem}
From the long exact sequence of homology groups associated to the short exact sequence of chain complexes $0 \to C_i(X) \xrightarrow{n} C_i(X) \to C_i(X; \ZZ_n) \to 0$ deduce immediately that there are short exact sequences

$$0 \to H_i(X)/nH_i(X) \to H_i(X; \ZZ_n) \to n\text{-Torsion}(H_{i-1}(X)) \to 0$$

where $n$-Torsion$(G)$ is the kernel of the map $G \xrightarrow{n} G$, $g \mapsto ng$.
Use this to show that $\tilde{H}_i(X; \ZZ_p) = 0$ for all $i$ and all primes $p$ iff $\tilde{H}_i(X)$ is a vector space over $\QQ$ for all $i$.
:::

::: {.solution}
The short exact sequence of chain complexes
$$
0\longrightarrow C_*(X)
\xrightarrow{\,n\,}C_*(X)
\longrightarrow C_*(X;\ZZ_n)
\longrightarrow0
$$
is the one discussed in the subsection on homology with coefficients (pp. 153--154), where $C_i(X;\ZZ_n)$ is identified with the chains with $\ZZ_n$ coefficients; the exactness of the sequence of chain complexes is immediate because $C_i(X)$ is free. It gives the long exact sequence, by Theorem 2.16 (p. 117),
$$
\cdots\to H_i(X)\xrightarrow{n}H_i(X)
\to H_i(X;\ZZ_n)
\to H_{i-1}(X)\xrightarrow{n}H_{i-1}(X)\to\cdots.
$$
For $i\ge1$ the reduced and ordinary groups agree in every degree occurring here; the case $i=0$ is treated at the end.

::: pf

::: {.pf-step #s1}

Exactness yields a short exact sequence
$$
0\to H_i(X)/nH_i(X)
\to H_i(X;\ZZ_n)
\to {}_nH_{i-1}(X)
\to0,
$$
where
$$
{}_nG=\ker(n:G\to G).
$$

::: pf-proof

The kernel of the map into $H_i(X;\ZZ_n)$ is the image $nH_i(X)$, so the first map factors injectively through the cokernel
$$
H_i(X)/nH_i(X).
$$
The image of the connecting map is exactly the kernel of multiplication by $n$ on $H_{i-1}(X)$. These two observations give the displayed short exact sequence.

:::

:::

::: pf-step

If
$$
\widetilde H_i(X;\ZZ_p)=0
$$
for every $i$ and every prime $p$, then every integral reduced homology group
$$
G=\widetilde H_i(X)
$$
is a $\QQ$-vector space.

::: pf-proof

Applying step [](#s1){.pf-ref} with $n=p$ gives simultaneously
$$
G/pG=0
$$
and
$$
{}_pG=0
$$
for every prime $p$. Thus multiplication by $p$ is both surjective and injective on $G$. Hence multiplication by every nonzero integer is bijective. There is therefore a unique division operation by each nonzero integer, defining a unique $\QQ$-vector-space structure on the abelian group $G$.

:::

:::

::: pf-step

Conversely, if every $\widetilde H_i(X)$ is a $\QQ$-vector space, then
$$
\widetilde H_i(X;\ZZ_p)=0
$$
for all $i$ and all primes $p$.

::: pf-proof

On a $\QQ$-vector space, multiplication by $p$ is an automorphism. Hence both
$$
G/pG
$$
and ${}_pG$ vanish. The short exact sequence in step [](#s1){.pf-ref} then forces the homology with $\ZZ_p$ coefficients to vanish.

:::

:::

:::

Thus
$$
\boxed{
\widetilde H_i(X;\ZZ_p)=0\text{ for all }i,p
\iff
\widetilde H_i(X)\text{ is a }\QQ\text{-vector space for all }i.}
$$
In degree $0$ both sides say the same thing about the number of path components: $\widetilde H_0(X;\ZZ_p)\cong\ZZ_p^{c-1}$ and $\widetilde H_0(X)\cong\ZZ^{c-1}$ for $c$ the number of path components, by Proposition 2.6 (p. 109) applied to each coefficient group, so both vanish for all $p$ exactly when $c=1$, which is also exactly when $\widetilde H_0(X)$ is a $\QQ$-vector space.The coefficient exact sequence and divisibility conclusion match **Kenneth DeMason, *M382C Full Credit HW Problems* (2021)**, Hatcher 2.2.40, printed p. 68. In particular, $G/pG=0$ and ${}_pG=0$ for all primes $p$ says precisely that $G$ is uniquely $p$-divisible for every $p$, which is the scalar restriction from $\QQ$ to $\ZZ$. Hence it has a natural $\QQ$-vector-space structure exactly when every reduced mod-$p$ group vanishes.


:::
