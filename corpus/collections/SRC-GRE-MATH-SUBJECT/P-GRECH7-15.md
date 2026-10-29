---
schema: qual/card@1
id: P-GRECH7-15
kind: problem
title: Ways to split six students into three teams for three tasks
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 15 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
A teacher is assigning 6 students to one of three tasks. She will assign students in teams of at least one student, and all students will be assigned to teams. If each task will have exactly one team assigned to it, then which of the following are possible combinations of teams to tasks?

I. $90$

II. $60$

III. $45$

(A) I only
(B) I and II only
(C) I and III only
(D) II and III only
(E) I, II, and III
:::

::: {.solution}

::: pf

::: pf-step

The only possible multisets of team sizes are
$$
\{2,2,2\},\qquad \{3,2,1\},\qquad \{4,1,1\}.
$$


::: pf-proof

The three team sizes are positive integers whose sum is $6$. Writing them in nonincreasing order, the only partitions of $6$ into exactly three positive parts are
$$
2+2+2,
\qquad
3+2+1,
\qquad
4+1+1.
$$

:::

:::

::: {.pf-step #s1-2}

If the three task-teams have sizes $2,2,2$, then there are
$$
\binom62\binom42\binom22=90
$$
assignments.


::: pf-proof

Choose the two students for the first task, then two of the remaining four for the second task; the final two students form the team for the third task. The tasks are distinct, so these choices determine an assignment uniquely.

:::

:::

::: {.pf-step #s1-3}

If the task-teams have sizes $3,2,1$ in some fixed order, then there are
$$
\binom63\binom32\binom11=60
$$
assignments.


::: pf-proof

Choose the three students for the task receiving the $3$-person team and then two of the remaining three for the task receiving the $2$-person team. The last student is forced onto the remaining task.

:::

:::

::: {.pf-step #s1-4}

If the task-teams have sizes $4,1,1$ in some fixed order, then there are
$$
\binom64\binom21\binom11=30
$$
assignments.


::: pf-proof

Choose the four students for the $4$-person team and then one of the remaining two for the first singleton task; the final student is forced onto the last task.

:::

:::

::: {.pf-step #s1-5}

Hence among the listed numbers, exactly I and II are possible.


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} show that the possible counts are $90$, $60$, and $30$. Thus I and II occur, while III, which is $45$, does not.

:::

:::

::: {.pf-step #s1-6}

Therefore the answer is
$$
\boxed{\text{I and II only}},
$$
which is choice (B).


::: pf-proof

This is the conclusion of step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the required choice.

:::

:::

:::
