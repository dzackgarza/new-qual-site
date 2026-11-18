---
schema: qual/card@1
id: P-CASP05B
kind: problem
title: "Jensen-type inequality for bounded analytic functions with prescribed zeros"
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
    Rewritten as a Lamport structured proof of the argument already on the card, keeping the
    remark that records the multiplicity hypothesis the printed statement needs. Added: the
    verification of the three properties of phi_c (automorphism with inverse phi_{-c}, vanishing
    at c, modulus 1 on the circle via 1 - conj(c) z = z(conj z - conj c)) and |phi_c(0)| = |c|;
    the removability of the quotient's singularities from the multiplicity hypothesis; and the
    limiting argument at r tending to 1 for |g| <= M, which the prose compressed into "since
    |f| <= M and |phi_{c_j}| = 1 on the circle", where the modulus of phi_c on the circle |z| = r
    is not 1 and a limit must be taken. Not claimed: a retained solution set; the provenance
    names the examination paper.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, keeping the
    remark that records the multiplicity hypothesis the printed statement needs. Added: the
    verification of the three properties of phi_c (automorphism with inverse phi_{-c}, vanishing
    at c, modulus 1 on the circle via 1 - conj(c) z = z(conj z - conj c)) and |phi_c(0)| = |c|;
    the removability of the quotient's singularities from the multiplicity hypothesis; and the
    limiting argument at r tending to 1 for |g| <= M, which the prose compressed into "since
    |f| <= M and |phi_{c_j}| = 1 on the circle", where the modulus of phi_c on the circle |z| = r
    is not 1 and a limit must be taken. Not claimed: a retained solution set; the provenance
    names the examination paper.
---

::: {.problem}
Let $f \in H(\DD)$, and let $c_1, \ldots, c_n \in \DD \setminus \{0\}$ be zeros of $f$ listed with multiplicity not exceeding their multiplicities as zeros of $f$.
Show that if $\abs{f(z)} \leq M$ for $\abs{z} < 1$, then $$\abs{f(0)} \leq M \prod_{j=1}^{n} \abs{c_j}.$$

Hint: Consider the function $g(z) = f(z) / \prod_j \phi_{c_j}(z)$, where $\phi_{c_j}$ is a one-to-one analytic map of $\DD$ onto itself vanishing at $c_j$.
:::

::: {.remark}
The official Spring 2005 source does not specify distinctness or multiplicity
for the listed zeros. Under literal repeated enumeration the printed statement
is false; the hypothesis above records the multiplicity condition required by
the supplied Blaschke-product hint.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2005 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose, with the limiting argument at $r\uparrow1$ written out; the remark after the solution records the multiplicity hypothesis the printed statement needs.

Throughout $f\in H(\DD)$ with $\abs f\le M$, and $c_1,\dots,c_n\in\DD\setminus\set0$ are zeros of $f$ listed with multiplicity not exceeding their multiplicities.

::: pf

