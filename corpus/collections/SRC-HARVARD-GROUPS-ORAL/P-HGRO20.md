---
schema: qual/card@1
id: P-HGRO20
kind: problem
title: A subgroup of least prime index is normal
classification:
  areas: [algebra]
  topics: [Group Actions]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $H\leq G$, where $G$ is finite.
Suppose $[G:H]$ is the smallest prime that divides $|G|$.
Prove that $H$ is normal in $G$.
:::

::: {.solution}
Let $p=[G:H]$, and let $\varphi\colon G\to\operatorname{Sym}(G/H)\cong S_p$ be
the homomorphism given by left multiplication on the cosets of $H$. Put
$K=\ker\varphi$.

<1>1. $K=\bigcap_{g\in G}gHg^{-1}$; in particular $K\trianglelefteq G$ and
$K\le H$.

::: {.proof}
An element $x$ acts trivially on $G/H$ exactly when $xgH=gH$, that is,
$x\in gHg^{-1}$, for every $g\in G$. A kernel is normal, and the term $g=1$
gives $K\le H$.
:::

<1>2. $[G:K]=p$.

::: {.proof}
By the first isomorphism theorem $[G:K]=\abs{\varphi(G)}$, which divides both
$\abs{G}$ and $\abs{S_p}=p!$. Every prime divisor of $[G:K]$ divides $\abs{G}$,
so it is at least $p$, and divides $p!$, so it is at most $p$; hence $[G:K]$ is
a power of $p$. Since $p^2\nmid p!$, $[G:K]\in\{1,p\}$. Finally
$[G:K]=[G:H][H:K]\ge p$.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>2, $[G:K]=p=[G:H]$, so $[H:K]=1$ and $H=K$, which is normal by step
<1>1.
:::
:::
