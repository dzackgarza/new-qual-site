---
schema: qual/card@1
id: FF-WV2QN
kind: fact
title: 'What is Young''s inequality?'
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - lp-spaces
  - norms
relations: []
review: draft
---

::: {.fact title="What is Young's inequality?"}
For $ 1\leq p, q\leq r \leq \infty $ with $ {1\over p} + {1\over q} - {1\over r} = 1 $, then

$${\left\lVert {f\ast g} \right\rVert}_r \leq {\left\lVert {f} \right\rVert}_p {\left\lVert {g} \right\rVert}_q$$

Useful cases:

$$\begin{aligned} \|f * g\|_1 & \leq\|f\|_1\|g\|_1 \\ \|f * g\|_p & \leq\|f\|_1\|g\|_p \\ \|f * g\|_{\infty} & \leq\|f\|_p\|g\|_q \\ \|f * g\|_{\infty} & \leq\|f\|_2\|g\|_2\end{aligned}$$
:::
