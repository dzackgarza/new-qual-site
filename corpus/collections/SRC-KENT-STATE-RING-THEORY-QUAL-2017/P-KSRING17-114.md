---
schema: qual/card@1
id: P-KSRING17-114
kind: problem
title: Nilpotents form an ideal in a ring with no nontrivial automorphisms
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 114 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a ring with identity such that the identity map is the only ring automorphism of R. Prove that the set N of all nilpotent elements of R is an ideal of R.
:::

::: {.solution}
Let
$$
N
\coloneqq
\{n\in R:n^k=0\text{ for some }k\ge1\}.
$$

<1>1. Every unit of $R$ is central.

::: {.proof}
Let
$$
u\in R^\times.
$$
Conjugation by $u$ defines a ring automorphism
$$
\operatorname{Ad}_u:R\to R,
\qquad
\operatorname{Ad}_u(r)
\coloneqq
uru^{-1}.
$$
By hypothesis, the identity map is the only ring automorphism of $R$.
Therefore
$$
uru^{-1}
=
r
$$
for every
$$
r\in R.
$$
Multiplying on the right by $u$ gives
$$
ur=ru.
$$
Thus
$$
u\in Z(R).
$$
:::

<1>2. If
$$
n\in N,
$$
then
$$
1+n
$$
is a unit.

::: {.proof}
Choose
$$
k\ge1
$$
such that
$$
n^k=0.
$$
Then
$$
\begin{aligned}
(1+n)
\left(
1-n+n^2-\cdots+(-1)^{k-1}n^{k-1}
\right)
&=
1+(-1)^{k-1}n^k\\
&=
1.
\end{aligned}
$$
The same finite geometric-series computation on the other side gives a two-sided inverse.
Hence
$$
1+n
\in
R^\times.
$$
:::

<1>3. Every nilpotent element of $R$ is central.

::: {.proof}
Let
$$
n\in N.
$$
By step <1>2,
$$
1+n
$$
is a unit.
By step <1>1,
$$
1+n
$$
is central.
Since $1$ is central,
$$
n
=
(1+n)-1
$$
is also central.
Thus
$$
\boxed{
N\subseteq Z(R).
}
$$
:::

<1>4. If
$$
n,m\in N,
$$
then
$$
n+m
\in
N.
$$

::: {.proof}
Choose
$$
a,b\ge1
$$
with
$$
n^a=0,
\qquad
m^b=0.
$$
By step <1>3, both $n$ and $m$ are central, hence commute.
Therefore the binomial theorem applies:
$$
(n+m)^{a+b-1}
=
\sum_{j=0}^{a+b-1}
\binom{a+b-1}{j}
n^j m^{a+b-1-j}.
$$
For each summand, either
$$
j\ge a,
$$
so
$$
n^j=0,
$$
or
$$
j\le a-1,
$$
so
$$
a+b-1-j
\ge
b,
$$
and
$$
m^{a+b-1-j}=0.
$$
Thus every summand vanishes and
$$
(n+m)^{a+b-1}=0.
$$
Hence
$$
n+m\in N.
$$
:::

<1>5. If
$$
n\in N,
$$
then
$$
-n\in N.
$$

::: {.proof}
If
$$
n^k=0,
$$
then
$$
(-n)^k
=
(-1)^k n^k
=
0.
$$
:::

<1>6. The set $N$ is an additive subgroup of $R$.

::: {.proof}
The element
$$
0
$$
is nilpotent.
Step <1>4 gives closure under addition, and step <1>5 gives closure under additive inverses.
:::

<1>7. If
$$
r\in R
$$
and
$$
n\in N,
$$
then
$$
rn
\in
N
$$
and
$$
nr
\in
N.
$$

::: {.proof}
By step <1>3,
$$
n
$$
is central, so
$$
rn=nr.
$$
Choose
$$
k\ge1
$$
with
$$
n^k=0.
$$
Because $r$ commutes with $n$,
$$
(rn)^k
=
r^k n^k
=
0.
$$
Thus
$$
rn\in N.
$$
Since
$$
nr=rn,
$$
one also has
$$
nr\in N.
$$
:::

<1>8. Therefore
$$
\boxed{
N
\text{ is a two-sided ideal of }R.
}
$$

::: {.proof}
Step <1>6 shows that $N$ is an additive subgroup, and step <1>7 shows that it absorbs multiplication from both sides by arbitrary elements of $R$.
Hence
$$
N\trianglelefteq R.
$$
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required conclusion.
:::
:::
