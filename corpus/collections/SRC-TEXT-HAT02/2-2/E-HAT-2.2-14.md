---
schema: qual/card@1
id: E-HAT-2.2-14
kind: problem
title: Even maps $S^n \to S^n$ must have even degree; degree zero when $n$ even
classification:
  areas:
  - topology
  topics:
  - Degree
  - Projective Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 14; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof checked via cellular homology, covering spaces, and degree.
---

A map $f: S^n \to S^n$ satisfying $f(x) = f(-x)$ for all $x$ is called an even map.
Show that an even map $S^n \to S^n$ must have even degree, and that the degree must in fact be zero when $n$ is even.
When $n$ is odd, show there exist even maps of any given even degree.
[Hints: If $f$ is even, it factors as a composition $S^n \to \mathbb{RP}^n \to S^n$. Using the calculation of $H_n(\mathbb{RP}^n)$ in the text, show that the induced map $H_n(S^n) \to H_n(\mathbb{RP}^n)$ sends a generator to twice a generator when $n$ is odd. It may be helpful to show that the quotient map $\mathbb{RP}^n \to \mathbb{RP}^n/\mathbb{RP}^{n-1}$ induces an isomorphism on $H_n$ when $n$ is odd.]

::: {.solution}
Let $f:S^n\to S^n$ be even, so $f(x)=f(-x)$. Then $f$ factors through the antipodal quotient:
\[
S^n\xrightarrow{q}\mathbb{RP}^n\xrightarrow{g}S^n.
\]

<1>1. If $n$ is even, then $\deg f=0$.
::: {.proof}
For even $n$,
\[
H_n(\mathbb{RP}^n;\mathbb Z)=0.
\]
Hence the induced map
\[
H_n(S^n)\xrightarrow{q_*}H_n(\mathbb{RP}^n)
\]
is zero, and therefore
\[
f_*=g_*q_*=0.
\]
Thus $\deg f=0$.
:::

<1>2. If $n$ is odd, every even map has even degree.
::: {.proof}
For odd $n$, $\mathbb{RP}^n$ is orientable and
\[
H_n(\mathbb{RP}^n)\cong\mathbb Z.
\]
The quotient map $q:S^n\to\mathbb{RP}^n$ is a two-sheeted covering between oriented closed $n$-manifolds, so
\[
q_*[S^n]=2[\mathbb{RP}^n].
\]
If $g_*$ is multiplication by $k$, then
\[
f_*[S^n]=g_*q_*[S^n]=2k[S^n].
\]
Hence $\deg f=2k$ is even.
:::

<1>3. When $n$ is odd, every even integer occurs as the degree of an even map.
::: {.proof}
Collapse the $(n-1)$-skeleton of $\mathbb{RP}^n$:
\[
c:\mathbb{RP}^n\to\mathbb{RP}^n/\mathbb{RP}^{n-1}\cong S^n.
\]
For odd $n$, the top cellular boundary in $\mathbb{RP}^n$ is zero, so the unique top cell generates $H_n(\mathbb{RP}^n)$. The quotient map $c$ carries this top cell homeomorphically to the top cell of $S^n$, hence
\[
c_*:H_n(\mathbb{RP}^n)\xrightarrow{\cong}H_n(S^n).
\]
Given any $k\in\mathbb Z$, choose a degree-$k$ map
\[
h_k:S^n\to S^n.
\]
Then
\[
f_k=h_k\circ c\circ q:S^n\to S^n
\]
is even because it factors through $q$, and
\[
\deg f_k=k\cdot1\cdot2=2k.
\]
Thus every prescribed even degree occurs.
:::
:::
