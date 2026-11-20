---
schema: qual/card@1
id: E-HAT-4.1-14
kind: problem
title: "Homotopy equivalent skeleta"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Read against the book (AT.txt:17874-17875 for the statement, 17395-17397 for cellular approximation).
    Correct: cellular approximation makes f and g cellular, so they restrict to the n-skeleta; the
    homotopy gf ~ id restricted to X^n x I is a map of CW pairs already cellular on X^n x dI, so its
    relative form homotopes it rel the two ends to a cellular map, whose image lies in X^{n+1} = X^n
    because X^n x I has dimension n+1 and there are no (n+1)-cells. The same for f_n g_n, so the
    restrictions are homotopy inverses. The (n+1)-cell hypothesis is used exactly where it is needed.
    Not checked: nothing beyond the written argument.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set is cited on the card and none was
    located among the retained Hatcher sets, so the argument is the card's own. Checked against
    Hatcher, Section 4.1 Exercise 14, printed p. 359, and the cellular approximation theorem
    (p. 349). Each step re-read: cellular approximations of the two homotopy inverses still
    compose to maps homotopic to the identities; a cellular map carries the n-skeleton into the
    n-skeleton, which is what allows the restrictions f_n and g_n; and the homotopy
    g f = id restricted to X^n x I is a homotopy from an (n+1)-dimensional complex, so its
    cellular approximation lands in the (n+1)-skeleton, which is the n-skeleton precisely because
    there are no (n+1)-cells. The same argument is applied to Y. Not claimed: the result for
    skeleta of a single complex, or any statement about the maps themselves rather than the
    skeleta.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The card said no retained solution set solves §4.1 Exercise 14, and that is false. Proudfoot's
    Homework #6, retained as `tmp/sources/uoregon-proudfoot-634-hw6.pdf`, solves exactly this exercise,
    by the same argument: replace f and g by cellular maps, then apply cellular approximation to the
    homotopy g f = id_X so that it restricts to X_n x [0,1] -> X_{n+1} = X_n. The rendered sentence now
    cites that solution by set and exercise number and says what the card adds — the relative form of
    cellular approximation keeping the ends fixed, and where the hypothesis on the (n+1)-cells is used.
    The proof steps are unchanged. Page locators removed from the same paragraph; Theorem 4.8 and
    Example 4.11 are cited by number.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.1 Exercise 14, Theorem 4.8,
    Example 4.11 and the published solution named above. Correct: cellular maps carry n-skeleta into
    n-skeleta; the restricted homotopy is homotopic rel X^n x boundary to a cellular one by the
    relative form, so it lands in the (n+1)-skeleton, which is the n-skeleton because there are no
    (n+1)-cells; and the same argument with X and Y exchanged gives the other composite. No step
    changed in this pass.
---

::: {.problem}
Use cellular approximation to show that the $n$-skeleta of homotopy equivalent CW complexes without cells of dimension $n+1$ are also homotopy equivalent.
:::

::: {.solution}
The argument is that of a retained published solution: **Nicholas Proudfoot, *Math 634: Algebraic Topology I* (University of Oregon, Fall 2015), Solutions to Homework #6, §4.1 Exercise 14**, which replaces $f$ and $g$ by cellular maps and then applies cellular approximation to the homotopy $g\circ f\simeq\operatorname{id}_X$ to land it in $X_n\times[0,1]\to X_{n+1}=X_n$. Checked against Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 14, and against the cellular approximation theorem of §4.1, Theorem 4.8, together with its relative form for homotopies, Example 4.11. The card's own contribution is the explicit statement that the relative form is what keeps the ends fixed, and the identification of where the hypothesis on the $(n+1)$-cells is used.

::: pf

::: {.pf-step #maps}
There are maps $f:X\to Y$ and $g:Y\to X$, homotopic to cellular maps, with $g f\simeq\operatorname{id}_X$ and $f g\simeq\operatorname{id}_Y$.

::: pf-proof
$X$ and $Y$ are homotopy equivalent, so homotopy inverse maps $f$ and $g$ exist. By the cellular approximation theorem each is homotopic to a cellular map; replacing $f$ and $g$ by those cellular maps, again written $f$ and $g$, keeps the two homotopy relations $g f\simeq\operatorname{id}_X$ and $f g\simeq\operatorname{id}_Y$, because a homotopy is unchanged up to homotopy by replacing one of its ends.
:::

:::

::: {.pf-step #restrict}
$f(X^n)\subseteq Y^n$ and $g(Y^n)\subseteq X^n$, so $f$ and $g$ restrict to maps $f_n:X^n\to Y^n$ and $g_n:Y^n\to X^n$.

::: pf-proof
A cellular map carries the $n$-skeleton into the $n$-skeleton: the image of an $n$-cell is a cell of dimension at most $n$, and the image of a point of the $n$-skeleton is a point of the $n$-skeleton.
:::

:::

::: {.pf-step #left}
$g_n f_n\simeq\operatorname{id}_{X^n}$ through maps into $X^n$.

::: pf-proof
$g_n f_n:X^n\to X^n$ is the restriction of $g f$, and $g f\simeq\operatorname{id}_X$ through a homotopy $H:X\times I\to X$. Restricting $H$ to $X^n\times I$ gives a homotopy from $g_n f_n$ to $\operatorname{id}_{X^n}$ as maps into $X$. The product CW structure on $X^n\times I$ has cells $e^p\times\{0\}$, $e^p\times\{1\}$ and $e^p\times(0,1)$ for cells $e^p$ of $X^n$ with $p\le n$, all of dimension at most $n+1$; by cellular approximation for homotopies, relative to $X^n\times\partial I$, the restricted homotopy is homotopic rel $X^n\times\partial I$ to a cellular map $H':X^n\times I\to X$. A cellular map from an $(n+1)$-dimensional complex has image in the $(n+1)$-skeleton, so $H'(X^n\times I)\subseteq X^{n+1}=X^n$, the last equality because $X$ has no $(n+1)$-cells. Since $H'$ agrees with $H$ on $X^n\times\partial I$, it is a homotopy from $g_n f_n$ to $\operatorname{id}_{X^n}$ with values in $X^n$.
:::

:::

::: {.pf-step #right}
$f_n g_n\simeq\operatorname{id}_{Y^n}$ through maps into $Y^n$.

::: pf-proof
The argument of step [](#left){.pf-ref} applies with $X$ and $Y$ interchanged and with $f$ and $g$ interchanged: $Y$ likewise has no $(n+1)$-cells, and $f g\simeq\operatorname{id}_Y$.
:::

:::

::: {.pf-step}
$X^n\simeq Y^n$.

::: pf-proof
Steps [](#restrict){.pf-ref}, [](#left){.pf-ref} and [](#right){.pf-ref} exhibit $f_n:X^n\to Y^n$ and $g_n:Y^n\to X^n$ with both composites homotopic to the respective identities, so $f_n$ is a homotopy equivalence with homotopy inverse $g_n$:
$$
\boxed{X^n\simeq Y^n.}
$$
The hypothesis that neither complex has cells in dimension $n+1$ is used twice, once for $X$ and once for $Y$, in the identification of the $(n+1)$-skeleton with the $n$-skeleton.
:::

:::

:::
:::
