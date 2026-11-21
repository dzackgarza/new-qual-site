---
schema: qual/card@1
id: P-CASP06F
kind: problem
title: "Jensen's inequality for zeros of an analytic function on a disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: that the denominator of the Blaschke factor does not vanish on the closed
    disk (otherwise |a| R < R^2, a contradiction), so B_a is holomorphic there; the boundary
    computation |R^2 - conj(a) z| = R |a - z| from R^2 = z conj(z); the verification that the
    quotient has removable singularities at the zeros because numerator and denominator carry
    the same power of the same linear factor; and the value |B_a(0)| = |a|/R feeding the final
    substitution. Not claimed: a retained solution set; the provenance names the examination
    paper.
---

::: {.problem}
Let $f$ be holomorphic on the closed disc of radius $R$ and assume that $f(0) \neq 0$.
Let the zeros of $f$ in the open disc be ordered by increasing absolute value, $z_1, z_2, \ldots, z_N$, each zero being repeated according to its multiplicity.
Prove that $$\abs{f(0)} \leq \frac{\sup_{\abs{z}=R} \abs{f(z)}}{R^N} \abs{z_1 z_2 \cdots z_N}.$$
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2006 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose: the Blaschke factors remove the zeros without changing the boundary modulus, and the maximum principle finishes.

Throughout $f$ is holomorphic on the closed disc $\abs z\le R$ with $f(0)\ne0$, and $z_1,\dots,z_N$ are the zeros of $f$ in $\abs z<R$, repeated by multiplicity.

::: pf

::: {.pf-step #blaschke}
For $a$ with $\abs a<R$ the function $B_a(z)=\dfrac{R(z-a)}{R^2-\overline a z}$ is holomorphic on a neighbourhood of $\abs z\le R$, vanishes simply at $a$, has no other zero there, and satisfies $\abs{B_a(z)}=1$ on $\abs z=R$.

::: pf-proof
The denominator is nonzero on $\abs z\le R$: if $R^2=\overline a z$ with $\abs z\le R$ then $R^2=\abs a\abs z\le\abs aR<R^2$, a contradiction. So $B_a$ is holomorphic on a neighbourhood and vanishes exactly at $z=a$, simply, since $R(a-a)=0$ and the denominator is nonzero there. On $\abs z=R$ use $R^2=z\overline z$: $R^2-\overline az=z\overline z-\overline az=-z\,\overline{(a-z)}$, so $\abs{R^2-\overline az}=\abs z\abs{a-z}=R\abs{z-a}$; hence $\abs{B_a(z)}=R\abs{z-a}/(R\abs{z-a})=1$.

:::

:::

::: {.pf-step #quotient}
$g=f/\prod_{j=1}^NB_{z_j}$ extends holomorphically over the zeros and is zero-free on $\abs z<R$, and $\abs{g}= \abs f$ on $\abs z=R$.

::: pf-proof
Near a zero $z_j$ of multiplicity $m_j$ the numerator has a factor $(z-z_j)^{m_j}$, and the product of the $B_{z}$ over the $m_j$ copies of $z_j$ in the list has the same factor $(z-z_j)^{m_j}$ times a nonvanishing holomorphic factor; the quotient therefore has a removable singularity at $z_j$ and is holomorphic and nonzero there. Away from the zeros the quotient is holomorphic and nonzero, and by step [](#blaschke){.pf-ref} there are no other zeros of $g$ in the disk. On $\abs z=R$ each factor has modulus $1$, so $\abs g=\abs f$.

:::

:::

::: {.pf-step #value-at-zero}
$\abs{g(0)}=\abs{f(0)}\,R^N/\prod_{j=1}^N\abs{z_j}$.

::: pf-proof
$\abs{B_a(0)}=\abs{R(0-a)}/\abs{R^2-\bar a\cdot0}=R\abs a/R^2=\abs a/R$, so $\prod_j\abs{B_{z_j}(0)}=\prod_j\abs{z_j}/R^N$ and the claim follows from $g(0)=f(0)/\prod_jB_{z_j}(0)$.

:::

:::

::: {.pf-step #conclusion}
$\abs{f(0)}\le\dfrac{\sup_{\abs z=R}\abs{f(z)}}{R^N}\abs{z_1z_2\cdots z_N}$.

::: pf-proof
$g$ is holomorphic on a neighbourhood of the closed disc, so the maximum modulus principle gives $\abs{g(0)}\le\sup_{\abs z=R}\abs{g(z)}=\sup_{\abs z=R}\abs{f(z)}$ by step [](#quotient){.pf-ref}. Substituting the value from step [](#value-at-zero){.pf-ref} and multiplying by $\prod_j\abs{z_j}/R^N>0$ gives the displayed inequality; note $\abs{z_1\cdots z_N}=\prod_j\abs{z_j}$.

:::

:::

:::
:::
