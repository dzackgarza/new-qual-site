---
schema: qual/card@1
id: P-ARTALG-JU03-8
kind: problem
title: 'Abelian groups of order $720$ and cancellation for finitely generated $\ZZ$-modules'
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the order 720 and the finite-generation and direct-sum hypotheses with July 2003 problem 8 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Enumerated every partition of 4 and 2, checked uniqueness rather than relying only on group exponents, and canceled all free-rank and prime-power multiplicity invariants."
---

::: {.problem}
(a) How many abelian groups of order 720 are there?

(b) Let $L, M, N$ be finitely generated $\mathbb{Z}$-modules, such that $L \oplus M \cong L \oplus N$.
Prove that $M \cong N$.
:::

::: {.solution}
Write $C_m=\mathbb Z/m\mathbb Z$ as an additive group.

<1>1. A finitely generated abelian group $A$ has a decomposition
$$
A\cong\mathbb Z^{r_A}\oplus
\bigoplus_{p\ \mathrm{prime}}\ \bigoplus_{e\geq1}
(C_{p^e})^{m_A(p,e)},
$$
where $r_A$ and all $m_A(p,e)$ are nonnegative integers and only
finitely many multiplicities are nonzero. These integers are
uniquely determined by $A$. This is the elementary-divisor form
of the structure theorem for finitely generated abelian groups
[@DF04]. In particular, equality of all these invariants is
equivalent to isomorphism.

<1>2. There are exactly $10$ abelian groups of order $720$, up to
isomorphism.

::: {.proof}
Since $720=2^4\cdot3^2\cdot5$, finiteness forces $r_A=0$,
and the exponents of the cyclic factors for each prime must sum
to that prime's exponent in $720$.

The partitions of $4$ are exactly
$$
(4),\quad(3,1),\quad(2,2),\quad(2,1,1),\quad(1,1,1,1).
$$
Indeed, a largest part of $4$ or $3$ leaves respectively $0$ or
$1$; a largest part of $2$ leaves either another $2$ or two
$1$'s; and otherwise every part is $1$.
They give the five possible $2$-primary groups
$$
C_{16},\quad C_8\oplus C_2,\quad C_4\oplus C_4,\quad
C_4\oplus C_2\oplus C_2,\quad C_2^{\oplus4}.
$$
The only partitions of $2$ are $(2)$ and $(1,1)$, giving
$C_9$ and $C_3\oplus C_3$ as the two possible $3$-primary groups.
The $5$-primary group must be $C_5$.

Taking one of the five groups in the first list, one of the two
in the second, and their direct sum with $C_5$ gives
$5\cdot2=10$ groups, each of order $16\cdot9\cdot5=720$.
Step <1>1 proves that this list is exhaustive and that distinct
choices are nonisomorphic, since they give different prime-power
multiplicities.
:::

<1>3. Finitely generated $\mathbb Z$-modules admit cancellation
of a common direct summand.

::: {.proof}
Apply step <1>1 to $L,M,N$. Combining their decompositions shows
that direct sums add the free ranks and every prime-power
multiplicity. Thus the isomorphism $L\oplus M\cong L\oplus N$
and uniqueness give
$$
r_L+r_M=r_L+r_N,
$$
and, for every prime $p$ and positive integer $e$,
$$
m_L(p,e)+m_M(p,e)=m_L(p,e)+m_N(p,e).
$$
All these numbers are finite nonnegative integers. Subtracting
the common terms gives $r_M=r_N$ and
$m_M(p,e)=m_N(p,e)$ for all $p,e$. Matching the summands in
the two decompositions now gives $M\cong N$.
An additive-group isomorphism is $\mathbb Z$-linear because it
preserves integer multiples, so this is the required module
isomorphism.
:::
:::
