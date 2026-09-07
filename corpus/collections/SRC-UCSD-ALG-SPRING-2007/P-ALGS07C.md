---
schema: qual/card@1
id: P-ALGS07C
kind: problem
title: "All R[x]-module structures on a 3-dimensional real vector space"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared the statement with Problem 3 on page 5 of the official Spring 2007 UCSD algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Re-derived the classification from Cayley-Hamilton and the elementary-divisor theorem over R[x], including all degree-three partitions and the irreducible-quadratic case.
---

::: problem
Describe, up to isomorphism, all the $\mathbb{R}[x]$-module structures one might put on a 3-dimensional real vector space (extending the fixed $\mathbb{R}$-action).
:::

::: {.solution}
<1>1. An $\mathbb{R}[x]$-module structure on $V$ extending its given $\mathbb{R}$-vector-space structure is equivalent to a linear operator $T\in\operatorname{End}_{\mathbb{R}}(V)$.
::: {.proof}
Given such a module structure, define $T(v)=x\cdot v$. Since the $\mathbb{R}$-action is fixed, $T$ is $\mathbb{R}$-linear, and then
\[
p(x)\cdot v=p(T)v
\]
for every $p\in\mathbb{R}[x]$.
Conversely, any $T\in\operatorname{End}_{\mathbb{R}}(V)$ defines an $\mathbb{R}[x]$-action by this formula.
An isomorphism $V_T\to V_{T'}$ is exactly an invertible $\mathbb{R}$-linear map $P$ satisfying $PT=T'P$, so isomorphism classes are similarity classes of operators on $\mathbb{R}^3$.
:::

<1>2. As an $\mathbb{R}[x]$-module, $V$ is finitely generated torsion of total elementary-divisor degree $3$.
::: {.proof}
A real basis of $V$ also generates $V$ as an $\mathbb{R}[x]$-module, so $V$ is finitely generated.
Let $\chi_T(x)$ be the characteristic polynomial of $T$.
By Cayley--Hamilton,
\[
\chi_T(T)=0,
\]
so $\chi_T(x)$ annihilates all of $V$; hence $V$ is torsion.
Since $\mathbb{R}[x]$ is a PID, the elementary-divisor theorem gives
\[
V\cong\bigoplus_j \mathbb{R}[x]/(p_j^{e_j}),
\]
with $p_j$ monic irreducible.
As real vector spaces,
\[
\dim_{\mathbb{R}}\mathbb{R}[x]/(p_j^{e_j})=e_j\deg p_j,
\]
so
\[
\sum_j e_j\deg p_j=3.
\]
:::

<1>3. The only monic irreducibles over $\mathbb{R}$ have degree $1$ or $2$.
::: {.proof}
Every real polynomial of odd degree has a real root. Thus an irreducible real polynomial has degree at most $2$.
The monic irreducibles are the linear factors $x-\lambda$ and the quadratics
\[
x^2+ax+b,
\qquad a^2-4b<0.
\]
:::

<1>4. Therefore every $3$-dimensional $\mathbb{R}[x]$-module is isomorphic to exactly one module from the following four families, modulo the evident permutation of direct-sum factors.

<2>1. Three linear elementary divisors:
\[
\mathbb{R}[x]/(x-\lambda_1)
\oplus
\mathbb{R}[x]/(x-\lambda_2)
\oplus
\mathbb{R}[x]/(x-\lambda_3),
\]
with $\lambda_i\in\mathbb{R}$.

<2>2. One squared linear divisor and one linear divisor:
\[
\mathbb{R}[x]/((x-\lambda)^2)
\oplus
\mathbb{R}[x]/(x-\mu),
\]
with $\lambda,\mu\in\mathbb{R}$.

<2>3. One cubed linear divisor:
\[
\mathbb{R}[x]/((x-\lambda)^3),
\]
with $\lambda\in\mathbb{R}$.

<2>4. One irreducible quadratic divisor and one linear divisor:
\[
\mathbb{R}[x]/(q(x))
\oplus
\mathbb{R}[x]/(x-\lambda),
\]
where $q(x)=x^2+ax+b$ satisfies $a^2-4b<0$ and $\lambda\in\mathbb{R}$.

::: {.proof}
The degree equation in <1>2 has only the partitions
\[
3=1+1+1=2+1=3.
\]
If all irreducibles involved are linear, these give respectively <2>1, <2>2, and <2>3; in the degree-$2$ summand of <2>2 the elementary divisor must be $(x-\lambda)^2$.
If an irreducible quadratic occurs, it contributes degree $2$, leaving exactly one linear degree-$1$ summand, which gives <2>4.
There is no other possibility because irreducibles over $\mathbb{R}$ have degree only $1$ or $2$.
The elementary-divisor theorem also gives uniqueness of the multiset of elementary divisors, hence these families classify the module structures up to isomorphism.
:::

<1>5. In operator language, the four families are respectively: three $1\times1$ real Jordan blocks; a $2\times2$ real Jordan block plus a $1\times1$ block; one $3\times3$ real Jordan block; or one real $2\times2$ block for a nonreal conjugate pair plus one real $1\times1$ block.
::: {.proof}
These are precisely the rational/Jordan forms associated to the elementary divisors listed in <1>4.
:::
:::
