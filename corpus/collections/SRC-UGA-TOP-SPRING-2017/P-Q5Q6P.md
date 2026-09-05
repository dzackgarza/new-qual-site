---
schema: qual/card@1
id: P-Q5Q6P
kind: problem
title: The torus $S^1\times S^1$ is not a union of two disks
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Products
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement and its explicit warning about arbitrary disk intersection against problem 3 of the official UGA Spring 2017 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the relative cup-product obstruction after replacing each embedded closed disk by a contractible open collar neighborhood; the argument makes no assumption on the intersection of the two disks.
---

::: problem
Show that $S^1 \times S^1$ is not the union of two disks (where there is no assumption that the disks intersect along their boundaries).
:::

::: {.solution}
Let
\[
T^2=S^1\times S^1.
\]

<1>1. If an embedded closed disk $D\subset T^2$ is given, then $D$ is contained in a contractible open subset of $T^2$.
::: {.proof}
The boundary $\partial D$ is an embedded circle in the surface $T^2$.
By the collar theorem for surfaces, $\partial D$ has a collar
\[
\partial D\times(-\varepsilon,\varepsilon)
\]
in which $D$ occupies one side of the collar.
Adjoining a sufficiently thin strip from the other side gives a slightly larger embedded disk $D'$ with
\[
D\subset\operatorname{int}(D').
\]
The open set
\[
U=\operatorname{int}(D')
\]
is homeomorphic to an open disk and hence is contractible.
:::

<1>2. Suppose, for contradiction, that
\[
T^2=A\cup B
\]
with $A$ and $B$ each homeomorphic to a closed disk.
Then there are contractible open sets $U,V\subset T^2$ such that
\[
A\subset U,
\qquad
B\subset V,
\qquad
T^2=U\cup V.
\]
::: {.proof}
Apply <1>1 separately to $A$ and $B$.
Since $A\cup B=T^2$, any open neighborhoods $U\supset A$ and $V\supset B$ also satisfy
\[
U\cup V=T^2.
\]
:::

<1>3. If a space $X$ is the union of two contractible open sets $U$ and $V$, then the cup product of any two positive-degree integral cohomology classes on $X$ is zero.
::: {.proof}
Let
\[
\alpha\in H^p(X;\ZZ),
\qquad
\beta\in H^q(X;\ZZ),
\qquad
p,q>0.
\]
Because $U$ and $V$ are contractible,
\[
H^p(U;\ZZ)=0,
\qquad
H^q(V;\ZZ)=0.
\]
Hence the long exact sequences of the pairs $(X,U)$ and $(X,V)$ show that $\alpha$ and $\beta$ lift to relative classes
\[
\bar\alpha\in H^p(X,U;\ZZ),
\qquad
\bar\beta\in H^q(X,V;\ZZ).
\]

The relative cup product has the form
\[
H^p(X,U;\ZZ)\times H^q(X,V;\ZZ)
\longrightarrow
H^{p+q}(X,U\cup V;\ZZ).
\]
Since $U\cup V=X$, its target is
\[
H^{p+q}(X,X;\ZZ)=0.
\]
Under the natural map from relative to absolute cohomology, the relative product maps to
\[
\alpha\smile\beta.
\]
Therefore
\[
\alpha\smile\beta=0.
\]
No condition on $U\cap V$ was used.
:::

<1>4. The torus has degree-one classes whose cup product is nonzero.
::: {.proof}
Let
\[
p_1,p_2:T^2=S^1\times S^1\longrightarrow S^1
\]
be the coordinate projections, and let
\[
u\in H^1(S^1;\ZZ)\cong\ZZ
\]
be a generator.
Set
\[
\alpha=p_1^*u,
\qquad
\beta=p_2^*u.
\]
The integral cohomology ring of the torus is the exterior algebra on these two degree-one generators.
In particular,
\[
H^2(T^2;\ZZ)\cong\ZZ
\]
and
\[
\alpha\smile\beta
\]
is a generator of this group.
Thus
\[
\alpha\smile\beta\ne0.
\]
:::

<1>5. Therefore $T^2$ cannot be the union of two disks.
::: {.proof}
Under the assumption in <1>2, the contractible open cover $T^2=U\cup V$ would imply by <1>3 that
\[
\alpha\smile\beta=0
\]
for the classes in <1>4. But <1>4 gives
\[
\alpha\smile\beta\ne0.
\]
This contradiction proves that no two embedded disks, regardless of how they intersect, can cover $S^1\times S^1$.
:::
:::
