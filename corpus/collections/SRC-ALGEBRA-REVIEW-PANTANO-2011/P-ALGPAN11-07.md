---
schema: qual/card@1
id: P-ALGPAN11-07
kind: problem
title: Properties of the operation a*b = a+b+2ab on the rationals
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Statement and choices transcribed from the ALGEBRA_REVIEW1.pdf page render; the machine extractions were garbled at this item.
---
::: {.problem}
Let $*$ be the binary operation on the rational numbers given by $a*b=a+b+2ab$.
Which of the following are true?

I. $*$ is commutative.

II. There is a rational number that is a $*$-identity.

III. Every rational number has a $*$-inverse.

(A) I only (B) II only (C) I and II only (D) I and III only (E) I, II, and III
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
I is true.

::: pf-proof
$a*b=a+b+2ab=b+a+2ba=b*a$, because addition and multiplication in $\QQ$ are commutative.
:::

:::

::: {.pf-step #s2}
II is true: $0$ is a $*$-identity.

::: pf-proof
$a*0=a+0+0=a$ for every $a\in\QQ$, and $0*a=a$ by step [](#s1){.pf-ref}.
:::

:::

::: {.pf-step #s3}
III is false: $-\tfrac12$ has no $*$-inverse.

::: pf-proof
One has $1+2(a*b)=(1+2a)(1+2b)$. So $a*b=0$ if and only if $(1+2a)(1+2b)=1$. For $a=-\tfrac12$ the left side is $0$ for every $b$, so no $b$ satisfies $a*b=0$, the identity of step [](#s2){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} show that exactly I and II are true: choice (C).
:::

:::

:::
