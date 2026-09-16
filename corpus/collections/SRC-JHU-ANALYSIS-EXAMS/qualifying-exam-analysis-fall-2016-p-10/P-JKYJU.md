---
schema: qual/card@1
id: P-JKYJU
kind: problem
title: Zero-count stability when the limit has no boundary zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Fall 2016 problem 6 with the retained source; the missing boundary-nonvanishing hypothesis is necessary, as shown by a zero approaching the unit circle from inside."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the counterexample to the unqualified statement, holomorphy of the limit, the positive minimum on the contour, and equality of finite zero counts with multiplicities."
---

::: {.problem}
Let $U\subset\mathbb C$ be open and contain the closure
$\overline D$ of a unit disk. Suppose holomorphic functions
$f_n:U\to\mathbb C$ converge uniformly on compact subsets
of $U$ to $f$, and assume that $f$ has no zero on $\partial D$.
Prove that for all sufficiently large $n$, the functions
$f_n$ and $f$ have the same number of zeros in $D$, counted
with multiplicity.
:::

::: {.remark}
Boundary nonvanishing cannot be dropped. On the unit disk
centered at zero, $f_n(z)=z-(1-1/n)$ for $n\geq2$ converges
locally uniformly on the plane to $f(z)=z-1$. Each $f_n$
has one zero in the disk, while $f$ has none there; its
zero is on the boundary.
:::

::: {.solution}
<1>1. The limit is holomorphic and has a positive boundary modulus minimum.

::: {.proof}
The local uniform limit theorem makes $f$ holomorphic
on $U$ [@SS03]. Since $f$ is continuous and nonzero on
the compact circle $\partial D$,
$$
\delta:=\min_{z\in\partial D}|f(z)|>0.
$$
In particular $f$ is not identically zero on the component
of $U$ containing $\overline D$. Its zeros in $\overline D$
are finite in number: an infinite set of distinct zeros
would have an accumulation point in this compact subset
of $U$, contradicting the identity theorem [@SS03].
Each zero has finite multiplicity by its Taylor expansion.
:::

<1>2. Uniform convergence on the boundary gives the same zero count.

::: {.proof}
Choose $N$ so that for every $n\geq N$,
$$
\sup_{z\in\partial D}|f_n(z)-f(z)|<\delta.
$$
Then $|f_n-f|<|f|$ throughout $\partial D$. Rouche's
theorem applies, since both functions are holomorphic
on a neighborhood of $\overline D$, and gives equality
of their numbers of zeros in $D$, counting multiplicities
[@SS03]. The same strict inequality shows that $f_n$
is nonzero on the boundary, so its zero count is finite
by the argument in step <1>1. This holds for every
$n\geq N$, as required.
:::
:::
