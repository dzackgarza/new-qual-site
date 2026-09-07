---
schema: qual/card@1
id: P-ALGF23B
kind: problem
title: "Groups of order pm with a self-normalizing Sylow p-subgroup"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 2 of the official UCSD Algebra Qualifying Exam, Fall 2023 source; all three parts and the self-normalizing Sylow hypothesis agree with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Replaced the retained induction with a direct Frattini-argument proof that the prime quotient in part (b) must have prime p, yielding the normal subgroup of order m.
---

::: problem
Suppose $G$ is a finite group, $p$ is prime, $m$ is an integer, $\gcd(p, m) = 1$, and $|G| = pm$.
Suppose $P$ is a Sylow $p$-subgroup and $N_G(P) = P$.

(a) Prove that if $G$ has a subgroup $H$ of order $m$, then $$H = \{x \in G \mid o(x) \neq p\}.$$ Deduce that in this case, $H$ is a characteristic subgroup.

(b) Suppose $G$ is solvable.
Prove that $G$ has a normal subgroup $N$ such that $G/N \cong \mathbb{Z}/\ell\mathbb{Z}$ for some prime $\ell$.

(c) Suppose $G$ is solvable.
Prove that $G$ has a normal subgroup of order $m$.

Hint: Use induction on $|G|$, the subgroup $N$ from the previous part, and a Sylow $\ell$-subgroup of $N$ if needed.
:::

::: {.solution}
<1>1. The number of Sylow $p$-subgroups of $G$ is $m$.
::: {.proof}
Because $p\nmid m$, a Sylow $p$-subgroup has order exactly $p$.
The conjugation action on the Sylow $p$-subgroups gives
\[
n_p=[G:N_G(P)].
\]
Using $N_G(P)=P$,
\[
n_p=\frac{pm}{p}=m.
\]
:::

<1>2. Exactly $m(p-1)$ elements of $G$ have order $p$.
::: {.proof}
Distinct subgroups of order $p$ intersect only in the identity.
Each of the $m$ Sylow $p$-subgroups from <1>1 contains exactly $p-1$ nonidentity elements, all of order $p$.
Every element of order $p$ generates a Sylow $p$-subgroup.
Hence the sets of nonidentity elements of the Sylow $p$-subgroups partition the elements of order $p$, and their total number is
\[
m(p-1).
\]
:::

<1>3. If $H\le G$ has order $m$, then
\[
H=\{x\in G:o(x)\ne p\}.
\]
::: {.proof}
By Lagrange's theorem and $p\nmid m$, no element of $H$ has order $p$.
Therefore
\[
H\subseteq\{x\in G:o(x)\ne p\}.
\]
By <1>2, the set on the right has cardinality
\[
pm-m(p-1)=m.
\]
Since $|H|=m$, the inclusion is an equality.
:::

<1>4. Every subgroup $H$ of order $m$ is characteristic in $G$.
::: {.proof}
Automorphisms preserve element orders.
Thus every automorphism of $G$ preserves the set
\[
\{x\in G:o(x)\ne p\},
\]
which equals $H$ by <1>3.
Hence $H$ is characteristic.
This proves part (a).
:::

<1>5. If $G$ is solvable, then it has a normal subgroup $N$ with
\[
G/N\cong\mathbb Z/\ell\mathbb Z
\]
for some prime $\ell$.
::: {.proof}
A nontrivial solvable group cannot be perfect: if
\[
[G,G]=G,
\]
then its derived series would remain equal to $G$ and could not terminate at the identity.
Hence the abelianization
\[
G^{\mathrm{ab}}=G/[G,G]
\]
is a nontrivial finite abelian group.

Choose a maximal proper subgroup $M<G^{\mathrm{ab}}$.
Then $G^{\mathrm{ab}}/M$ is a finite simple abelian group, hence cyclic of prime order $\ell$.
Let $N$ be the inverse image of $M$ under the quotient map
\[
G\twoheadrightarrow G^{\mathrm{ab}}.
\]
Then $N\trianglelefteq G$ and
\[
G/N\cong G^{\mathrm{ab}}/M\cong\mathbb Z/\ell\mathbb Z.
\]
This proves part (b).
:::

<1>6. If $N\trianglelefteq G$ is a proper normal subgroup and $p$ divides $|N|$, then the hypothesis $N_G(P)=P$ leads to a contradiction.
::: {.proof}
If $p\mid|N|$, then a Sylow $p$-subgroup of $N$ has order $p$ and is also a Sylow $p$-subgroup of $G$.
Because $N$ is normal, it contains every $G$-conjugate of that Sylow subgroup; in particular, after conjugating if necessary, we may take
\[
P\le N.
\]

For completeness, the Frattini argument in this situation gives
\[
G=N\,N_G(P).
\]
Indeed, for any $g\in G$, normality of $N$ implies $gPg^{-1}\le N$; it is another Sylow $p$-subgroup of $N$.
By Sylow conjugacy inside $N$, there exists $n\in N$ such that
\[
n(gPg^{-1})n^{-1}=P.
\]
Thus $ng\in N_G(P)$, and so $g\in N N_G(P)$.

Now $N_G(P)=P\le N$, so
\[
G=N\,N_G(P)=N,
\]
contradicting that $N$ is proper.
:::

<1>7. If $G$ is solvable, it has a normal subgroup of order $m$.
::: {.proof}
Take $N\trianglelefteq G$ from <1>5, so
\[
[G:N]=\ell
\]
for a prime $\ell$.
If $\ell\ne p$, then
\[
|N|=\frac{pm}{\ell}
\]
is divisible by $p$, because $\ell$ divides $m$.
This contradicts <1>6.
Therefore
\[
\ell=p.
\]
Consequently
\[
|N|=\frac{|G|}{p}=m.
\]
Since $N\trianglelefteq G$, this is the required normal subgroup.
This proves part (c).
:::
:::
