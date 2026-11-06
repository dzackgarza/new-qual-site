---
schema: qual/card@1
id: P-UCTOP290-S6-1-TORUS
kind: problem
title: Homology of a torus with an attached disk
classification:
  areas:
  - topology
  topics:
  - Simplicial Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 1 in the PDF page image; the source does not specify the disk attaching circle.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 6, problem 1, last item
    (assets/attachments/UCSD_290_F14_sheet6.pdf, printed page 258), from the
    checked-in extraction and a 300 dpi render. The printed item is "the torus
    with a disc attached inside it" and, like the rest of problem 1, it does not
    say along which circle the disc is attached. The card states the item and
    answers for a general attaching circle with the two cases separated, which
    is a completion rather than a repair of the printed words; that the source
    leaves the circle unspecified was already recorded, and is confirmed here.
---

::: {.problem}
Give a simplicial or $\Delta$-complex model and compute
the integral homology of “the torus with a disc attached
inside it.” Describe generators.
:::

::: {.solution}

Let $X$ be the torus $T^2$ with a closed disc $D$ attached along a circle
$\gamma\subset T^2$, and let $X$ be built as a cell complex: triangulate $T^2$
so that $\gamma$ is a subcomplex, triangulate $D$ so that its boundary matches
$\gamma$ edge by edge, and glue.

::: pf

::: {.pf-step #model}

$X$ has $H_0=\ZZ$, and its cellular chain complex in degrees one and two is
$$
\ZZ^2=\langle \text{the torus's two 1-cells}\rangle\xleftarrow{\ \partial_2\ }\ZZ^2=\langle\text{the torus 2-cell},\ \text{the disc}\rangle ,
$$
where the torus $2$-cell has boundary $0$ and the disc's boundary is the class
of $\gamma$ in $H_1(T^2;\ZZ)$.

::: pf-proof

Triangulating $T^2$ with $\gamma$ a subcomplex and gluing a triangulated disc
along it gives a finite simplicial complex containing $T^2$ as a subcomplex;
its homology is that of the CW complex with one $0$-cell, two $1$-cells and
two $2$-cells obtained by collapsing a maximal tree of the $1$-skeleton. The
torus $2$-cell closes up on itself, so its boundary is $0$, and the disc's
boundary is $\gamma$, whose class in $H_1(T^2;\ZZ)$ is some $(p,q)\in\ZZ^2$ in
the standard basis.

:::

:::

::: {.pf-step #nontrivial}

If $(p,q)\ne(0,0)$ then
$$
H_1(X;\ZZ)=\ZZ^2/\langle(p,q)\rangle\cong\ZZ\oplus\ZZ/d,\qquad H_2(X;\ZZ)=\ZZ,
$$
where $d=\gcd(p,q)$; the surviving $H_2$ generator is the fundamental class of
the torus.

::: pf-proof

With $\partial_1=0$ on the two $1$-cells,
$H_1=\ZZ^2/\operatorname{im}\partial_2$ and $\operatorname{im}\partial_2$ is
spanned by $(p,q)$, since the disc contributes that vector and the torus
$2$-cell contributes $0$. An automorphism of $\ZZ^2$ carries $(p,q)$ to
$(d,0)$, so the quotient is $\ZZ\oplus\ZZ/d$. For $H_2=\ker\partial_2$ the two
$2$-cells are independent and neither is a boundary, so the kernel is $\ZZ^2$
if $(p,q)=0$ and is spanned by the torus $2$-cell alone otherwise, because
then the disc's boundary is nonzero and the disc is not a cycle.

:::

:::

::: {.pf-step #trivial}

If $\gamma$ bounds an embedded disc in $T^2$, then $(p,q)=(0,0)$ as a chain
and $H_0,H_1,H_2$ are $\ZZ,\ZZ^2,\ZZ^2$.

::: pf-proof

A disc in the torus has a boundary that is the boundary of its own $2$-chain,
so the class of $\gamma$ is $0$ in $H_1$ and, after subdividing so that the
disc is a subcomplex, $\gamma$ is the boundary of one of the torus's
$2$-chains; then $\ker\partial_2$ is spanned by the torus $2$-cell and by the
difference of the attached disc with that $2$-chain, giving $\ZZ^2$, and
$\operatorname{im}\partial_2=0$, giving $H_1=\ZZ^2$. This is the reading in
which "attached inside" means glued along the boundary of a disc contained in
the torus; then $X$ is $T^2$ with a $2$-sphere attached along the circle
$\gamma$, that is $T^2\vee S^2$ up to homotopy, since a cell attached along a
null-homotopic loop splits off as a sphere; its Euler characteristic
$1-2+2=1$ agrees with $\chi(T^2\vee S^2)=0+2-1$, so $X$ is not a surface. The
source does not settle which reading it intends.

:::

:::

:::


:::
