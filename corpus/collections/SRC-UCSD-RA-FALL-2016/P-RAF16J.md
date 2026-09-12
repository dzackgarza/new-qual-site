---
schema: qual/card@1
id: P-RAF16J
kind: problem
title: "Support of a Radon measure"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 10 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\mu$ be a Radon measure on a locally compact Hausdorff space $X$.

(1) Let $V$ be the union of all open subsets $U \subseteq X$ such that $\mu(U) = 0$.
Prove that $V$ is open and $\mu(V) = 0$.
The complement of $V$ is called the support of $\mu$ and is denoted by $\operatorname{supp}(\mu)$.

(2) Assume in addition that $X$ is compact and $\mu(X) = 1$.
Denote $K = \operatorname{supp}(\mu)$.
Prove that $K$ is compact, $\mu(K) = 1$, and $\mu(H) < 1$ for every proper compact subset $H$ of $K$.
:::

::: solution
<1>1. Show that $V$ is open and null.
::: proof
By definition, $V$ is a union of open sets, so $V$ is open.

Suppose for contradiction that $\mu(V)>0$. Since $\mu$ is Radon, it is inner regular on the open set $V$, so there exists a compact set
\[
C\subseteq V
\]
with
\[
\mu(C)>0.
\]
For every $x\in C$, because $x\in V$, there is an open set $U_x$ such that
\[
x\in U_x,
\qquad
\mu(U_x)=0.
\]
The family $(U_x)_{x\in C}$ covers the compact set $C$, so finitely many of them cover $C$:
\[
C\subseteq U_{x_1}\cup\cdots\cup U_{x_N}.
\]
Hence
\[
\mu(C)
\le\sum_{j=1}^N\mu(U_{x_j})=0,
\]
a contradiction. Therefore
\[
\boxed{\mu(V)=0.}
\]
:::

<1>2. Prove the basic properties of the support in the compact probability case.
::: proof
Now assume $X$ is compact and $\mu(X)=1$, and put
\[
K:=\operatorname{supp}(\mu)=X\setminus V.
\]
Since $V$ is open, $K$ is closed in the compact space $X$, hence compact. Also
\[
\mu(K)=\mu(X)-\mu(V)=1.
\]
:::

<1>3. Show that no proper compact subset of $K$ has full measure.
::: proof
Let $H\subsetneq K$ be compact. Choose
\[
x\in K\setminus H.
\]
Because $X$ is Hausdorff and $H$ is compact, there exists an open neighborhood $U$ of $x$ such that
\[
U\cap H=\varnothing.
\]

Since $x\in K=X\setminus V$, no open neighborhood of $x$ can have measure zero. Hence
\[
\mu(U)>0.
\]
Because $H$ and $U$ are disjoint,
\[
\mu(H)+\mu(U)\le\mu(X)=1.
\]
Therefore
\[
\boxed{\mu(H)\le1-\mu(U)<1.}
\]
Thus every proper compact subset of the support has strictly smaller measure.
:::
:::
