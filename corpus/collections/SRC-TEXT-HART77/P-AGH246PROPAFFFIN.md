---
schema: qual/card@1
id: P-AGH246PROPAFFFIN
kind: problem
title: Proper morphisms of affine varieties are finite
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Morphisms
  - Finite Morphisms
  - Affine Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against Hartshorne II.4.6 and the stated II.4.11A valuation-ring characterization of integral closure.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $f: X \to Y$ be a proper morphism of affine varieties over $k$.
Then $f$ is a finite morphism.
*Hint:* Use (4.11A).
:::

::: {.solution}
Write
\[
X=\Spec A,
\qquad
Y=\Spec B,
\]
where $A$ and $B$ are finitely generated integral $k$-algebras, and let
\[
\phi:B\longrightarrow A
\]
be the ring homomorphism corresponding to $f$.
Put
\[
K=\operatorname{Frac}(A).
\]

<1>1. Let $R\subseteq K$ be any valuation ring containing the subring $\phi(B)$.  Then there is a commutative diagram
\[
\begin{array}{ccc}
\Spec K&\longrightarrow&X\\
\downarrow&&\downarrow{\scriptstyle f}\\
\Spec R&\longrightarrow&Y.
\end{array}
\]
::: {.proof}
The top morphism is induced by the inclusion
\[
A\hookrightarrow K.
\]
The bottom morphism is induced by the ring homomorphism
\[
B\xrightarrow{\phi}\phi(B)\hookrightarrow R.
\]
After composing with the inclusion $R\hookrightarrow K$, both routes on coordinate rings are the same map
\[
B\xrightarrow{\phi}A\hookrightarrow K.
\]
Hence the square commutes.
:::

<1>2. Properness of $f$ gives a lift
\[
\Spec R\longrightarrow X
\]
in the diagram of <1>1.
::: {.proof}
The valuative criterion for properness applies to every valuation ring and every such commutative square.  Since $f$ is proper, a unique lift exists.
:::

<1>3. The lift in <1>2 forces
\[
\boxed{A\subseteq R.}
\]
::: {.proof}
The lift corresponds to a ring homomorphism
\[
A\longrightarrow R
\]
whose composite with the inclusion
\[
R\hookrightarrow K
\]
equals the original inclusion
\[
A\hookrightarrow K,
\]
because the lift restricts on the generic point to the top arrow in <1>1.

Therefore every $a\in A$ maps to the same element $a\in K$, now lying in $R$.  Hence $A\subseteq R$.
:::

<1>4. Every element of $A$ is integral over $\phi(B)$.
::: {.proof}
Hartshorne II.4.11A states that if $C$ is a subring of a field $K$, then the integral closure of $C$ in $K$ is the intersection of all valuation rings of $K$ which contain $C$.

Take
\[
C=\phi(B)\subseteq K.
\]
By <1>3, every valuation ring $R$ of $K$ containing $C$ also contains $A$.  Therefore
\[
A
\subseteq
\bigcap_{R\supseteq C}R
=
\overline C^{\,K},
\]
the integral closure of $C$ in $K$.  Thus every $a\in A$ is integral over $C=\phi(B)$.
:::

<1>5. The $B$-algebra $A$ is finitely generated.
::: {.proof}
The morphism $f$ is proper, hence of finite type by definition.  Since both source and target are affine, the affine criterion for finite type gives
\[
A=B[a_1,\ldots,a_n]
\]
for finitely many elements $a_i\in A$.
:::

<1>6. A finitely generated integral algebra is finite as a module.  Hence $A$ is a finite $B$-module.
::: {.proof}
By <1>4, each generator $a_i$ from <1>5 is integral over the image of $B$.  Thus for each $i$ there is a monic equation
\[
a_i^{d_i}+b_{i,d_i-1}a_i^{d_i-1}+\cdots+b_{i,0}=0
\]
with coefficients from the image of $B$.

Consequently every sufficiently high power of $a_i$ is a $B$-linear combination of lower powers.  Therefore $A$ is generated as a $B$-module by the finitely many monomials
\[
a_1^{e_1}\cdots a_n^{e_n},
\qquad
0\le e_i<d_i.
\]
Hence $A$ is finite as a $B$-module.
:::

<1>7. Therefore
\[
\boxed{f:X\longrightarrow Y\text{ is finite}.}
\]
::: {.proof}
For an affine morphism
\[
\Spec A\longrightarrow\Spec B,
\]
finiteness is exactly the condition that $A$ be finite as a $B$-module.  This is <1>6.
:::

<1>8. Q.E.D.
::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
