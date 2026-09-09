---
schema: qual/card@1
id: E-HAT-3.2-3
kind: problem
title: Hatcher Section 3.2 Exercise 3
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

# E-HAT-3.2-3

(a) Using the cup product structure, show there is no map $\mathbb{RP}^n \to \mathbb{RP}^m$ inducing a nontrivial map $H^1(\mathbb{RP}^m; \mathbb{Z}_2) \to H^1(\mathbb{RP}^n; \mathbb{Z}_2)$ if $n > m$.
What is the corresponding result for maps $\mathbb{CP}^n \to \mathbb{CP}^m$?

(b) Prove the Borsuk–Ulam theorem by the following argument.
Suppose on the contrary that $f: S^n \to \mathbb{R}^n$ satisfies $f(x) \neq f(-x)$ for all $x$.
Then define $g: S^n \to S^{n-1}$ by $g(x) = \bigl(f(x) - f(-x)\bigr) / \bigl|f(x) - f(-x)\bigr|$, so $g(-x) = -g(x)$ and $g$ induces a map $\mathbb{RP}^n \to \mathbb{RP}^{n-1}$.
Show that part (a) applies to this map.

::: {.solution}
With $\mathbb Z_2$ coefficients,
\[
H^*(\mathbb{RP}^r;\mathbb Z_2)\cong
\mathbb Z_2[\alpha]/(\alpha^{r+1}),\qquad |\alpha|=1.
\]
Suppose $f:\mathbb{RP}^n\to\mathbb{RP}^m$ with $n>m$ induces a nonzero map on $H^1$. Since both $H^1$ groups are one-dimensional, if $\alpha_m,\alpha_n$ denote the generators then
\[
f^*(\alpha_m)=\alpha_n.
\]
Hence
\[
0=f^*(\alpha_m^{m+1})=\alpha_n^{m+1},
\]
contradicting $m+1\le n$, since $\alpha_n^{m+1}\ne0$. Thus every such map is zero on $H^1$.

Similarly
\[
H^*(\mathbb{CP}^r;\mathbb Z)\cong
\mathbb Z[\beta]/(\beta^{r+1}),\qquad |\beta|=2.
\]
If $n>m$ and $f:\mathbb{CP}^n\to\mathbb{CP}^m$ has $f^*(\beta_m)=d\beta_n$, then
\[
0=f^*(\beta_m^{m+1})=d^{m+1}\beta_n^{m+1}.
\]
Since $H^{2m+2}(\mathbb{CP}^n;\mathbb Z)$ is torsion-free and $\beta_n^{m+1}\ne0$, this forces $d=0$. Hence $f^*:H^2\to H^2$ is zero.

For Borsuk--Ulam, suppose $f:S^n\to\mathbb R^n$ satisfies $f(x)\ne f(-x)$ for all $x$. Then
\[
g(x)=\frac{f(x)-f(-x)}{|f(x)-f(-x)|}
\]
defines an antipodal-equivariant map $g:S^n\to S^{n-1}$, so it descends to
\[
\bar g:\mathbb{RP}^n\to\mathbb{RP}^{n-1}.
\]
The map $\bar g$ is nontrivial on $H^1(-;\mathbb Z_2)$: on fundamental groups it sends the nontrivial loop in $\mathbb{RP}^n$ to the nontrivial loop in $\mathbb{RP}^{n-1}$, because an equivariant lift joins antipodal endpoints upstairs. This contradicts the first part with $m=n-1$. Therefore some $x$ satisfies $f(x)=f(-x)$.
:::
