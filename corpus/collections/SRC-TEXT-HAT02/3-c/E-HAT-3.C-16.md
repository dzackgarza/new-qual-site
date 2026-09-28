---
schema: qual/card@1
id: E-HAT-3.C-16
kind: problem
title: "Classification of Hopf algebras over $\\mathbb{Z}$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 16; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Classify algebraically the Hopf algebras $A$ over $\mathbb{Z}$ such that $A^n$ is free for each $n$ and $A \otimes \mathbb{Q} \approx \mathbb{Q}[\alpha]$.
In particular, determine which Hopf algebras $A \otimes \mathbb{Z}_p$ arise from such $A$'s.
:::

::: {.solution}
We classify these Hopf algebras as integral Hopf lattices in a rational polynomial Hopf algebra.

Let $A$ satisfy the hypotheses and let $d>0$ be the least positive degree in which $A\otimes\mathbb Q$ is nonzero. Since
\[
A\otimes\mathbb Q\cong\mathbb Q[t]
\]
as a graded algebra, $|t|=d$ is even. In degree $d$ there are no positive-degree decomposable terms, so the Hopf axioms force
\[
\Delta(t)=t\otimes1+1\otimes t.
\]
Consequently
\[
\Delta(t^n)=\sum_{i=0}^n\binom ni t^i\otimes t^{n-i}.
\]

Since each $A^{nd}$ is a free rank-one subgroup of $\mathbb Q t^n$, choose generators
\[
x_n=q_nt^n,
\qquad q_n\in\mathbb Q_{>0},
\qquad q_0=q_1=1,
\]
where rescaling $t$ has been used to normalize $q_1=1$. Then
\[
x_ix_j=m_{ij}x_{i+j},
\qquad
m_{ij}=\frac{q_iq_j}{q_{i+j}},
\]
and
\[
\Delta(x_{i+j})
=\sum_{i+j=n}c_{ij}x_i\otimes x_j,
\qquad
c_{ij}=\binom{i+j}{i}\frac{q_{i+j}}{q_iq_j}.
\]
Thus $A$ is an integral Hopf algebra exactly when, for every $i,j\ge0$,
\[
\boxed{m_{ij}\in\mathbb Z_{>0},\qquad
c_{ij}=\frac{\binom{i+j}{i}}{m_{ij}}\in\mathbb Z_{>0}.}
\]
Equivalently,
\[
\boxed{m_{ij}\mid\binom{i+j}{i}.}
\]
Associativity is exactly the cocycle relation
\[
\boxed{m_{ij}m_{i+j,k}=m_{jk}m_{i,j+k}}
\]
with $m_{i0}=m_{0i}=1$. Conversely, any positive-integer system $(m_{ij})$ satisfying these divisor and cocycle conditions determines $q_n$ recursively by
\[
q_0=q_1=1,
\qquad
q_{n+1}=\frac{q_n}{m_{n,1}},
\]
and the cocycle identity then gives
\[
m_{ij}=q_iq_j/q_{i+j}
\]
for all $i,j$. The formulas above define a Hopf-stable lattice
\[
A=\bigoplus_{n\ge0}\mathbb Z\,q_nt^n\subset\mathbb Q[t].
\]
This proves the classification. The two extreme cases are
\[
m_{ij}=1,
\]
which gives the polynomial Hopf algebra $\mathbb Z[t]$, and
\[
m_{ij}=\binom{i+j}{i},
\]
which gives the divided-power Hopf algebra $\Gamma_{\mathbb Z}[t]$.

Now fix a prime $p$ and reduce modulo $p$. With $\bar x_n$ denoting the image of $x_n$, every reduction arising from an integral form above has
\[
\bar x_i\bar x_j=\overline{m_{ij}}\,\bar x_{i+j},
\]
\[
\Delta(\bar x_n)
=\sum_{i=0}^n
\overline{\frac{\binom ni}{m_{i,n-i}}}
\,\bar x_i\otimes\bar x_{n-i}.
\]
Hence the mod-$p$ Hopf algebra is determined by the $p$-adic valuations
\[
e_{ij}=v_p(m_{ij}).
\]
They satisfy
\[
0\le e_{ij}\le v_p\binom{i+j}{i},
\]
and the additive cocycle relation
\[
e_{ij}+e_{i+j,k}=e_{jk}+e_{i,j+k}.
\]
Conversely, any such $p$-adic divisor cocycle lifts: take
\[
m_{ij}=p^{e_{ij}}
\]
(and choose valuation $0$ at all other primes), then the preceding integral construction produces a Hopf algebra whose reduction has exactly this structure. Up to rescaling each one-dimensional graded piece by a unit of $\mathbb F_p$, these are precisely the Hopf algebras $A\otimes\mathbb F_p$ that arise.

In particular, the polynomial and divided-power reductions are the two extreme valuation choices $e_{ij}=0$ and
\[
e_{ij}=v_p\binom{i+j}{i},
\]
while intermediate divisor cocycles give the mixed integral forms.
:::
