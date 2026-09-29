---
schema: qual/card@1
id: P-AGH2314CLOSEDDENSE
kind: problem
title: Closed points are dense in a scheme of finite type over a field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Closed Points
  - Finite Type
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.14 statement and the Jacobson property of finite-type schemes over a field.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
If $X$ is a scheme of finite type over a field, show that the closed points of $X$ are dense.
Give an example to show that this is not true for arbitrary schemes.
:::

::: {.solution}

::: pf

::: {.pf-step #affine-opens-finitely-generated-k-algebra}
Let $X$ be of finite type over a field $k$.  Every affine open
\[
U=\Spec A\subseteq X
\]
has $A$ a finitely generated $k$-algebra.

::: pf-proof
Apply Hartshorne II.3.3(c) to the finite type structure morphism
\[
X\longrightarrow\Spec k.
\]
Since the target is affine, every affine open in $X$ has coordinate ring finitely generated over $k$.
:::

:::

::: {.pf-step #finite-residue-field-implies-closed}
If $x\in X$ has residue field $\kappa(x)$ finite over $k$, then $x$ is a closed point of $X$.

::: pf-proof
Suppose $y$ is a specialization of $x$.  Choose an affine neighborhood
\[
V=\Spec B
\]
of $y$.  Open subsets are stable under generization, so $x\in V$ as well.

Let $\mathfrak p\subseteq B$ be the prime corresponding to $x$.  By step [](#affine-opens-finitely-generated-k-algebra){.pf-ref}, $B$ is a finitely generated $k$-algebra, hence so is $B/\mathfrak p$.  Moreover
\[
B/\mathfrak p\subseteq\kappa(x),
\]
and $\kappa(x)$ is finite-dimensional over $k$.  Therefore $B/\mathfrak p$ is finite-dimensional over $k$.  Being a domain, it is a field.  Thus $\mathfrak p$ is maximal in $B$.

Hence $x$ has no proper specialization inside $V$.  Since $y\in V$ is a specialization of $x$, we obtain $y=x$.  Therefore $x$ has no proper specialization in $X$ and is closed.
:::

:::

::: {.pf-step #nonempty-open-contains-closed-point}
Every nonempty open subset $W\subseteq X$ contains a closed point of $X$.

::: pf-proof
Choose any point of $W$ and an affine neighborhood
\[
U=\Spec A\subseteq W.
\]
The nonzero ring $A$ has a maximal ideal $\mathfrak m$, giving a point $x\in U$.

By step [](#affine-opens-finitely-generated-k-algebra){.pf-ref}, $A$ is a finitely generated $k$-algebra.  Zariski's lemma therefore implies that
\[
\kappa(x)=A/\mathfrak m
\]
is a finite algebraic extension of $k$.  Step [](#finite-residue-field-implies-closed){.pf-ref} now shows that $x$ is closed in all of $X$.
:::

:::

::: {.pf-step #closed-points-dense}
The closed points of $X$ are dense.

::: pf-proof
A subset is dense exactly when every nonempty open subset meets it.  This is precisely step [](#nonempty-open-contains-closed-point){.pf-ref}.
:::

:::

::: {.pf-step #counterexample-dvr}
The conclusion fails for arbitrary schemes.

::: pf-proof
Let
\[
R=k[t]_{(t)}
\]
be the local ring of the affine line at the origin, and put
\[
X=\Spec R.
\]
The only prime ideals of the discrete valuation ring $R$ are
\[
(0)
\qquad\text{and}\qquad
(t).
\]
The only closed point is $(t)$.  Its closure is itself:
\[
\overline{\{(t)\}}=\{(t)\}\ne X.
\]
Thus the set of closed points is not dense.
:::

:::

::: pf-qed
Step [](#closed-points-dense){.pf-ref} proves density for finite-type schemes over a field, and step [](#counterexample-dvr){.pf-ref} gives the requested counterexample.
:::

:::

:::
