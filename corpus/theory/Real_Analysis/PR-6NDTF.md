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

:::{.proposition}
Let $E$ be a Lebesgue measurable subset of $\RR^n$, where $n=n_1+n_2$. Then

- For almost every $x\in \RR^{n_1}$, the slice $E_x \definedas \theset{y \in \RR^{n_2} \mid  (x,y) \in E}$ is measurable in $\RR^{n_2}$.

- For almost every $x$, define the slice integral by

\[
F: \RR^{n_1} &\to [0,+\infty] \\
x &\mapsto m(E_x) = \int_{\RR^{n_2}} \chi_{E_x} ~dy
\]

The value $+\infty$ is allowed. Setting $F=0$ on the exceptional null set gives a measurable function on all of $\RR^{n_1}$, and 
\[
m(E) = \int_{\RR^{n_1}} F(x) ~dx 
= \int_{\RR^{n_1}} \int_{\RR^{n_2}} \chi_{E_x} ~dy ~dx
.\]

:::
