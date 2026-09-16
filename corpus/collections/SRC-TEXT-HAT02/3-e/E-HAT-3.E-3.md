---
schema: qual/card@1
id: E-HAT-3.E-3
kind: problem
title: "Bockstein homomorphisms on smash products of Moore spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.E, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $X$ be the smash product of $k$ copies of a Moore space $M(\mathbb{Z}_p, n)$ with $p$ prime.
Compute the Bockstein homomorphisms in $H^*(X; \mathbb{Z}_p)$ and use this to describe $H^*(X; \mathbb{Z})$.
:::

::: {.solution}
Let
\[
M=M(\mathbb Z_p,n).
\]
With $\mathbb Z_p$ coefficients, its reduced cohomology has one generator
\[
a\in\widetilde H^n(M;\mathbb Z_p)
\]
and one generator
\[
b\in\widetilde H^{n+1}(M;\mathbb Z_p),
\]
with Bockstein
\[
\beta(a)=b,
\qquad \beta(b)=0.
\]

For the smash product of $k$ copies,
\[
X=M^{\wedge k},
\]
the reduced Künneth theorem over the field $\mathbb Z_p$ gives
\[
\widetilde H^*(X;\mathbb Z_p)
\cong
\widetilde H^*(M;\mathbb Z_p)^{\otimes k}.
\]
A basis consists of tensors
\[
u_1\otimes\cdots\otimes u_k,
\qquad u_i\in\{a,b\}.
\]
The Bockstein is a graded derivation, hence
\[
\beta(u_1\otimes\cdots\otimes u_k)
=
\sum_{j=1}^k
(-1)^{|u_1|+\cdots+|u_{j-1}|}
 u_1\otimes\cdots\otimes\beta(u_j)\otimes\cdots\otimes u_k.
\]
Thus the Bockstein complex is the $k$-fold tensor product of the two-term acyclic complex
\[
\mathbb Z_p\{a\}\xrightarrow{\cong}\mathbb Z_p\{b\}.
\]
In particular its Bockstein cohomology is zero.

To recover the integral groups explicitly, use cellular chains. The reduced cellular chain complex of $M$ is the two-term complex
\[
0\to\mathbb Z\xrightarrow{p}\mathbb Z\to0
\]
in degrees $n+1,n$. The reduced chain complex of $X$ is its $k$-fold tensor product, the Koszul complex for the sequence $(p,\dots,p)$. Its homology is
\[
\widetilde H_{kn+j}(X;\mathbb Z)
\cong(\mathbb Z_p)^{\binom{k-1}{j}},
\qquad 0\le j\le k-1,
\]
and zero in all other degrees. This follows inductively from the Künneth short exact sequence: tensoring with one more Moore complex replaces the multiplicities by adjacent sums, giving Pascal's identity.

All these homology groups are torsion, so the cohomology universal coefficient theorem shifts them up by one degree through Ext. Hence
\[
\boxed{
\widetilde H^{kn+r}(X;\mathbb Z)
\cong(\mathbb Z_p)^{\binom{k-1}{r-1}}
\quad(1\le r\le k),}
\]
and the reduced integral cohomology vanishes in all other degrees.
:::
