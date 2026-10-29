---
schema: qual/card@1
id: T-JEZZY
kind: theorem
title: Gauss's lemma
slogan: 'For a primitive polynomial over a UFD, irreducibility is unchanged on passing to the fraction field.'
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
  - Irreducibility Criteria
prompts:
- State Gauss' lemma.
relations: []
review: draft
---

::: {.theorem}
Let $R$ be a [[D-INULL|unique factorization domain]] with [[D-OXIVT|field of fractions]] $F$, and let $p\in R[x]$ be [[D-4VC6X|primitive]].
Then $p$ is irreducible in $R[x]$ if and only if $p$ is [[D-BVMTZ|irreducible]] in $F[x]$.

More precisely, if $p=AB$ with $A,B\in F[x]$ nonconstant, then there exist $r,s\in F^\times$ with $rs=1$ such that $rA,sB\in R[x]$, so $p=(rA)(sB)$ is a factorization of $p$ in $R[x]$ into nonconstant polynomials.
:::

::: {.example}
Every monic polynomial in $R[x]$ is primitive, since its leading coefficient $1$ is a unit; so a monic $p\in\ZZ[x]$ is irreducible in $\ZZ[x]$ if and only if it is irreducible in $\QQ[x]$.
:::

::: {.remark title="Variations"}
The primitivity hypothesis is needed only for the irreducibility equivalence.
For an arbitrary $p\in R[x]$, a factorization $p=AB$ with $A,B\in F[x]$ nonconstant still descends: there are $A',B'\in R[x]$ with $\deg A'=\deg A$, $\deg B'=\deg B$, and $p=A'B'$.
In particular, if $p$ is [[D-BVMTZ|reducible]] in $F[x]$, then $p$ is reducible in $R[x]$.
To see this, write $p=cp_0$ with $c\in R$ a greatest common divisor of the coefficients and $p_0$ primitive; here $p\neq0$ because $A,B\neq0$.
Apply the precise form above to $p_0=(c^{-1}A)B$ to get $p_0=A_0B_0$ with $A_0,B_0\in R[x]$ of the same degrees, and put $A'=cA_0$, $B'=B_0$.
:::

::: {.remark}
If $R$ is a unique factorization domain, then so is $R[x]$; the proof uses Gauss's lemma to reduce factorization in $R[x]$ to factorization in $R$ and in the principal ideal domain $F[x]$.
By induction, $R[x_1,\ldots,x_n]$ is a unique factorization domain, and so is the polynomial ring over $R$ in any set of variables, since each polynomial involves finitely many variables.
:::
