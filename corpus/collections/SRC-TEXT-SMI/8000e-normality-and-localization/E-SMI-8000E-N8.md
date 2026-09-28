---
schema: qual/card@1
id: E-SMI-8000E-N8
kind: problem
title: Unique factorization localizes
classification:
  areas:
  - algebra
  topics:
  - Localization
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
If $R$ is a ufd and $P$ prime, prove that $R_P$ is also a ufd.
:::

::: {.solution}
Let $S = R \setminus P$, so $R_P = S^{-1}R$. We use Kaplansky's criterion: an integral domain is a UFD if and only if every nonzero prime ideal contains a prime element.

<1>1. $R_P$ is an integral domain.
::: {.proof}
$S$ is multiplicatively closed with $0 \notin S$, so $R_P$ is a subring of the fraction field of the domain $R$.
:::

<1>2. Every nonzero prime ideal $\mathfrak q$ of $R_P$ contains $p/1$ for a prime element $p$ of $R$ with $p \in P$.
::: {.proof}
The contraction $\mathfrak p = \{a \in R : a/1 \in \mathfrak q\}$ is a prime ideal of $R$ disjoint from $S$, so $\mathfrak p \subseteq P$. It is nonzero: if $a/s \in \mathfrak q$ is nonzero, then $a = s \cdot (a/s) \in \mathfrak p$ and $a \neq 0$. Choose $0 \ne x \in \mathfrak p$; $x$ is a nonunit because $\mathfrak p$ is proper, so $x = p_1 \cdots p_k$ with each $p_i$ prime in the UFD $R$. Since $\mathfrak p$ is prime, some $p = p_i$ lies in $\mathfrak p \subseteq P$, and $p/1 \in \mathfrak q$.
:::

<1>3. For a prime element $p$ of $R$ with $p \in P$, the element $\pi = p/1$ is prime in $R_P$.
::: {.proof}
$\pi \neq 0$ because $p \neq 0$, and $\pi$ is not a unit because $p \in P$ (the units of $R_P$ are the $a/s$ with $a \notin P$). Suppose $\pi$ divides $\frac{a}{s_1}\cdot\frac{b}{s_2}$, say $\frac{ab}{s_1 s_2} = \frac{p c}{s_3}$ with $c \in R$, $s_3 \in S$. Since $R$ is a domain, $s_3 ab = s_1 s_2 p c$, so $p \mid s_3 ab$ in $R$. As $s_3 \notin P \supseteq (p)$, $p \nmid s_3$, so $p \mid a$ or $p \mid b$. If $a = p a'$, then $\frac{a}{s_1} = \pi \cdot \frac{a'}{s_1}$; similarly for $b$. Hence $\pi$ is prime.
:::

<1>4. Q.E.D.
::: {.proof}
By steps <1>2 and <1>3, every nonzero prime ideal of the domain $R_P$ (step <1>1) contains a prime element, so $R_P$ is a UFD by Kaplansky's criterion.
:::
:::
