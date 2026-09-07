---
schema: qual/card@1
id: P-ALGF21F
kind: problem
title: $A \otimes_{\mathbb{Z}} B$ is the coproduct in commutative unital rings
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 6 of the official UCSD Algebra Qualifying Exam, Fall 2021 source; the coproduct statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the canonical unital ring maps, construction of the mediating map by the balanced bilinear map (a,b) -> f(a)g(b), multiplicativity, and uniqueness on pure tensors.
---

::: problem
Prove that in the category of commutative rings with unit, $A \otimes_{\mathbb{Z}} B$ is the coproduct of the rings $A$ and $B$.
:::

::: {.solution}
<1>1. There are canonical unital ring homomorphisms
\[
i_A:A\longrightarrow A\otimes_{\mathbb Z}B,
\qquad
a\longmapsto a\otimes1,
\]
and
\[
i_B:B\longrightarrow A\otimes_{\mathbb Z}B,
\qquad
b\longmapsto1\otimes b.
\]
::: {.proof}
Additivity follows from bilinearity of the tensor product.
For multiplication,
\[
(a\otimes1)(a'\otimes1)=aa'\otimes1
\]
and similarly for $B$.
Both maps send the unit to
\[
1\otimes1,
\]
the unit of the tensor-product ring.
:::

<1>2. Let $C$ be a commutative unital ring and let
\[
f:A\longrightarrow C,
\qquad
g:B\longrightarrow C
\]
be unital ring homomorphisms.
The rule
\[
\beta(a,b)=f(a)g(b)
\]
defines a $\mathbb Z$-balanced bilinear map
\[
\beta:A\times B\longrightarrow C.
\]
::: {.proof}
Additivity in each variable follows from additivity of $f$ and $g$ and distributivity in $C$.
For $n\in\mathbb Z$,
\[
\beta(na,b)=f(na)g(b)=n f(a)g(b)
\]
and
\[
\beta(a,nb)=f(a)g(nb)=f(a)n g(b)=n f(a)g(b).
\]
Hence
\[
\beta(na,b)=\beta(a,nb),
\]
so $\beta$ is balanced.
:::

<1>3. There is a unique group homomorphism
\[
h:A\otimes_{\mathbb Z}B\longrightarrow C
\]
such that
\[
h(a\otimes b)=f(a)g(b)
\]
for all $a\in A$ and $b\in B$.
::: {.proof}
This is exactly the universal property of the tensor product applied to the balanced bilinear map $\beta$ from <1>2.
:::

<1>4. The map $h$ is a unital ring homomorphism.
::: {.proof}
By <1>3, $h$ is additive.
For pure tensors,
\[
\begin{aligned}
h\bigl((a\otimes b)(a'\otimes b')\bigr)
&=h(aa'\otimes bb')\\
&=f(aa')g(bb')\\
&=f(a)f(a')g(b)g(b')\\
&=f(a)g(b)f(a')g(b')\\
&=h(a\otimes b)h(a'\otimes b'),
\end{aligned}
\]
where commutativity of $C$ is used in the fourth equality.
Since pure tensors generate $A\otimes_{\mathbb Z}B$ additively, distributivity extends this identity to arbitrary elements.
Also
\[
h(1\otimes1)=f(1)g(1)=1,
\]
so $h$ is unital.
:::

<1>5. The map $h$ satisfies
\[
h\circ i_A=f
\qquad\text{and}\qquad
h\circ i_B=g.
\]
::: {.proof}
For $a\in A$,
\[
h(i_A(a))
=h(a\otimes1)
=f(a)g(1)
=f(a).
\]
Similarly, for $b\in B$,
\[
h(i_B(b))
=h(1\otimes b)
=f(1)g(b)
=g(b).
\]
:::

<1>6. The map $h$ is the unique unital ring homomorphism with the property in <1>5.
::: {.proof}
Let
\[
k:A\otimes_{\mathbb Z}B\longrightarrow C
\]
be another unital ring homomorphism satisfying
\[
k\circ i_A=f,
\qquad
k\circ i_B=g.
\]
Every pure tensor factors as
\[
a\otimes b
=(a\otimes1)(1\otimes b).
\]
Therefore
\[
\begin{aligned}
k(a\otimes b)
&=k(a\otimes1)k(1\otimes b)\\
&=f(a)g(b)\\
&=h(a\otimes b).
\end{aligned}
\]
Since pure tensors generate the tensor product additively and both maps are additive, $k=h$.
:::

<1>7. Hence $A\otimes_{\mathbb Z}B$, together with $i_A$ and $i_B$, is the coproduct of $A$ and $B$ in the category of commutative unital rings.
::: {.proof}
Existence of the mediating morphism is <1>3--<1>5, and uniqueness is <1>6.
This is precisely the coproduct universal property.
:::
:::
