---
schema: qual/card@1
id: P-CASP05B
kind: problem
title: "Jensen-type inequality for bounded analytic functions with prescribed zeros"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f \in H(\mathbb{D})$, and let $c_1, \ldots, c_n \in \mathbb{D} \setminus \{0\}$ be zeros of $f$ listed with multiplicity not exceeding their multiplicities as zeros of $f$.
Show that if $|f(z)| \leq M$ for $|z| < 1$, then $$|f(0)| \leq M \prod_{j=1}^{n} |c_j|.$$

Hint: Consider the function $g(z) = f(z) / \prod_j \phi_{c_j}(z)$, where $\phi_{c_j}$ is a one-to-one analytic map of $\mathbb{D}$ onto itself vanishing at $c_j$.
:::

::: remark
The official Spring 2005 source does not specify distinctness or multiplicity
for the listed zeros. Under literal repeated enumeration the printed statement
is false; the hypothesis above records the multiplicity condition required by
the supplied Blaschke-product hint.
:::

::: solution
For $c\in\mathbb D$, put
\[
\phi_c(z)=\frac{z-c}{1-\overline c z}.
\]
This is an automorphism of $\mathbb D$, vanishes at $c$, and satisfies
$|\phi_c|=1$ on the unit circle. By the multiplicity hypothesis,
\[
g(z)=\frac{f(z)}{\prod_{j=1}^n\phi_{c_j}(z)}
\]
extends holomorphically across every $c_j$.

Fix $0<r<1$ larger than all $|c_j|$. On $|z|=r$, one can instead use the
finite Blaschke factors after a standard maximum-principle argument on
$\mathbb D$; equivalently, apply the maximum principle to $g$ on disks and
let $r\uparrow1$. Since $|f|\le M$ and $|\phi_{c_j}(e^{it})|=1$, one obtains
\[
|g(z)|\le M\qquad(z\in\mathbb D).
\]
Evaluating at $0$ gives
\[
|g(0)|
=\frac{|f(0)|}{\prod_j|\phi_{c_j}(0)|}
=\frac{|f(0)|}{\prod_j|c_j|}
\le M.
\]
Therefore
\[
\boxed{|f(0)|\le M\prod_{j=1}^n|c_j|}.
\]
:::
