---
schema: qual/card@1
id: P-MAXAT-6-04
kind: problem
title: Only $\RP^1$, $\RP^3$ and $\RP^7$ can be parallelizable
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
Show that the only real projective spaces which can be parallelizable are $\RP^{1}$, $\RP^{3}$ and $\RP^{7}$.
:::

::: {.solution}

Assume $n>0$. If $\RP^n$ is parallelizable, its tangent bundle is trivial. The key point is that this forces the existence of a real division algebra of dimension $n+1$ in the sense needed by the classical Hopf invariant one theorem.

::: pf

::: {.pf-step #s1-1}

If $\RP^n$ is parallelizable, then its double cover $S^n$ is parallelizable.


::: pf-proof

Let
$$
p:S^n\to\RP^n
$$
be the antipodal covering. Since $p$ is a local diffeomorphism,
$$
TS^n\cong p^*T\RP^n.
$$
The pullback of a trivial bundle is trivial, so parallelizability of $T\RP^n$ implies parallelizability of $TS^n$.

:::

:::

::: {.pf-step #s1-2}

By the theorem on parallelizable spheres,
$$
S^n\text{ parallelizable}
\quad\Longrightarrow\quad
n\in\{1,3,7\}.
$$


::: pf-proof

If $S^n$ is parallelizable, it has $n$ pointwise linearly independent tangent vector fields. Together with the radial vector field in $\RR^{n+1}$ these determine a nonsingular bilinear multiplication after the standard clutching construction, equivalently an element of Hopf invariant one. Adams's Hopf invariant one theorem says such an element exists only in dimensions
$$
n=1,3,7
$$
for positive-dimensional spheres. This is the classical theorem that the only parallelizable spheres are $S^0,S^1,S^3,S^7$.

:::

:::

::: {.pf-step #s1-3}

Therefore, if $\RP^n$ is parallelizable and $n>0$, then
$$
n\in\{1,3,7\}.
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The spaces $\RP^1$, $\RP^3$, and $\RP^7$ are in fact parallelizable.


::: pf-proof

Use the normed real division algebras
$$
\CC,\qquad\quaternions,\qquad\octonions
$$
of real dimensions $2,4,8$. Their unit spheres are respectively
$$
S^1,S^3,S^7.
$$
Fix an orthonormal basis $1,e_1,\ldots,e_n$ of imaginary units. On the unit sphere, the vector fields
$$
V_i(x)=e_i x,
\qquad i=1,\ldots,n,
$$
are tangent and pointwise linearly independent because multiplication by a nonzero element is an invertible linear map and $\langle e_ix,x\rangle=0$ by norm multiplicativity.

:::

:::

::: {.pf-step #s1-5}

These framings descend through the antipodal quotient
$$
S^n\to\RP^n
$$
for $n=1,3,7$.


::: pf-proof

Bilinearity gives
$$
V_i(-x)=e_i(-x)=-e_ix=-V_i(x).
$$
The derivative of the antipodal map is also $-I$, so
$$
d(-I)_x(V_i(x))=V_i(-x).
$$
Thus each vector field is equivariant for the deck transformation and descends to a tangent vector field on projective space. Pointwise linear independence is preserved under the covering map, giving a global frame downstairs.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\RP^1,\quad\RP^3,\quad\RP^7
$$
are parallelizable.


::: pf-proof

Step [](#s1-4){.pf-ref} constructs global frames upstairs and step [](#s1-5){.pf-ref} descends them to the three projective spaces.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\RP^n\text{ is parallelizable for }n>0
\iff n=1,3,7.}
$$


::: pf-proof

Necessity is step [](#s1-3){.pf-ref} and sufficiency is step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves the assertion in the problem.

:::

:::

:::
