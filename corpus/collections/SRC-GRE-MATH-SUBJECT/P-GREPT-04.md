---
schema: qual/card@1
id: P-GREPT-04
kind: problem
title: "Cardinality of $A\\cup\\mathcal P(A)$ for $A=\\{\\varnothing,a\\}$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 4 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $A = \{\varnothing, a\}$, where $\varnothing$ is the empty set. If $B$ is the set of all subsets of $A$, what's the cardinality of the set $A \cup B$?

(A) $4$
(B) $5$
(C) $6$
(D) $7$
(E) $8$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $a=\{\varnothing\}$, then
$$
\cardinality{A\cup B}=4.
$$


::: pf-proof

For this choice,
$$
A=\{\varnothing,\{\varnothing\}\}.
$$
Its power set $B=\mathcal P(A)$ has four elements. Moreover,
$\varnothing\in B$ and $a=\{\varnothing\}\in B$, so $A\subseteq B$.
Therefore $A\cup B=B$ and $\cardinality{A\cup B}=4$.

:::

:::

::: {.pf-step #s1-2}

If $a=\{\{\varnothing\}\}$, then
$$
\cardinality{A\cup B}=5.
$$


::: pf-proof

Now
$$
A=\{\varnothing,\{\{\varnothing\}\}\},
$$
so again $\cardinality{B}=\cardinality{\mathcal P(A)}=4$. The sole element of
$a=\{\{\varnothing\}\}$ is $\{\varnothing\}$, which is not an element of
$A$. Hence $a\nsubseteq A$, so $a\notin\mathcal P(A)=B$. Since
$\varnothing\in B$, adjoining the two elements of $A$ to $B$ adds exactly the
new element $a$. Thus $\cardinality{A\cup B}=5$.

:::

:::

::: {.pf-step #s1-3}

Therefore the requested cardinality is
$$
\boxed{\text{not determined by the stated hypotheses}}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives cardinality $4$, while step [](#s1-2){.pf-ref} gives cardinality $5$, and
both choices of $a$ satisfy the printed statement. Thus no single listed
choice follows from the stated hypotheses.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves that the problem is underdetermined as written.

:::

:::

:::

::: {.remark}
The source gives answer (B). That answer follows after adding the intended
hypothesis $a\notin\mathcal P(A)$: then $a\ne\varnothing$, so $\cardinality{A}=2$ and
$\cardinality{B}=4$; also $\varnothing\in B$ while $a\notin B$, hence
$\cardinality{A\cup B}=5$.
:::
