---
schema: qual/card@1
id: P-MMAQ-5EFTFEKRDI
kind: problem
title: An irreducible quintic over $\mathbb{Q}$ with three real roots is not solvable
  by radicals, and a quadratic Galois subfield of its splitting field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $f(x)$ be an irreducible polynomial of degree 5 over the field $\mathbb Q$ of rational numbers with exactly 3 real roots.

- Show that $f(x)$ is not solvable by radicals.

- Let $E$ be the splitting field of $f$ over $\mathbb Q$.
  Construct a Galois extension $K$ of degree 2 over $\mathbb Q$ lying in $E$ such that *no* field $F$ strictly between $K$ and $E$ is Galois over $\mathbb Q$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let
\[
G=\operatorname{Gal}(E/\mathbb Q).
\]
Then $G$ acts transitively on the five roots of $f$.

::: pf-proof

The polynomial $f$ is irreducible over $\mathbb Q$ and, since the characteristic is zero, it is separable. In the splitting field of an irreducible separable polynomial, the Galois group acts transitively on the roots: any $\mathbb Q$-embedding sending one root to another extends to an automorphism of the normal splitting field $E$.

:::

:::

::: {.pf-step #s2}

The group $G$ contains a $5$-cycle.

::: pf-proof

By step [](#s1){.pf-ref}, the action of $G$ on five roots is transitive. Orbit-stabilizer therefore implies that $5$ divides $|G|$. By Cauchy's theorem, $G$ contains an element of order $5$. Viewed inside $S_5$, any element of order $5$ is a $5$-cycle.

:::

:::

::: {.pf-step #s3}

The group $G$ contains a transposition.

::: pf-proof

Complex conjugation preserves $E$ because $f$ has rational coefficients. By hypothesis, three roots of $f$ are real, so complex conjugation fixes those three roots. The remaining two roots are nonreal and, because the coefficients are real, form a conjugate pair; complex conjugation swaps them. Hence its permutation of the five roots is a transposition.

:::

:::

::: {.pf-step #s4}

A $5$-cycle together with any transposition generates $S_5$.

::: pf-proof

Let
\[
\sigma=(0\,1\,2\,3\,4)
\]
be a $5$-cycle after relabeling the roots, and let
\[
\tau=(a\,b)
\]
be any transposition. Conjugating by powers of $\sigma$ gives the transpositions
\[
\sigma^k\tau\sigma^{-k}=(a+k\,b+k)
\qquad (k\in\mathbb Z/5\mathbb Z).
\]
Let $d=b-a\not\equiv0\pmod5$. These are the edges
\[
(k\,\,k+d)
\]
of a graph on $\mathbb Z/5\mathbb Z$. Since $5$ is prime and $d\ne0$, repeated addition of $d$ reaches every residue class, so this graph is connected. Transpositions along the edges of a connected graph generate the full symmetric group on its vertices. Hence
\[
\langle\sigma,\tau\rangle=S_5.
\]

:::

:::

::: {.pf-step #s5}

Therefore
\[
G=S_5.
\]

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, $G$ contains a $5$-cycle and a transposition. By step [](#s4){.pf-ref}, those two elements generate $S_5$. Since $G\le S_5$, it follows that $G=S_5$.

:::

:::

::: pf-step

The polynomial $f$ is not solvable by radicals.

::: pf-proof

A polynomial over a field of characteristic zero is solvable by radicals only if the Galois group of its splitting field is a solvable group. By step [](#s5){.pf-ref} this Galois group is $S_5$. The subgroup $A_5\trianglelefteq S_5$ is nonabelian simple, hence not solvable; therefore $S_5$ is not solvable. Thus $f$ is not solvable by radicals.

:::

:::

::: {.pf-step #s7}

Let $r_1,\dots,r_5$ be the roots of $f$ and define
\[
\delta=\prod_{1\le i<j\le5}(r_i-r_j).
\]
Then
\[
\delta^2=\Delta(f)\in\mathbb Q,
\]
and
\[
K=\mathbb Q(\delta)=\mathbb Q(\sqrt{\Delta(f)})
\]
is the fixed field $E^{A_5}$.

::: pf-proof

For $\sigma\in S_5=G$, permuting the roots changes the Vandermonde product by the sign of the permutation:
\[
\sigma(\delta)=\operatorname{sgn}(\sigma)\delta.
\]
Hence every element of $A_5$ fixes $\delta$, while every odd permutation sends $\delta$ to $-\delta$. Since $G$ contains odd permutations, $\delta\notin\mathbb Q$. Therefore the stabilizer of $\delta$ in $G$ is exactly $A_5$, so by the Galois correspondence
\[
\mathbb Q(\delta)=E^{A_5}.
\]
Also $\delta^2$ is the discriminant $\Delta(f)$, which lies in $\mathbb Q$.

:::

:::

::: pf-step

The extension $K/\mathbb Q$ is Galois of degree $2$.

::: pf-proof

By step [](#s7){.pf-ref},
\[
K=E^{A_5}.
\]
Since $A_5\trianglelefteq S_5$ and
\[
[S_5:A_5]=2,
\]
the Galois correspondence gives
\[
[K:\mathbb Q]=2
\]
and
\[
\operatorname{Gal}(K/\mathbb Q)\cong S_5/A_5\cong C_2.
\]
Thus $K/\mathbb Q$ is Galois.

:::

:::

::: pf-step

No field $F$ satisfying
\[
K\subsetneq F\subsetneq E
\]
is Galois over $\mathbb Q$.

::: pf-proof

Let
\[
H=\operatorname{Gal}(E/F).
\]
Because $K=E^{A_5}$, the strict containments $K\subsetneq F\subsetneq E$ correspond to
\[
1<H<A_5.
\]
If $F/\mathbb Q$ were Galois, then by the Galois correspondence $H$ would be normal in
\[
G=S_5.
\]
But a normal subgroup $H\trianglelefteq S_5$ contained in $A_5$ is also normal in $A_5$. Since $A_5$ is simple, such an $H$ is either $1$ or $A_5$, contradicting
\[
1<H<A_5.
\]
Therefore no strict intermediate field between $K$ and $E$ is Galois over $\mathbb Q$.

:::

:::

:::

:::
