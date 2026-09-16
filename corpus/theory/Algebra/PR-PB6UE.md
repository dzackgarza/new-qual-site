---
schema: qual/card@1
id: PR-PB6UE
kind: proposition
title: A monic integer polynomial irreducible modulo a prime is irreducible over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Finite Fields
  - Polynomials
relations: []
review: draft
---

::: {.proposition}
Let $f\in \ZZ[x]$ be monic.
If there exists a prime $p$ such that the reduction $\bar f\in\FF_p[x]$ is [[D-BVMTZ|irreducible]], then $f$ is irreducible in $\QQ[x]$.
:::

::: {.proof}
Suppose $f=gh$ with $g,h\in\QQ[x]$ of degree at least $1$.
By Gauss's lemma we may take $g,h$ monic in $\ZZ[x]$.
Reducing modulo $p$ gives $\bar f=\bar g\bar h$, and since $g$ and $h$ are monic, $\deg\bar g=\deg g\geq1$ and $\deg\bar h=\deg h\geq1$.
This contradicts the irreducibility of $\bar f$.
:::

::: {.example}
The converse fails: $x^4+1$ is irreducible in $\QQ[x]$ but reducible modulo every prime $p$.
Modulo $2$, $x^4+1=(x+1)^4$.
For $p$ odd, at least one of $-1$, $2$, $-2$ is a square modulo $p$, since the product of two nonsquares is a square.
If $i^2=-1$ then $x^4+1=(x^2-i)(x^2+i)$; if $c^2=2$ then $x^4+1=(x^2+cx+1)(x^2-cx+1)$; if $c^2=-2$ then $x^4+1=(x^2+cx-1)(x^2-cx-1)$.
For a monic irreducible $f\in\ZZ[x]$, the Chebotarev density theorem shows that $\bar f$ is reducible for every prime $p$ exactly when the Galois group of $f$ over $\QQ$ contains no $(\deg f)$-cycle; the Galois group of $x^4+1$ over $\QQ$ is $(\ZZ/2\ZZ)^2$.
:::
