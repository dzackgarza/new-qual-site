---
schema: qual/card@1
id: P-CH10A-3
kind: problem
title: Differentiation is a homomorphism on $\RR[x]$
classification:
  areas:
    - algebra
  topics:
    - Group Homomorphisms
relations: []
review: draft
audit:
  - event: source-checked
    by: claude-opus-5
    date: 2026-09-16
    note: Stated the Example 4 map (differentiation on R[x]) in the statement, taken from the source's own solution on page 1 of Ch10PtASltns.pdf.
  - event: source-checked
    by: claude
    date: 2026-11-18
    note: >-
      Read against Gallian, Contemporary Abstract Algebra (7th edition), Chapter 10 "Group
      Homomorphisms", printed p. 201 (PDF p. 216 of
      tmp/sources/Gallian-Contemporary-Abstract-Algebra-7e.pdf), where Example 4 reads: "Let R[x]
      denote the group of all polynomials with real coefficients under addition. For any f in R[x],
      let f' denote the derivative of f. Then the mapping f -> f' is a homomorphism from R[x] to
      itself." The stored statement matches, including that the group is R[x] under addition.
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Structured the one-line verification into numbered steps: the sum rule for derivatives as the
      single fact used, the conclusion that the map is a homomorphism of additive groups, the kernel
      as the constant polynomials, and the remark that the map is not a ring homomorphism since
      1 maps to 0, which the exercise does not ask about. No defect found in the outline's
      argument.
---

::: {.problem}
Prove that the mapping given in Example 4, the map $\phi : \RR[x] \to \RR[x]$ defined by $f \mapsto f'$, is a homomorphism.
:::

::: {.solution}

The argument is the outline's, written out; the statement was checked against Gallian, *Contemporary Abstract Algebra* (7th edition), Chapter 10, Example 4, where $\RR[x]$ is the group of polynomials with real coefficients **under addition** and the map is $f\mapsto f'$.

::: pf

::: {.pf-step #gen}
For $f,g\in\RR[x]$ and $a,b\in\RR$, $(af+bg)'=af'+bg'$.

::: pf-proof
Differentiation is defined on monomials by $(x^{k})'=kx^{k-1}$ and extended by linearity, $(\sum_{k}c_{k}x^{k})'=\sum_{k}c_{k}kx^{k-1}$; substituting the coefficients of $af+bg$, namely $ac_{k}+bd_{k}$, gives $\sum_{k}(ac_{k}+bd_{k})kx^{k-1}=a\sum_{k}c_{k}kx^{k-1}+b\sum_{k}d_{k}kx^{k-1}$, which is $af'+bg'$. The case $a=b=1$ is the sum rule.
:::

:::

::: {.pf-step #hom}
$\phi(f+g)=\phi(f)+\phi(g)$ for all $f,g$, so $\phi$ is a homomorphism of the additive group $\RR[x]$ into itself.

::: pf-proof
$\phi(f+g)=(f+g)'=f'+g'=\phi(f)+\phi(g)$ by step [](#gen){.pf-ref} with $a=b=1$. A map between groups preserving the operation is a homomorphism; the identity of $\RR[x]$ is the zero polynomial and $\phi(0)=0$, as the formula also shows.
:::

:::

::: {.pf-step #kernel}
The kernel of $\phi$ is the set of constant polynomials.

::: pf-proof
If $f=\sum_{k=0}^{n}c_{k}x^{k}$ then $f'=\sum_{k\geq1}kc_{k}x^{k-1}$, which is zero exactly when $kc_{k}=0$ for every $k\geq1$; over $\RR$ this means $c_{k}=0$ for $k\geq1$, that is $f=c_{0}$ is constant. Conversely a constant has derivative $0$.
:::

:::

::: {.pf-step #not-ring}
$\phi$ is not a homomorphism of rings, since $\phi(1)=0\neq1$; the exercise concerns the additive group only.

::: pf-proof
The derivative of the constant polynomial $1$ is $0$, while a ring homomorphism would have to send the multiplicative identity to the multiplicative identity. So the map preserves addition but not multiplication, which is why the statement is about $\RR[x]$ as a group under addition.
:::

:::

:::

:::