::: {.pf-step #factor}
For $c\in\DD$ the function $\phi_c(z)=\dfrac{z-c}{1-\overline cz}$ is an automorphism of $\DD$ vanishing at $c$, with $\abs{\phi_c}=1$ on the unit circle and $\abs{\phi_c(0)}=\abs c$.

::: pf-proof
$1-\overline cz\ne0$ on $\DD$ since $\abs{\overline cz}<1$; $\phi_c$ is a Möbius map carrying $\DD$ onto $\DD$ (its inverse is $\phi_{-c}$), it vanishes exactly at $z=c$, and on $\abs z=1$ one has $\abs{z-c}=\abs{1-\overline cz}$, since $1-\overline cz=z(\overline z-\overline c)$ gives $\abs{1-\overline cz}=\abs z\abs{\overline z-\overline c}=\abs{c-z}$. Finally $\abs{\phi_c(0)}=\abs{-c}=\abs c$.

:::

:::

::: {.pf-step #quotient}
$g=f/\prod_{j=1}^n\phi_{c_j}$ extends holomorphically across the $c_j$, and $\abs{g(0)}=\abs{f(0)}/\prod_j\abs{c_j}$.

::: pf-proof
At a zero $c$ of $f$ of multiplicity $m\ge1$, the list contains $c$ at most $m$ times by hypothesis; writing $f(z)=(z-c)^mh(z)$ with $h$ holomorphic and $h(c)\ne0$, and $\phi_c(z)=(z-c)/(1-\overline cz)$ with $1-\overline cz$ nonvanishing, the quotient has a removable singularity at $c$ and becomes holomorphic there. Away from the $c_j$ it is holomorphic. So $g$ is holomorphic on $\DD$, and at $0$ the value of each $\phi_{c_j}$ has modulus $\abs{c_j}$ by step [](#factor){.pf-ref}.

:::

:::

::: {.pf-step #bound}
$\abs{g(z)}\le M$ for every $z\in\DD$.

::: pf-proof
Fix $z\in\DD$ and let $r$ range over $($\abs z,1)$ with $r>\max_j\abs{c_j}$. On the closed disk $\abs\zeta\le r$ the function $g$ is holomorphic, so the maximum modulus principle gives $\abs{g(z)}\le\max_{\abs\zeta=r}\abs{g(\zeta)}$. There,
$$
\abs{g(\zeta)}=\frac{\abs{f(\zeta)}}{\prod_j\abs{\phi_{c_j}(\zeta)}}\le\frac{M}{\prod_j\abs{\phi_{c_j}(\zeta)}} .
$$
As $r\uparrow1$ the points $\zeta$ with $\abs\zeta=r$ tend to the unit circle uniformly, where $\abs{\phi_{c_j}}=1$ by step [](#factor){.pf-ref}, and $\phi_c$ is continuous and nonzero near the closed disk, so $\prod_j\abs{\phi_{c_j}(\zeta)}\to1$ uniformly on $\abs\zeta=r$; hence $\max_{\abs\zeta=r}\abs g\le M(1+o(1))$. Letting $r\uparrow1$ gives $\abs{g(z)}\le M$.

:::

:::

::: {.pf-step #conclusion}
$\abs{f(0)}\le M\prod_{j=1}^n\abs{c_j}$.

::: pf-proof
$\abs{g(0)}\le M$ by step [](#bound){.pf-ref}, and $\abs{g(0)}=\abs{f(0)}/\prod_j\abs{c_j}$ by step [](#quotient){.pf-ref}; multiplying by the positive number $\prod_j\abs{c_j}$ gives the claim.

:::

:::

:::
:::

::: {.remark}
The official Spring 2005 source does not specify distinctness or multiplicity
for the listed zeros. Under literal repeated enumeration the printed statement
is false; the hypothesis above records the multiplicity condition required by
the supplied Blaschke-product hint.
:::

::: {.solution}
For $c\in\DD$, put
$$
\phi_c(z)=\frac{z-c}{1-\overline c z}.
$$
This is an automorphism of $\DD$, vanishes at $c$, and satisfies
$\abs{\phi_c}=1$ on the unit circle. By the multiplicity hypothesis,
$$
g(z)=\frac{f(z)}{\prod_{j=1}^n\phi_{c_j}(z)}
$$
extends holomorphically across every $c_j$.

Fix $0<r<1$ larger than all $\abs{c_j}$. On $\abs{z}=r$, one can instead use the
finite Blaschke factors after a standard maximum-principle argument on
$\DD$; equivalently, apply the maximum principle to $g$ on disks and
let $r\uparrow1$. Since $\abs{f}\le M$ and $\abs{\phi_{c_j}(e^{it})}=1$, one obtains
$$
\abs{g(z)}\le M\qquad(z\in\DD).
$$
Evaluating at $0$ gives
$$
\abs{g(0)}
=\frac{\abs{f(0)}}{\prod_j\abs{\phi_{c_j}(0)}}
=\frac{\abs{f(0)}}{\prod_j\abs{c_j}}
\le M.
$$
Therefore
$$
\boxed{\abs{f(0)}\le M\prod_{j=1}^n\abs{c_j}}.
$$
:::
