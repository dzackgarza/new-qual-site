---
schema: qual/card@1
id: P-CTBJD
kind: problem
title: Groups of order $pqr$ are not simple; simplicity of groups of order $12p$ for
  $p=5,7,11$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
- Let $p<q<r$ be prime integers.
  Show that a group of order $pqr$ cannot be simple.

- Consider groups of orders $2^2\cdot 3\cdot p$ where $p$ has the values 5, 7, and 11. For each of those values of $p$, either display a simple group of order $2^2\cdot 3\cdot p$, or show that there cannot be a simple group of that order.
:::

::: {.solution}
<1>1. Let $G$ have order $pqr$ with $p<q<r$ prime. Then $G$ is not simple.
::: {.proof}
Suppose for contradiction that $G$ is simple. Let $n_r$ be the number of Sylow $r$-subgroups. The Sylow theorems give
\[
n_r\equiv1\pmod r,
\qquad
n_r\mid pq.
\]
Since $G$ is simple, $n_r\ne1$. The only divisors of $pq$ are $1,p,q,pq$, and both $p$ and $q$ are strictly less than $r$, so neither can be congruent to $1$ modulo $r$. Hence
\[
n_r=pq.
\]
Distinct Sylow $r$-subgroups intersect trivially, so they contribute
\[
pq(r-1)
\]
nonidentity elements of order $r$.

Now let $n_q$ be the number of Sylow $q$-subgroups. Again simplicity gives $n_q>1$, while
\[
n_q\equiv1\pmod q,
\qquad
n_q\mid pr.
\]
Since $p<q$, we cannot have $n_q=p$. Therefore $n_q\ge r$, because the remaining nontrivial divisors of $pr$ are $r$ and $pr$. Distinct Sylow $q$-subgroups intersect trivially, so there are at least
\[
r(q-1)
\]
nonidentity elements of order $q$.

The sets of nonidentity elements of order $r$ and of order $q$ are disjoint. Hence $G$ would contain at least
\[
pq(r-1)+r(q-1)
\]
nonidentity elements. But
\[
pq(r-1)+r(q-1)-(pqr-1)
=r(q-1)-pq+1.
\]
Since $q>p$, we have $q-1\ge p$, and since $r>q$,
\[
r(q-1)\ge rp>pq.
\]
Thus
\[
pq(r-1)+r(q-1)>pqr-1,
\]
more nonidentity elements than $G$ possesses. This contradiction proves that $G$ is not simple.
:::

<1>2. There is a simple group of order $2^2\cdot3\cdot5=60$.
::: {.proof}
The alternating group $A_5$ has order
\[
|A_5|=\frac{5!}{2}=60,
\]
and $A_5$ is simple.
:::

<1>3. No group of order $2^2\cdot3\cdot7=84$ is simple.
::: {.proof}
Let $G$ have order $84$. If $n_7$ denotes the number of Sylow $7$-subgroups, then
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid12.
\]
Among the divisors of $12$, only $1$ is congruent to $1$ modulo $7$. Hence
\[
n_7=1.
\]
Thus the Sylow $7$-subgroup is normal, so $G$ is not simple.
:::

<1>4. No group of order $2^2\cdot3\cdot11=132$ is simple.
::: {.proof}
Suppose for contradiction that $G$ is simple of order $132$. For the Sylow $11$-subgroups,
\[
n_{11}\equiv1\pmod{11},
\qquad
n_{11}\mid12.
\]
Thus $n_{11}=1$ or $12$. Simplicity excludes $1$, so
\[
n_{11}=12.
\]
These Sylow subgroups contribute
\[
12(11-1)=120
\]
nonidentity elements of order $11$.

Now
\[
n_3\equiv1\pmod3,
\qquad
n_3\mid44.
\]
The possibilities are $n_3=1,4,22$. Simplicity excludes $1$. If $n_3=22$, the Sylow $3$-subgroups would contribute
\[
22(3-1)=44
\]
nonidentity elements of order $3$, disjoint from the $120$ nonidentity elements of order $11$. That would give at least $164$ nonidentity elements in a group with only $131$, impossible. Hence
\[
n_3=4.
\]

Conjugation gives an action of $G$ on the set of its four Sylow $3$-subgroups, hence a homomorphism
\[
\varphi:G\longrightarrow S_4.
\]
The action is transitive by Sylow conjugacy and has more than one point, so $\varphi$ is nontrivial. Its kernel is normal in $G$. Since $G$ is assumed simple, a nontrivial homomorphism must have trivial kernel, so $\varphi$ would be injective. Then $|G|$ would divide $|S_4|=24$, contradicting $|G|=132$. Therefore no group of order $132$ is simple.
:::
:::
