---
schema: qual/card@1
id: P-FOU3L
kind: problem
title: Invertibility outside $\langle p\rangle$ and purity in $\langle p\rangle$-primary modules over a PID
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Primary Decomposition
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $R$ be a PID and $M$ be an $R\dash$module.
Let $p$ be a prime element of $R$.
The module $M$ is called *$\generators{p}\dash$primary* if for every $m \in M$ there exists $k > 0$ such that $p^k m = 0$.

a. Suppose M is $\generators{p}\dash$primary.
Show that if $m \in M$ and $t \in R, ~t \not\in \generators{p}$, then there exists $a \in R$ such that $atm = m$.

b. A submodule $S$ of $M$ is said to be *pure* if $S \cap r M = rS$ for all $r \in R$.
Show that if $M$ is $\generators{p}\dash$primary, then $S$ is pure if and only if $S \cap p^k M = p^k S$ for all $k \geq 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $m\in M$ and $t\notin(p)$, then there is $a\in R$ with $atm=m$.


::: pf-proof

Choose $k>0$ such that $p^km=0$. In the PID $R$, the prime $p$ does not divide $t$, so the ideals $(t)$ and $(p^k)$ are comaximal. By Bézout's identity, there exist $a,b\in R$ with $at+bp^k=1$. Acting on $m$ yields $atm=m-bp^km=m$.

:::

:::

::: {.pf-step #s1-2}

For every $(p)$-primary $R$-module $L$ and $t\notin(p)$, multiplication by $t$ is surjective on $L$.


::: pf-proof

Given $\ell\in L$, the argument of step [](#s1-1){.pf-ref} applies verbatim to the $(p)$-primary module $L$ and produces an $a\in R$ such that $\ell=t(a\ell)$. Thus $tL=L$.

:::

:::

::: {.pf-step #s1-3}

If $S$ is pure in $M$, then $S\cap p^kM=p^kS$ for all $k\geq0$.


::: pf-proof

The defining identity of purity holds for every $r\in R$. In particular, it holds with $r=p^k$ for every $k\geq0$.

:::

:::

::: {.pf-step #s1-4}

If $S\cap p^kM=p^kS$ for all $k\geq0$, then $S$ is pure in $M$.


::: pf-proof

Fix $r\in R$. If $r=0$, the required equality $S\cap rM=rS$ is immediate. Otherwise, unique factorization in the PID gives $r=up^kt$ for a unit $u\in R^\times$, an integer $k\geq0$, and $t\notin(p)$. The submodule $S$ of the $(p)$-primary module $M$ is itself $(p)$-primary. By step [](#s1-2){.pf-ref} applied to $M$ and to $S$, the equalities $tM=M$ and $tS=S$ hold. Multiplication by a unit also preserves both modules, so $rM=p^kM$ and $rS=p^kS$. The hypothesis therefore gives
$$
S\cap rM=S\cap p^kM=p^kS=rS.
$$
Since $r$ was arbitrary, $S$ is pure.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} prove the two implications of part (b).

:::

:::

:::
