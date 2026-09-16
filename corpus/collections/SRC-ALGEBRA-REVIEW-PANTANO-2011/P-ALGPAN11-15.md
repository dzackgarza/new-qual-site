---
schema: qual/card@1
id: P-ALGPAN11-15
kind: problem
title: Which listed ring has zero divisors
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the misattached Euclidean-algorithm scan (test 1, problem 33) with a transcription of test 1, problem 40 from ALGEBRA_REVIEW1.pdf page 5.
---

::: {.problem}
For which of the following rings is it possible for the product of two nonzero elements to be zero?

(A) The ring of complex numbers

(B) The ring of integers modulo $11$

(C) The ring of continuous real-valued functions on $[0,1]$

(D) The ring $\{a + b\sqrt{2} : a \text{ and } b \text{ are rational numbers}\}$

(E) The ring of polynomials in $x$ with real coefficients
:::

::: {.solution}
The answer is $\boxed{\text{(C)}}$, the ring $C([0,1],\mathbb R)$ of continuous real-valued functions.

<1>1. Choice (C) has nonzero zero divisors.
::: {.proof}
Define
\[
f(x)=\max\{0,\tfrac12-x\},
\qquad
g(x)=\max\{0,x-\tfrac12\}.
\]
Both are nonzero continuous functions on $[0,1]$, but their supports meet only at $x=1/2$, where both vanish.
Hence
\[
fg=0.
\]
:::

<1>2. The other listed rings are integral domains.
::: {.proof}
$\mathbb C$ is a field; $\mathbb Z/11$ is a field because $11$ is prime; $\mathbb Q(\sqrt2)$ is a field; and $\mathbb R[x]$ is a polynomial ring over a field, hence an integral domain.
None of them has nonzero zero divisors.
:::
:::
