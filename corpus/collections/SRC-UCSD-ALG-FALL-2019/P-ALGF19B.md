---
schema: qual/card@1
id: P-ALGF19B
kind: problem
title: Groups with $|\mathrm{Syl}_p(G)| = p+1$ and $|\mathrm{Syl}_q(G)| = q+1$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 2 of the official UCSD Algebra Qualifying Exam, Fall 2019 source; all three parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the conjugation-orbit argument, the Sylow-count dichotomy inside H, and normality of Q from the parity obstruction q+1 not dividing the odd order of P.
---

::: problem
For any finite group $H$ and prime $\ell$, we denote the set of Sylow $\ell$-subgroups of $H$ by $\mathrm{Syl}_\ell(H)$.
Suppose $p < q$ are odd primes, $G$ is a finite group, and $|\mathrm{Syl}_p(G)| = p + 1$ and $|\mathrm{Syl}_q(G)| = q + 1$.

(a) Suppose $P \in \mathrm{Syl}_p(G)$.
Prove that $G$ has a Sylow $q$-subgroup $Q$ such that $Q \subseteq N_G(P)$.

(b) In the setting of part (a), let $H = PQ$.
Argue why $H$ is a subgroup and prove that either $Q \trianglelefteq H$ or $|\mathrm{Syl}_q(H)| = q + 1$.

(c) In the setting of part (b), prove that $H \simeq P \times Q$.
:::

::: {.solution}
<1>1. A Sylow $q$-subgroup of $G$ normalizes $P$.
::: {.proof}
Let $Q\in\operatorname{Syl}_q(G)$ and let $Q$ act by conjugation on the set
\[
\operatorname{Syl}_p(G).
\]
Every orbit has cardinality a power of $q$. Since $p<q$ are distinct odd primes,
\[
|\operatorname{Syl}_p(G)|=p+1<q.
\]
Hence no orbit can have cardinality $q$ or larger, so every orbit has cardinality $1$.
In particular $Q$ fixes the given $P$, which means
\[
Q\subseteq N_G(P).
\]
This proves part (a).
:::

<1>2. The set $H=PQ$ is a subgroup, and $P\trianglelefteq H$.
::: {.proof}
By <1>1, every element of $Q$ normalizes $P$. Thus $Q\subseteq N_G(P)$, so $PQ$ is a subgroup of $G$ and $P$ is normal in $H=PQ$.

Because $P$ is a $p$-group and $Q$ is a $q$-group with $p\ne q$,
\[
P\cap Q=1.
\]
Consequently
\[
|H|=|P|\,|Q|.
\]
:::

<1>3. Either $Q\trianglelefteq H$ or
\[
|\operatorname{Syl}_q(H)|=q+1.
\]
::: {.proof}
Since $Q$ is a Sylow $q$-subgroup of $G$, it is also a Sylow $q$-subgroup of $H$.
Moreover, every Sylow $q$-subgroup of $H$ has order $|Q|$, hence is also a Sylow $q$-subgroup of $G$. Therefore
\[
|\operatorname{Syl}_q(H)|
\le
|\operatorname{Syl}_q(G)|
=q+1.
\]

Sylow's theorem gives
\[
|\operatorname{Syl}_q(H)|\equiv1\pmod q.
\]
The only positive integers at most $q+1$ with this congruence are $1$ and $q+1$.
If the number is $1$, then $Q$ is normal in $H$; otherwise it equals $q+1$.
This proves part (b).
:::

<1>4. In fact $Q\trianglelefteq H$.
::: {.proof}
Again by Sylow's theorem,
\[
|\operatorname{Syl}_q(H)|\mid[H:Q].
\]
By <1>2,
\[
[H:Q]=|P|,
\]
which is a power of the odd prime $p$ and is therefore odd.

The alternative $|\operatorname{Syl}_q(H)|=q+1$ from <1>3 is impossible because $q$ is odd, so $q+1$ is even and cannot divide the odd integer $|P|$.
Hence
\[
|\operatorname{Syl}_q(H)|=1,
\]
and therefore $Q\trianglelefteq H$.
:::

<1>5. The multiplication map $P\times Q\to H$ is an isomorphism.
::: {.proof}
By <1>2 and <1>4, both $P$ and $Q$ are normal in $H$. For $x\in P$ and $y\in Q$, the commutator
\[
[x,y]=xyx^{-1}y^{-1}
\]
lies in $P$ because $P\trianglelefteq H$, and it lies in $Q$ because $Q\trianglelefteq H$.
Since $P\cap Q=1$, we obtain
\[
[x,y]=1.
\]
Thus every element of $P$ commutes with every element of $Q$.

It follows that
\[
\mu:P\times Q\longrightarrow H,
\qquad
\mu(x,y)=xy,
\]
is a homomorphism. It is surjective because $H=PQ$, and its kernel is trivial because $P\cap Q=1$. Hence
\[
H\cong P\times Q.
\]
This proves part (c).
:::
:::
