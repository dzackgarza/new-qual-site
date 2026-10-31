---
schema: qual/card@1
id: E-F46JG
kind: problem
title: Every topological group is completely regular
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Prove the following.

Theorem.
Every topological group is completely regular.

Proof.
Let $V_0$ be a neighborhood of the identity element $e$, in the topological group $G$.
In general, choose $V_n$ to be a neighborhood of $e$ such that $V_n \cdot V_n \subset V_{n-1}$.
Consider the set of all dyadic rationals $p$, that is, all rational numbers of the form $k/2^n$, with $k$ and $n$ integers.
For each dyadic rational $p$ in $(0, 1]$, define an open set $U(p)$ inductively as follows: $U(1) = V_0$ and $U(\tfrac{1}{2}) = V_1$.
Given $n$, if $U(k/2^n)$ is defined for $0 < k/2^n \leq 1$, define

$$
U(1/2^{n+1}) = V_{n+1},
$$

$$
U((2k+1)/2^{n+1}) = V_{n+1} \cdot U(k/2^n)
$$

for $0 < k < 2^n$.
For $p \leq 0$, let $U(p) = \varnothing$, and for $p > 1$, let $U(p) = G$.
Show that

$$
V_n \cdot U(k/2^n) \subset U((k+1)/2^n)
$$

for all $k$ and $n$.
Proceed as in the Urysohn lemma.

This exercise is adapted from [M-Z], to which the reader is referred for further results on topological groups.
:::

::: {.solution}

By Munkres's definition, a topological group is $T_1$; the supplementary exercises of §22 show it is Hausdorff. Let $A$ be closed and $x\notin A$. Translation reduces the problem to separating $e$ from the closed set $x^{-1}A$. Choose a symmetric open neighborhood $V_0$ of $e$ disjoint from $x^{-1}A$, and recursively choose symmetric open neighborhoods $V_{n+1}$ with $V_{n+1}^2\subset V_n$. These choices are possible by continuity of multiplication and inversion.

Use the dyadic sets $U(p)$ in the question. We check the asserted inclusion for $0\le k<2^n$ by induction on $n$. At $n=0$ it reads $V_0U(0)=\varnothing\subset U(1)$. At level $n+1$, the case $k=0$ is again immediate. If $k=2j$ with $j\ge1$, the definition gives
$$
V_{n+1}U(j/2^n)=U((2j+1)/2^{n+1}).
$$
If $k=1$, then $V_{n+1}U(1/2^{n+1})=V_{n+1}^2\subset V_n=U(1/2^n)$. For $k=2j+1$ with $j\ge1$, the induction hypothesis gives
$$
V_{n+1}U((2j+1)/2^{n+1})
=V_{n+1}^2U(j/2^n)
\subset V_nU(j/2^n)
\subset U((j+1)/2^n).
$$
This proves the inclusion, including the two boundary cases that use the separate definitions of $U(0)$ and $U(1/2^{n+1})$.

Since $e\in V_n$, adjacent dyadic sets are nested. For any dyadic $0<p<q\le1$, choose a fine enough level that the interval $(p,q)$ contains adjacent dyadics $r,r+2^{-n}$. Then $U(p)\subset U(r)$, and symmetry of $V_n$ gives
$$
\overline{U(r)}\subset V_nU(r)\subset U(r+2^{-n})\subset U(q).
$$
Indeed, if $z\in\overline{U(r)}$, then $V_nz$ meets $U(r)$, so $z\in V_n^{-1}U(r)=V_nU(r)$. Consequently $\overline{U(p)}\subset U(q)$ whenever $p<q$ are dyadic in $(0,1]$.

Define
$$
f(z)=\inf\{p\in\mathcal D:z\in U(p)\},
$$
where $\mathcal D$ is the set of dyadic rationals. The set in the infimum is nonempty because $U(p)=G$ for $p>1$, and $0\le f\le1$. For $0<t\le1$, the set $\{f<t\}$ is the union of the $U(p)$ with dyadic $p<t$, so it is open. The closure inclusion shows that $\{f>t\}$ is the union of the complements of $\overline{U(p)}$ with dyadic $p>t$; this is open as well. Thus $f$ is continuous. Since $e\in V_n=U(2^{-n})$ for every $n$, $f(e)=0$. Every $U(p)$ for $p\le1$ lies in $U(1)=V_0$, so $f=1$ on $G\setminus V_0$, in particular on $x^{-1}A$. Translating back separates $x$ from $A$. The $T_1$ property from the definition completes the claim.

:::
