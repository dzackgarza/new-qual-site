---
schema: qual/card@1
id: E-SS5.EX-7
kind: problem
title: Convergence of $\prod(1+a_n)$ compared with $\sum a_n$
classification:
  areas:
  - complex-analysis
  topics:
  - Infinite Products
  - Convergence Tests
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Split this exercise from source bleed in E-SS5.EX-6 and added the necessary exclusion of zero factors in part (a).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose argument into numbered steps without changing the mathematics, and
    re-checked each step against the definitions and theorems it invokes. What was not checked: no
    copy of Stein and Shakarchi and no solution set for it is retained in tmp/sources (the
    collection provenance is the Google Books ISBN link), so the printed statement and page were
    not re-read; the exercise number is the one the collection index records. No published
    solution is transcribed; the argument remains the card's own, as its solution section says.
---

::: {.exercise}
Establish the following properties of infinite products.

(a) Suppose $a_n\neq -1$ for every $n$. Show that if $\sum \abs{a_n}^2$ converges, then the product $\prod (1+a_n)$ converges to a non-zero limit if and only if $\sum a_n$ converges.

(b) Find an example of a sequence of complex numbers $\{a_n\}$ such that $\sum a_n$ converges but $\prod(1+a_n)$ diverges.

(c) Also find an example such that $\prod(1+a_n)$ converges to a non-zero limit and $\sum a_n$ diverges.
:::

::: {.solution}

The argument is the card's own: the book is retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, and no published solution set of this exercise is retained, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 5, Exercise 7. Here $a_n\neq-1$ for every $n$, so no factor $1+a_n$ vanishes; the principal logarithm is used once $\abs{a_n}<1$, and the expansion $\log(1+a)=\sum_{k\geq1}(-1)^{k+1}a^{k}/k$ then gives $\log(1+a)=a+O(\abs{a}^{2})$ with an absolute constant.

::: pf

::: {.pf-step #log}

If $\sum\abs{a_n}^{2}$ converges then $a_n\to0$, so for $n\geq N$ one has $\abs{a_n}\leq1/2$ and $\log(1+a_n)=a_n+O(\abs{a_n}^{2})$.

::: pf-proof

Terms of a convergent series tend to $0$; on $\abs{a}\leq1/2$ the principal branch of the logarithm is holomorphic and its Taylor series gives $\log(1+a)-a=\sum_{k\geq2}(-1)^{k+1}a^{k}/k$, whose modulus is at most $\abs{a}^{2}\sum_{k\geq2}2^{-(k-2)}=C\abs{a}^{2}$.

:::

:::

::: {.pf-step #a}

(a) $\prod(1+a_n)$ converges to a nonzero limit if and only if $\sum a_n$ converges.

::: pf-proof

A product $\prod(1+a_n)$ with no zero factor converges to a nonzero limit exactly when the series $\sum\log(1+a_n)$ of principal logarithms converges, the partial products being the exponentials of its partial sums. By step [](#log){.pf-ref} the difference $\log(1+a_n)-a_n$ is $O(\abs{a_n}^{2})$, and $\sum\abs{a_n}^{2}<\infty$ by hypothesis; adding an absolutely convergent series does not change convergence, so $\sum\log(1+a_n)$ converges exactly when $\sum a_n$ does.

:::

:::

::: {.pf-step #b}

(b) $a_n=(-1)^{n}/\sqrt{n}$ has $\sum a_n$ convergent and $\prod(1+a_n)$ divergent.

::: pf-proof

The alternating series test applies since $1/\sqrt{n}$ decreases to $0$, so $\sum a_n$ converges. Here $\log(1+a_n)=a_n-\frac{a_n^{2}}{2}+O(\abs{a_n}^{3})$, and $\sum\abs{a_n}^{3}=\sum n^{-3/2}$ converges while $\sum a_n^{2}=\sum\frac1n$ diverges; hence the partial sums of $\log(1+a_n)$ tend to $-\infty$, and the partial products, being their exponentials, tend to $0$.

:::

:::

::: {.pf-step #c}

(c) $b_n=(-1)^{n}/\sqrt{n}$ and $a_n=e^{b_n}-1$ have $\prod(1+a_n)$ convergent to a nonzero limit and $\sum a_n$ divergent.

::: pf-proof

Since $1+a_n=e^{b_n}$, the $N$-th partial product is $\exp(\sum_{n\leq N}b_n)$, which converges to $\exp(\sum b_n)\neq0$ because $\sum b_n$ converges. Also $a_n=b_n+\frac{b_n^{2}}{2}+O(\abs{b_n}^{3})$, and $\sum b_n$ and $\sum\abs{b_n}^{3}$ converge while $\frac12\sum b_n^{2}=\frac12\sum\frac1n$ diverges to $+\infty$; so $\sum a_n$ diverges.

:::

:::

:::

:::
