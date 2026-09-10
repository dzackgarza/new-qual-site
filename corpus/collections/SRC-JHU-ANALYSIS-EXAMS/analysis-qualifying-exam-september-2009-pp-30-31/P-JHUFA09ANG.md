---
schema: qual/card@1
id: P-JHUFA09ANG
kind: problem
title: The sharp derivative bound for an upper-half-plane map with $f(i)=1/2$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the upper-half-plane source, unit-disk target and prescribed value at i with September 2009 problem 7 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked both normalization derivatives, derived the bound three eighths, and exhibited every extremizer rather than just an upper estimate."
---

7. Let $f:H\to D$ be a holomorphic map from the upper half plane

$H = \left\{ z \in \mathbb { C } : \operatorname { I m } z > 0 \right\}$ to the unit disk $D = \{ z \in \mathbb { C } : | z | < 1 \}$

Suppose that $f ( i ) = 1 / 2$ . Determine the maximal possible value of $| f ^ { \prime } ( i ) |$

::: solution
The maximum is $\boxed{3/8}$.

<1>1. Normalize both the source and the target to a disk map fixing zero.

::: proof
The maps
$$
\phi(z)=\frac{z-i}{z+i},\qquad
\psi(w)=i\frac{1+w}{1-w}
$$
are inverse holomorphic bijections $H\to D$ and $D\to H$.
Indeed, direct substitution verifies the inverse identities,
and for $z\in H$,
$|z+i|^2-|z-i|^2=4\operatorname{Im}z>0$.
For $w\in D$, the inverse satisfies
$\operatorname{Im}\psi(w)=(1-|w|^2)/|1-w|^2>0$.
They send $i$ to zero and zero to $i$, respectively.

Likewise
$$
T(v)=\frac{v-1/2}{1-v/2},\qquad
T^{-1}(u)=\frac{u+1/2}{1+u/2}
$$
are inverse disk automorphisms, since
$$
1-|T(v)|^2=\frac{(3/4)(1-|v|^2)}{|1-v/2|^2}>0
$$
and the analogous identity holds for the inverse.
Therefore $F=T\circ f\circ\psi$ maps $D$ holomorphically
into $D$ and satisfies $F(0)=0$.
:::

<1>2. Schwarz's lemma gives the numerical bound.

::: proof
Direct differentiation yields $\psi'(0)=2i$ and
$T'(1/2)=4/3$. The chain rule gives
$$
F'(0)=\frac43f'(i)\,2i.
$$
Schwarz's lemma implies $|F'(0)|\leq1$ [@SS03]. Hence
$$
|f'(i)|\leq\frac38.
$$
:::

<1>3. The bound is attained, and the extremizers are explicit.

::: proof
For any $\lambda\in\mathbb C$ with $|\lambda|=1$, define
$$
f_\lambda(z)=T^{-1}(\lambda\phi(z))
=\frac{\lambda\phi(z)+1/2}{1+\lambda\phi(z)/2}.
$$
This is a holomorphic map $H\to D$ with $f_\lambda(i)=1/2$.
Its normalized map is $F(w)=\lambda w$, so the derivative
identity in step <1>2 gives $|f_\lambda'(i)|=3/8$.
For example $\lambda=1$ gives $f_1(z)=(3z-i)/(3z+i)$.

Conversely, equality in the derivative bound forces
$|F'(0)|=1$, so the equality case of Schwarz's lemma
gives $F(w)=\lambda w$ for some $|\lambda|=1$ [@SS03].
Undoing the two normalizations gives exactly $f_\lambda$.
This proves attainability and the asserted maximum.
:::
:::
