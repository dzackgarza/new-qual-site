---
schema: qual/card@1
id: P-EMAG9
kind: problem
title: At most one subgroup per order forces cyclicity; finite subgroups of $F^\times$ are cyclic
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts with Groups 9 in the retained source extraction; part (a) assumes neither commutativity nor existence of a subgroup for each divisor."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the cyclic-group counting identity, termwise equality without assuming subgroup existence, and uniqueness from the polynomial root bound in arbitrary characteristic."
---

::: problem
(a) Let $G$ be a group of order $n$.
Suppose that for every divisor $d$ of $n$, $G$ contains at most one subgroup of order $d$.
Show that $G$ is cyclic.

(b) Let $F$ be a field.
Show that every finite subgroup of the group of units $F^\times$ is cyclic.
:::

::: solution
<1>1. For every positive integer $n$,
$\sum_{d\mid n}\varphi(d)=n$, where $\varphi(d)$ is
the number of integers $1\leq j\leq d$ relatively prime to $d$.

::: proof
In a cyclic group $C_n=\langle c\rangle$, the order of
$c^k$ is $n/\gcd(n,k)$: its $r$th power is the identity
exactly when $n\mid kr$. For $d\mid n$, the elements
of order exactly $d$ are consequently
$c^{(n/d)j}$ with $j$ ranging over the residues prime to
$d$. There are exactly $\varphi(d)$ of them. Partitioning
the $n$ elements according to their orders proves the
identity, including $\varphi(1)=1$ for the identity element.
:::

<1>2. The group $G$ in part (a) is cyclic.

::: proof
For $d\mid n$, let $a_d$ count the elements of $G$ of
order $d$. If no such element exists, $a_d=0$.
Otherwise choose one, say $g$. Its cyclic subgroup has
order $d$. Every other element of order $d$ generates
a subgroup of that order and hence, by hypothesis,
generates the same subgroup $\langle g\rangle$.
Thus the elements counted by $a_d$ are exactly its
generators, and step <1>1 gives $a_d=\varphi(d)$.
In particular $0\leq a_d\leq\varphi(d)$ for every divisor.

Lagrange's theorem puts every element order among the
divisors of $n$ [@DF04]. Therefore
$$
\sum_{d\mid n}a_d=|G|=n=\sum_{d\mid n}\varphi(d).
$$
All summands $\varphi(d)-a_d$ are nonnegative and their
sum is zero, so each vanishes. In particular
$a_n=\varphi(n)>0$: the residue of $1$ is prime to $n$,
also when $n=1$ under the convention above.
There is an element of order $n$, which generates $G$.
No commutativity assumption on $G$ was used.
:::

<1>3. Every finite subgroup $H\leq F^\times$ is cyclic.

::: proof
For any positive integer $d$, the polynomial $T^d-1$
has at most $d$ roots in $F$. This follows by induction
on degree from the factor theorem: a root $a$ gives
a factor $T-a$, and every other root is a root of
the quotient polynomial, since $F$ is a field.

If $A\leq H$ has order $d$, then $a^d=1$ for every
$a\in A$ by Lagrange's theorem [@DF04]. Hence $A$ is
contained in the root set of $T^d-1$. That set has at
most $d$ members and already contains the $d$ members
of $A$, so it is exactly $A$. Any other subgroup of
order $d$ must equal the same root set and hence equal
$A$. Thus $H$ has at most one subgroup of each order
dividing $|H|$. Step <1>2 proves that $H$ is cyclic.
The argument works in every characteristic and includes
the trivial subgroup.
:::
:::
