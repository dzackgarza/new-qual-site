---
schema: qual/card@1
id: P-DWFMA
kind: problem
title: Every Lebesgue measurable set contains a Borel set of full measure
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
solved: true
---

Let $E\subset \RR$ be a Lebesgue measurable set.
Show that there is a Borel set $B \subset E$ such that $m(E\setminus B) = 0$.

:::{.concept}
\envlist

- Definition of measurability: there exists an open $O\supset E$ such that $m_*(O\setminus E) < \eps$ for all $\eps> 0$.
- Theorem: $E$ is Lebesgue measurable iff there exists a closed set $F\subseteq E$ such that $m_*(E\setminus F) < \eps$ for all $\eps>0$.
- Every $F_\sigma, G_\delta$ is Borel.
- Claim: $E$ is measurable $\iff$ for every $\varepsilon$ there exist $F_\varepsilon \subset E \subset G_\varepsilon$ with $F_\varepsilon$ closed and $G_\varepsilon$ open and $m(G_\varepsilon \setminus E)< \varepsilon$ and $m(E\setminus F_\varepsilon) < \varepsilon$.
  - Proof: existence of $G_\eps$ is the definition of measurability.
  - Existence of $F_\eps$: ?

- Claim: $E$ is measurable $\implies$ there exists an open $O\supseteq E$ such that $m(O\setminus E) = 0$.
  - Since $E$ is measurable, for each $n\in \NN$ choose $G_n \supseteq E$ such that $m_*(G_n\setminus E) < {1\over n}$.
  - Set $O_N \definedas \Intersect_{n=1}^N G_n$ and $O\definedas \Intersect_{n=1}^\infty G_n$.
  - Suppose $E$ is bounded.
    - Note $O_N \searrow O$ and $m_*(O_1) < \infty$ if $E$ is bounded, since in this case
    \[
    m_*(G_n\setminus E) = m_*(G_1) - m_*(E) < 1 \iff m_*(G_1) < m_*(E) + {1\over n} < \infty
    .\]
    - Note $O_N \setminus E \searrow O \setminus E$ since $O_N\setminus E \definedas O_N \Intersect E^c \supseteq O_{N+1} \Intersect E^c$ for all $N$, and again $m_*(O_1 \setminus E) < \infty$.
    - So it's valid to apply continuity of measure from above:
\[
m_*(O\setminus E) 
&= \lim_{N\to\infty} m_*(O_N\setminus E) \\ 
&\leq \lim_{N\to \infty} m_*(G_N\setminus E) \\ 
&= \lim_{N\to\infty} {1\over N} = 0
,\]
      where the inequality uses subadditivity on $\Intersect_{n=1}^N G_n \subseteq G_N$
  - Suppose $E$ is unbounded.
    - Write $E^k = E \Intersect [k, k+1]^d \subset \RR^d$ as the intersection of $E$ with an annulus, and note that $E = \disjoint_{k\in \NN} E_k$.
    - Each $E_k$ is bounded, so apply the previous case to obtain $O_k \supseteq E_k$ with $m(O_k\setminus E_k) = 0$.
    - So write $O_k = E_k \disjoint N_k$ where $N_k \definedas O_k \setminus E_k$ is a null set.
    - Define $O = \Union_{k\in \NN} O_k$, note that $E\subseteq O$.
    - Now note
\[
O\setminus E 
&= \qty{\disjoint_k O_k}\setminus \qty{\disjoint_K E_k} \\
&\subseteq \disjoint_k \qty{O_k \setminus E_k} \\
\implies m_*(O\setminus E) 
&\leq m_*\qty{\disjoint \qty{O_k \setminus E_k} } = 0
,\]
  since any countable union of null sets is again null.
  - So $O\supseteq E$ with $m(O\setminus E) = 0$.
- Theorem: since $E$ is measurable, $E^c$ is measurable
  - Proof: It suffices to write $E^c$ as the union of two measurable sets, $E^c = S \Union (E^c - S)$, where $S$ is to be determined.
  - We'll produce an $S$ such that $m_*(E^c - S) = 0$ and use the fact that any subset of a null set is measurable.
  - Since $E$ is measurable, for every $\eps > 0$ there exists an open $\OO_\eps \supseteq E$ such that $m_*(\OO_\eps \setminus E) < \eps$.
  - Take the sequence $\theset{\eps_n \definedas {1\over n}}$ to produce a sequence of sets $\OO_n$.
  - Note that each $\OO_n^c$ is closed and 
  \[
  \OO_n \supseteq E \iff \OO_n^c \subseteq E^c
  .\]
  - Set $S \definedas \Union_n \OO_n^c$, which is a union of closed sets, thus an $F_\sigma$ set, thus Borel, thus measurable.
  - Note that $S\subseteq E^c$ since each $\OO_n \subseteq E^c$.
  - Note that
  \[
  E^c\setminus S 
  &\definedas E^c \setminus \qty{\Union_{n=1}^\infty \OO_n^c} \\
&\definedas E^c \Intersect \qty{\Union_{n=1}^\infty \OO_n^c}^c  \quad\text{definition of set minus} \\ 
  &= E^c \Intersect \qty{\Intersect_{n=1}^\infty \OO_n}^c  \quad \text{De Morgan's law}\\
  &= E^c \Union \qty{\Intersect_{n=1}^\infty \OO_n}  \\
  &\definedas \qty{ \Intersect_{n=1}^\infty \OO_n} \setminus E \\
  & \subseteq \OO_N \setminus E \quad \text{for every } N\in \NN
  .\]
  - Then by subadditivity,
    $$
    m_*(E^c\setminus S) \leq m_*(\OO_N \setminus E) \leq {1\over N} \quad \forall N \implies m_*(E^c\setminus S) = 0
    .$$
  - Thus $E^c\setminus S$ is measurable.
:::

:::{.solution}
\envlist

- Since $E$ is measurable, $E^c$ is measurable.
- Since $E^c$ is measurable exists an open $O\supseteq E^c$ such that $m(O\setminus E^c) = 0$.
- Set $B \definedas O^c$, then $O\supseteq E^c \iff \OO^c \subseteq E \iff B\subseteq E$.
- Computing measures yields 
\[
E\setminus B \definedas E\setminus  \OO^c \definedas E\Intersect (\OO^c)^c = E\Intersect \OO = \OO \Intersect(E^c)^c \definedas \OO \setminus E^c
,\]
  thus $m(E\setminus B) = m(\OO\setminus E^c) = 0$.
- Since $\OO$ is open, $B$ is closed and thus Borel.

d.irect Proof (Todo)

:::

