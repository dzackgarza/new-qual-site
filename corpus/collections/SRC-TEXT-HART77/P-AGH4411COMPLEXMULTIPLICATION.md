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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.4.11, printed p. 93,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.4.11, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed the degree as the area ratio $A_{\alpha L}/A_L=\abs{\alpha}^2$, the dual identity $\times\bar\alpha\circ\times\alpha=[\alpha\bar\alpha]$, and the two inclusions $\ZZ[\tau]\subseteq R\subseteq\ZZ[\tau]$ that give (c).
    Not checked: Yang's Solutions outside printed p. 93; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card now carries a published-solution remark naming Yang Pi-Yeh's
    Solution 4.4.11 at printed p. 93; it had none before. No
    step, statement or hypothesis of the card changes.
---

::: {.problem}
Let $X$ be an elliptic curve over $\CC$, defined by the elliptic functions with periods $1, \tau$.
Let $R$ be the ring of endomorphisms of $X$.

(a) If $f \in R$ is a nonzero endomorphism corresponding to complex multiplication by $\alpha$, as in (4.18), show that $\deg f=\abs{\alpha}^2$.

(b) If $f \in R$ corresponds to $\alpha \in \CC$ again, show that the dual $\hat{f}$ of (Ex. 4.7) corresponds to the complex conjugate $\bar{\alpha}$ of $\alpha$.

(c) If $\tau \in \QQ(\sqrt{-d})$ happens to be integral over $\ZZ$, show that $R=\ZZ[\tau]$.
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

::: pf

::: {.pf-step #s1}

If $0\ne\alpha\in R$ and $f=f_\alpha$, then
$$
\boxed{\deg f=\abs{\alpha}^2.}
$$

::: pf-proof

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
separable. Hence its degree is the number of points in its kernel.
Therefore
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

:::

::: {.pf-step #s2}

If $f_\alpha$ corresponds to $\alpha\in R$, then its dual corresponds
to $\bar\alpha$.

::: pf-proof

If $\alpha=0$, both the dual endomorphism and complex conjugate are zero.
Assume $\alpha\ne0$, and let $\beta\in R$ correspond to $\widehat f_\alpha$.
By [[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7(c)]],
$$
\widehat f_\alpha\circ f_\alpha=[\deg f_\alpha]_X.
$$
On the complex torus, composition multiplies the corresponding complex
numbers. By step [](#s1){.pf-ref},
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

:::

::: {.pf-step #s3}

If $\tau$ is integral over $\ZZ$, then
$$
\boxed{R=\ZZ[\tau].}
$$

::: pf-proof

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

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::

::: {.remark title="Published solution"}
Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.4.11, printed p. 93, does all three parts in a few lines each. (a) The degree is the index of the sublattice, so with $A_L$ the area of the period parallelogram $\deg f=A_{\alpha L}/A_L=\abs{\alpha}^2$. (b) Since $\times\alpha$ is $\CC\to\CC$ and multiplication by $N=\deg f=\alpha\bar\alpha$ induces $N_X$, the morphism $\times\bar\alpha$ is the dual: it satisfies $\times\bar\alpha\circ\times\alpha=\times N$, which is what $[N]=\hat f\circ f$ asks for. (c) If $\tau$ is integral over $\ZZ$ in the quadratic field, then $\tau^2$ is an integral combination of $\tau$ and $1$, so $\ZZ[\tau]=\ZZ\oplus\ZZ\tau=L_\tau$ and $\ZZ[\tau]\subseteq R$; conversely an $\alpha$ with $\alpha L_\tau\subseteq L_\tau$ has $\alpha=\alpha\cdot1\in L_\tau$, so $\alpha\in\ZZ[\tau]$. The one thing the entry takes for granted is that $R$ is the ring of endomorphisms fixing the origin, which is how the exercise's ring has to be read for composition to be defined.
:::
