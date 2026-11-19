---
schema: qual/card@1
id: P-HLKLH
kind: problem
title: A holomorphic function with $\abs{f}=1$ on the unit circle, or $\abs{f}\geq 1$ with an interior point of modulus less than $1$, covers the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Open Mapping Theorem
  - Rouché
  - Zeros
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. The Rouché input is stated once, as
    its own step, with the threshold min |g| on the circle, and both parts are then derived from
    it: (a) the boundary hypothesis |f| = 1 makes |f| attain its maximum on the boundary, so a
    nonconstant f has |f| < 1 inside and, were f zero-free, 1/f would have |1/f| < 1 inside,
    which the two cannot both satisfy; (b) the maximum principle applied to 1/f forces |f| >= 1
    throughout, contradicting the interior point. Two small repairs to the prose: it says the
    maximum-modulus principle gives |f| <= 1 and |f| >= 1 and hence |f| identically 1 forcing
    constancy, which is correct, but it does not say that strict inequality holds inside for a
    nonconstant f; and in (b) it applies the principle to 1/f without noting |1/f| <= 1 on the
    boundary is what is being used. Both are now explicit. Statement and hint unchanged; the card
    says the argument is its own.
---

::: {.problem}
Let $f$ be non-constant and holomorphic in an open set containing the closed unit disc.

(a) Show that if $\abs{f(z)} = 1$ whenever $\abs{z} = 1$, then the image of $f$ contains the unit disc.

> Hint: Show that $f(z) = w_0$ has a root for every $w_0 \in \DD$, for which it suffices to show that $f(z) = 0$ has a root.
> Conclude using the maximum modulus principle.

(b) If $\abs{f(z)} \geq 1$ whenever $\abs{z} = 1$ and there exists a $z_0\in \DD$ such that $\abs{f(z_0)} < 1$, then the image of $f$ contains the unit disc.
:::

::: {.solution}
Both parts reduce to Rouché: on the boundary circle $\abs{f}$ dominates the constant $w$ for every $\abs w<1$, so $f-w$ has exactly as many zeros in the disc as $f$, and it suffices to know that $f$ has a zero there. In (a) a zero-free $f$ would make $1/f$ holomorphic across the closed disc with $\abs{f}=\abs{1/f}=1$ on the circle, forcing $\abs f$ constant; in (b) a zero-free $f$ would force $\abs{f}\ge1$ throughout by the maximum principle on $1/f$, contradicting the point $z_0$. The argument is this card's own: no retained solution set covers this problem.

::: pf

::: {.pf-step #rouche}
If $g$ is holomorphic on a neighbourhood of $\overline\DD$ with $g\ne0$ on $\abs z=1$, then for every $\abs w<\min_{\abs z=1}\abs{g(z)}$ the functions $g-w$ and $g$ have the same number of zeros in $\DD$.

::: pf-proof
On the circle $\abs z=1$ one has $\abs{w}<\abs{g(z)}$, so the strict inequality of Rouché's theorem holds for $g$ and the constant $-w$: $g-w=g+(-w)$ has as many zeros in $\DD$, counted with multiplicity, as $g$. Both functions are holomorphic on a neighbourhood of the closed disc, which is the hypothesis Rouché's theorem requires.
:::

:::


::: {.pf-step #parta-zero}
(a) If $\abs{f(z)}=1$ on $\abs z=1$ then $f$ has a zero in $\DD$.

::: pf-proof
Suppose not. Then $f\ne0$ on $\overline\DD$: no zero in the open disc by assumption, and none on the circle since $\abs f=1$ there. So $1/f$ is holomorphic on a neighbourhood of $\overline\DD$. The maximum modulus principle applied to the nonconstant $f$ gives $\abs{f(z)}<1$ for $\abs z<1$, because the maximum of $\abs f$ on $\overline\DD$ is $1$, attained on the boundary, and a nonconstant holomorphic function on a connected domain attains no interior maximum; applied to $1/f$, whose boundary values also have modulus $1$, it gives $\abs{1/f(z)}<1$, i.e. $\abs{f(z)}>1$, for $\abs z<1$. Both cannot hold for any $z\in\DD$, which is impossible for any $z\in\DD$. Hence $f$ has a zero in $\DD$.
:::

:::


::: {.pf-step #parta}
(a) $\DD\subseteq f(\DD)$.

::: pf-proof
Let $\abs w<1$. On the circle $\abs z=1$ one has $\abs{f(z)}=1>\abs w$, so step [](#rouche){.pf-ref} applies with $g=f$ and shows that $f-w$ has as many zeros in $\DD$ as $f$ does; by step [](#parta-zero){.pf-ref} that number is at least one, so $f-w$ has a zero, that is $w=f(z)$ for some $z\in\DD$. Since $w$ was arbitrary in $\DD$, the image of $f$ contains $\DD$.
:::

:::


::: {.pf-step #partb-zero}
(b) If $\abs{f(z)}\ge1$ on $\abs z=1$ and $\abs{f(z_0)}<1$ for some $z_0\in\DD$, then $f$ has a zero in $\DD$.

::: pf-proof
If $f$ had no zero in $\DD$, then $1/f$ would be holomorphic on $\DD$ and, by the hypothesis, $\abs{1/f}\le1$ on the circle. The maximum modulus principle applied to $1/f$ on $\DD$ (with boundary values at most $1$, and using continuity on $\overline\DD$) gives $\abs{1/f(z)}\le1$, i.e. $\abs{f(z)}\ge1$, for every $z\in\DD$ — contradicting $\abs{f(z_0)}<1$. So $f$ has a zero.
:::

:::


::: {.pf-step #partb}
(b) $\DD\subseteq f(\DD)$.

::: pf-proof
Let $\abs w<1$. On the circle $\abs{f(z)}\ge1>\abs w$, so step [](#rouche){.pf-ref} with $g=f$ gives that $f-w$ has as many zeros in $\DD$ as $f$, and by step [](#partb-zero){.pf-ref} that number is at least one. Hence $w=f(z)$ for some $z\in\DD$, and since $w$ was arbitrary, $\DD\subseteq f(\DD)$.
:::

:::


::: {.pf-step #conclusion}
Both (a) and (b) hold: in either case the image of $f$ contains the unit disc.

::: pf-proof
Step [](#parta){.pf-ref} proves (a) from the boundary-modulus hypothesis, and step [](#partb){.pf-ref} proves (b) from the weaker hypothesis with the interior point; in both cases the conclusion is $\DD\subseteq f(\DD)$, and in both the only input beyond the maximum modulus principle is Rouché's theorem in the form of step [](#rouche){.pf-ref}.
:::

:::

:::
:::
