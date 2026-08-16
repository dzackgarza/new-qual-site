---
schema: qual/card@1
id: P-PUDXH
kind: problem
title: "Let $f, g$ be non-negative measurable functions on $[0, \\infty)$ with"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - fubini-tonelli
  - norms
relations: []
review: draft
---

::: problem
Let $f, g$ be non-negative measurable functions on $[0, \infty)$ with
\[
A &\da \int_0^{\infty } f(y) y^{-1/2} \dy < \infty \\
B &\da \qty{ \int_0^{\infty } \abs{ g(y) } }^2 \dy < \infty  
.\]

Show that
\[
\int_0^{\infty } \qty{ \int_0^{\infty } f(y) \dy } {g(x) \over x} \dx \leq AB
.\]
:::
