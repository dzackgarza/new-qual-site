---
schema: qual/card@1
id: P-UCLAB18F-12
kind: problem
title: An operator preserving every hyperplane is scalar
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $V$ be finite-dimensional and let $T:V\to V$ be linear.
Suppose $T(W)\subseteq W$ for every subspace $W\subset V$ with $\dim W=\dim V-1$.
Prove that $T$ is a scalar multiple of the identity.
:::

::: {.solution}
Let
\[
n=\dim V.
\]

<1>1. If $n\le1$, then $T$ is a scalar multiple of the identity.

::: {.proof}
If $n=0$, there is only the zero endomorphism.
If $n=1$, every endomorphism is multiplication by a scalar.
:::

<1>2. Assume $n\ge2$.
For every nonzero $v\in V$,
\[
\bigcap_{\substack{W\subset V\\ \dim W=n-1\\ v\in W}}W
=
\operatorname{span}\{v\}.
\]

::: {.proof}
The line
\[
\operatorname{span}\{v\}
\]
is contained in every hyperplane $W$ containing $v$, so it is contained in the intersection.

Conversely, let
\[
u\notin\operatorname{span}\{v\}.
\]
Since $u,v$ are linearly independent, extend them to a basis
\[
v,u,e_3,\ldots,e_n
\]
of $V$.
Define a linear functional
\[
\varphi:V\to\mathbb F
\]
by
\[
\varphi(v)=0,
\qquad
\varphi(u)=1,
\qquad
\varphi(e_j)=0
\quad
(j\ge3).
\]
Then
\[
W=\ker\varphi
\]
is a hyperplane containing $v$ but not $u$.
Thus $u$ is not in the intersection of all such hyperplanes.
Hence the intersection is exactly $\operatorname{span}\{v\}$.
:::

<1>3. Every one-dimensional subspace of $V$ is invariant under $T$.

::: {.proof}
Fix nonzero
\[
v\in V.
\]
If $W$ is any hyperplane containing $v$, the hypothesis gives
\[
T(W)\subseteq W.
\]
Since
\[
v\in W,
\]
it follows that
\[
Tv\in W.
\]
This holds for every hyperplane containing $v$.
Therefore
\[
Tv
\in
\bigcap_{\substack{W\subset V\\ \dim W=n-1\\ v\in W}}W.
\]
By step <1>2,
\[
Tv\in\operatorname{span}\{v\}.
\]
Thus the line spanned by $v$ is invariant.
:::

<1>4. Every nonzero vector is an eigenvector of $T$.

::: {.proof}
By step <1>3, for each nonzero $v$ there exists a scalar $\lambda_v$ such that
\[
Tv=\lambda_vv.
\]
:::

<1>5. If $u,v$ are linearly independent, then
\[
\lambda_u=\lambda_v.
\]

::: {.proof}
By step <1>4,
\[
Tu=\lambda_uu,
\qquad
Tv=\lambda_vv.
\]
The vector
\[
u+v
\]
is nonzero, so step <1>4 also gives
\[
T(u+v)=\lambda_{u+v}(u+v).
\]
By linearity,
\[
\lambda_uu+\lambda_vv
=
\lambda_{u+v}u+\lambda_{u+v}v.
\]
Since $u$ and $v$ are linearly independent,
\[
\lambda_u=\lambda_{u+v}=\lambda_v.
\]
:::

<1>6. There is a single scalar $\lambda$ such that
\[
Tv=\lambda v
\]
for every $v\in V$.

::: {.proof}
Choose any nonzero
\[
u\in V
\]
and set
\[
\lambda=\lambda_u.
\]
Let $v\ne0$.
If $v$ is linearly independent of $u$, step <1>5 gives
\[
\lambda_v=\lambda.
\]
If $v$ is linearly dependent on $u$, then
\[
v=cu
\]
for some nonzero scalar $c$, and
\[
Tv=cTu=c\lambda u=\lambda v.
\]
The zero vector also satisfies
\[
T0=\lambda0.
\]
:::

<1>7. Therefore
\[
\boxed{T=\lambda I}.
\]

::: {.proof}
Step <1>6 says that $T$ and $\lambda I$ agree on every vector of $V$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>1 handles dimensions at most one, and steps <1>2--<1>7 prove the result for $n\ge2$.
:::
:::
