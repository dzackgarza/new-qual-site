---
schema: qual/card@1
id: E-HAT-2.B-8
kind: problem
title: "Real division algebras and the Borsuk--Ulam theorem"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the determinant or transfer-sequence argument, including the mod-2 endpoint maps.
---

Show that $\mathbb{R}^{2n+1}$ is not a division algebra over $\mathbb{R}$ if $n > 0$ by considering how the determinant of the linear map $x \mapsto ax$ given by the multiplication in a division algebra structure would vary as $a$ moves along a path in $\mathbb{R}^{2n+1} - \{0\}$ joining two antipodal points.

::: {.solution}
Assume for contradiction that $A=\mathbb R^{2n+1}$, with $n>0$, has the structure of a real division algebra. For $a\in A$ let
\[
L_a:A\to A,\qquad L_a(x)=ax.
\]

<1>1. If $a\ne0$, then $L_a$ is invertible, hence
\[
\det L_a\ne0.
\]
::: {.proof}
In a division algebra the equation $ax=b$ is solvable for every $b$ whenever $a\ne0$, so $L_a$ is surjective. Since $A$ is finite-dimensional, $L_a$ is therefore an isomorphism.
:::

<1>2. Choose $a\ne0$. Since $2n+1\ge3$, there is a path
\[
\gamma:[0,1]\to A-\{0\}
\]
with $\gamma(0)=a$ and $\gamma(1)=-a$.
::: {.proof}
The punctured Euclidean space $\mathbb R^{2n+1}-\{0\}$ is path-connected when $2n+1>1$; for instance join antipodal points by a semicircle on the sphere of radius $\|a\|$.
:::

<1>3. The function
\[
t\longmapsto \det L_{\gamma(t)}
\]
is continuous and never zero, but its endpoint values have opposite signs.
::: {.proof}
Bilinearity of multiplication implies that the matrix entries of $L_a$ depend linearly, hence continuously, on $a$. Thus the determinant depends continuously on $a$. By <1>1 it never vanishes along $\gamma$. On the other hand
\[
L_{-a}=-L_a,
\]
so, because the dimension $2n+1$ is odd,
\[
\det L_{-a}=(-1)^{2n+1}\det L_a=-\det L_a.
\]
:::

<1>4. This is impossible.
::: {.proof}
A continuous nonzero real-valued function on the connected interval $[0,1]$ has constant sign. The endpoint calculation in <1>3 contradicts this.
:::

Hence
\[
\boxed{\mathbb R^{2n+1}\text{ admits no real division-algebra structure for }n>0.}
\]
:::
