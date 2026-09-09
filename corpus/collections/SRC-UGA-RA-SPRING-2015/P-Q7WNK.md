---
schema: qual/card@1
id: P-Q7WNK
kind: problem
title: Equivalent approximation of Borel sets by open and closed sets versus $G_\delta$
  and $F_\sigma$ sets for a finite Borel measure on $\RR^n$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Spring 2015 Problem 3 in the preserved UGA real-analysis source extraction.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the legacy proof of (2) implies (1), which had reversed the set difference in the continuity-from-above step.
---

::: problem
Let $\mu$ be a finite Borel measure on $\RR^n$ and $E$ be a Borel subset of $\RR^n$.
Prove that the following two statements are equivalent:

1. For any $\varepsilon > 0$, there exists an open set $G$ and closed set $F$ such that
$$
F \subseteq E \subseteq G \quad \text{and} \quad \mu(G\setminus F) < \varepsilon.
$$

2. There exists a $G_\delta$ set $V$ and an $F_\sigma$ set $H$ such that
$$
H \subseteq E \subseteq V \quad \text{and}\quad \mu(V\setminus H) = 0.
$$
:::
::: solution
<1>1. Prove (1) implies (2).
::: proof
For each $k\ge1$, apply (1) with $\varepsilon=2^{-k}$ to obtain a closed set $F_k$ and an open set $G_k$ such that
\[
F_k\subseteq E\subseteq G_k,
\qquad
\mu(G_k\setminus F_k)<2^{-k}.
\]
Set
\[
H:=\bigcup_{k=1}^\infty F_k,
\qquad
V:=\bigcap_{k=1}^\infty G_k.
\]
Then $H$ is $F_\sigma$, $V$ is $G_\delta$, and
\[
H\subseteq E\subseteq V.
\]
Moreover, for every $k$,
\[
V\setminus H\subseteq G_k\setminus F_k,
\]
so
\[
0\le \mu(V\setminus H)\le 2^{-k}.
\]
Letting $k\to\infty$ gives
\[
\mu(V\setminus H)=0.
\]
:::

<1>2. Prove (2) implies (1).
::: proof
Write
\[
V=\bigcap_{k=1}^\infty V_k,
\qquad
H=\bigcup_{k=1}^\infty H_k,
\]
with each $V_k$ open and each $H_k$ closed. Replacing $V_k$ by $\bigcap_{j\le k}V_j$ and $H_k$ by $\bigcup_{j\le k}H_j$, we may assume
\[
V_k\downarrow V,
\qquad
H_k\uparrow H.
\]
Because $\mu$ is finite, continuity from above gives
\[
\mu(V_k\setminus V)\to0,
\]
and continuity from below gives
\[
\mu(H\setminus H_k)\to0.
\]
Given $\varepsilon>0$, choose $m,n$ such that
\[
\mu(V_m\setminus V)<\frac\varepsilon2,
\qquad
\mu(H\setminus H_n)<\frac\varepsilon2.
\]
Put
\[
G:=V_m,
\qquad
F:=H_n.
\]
Then $G$ is open, $F$ is closed, and
\[
F\subseteq H\subseteq E\subseteq V\subseteq G.
\]
Since $\mu(V\setminus H)=0$,
\[
G\setminus F
\subseteq
(G\setminus V)\cup(V\setminus H)\cup(H\setminus F),
\]
so
\[
\mu(G\setminus F)
\le \mu(G\setminus V)+\mu(V\setminus H)+\mu(H\setminus F)
<\varepsilon.
\]
This is (1).
:::
:::
