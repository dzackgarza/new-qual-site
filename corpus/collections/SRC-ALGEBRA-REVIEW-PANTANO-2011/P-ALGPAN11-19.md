---
schema: qual/card@1
id: P-ALGPAN11-19
kind: problem
title: Remainders in the Euclidean algorithm for 273 and 110
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
  note: Replaced the misattached pentagram scan (test 1, problem 60, owned by P-ALGPAN11-18) with a transcription of test 1, problem 33, the Euclidean-algorithm question its solution answers, from ALGEBRA_REVIEW1.pdf page 4.
---

::: {.problem}
The Euclidean algorithm is used to find the greatest common divisor (gcd) of two positive integers `a` and `b`.

```text
input(a)
input(b)
while b > 0
begin
  r := a mod b
  a := b
  b := r
end
gcd := a
output(gcd)
```

When the algorithm is used to find the greatest common divisor of `a` $= 273$ and `b` $= 110$, which of the following is the sequence of computed values for `r`?

(A) $2, 26, 1, 0$

(B) $2, 53, 1, 0$

(C) $53, 2, 1, 0$

(D) $53, 4, 1, 0$

(E) $53, 5, 1, 0$
:::

::: {.solution}
The successive remainders are
\[
\boxed{53,4,1,0},
\]
so the answer is $\boxed{\text{(D)}}$.

<1>1. Execute the Euclidean algorithm.
::: {.proof}
\[
273=2\cdot110+53,
\]
so the first remainder is $53$.
Then
\[
110=2\cdot53+4,
\]
so the second is $4$.
Next
\[
53=13\cdot4+1,
\]
and finally
\[
4=4\cdot1+0.
\]
Thus the algorithm computes $r=53,4,1,0$ in order.
:::
:::
