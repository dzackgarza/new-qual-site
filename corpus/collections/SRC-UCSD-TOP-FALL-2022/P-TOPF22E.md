---
schema: qual/card@1
id: P-TOPF22E
kind: problem
title: "Long exact sequence for homology with Z, R, and R/Z coefficients; homology of RP^infinity with T coefficients"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Coefficients
  - Exact Sequences
  - Projective Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Consider the circle in the form of the abelian group $T = \mathbb{R}/\mathbb{Z}$.
Show that there is a long exact sequence relating homology with coefficients in $\mathbb{Z}$, $\mathbb{R}$ and $T$ and use it to compute $H_*(\mathbb{RP}^\infty; T)$.
:::

::: {.solution}
**Goal.** Derive the long exact sequence relating $H_*(\cdot;\ZZ)$, $H_*(\cdot;\RR)$, $H_*(\cdot;T)$, and compute $H_*(\RP^\infty; T)$.

<1>1. The short exact sequence $0 \to \ZZ \to \RR \to T \to 0$ of coefficient groups.
Proof: $\ZZ \hookrightarrow \RR$ and $T = \RR/\ZZ$.

<1>2. This induces a long exact sequence in homology:
$$
\cdots \to H_n(X;\ZZ) \to H_n(X;\RR) \to H_n(X;T) \to H_{n-1}(X;\ZZ) \to \cdots
$$
Proof: the short exact sequence of coefficients induces a long exact sequence in homology (via the universal coefficient theorem / the long exact sequence of the tensor product).

<1>3. Compute $H_*(\RP^\infty;\ZZ)$ and $H_*(\RP^\infty;\RR)$.
<2>1. $H_n(\RP^\infty;\ZZ) = \ZZ$ for $n = 0$, $\ZZ/2$ for $n$ odd, $0$ otherwise.
Proof: standard homology of $\RP^\infty$.
<2>2. $H_n(\RP^\infty;\RR) = \RR$ for $n = 0$, $0$ for $n > 0$.
Proof: $\RP^\infty$ has no free part in positive degrees (all positive homology is $\ZZ/2$ torsion), so tensoring with $\RR$ kills it.

<1>4. Compute $H_*(\RP^\infty; T)$ from the long exact sequence.
<2>1. For $n \ge 1$ even: $H_n(\RP^\infty;\ZZ) = 0$ and $H_n(\RP^\infty;\RR) = 0$, so $H_n(\RP^\infty;T) \cong H_{n-1}(\RP^\infty;\ZZ) = \ZZ/2$ (for $n$ even, $n-1$ odd).
Proof: the LES gives $0 \to H_n(\cdot;T) \to H_{n-1}(\cdot;\ZZ) \to H_{n-1}(\cdot;\RR) = 0$, so $H_n(\cdot;T) \cong H_{n-1}(\cdot;\ZZ) = \ZZ/2$.
<2>2. For $n \ge 1$ odd: $H_n(\RP^\infty;\ZZ) = \ZZ/2$ and $H_n(\RP^\infty;\RR) = 0$, so the LES gives $0 \to H_n(\cdot;T) \to H_{n-1}(\cdot;\ZZ) = 0$, hence $H_n(\cdot;T) = 0$.
Proof: $H_{n-1}(\cdot;\ZZ) = 0$ for $n-1$ even, so $H_n(\cdot;T) = 0$.
<2>3. $H_0(\RP^\infty;T) = T$.
Proof: $H_0(X;G) = G$ for path-connected $X$.

<1>5. Q.E.D.
Proof: $H_0(\RP^\infty;T) = T$, $H_n(\RP^\infty;T) = \ZZ/2$ for $n$ even $\ge 2$, and $H_n(\RP^\infty;T) = 0$ for $n$ odd.
:::
