---
schema: qual/card@1
id: P-MAXAT-3-05
kind: problem
title: Cohomology rings of $\SU(n)$, $\U(n)$ and $V_k(\CC^n)$
classification:
  areas: [topology]
  topics:
  - Cohomology of Lie Groups
  - Stiefel Manifolds
  - Serre Spectral Sequence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 3, problem 5 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The corpus audit's duplicate-bodies violation on this card and P-MAXAT-4-01 was traced to the source
    rather than to the corpus. Read in this pass: assets/attachments/Problems_in_Algebraic_Topology_-_Unknown.pdf,
    which is three pages, section 3 "Cohomology ring" item (5) on printed p. 2 reading "Find the ring structure on
    H*(SU(n)), H*(U(n)), H*(V_k(C^n))." and section 4 "Spectral Sequences and Applications" item (1) on the same
    page repeating the sentence verbatim. The source prints the question twice, so two cards with one body are
    correct; the card now says so and names its sibling. Not checked: whether the author intended the second
    printing to be answered by a spectral-sequence argument instead, which is an inference from the section title
    and is not recorded on the card as a claim about the source.
---

::: {.problem}
Find the ring structure on $H^{*}(SU(n))$, $H^{*}(U(n))$, $H^{*}(V_{k}(\CC^{n}))$.
:::

::: {.solution}

The printed source states this problem twice: as Problem 3.5 in the section "Cohomology ring" and verbatim again as Problem 4.1 in the section "Spectral Sequences and Applications", both on printed p. 2 of `assets/attachments/Problems_in_Algebraic_Topology_-_Unknown.pdf`. This card answers the first printing, by the cellular and fibration computation that section asks for; the second printing has its own card, `P-MAXAT-4-01`, whose statement is identical because the source's is. The two cards therefore share a body by design, and the corpus audit's `duplicate-bodies` violation on that pair is this duplication, not a transcription error.

All cohomology groups are taken with integral coefficients. The rings are exterior algebras on odd-degree generators.

::: pf

::: {.pf-step #s1-1}

The determinant fibration
$$
SU(n)\longrightarrow U(n)\xrightarrow{\det}S^1
$$
is in fact a product decomposition as spaces:
$$
U(n)\cong SU(n)\times S^1.
$$


::: pf-proof

Define a section $s:S^1\to U(n)$ by
$$
s(z)=\operatorname{diag}(z,1,\ldots,1).
$$
Then every $A\in U(n)$ can be written uniquely as
$$
A=B\,s(\det A),
\qquad
B=A,s(\det A)^{-1}\in SU(n).
$$
The resulting maps in both directions are continuous, giving a homeomorphism of spaces. No assertion that this is a direct product of groups is needed.

:::

:::

::: {.pf-step #s1-2}

There is a sphere fibration
$$
SU(n-1)\longrightarrow SU(n)\longrightarrow S^{2n-1}.
$$


::: pf-proof

Let $SU(n)$ act transitively on the unit sphere $S^{2n-1}\subset\CC^n$ by its standard representation. The stabilizer of the last basis vector consists of block matrices
$$
\begin{pmatrix}A&0\\0&1\end{pmatrix},
\qquad A\in SU(n-1).
$$
Thus the orbit map identifies the quotient $SU(n)/SU(n-1)$ with $S^{2n-1}$ and yields the displayed principal bundle.

:::

:::

::: {.pf-step #s1-3}

Inductively,
$$
\boxed{
H^*(SU(n);\ZZ)
\cong\Lambda(x_3,x_5,\ldots,x_{2n-1}),
\qquad \gradeddegree{x_{2j-1}}=2j-1.}
$$


::: pf-proof

For $n=2$, $SU(2)\cong S^3$, so the claim holds. Assume it for $SU(n-1)$ and use the Serre cohomology spectral sequence of step [](#s1-2){.pf-ref}. Its $E_2$ page is
$$
H^*(S^{2n-1};\ZZ)\otimes H^*(SU(n-1);\ZZ).
$$
The fiber cohomology is generated in degrees at most $2n-3$. Degree considerations leave no possible nonzero differential involving the base generator in degree $2n-1$, so the spectral sequence collapses. All groups are free abelian, so there are no additive extension problems. The restriction to the fiber identifies the old generators $x_3,\ldots,x_{2n-3}$, while a class $x_{2n-1}$ lifting the sphere generator supplies the new factor. Odd degree and torsion-freeness imply $x_{2n-1}^2=0$, giving the exterior algebra.

:::

:::

::: {.pf-step #s1-4}

Consequently,
$$
\boxed{
H^*(U(n);\ZZ)
\cong\Lambda(x_1,x_3,x_5,\ldots,x_{2n-1}),
\qquad \gradeddegree{x_{2j-1}}=2j-1.}
$$


::: pf-proof

By step [](#s1-1){.pf-ref} and the Künneth theorem,
$$
H^*(U(n))
\cong H^*(SU(n))\otimes H^*(S^1).
$$
Step [](#s1-3){.pf-ref} gives the first factor, while
$$
H^*(S^1;\ZZ)=\Lambda(x_1).
$$
Tensoring the exterior algebras gives the displayed presentation.

:::

:::

::: pf-step

The complex Stiefel manifold of orthonormal $k$-frames is
$$
V_k(\CC^n)\cong U(n)/U(n-k).
$$


::: pf-proof

The group $U(n)$ acts transitively on ordered orthonormal $k$-frames. The stabilizer of the standard frame $(e_1,\ldots,e_k)$ acts arbitrarily on its orthogonal complement and is therefore the subgroup $U(n-k)$.

:::

:::

::: {.pf-step #s1-6}

Forgetting the last vector gives a sphere fibration
$$
S^{2(n-k)+1}
\longrightarrow V_k(\CC^n)
\longrightarrow V_{k-1}(\CC^n).
$$


::: pf-proof

Over a fixed orthonormal $(k-1)$-frame, the last vector can be any unit vector in its complex orthogonal complement, which has complex dimension $n-k+1$. Its unit sphere has real dimension
$$
2(n-k+1)-1=2(n-k)+1.
$$
Local orthonormal trivializations give the bundle.

:::

:::

::: {.pf-step #s1-7}

Induction on $k$ gives
$$
\boxed{
H^*(V_k(\CC^n);\ZZ)
\cong
\Lambda(x_{2(n-k)+1},x_{2(n-k)+3},\ldots,x_{2n-1}).}
$$


::: pf-proof

For $k=1$, $V_1(\CC^n)=S^{2n-1}$, giving one exterior generator in degree $2n-1$. Assume the formula for $k-1$. Apply the Serre spectral sequence to step [](#s1-6){.pf-ref}. The new sphere generator has degree $2(n-k)+1$, while the existing generators begin in degree $2(n-k+1)+1=2(n-k)+3$. Degree considerations force collapse, and all groups are free abelian. The new odd-degree generator squares to zero, and together with the inductively existing generators yields the stated exterior algebra.

:::

:::

::: {.pf-step #s1-8}

Thus the three ring structures are
$$
\boxed{H^*(SU(n))=\Lambda(x_3,x_5,\ldots,x_{2n-1}),}
$$
$$
\boxed{H^*(U(n))=\Lambda(x_1,x_3,\ldots,x_{2n-1}),}
$$
and
$$
\boxed{H^*(V_k(\CC^n))
=\Lambda(x_{2(n-k)+1},x_{2(n-k)+3},\ldots,x_{2n-1}).}
$$


::: pf-proof

These are steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}, and [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} gives all requested integral cohomology rings and generator degrees.

:::

:::

:::
