---
schema: qual/card@1
id: E-SMI-8000E-ED2
kind: exercise
title: Submodules of free modules over a Euclidean domain are free of no greater rank
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Prove every submodule of $R^m$ is finitely generated, and in fact isomorphic to $R^n$ where $n$ is at most equal to $m$.
[Hint: read the proof for $\ZZ$.]
:::

::: {.solution}
<1>1. Base case ($m = 1$):
<2>1. A submodule of $R^1 = R$ is an ideal $I \subseteq R$.
Because $R$ is a Euclidean domain, every ideal is principal: $I = \langle a \rangle = aR$ for some $a \in R$.
Proof: Euclidean algorithm implies $R$ is a PID.
<2>2. - If $a = 0$, then $I = \{0\} \cong R^0$ is free of rank $0 \le 1$.
- If $a \neq 0$, the map $\phi: R \to aR$ given by $r \mapsto ar$ is an isomorphism of $R$-modules because $R$ is an integral domain ($\ker \phi = \{0\}$).
Thus $I \cong R^1$ is free of rank $1 \le 1$.
Proof: base case established.

<1>2. Inductive step:
<2>1. Assume by induction that every submodule of $R^{m-1}$ is free of rank at most $m - 1$.
Let $M \subseteq R^m$ be an $R$-submodule.
Proof: induction hypothesis.
<2>2. Consider the projection onto the first coordinate:
\[
\pi: R^m \to R, \qquad (x_1, x_2, \dots, x_m) \mapsto x_1.
\]
The restriction $\pi|_M: M \to R$ is an $R$-module homomorphism, and its image $I = \pi(M)$ is an ideal of $R$.
Proof: projection homomorphism.
<2>3. Because $R$ is a PID, $I = aR$ for some $a \in R$.
- **Case 1: $I = \{0\}$.**
  Then $M \subseteq \ker(\pi) \cong R^{m-1}$.
  By the induction hypothesis, $M$ is free of rank $n \le m - 1 \le m$.
- **Case 2: $I = aR \neq \{0\}$.**
  Then $I \cong R$ is free of rank 1.
  Choose $v \in M$ such that $\pi(v) = a$.
  The short exact sequence:
  \[
  0 \longrightarrow M \cap \ker(\pi) \longrightarrow M \xrightarrow{\pi|_M} I \longrightarrow 0
  \]
  splits because $I \cong R$ is a free (hence projective) $R$-module, with splitting given by $r a \mapsto r v$.
Proof: splitting lemma for modules.
<2>4. Therefore:
\[
M \cong (M \cap \ker(\pi)) \oplus I \cong (M \cap \ker(\pi)) \oplus R.
\]
Because $M \cap \ker(\pi) \subseteq \ker(\pi) \cong R^{m-1}$, by the induction hypothesis $M \cap \ker(\pi) \cong R^k$ for some $k \le m - 1$.
Hence:
\[
M \cong R^k \oplus R \cong R^{k+1},
\]
which is free of rank $n = k + 1 \le (m - 1) + 1 = m$.
Proof: direct sum of free modules is free.

<1>3. Conclusion:
Every submodule of $R^m$ is free of rank $n \le m$, and in particular finitely generated. Q.E.D.
Proof: <1>1 and <1>2.
:::
