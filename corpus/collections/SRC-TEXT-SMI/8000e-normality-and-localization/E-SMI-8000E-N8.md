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
<1>1. Multiplicative localization setup and Kaplansky's criterion:
<2>1. Let $S = R \setminus P$. Since $P$ is a prime ideal in the integral domain $R$, $S$ is a multiplicatively closed subset of $R$ with $0 \notin S$, so the localization $R_P = S^{-1}R$ is an integral domain.
<2>2. **Kaplansky's Criterion for UFDs:** An integral domain $A$ is a unique factorization domain (UFD) if and only if every non-zero prime ideal of $A$ contains a non-zero prime element.

<1>2. Proof that every non-zero prime ideal of $R_P$ contains a prime element:
<2>1. Let $\mathfrak{q}$ be a non-zero prime ideal in $R_P = S^{-1}R$.
The contraction $\mathfrak{p} = \mathfrak{q} \cap R$ is a non-zero prime ideal in $R$ satisfying $\mathfrak{p} \subseteq P$ (so $\mathfrak{p} \cap S = \emptyset$) and $\mathfrak{q} = S^{-1}\mathfrak{p}$.
<2>2. Choose any non-zero element $x \in \mathfrak{p}$.
Since $R$ is a UFD, $x$ has a factorization into prime elements in $R$:
\[
x = p_1 p_2 \cdots p_k \in \mathfrak{p},
\]
where each $p_i \in R$ is a prime element.
Since $\mathfrak{p}$ is a prime ideal, $p_j \in \mathfrak{p}$ for some $j \in \{1, \ldots, k\}$.
<2>3. Consider the element $\pi = \frac{p_j}{1} \in S^{-1}\mathfrak{p} = \mathfrak{q}$.
We verify that $\pi$ is a prime element in $R_P$:
- $\pi \neq 0$ because $p_j \neq 0$.
- $\pi$ is not a unit in $R_P$ because $p_j \in \mathfrak{p} \subseteq P$, so $p_j \notin S$.
- Let $\frac{a}{s_1}, \frac{b}{s_2} \in R_P$ such that $\pi \mid \frac{a}{s_1}\frac{b}{s_2}$ in $R_P$.
  This means $\frac{ab}{s_1 s_2} = \frac{p_j c}{s_3}$ for some $\frac{c}{s_3} \in R_P$, so there exists $u \in S$ such that:
\[
u s_3 a b = u s_1 s_2 p_j c \implies p_j \mid (u s_3) a b \quad \text{in } R.
\]
Because $p_j$ is a prime element in $R$, $p_j \mid u s_3$ or $p_j \mid a$ or $p_j \mid b$.
Since $u, s_3 \in S = R \setminus P$ and $p_j \in P$, $p_j \nmid u s_3$.
Therefore $p_j \mid a$ or $p_j \mid b$ in $R$, which implies $\pi \mid \frac{a}{s_1}$ or $\pi \mid \frac{b}{s_2}$ in $R_P$.
Thus $\pi$ is a prime element of $R_P$.

<1>3. Conclusion:
Since every non-zero prime ideal $\mathfrak{q} \subseteq R_P$ contains the prime element $\frac{p_j}{1}$, by Kaplansky's Criterion $R_P$ is a UFD. Q.E.D.
:::
