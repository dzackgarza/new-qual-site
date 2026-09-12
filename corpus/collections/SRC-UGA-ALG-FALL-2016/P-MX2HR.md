---
schema: qual/card@1
id: P-MX2HR
kind: problem
title: Solvable groups, and every group of order $36$ is solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Sylow Theory
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-11
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-11
---

::: problem
a. Define what it means for a group $G$ to be *solvable*.

a. Show that every group $G$ of order 36 is solvable.

> Hint: you can use that $S_4$ is solvable.
:::

::: {.solution}
<1>1. A group $G$ is **solvable** if its derived series
\[
G^{(0)}=G,
\qquad
G^{(i+1)}=[G^{(i)},G^{(i)}]
\]
reaches the trivial subgroup after finitely many steps.
::: {.proof}
Equivalently, $G$ is solvable if there exists $r\ge0$ such that
\[
G^{(r)}=1.
\]
This is the definition used below.
:::

<1>2. If
\[
1\longrightarrow N\longrightarrow G\longrightarrow Q\longrightarrow1
\]
is exact and both $N$ and $Q$ are solvable, then $G$ is solvable.
::: {.proof}
Suppose $Q^{(r)}=1$. The image of $G^{(r)}$ in $Q$ lies in $Q^{(r)}$, so
\[
G^{(r)}\subseteq N.
\]
If $N^{(s)}=1$, then
\[
G^{(r+s)}
=(G^{(r)})^{(s)}
\subseteq N^{(s)}
=1.
\]
Thus $G$ is solvable.
:::

Now let $|G|=36=2^2\cdot3^2$.

<1>3. The number $n_3$ of Sylow $3$-subgroups is either $1$ or $4$.
::: {.proof}
Sylow's theorems give
\[
n_3\equiv1\pmod3
\qquad\text{and}\qquad
n_3\mid4.
\]
The divisors of $4$ are $1,2,4$, and those congruent to $1$ modulo $3$ are $1$ and $4$.
:::

<1>4. If $n_3=1$, then $G$ is solvable.
::: {.proof}
Let $P$ be the unique Sylow $3$-subgroup. Then $P\trianglelefteq G$ and
\[
|P|=9.
\]
Every group of order $p^2$ is abelian, so $P$ is abelian and therefore solvable.
The quotient has order
\[
|G/P|=4,
\]
and every group of order $4$ is abelian, hence solvable.
By <1>2, $G$ is solvable.
:::

<1>5. Suppose $n_3=4$. Conjugation on the set of the four Sylow $3$-subgroups gives a homomorphism
\[
\varphi:G\longrightarrow S_4.
\]
Its image has order $4$ or $12$.
::: {.proof}
The conjugation action of $G$ on its Sylow $3$-subgroups is transitive, because all Sylow subgroups are conjugate. Hence $\operatorname{im}\varphi$ acts transitively on a set of four points, so by orbit-stabilizer its order is divisible by $4$.

Also
\[
|\operatorname{im}\varphi|\mid |G|=36
\]
by the first isomorphism theorem, and
\[
|\operatorname{im}\varphi|\mid |S_4|=24.
\]
Thus its order divides
\[
\gcd(36,24)=12.
\]
The positive divisors of $12$ divisible by $4$ are $4$ and $12$.
:::

<1>6. In the case $n_3=4$, the kernel of $\varphi$ is abelian and the image of $\varphi$ is solvable.
::: {.proof}
By <1>5,
\[
|\ker\varphi|
=\frac{|G|}{|\operatorname{im}\varphi|}
\]
is either
\[
\frac{36}{4}=9
\]
or
\[
\frac{36}{12}=3.
\]
Every group of order $3$ or $9$ is abelian, so $\ker\varphi$ is solvable.

The image $\operatorname{im}\varphi$ is a subgroup of $S_4$. By the allowed fact that $S_4$ is solvable, every subgroup of $S_4$ is solvable, because the derived series of a subgroup is contained term-by-term in the derived series of the ambient group.
:::

<1>7. Therefore every group of order $36$ is solvable.
::: {.proof}
If $n_3=1$, this is <1>4.
If $n_3=4$, then
\[
1\longrightarrow\ker\varphi
\longrightarrow G
\longrightarrow\operatorname{im}\varphi
\longrightarrow1
\]
is exact, with solvable kernel and solvable quotient by <1>6. Hence $G$ is solvable by <1>2.
:::
:::
