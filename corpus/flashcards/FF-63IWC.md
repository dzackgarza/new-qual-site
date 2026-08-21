---
schema: qual/card@1
id: FF-63IWC
kind: fact
title: What is equicontinuity? Uniform equicontinuity?
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Metric Spaces
relations: []
review: draft
---

::: {.fact title="What is equicontinuity? Uniform equicontinuity?"}
For $ X, Y $ metric spaces and $ \mathcal{F} $ a family of functions, $ F $ is *equicontinuous at $ x_0 $* $ \iff $ for every $ \varepsilon > 0 $ there exists a $ \delta(\varepsilon, x_0)>0 $ such that

$$x\in B_\delta(x_0) \implies f_i(x) \in B_\varepsilon(f_i(x_0))$$

for all $ f_i \in \mathcal{F} $.

The family $ F $ is *uniformly equicontinuous* $ \iff $ $ \delta(\varepsilon) $ only depends on $ \varepsilon $ and holds for any pair $ x_1, x_2 $ with $ x_1 \in B_\delta(x_2) $.
:::
