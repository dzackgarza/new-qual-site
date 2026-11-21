---
schema: qual/card@1
id: P-APAS21D
kind: problem
title: Orthogonal projections onto $\operatorname{range}(C^H)$ and $\operatorname{null}(C)$; projectors onto a line
classification:
  areas:
  - applied-algebra
  topics:
  - Inner Product Spaces
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, with (a), (b)(i) and (b)(ii) as top-level steps and
    (b)(ii) as the QED step. Re-checked: $\rank C=m$ makes $C^H$ injective, so $\langle CC^Hu,u\rangle
    =\norm{C^Hu}^2$ vanishes only at $u=0$ and $CC^H$ is positive definite, hence invertible;
    $P=C^H(CC^H)^{-1}C$ is Hermitian and idempotent, fixes $\operatorname{range}C^H$ and has range
    inside it; $CQ=0$ and $Cx=0\Rightarrow Qx=x$ identify the range of $Q$ with $\ker C$;
    $A=yz^H$ with $z^Hy=1$ is idempotent with range $Y$ and is oblique unless $z$ is parallel to $y$;
    and $z=y/(y^Hy)$ makes it Hermitian, hence the unique orthogonal projection onto $Y$. Added: the
    positivity argument, the verification that $A$ is oblique rather than orthogonal in (b)(i), and
    the uniqueness of an orthogonal projection with a given range, which the prose asserted only for
    the particular formula. Presentation repair: `\operatorname{rank}` is written `\rank`, the
    vocabulary macro. The collection's provenance is the Spring 2021 examination paper, so no
    retained solution set covers the problem.
---

::: {.problem}
Throughout, $M_{m,n}$ denotes the set of $m \times n$ matrices with complex components, $\CC^n$ is the set of column vectors with $n$ complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) Let $C \in M_{m,n}$ with $\rank(C) = m$.
Find orthogonal projections that project $x \in \CC^n$ onto $\operatorname{range}(C^H)$ and $\operatorname{null}(C)$.
Verify that your projections satisfy the properties of an orthogonal projection.

(b) For a given nonzero $y \in \CC^n$, let $Y = \operatorname{span}(y)$.

(i) Find an oblique projector $A$ that projects vectors onto $Y$.
Find the complementary projection.

(ii) Find the unique orthogonal projector $A$ that projects vectors onto $Y$.
Find the complementary projection associated with $A$.
:::

::: {.solution}
The collection's provenance is the examination paper, so no retained solution set covers the problem; the computation is the card's own, and each claimed projection is checked against the three defining properties — idempotence, self-adjointness, and the stated range.

::: pf

::: {.pf-step #invertible}
(a) If $C\in M_{m,n}$ has $\rank C=m$, then $CC^H$ is positive definite and invertible.

::: pf-proof
For $u\in\CC^m$, $\langle CC^Hu,u\rangle=\langle C^Hu,C^Hu\rangle=\norm{C^Hu}^2\ge0$, with equality only if $C^Hu=0$. Since $\rank C=m$ the rows of $C$ are independent, so $C^H$ has trivial kernel and $C^Hu=0$ forces $u=0$. Hence $CC^H$ is positive definite, and a positive definite matrix is invertible.
:::

:::

::: {.pf-step #part-a}
(a) $P=C^H(CC^H)^{-1}C$ is the orthogonal projection onto $\operatorname{range}(C^H)$, and $Q=I-P$ is the orthogonal projection onto $\ker C$.

::: pf-proof
$P^H=C^H((CC^H)^{-1})^HC=P$ because $CC^H$ is Hermitian, and
$$
P^2=C^H(CC^H)^{-1}CC^H(CC^H)^{-1}C=C^H(CC^H)^{-1}C=P,
$$
so $P$ is an orthogonal projection. Its range lies in $\operatorname{range}(C^H)$, and $P(C^Hu)=C^H(CC^H)^{-1}CC^Hu=C^Hu$ fixes that range, so the range is exactly $\operatorname{range}(C^H)$. Since $\ker C=(\operatorname{range}C^H)^\perp$, the complementary projection $Q=I-P$ has range $\ker C$: indeed $CQ=C-CC^H(CC^H)^{-1}C=0$ gives $\operatorname{range}Q\subseteq\ker C$, and $Cx=0$ gives $Qx=x-Px=x$ because $Px=C^H(CC^H)^{-1}Cx=0$. $Q$ is idempotent and self-adjoint as the complement of such a $P$.
:::

:::

::: {.pf-step #oblique}
(b)(i) For $y\ne0$ and any $z$ with $z^Hy=1$, the matrix $A=yz^H$ is a projection onto $Y=\operatorname{span}(y)$, with complementary projection $I-A$.

::: pf-proof
Such a $z$ exists because $y\ne0$: take $z=y/(y^Hy)$, or any vector with nonzero inner product with $y$ rescaled. Then
$$
A^2=yz^Hyz^H=y(z^Hy)z^H=yz^H=A,
$$
so $A$ is a projection; its range is contained in $\CC y=Y$ and contains $y=Ay$ because $Ay=y(z^Hy)=y$, so the range is $Y$. The complementary projection is $I-A$, which is idempotent with range the kernel of $A$; it is not self-adjoint unless $z$ is parallel to $y$, so $A$ is in general an oblique projection.
:::

:::

::: {.pf-step}
(b)(ii) The orthogonal projection onto $Y$ is $A=yy^H/(y^Hy)$, with complementary orthogonal projection $I-yy^H/(y^Hy)$ onto $Y^\perp$.

::: pf-proof
Taking $z=y/(y^Hy)$ in step [](#oblique){.pf-ref} gives $A=yy^H/(y^Hy)$, and this satisfies $z^Hy=(y^Hy)/(y^Hy)=1$. It is self-adjoint because $(yy^H)^H=yy^H$ and $y^Hy$ is real, and idempotent because $y^Hy>0$ gives $A^2=yy^Hyy^H/(y^Hy)^2=yy^H/(y^Hy)=A$; so it is an orthogonal projection, and by step [](#oblique){.pf-ref} its range is $Y$. An orthogonal projection is determined by its range, so this is the unique one. Its complement $I-A$ is the orthogonal projection onto the orthogonal complement of the range, namely $Y^\perp$. Parts (a) and (b)(i) are steps [](#part-a){.pf-ref} and [](#oblique){.pf-ref}.
:::

:::

:::
:::
