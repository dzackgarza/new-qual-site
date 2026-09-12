---
schema: qual/card@1
id: P-ALGS12F
kind: problem
title: Galois group of $(x^3-2)(x^2-3)$ over $\mathbb{Q}$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared against the official UCSD Spring 2012 Algebra qualifying exam; statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Computed the compositum degree and distinguished the three nonabelian groups of order twelve via Sylow-2 structure.
---

::: problem
Let $K$ be the splitting field over $\mathbb{Q}$ of the polynomial $f(x) = (x^3-2)(x^2-3)$.

(a) Show that $[K:\mathbb{Q}] = 12$.

(b) Take as given that every non-Abelian group of order twelve is isomorphic to either $A_4$, the dihedral group $D_{12}$, or else the semidirect product $\mathbb{Z}/3\mathbb{Z} \rtimes_\phi \mathbb{Z}/4\mathbb{Z}$ where $\phi$ sends the generator of $\mathbb{Z}/4\mathbb{Z}$ to the non-identity automorphism of $\mathbb{Z}/3\mathbb{Z}$.
For each of these three groups, calculate what a Sylow-$2$ subgroup is up to isomorphism, and whether or not it is normal in the group.

(c) Which group of order twelve must the Galois group $\mathrm{Gal}(K/\mathbb{Q})$ be?
:::

::: {.solution}
Let $\alpha=\sqrt[3]{2}$ and let $\omega$ be a primitive cube root of unity.
The splitting field of $x^3-2$ is
\[
E=\mathbb Q(\alpha,\omega).
\]

<1>1. We have $[K:\mathbb Q]=12$.
::: {.proof}
The polynomial $x^3-2$ is Eisenstein at $2$, hence irreducible over $\mathbb Q$.
Its discriminant is
\[
-27\cdot 2^2=-108,
\]
which is not a square in $\mathbb Q$.
Therefore its splitting field $E$ has degree $6$ and
\[
\operatorname{Gal}(E/\mathbb Q)\cong S_3.
\]
The unique subgroup of index $2$ in $S_3$ is $A_3$, so $E$ has a unique quadratic subfield.
It is
\[
\mathbb Q(\omega)=\mathbb Q(\sqrt{-3}).
\]
In particular $\sqrt3\notin E$.
Hence
\[
[E(\sqrt3):E]=2.
\]
Since $K$ is the compositum of $E$ with the splitting field $\mathbb Q(\sqrt3)$ of $x^2-3$, we obtain
\[
[K:\mathbb Q]=[K:E][E:\mathbb Q]=2\cdot6=12.
\]
:::

<1>2. The Sylow-$2$ subgroups of the three listed nonabelian groups of order $12$ are as follows.
::: {.proof}
For $A_4$, the Klein four subgroup
\[
V_4=\{e,(12)(34),(13)(24),(14)(23)\}
\]
has order $4$, so it is a Sylow-$2$ subgroup; it is normal.

For the dihedral group $D_{12}=\langle r,s\mid r^6=s^2=1,\ srs=r^{-1}\rangle$, a Sylow-$2$ subgroup is
\[
\langle r^3,s\rangle\cong V_4.
\]
There are three such subgroups, so it is not normal.

For $C_3\rtimes C_4$ with the generator of $C_4$ acting on $C_3$ by inversion, the displayed $C_4$ is a Sylow-$2$ subgroup.
It is not normal: if $a$ generates $C_3$ and $b$ generates $C_4$, with $bab^{-1}=a^{-1}$, then conjugating $b$ by $a$ does not remain in $\langle b\rangle$.
:::

<1>3. We have
\[
\operatorname{Gal}(K/\mathbb Q)\cong D_{12}.
\]
::: {.proof}
Both $E/\mathbb Q$ and $\mathbb Q(\sqrt3)/\mathbb Q$ are Galois, and their intersection is $\mathbb Q$ because $\sqrt3\notin E$.
Hence restriction gives
\[
\operatorname{Gal}(K/\mathbb Q)
 \cong \operatorname{Gal}(E/\mathbb Q)\times
       \operatorname{Gal}(\mathbb Q(\sqrt3)/\mathbb Q)
 \cong S_3\times C_2.
\]
This group has a Sylow-$2$ subgroup isomorphic to $C_2\times C_2$, and it is not normal.
By <1>2 it is therefore neither $A_4$ nor $C_3\rtimes C_4$, so among the three listed nonabelian groups it is $D_{12}$.
Equivalently, $S_3\times C_2\cong D_{12}$.
:::
:::
