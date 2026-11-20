---
schema: qual/card@1
id: P-ALGS07C
kind: problem
title: "All $\\RR[x]$-module structures on a 3-dimensional real vector space"
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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Three of the card's nine steps --- the three families 4.1, 4.2 and 4.3 --- listed their
    elementary divisors with no proof body; each now carries a `pf-proof` giving the real
    dimension of each summand and naming the elementary divisors it produces. No claim was
    changed; step 4.4, which carries the argument that the list is exhaustive, keeps its own
    proof. Checked: that each of the four families has real dimension $3$; that the
    elementary-divisor multisets of the four families are pairwise distinct, so no two of them
    are isomorphic; and that $\RR[x]/(x-\lambda)$ is one-dimensional over $\RR$. Not checked:
    the printed examination paper, the statement being vouched for by the `source-checked`
    event of 2026-09-07; no published solution was consulted.
---

::: {.problem}
Describe, up to isomorphism, all the $\RR[x]$-module structures one might put on a 3-dimensional real vector space (extending the fixed $\RR$-action).
:::

::: {.solution}

::: pf

::: pf-step

An $\RR[x]$-module structure on $V$ extending its given $\RR$-vector-space structure is equivalent to a linear operator $T\in\operatorname{End}_{\RR}(V)$.

::: pf-proof

Given such a module structure, define $T(v)=x\cdot v$.
Since the $\RR$-action is fixed, $T$ is $\RR$-linear, and then
$$
p(x)\cdot v=p(T)v
$$
for every $p\in\RR[x]$.
Conversely, any $T\in\operatorname{End}_{\RR}(V)$ defines an $\RR[x]$-action by this formula.
An isomorphism $V_T\to V_{T'}$ is exactly an invertible $\RR$-linear map $P$ satisfying $PT=T'P$, so isomorphism classes are similarity classes of operators on $\RR^3$.

:::

:::

::: {.pf-step #s2}

As an $\RR[x]$-module, $V$ is finitely generated torsion of total elementary-divisor degree $3$.

::: pf-proof

A real basis of $V$ also generates $V$ as an $\RR[x]$-module, so $V$ is finitely generated.
Let $\chi_T(x)$ be the characteristic polynomial of $T$.
By Cayley--Hamilton,
$$
\chi_T(T)=0,
$$
so $\chi_T(x)$ annihilates all of $V$; hence $V$ is torsion.
Since $\RR[x]$ is a PID, the elementary-divisor theorem gives
$$
V\cong\bigoplus_j \RR[x]/(p_j^{e_j}),
$$
with $p_j$ monic irreducible.
As real vector spaces,
$$
\dim_{\RR}\RR[x]/(p_j^{e_j})=e_j\deg p_j,
$$
so
$$
\sum_j e_j\deg p_j=3.
$$

:::

:::

::: pf-step

The only monic irreducibles over $\RR$ have degree $1$ or $2$.

::: pf-proof

Every real polynomial of odd degree has a real root.
Thus an irreducible real polynomial has degree at most $2$.
The monic irreducibles are the linear factors $x-\lambda$ and the quadratics
$$
x^2+ax+b,
\qquad a^2-4b<0.
$$

:::

:::

::: {.pf-step #s4}

Therefore every $3$-dimensional $\RR[x]$-module is isomorphic to exactly one module from the following four families, modulo the evident permutation of direct-sum factors.

::: pf-proof

The degree equation of step 2 has the partitions $3=1+1+1=2+1=3$, and step 3 says the irreducibles are linear or quadratic; the four cases are enumerated in steps 4.1--4.4, each of which is a module of real dimension $3$.

::: {.pf-step #s4-1}

Three linear elementary divisors:
$$
\RR[x]/(x-\lambda_1)
\oplus
\RR[x]/(x-\lambda_2)
\oplus
\RR[x]/(x-\lambda_3),
$$
with $\lambda_i\in\RR$.

::: pf-proof

Each $\RR[x]/(x-\lambda_i)$ is a field, hence a one-dimensional real vector space (a basis is the class of $1$), on which $x$ acts as multiplication by $\lambda_i$; the direct sum is therefore a real vector space of dimension $1+1+1=3$. Its elementary divisors are the three monic linear polynomials $x-\lambda_1,x-\lambda_2,x-\lambda_3$, and every module whose elementary divisors are three linear polynomials arises this way.

:::

:::

::: {.pf-step #s4-2}

One squared linear divisor and one linear divisor:
$$
\RR[x]/((x-\lambda)^2)
\oplus
\RR[x]/(x-\mu),
$$
with $\lambda,\mu\in\RR$.

::: pf-proof

The quotient $\RR[x]/((x-\lambda)^2)$ has the real basis the classes of $1$ and $x-\lambda$, so its dimension is $2=2\deg(x-\lambda)$; with the one-dimensional second summand the dimension is $2+1=3$. Its elementary divisors are $(x-\lambda)^2$ and $x-\mu$, both powers of linear polynomials, and every module with that multiset of elementary divisors is this direct sum by the elementary-divisor theorem.

:::

:::

::: {.pf-step #s4-3}

One cubed linear divisor:
$$
\RR[x]/((x-\lambda)^3),
$$
with $\lambda\in\RR$.

::: pf-proof

The quotient $\RR[x]/((x-\lambda)^3)$ has the real basis the classes of $1,x-\lambda,(x-\lambda)^2$, so its dimension is $3=3\deg(x-\lambda)$, and its single elementary divisor is $(x-\lambda)^3$; conversely a module with that elementary divisor is this quotient.

:::

:::

::: {.pf-step #s4-4}

One irreducible quadratic divisor and one linear divisor:
$$
\RR[x]/(q(x))
\oplus
\RR[x]/(x-\lambda),
$$
where $q(x)=x^2+ax+b$ satisfies $a^2-4b<0$ and $\lambda\in\RR$.

::: pf-proof

The degree equation in step [](#s2){.pf-ref} has only the partitions
$$
3=1+1+1=2+1=3.
$$
If all irreducibles involved are linear, these give respectively steps [](#s4-1){.pf-ref}, [](#s4-2){.pf-ref} and [](#s4-3){.pf-ref}; in the degree-$2$ summand of step [](#s4-2){.pf-ref} the elementary divisor must be $(x-\lambda)^2$.
If an irreducible quadratic occurs, it contributes degree $2$, leaving exactly one linear degree-$1$ summand, which gives step [](#s4-4){.pf-ref}. There is no other possibility because irreducibles over $\RR$ have degree only $1$ or $2$.
The elementary-divisor theorem also gives uniqueness of the multiset of elementary divisors, hence these families classify the module structures up to isomorphism.

:::

:::

:::

:::

::: pf-step

In operator language, the four families are respectively: three $1\times1$ real Jordan blocks; a $2\times2$ real Jordan block plus a $1\times1$ block; one $3\times3$ real Jordan block; or one real $2\times2$ block for a nonreal conjugate pair plus one real $1\times1$ block.

::: pf-proof

These are precisely the rational/Jordan forms associated to the elementary divisors listed in step [](#s4){.pf-ref}.

:::

:::

:::
:::