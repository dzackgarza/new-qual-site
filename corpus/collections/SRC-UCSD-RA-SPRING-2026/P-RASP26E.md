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

::: problem
Construct a meager (i.e. first category) subset $E$ of $\mathbb{R}$ that is conull in $\mathbb{R}$ with respect to the Lebesgue measure (i.e., $m(\mathbb{R} \setminus E) = 0$).
:::

::: solution
Enumerate the rationals as
\[
\mathbb Q=\{q_1,q_2,\ldots\}.
\]
For each $n\ge1$, define
\[
U_n:=\bigcup_{k=1}^\infty
\left(q_k-2^{-n-k-2},\ q_k+2^{-n-k-2}\right).
\]

Each $U_n$ is open and dense because it contains every rational number. Also
\[
m(U_n)
\le\sum_{k=1}^\infty 2^{-n-k-1}
=2^{-n-1}.
\]

Set
\[
N:=\bigcap_{n=1}^\infty U_n.
\]
Since every $U_n$ is open and dense, the Baire Category Theorem implies that $N$ is dense. Moreover,
\[
m(N)\le m(U_n)\le2^{-n-1}
\]
for every $n$, hence
\[
m(N)=0.
\]

Now put
\[
E:=\mathbb R\setminus N.
\]
Then
\[
m(\mathbb R\setminus E)=m(N)=0,
\]
so $E$ is conull.

On the other hand,
\[
E=\bigcup_{n=1}^\infty(\mathbb R\setminus U_n).
\]
Each $\mathbb R\setminus U_n$ is closed and has empty interior because $U_n$ is dense. Hence each is nowhere dense. Therefore $E$ is a countable union of nowhere dense sets, i.e.
\[
\boxed{E\text{ is meager and conull}.}
\]
:::
