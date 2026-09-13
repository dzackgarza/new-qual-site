---
schema: qual/card@1
id: P-UCLAB13S-02
kind: problem
title: An error bound for Simpson's rule
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
The approximation from Simpson's Rule for $\int_a^b f(x)\,dx$ is
\[
S_{[a,b]}f=
\left[
\frac23 f\!\left(\frac{a+b}{2}\right)
+\frac13\left(\frac{f(a)+f(b)}2\right)
\right](b-a).
\]
If $f$ has continuous derivatives up to order three, prove that
\[
\left|\int_a^b f(x)\,dx-S_{[a,b]}f\right|
\le C(b-a)^4\max_{[a,b]}|f^{(3)}(x)|,
\]
where $C$ does not depend on $f$.
:::
