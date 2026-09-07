---
schema: qual/card@1
id: P-ALGF25B
kind: problem
title: Minimal Sylow intersections and the normalizer of $N$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared all four parts with Problem 2 on page 3 of the official FA25 algebra exam PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Re-derived the normalizer argument and checked that minimality is used only after producing a distinct Sylow intersection contained in P1 cap P2.
---

::: problem
Suppose $G$ is a finite group.
Let $\operatorname{Syl}_p(G)$ be the set of all Sylow $p$-subgroups of $G$.
Suppose $P_1, P_2 \in \operatorname{Syl}_p(G)$ are distinct and $P_1 \cap P_2$ is minimal among all the subgroups that are the intersection of two distinct Sylow $p$-subgroups.
Suppose $N$ is a subgroup of $P_1 \cap P_2$ and $N \trianglelefteq P_i$ for $i = 1, 2$, and let $H := N_G(N)$.

(a) Prove that for every $P \in \operatorname{Syl}_p(G)$, there exists $h \in H$ such that $hPh^{-1} \cap H \subseteq P_1$.

(b) Prove that for every $P \in \operatorname{Syl}_p(G)$, there exists $h \in H$ such that $hPh^{-1} \cap P_2 = P_1 \cap P_2$.

(c) Prove that for every $P \in \operatorname{Syl}_p(G)$, $N \subseteq P$.

(d) Suppose $P_1$ is abelian.
Prove that
\[
P_1 \cap P_2 = \bigcap_{P \in \operatorname{Syl}_p(G)} P.
\]
:::

::: {.solution}
Put $D=P_1\cap P_2$.

<1>1. The subgroups $P_1$ and $P_2$ are Sylow $p$-subgroups of $H=N_G(N)$.
::: {.proof}
Because $N\trianglelefteq P_i$, every element of $P_i$ normalizes $N$; hence
\[
P_1,P_2\le H.
\]
Each $P_i$ is already a Sylow $p$-subgroup of $G$, so no $p$-subgroup of the subgroup $H\le G$ can properly contain it.
Thus $P_1,P_2\in\operatorname{Syl}_p(H)$.
:::

<1>2. For every $P\in\operatorname{Syl}_p(G)$, there exists $h\in H$ such that
\[
hPh^{-1}\cap H\subseteq P_1.
\]
::: {.proof}
The intersection $P\cap H$ is a $p$-subgroup of $H$.
Choose a Sylow $p$-subgroup $Q$ of $H$ containing $P\cap H$.
By Sylow conjugacy inside $H$, there is $h\in H$ such that
\[
hQh^{-1}=P_1.
\]
Since $h$ normalizes $H$,
\[
hPh^{-1}\cap H
=h(P\cap H)h^{-1}
\subseteq hQh^{-1}
=P_1.
\]
This proves part (a).
:::

<1>3. The same $h$ may be chosen so that
\[
hPh^{-1}\cap P_2=D.
\]
::: {.proof}
Take $h$ from <1>2 and write $P'=hPh^{-1}$.
Since $P_2\le H$,
\[
P'\cap P_2\subseteq P'\cap H\subseteq P_1,
\]
and therefore
\[
P'\cap P_2\subseteq P_1\cap P_2=D.
\]

The Sylow subgroups $P'$ and $P_2$ are distinct.
Indeed, if $P'=P_2$, then $P_2=P'\cap H\subseteq P_1$, forcing $P_2=P_1$, contrary to the hypothesis.
Thus $P'\cap P_2$ is itself an intersection of two distinct Sylow $p$-subgroups.
By the minimality of $D$ among all such intersections, the displayed containment cannot be strict.
Hence
\[
P'\cap P_2=D,
\]
which proves part (b).
:::

<1>4. The subgroup $N$ is contained in every Sylow $p$-subgroup of $G$.
::: {.proof}
Fix $P\in\operatorname{Syl}_p(G)$ and choose $h\in H$ as in <1>3.
Since $N\subseteq D$,
\[
N\subseteq D=hPh^{-1}\cap P_2\subseteq hPh^{-1}.
\]
But $h\in H=N_G(N)$, so $h^{-1}Nh=N$.
Conjugating the containment by $h^{-1}$ gives $N\subseteq P$.
This proves part (c).
:::

<1>5. If $P_1$ is abelian, then $D$ is exactly the intersection of all Sylow $p$-subgroups of $G$.
::: {.proof}
Every Sylow $p$-subgroup of $G$ is conjugate to $P_1$, so every Sylow $p$-subgroup is abelian; in particular, $P_2$ is abelian.
Therefore
\[
D\trianglelefteq P_1
\qquad\text{and}\qquad
D\trianglelefteq P_2.
\]
Apply part (c) with $N=D$.
It gives
\[
D\subseteq P
\qquad\text{for every }P\in\operatorname{Syl}_p(G),
\]
so
\[
D\subseteq\bigcap_{P\in\operatorname{Syl}_p(G)}P.
\]
The reverse containment is immediate because the intersection on the right is contained in both $P_1$ and $P_2$.
Hence
\[
P_1\cap P_2=D=\bigcap_{P\in\operatorname{Syl}_p(G)}P,
\]
proving part (d).
:::
:::
