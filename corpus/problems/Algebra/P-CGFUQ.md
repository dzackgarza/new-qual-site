---
schema: qual/card@1
id: P-CGFUQ
kind: problem
title: Definitions of UFD and PID, and a UFD that is not a PID
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Principal Ideal Domains
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $R$ be a commutative ring.

1. Say what it means for $R$ to be a unique factorization domain (UFD).

2. Say what it means for $R$ to be a principal ideal domain (PID)

3. Give an example of a UFD that is not a PID. Prove that it is not a PID.
:::

::: {.solution}
(1) A commutative ring $R$ with $1\neq0$ is a \dfn{unique factorization domain} if $R$ is an integral domain, every nonzero nonunit $r\in R$ is a finite product $r=p_1\cdots p_k$ of irreducible elements, and whenever $r=q_1\cdots q_m$ is another such product, $m=k$ and there is $\sigma\in S_k$ with $q_i$ associate to $p_{\sigma(i)}$ for every $i$.

(2) A commutative ring $R$ with $1\neq0$ is a \dfn{principal ideal domain} if $R$ is an integral domain and every ideal of $R$ has the form $aR$ for some $a\in R$.

(3) The ring $\ZZ[x]$ is a UFD that is not a PID.

<1>1. $\ZZ[x]$ is a UFD.

::: {.proof}
$\ZZ$ is a UFD, and by Gauss's lemma a polynomial ring over a UFD is a UFD.
:::

<1>2. The ideal $I=(2,x)=\{h\in\ZZ[x]:h(0)\in2\ZZ\}$ is not principal.

::: {.proof}
Every $2f+xg$ has constant term $2f(0)$, and conversely $h=h(0)+x\,\frac{h-h(0)}{x}$ with $h(0)$ even lies in $I$.
Suppose $I=(d)$. Since $2\in(d)$, $d$ divides $2$, so $\deg d=0$ and $d=c\in\{\pm1,\pm2\}$.
If $c=\pm1$, then $1\in I$, but $1$ has odd constant term.
If $c=\pm2$, then $x\in(2)$, but the coefficient $1$ of $x$ is odd.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, $\ZZ[x]$ is a UFD with a non-principal ideal.
:::
:::
