---
schema: qual/card@1
id: FF-IAUQG
kind: fact
title: "What is the $M{\\hbox{-}}$test?"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - series-of-functions
relations: []
review: draft
---

::: {.fact title="What is the $ M{\hbox{-}} $test?"}
$ \sum_{n\geq 0} {\left\lVert {f_n} \right\rVert}_{\infty, A} < \infty \implies \sum f_n $ converges absolutely and uniformly on $ A $.

Here $ {\left\lVert {f_n} \right\rVert}_{\infty, A}\coloneqq\sup_{x\in A}{\left\lvert {f_n(x)} \right\rvert} $.

Equivalently, if there is a sequence $ \left\{{M_n}\right\} $ where $ {\left\lvert {f_n(x)} \right\rvert} \leq M_n $ for all $ x\in A $ and $ \sum M_n < \infty $.
:::
