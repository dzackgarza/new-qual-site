---
schema: qual/card@1
id: P-AGH2217AFFINECRIT
kind: problem
title: A criterion for affineness via distinguished opens generating the unit ideal
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Affineness Criteria
  - Isomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.17 statement and the immediately preceding II.2.16 localization result.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
a. Let $f: X \to Y$ be a morphism of schemes, and suppose that $Y$ can be covered by open subsets $U_i$ such that for each $i$ the induced map $f\inv(U_i) \to U_i$ is an isomorphism.
Then $f$ is an isomorphism.

b. A scheme $X$ is affine if and only if there is a finite set of elements $f_1, \ldots, f_r \in A = \Gamma(X, \OO_X)$ such that the open subsets $X_{f_i}$ are affine and $f_1, \ldots, f_r$ generate the unit ideal in $A$.
:::

::: {.remark}
Part (b) uses Hartshorne II.2.4 and II.2.16(d).
:::

::: {.solution}
<1>1. Under the hypotheses of part (a), the local inverses
\[
g_i:U_i\longrightarrow f^{-1}(U_i)
\]
glue to a morphism
\[
g:Y\longrightarrow X.
\]
::: {.proof}
For each $i$, the restriction
\[
f_i=f|_{f^{-1}(U_i)}:f^{-1}(U_i)\longrightarrow U_i
\]
is an isomorphism, so let $g_i=f_i^{-1}$.

On $U_i\cap U_j$, both $g_i$ and $g_j$ are inverse to the restriction
\[
f:f^{-1}(U_i\cap U_j)\longrightarrow U_i\cap U_j.
\]
Hence they agree.  Morphisms of schemes glue uniquely on an open cover of the source, so the $g_i$ determine a morphism $g:Y\to X$.
:::

<1>2. The morphism $g$ is inverse to $f$; therefore $f$ is an isomorphism.
::: {.proof}
On every $U_i$,
\[
(f\circ g)|_{U_i}=f_i\circ g_i=\id_{U_i},
\]
so $f\circ g=\id_Y$.  Likewise the opens $f^{-1}(U_i)$ cover $X$, and
\[
(g\circ f)|_{f^{-1}(U_i)}=g_i\circ f_i=\id_{f^{-1}(U_i)}.
\]
Thus $g\circ f=\id_X$.
:::

<1>3. If $X$ is affine, then the condition in part (b) holds.
::: {.proof}
Write $X=\Spec A$ and take $f_1=1\in A$.  Then $X_{f_1}=X$ is affine and $f_1$ generates the unit ideal.
:::

<1>4. Conversely, suppose that
\[
A=\Gamma(X,\mathcal O_X)
\]
contains elements $f_1,\ldots,f_r$ such that each $X_{f_i}$ is affine and the $f_i$ generate the unit ideal.  Then the $X_{f_i}$ cover $X$.
::: {.proof}
Choose $a_i\in A$ with
\[
\sum_i a_if_i=1.
\]
If a point $x\in X$ lay outside every $X_{f_i}$, then every germ $(f_i)_x$ would lie in the maximal ideal $\mathfrak m_x\subseteq\mathcal O_{X,x}$.  Passing the displayed identity to the stalk would give
\[
1=\sum_i(a_i)_x(f_i)_x\in\mathfrak m_x,
\]
which is impossible.  Hence the $X_{f_i}$ cover $X$.
:::

<1>5. The finite affine cover $\{X_{f_i}\}$ satisfies the hypothesis of Hartshorne II.2.16(c).
::: {.proof}
For all $i,j$,
\[
X_{f_i}\cap X_{f_j}=X_{f_if_j}.
\]
Inside the affine scheme $X_{f_i}$ this is the distinguished open where $f_j|_{X_{f_i}}$ is invertible.  Hence it is affine, and in particular quasi-compact.
:::

<1>6. Let
\[
\eta:X\longrightarrow\Spec A
\]
be the canonical morphism corresponding under Hartshorne II.2.4 to the identity homomorphism $A\to A$.  Then
\[
\eta^{-1}(D(f_i))=X_{f_i}
\]
for every $i$.
::: {.proof}
For $x\in X$, the prime ideal corresponding to $\eta(x)$ is
\[
\{a\in A:a_x\in\mathfrak m_x\}.
\]
Therefore
\[
\eta(x)\in D(f_i)
\iff
(f_i)_x\notin\mathfrak m_x
\iff
x\in X_{f_i}.
\]
:::

<1>7. For every $i$, the restriction
\[
\eta_i:X_{f_i}\longrightarrow D(f_i)
\]
is an isomorphism.
::: {.proof}
By <1>5, Hartshorne II.2.16(d) applies to $X$, so
\[
\Gamma(X_{f_i},\mathcal O_X)\cong A_{f_i}.
\]
By II.2.1,
\[
D(f_i)\cong\Spec A_{f_i}.
\]
Since $X_{f_i}$ is affine,
\[
X_{f_i}
\cong
\Spec\Gamma(X_{f_i},\mathcal O_X)
\cong
\Spec A_{f_i}
\cong
D(f_i).
\]
Under these identifications, $\eta_i$ is induced by the localization map $A_{f_i}\to\Gamma(X_{f_i},\mathcal O_X)$, which is the isomorphism above.  Hence $\eta_i$ is an isomorphism.
:::

<1>8. The distinguished opens $D(f_1),\ldots,D(f_r)$ cover $\Spec A$.
::: {.proof}
Their complement is
\[
V(f_1,\ldots,f_r).
\]
Since the $f_i$ generate the unit ideal, this is
\[
V(1)=\varnothing.
\]
:::

<1>9. The canonical morphism $\eta:X\to\Spec A$ is an isomorphism.  Consequently $X$ is affine.
::: {.proof}
By <1>8, the $D(f_i)$ cover $\Spec A$.  By <1>6 and <1>7, for every $i$ the induced map
\[
\eta^{-1}(D(f_i))=X_{f_i}\longrightarrow D(f_i)
\]
is an isomorphism.  Part (a), proved in <1>1--<1>2, therefore shows that $\eta$ is an isomorphism.
:::

<1>10. Hence
\[
\boxed{
X\text{ is affine}
\iff
\begin{array}{c}
\text{there exist finitely many }f_i\in\Gamma(X,\mathcal O_X)\\
\text{generating the unit ideal such that every }X_{f_i}\text{ is affine.}
\end{array}
}
\]
::: {.proof}
The forward implication is <1>3 and the reverse implication is <1>4--<1>9.
:::

<1>11. Q.E.D.
::: {.proof}
Steps <1>1--<1>2 prove part (a), and steps <1>3--<1>10 prove part (b).
:::
:::
