---
schema: qual/card@1
id: P-RASP21F
kind: problem
title: "Radon measure extension from a closed subset"
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
  date: 2026-09-09
  note: Checked against Problem 6 of the official UCSD Spring 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $X$ be an LCH space, and $Y$ a closed subset of $X$.
Show that if $\mu$ is a Radon measure on $Y$, then $\nu(E) := \mu(E \cap Y)$ defines a Radon measure $\nu$ on $X$.
Also demonstrate that $Y$ being closed is needed here, by giving an example where $Y$ is not closed and the corresponding $\nu$ is not Radon.
:::


::: solution
<1>1. Show that $\nu$ is a Borel measure on $X$.
::: proof
Because $Y$ is closed, it is Borel in $X$. If $E\subseteq X$ is Borel, then $E\cap Y$ is Borel in the subspace $Y$, so
\[
\nu(E):=\mu(E\cap Y)
\]
is well defined. Countable additivity follows immediately from countable additivity of $\mu$ and the identity
\[
\left(\bigcup_jE_j\right)\cap Y
=\bigcup_j(E_j\cap Y)
\]
for disjoint Borel sets $E_j$.
:::

<1>2. Prove finiteness on compact sets.
::: proof
Let $K\subseteq X$ be compact. Since $Y$ is closed in $X$, the intersection $K\cap Y$ is compact in $X$, hence compact in the subspace $Y$. Because $\mu$ is Radon on $Y$,
\[
\nu(K)=\mu(K\cap Y)<\infty.
\]
Thus $\nu$ is finite on compact subsets of $X$.
:::

<1>3. Prove inner regularity.
::: proof
Let $E\subseteq X$ be Borel. Since $\mu$ is Radon on $Y$,
\[
\mu(E\cap Y)
=\sup\{\mu(L):L\subseteq E\cap Y,\ L\text{ compact in }Y\}.
\]
The inclusion $Y\hookrightarrow X$ is continuous, so every compact subset $L$ of $Y$ is also compact in $X$. For such $L$,
\[
\nu(L)=\mu(L).
\]
Therefore
\[
\nu(E)
=\sup\{\nu(L):L\subseteq E,\ L\text{ compact in }X\}.
\]
Hence $\nu$ is inner regular. Together with Step 2, this shows that $\nu$ is a Radon measure on the LCH space $X$.
:::

<1>4. Show that closedness of $Y$ is necessary.
::: proof
Take
\[
X=\mathbb R,
\qquad
Y=\left\{\frac1n:n\in\mathbb N\right\}.
\]
Then $Y$ is not closed in $X$, since $0\in\overline Y\setminus Y$. In its subspace topology, $Y$ is discrete. Let $\mu$ be counting measure on $Y$.

Every compact subset of $Y$ is finite: an infinite subset of $Y$ has a sequence tending to $0$, which has no limit point in $Y$, so it cannot be compact. Hence counting measure is finite on compact subsets of $Y$; on this discrete LCH space it is also inner regular. Thus $\mu$ is a Radon measure on $Y$.

The corresponding measure on $X$ is
\[
\nu(E)=\#(E\cap Y).
\]
But
\[
K:=\{0\}\cup Y
\]
is compact in $\mathbb R$, while
\[
\nu(K)=\#Y=\infty.
\]
Therefore $\nu$ is not Radon on $X$. This proves that the assumption that $Y$ is closed cannot be omitted.
:::
:::
