---
schema: qual/card@1
id: P-ALGF18A
kind: problem
title: Group of order $2pq$ has normal subgroups of orders $pq$ and $q$
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 1 of the official UCSD Algebra Qualifying Exam, Fall 2018 source; the hypotheses and requested normal subgroups agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Replaced the false claim 2p<q with a complete Sylow case split; in the exceptional n_q=2p case, element counting forces a normal Sylow p-subgroup.
---

::: problem
Suppose $p < q$ are two odd primes.
Suppose $G$ is a group of order $2pq$.
Prove that $G$ has normal subgroups $N_1$ and $N_2$ such that $|N_1| = pq$, $|N_2| = q$, and $N_2 \subseteq N_1$.
:::

::: {.solution}
Let $n_q$ denote the number of Sylow $q$-subgroups of $G$.

<1>1. Either the Sylow $q$-subgroup of $G$ is normal, or
\[
n_q=2p.
\]
::: {.proof}
Sylow's theorem gives
\[
n_q\equiv1\pmod q,
\qquad
n_q\mid2p.
\]
The positive divisors of $2p$ are
\[
1,2,p,2p.
\]
Since $p<q$ and $q$ is odd, neither $2$ nor $p$ is congruent to $1$ modulo $q$.
Thus, if $n_q\neq1$, the only remaining possibility is
\[
n_q=2p.
\]
:::

<1>2. If $n_q=1$, there are normal subgroups
\[
N_2\triangleleft N_1\triangleleft G
\]
with $|N_2|=q$ and $|N_1|=pq$.
::: {.proof}
Let $N_2$ be the unique Sylow $q$-subgroup. Then
\[
N_2\triangleleft G.
\]
The quotient $G/N_2$ has order $2p$.
Its number of Sylow $p$-subgroups divides $2$ and is congruent to $1$ modulo $p$.
Because $p$ is odd, that number is $1$.
Hence $G/N_2$ has a normal subgroup of order $p$.
Let $N_1$ be its inverse image under the quotient map.
Then
\[
N_1\triangleleft G,
\qquad
N_2\subseteq N_1,
\qquad
|N_1|=pq.
\]
:::

<1>3. Suppose $n_q=2p$. Then the Sylow $p$-subgroup of $G$ is normal.
::: {.proof}
Distinct Sylow $q$-subgroups intersect trivially, because each has prime order $q$.
Thus the $2p$ Sylow $q$-subgroups contribute
\[
2p(q-1)
\]
distinct nonidentity elements of order $q$.
Therefore the number of elements of $G$ not among these nonidentity $q$-elements is
\[
2pq-2p(q-1)=2p.
\]

Let $n_p$ be the number of Sylow $p$-subgroups.
Distinct Sylow $p$-subgroups likewise intersect trivially, so their nonidentity elements contribute
\[
n_p(p-1)
\]
distinct elements, all of which lie outside the nonidentity $q$-elements.
Hence
\[
n_p(p-1)\le 2p-1,
\]
because the identity is one of the $2p$ remaining elements.
Consequently
\[
n_p<3.
\]
But Sylow's theorem also gives
\[
n_p\equiv1\pmod p.
\]
Since $p\ge3$, the only positive integer less than $3$ satisfying this congruence is
\[
n_p=1.
\]
Thus the Sylow $p$-subgroup $P$ is normal in $G$.
:::

<1>4. In the case $n_q=2p$, there are again normal subgroups
\[
N_2\triangleleft N_1\triangleleft G
\]
with $|N_2|=q$ and $|N_1|=pq$.
::: {.proof}
By <1>3, let $P\triangleleft G$ be the Sylow $p$-subgroup.
Then
\[
|G/P|=2q.
\]
The number of Sylow $q$-subgroups of $G/P$ divides $2$ and is congruent to $1$ modulo $q$, hence equals $1$.
Let $\overline N_1$ be this unique subgroup of order $q$, and let $N_1$ be its inverse image in $G$.
Then
\[
N_1\triangleleft G,
\qquad
|N_1|=pq.
\]

Inside the group $N_1$ of order $pq$, the number of Sylow $q$-subgroups divides $p$ and is congruent to $1$ modulo $q$.
Since $p<q$, that number is $1$.
Let $N_2$ be this unique Sylow $q$-subgroup of $N_1$.
It is characteristic in $N_1$, because every automorphism of $N_1$ permutes its Sylow $q$-subgroups.
Since $N_1\triangleleft G$, it follows that
\[
N_2\triangleleft G.
\]
Finally,
\[
|N_2|=q,
\qquad
N_2\subseteq N_1.
\]
:::

<1>5. The required subgroups exist in every case.
::: {.proof}
By <1>1, either $n_q=1$ or $n_q=2p$.
The first case is settled by <1>2 and the second by <1>4.
:::
:::
