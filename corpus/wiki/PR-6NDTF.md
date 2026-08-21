---
schema: qual/card@1
id: PR-6NDTF
kind: proposition
title: Measurable Slices
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Measure Theory
relations: []
review: draft
---

:::{.proposition title="Measurable Slices"}
Let $E$ be a measurable subset of $\RR^n$. Then

- For almost every $x\in \RR^{n_1}$, the slice $E_x \definedas \theset{y \in \RR^{n_2} \mid  (x,y) \in E}$ is measurable in $\RR^{n_2}$.

- The function

\[
F: \RR^{n_1} &\to \RR \\
x &\mapsto m(E_x) = \int_{\RR^{n_2}} \chi_{E_x} ~dy
\]

is measurable and 
\[
m(E) = \int_{\RR^{n_1}} m(E_x) ~dx 
= \int_{\RR^{n_1}} \int_{\RR^{n_2}} \chi_{E_x} ~dy ~dx
.\]

:::
