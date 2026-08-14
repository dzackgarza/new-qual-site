---
schema: qual/card@1
id: P-63TON
kind: problem
title: "Let $R$ be an integral domain with quotient field $F$."
classification:
  areas:
  - algebra
  topics:
  - factorization
  - polynomials
  - integral-domains
relations: []
review: draft
---
a.
Let $R$ be an integral domain with quotient field $F$.
Suppose that $p(x), a(x), b(x)$ are monic polynomials in $F[x]$ with $p(x) = a(x) b(x)$ and with $p(x) \in R[x]$, $a(x)$ not in $R[x]$, and both $a(x), b(x)$ not constant.

  Prove that $R$ is not a UFD.

  > (You may assume Gauss' lemma)

b.
Prove that $\ZZ[2\sqrt{2}]$ is not a UFD.

  > Hint: let $p(x) = x^2-2$.

:::{.concept}
\envlist

- Gauss' lemma: for $R$ a UFD with fraction field $F$, if $f\in R[x]$ is reducible in $F[x]$ with $f=pq$ then there are $r,s\in F\units$ with $rs=1$ such that $rp, sq\in R[x]$, so $f = (rp)(sq)$ reduces in $R[x]$.
- Corollary: $R$ is a UFD iff $R[x]$ is a UFD.
:::

:::{.solution}
\envlist

:::{.proof title="of 1"}
\envlist

- The important assumption is $a(x)\not\in R[x]$, we'll assume $R$ is a UFD and try to contradict this.
- Write $f(x) = a(x)b(x)\in F[x]$, then if $R$ is a UFD we have $r,s\in F$ such that $f(x) = ra(x) sb(x) \in R[x]$.
- Since $a(x), b(x)$ are monic and $f=ab$, $f$ is monic, and by the factorization in $R[x]$ we have $rs=1$.
  Moreover $ra(x)\in R[x]$ with $a$ monic makes $r$ the leading coefficient of $ra$, so $r\in R$; likewise $s\in R$.
  With $rs=1$ this puts $r,s\in R\units$.
- Then using that $ra(x)\in R[x]$, we have $r\inv ra(x) = a(x)\in R[x]$. $\contradiction$

:::


:::{.proof title="of b"}
\envlist

- Set $R = \ZZ[2\sqrt 2], F = \QQ[2\sqrt 2]$.
- Let $p(x) \da x^2-2 \in R[x]$ which splits as $p(x) = (x+ \sqrt{2} )(x - \sqrt{2} ) \da a(x) b(x) \in F[x]$.
- Note neither $a(x), b(x)$ are in $R[x]$.
  - Explicitly, $R = \ts{ c + 2d\sqrt 2 \suchthat c,d\in \ZZ }$, so every monic linear $p\in R[x]$ is of the form $x + (c + 2d\sqrt 2)$.
    Matching $\pm\sqrt 2 = c + 2d\sqrt 2$ forces $c=0$ and $2d = \pm 1$, which has no solution in $\ZZ$.
- So we have $p(x) \in R[x]$ splitting as $p=ab$ in $F[x]$ with $a\not \in R[x]$, so part (a) applies.

:::

:::

