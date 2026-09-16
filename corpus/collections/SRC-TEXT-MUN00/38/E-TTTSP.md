---
schema: qual/card@1
id: E-TTTSP
kind: problem
title: Compactifications of the minimal uncountable well-ordered set
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Show that every continuous real-valued function defined on $S_\Omega$ is "eventually constant."
[Hint: First prove that for each $\epsilon$, there is an element $\alpha$ of $S_\Omega$ such that $\abs{f(\beta) - f(\alpha)} < \epsilon$ for all $\beta > \alpha$. Then let $\epsilon = 1/n$ for $n \in \mathbb{Z}_+$ and consider the corresponding points $\alpha_n$.]

(b) Show that the one-point compactification of $S_\Omega$ and the Stone-Čech compactification are equivalent.

(c) Conclude that every compactification of $S_\Omega$ is equivalent to the one-point compactification.
:::

::: {.solution}
Write \(S_\Omega=[0,\Omega)\), where \(\Omega\) is the first uncountable ordinal.

(a) We first show that for every \(\varepsilon>0\) there is \(\alpha<\Omega\) such that
\[
|f(\beta)-f(\gamma)|<\varepsilon
\qquad(\beta,\gamma>\alpha).
\]
If not, recursively choose ordinals
\[
\alpha_1<\beta_1<\alpha_2<\beta_2<\cdots<\Omega
\]
with
\[
|f(\alpha_n)-f(\beta_n)|\ge\varepsilon.
\]
The supremum
\[
\lambda=\sup_n\beta_n
\]
is still countable, hence \(\lambda<\Omega\). Both sequences \((\alpha_n)\) and \((\beta_n)\) converge to \(\lambda\) in the order topology, so continuity of \(f\) gives
\[
f(\alpha_n)\to f(\lambda),\qquad f(\beta_n)\to f(\lambda),
\]
contradicting the displayed lower bound.

For each \(n\ge1\), choose \(\alpha_n\) so that the oscillation of \(f\) on \((\alpha_n,\Omega)\) is \(<1/n\). Let
\[
\alpha=\sup_n\alpha_n<\Omega.
\]
If \(\beta,\gamma>\alpha\), then
\[
|f(\beta)-f(\gamma)|<1/n
\]
for every \(n\), hence \(f(\beta)=f(\gamma)\). Thus \(f\) is eventually constant.

(b) Let \(S_\Omega^*=S_\Omega\cup\{\Omega\}\) be the one-point compactification, which is the ordinal interval \([0,\Omega]\). Every bounded continuous real-valued function on \(S_\Omega\) is eventually constant by (a), so it extends continuously to \(\Omega\) by assigning that eventual constant value there. By the Stone--Čech characterization via extension of bounded continuous real-valued functions, \(S_\Omega^*\) is equivalent to \(\beta S_\Omega\).

(c) Let \(Y\) be any compactification of \(S_\Omega\). By maximality of the Stone--Čech compactification there is a continuous surjection
\[
q:\beta S_\Omega\longrightarrow Y
\]
that is the identity on \(S_\Omega\). By (b), \(\beta S_\Omega-S_\Omega\) consists of the single point \(\Omega\). Since \(q\) fixes every point of \(S_\Omega\), surjectivity implies that \(Y-S_\Omega\) has at most one point; it is nonempty because \(S_\Omega\) is not compact. Thus \(Y\) is a one-point compactification. One-point compactifications of locally compact Hausdorff spaces are unique up to equivalence, so every compactification of \(S_\Omega\) is equivalent to \(S_\Omega^*\).
:::
