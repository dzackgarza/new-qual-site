---
schema: qual/card@1
id: E-SMI-8000E-SY5
kind: problem
title: Solvability of groups of order pq and p^2 q
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Smith 8000e Sylow problem 5 and the packet's immediately preceding definition of solvability."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Handled order pq by the normal Sylow subgroup for the larger prime; handled order p^2q by Sylow counts, isolating the exceptional order-12 case and proving its Sylow 2-subgroup unique by element counting."
---

::: {.exercise}
If $p$, $q$ are distinct primes, prove:

(i) every group of order $pq$ is solvable;

(ii) every group of order $p^2 q$ is solvable.

[A group $G$ is called "solvable" if there exists a sequence of subgroups $G = H_1, \ldots, H_n = \ts{e}$ such that each $H_{i+1}$ is a normal subgroup of $H_i$, and each quotient $H_i / H_{i+1}$ is abelian.]
:::

::: {.solution}
<1>1. Every group of order $pq$ is solvable.
::: {.proof}
Let $p$ and $q$ be distinct primes, and relabel them if necessary so that
$$
p<q.
$$
Let $n_q$ be the number of Sylow $q$-subgroups. Sylow's theorem gives
$$
n_q\mid p,
\qquad
n_q\equiv1\pmod q.
$$
Thus $n_q$ is either $1$ or $p$. Since $1<p<q$, the value $p$ cannot be
congruent to $1$ modulo $q$. Hence
$$
n_q=1.
$$
So the Sylow $q$-subgroup $Q$ is normal. Because $|Q|=q$, it is cyclic, and
the quotient $G/Q$ has order $p$, hence is cyclic. Therefore
$$
G\trianglerighteq Q\trianglerighteq1
$$
is an abelian normal tower, and $G$ is solvable.
:::

<1>2. If $|G|=p^2q$ and $q<p$, then $G$ is solvable.
::: {.proof}
Let $P$ be a Sylow $p$-subgroup. Its number $n_p$ satisfies
$$
n_p\mid q,
\qquad
n_p\equiv1\pmod p.
$$
Thus $n_p$ is $1$ or $q$. Since $q<p$, the value $q$ cannot be congruent to
$1$ modulo $p$. Hence $n_p=1$, so
$$
P\trianglelefteq G.
$$
Every group of order $p^2$ is abelian, so $P$ is abelian, and $G/P$ has
prime order $q$, hence is cyclic. Therefore
$$
G\trianglerighteq P\trianglerighteq1
$$
is an abelian normal tower.
:::

<1>3. If $|G|=p^2q$ and $p<q$, then either the Sylow $q$-subgroup is normal or $(p,q)=(2,3)$.
::: {.proof}
Let $n_q$ denote the number of Sylow $q$-subgroups. Then
$$
n_q\mid p^2,
\qquad
n_q\equiv1\pmod q.
$$
Hence
$$
n_q\in\{1,p,p^2\}.
$$
The value $p$ is impossible because $1<p<q$. If $n_q\ne1$, then
$n_q=p^2$, so
$$
p^2\equiv1\pmod q.
$$
Thus
$$
q\mid(p^2-1)=(p-1)(p+1).
$$
Since $q>p$, the prime $q$ cannot divide $p-1$; hence it divides $p+1$.
But
$$
p<q\le p+1,
$$
so $q=p+1$. Two consecutive integers greater than $2$ cannot both be prime,
therefore
$$
\boxed{p=2,\qquad q=3.}
$$
Outside this exceptional case, $n_q=1$, so the Sylow $q$-subgroup is normal
and the same tower argument as in step <1>1 proves solvability.
:::

<1>4. Every group of order $12$ is solvable.
::: {.proof}
Let $|G|=12$. If the Sylow $3$-subgroup is normal, then it is cyclic of order
$3$, and the quotient has order $4$, hence is abelian; so $G$ is solvable.

It remains to treat the case of four Sylow $3$-subgroups. Distinct subgroups
of order $3$ intersect only in the identity, so these four subgroups contain
$$
4(3-1)=8
$$
distinct nonidentity elements, all of order $3$.

Thus exactly three nonidentity elements of $G$ remain. Any Sylow $2$-subgroup
$P$ has order $4$ and hence has exactly three nonidentity elements. None of
them can have order $3$, so all three lie among those remaining elements.
Consequently every Sylow $2$-subgroup has the same underlying set
$$
\{1\}\cup\{\text{the three remaining elements}\}.
$$
Hence the Sylow $2$-subgroup is unique and normal.

Every group of order $4$ is abelian, and the quotient by this normal subgroup
has order $3$, hence is cyclic. Therefore
$$
G\trianglerighteq P\trianglerighteq1
$$
is an abelian normal tower. So every group of order $12$ is solvable.
:::

Combining the cases proves
$$
\boxed{\text{every group of order }pq\text{ or }p^2q\text{ is solvable}.}
$$
:::
