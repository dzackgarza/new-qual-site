---
schema: qual/card@1
id: P-HULLX
kind: problem
title: Groups of order $p^m n$ are not simple for sufficiently large $m$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $p, n$ be integers such that $p$ is prime and $p$ does not divide $n$.
Find a real number $k = k (p, n)$ such that for every integer $m\geq k$, every group of order $p^m n$ is not simple.
:::

::: {.solution}
Let $G$ have order $p^m n$, with $p\nmid n$. We claim that one may take
\[
k(p,n)=\left\lfloor \log_p((n-1)!)\right\rfloor+1.
\]
(For $n=1$, this gives $k=1$.)

Suppose $m\ge k(p,n)$ and, toward a contradiction, that $G$ is simple. Let $r$ be the number of Sylow $p$-subgroups. If $r=1$, the unique Sylow $p$-subgroup is normal, contradicting simplicity. Thus $r>1$.

Conjugation gives a transitive action of $G$ on its $r$ Sylow $p$-subgroups and hence a homomorphism
\[
G\longrightarrow S_r.
\]
Its kernel is normal. The action is nontrivial because $r>1$, so the kernel is not all of $G$; simplicity therefore forces the kernel to be trivial. Hence
\[
|G|\le r!.
\]
By Sylow's theorem $r\mid n$, so $r\le n$. Consequently
\[
p^m n=|G|\le r!\le n!.
\]
But $m\ge k(p,n)$ implies
\[
p^m>(n-1)!,
\]
and therefore $p^m n>n!$, a contradiction. Thus every group of order $p^m n$ is nonsimple for every integer $m\ge k(p,n)$.
:::
