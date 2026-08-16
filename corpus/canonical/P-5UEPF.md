---
schema: qual/card@1
id: P-5UEPF
kind: problem
title: Let $E\subset \RR$ be a Lebesgue measurable set. Show that there is a...
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
---

::: problem
Let $E\subset \RR$ be a Lebesgue measurable set.
Show that there is a Borel set $B \subset E$ such that $m(E\setminus B) = 0$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Case 1: $m(E) < \infty$.**
By the outer regularity of Lebesgue measure applied to the complement $E^c$, for every $n \in \NN$, there exists an open set $U_n \supseteq E^c$ such that $m(U_n \setminus E^c) < \frac{1}{n}$.
Let $F_n = U_n^c$. Then $F_n$ is closed (hence Borel), and $F_n \subseteq E$.
Furthermore:
$$
E \setminus F_n = E \cap U_n = U_n \setminus E^c,
$$
so $m(E \setminus F_n) < \frac{1}{n}$.
Define $B = \bigcup_{n=1}^\infty F_n$. As a countable union of closed sets, $B$ is an $F_\sigma$ set (hence Borel), and $B \subseteq E$.
Then:
$$
E \setminus B = E \setminus \bigcup_{n=1}^\infty F_n = \bigcap_{n=1}^\infty (E \setminus F_n),
$$
so $m(E \setminus B) \leq m(E \setminus F_n) < \frac{1}{n}$ for all $n \geq 1$.
Taking $n \to \infty$ gives $m(E \setminus B) = 0$.

**Case 2: General $E \subseteq \RR$.**
Decompose $\RR$ into a countable union of bounded disjoint intervals: $\RR = \bigcup_{k \in \ZZ} [k, k+1)$.
Let $E_k = E \cap [k, k+1)$. Then $m(E_k) \leq 1 < \infty$ for each $k$.
By Case 1, for each $k \in \ZZ$, there exists a Borel set $B_k \subseteq E_k$ such that $m(E_k \setminus B_k) = 0$.
Define $B = \bigcup_{k \in \ZZ} B_k$. Then $B$ is Borel, $B \subseteq \bigcup_{k} E_k = E$, and:
$$
E \setminus B = \bigcup_{k \in \ZZ} (E_k \setminus B) \subseteq \bigcup_{k \in \ZZ} (E_k \setminus B_k).
$$
By countable subadditivity:
$$
m(E \setminus B) \leq \sum_{k \in \ZZ} m(E_k \setminus B_k) = 0,
$$
which proves $m(E \setminus B) = 0$.
:::
