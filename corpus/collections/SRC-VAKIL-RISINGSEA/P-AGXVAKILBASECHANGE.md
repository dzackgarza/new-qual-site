---
schema: qual/card@1
id: P-AGXVAKILBASECHANGE
kind: problem
title: Extension of scalars as a functor, and the ring structure on $B\tensor_A C$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Tensor Products
  - Functors
relations: []
review: draft
---

::: problem
**Part a**: for $M$ an $A\dash$module and $\phi: A\to B$ a morphism of rings, give $B\tensor_A M$ the structure of a $B\dash$module and show that it describes a functor $\mods{A}\to \mods{B}$.

**Part b**: if $\psi: A\to C$ is another ring morphism, show that $B\tensor_A C$ has a ring structure.
:::

::: solution
**Part a**:

- $B\tensor_A M$ makes sense: $B$ is a $(B, A)\dash$bimodule with the usual multiplication on the left and the right action
\[
A &\to \Endo(B) \\
a &\mapsto (b\mapsto b\cdot \phi(a))
.\]

- $B\tensor_A M$ is a left $B\dash$module via
\[
B &\to \Endo(B\tensor_A M) \\
b_0 &\mapsto (b\tensor m \mapsto b_0 b \tensor m)
.\]

- This describes a functor:
\[
F: \mods{A} &\to \mods{B} \\
X &\mapsto B\tensor_A X \\
(X\xrightarrow{f} Y) &\mapsto (B\tensor_A X \xrightarrow{\id_B \tensor f} B\tensor_A Y)
.\]

  Need to check that $F$ preserves the identity morphism, i.e. $X\in \mods{A}$ implies $F(\id_X) = \id_{F(X)}$, and that $F$ preserves composition, i.e. $F(f\circ g) = F(f) \circ F(g)$.

- Preserving identity morphisms: by construction $\id_X$ maps to $B\tensor_A X \xrightarrow{\id_B \tensor \id_X} B\tensor_A X$, which one argues is the identity map of $B\dash$modules.

- Preserving composition:
\[
(X\xrightarrow{f} Y \xrightarrow{g} Z) \mapsto (B\tensor_A X \xrightarrow{\id_B\tensor f} B\tensor_A Y \xrightarrow{\id_B \tensor g} B\tensor_A Z) = (B\tensor_A X \xrightarrow{\id_B \tensor (g\circ f)} B\tensor_A Z )
.\]

**Part b**:

- $B\tensor_A C$ makes sense, since $C$ is a left $A\dash$module via $a\mapsto (c\mapsto \psi(a)c)$.

- We must define $(B\tensor_A C, P, M)$ so that it is an abelian group under $P$ (plus), a monoid under $M$ (multiplication), with left and right distributivity.

- Start by defining these on cartesian products:
\[
P: \qty{B\tensor_A C}^{\cross 2} &\to B\tensor_A C \\
P\qty{ (b_1 \tensor c_1), (b_2\tensor c_2)} &= (b_1 +_B b_2) \tensor (c_1 +_C c_2)
,\]
\[
M: \qty{B\tensor_A C}^{\cross 2} &\to B\tensor_A C \\
M\qty{ (b_1 \tensor c_1),  (b_2\tensor c_2)} &= (b_1 \cdot_B b_2) \tensor (c_1 \cdot_C c_2)
.\]

- Check $A\dash$bilinearity:
\[
P(a\cdot (b_1\tensor c_1),\, (b_2\tensor c_2))
&\da \qty{ a \cdot (b_1 + b_2)} \tensor (c_1 + c_2)  \\
&= \qty{ (b_1 + b_2)} \tensor a\cdot (c_1 + c_2) \quad\text{since $C$ is a left $A\dash$module} \\
&\da P((b_1\tensor c_1),\, a\cdot (b_2\tensor c_2))
,\]
\[
M(a\cdot (b_1\tensor c_1),\, (b_2\tensor c_2))
&\da \qty{a\cdot (b_1 \cdot b_2)} \tensor (c_1 \cdot c_2) \\
&= (b_1 \cdot b_2) \tensor \qty{ a\cdot (c_1 \cdot c_2) } \quad\text{since $C$ is a left $A\dash$module} \\
&\da M((b_1\tensor c_1),\, a\cdot (b_2\tensor c_2))
.\]

- So these lift to maps out of $(B\tensor_A C)^{\tensor 2}$.

- $P$ forms an abelian group: clear, because $+_B$ and $+_C$ do, and commuting is done within each factor.

- Checking distributivity; claim: it suffices to check on elementary tensors and extend by linearity.
\[
(b_0 \tensor c_0) \cdot \qty{(b_1 \tensor c_1) + (b_2\tensor c_2) }
&= (b_0\tensor c_0) \cdot \qty{ (b_1 + b_2) \tensor (c_1 + c_2) } \\
&= (b_0(b_1 + b_2)) \tensor ( c_0(c_1 + c_2)) \\
&= (b_0 b_1 + b_0 b_2) \tensor (c_0 c_1 + c_0 c_2) \\
&= \cdots
.\]
:::

::: {.remark}
Erratum: part b defines the ring operations incorrectly and does not finish.

- Addition on $B\tensor_A C$ is the abelian-group addition the tensor product already has; the formula $(b_1\tensor c_1) + (b_2\tensor c_2) = (b_1+b_2)\tensor(c_1+c_2)$ is false, since the right side expands to $b_1\tensor c_1 + b_1\tensor c_2 + b_2\tensor c_1 + b_2\tensor c_2$.
- Multiplication $(b_1\tensor c_1)(b_2\tensor c_2) = b_1b_2 \tensor c_1c_2$ is well-defined because the map $(b_1, c_1, b_2, c_2) \mapsto b_1b_2\tensor c_1c_2$ is $A$-multilinear and balanced in each tensor factor, $b_1\phi(a)b_2\tensor c_1c_2 = b_1b_2\tensor \psi(a)c_1c_2$ as $B$ and $C$ are commutative; it therefore induces $(B\tensor_A C)\tensor_A(B\tensor_A C) \to B\tensor_A C$. The displayed bilinearity check moves a scalar across the whole product rather than across one tensor factor.
- Distributivity, left as "$\cdots$", is the bilinearity of this induced multiplication; associativity and the unit $1\tensor 1$ are checked on elementary tensors.
:::
