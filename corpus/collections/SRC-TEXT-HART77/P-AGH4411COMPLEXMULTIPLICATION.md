---
schema: qual/card@1
id: P-AGH4411COMPLEXMULTIPLICATION
kind: problem
title: Complex multiplication by $\alpha$ has degree $\abs{\alpha}^2$ and dual $\bar\alpha$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.11 together with IV.4.7 and the complex-torus
    description in IV.4.18. Cross-checked degree-as-norm and dual-as-complex-
    conjugation against standard complex elliptic-curve notes.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be an elliptic curve over $\CC$, defined by the elliptic functions with periods $1, \tau$.
Let $R$ be the ring of endomorphisms of $X$.

a. If $f \in R$ is a nonzero endomorphism corresponding to complex multiplication by $\alpha$, as in (4.18), show that $\deg f=\abs{\alpha}^2$.

b. If $f \in R$ corresponds to $\alpha \in \CC$ again, show that the dual $\hat{f}$ of (Ex.
4.7) corresponds to the complex conjugate $\bar{\alpha}$ of $\alpha$.

c. If $\tau \in \QQ(\sqrt{-d})$ happens to be integral over $\ZZ$, show that $R=\ZZ[\tau]$.
:::

::: {.solution}
Put
$$
\Lambda=\ZZ+\ZZ\tau,
\qquad
X(\CC)\cong\CC/\Lambda.
$$
Under this uniformization,
$$
R
=
\{\alpha\in\CC:\alpha\Lambda\subseteq\Lambda\}.
$$

<1>1. If $0\ne\alpha\in R$ and $f=f_\alpha$, then
$$
\boxed{\deg f=\abs{\alpha}^2.}
$$

::: {.proof}
The kernel of
$$
f_\alpha:\CC/\Lambda\longrightarrow\CC/\Lambda,
\qquad
z+\Lambda\longmapsto\alpha z+\Lambda
$$
is
$$
\alpha^{-1}\Lambda/\Lambda.
$$
Multiplication by $\alpha$ identifies this finite group with
$$
\Lambda/\alpha\Lambda.
$$
Since the base field is $\CC$, the nonzero isogeny $f_\alpha$ is
separable. Hence its degree is the number of points in its kernel, as in
[[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7(c)]]. Therefore
$$
\deg f_\alpha
=
[\Lambda:\alpha\Lambda].
$$

Let $A(\Lambda)$ denote the Euclidean area of a fundamental parallelogram
of $\Lambda$. Multiplication by $\alpha$ scales area by $\abs{\alpha}^2$,
so
$$
A(\alpha\Lambda)=\abs{\alpha}^2A(\Lambda).
$$
For a sublattice of finite index,
$$
[\Lambda:\alpha\Lambda]
=
\frac{A(\alpha\Lambda)}{A(\Lambda)}.
$$
Combining the last three displays proves part (a).
:::

<1>2. If $f_\alpha$ corresponds to $\alpha\in R$, then its dual corresponds
to $\bar\alpha$.

::: {.proof}
If $\alpha=0$, both the dual endomorphism and complex conjugate are zero.
Assume $\alpha\ne0$, and let $\beta\in R$ correspond to $\widehat f_\alpha$.
By [[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7(c)]],
$$
\widehat f_\alpha\circ f_\alpha=[\deg f_\alpha]_X.
$$
On the complex torus, composition multiplies the corresponding complex
numbers. By step <1>1,
$$
\beta\alpha
=
\deg f_\alpha
=
\abs{\alpha}^2
=
\bar\alpha\alpha.
$$
Since $\alpha\ne0$, cancellation gives
$$
\beta=\bar\alpha.
$$
This proves part (b).
:::

<1>3. If $\tau$ is integral over $\ZZ$, then
$$
\boxed{R=\ZZ[\tau].}
$$

::: {.proof}
First let $\alpha\in R$. Since $1\in\Lambda$ and
$\alpha\Lambda\subseteq\Lambda$, one has
$$
\alpha=\alpha\cdot1\in\Lambda.
$$
Thus
$$
\alpha=a+b\tau
$$
for some $a,b\in\ZZ$, so
$$
R\subseteq\ZZ+\ZZ\tau.
$$

Because $\tau\in\QQ(\sqrt{-d})\setminus\QQ$ is integral, its monic minimal
polynomial over $\QQ$ has the form
$$
T^2-uT+v
$$
with $u,v\in\ZZ$. Hence
$$
\tau^2=u\tau-v\in\ZZ+\ZZ\tau.
$$
It follows that $\ZZ+\ZZ\tau$ is a subring of $\CC$, namely
$\ZZ[\tau]$.

Conversely, if $\alpha=a+b\tau\in\ZZ[\tau]$, then
$$
\alpha\cdot1\in\Lambda,
\qquad
\alpha\tau=a\tau+b\tau^2\in\Lambda.
$$
Since $1,\tau$ generate $\Lambda$ over $\ZZ$, this implies
$$
\alpha\Lambda\subseteq\Lambda.
$$
Thus $\alpha\in R$, proving the reverse inclusion and part (c).
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 prove parts (a), (b), and (c), respectively.
:::
:::
