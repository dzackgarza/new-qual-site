---
schema: qual/card@1
id: E-MUN-1-3
kind: problem
title: Contrapositive, converse, and truth of conditional statements
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §1 Exercise 3, printed p. 14, both parts as
    printed; the stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.3,
    printed p. 6 (tmp/sources/munkres-solutions-whitman.pdf). His truth values are the
    card's: (a) the statement and its contrapositive are true and the converse fails at
    x = 2; (b) all three fail, at x = 1/2 for the statement and its contrapositive and at
    x = -1 for the converse. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the transcribed answer into numbered steps: the four statements of each part are
    written out, the equivalence of an implication with its contrapositive is separated from the
    truth values, and each truth value is decided by an exhibited point or by a sign computation.
    Checked in the process: the two negations (x^2 - x > 0 negated to x^2 - x <= 0, x < 0 negated
    to x >= 0) are correct over the reals by trichotomy, and each sign computation is arithmetic
    (x once and x - 1 once negative in (a); 1/4 - 1/2 = -1/4 and 1 + 1 = 2 in (b)). Not checked
    this session: the page of the Whitman manual, which the earlier transcription note records as
    printed p. 6 of tmp/sources/munkres-solutions-whitman.pdf; nothing in the restructured text
    goes beyond the argument recorded there and the truth values are unchanged.
---

::: {.exercise}

(a) Write the contrapositive and converse of the following statement: "If $x < 0$, then $x^2 - x > 0$," and determine which (if any) of the three statements are true.

(b) Do the same for the statement "If $x > 0$, then $x^2 - x > 0$ ."
:::

::: {.solution}

The answer, including all six truth values, is that of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.3, printed p. 6** (`tmp/sources/munkres-solutions-whitman.pdf`); the arithmetic is shown here and the restatement of each implication is written out before it is judged.

Throughout, $P\Longrightarrow Q$ is read as the material conditional, which is false exactly when $P$ is true and $Q$ is false; this is the convention under which Munkres, *Topology* (2000), §1 asks the exercise.

::: pf

::: {.pf-step #contrapositive}
For statements $P,Q$ over a fixed universe, the contrapositive of $P\Longrightarrow Q$ is $(\text{not }Q)\Longrightarrow(\text{not }P)$, and it has the same truth value as $P\Longrightarrow Q$.

::: pf-proof
If $P\Longrightarrow Q$ is true and not $Q$ holds, then $P$ cannot hold, since it would force $Q$; so $(\text{not }Q)\Longrightarrow(\text{not }P)$ is true. Conversely if $(\text{not }Q)\Longrightarrow(\text{not }P)$ is true and $P$ holds, then not $P$ fails, so not $Q$ must fail, that is $Q$ holds. Hence each is false exactly in the case $P$ true and $Q$ false.
:::

:::

::: {.pf-step #converse}
The converse of $P\Longrightarrow Q$ is $Q\Longrightarrow P$; it is false exactly when $Q$ is true and $P$ is false, and it carries no information about the truth of $P\Longrightarrow Q$.

::: pf-proof
Immediate from the truth rule stated above with the roles of $P$ and $Q$ exchanged: $Q\Longrightarrow P$ is false exactly when $Q$ is true and $P$ is false, a case in which $P\Longrightarrow Q$ is true. The two statements are therefore independent, and each has to be judged separately.
:::

:::

::: {.pf-step #a-forms}
In (a), with $P$ the statement $x<0$ and $Q$ the statement $x^{2}-x>0$ over $\RR$, the contrapositive is $x^{2}-x\leq0\Longrightarrow x\geq0$ and the converse is $x^{2}-x>0\Longrightarrow x<0$.

::: pf-proof
Over $\RR$ trichotomy gives that not $(x<0)$ is $x\geq0$ and that not $(x^{2}-x>0)$ is $x^{2}-x\leq0$; substituting in step [](#contrapositive){.pf-ref} and in the definition of the converse in step [](#converse){.pf-ref} gives the two statements.
:::

:::

::: {.pf-step #a-true}
The statement of (a) is true, hence so is its contrapositive.

::: pf-proof
Let $x<0$. Then $x<0$ and $x-1<0-1<0$, so both factors of $x^{2}-x=x(x-1)$ are negative; a product of two negative reals is positive, so $x^{2}-x>0$. This proves $P\Longrightarrow Q$, and its contrapositive is true by step [](#contrapositive){.pf-ref}.
:::

:::

::: {.pf-step #a-converse-false}
The converse in (a) is false.

::: pf-proof
Take $x=2$. Then $x^{2}-x=4-2=2>0$, while $x<0$ fails; by step [](#converse){.pf-ref} this single case refutes $x^{2}-x>0\Longrightarrow x<0$.
:::

:::

::: {.pf-step #b-forms}
In (b), with $P$ the statement $x>0$ and $Q$ the statement $x^{2}-x>0$ over $\RR$, the contrapositive is $x^{2}-x\leq0\Longrightarrow x\leq0$ and the converse is $x^{2}-x>0\Longrightarrow x>0$.

::: pf-proof
As in step [](#a-forms){.pf-ref}, using that not $(x>0)$ is $x\leq0$ and not $(x^{2}-x>0)$ is $x^{2}-x\leq0$.
:::

:::

::: {.pf-step #b-false}
The statement of (b) and its contrapositive are false.

::: pf-proof
Take $x=\tfrac12$. Then $x>0$ holds while $x^{2}-x=\tfrac14-\tfrac12=-\tfrac14\leq0$, so $P$ is true and $Q$ is false and $P\Longrightarrow Q$ is false. By step [](#contrapositive){.pf-ref} the contrapositive has the same truth value, hence is false as well; directly, $x^{2}-x=-\tfrac14\leq0$ holds while $x\leq0$ fails.
:::

:::

::: {.pf-step #b-converse-false}
The converse in (b) is false.

::: pf-proof
Take $x=-1$. Then $x^{2}-x=1+1=2>0$ while $x>0$ fails, so by step [](#converse){.pf-ref} the converse $x^{2}-x>0\Longrightarrow x>0$ is false.
:::

:::

::: {.pf-step}
In (a) the statement and its contrapositive are true and the converse is false; in (b) all three are false.

::: pf-proof
Combine steps [](#a-true){.pf-ref}, [](#a-converse-false){.pf-ref}, [](#b-false){.pf-ref} and [](#b-converse-false){.pf-ref}.
:::

:::

:::

:::
