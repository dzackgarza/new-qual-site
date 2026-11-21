---
schema: qual/card@1
id: P-RASP26E
kind: problem
title: "Meager conull set"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UCSD Spring 2026 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Construct a meager (i.e. first category) subset $E$ of $\RR$ that is conull in $\RR$ with respect to the Lebesgue measure (i.e., $m(\RR \setminus E) = 0$).
:::

::: {.solution}

The construction is the card's own, a countable intersection of dense open sets of small measure; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Enumerate the rationals as $\QQ=\{q_{1},q_{2},\ldots\}$ and for $n\ge1$ put
$$
U_{n}=\bigcup_{k=1}^{\infty}\big(q_{k}-2^{-n-k-2},\,q_{k}+2^{-n-k-2}\big).
$$

::: pf

::: {.pf-step #measure}
Each $U_{n}$ is open and dense, and $m(U_{n})\le2^{-n-1}$.

::: pf-proof
$U_{n}$ is a union of open intervals, hence open; it contains every rational, hence is dense in $\RR$. The $k$-th interval has length $2\cdot2^{-n-k-2}=2^{-n-k-1}$, so by countable subadditivity of Lebesgue measure
$$
m(U_{n})\le\sum_{k=1}^{\infty}2^{-n-k-1}=2^{-n-1}\sum_{k=1}^{\infty}2^{-k}=2^{-n-1}.
$$
:::

:::

::: {.pf-step #null-dense}
$N=\bigcap_{n}U_{n}$ is dense and $m(N)=0$.

::: pf-proof
$\RR$ is a complete metric space and each $U_{n}$ is open and dense, so the Baire category theorem gives that $N$ is dense. For every $n$ one has $N\subset U_{n}$, hence $m(N)\le m(U_{n})\le2^{-n-1}$ by step [](#measure){.pf-ref}; letting $n\to\infty$ gives $m(N)=0$.
:::

:::

::: {.pf-step #meager}
$E=\RR\setminus N$ is meager and conull.

::: pf-proof
$E=\bigcup_{n}(\RR\setminus U_{n})$. Each $\RR\setminus U_{n}$ is closed, and it has empty interior because $U_{n}$ is dense; so each is nowhere dense, and $E$ is a countable union of nowhere dense sets, that is meager. And $m(\RR\setminus E)=m(N)=0$ by step [](#null-dense){.pf-ref}, so $E$ is conull. Hence
$$
\boxed{E=\RR\setminus\bigcap_{n}U_{n}\ \text{is meager and conull}.}
$$
:::

:::

:::
:::
