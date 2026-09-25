---
schema: qual/card@1
id: P-BKS11-8B
kind: problem
title: Order of $\operatorname{GL}_n(\mathbb F_p)$ modulo $p$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 5 of the retained Spring 2011 solution PDF and independently reviewed the ordered-basis count.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the factorization of |GL_n(F_p)|, the exact p-adic exponent, and the residual congruence modulo p.
---

::: {.problem}
For $p \textrm { a }$ prime show that the number of non-singular $n \times n$ matrices with entries in the field with p elements has the form $p ^ { r } s$ where $s \equiv ( - 1 ) ^ { n }$ (mod p), and find r.
:::

::: {.solution}
<1>1. The number of nonsingular $n\times n$ matrices over $\FF_p$ is
$$
\abs{\operatorname{GL}_n(\FF_p)}
=
\prod_{k=0}^{n-1}(p^n-p^k).
$$

::: {.proof}
An invertible matrix is the same thing as an ordered basis of
$\FF_p^n$, given by its columns.

The first column can be any nonzero vector, giving
$$
p^n-1
$$
choices. After $k$ linearly independent columns have been chosen, their
span has $p^k$ elements, so the next column has
$$
p^n-p^k
$$
choices. Multiplying these numbers for $k=0,\ldots,n-1$ gives the stated
formula.
:::

<1>2. One has
$$
\abs{\operatorname{GL}_n(\FF_p)}
=
p^{n(n-1)/2}
\prod_{j=1}^n(p^j-1).
$$

::: {.proof}
For each $k$,
$$
p^n-p^k
=
p^k(p^{n-k}-1).
$$
Therefore
$$
\begin{aligned}
\prod_{k=0}^{n-1}(p^n-p^k)
&=
p^{0+1+\cdots+(n-1)}
\prod_{k=0}^{n-1}(p^{n-k}-1)\\
&=
p^{n(n-1)/2}
\prod_{j=1}^n(p^j-1).
\end{aligned}
$$
:::

<1>3. If
$$
s\coloneqq\prod_{j=1}^n(p^j-1),
$$
then
$$
s\equiv(-1)^n\pmod p.
$$

::: {.proof}
For every $j\geq1$,
$$
p^j-1\equiv-1\pmod p.
$$
Multiplying the $n$ congruences gives the claim.
:::

<1>4. The required exponent is
$$
\boxed{
r=\frac{n(n-1)}2
}.
$$

::: {.proof}
Step <1>2 gives the representation
$$
\abs{\operatorname{GL}_n(\FF_p)}
=
p^{n(n-1)/2}s,
$$
and step <1>3 gives
$$
s\equiv(-1)^n\pmod p.
$$
In particular $p\nmid s$, so the displayed exponent of $p$ is exact.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>2--<1>4 give the requested form and determine $r$.
:::
:::
