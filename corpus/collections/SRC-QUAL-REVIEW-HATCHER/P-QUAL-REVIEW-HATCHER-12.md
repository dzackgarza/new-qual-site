---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-12
kind: problem
title: The dimension of a manifold is intrinsic
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 12 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Let $M$ be an $n$-manifold.
Prove that $M$ is not a $k$-manifold for any $k\ne n$.
:::

::: {.solution}
Fix
\[
x\in M.
\]

<1>1. Since \(M\) is an \(n\)-manifold, there is an open neighborhood
\[
U\ni x
\]
and a homeomorphism
\[
\phi:U\to V
\]
onto an open set
\[
V\subseteq\mathbb R^n
\]
with
\[
\phi(x)=0.
\]

::: {.proof}
This is the definition of an \(n\)-manifold, after translating the Euclidean chart so that the image of \(x\) is the origin.
:::

<1>2. Excision gives
\[
\boxed{
H_i(M,M\setminus\{x\})
\cong
H_i(U,U\setminus\{x\})}.
\]

::: {.proof}
The complement
\[
M-U
\]
has closure contained in
\[
M\setminus\{x\},
\]
so excising \(M-U\) from the pair
\[
(M,M\setminus\{x\})
\]
gives the displayed isomorphism.
:::

<1>3. Via the chart,
\[
\boxed{
H_i(U,U\setminus\{x\})
\cong
H_i(V,V\setminus\{0\})}.
\]

::: {.proof}
A homeomorphism of pairs induces isomorphisms on relative homology.
:::

<1>4. Shrinking \(V\) if necessary, excision identifies
\[
H_i(V,V\setminus\{0\})
\]
with
\[
H_i(\mathbb R^n,\mathbb R^n\setminus\{0\}).
\]

::: {.proof}
Choose an open ball \(B\) centered at \(0\) with
\[
\overline B\subseteq V.
\]
Excision gives
\[
H_i(V,V\setminus\{0\})
\cong
H_i(B,B\setminus\{0\}),
\]
and the same argument gives
\[
H_i(\mathbb R^n,\mathbb R^n\setminus\{0\})
\cong
H_i(B,B\setminus\{0\}).
\]
:::

<1>5. The space
\[
\mathbb R^n\setminus\{0\}
\]
deformation retracts onto
\[
S^{n-1}.
\]

::: {.proof}
Use radial projection
\[
v\longmapsto\frac{v}{\|v\|}.
\]
:::

<1>6. Since \(\mathbb R^n\) is contractible, the long exact sequence of the pair gives
\[
\boxed{
H_i(\mathbb R^n,\mathbb R^n\setminus\{0\})
\cong
\widetilde H_{i-1}(\mathbb R^n\setminus\{0\})}.
\]

::: {.proof}
For \(i>0\), the absolute homology groups of \(\mathbb R^n\) vanish, so the connecting maps in the long exact sequence are isomorphisms. The reduced formulation also handles the degree-zero edge cleanly.
:::

<1>7. Therefore
\[
H_i(\mathbb R^n,\mathbb R^n\setminus\{0\})
\cong
\widetilde H_{i-1}(S^{n-1}).
\]

::: {.proof}
Apply step <1>5 to step <1>6.
:::

<1>8. Hence
\[
\boxed{
H_i(M,M\setminus\{x\};\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&i=n,\\
0,&i\ne n.
\end{cases}}
\]

::: {.proof}
By steps <1>2--<1>7, the local relative homology is the reduced homology of \(S^{n-1}\), shifted by one degree. The sphere has reduced homology \(\mathbb Z\) only in degree \(n-1\).
:::

Now suppose, toward a contradiction, that \(M\) is also a \(k\)-manifold.

<1>9. Applying the same local-homology calculation using a \(k\)-dimensional chart gives
\[
\boxed{
H_i(M,M\setminus\{x\};\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&i=k,\\
0,&i\ne k.
\end{cases}}
\]

::: {.proof}
Repeat steps <1>1--<1>8 with \(\mathbb R^k\) in place of \(\mathbb R^n\).
:::

<1>10. The local homology group in step <1>8 is nonzero exactly in degree \(n\), while the same group in step <1>9 is nonzero exactly in degree \(k\).

::: {.proof}
Both statements concern the same pair
\[
(M,M\setminus\{x\}),
\]
so both degree descriptions must agree.
:::

<1>11. Therefore
\[
\boxed{n=k}.
\]

::: {.proof}
If \(n\ne k\), then at degree \(i=n\), step <1>8 gives \(\mathbb Z\) while step <1>9 gives \(0\), contradiction.
:::

<1>12. Hence an \(n\)-manifold cannot also be a \(k\)-manifold for any
\[
\boxed{k\ne n}.
\]

::: {.proof}
Step <1>11 shows equality of dimensions is necessary.
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>12 is the required conclusion.
:::
:::
