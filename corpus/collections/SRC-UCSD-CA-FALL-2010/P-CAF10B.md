---
schema: qual/card@1
id: P-CAF10B
kind: problem
title: "Meromorphic functions asymptotic to tan z in the plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Poles
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The conclusion $f = c\tan z$, $c \ne 0$, is correct and is kept;
    the card's argument through the bounded quotient g = 1 - tan/f is also kept and is now
    written as steps. Added: the proof that f is not identically zero, without which the
    quotient is not defined anywhere; the reason Omega is connected, so that the identity
    theorem can be used at the end; and the removable-singularity step spelled out at an
    arbitrary point a — including the case where a is a pole of tan and where a is a zero of f,
    which the card passed over with 'bounded on a punctured neighborhood'. No statement was
    changed. Not claimed: a retained solution set; the collection's provenance is the
    examination paper only.
---

::: {.problem}
Find all functions $f(z)$ that satisfy the two requirements:

(i) $f(z)$ is meromorphic in the plane $\CC$.

(ii) There exists a constant $C > 0$ such that $\abs{f(z) - \tan z} \leq C\abs{f(z)}$ for all $z$ outside the poles of $f(z)$ and $\tan z$.
:::

::: {.solution}
Throughout $\tan z = \sin z/\cos z$ is meromorphic on $\CC$ with simple poles at $\pi/2 + k\pi$, $k \in \ZZ$, and the two requirements are: (i) $f$ is meromorphic in the plane; (ii) there is $C > 0$ with $\abs{f(z) - \tan z} \le C\abs{f(z)}$ at every point where neither $f$ nor $\tan$ has a pole. The collection's `provenance` is the Fall 2010 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #in}
Every $f = c\tan z$ with $c \in \CC^{*}$ satisfies (i) and (ii).

::: pf-proof
$c\tan z$ is meromorphic as a nonzero constant multiple of the meromorphic function $\tan$. At a point where $\tan$ has no pole, $\abs{f - \tan} = \abs{c-1}\abs{\tan} = \frac{\abs{c-1}}{\abs{c}}\abs{f}$, so (ii) holds with $C = \abs{c-1}/\abs{c}$.

:::

:::

::: {.pf-step #nonzero}
If $f$ satisfies (i) and (ii) then $f$ is not identically zero.

::: pf-proof
At a point where $f(z) = 0$ and $\tan z \ne 0$, condition (ii) would read $\abs{\tan z} \le 0$, which is false; there are infinitely many such points, so $f$ cannot vanish identically.

:::

:::

::: {.pf-step #g}
On $\Omega \coloneqq \CC$ minus the zeros of $f$, the function $g \coloneqq 1 - \tan/f$ is meromorphic with $\abs{g} \le C$ wherever it is defined.

::: pf-proof
$\Omega$ is the complement of a closed discrete set, hence open, and it is connected: a discrete closed set does not separate the plane. Both $\tan$ and $f$ are meromorphic and $f$ has no zeros on $\Omega$, so the quotient $\tan/f$ is meromorphic there, and so is $g$. Dividing the inequality of (ii) by $\abs{f} \ne 0$ gives $\abs{1 - \tan/f} \le C$, which is $\abs{g} \le C$, at every point of $\Omega$ where $\tan$ has no pole.

:::

:::

::: {.pf-step #removable}
$g$ extends to a holomorphic function on $\CC$, still bounded by $C$.

::: pf-proof
Fix $a \in \CC$ and a punctured disc $D$ about $a$ small enough that it meets neither the poles of $f$ nor the zeros of $f$ except possibly at $a$, and contains no pole of $\tan$ except possibly at $a$. On $D$ minus at most one point $g$ is defined and satisfies $\abs{g} \le C$; by continuity of the meromorphic $g$ it satisfies the bound on all of $D$ minus that one point. So $g$ is bounded on the punctured disc, and Riemann's removable singularity theorem makes $a$ a removable singularity. As $a$ was arbitrary, $g$ extends holomorphically to $\CC$, and the bound $\abs{g} \le C$ passes to the extension by continuity.

:::

:::

::: {.pf-step #constant}
$g$ is constant: $g \equiv \gamma$ for some $\gamma \in \CC$ of modulus at most $C$.

::: pf-proof
The extension of step [](#removable){.pf-ref} is a bounded entire function, so Liouville's theorem makes it constant.

:::

:::

::: {.pf-step #lambda}
$\lambda \coloneqq 1 - \gamma$ is nonzero.

::: pf-proof
Were $\lambda = 0$, then $1 - \tan/f = 1$ identically, so $\tan/f = 0$, so $\tan = 0$ at every point of $\Omega$ where $\tan$ and $f$ are finite and $f \ne 0$. That set is a nonempty open set, since $f$ is a nonzero meromorphic function and $\tan$ has only simple zeros; the identity theorem then gives $\tan \equiv 0$, which is false, for instance at $z = \pi/2$, where $\tan$ has a pole.

:::

:::

::: pf-step
The functions satisfying (i) and (ii) are exactly $\boxed{f(z) = c\tan z \text{ with } c \in \CC^{*}}$.

::: pf-proof
Step [](#in){.pf-ref} shows that every such $f$ works. Conversely, for $f$ satisfying (i) and (ii), steps [](#constant){.pf-ref} and [](#lambda){.pf-ref} give $\tan/f = \lambda \ne 0$ as meromorphic functions on $\Omega$, hence $f = \lambda^{-1}\tan$ on $\Omega$ and therefore on $\CC$ by meromorphic continuation; and $c \coloneqq \lambda^{-1}$ is a nonzero complex number.

:::

:::

:::
:::
