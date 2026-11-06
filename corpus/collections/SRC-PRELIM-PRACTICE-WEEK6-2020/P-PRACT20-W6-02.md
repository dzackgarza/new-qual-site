---
schema: qual/card@1
id: P-PRACT20-W6-02
kind: problem
title: The nested radical $\sqrt{x+\sqrt{x+\sqrt{x+\cdots}}}$
classification:
  areas:
  - prelim
  topics:
  - Sequences
  - Monotone Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-PRACTICE-WEEK6-2020 has an empty provenance list, and the only
    retained pages of the practice sheet are the three page images
    assets/attachments/prelim-practice-week6-2020/page-4.png, page-5.png and
    page-11.png, none of which carries this problem; so there is no printed page
    to compare the statement with. What was checked is the statement as it stands
    on the card: the recursion, the fixed point equation and the behaviour as x decreases to 0 were re-derived; the statement is the standard reading of the nested radical, which the solution answers
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. Monotone bounded convergence, the fixed point equation, and the jump of the limit at x = 0
---

::: {.problem}
Fix $x > 0$. Give a rigorous meaning to $\sqrt{x + \sqrt{x + \sqrt{x + \cdots}}}$ by proving that the sequence
$$
a_{0} = \sqrt{x}, \quad a_{n} = \sqrt{x + a_{n-1}}, \quad n = 1, 2, 3, \dots
$$
converges and finding the limit.
What happens as $x \searrow 0$?
:::

::: {.solution}

Fix $x>0$ and let $a_0=\sqrt x$, $a_n=\sqrt{x+a_{n-1}}$; let
$L=\frac{1+\sqrt{1+4x}}{2}$ be the positive root of $L^2=x+L$.

::: pf

::: {.pf-step #bounded}

$0<a_n\le L$ for all $n$, and $(a_n)$ is nondecreasing.

::: pf-proof

All terms are positive. Since $L>0$ and $L^2=x+L\ge x$, we get $a_0=\sqrt x\le
L$; if $a_{n-1}\le L$ then $x+a_{n-1}\le x+L=L^2$ and $a_n=\sqrt{x+a_{n-1}}\le
L$, which gives the bound by induction. Monotonicity: $a_1=\sqrt{x+\sqrt
x}\ge\sqrt x=a_0$, and $a_{n-1}\ge a_{n-2}$ gives
$a_n=\sqrt{x+a_{n-1}}\ge\sqrt{x+a_{n-2}}=a_{n-1}$.

:::

:::

::: {.pf-step #converges}

$(a_n)$ converges, and its limit is $L$.

::: pf-proof

A nondecreasing sequence bounded above converges, so $a_n\to a$ with $a\le L$.
The square root is continuous, so passing to the limit in the recursion gives
$a=\sqrt{x+a}$, that is $a^2=x+a$. The roots of $t^2-t-x=0$ are
$\frac{1\pm\sqrt{1+4x}}{2}$, and $a\ge0$ selects $L$. So the nested radical,
defined as the limit of this recursion, equals $\frac{1+\sqrt{1+4x}}{2}$.

:::

:::

::: {.pf-step #xzero}

As $x\searrow0$ the limit tends to $1$, while at $x=0$ every term is $0$ and
the limit is $0$.

::: pf-proof

$x\mapsto\frac{1+\sqrt{1+4x}}{2}$ is continuous at $0$ with value $1$, so the
limit of the sequence tends to $1$ as $x\to0^{+}$. At $x=0$ the recursion is
$a_0=0$, $a_n=\sqrt{a_{n-1}}$, so all terms vanish and the limit is $0$. Hence
the limiting value is discontinuous at $x=0$ even though each $a_n$ is
continuous there, and the convergence is not uniform in $x$ on any interval
$(0,\delta)$.

:::

:::

:::


:::
