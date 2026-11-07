---
schema: qual/card@1
id: E-HAT-2.2-2
kind: problem
title: Map of $S^{2n}$ has fixed point or antipodal point; $\RP^{2n}$ maps have fixed points
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Point Theorems
  - Projective Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.2, Exercise 2.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both parts: a fixed-point-free map of $S^{2n}$ has degree $(-1)^{2n+1}$, $-f$ is
    fixed-point-free exactly when $f$ avoids $-x$, and $\deg(-f)=-\deg f$ gives the contradiction;
    the lift of $g\circ p$ through $p$ exists because $\pi_1(S^{2n})=0$ and $[x]=[-x]$ turns
    $\tilde g(x)=\pm x$ into a fixed class; and a real-eigenvector-free matrix is injective on
    lines, so it induces a fixed-point-free map of $\RP^{2n-1}$, with the block rotation having
    eigenvalues $\pm i$.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Read again against Hatcher, §2.2 Exercise 2, printed p. 155: the printed statement matches the
    card word for word, including the third part's "linear transformations R^{2n} -> R^{2n}
    without eigenvectors". Checked on printed p. 134 the three degree properties the proof cites:
    (f) the antipodal map has degree (-1)^{n+1}, (g) a fixed-point-free map has degree (-1)^{n+1},
    and (d) multiplicativity, so deg(-f) = -deg f as used in the second part's contradiction. The
    lift of g circ p through the quotient p exists because pi_1(S^{2n}) = 0, and the exhibited
    block rotation has eigenvalues plus or minus i and so no real eigenvector. No defect.
---

::: {.problem}
Given a map $f: S^{2n} \to S^{2n}$, show that there is some point $x \in S^{2n}$ with either $f(x) = x$ or $f(x) = -x$.
Deduce that every map $\RP^{2n} \to \RP^{2n}$ has a fixed point.
Construct maps $\RP^{2n-1} \to \RP^{2n-1}$ without fixed points from linear transformations $\RR^{2n} \to \RR^{2n}$ without eigenvectors.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
Every map $f: S^{2n} \to S^{2n}$ has $f(x) = x$ or $f(x) = -x$ for some $x$.

::: pf-proof

::: {.pf-step #s1-1}
If $f(x) \neq x$ for all $x$, then $f$ has no fixed point, so $\deg f = (-1)^{2n+1} = -1$.

::: pf-proof
a fixed-point-free map of $S^m$ has degree $(-1)^{m+1}$: the antipodal map $x\mapsto -x$ has degree $(-1)^{m+1}$ by property (f) of degree (Hatcher, p. 134) and any fixed-point-free map is homotopic to it, as in property (g) on the same page.
:::

:::

::: pf-step
If also $f(x) \neq -x$ for all $x$, then $-f$ has no fixed point, so $\deg(-f) = -1$.

::: pf-proof
$-f$ is fixed-point-free, so by step [](#s1-1){.pf-ref} its degree is $(-1)^{2n+1} = -1$.
:::

:::

::: {.pf-step #s1-3}
But $\deg(-f) = (-1)^{2n+1}\deg f = -\deg f = -(-1) = 1$, contradiction.

::: pf-proof
$-f$ is the composite of the antipodal map with $f$, which has degree $(-1)^{2n+1}$ by property (f) of degree (Hatcher, p. 134), so $\deg(-f) = (-1)^{2n+1}\deg f = -\deg f$ by property (d) on the same page.
:::

:::

::: pf-step
Hence $f(x) = x$ or $f(x) = -x$ for some $x$.

::: pf-proof
Step [](#s1-3){.pf-ref} contradicts the assumption that neither holds.
:::

:::

:::

:::

::: {.pf-step #s2}
Every map $\RP^{2n} \to \RP^{2n}$ has a fixed point.

::: pf-proof

::: pf-step
For a map $g: \RP^{2n} \to \RP^{2n}$ there is a map $\tilde g: S^{2n} \to S^{2n}$ with $p \circ \tilde g = g \circ p$, where $p: S^{2n} \to \RP^{2n}$ is the quotient map.

::: pf-proof
The map $g \circ p: S^{2n} \to \RP^{2n}$ lifts through the covering $p$ by the lifting criterion (Hatcher, Proposition 1.33, p. 61), whose hypotheses hold because $S^{2n}$ is path connected and locally path connected and $\pi_1(S^{2n}) = 0$ for $2n\ge2$ (Proposition 1.14, p. 35).
:::

:::

::: pf-step
By step [](#s1){.pf-ref}, $\tilde g(x) = x$ or $\tilde g(x) = -x$ for some $x$.

::: pf-proof
apply step [](#s1){.pf-ref} to $\tilde g$.
:::

:::

::: pf-step
In either case $g([x]) = [x]$.

::: pf-proof
$[x] = [-x]$ in $\RP^{2n}$, and $g([x]) = [\tilde g(x)] = [x]$ or $[-x] = [x]$.
:::

:::

:::

:::

::: {.pf-step #s3}
A linear map $\RR^{2n} \to \RR^{2n}$ without real eigenvectors induces a map $\RP^{2n-1} \to \RP^{2n-1}$ without fixed points.

::: pf-proof

::: pf-step
A linear map $T: \RR^{2n} \to \RR^{2n}$ without real eigenvectors induces a map $\RP^{2n-1} \to \RP^{2n-1}$.

::: pf-proof
$T$ has no kernel, since a nonzero vector in the kernel would be an eigenvector for $0$; so $T$ sends each line through the origin to a line, and $[v] \mapsto [Tv]$ is a continuous map of $\RP^{2n-1}$. A fixed line $[v] = [Tv]$ would make $v$ an eigenvector.
:::

:::

::: pf-step
Example: $T(x_1, \dots, x_{2n}) = (-x_2, x_1, -x_4, x_3, \dots, -x_{2n}, x_{2n-1})$, a block rotation by $90^\circ$ in each coordinate pair.

::: pf-proof
$T$ has no real eigenvectors (its eigenvalues are $\pm i$), so the induced map on $\RP^{2n-1}$ has no fixed point.
:::

:::

:::

:::

:::
The three parts are checked against **Kenneth DeMason, *M382C Full Credit HW Problems* (2021)**, Hatcher 2.2.2, printed p. 64 (`tmp/sources/demason-m382c-hatcher-20210404.pdf`): fixed-point-freeness gives antipodal degree $-1$, absence of antipodal matching identities gives degree $1$, lifting to $S^{2n}$ gives the projective-space result, and the standard no-real-eigenvector rotation gives the odd-dimensional fixed-point-free example. The card contains the same computations and their explicit homotopies.


:::
