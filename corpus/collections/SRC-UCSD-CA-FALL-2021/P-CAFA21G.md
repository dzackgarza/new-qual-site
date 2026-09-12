---
schema: qual/card@1
id: P-CAFA21G
kind: problem
title: "Entire functions with modulus 1 on the real line"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Describe all entire functions $f : \mathbb{C} \to \mathbb{C}$ such that for all $z \in \mathbb{R}$ we have $|f(z)| = 1$.
:::

::: solution
Define
\[
f^*(z)=\overline{f(\overline z)}.
\]
This is entire, and for real $x$,
\[
f(x)f^*(x)=|f(x)|^2=1.
\]
By the identity theorem,
\[
f(z)f^*(z)=1
\]
for every $z\in\mathbb C$. Hence $f$ has no zeros.

Because $\mathbb C$ is simply connected, a zero-free entire function has an
entire logarithm: $f=e^g$ for some entire $g$. For real $x$,
$|e^{g(x)}|=1$, so $\operatorname{Re}g(x)=0$. Thus
\[
h=-ig
\]
is entire and real-valued on $\mathbb R$, and
\[
f(z)=e^{ih(z)}.
\]
Conversely, every entire $h$ with $h(\mathbb R)\subset\mathbb R$ gives an
entire function $e^{ih}$ of modulus $1$ on the real axis. Therefore the full
class is
\[
\boxed{f(z)=e^{ih(z)},\qquad h\text{ entire and }h(\mathbb R)\subset\mathbb R.}
\]
:::
