---
schema: qual/card@1
id: O-UGA-RA-2018-B-04
kind: occurrence
title: UGA Real Analysis 2018, problem 4
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - integrals
relations:
- kind: instance-of
  target: P-55AME
review: draft
payload:
  source: SRC-UGA-RA-2018-B
  locator: '4'
---

::: problem
Let $f\in L^1([0, 1])$.
Prove that
$$
\lim_{n \to \infty} \int_{0}^{1} f(x) \abs{\sin n x} ~d x= \frac{2}{\pi} \int_{0}^{1} f(x) ~d x
$$

> Hint: Begin with the case that $f$ is the characteristic function of an interval.
:::
