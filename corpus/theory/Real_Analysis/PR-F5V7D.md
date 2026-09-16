---
schema: qual/card@1
id: PR-F5V7D
kind: proposition
title: No function $\RR\to\RR$ is discontinuous exactly on the irrationals
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
There is no function $f\colon\RR\to\RR$ whose set of points of discontinuity is $\RR\setminus\QQ$.
:::

::: {.proof}
For $f\colon\RR\to\RR$ and $x\in\RR$, let $\omega_f(x)\coloneqq\inf_{\delta>0}\sup\theset{\abs{f(y)-f(z)} : y,z\in(x-\delta,x+\delta)}$ be the oscillation of $f$ at $x$.
Then $f$ is discontinuous at $x$ if and only if $\omega_f(x)>0$, and each set $F_n\coloneqq\theset{x : \omega_f(x)\geq 1/n}$ is closed: if $\omega_f(x)<1/n$, some interval $(x-\delta,x+\delta)$ has $\sup\abs{f(y)-f(z)}<1/n$ over it, and every point of that interval has oscillation $<1/n$.
Hence the discontinuity set $\bigcup_n F_n$ is an [[D-RPOGQ|$F_\sigma$ set]].

Suppose $\RR\setminus\QQ=\bigcup_n F_n$ with each $F_n$ closed.
Each $F_n$ contains no rational number, so it has empty interior, and $\QQ=\bigcup_{q\in\QQ}\theset{q}$ is a countable union of closed sets with empty interior.
Then $\RR=\bigcup_n F_n\cup\bigcup_{q\in\QQ}\theset{q}$ is a countable union of [[D-2MJRE|nowhere dense]] closed sets, contradicting the Baire category theorem for the complete metric space $\RR$.
:::
