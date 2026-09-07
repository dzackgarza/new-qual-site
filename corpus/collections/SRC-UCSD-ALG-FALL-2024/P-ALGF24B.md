---
schema: qual/card@1
id: P-ALGF24B
kind: problem
title: Minimal normal subgroup of a finite solvable group; Hall subgroup of order $m$
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Normal Subgroups
  - Solvable Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Compared both parts and the hint with Problem 2 on page 3 of the official FA24 algebra exam PDF.
- event: solution-written
  by: gpt-6-astra-pro
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Checked every induction order and coprimality condition; the remaining normal Hall p-subgroup case is proved by a Sylow normalizer argument, without assuming Hall existence or Schur-Zassenhaus.
---

::: problem
Suppose $G$ is a non-trivial finite solvable group, $|G| = mn$, and $\gcd(m,n) = 1$.

(a) Suppose $Q$ is a minimal normal subgroup of $G$; that means $Q$ is a normal subgroup, $Q \neq \{1\}$, and no proper non-trivial subgroup of $Q$ is normal in $G$.
Prove that $Q$ is an abelian $p$-group for some prime $p$.

(b) Prove that $G$ has a subgroup of order $m$.
:::

::: hint
Use induction and make use of $G/Q$.
:::

::: {.solution}
<1>1. Every minimal nontrivial normal subgroup $Q$ of a finite solvable group $G$ is an abelian $p$-group for some prime $p$.
::: {.proof}
The commutator subgroup $Q'=[Q,Q]$ is characteristic in $Q$, hence normal in $G$.
The group $Q$ is solvable, because its derived series is termwise contained in the derived series of $G$.
Therefore $Q'\ne Q$: otherwise every term of the derived series of the nontrivial group $Q$ would equal $Q$.
Minimal normality now forces $Q'=1$, so $Q$ is abelian.

Choose a prime $p$ dividing $|Q|$.
In an abelian group, conjugation is trivial, so the Sylow conjugacy theorem implies that its Sylow $p$-subgroup $P$ is unique.
Every automorphism of $Q$ sends $P$ to a Sylow $p$-subgroup, hence to itself.
Thus $P$ is characteristic in $Q$ and normal in $G$.
Since $P\ne1$, minimal normality gives $P=Q$.
This proves part (a).
:::

<1>2. For part (b), induction on $|G|$ reduces the problem to the case in which a minimal normal subgroup $Q$ has order $n=p^a$, with $p\nmid m$.
::: {.proof}
We prove the assertion for all finite solvable groups, including the trivial group, for which it is immediate.
The cases $m=1$ and $n=1$ are solved by the subgroups $1$ and $G$, respectively.
Assume $m,n>1$ and the assertion for every smaller finite solvable group.
Choose a minimal nontrivial normal subgroup $Q$; this exists because $G$ is finite.
By <1>1, $|Q|=p^a$ for a prime $p$ and $a\ge1$.
Subgroups and quotients of solvable groups are solvable, as follows by taking the images or restrictions of their derived series.

If $p\mid m$, coprimality gives $p^a\mid m$ and
\[
|G/Q|=(m/p^a)n,\qquad \gcd(m/p^a,n)=1.
\]
Induction gives a subgroup of $G/Q$ of order $m/p^a$.
Its inverse image in $G$ has order $m$, as required.

If $p\mid n$, induction gives a subgroup $\overline H\le G/Q$ of order $m$.
Its inverse image $H$ has order $mp^a$.
When $H<G$, induction applied to $H$, with the coprime factors $m$ and $p^a$, produces a subgroup of order $m$.
The only remaining case is $H=G$, in which $n=p^a=|Q|$.
:::

<1>3. In the remaining case, there is a nontrivial $r$-subgroup $R$ for a prime $r\ne p$ such that
\[
G=Q N_G(R).
\]
::: {.proof}
The nontrivial solvable group $G/Q$ has a minimal nontrivial normal subgroup $\overline B$.
By <1>1 applied to $G/Q$, it has order $r^b$ for some prime $r$ and $b\ge1$.
Since $|G/Q|=m$, we have $r\ne p$.
Let $B$ be the inverse image of $\overline B$ in $G$.
Then $B\trianglelefteq G$ and $|B|=p^a r^b$.
Choose a Sylow $r$-subgroup $R$ of $B$.
It has order $r^b$, intersects $Q$ trivially, and satisfies $B=QR$ by counting orders.

For every $g\in G$, normality of $B$ implies that $gRg^{-1}$ is also a Sylow $r$-subgroup of $B$.
Sylow conjugacy gives $b_0\in B$ such that $gRg^{-1}=b_0Rb_0^{-1}$.
Thus $b_0^{-1}g\in N_G(R)$, proving $G=BN_G(R)$.
Since $B=QR$ and $R\le N_G(R)$, this is $G=QN_G(R)$.
:::

<1>4. Write $N=N_G(R)$ and $K=Q\cap N$.
Then either $N$ has order $m$, or $R$ is normal in $G$.
::: {.proof}
The subgroup $K$ is normalized by $N$, since $Q$ is normal in $G$.
It is also normalized by $Q$, since $Q$ is abelian.
By $G=QN$ from <1>3, $K$ is normal in $G$.
Minimal normality of $Q$ therefore gives $K=1$ or $K=Q$.

If $K=1$, the product formula gives
\[
|N|=\frac{|G|}{|Q|}=m,
\]
so $N$ is the desired subgroup.
If $K=Q$, then $Q\le N$, whence $G=QN=N$.
Thus every element of $G$ normalizes $R$, and $R\trianglelefteq G$.
:::

<1>5. The case $R\trianglelefteq G$ also yields a subgroup of order $m$.
::: {.proof}
Here $|R|=r^b>1$ divides $m$ and
\[
|G/R|=(m/r^b)n,\qquad \gcd(m/r^b,n)=1.
\]
Induction applies to the smaller solvable group $G/R$ and gives a subgroup of order $m/r^b$.
Its inverse image in $G$ has order $m$.
This completes the remaining case of <1>2, the induction, and part (b).
:::
:::
