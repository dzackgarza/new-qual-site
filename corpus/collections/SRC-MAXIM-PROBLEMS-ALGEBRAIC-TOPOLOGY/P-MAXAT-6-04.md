---
schema: qual/card@1
id: P-MAXAT-6-04
kind: problem
title: Maxim algebraic topology 6.4
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 4 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that the only real projective spaces which can be parallelizable are P 1 , P 3 and $\mathbb { P } ^ { 7 }$
:::

::: {.solution}
Assume $n>0$. If $\mathbb{RP}^n$ is parallelizable, its tangent bundle is trivial. The key point is that this forces the existence of a real division algebra of dimension $n+1$ in the sense needed by the classical Hopf invariant one theorem.

<1>1. If $\mathbb{RP}^n$ is parallelizable, then its double cover $S^n$ is parallelizable.

::: {.proof}
Let
\[
p:S^n\to\mathbb{RP}^n
\]
be the antipodal covering. Since $p$ is a local diffeomorphism,
\[
TS^n\cong p^*T\mathbb{RP}^n.
\]
The pullback of a trivial bundle is trivial, so parallelizability of $T\mathbb{RP}^n$ implies parallelizability of $TS^n$.
:::

<1>2. By the theorem on parallelizable spheres,
\[
S^n\text{ parallelizable}
\quad\Longrightarrow\quad
n\in\{1,3,7\}.
\]

::: {.proof}
If $S^n$ is parallelizable, it has $n$ pointwise linearly independent tangent vector fields. Together with the radial vector field in $\mathbb R^{n+1}$ these determine a nonsingular bilinear multiplication after the standard clutching construction, equivalently an element of Hopf invariant one. Adams's Hopf invariant one theorem says such an element exists only in dimensions
\[
n=1,3,7
\]
for positive-dimensional spheres. This is the classical theorem that the only parallelizable spheres are $S^0,S^1,S^3,S^7$.
:::

<1>3. Therefore, if $\mathbb{RP}^n$ is parallelizable and $n>0$, then
\[
n\in\{1,3,7\}.
\]

::: {.proof}
Combine steps <1>1 and <1>2.
:::

<1>4. The spaces $\mathbb{RP}^1$, $\mathbb{RP}^3$, and $\mathbb{RP}^7$ are in fact parallelizable.

::: {.proof}
Use the normed real division algebras
\[
\mathbb C,\qquad\mathbb H,\qquad\mathbb O
\]
of real dimensions $2,4,8$. Their unit spheres are respectively
\[
S^1,S^3,S^7.
\]
Fix an orthonormal basis $1,e_1,\ldots,e_n$ of imaginary units. On the unit sphere, the vector fields
\[
V_i(x)=e_i x,
\qquad i=1,\ldots,n,
\]
are tangent and pointwise linearly independent because multiplication by a nonzero element is an invertible linear map and $\langle e_ix,x\rangle=0$ by norm multiplicativity.
:::

<1>5. These framings descend through the antipodal quotient
\[
S^n\to\mathbb{RP}^n
\]
for $n=1,3,7$.

::: {.proof}
Bilinearity gives
\[
V_i(-x)=e_i(-x)=-e_ix=-V_i(x).
\]
The derivative of the antipodal map is also $-I$, so
\[
d(-I)_x(V_i(x))=V_i(-x).
\]
Thus each vector field is equivariant for the deck transformation and descends to a tangent vector field on projective space. Pointwise linear independence is preserved under the covering map, giving a global frame downstairs.
:::

<1>6. Hence
\[
\mathbb{RP}^1,\quad\mathbb{RP}^3,\quad\mathbb{RP}^7
\]
are parallelizable.

::: {.proof}
Step <1>4 constructs global frames upstairs and step <1>5 descends them to the three projective spaces.
:::

<1>7. Therefore
\[
\boxed{
\mathbb{RP}^n\text{ is parallelizable for }n>0
\iff n=1,3,7.}
\]

::: {.proof}
Necessity is step <1>3 and sufficiency is step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 proves the assertion in the problem.
:::
:::
