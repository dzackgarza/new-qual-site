---
schema: qual/card@1
id: E-HAT-3.C-16
kind: problem
title: Classification of Hopf algebras over $\ZZ$
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
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
Classify algebraically the Hopf algebras $A$ over $\ZZ$ such that $A^n$ is free for each $n$ and $A \otimes \QQ \approx \QQ[\alpha]$.
In particular, determine which Hopf algebras $A \otimes \ZZ_p$ arise from such $A$'s.
:::

::: {.solution}
We classify these Hopf algebras as integral Hopf lattices in a rational polynomial Hopf algebra.

Let $A$ satisfy the hypotheses and let $d>0$ be the least positive degree in which $A\otimes\QQ$ is nonzero. Since
$$
A\otimes\QQ\cong\QQ[t]
$$
as a graded algebra, $\gradeddegree{t}=d$ is positive. Hatcher's Hopf algebra need not be graded-commutative, so $d$ may be odd. In degree $d$ there are no positive-degree decomposable terms, so the Hopf axioms force
$$
\Delta(t)=t\otimes1+1\otimes t.
$$
Consequently $\Delta(t^n)=\sum_{i+j=n}b_{ij}t^i\otimes t^j$. If $d$ is even, $b_{ij}=\binom{i+j}{i}$. If $d$ is odd, the two terms of $\Delta(t)$ anticommute in the graded tensor product, giving
$$
b_{ij}=\begin{cases}
0&i,j\text{ both odd},\\
\displaystyle\binom{\lfloor(i+j)/2\rfloor}{\lfloor i/2\rfloor}&\text{otherwise}.
\end{cases}
$$

Since each $A^{nd}$ is a free rank-one subgroup of $\QQ t^n$, choose generators
$$
x_n=q_nt^n,
\qquad q_n\in\QQ_{>0},
\qquad q_0=q_1=1,
$$
where rescaling $t$ has been used to normalize $q_1=1$. Then
$$
x_ix_j=m_{ij}x_{i+j},
\qquad
m_{ij}=\frac{q_iq_j}{q_{i+j}},
$$
and
$$
\Delta(x_n)
=\sum_{i+j=n}c_{ij}x_i\otimes x_j,
\qquad
c_{ij}=b_{ij}\frac{q_{i+j}}{q_iq_j}.
$$
Thus $A$ is an integral Hopf algebra exactly when, for every $i,j\ge0$,
$$
\boxed{m_{ij}\in\ZZ_{>0},\qquad
c_{ij}=\frac{b_{ij}}{m_{ij}}\in\ZZ.}
$$
Equivalently, $m_{ij}$ divides $b_{ij}$ whenever $b_{ij}\ne0$; a zero $b_{ij}$ imposes no divisibility condition.
Associativity is exactly the cocycle relation
$$
\boxed{m_{ij}m_{i+j,k}=m_{jk}m_{i,j+k}}
$$
with $m_{i0}=m_{0i}=1$. Conversely, any positive-integer system $(m_{ij})$ satisfying these divisor and cocycle conditions determines $q_n$ recursively by
$$
q_0=q_1=1,
\qquad
q_{n+1}=\frac{q_n}{m_{n,1}},
$$
and the cocycle identity then gives
$$
m_{ij}=q_iq_j/q_{i+j}
$$
for all $i,j$. The formulas above define a Hopf-stable lattice
$$
A=\bigoplus_{n\ge0}\ZZ\,q_nt^n\subset\QQ[t].
$$
This proves the classification. When $d$ is even, two examples are
$$
m_{ij}=1,
$$
which gives the polynomial Hopf algebra $\ZZ[t]$, and
$$
m_{ij}=\binom{i+j}{i},
$$
which gives the divided-power Hopf algebra $\Gamma_{\ZZ}[t]$. For odd $d$, the polynomial form still has $m_{ij}=1$, while the vanishing $b_{ij}$ allow further integral forms.

Now fix a prime $p$ and reduce modulo $p$. With $\bar x_n$ denoting the image of $x_n$, every reduction arising from an integral form above has
$$
\bar x_i\bar x_j=\overline{m_{ij}}\,\bar x_{i+j},
$$
$$
\Delta(\bar x_n)
=\sum_{i=0}^n
\overline{\frac{b_{i,n-i}}{m_{i,n-i}}}
\,\bar x_i\otimes\bar x_{n-i}.
$$
Up to a change of generator by a unit in each graded piece, the mod-$p$ Hopf algebra is determined by the $p$-adic valuations
$$
e_{ij}=v_p(m_{ij}).
$$
They satisfy
$$
0\le e_{ij}\le v_p(b_{ij}),
$$
and the additive cocycle relation
$$
e_{ij}+e_{i+j,k}=e_{jk}+e_{i,j+k}.
$$
Here $v_p(0)=\infty$, so a zero coproduct coefficient imposes no upper bound.
Conversely, any such $p$-adic divisor cocycle lifts: take
$$
m_{ij}=p^{e_{ij}}
$$
(and choose valuation $0$ at all other primes), then the preceding integral construction produces a Hopf algebra whose reduction has exactly this structure. Up to rescaling each one-dimensional graded piece by a unit of $\FF_p$, these are precisely the Hopf algebras $A\otimes\FF_p$ that arise.

When $d$ is even, the polynomial and divided-power reductions are the two extreme valuation choices $e_{ij}=0$ and
$$
e_{ij}=v_p\binom{i+j}{i},
$$
while intermediate divisor cocycles give the mixed integral forms.
:::
