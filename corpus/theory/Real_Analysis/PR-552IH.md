---
schema: qual/card@1
id: PR-552IH
kind: proposition
title: Measurability under product extension, invertible linear maps and the difference map
slogan: 'A Lebesgue measurable function stays measurable when extended to a product space, composed with an invertible linear map, or composed with the difference map $(x,y)\mapsto x-y$.'
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations:
- kind: related-to
  target: PR-EWXRO
review: draft
---

::: {.proposition}
Throughout, measurable means [[D-DHFN4|Lebesgue measurable]].

- If $f\colon\RR^{d_1}\to[-\infty,\infty]$ is measurable, then $F\colon\RR^{d_1}\times\RR^{d_2}\to[-\infty,\infty]$, $F(x,y)\coloneqq f(x)$, is measurable.

- If $f\colon\RR^d\to[-\infty,\infty]$ is measurable and $T\colon\RR^d\to\RR^d$ is an invertible linear map, then $f\circ T$ is measurable.

- If $f\colon\RR^d\to[-\infty,\infty]$ is measurable, then $(x,y)\mapsto f(x-y)$ is measurable on $\RR^d\times\RR^d$.
:::
