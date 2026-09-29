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
For $p$ a prime show that the number of non-singular $n \times n$ matrices with entries in the field with p elements has the form $p ^ { r } s$ where $s \equiv ( - 1 ) ^ { n }$ (mod p), and find r.
:::

::: {.solution}

::: pf

::: pf-step
The number of nonsingular $n\times n$ matrices over $\FF_p$ is
$$
\abs{\operatorname{GL}_n(\FF_p)}
=
\prod_{k=0}^{n-1}(p^n-p^k).
$$

::: pf-proof
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

:::

::: {.pf-step #factored-order}
One has
$$
\abs{\operatorname{GL}_n(\FF_p)}
=
p^{n(n-1)/2}
\prod_{j=1}^n(p^j-1).
$$

::: pf-proof
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

:::

::: {.pf-step #s-congruence}
If
$$
s\coloneqq\prod_{j=1}^n(p^j-1),
$$
then
$$
s\equiv(-1)^n\pmod p.
$$

::: pf-proof
For every $j\geq1$,
$$
p^j-1\equiv-1\pmod p.
$$
Multiplying the $n$ congruences gives the claim.
:::

:::

::: {.pf-step #exponent-value}
The required exponent is
$$
\boxed{
r=\frac{n(n-1)}2
}.
$$

::: pf-proof
Step [](#factored-order){.pf-ref} gives the representation
$$
\abs{\operatorname{GL}_n(\FF_p)}
=
p^{n(n-1)/2}s,
$$
and step [](#s-congruence){.pf-ref} gives
$$
s\equiv(-1)^n\pmod p.
$$
In particular $p\nmid s$, so the displayed exponent of $p$ is exact.
:::

:::

::: pf-qed
Steps [](#factored-order){.pf-ref}, [](#s-congruence){.pf-ref} and [](#exponent-value){.pf-ref} give the requested form and determine $r$.
:::

:::

:::
