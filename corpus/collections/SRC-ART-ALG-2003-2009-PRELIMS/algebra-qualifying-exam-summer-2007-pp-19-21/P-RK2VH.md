---
schema: qual/card@1
id: P-RK2VH
kind: problem
title: Sylow theorems; groups of order $105$ have a normal subgroup of order $35$,
  and both Sylow $5$- and $7$-subgroups are normal
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all four parts with the retained Summer 2007 Groups 1 source extraction, lines 752-759."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the complete Sylow-count possibilities, disjoint element count, normal inverse image, and conjugation argument for both Sylow subgroups."
---

::: problem
a. State the Sylow theorems.

b. Show that in a group of order 105, either the 5-Sylow or the 7-Sylow subgroup is normal.

c. Show that a group of order 105 has a normal subgroup of order 35.

d. Show that in a group of order 105, both the 5-Sylow and the 7-Sylow subgroups are normal.
:::

::: solution
<1>1. The Sylow theorems have the following form.

For a finite group $H$ of order $p^a m$, with $p$ prime and $p\nmid m$,
there is a subgroup of order $p^a$, called a Sylow $p$-subgroup.
Every $p$-subgroup of $H$ is contained in a Sylow $p$-subgroup, and
all Sylow $p$-subgroups are conjugate. Their number $n_p$ divides $m$
and satisfies $n_p\equiv1\pmod p$ [@DF04]. In particular, a Sylow
subgroup is normal if and only if it is the unique Sylow subgroup for
its prime: conjugacy proves one implication, and conjugation
preserves subgroup order for the other.

For the remaining parts, let $|G|=105=3\cdot5\cdot7$.

<1>2. At least one of the Sylow $5$- and $7$-subgroups is normal.

::: proof
The divisibility and congruence conditions in step <1>1 give
$$
n_5\in\{1,21\},\qquad n_7\in\{1,15\}.
$$
Indeed, the divisors of $21$ are $1,3,7,21$, of which only $1$ and
$21$ are $1$ modulo $5$; the divisors of $15$ are $1,3,5,15$, of
which only $1$ and $15$ are $1$ modulo $7$.

Distinct subgroups of prime order intersect only in the identity:
any nonidentity element of such a subgroup generates it. A subgroup
of order $5$ and one of order $7$ also intersect trivially, since the
order of an element in their intersection divides both primes.
Thus $n_5=21$ and $n_7=15$ would give
$$
21(5-1)+15(7-1)=174
$$
distinct nonidentity elements in a group having only $104$ of them.
This is impossible. Hence $n_5=1$ or $n_7=1$.
:::

<1>3. There is a normal subgroup $N\lhd G$ of order $35$.

::: proof
Choose a normal Sylow subgroup $P$ supplied by step <1>2, and write
$|P|=p$ and $\{p,q\}=\{5,7\}$. Then $|G/P|=3q$. The number of
Sylow $q$-subgroups of $G/P$ divides $3$ and is $1$ modulo $q$.
Since $q\geq5$, this number is $1$. Let $\overline Q$ be that unique,
and therefore normal, subgroup of order $q$.

For the quotient map $\rho:G\to G/P$, set
$N=\rho^{-1}(\overline Q)$. If $g\in G$ and $n\in N$, normality
of $\overline Q$ gives
$\rho(gng^{-1})\in\overline Q$, so $N\lhd G$.
The restriction $N\to\overline Q$ is surjective with kernel $P$;
its fibers are the cosets of $P$. Hence $|N|=pq=35$.
:::

<1>4. Both Sylow subgroups are normal in $G$.

::: proof
Inside $N$, the number of Sylow $5$-subgroups divides $7$ and is
$1$ modulo $5$, so it is $1$. The number of Sylow $7$-subgroups
divides $5$ and is $1$ modulo $7$, so it too is $1$.
Denote these unique subgroups by $P_5$ and $P_7$.

For $g\in G$, normality of $N$ implies $gP_pg^{-1}\subseteq N$
for $p=5,7$. This conjugate still has order $p$, so uniqueness inside
$N$ gives $gP_pg^{-1}=P_p$. Therefore $P_5$ and $P_7$ are normal
in $G$. They are Sylow subgroups of $G$ because $105$ contains each
of $5$ and $7$ to the first power. By conjugacy, they are also the
unique Sylow subgroups of $G$ for their respective primes.
:::
:::
