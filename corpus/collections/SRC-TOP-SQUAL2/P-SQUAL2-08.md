---
schema: qual/card@1
id: P-SQUAL2-08
kind: problem
title: Invariance of dimension for Euclidean spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Prove that if $\RR^n$ is homeomorphic to $\RR^m$, then $n=m$.
:::

::: {.solution}
Suppose there is a homeomorphism
\[
h:\mathbb R^n\to\mathbb R^m.
\]

<1>1. If \(n=0\), then
\[
\mathbb R^n
\]
is a one-point space.

::: {.proof}
By convention,
\[
\mathbb R^0=\{*\}.
\]
:::

<1>2. If \(n=0\), then necessarily \(m=0\).

::: {.proof}
A space homeomorphic to a one-point space has exactly one point. For every \(m\ge1\), the space \(\mathbb R^m\) has infinitely many points. Thus \(m=0\).
:::

Hence assume
\[
n,m\ge1.
\]

<1>3. Let
\[
p=0\in\mathbb R^n
\]
and set
\[
q=h(p)\in\mathbb R^m.
\]

::: {.proof}
This selects corresponding points under the homeomorphism.
:::

<1>4. The homeomorphism \(h\) restricts to a homeomorphism
\[
\boxed{
\mathbb R^n\setminus\{p\}
\cong
\mathbb R^m\setminus\{q\}}.
\]

::: {.proof}
Since \(h\) is bijective and
\[
h(p)=q,
\]
it carries the complement of \(\{p\}\) exactly onto the complement of \(\{q\}\). The restricted map and its inverse are continuous.
:::

<1>5. Translation gives
\[
\mathbb R^m\setminus\{q\}
\cong
\mathbb R^m\setminus\{0\}.
\]

::: {.proof}
The map
\[
x\longmapsto x-q
\]
is a homeomorphism of \(\mathbb R^m\) sending \(q\) to \(0\).
:::

<1>6. For every \(k\ge1\),
\[
\boxed{
\mathbb R^k\setminus\{0\}
\simeq
S^{k-1}}.
\]

::: {.proof}
Define
\[
H(x,t)
=
\left(
(1-t)+\frac{t}{\|x\|}
\right)x
\]
for \(x\ne0\). The scalar factor is positive, so the homotopy stays in
\[
\mathbb R^k\setminus\{0\}.
\]
At \(t=0\), it is the identity, and at \(t=1\), it sends \(x\) to
\[
x/\|x\|\in S^{k-1}.
\]
Points already on \(S^{k-1}\) remain fixed. Thus this is a deformation retraction.
:::

<1>7. Therefore
\[
\boxed{
\mathbb R^n\setminus\{p\}
\simeq
S^{n-1}}
\]
and
\[
\boxed{
\mathbb R^m\setminus\{q\}
\simeq
S^{m-1}}.
\]

::: {.proof}
For the \(n\)-dimensional space, \(p=0\), so apply step <1>6 directly. For the \(m\)-dimensional space, combine step <1>5 with step <1>6.
:::

<1>8. By steps <1>4 and <1>7,
\[
\boxed{
S^{n-1}\simeq S^{m-1}}.
\]

::: {.proof}
Homeomorphic spaces are homotopy equivalent, and homotopy equivalence is transitive.
:::

<1>9. For every \(r\ge0\),
\[
\widetilde H_j(S^r;\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&j=r,\\
0,&j\ne r.
\end{cases}
\]

::: {.proof}
This is the standard reduced homology computation for spheres.
:::

<1>10. Since homotopy equivalent spaces have isomorphic homology groups,
\[
\widetilde H_j(S^{n-1})
\cong
\widetilde H_j(S^{m-1})
\]
for every \(j\).

::: {.proof}
Apply homotopy invariance of reduced homology to step <1>8.
:::

<1>11. Taking
\[
j=n-1,
\]
one has
\[
\widetilde H_{n-1}(S^{n-1})
\cong
\mathbb Z.
\]

::: {.proof}
Apply step <1>9 with \(r=n-1\).
:::

<1>12. Hence
\[
\widetilde H_{n-1}(S^{m-1})
\cong
\mathbb Z.
\]

::: {.proof}
Use the isomorphism from step <1>10.
:::

<1>13. Therefore
\[
n-1=m-1.
\]

::: {.proof}
By step <1>9, the only degree in which \(S^{m-1}\) has nonzero reduced homology is degree \(m-1\). Step <1>12 shows its reduced homology is nonzero in degree \(n-1\). Hence these degrees are equal.
:::

<1>14. Thus
\[
\boxed{n=m}.
\]

::: {.proof}
Add \(1\) to the equality in step <1>13. The zero-dimensional case was already handled in step <1>2.
:::

<1>15. Q.E.D.

::: {.proof}
Step <1>14 is the required invariance-of-dimension conclusion.
:::
:::
