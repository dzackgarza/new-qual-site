---
schema: qual/card@1
id: P-CAFA19B
kind: problem
title: "Zero-free disk and characterization of extremal functions for bounded analytic functions"
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
    stood. Added: the normalisation g = 2f with 0 < 2r < 1; the Schwarz-Pick inequality written
    out with its two denominators; the identification of the left side with |g(0)| = 2r and the
    right side with |a|; the explicit computation e^{i theta} = -e^{-i phi} from g(0) = 2r and
    the substitution giving the displayed automorphism; and, for the converse that (b) asks
    for, the verification that each displayed f is a disc automorphism halved, so |f| <= 1/2,
    that f(0) = r is real, and that the zero at z = 2 r e^{i phi} is not cancelled because
    1 - 4r^2 != 0. Not claimed: a retained solution set; the provenance names the examination
    paper.
---

::: {.problem}
Let $f$ be analytic on $\DD$ with $\abs{f(z)} \leq 1/2$ on $\DD$ and $f(0) = r \in \RR$, where $0 < r < 1/2$.

(a) Prove that $f(z)$ has no zeros in the disk $\{\abs{z} < 2r\}$.

(b) Can $f(z)$ have a zero on the circle $\{\abs{z} = 2r\}$?
If so, find all such functions $f(z)$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Fall 2019 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $f$ is analytic on $\DD$ with $\abs{f}\le1/2$ and $f(0)=r\in(0,1/2)$, and $g\coloneqq2f$.

::: pf

::: {.pf-step #normalisation}
$g$ is a holomorphic self-map of $\DD$ with $g(0)=2r$, where $0<2r<1$.

::: pf-proof
$\abs{g}=2\abs{f}\le1$ on $\DD$ and $g(0)=2r$; since $0<r<1/2$, $2r\in(0,1)$.

:::

:::

::: {.pf-step #part-a}
$f$, hence $g$, has no zero with $\abs{z}<2r$.

::: pf-proof
Let $a\in\DD$ with $g(a)=0$. Schwarz–Pick applied to $g$ at the points $0$ and $a$ gives
$$
\abs{\frac{g(0)-g(a)}{1-\overline{g(a)}\,g(0)}}\le\abs{\frac{0-a}{1-\overline a\cdot0}} ,
$$
whose left side is $\abs{g(0)}=2r$ and whose right side is $\abs a$; so $2r\le\abs a$. Hence no zero of $g$, and so none of $f$, satisfies $\abs a<2r$.

:::

:::

::: {.pf-step #part-b-zeros}
If $f(a)=0$ with $\abs a=2r$, then $g$ is a disk automorphism
$$
g(z)=e^{i\theta}\frac{z-a}{1-\overline a z}.
$$

::: pf-proof
$g$ is a holomorphic self-map of $\DD$ and the inequality of step [](#part-a){.pf-ref} is an equality at the pair of distinct points $0\ne a$; the equality case of Schwarz–Pick then says that $g$ is a disk automorphism, and every automorphism of $\DD$ has the displayed form with $\theta\in\RR$.

:::

:::

::: {.pf-step #part-b-form}
A zero of $f$ on $\abs z=2r$ forces $a=2re^{i\phi}$ and
$$
f(z)=\frac12\cdot\frac{2r-e^{-i\phi}z}{1-2re^{-i\phi}z},\qquad \phi\in\RR,
$$
and conversely each of these functions has the required properties.

::: pf-proof
Write $a=2re^{i\phi}$. The condition $g(0)=2r$ with the form of step [](#part-b-zeros){.pf-ref} gives $e^{i\theta}(-a)=2r$, that is $e^{i\theta}=-2r/a=-e^{-i\phi}$. Substituting, $g(z)=-e^{-i\phi}(z-2re^{i\phi})/(1-2re^{-i\phi}z)=(2r-e^{-i\phi}z)/(1-2re^{-i\phi}z)$, and $f=g/2$ gives the displayed family. Conversely, for each $\phi$ the displayed $f$ is a disk automorphism divided by $2$, so $\abs{f}\le1/2$; at $0$ it equals $\frac12\cdot2r=r\in\RR$; and at $z=2re^{i\phi}$ the numerator $2r-e^{-i\phi}\cdot2re^{i\phi}=2r-2r=0$, so $f$ vanishes there, provided the zero is not cancelled by the denominator: the denominator there is $1-2re^{-i\phi}\cdot2re^{i\phi}=1-4r^2\ne0$ because $2r<1$. So yes, $f$ can have a zero on the circle, and exactly these functions do.

:::

:::

::: {.pf-step #conclusion}
(a) $f$ has no zeros in $\abs z<2r$; (b) $f$ may vanish on $\abs z=2r$, and precisely the functions of step [](#part-b-form){.pf-ref} do.

::: pf-proof
Step [](#part-a){.pf-ref} is (a), and steps [](#part-b-zeros){.pf-ref} and [](#part-b-form){.pf-ref} together settle (b), which asks first whether it can happen — yes, by the converse in step [](#part-b-form){.pf-ref} — and then for all such functions, which is the displayed family.

:::

:::

:::
:::
