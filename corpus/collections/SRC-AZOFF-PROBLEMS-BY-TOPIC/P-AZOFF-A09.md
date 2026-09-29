---
schema: qual/card@1
id: P-AZOFF-A09
kind: problem
title: Splitting an uncountable subset of $[0,1]$ into two uncountable halves
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used recursive bisection of [0,1]. If no midpoint splits E into two
    uncountable sides, one closed half retains uncountably many points while
    the discarded half contains only countably many. An infinite recursion
    leaves one point in the nested intersection, making E a singleton plus a
    countable union of countable discarded pieces, a contradiction. The
    source compilation contains no worked solution for this problem.
---

::: {.problem}
Show that if $E \subset [ 0 , 1 ]$ is uncountable, then there is some $t \in \mathbb { R }$ such that both $E \cap ( - \infty , t )$ and $E \cap ( t , \infty )$ are uncountable.
:::

::: {.solution}
Set
$$
I_0=[0,1].
$$

::: pf

::: {.pf-step #s1}

Starting from any closed interval
$$
I_n=[a_n,b_n]
$$
for which $E\cap I_n$ is uncountable, let
$$
m_n=\frac{a_n+b_n}{2}.
$$
Either both
$$
E\cap(-\infty,m_n)
\qquad\text{and}\qquad
E\cap(m_n,\infty)
$$
are uncountable, or there is a closed half $I_{n+1}$ of $I_n$ such that
$E\cap I_{n+1}$ is uncountable and
$$
E\cap(I_n\sm I_{n+1})
$$
is countable.

::: pf-proof

If both displayed sets are uncountable, the first alternative holds.

Otherwise at least one of them is countable. They cannot both be countable,
because then
$$
E
=
\bigl(E\cap(-\infty,m_n)\bigr)
\cup
\bigl(E\cap\{m_n\}\bigr)
\cup
\bigl(E\cap(m_n,\infty)\bigr)
$$
would be countable, contrary to the hypothesis.

Thus exactly one displayed side is countable. Choose $I_{n+1}$ to be the
closed half of $I_n$ lying on the other side of $m_n$. The discarded portion
of $E$ is contained in the countable side, while $E\cap I_{n+1}$ must be
uncountable because $E\cap I_n$ is uncountable and only a countable set has
been discarded.

:::

:::

::: {.pf-step #s2}

If the first alternative in step [](#s1){.pf-ref} never occurs, then there is a
unique point
$$
s\in\bigcap_{n=0}^{\infty}I_n.
$$

::: pf-proof

Under that assumption step [](#s1){.pf-ref} constructs a nested sequence
$$
I_0\supseteq I_1\supseteq I_2\supseteq\cdots
$$
of nonempty closed intervals. At each stage the length is halved, so
$$
\operatorname{length}(I_n)=2^{-n}\longrightarrow0.
$$
The nested interval theorem therefore gives exactly one point in their
intersection; call it $s$.

:::

:::

::: {.pf-step #s3}

The first alternative in step [](#s1){.pf-ref} must occur at some finite stage.

::: pf-proof

Suppose it never occurs. For each $n$, put
$$
D_n=E\cap(I_n\sm I_{n+1}).
$$
Step [](#s1){.pf-ref} says every $D_n$ is countable. By step [](#s2){.pf-ref},
$$
\bigcap_{n=0}^{\infty}I_n=\{s\}.
$$
Every point of $E$ other than possibly $s$ must leave the nested intervals at
some finite stage. Hence
$$
E
\subseteq
\{s\}
\cup
\bigcup_{n=0}^{\infty}D_n.
$$
The right-hand side is a singleton together with a countable union of
countable sets, and is therefore countable. This contradicts the assumption
that $E$ is uncountable.

:::

:::

::: {.pf-step #s4}

There is a real number $t$ such that both
$$
E\cap(-\infty,t)
\qquad\text{and}\qquad
E\cap(t,\infty)
$$
are uncountable.

::: pf-proof

By step [](#s3){.pf-ref}, the construction stops at some stage $n$ because the first
alternative in step [](#s1){.pf-ref} holds. Set
$$
t=\boxed{m_n}.
$$
That alternative says exactly that both displayed subsets of $E$ are
uncountable.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} supplies the required splitting point.

:::

:::

:::
