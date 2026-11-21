---
schema: qual/card@1
id: P-CAFA20B
kind: problem
title: 'The unique real zero of $a+z-e^{2z}$ in the left half-plane'
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
    Restructured as a Lamport proof of the argument already on the card, whose three ingredients
    (the identity |z_0 + a| = e^{2 Re z_0}, Rouche on |z + a| = 1, and conjugation symmetry) are
    correct. Added: the reverse inclusion D inside the left half-plane, which the card asserted
    as 'the disk lies in the left half-plane' and which is what makes the count of zeros in the
    disk a count in the half-plane; the bound Re z <= 1 - a on the circle, from which the Rouche
    inequality follows; the location of the single zero of the comparison function g(z) = z + a
    inside D; and the note that the count in the disk supplies existence as well as uniqueness.
    The problem block is unchanged. Not claimed: a retained solution set; the collection's
    provenance is the examination paper only.
---

::: {.problem}
Let $a \in \RR$ and $a > 2$.
Consider the equation $$(1)\quad a + z - e^{2z} = 0.$$

(a) Prove that if $z_0 \in \{\operatorname{Re}(z) < 0\}$ is a solution of (1), then $\abs{z_0 + a} < 1$.

(b) Prove the equation (1) has exactly one solution on the left half plane $\{\operatorname{Re}(z) < 0\}$.
Furthermore, prove that this solution must be a real number.
:::

::: {.solution}
Throughout $a > 2$ is real, $f(z) \coloneqq a + z - e^{2z}$, the left half-plane is $\HH^{-} \coloneqq \theset{z \mid \operatorname{Re}z < 0}$, and $D \coloneqq \theset{z \mid \abs{z+a} < 1}$. The collection's `provenance` is the Fall 2020 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #part-a}
(a) If $f(z_{0}) = 0$ and $\operatorname{Re}z_{0} < 0$ then $\abs{z_{0}+a} < 1$.

::: pf-proof
$f(z_{0}) = 0$ says $z_{0} + a = e^{2z_{0}}$, so $\abs{z_{0}+a} = \abs{e^{2z_{0}}} = e^{2\operatorname{Re}z_{0}}$, and $\operatorname{Re}z_{0} < 0$ makes this $< e^{0} = 1$ because the exponential is strictly increasing on $\RR$.

:::

:::

::: {.pf-step #cluster}
(b) The set of zeros of $f$ in $\HH^{-}$ equals the set of zeros of $f$ in $D$.

::: pf-proof
Step [](#part-a){.pf-ref} gives $\HH^{-} \cap \theset{f = 0} \subseteq D$. Conversely for $z \in D$ one has $\abs{z+a} < 1$, so $\operatorname{Re}z = \operatorname{Re}(z+a) - a \le \abs{z+a} - a < 1 - a < 0$ because $a > 2 > 1$; thus $D \subseteq \HH^{-}$ and the zeros in $D$ are zeros in $\HH^{-}$.

:::

:::

::: {.pf-step #rouche}
(b) On the circle $\abs{z+a} = 1$ one has $\abs{e^{2z}} < \abs{z+a}$.

::: pf-proof
On that circle $\operatorname{Re}z \le \abs{z+a} - a = 1 - a$, so $\abs{e^{2z}} = e^{2\operatorname{Re}z} \le e^{2(1-a)}$, and $1 - a < 0$ gives $e^{2(1-a)} < 1 = \abs{z+a}$.

:::

:::

::: {.pf-step #count}
(b) $f$ has exactly one zero in $D$.

::: pf-proof
Both $f$ and $g(z) \coloneqq z + a$ are holomorphic on a neighbourhood of the closed disc $\overline{D}$, and step [](#rouche){.pf-ref} gives the strict inequality $\abs{f - g} = \abs{e^{2z}} < \abs{g}$ on its boundary circle. By Rouché's theorem $f$ and $g$ have the same number of zeros in $D$, counted with multiplicity; $g$ has the single simple zero $-a$, which lies in $D$ since $\abs{-a + a} = 0 < 1$.

:::

:::

::: {.pf-step #unique}
(b) $f$ has exactly one zero in $\HH^{-}$.

::: pf-proof
By step [](#cluster){.pf-ref} the zeros in $\HH^{-}$ are the zeros in $D$, and step [](#count){.pf-ref} says there is exactly one of those; in particular a solution exists.

:::

:::

::: {.pf-step #real}
(b) The unique zero in $\HH^{-}$ is real.

::: pf-proof
The coefficients of the equation are real in the sense that $\overline{f(z)} = a + \bar z - e^{2\bar z} = f(\bar z)$ for every $z$, so if $f(z_{0}) = 0$ then $f(\overline{z_{0}}) = 0$. If $z_{0}$ is the unique zero in $\HH^{-}$ then $\operatorname{Re}\overline{z_{0}} = \operatorname{Re}z_{0} < 0$ puts $\overline{z_{0}}$ among the zeros in $\HH^{-}$, so $\overline{z_{0}} = z_{0}$ and $z_{0} \in \RR$.

:::

:::

::: pf-step
The answers are: (a) every left-half-plane zero $z_{0}$ satisfies $\abs{z_{0}+a} < 1$; (b) the equation has exactly one solution in $\HH^{-}$, and it is real.

::: pf-proof
Step [](#part-a){.pf-ref} is (a). For (b), steps [](#cluster){.pf-ref} and [](#count){.pf-ref} give uniqueness and existence together, and step [](#real){.pf-ref} gives that the solution is real.

:::

:::

:::
:::
