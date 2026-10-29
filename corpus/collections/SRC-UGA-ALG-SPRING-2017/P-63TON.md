---
schema: qual/card@1
id: P-63TON
kind: problem
title: A monic in $R[x]$ factoring into nonconstant monics in $F[x]$ with a factor outside $R[x]$ implies $R$ is not a UFD; $\ZZ[2\sqrt{2}]$ is not a UFD
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
  - Integral Domains
relations: []
review: draft
---
::: {.problem}
(a) Let $R$ be an integral domain with fraction field $F$. Suppose that $p(x), a(x), b(x) \in F[x]$ are non-constant monic polynomials such that $p(x) = a(x) b(x)$ with $p(x) \in R[x]$ and $a(x) \notin R[x]$. Prove that $R$ is not a unique factorization domain (UFD). (You may assume Gauss's Lemma.)

(b) Prove that $\ZZ[2\sqrt{2}]$ is not a UFD.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $R$ is a UFD and a monic polynomial $p\in R[x]$ factors as $p=ab$ with monic $a,b\in F[x]$, then $a,b\in R[x]$.

::: pf-proof

By Gauss's lemma, there are nonzero scalars $c,d\in F$ such that $ca,db\in R[x]$ and $cd=1$. Because $a,b$ are monic, the leading coefficients of $ca$ and $db$ are $c$ and $d$, respectively; hence $c,d\in R$. The identity $cd=1$ makes both scalars units of $R$. Multiplying by these units' inverses gives $a,b\in R[x]$.

:::

:::

::: {.pf-step #s2}

Under the hypotheses of part (a), $R$ is not a UFD.

::: pf-proof

If $R$ were a UFD, step [](#s1){.pf-ref} applied to the stated monic factorization would give $a\in R[x]$, contradicting the hypothesis $a\notin R[x]$.

:::

:::

::: {.pf-step #s3}

The ring $\ZZ[2\sqrt2]$ is not a UFD.

::: pf-proof

Put $R=\ZZ[2\sqrt2]=\{u+2v\sqrt2:u,v\in\ZZ\}$ and $F=\QQ(\sqrt2)$, its fraction field. In $R[x]$ the monic polynomial $p=x^2-2$ satisfies
$$
p=(x-\sqrt2)(x+\sqrt2)
$$
in $F[x]$. Both factors are nonconstant and monic. The element $\sqrt2$ is not in $R$: an equality $\sqrt2=u+2v\sqrt2$ with integers $u,v$ would imply $u=0$ and $2v=1$, which is impossible. Thus $x-\sqrt2\notin R[x]$. Step [](#s2){.pf-ref} applies and shows that $R$ is not a UFD.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part (a), and step [](#s3){.pf-ref} proves part (b).

:::

:::

:::
