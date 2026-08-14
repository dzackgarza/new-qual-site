---
schema: qual/card@1
id: FF-UW3C7
kind: fact
title: 'Is the composition of Lebesgue measurable functions again Lebesgue measurable?'
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - cantor-set
  - counterexamples
relations: []
review: draft
---

::: {.fact title="Is the composition of Lebesgue measurable functions again Lebesgue measurable?"}
**No:** Take $ f: [0, 1]\to [0, 1] $ the Cantor-Lebesgue function (monotonic and cts) and $ C $ the Cantor set

$ f(C) = [0, 1] $, so define $ g(x) = f(x) +x $ so $ g:[0, 1] \to [0, 2] $ (strictly monotonic and cts, so a homeomorphism), so $ g^{-1} $ is cts and thus measurable.

$ \mu(g(C)) = 1>0 $ (because $ f $ is constant on every interval in $ C^c $) so $ g(C) \supseteq A $ a non-measurable subset

$ g^{-1}(A) \subset C $ with $ \mu(C) = 0 $ implies $ g^{-1}(A) $ is a measurable set, so $ \chi_{g^{-1}(A)} $ is a measurable function

Then $ k\coloneqq\chi_{g^{-1}(A)} \circ g^{-1} $ isn't measurable since

$$k^{-1}(1) = \qty{ (g^{-1})^{-1}\circ \chi_{g^{-1}(A)} }(1) = g(g^{-1}(A)) = A.$$

is not a measurable set.
:::
