---
schema: qual/card@1
id: P-UCTOP290-S6-4
kind: problem
title: First singular homology is the abelianized fundamental group
classification:
  areas:
  - topology
  topics:
  - Singular Homology
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 4 in its checked-in extraction and page image; its part (d) can only assert injectivity after abelianization.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 6, problem 4
    (assets/attachments/UCSD_290_F14_sheet6.pdf, printed page 258), from the
    checked-in extraction and a 300 dpi render. The printed parts are (a) that
    h: pi_1(X,x_0) -> H_1(X) is a homomorphism, (b) that it factors through the
    abelianisation, (c) that h is surjective, with the hint about endpoints of
    singular 1-simplices, and (d) that h is injective, with the hint about
    reordering modulo the commutator subgroup. Part (d) as printed is false
    whenever pi_1 is nonabelian, since h kills commutators; the card states the
    repaired conclusion, that the induced map on the abelianisation is an
    isomorphism, and records the defect in a remark. That repair was read
    against the printed part (d) here and stands.
---

::: {.problem}
For a path-connected space $X$ with basepoint $x_0$,
show that sending a based loop to its singular
one-cycle induces an isomorphism
$$
\pi_1(X,x_0)/[\pi_1(X,x_0),\pi_1(X,x_0)]
\cong H_1(X;\ZZ).
$$
:::

::: {.solution}

Let $X$ be path-connected with basepoint $x_0$, write $G=\pi_1(X,x_0)$, and
let $h\colon G\to H_1(X;\ZZ)$ send the class of a based loop $\alpha$ to the
homology class of $\alpha$ regarded as a singular $1$-cycle.

::: pf

::: {.pf-step #homomorphism}

$h$ is a well-defined homomorphism, and it kills commutators.

::: pf-proof

A loop is a singular $1$-simplex that is a cycle, being a map of $S^1$;
homotopic loops bound a singular $2$-chain, the image of the homotopy
cylinder, so homotopic loops have equal homology classes and $h$ is well
defined. If $\alpha,\beta$ are based loops, the loop $\alpha\cdot\beta$ is the
concatenation, and its chain differs from the sum of the chains of $\alpha$
and $\beta$ by the singular $1$-simplex that is the constant path and by the
reparametrisation, both of which are boundaries of singular $2$-simplices; so
$h(\alpha\beta)=h(\alpha)+h(\beta)$. Then
$h(\alpha\beta\alpha^{-1}\beta^{-1})=h(\alpha)+h(\beta)-h(\alpha)-h(\beta)=0$,
and $h$ carries the commutator subgroup to $0$, hence induces $\bar h\colon
G/[G,G]\to H_1(X;\ZZ)$.

:::

:::

::: {.pf-step #phi}

For each singular $1$-simplex $\sigma$ with endpoints $x,y$ choose a path
$p_x$ from $x_0$ to $x$, with $p_{x_0}$ constant, and set
$\Phi(\sigma)=[\,p_x\cdot\sigma\cdot p_y^{-1}\,]$ in $G/[G,G]$. Extending by
linearity gives a well-defined homomorphism $\Phi\colon H_1(X;\ZZ)\to G/[G,G]$
with $\Phi\circ\bar h=\mathrm{id}$.

::: pf-proof

The class of $p_x\sigma p_y^{-1}$ lies in $G/[G,G]$, which is abelian, so
$\Phi$ extends to a homomorphism on $1$-chains. For a singular $2$-simplex
$\tau$ with vertices $x,y,z$, the chain
$\partial\tau=\sigma_{yz}-\sigma_{xz}+\sigma_{xy}$ is carried by $\Phi$ to the
class of the loop $p_x\cdot(\partial\tau\ \text{read as a path})\cdot
p_x^{-1}$, namely $p_x\sigma_{xy}\sigma_{yz}\sigma_{xz}^{-1}p_x^{-1}$; that
loop is the boundary of the singular $2$-simplex $\tau$, hence null-homotopic,
so $\Phi(\partial\tau)=0$. Therefore $\Phi$ vanishes on boundaries and is
defined on $H_1$. For a based loop $\alpha$,
$\Phi(h(\alpha))=\Phi(\alpha)=[p_{x_0}\alpha p_{x_0}^{-1}]=[\alpha]$, since
$p_{x_0}$ is constant; so $\Phi\circ\bar h$ is the identity of $G/[G,G]$, and
$\bar h$ is injective.

:::

:::

::: {.pf-step #inverse}

$\bar h\circ\Phi=\mathrm{id}$, so $\bar h$ is surjective and hence an
isomorphism $G/[G,G]\cong H_1(X;\ZZ)$; this gives the surjectivity the source
asks for in part (c) without choosing paths at each step of the argument.

::: pf-proof

Let $z=\sum_\sigma n_\sigma\sigma$ be a $1$-cycle. The chain representing
$h(\Phi([z]))$ is homologous to $\sum_\sigma
n_\sigma(p_{\sigma(0)}+\sigma-p_{\sigma(1)})$, the extra two terms being the
paths inserted by $\Phi$; because $\partial z=\sum_\sigma
n_\sigma(\sigma(1)-\sigma(0))=0$ as a $0$-chain, the two inserted sums are
equal, so this chain is homologous to $\sum_\sigma n_\sigma\sigma=z$. Hence
$\bar h(\Phi([z]))=[z]$ for every class, and $\bar h$ is surjective. With the
injectivity from step [](#phi){.pf-ref}, $\bar h$ is the asserted isomorphism.

:::

:::

:::

::: {.remark}

The source's final instruction says that $h$ is injective. For a nonabelian
fundamental group this is false: commutators lie in its kernel. The induced
map from the abelianisation is injective, and that is what is proved here.

:::


:::
