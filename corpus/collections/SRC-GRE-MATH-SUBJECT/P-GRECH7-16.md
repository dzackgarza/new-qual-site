---
schema: qual/card@1
id: P-GRECH7-16
kind: problem
title: Probability of watching all three shows from overlap percentages
classification:
  areas: [prelim]
  topics:
  - Probability
  - Inclusion-Exclusion
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 16 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Of the 600 residents of Clermontville, 35 percent watch the television show Island Survival, 40 percent watch Lovelost Lawyers, and 50 percent watch Medical Emergency. If all residents watch at least one of these three shows, and 18 percent watch exactly 2 of these shows, then what is the probability that a resident chosen at random watches all of the shows?

(A) $\frac{1}{4}$
(B) $\frac{1}{5}$
(C) $\frac{9}{50}$
(D) $\frac{7}{100}$
(E) $\frac{7}{200}$
:::

::: {.solution}

Let $n_1,n_2,n_3$ denote the numbers of residents who watch exactly one, exactly two, and exactly three of the shows, respectively.

::: pf

::: {.pf-step #s1-1}

One has
$$
n_1+n_2+n_3=600
$$
and
$$
n_2=0.18\cdot600=108.
$$


::: pf-proof

Every resident watches at least one show, so the three disjoint classes counted by $n_1,n_2,n_3$ exhaust all $600$ residents. The second equality is the stated $18\%$ of $600$.

:::

:::

::: {.pf-step #s1-2}

Counting show memberships with multiplicity gives
$$
n_1+2n_2+3n_3=0.35(600)+0.40(600)+0.50(600)=750.
$$


::: pf-proof

The three individual show audiences have sizes
$$
210,\qquad240,\qquad300,
$$
whose sum is $750$. A resident who watches exactly one show contributes once to this sum, one who watches exactly two contributes twice, and one who watches all three contributes three times.

:::

:::

::: {.pf-step #s1-3}

The number of residents who watch all three shows is
$$
n_3=21.
$$


::: pf-proof

From step [](#s1-1){.pf-ref},
$$
n_1=600-108-n_3=492-n_3.
$$
Substituting this and $n_2=108$ into step [](#s1-2){.pf-ref} gives
$$
(492-n_3)+216+3n_3=750,
$$
so $708+2n_3=750$ and hence $n_3=21$.

:::

:::

::: {.pf-step #s1-4}

Therefore the requested probability is
$$
\boxed{\frac{21}{600}=\frac{7}{200}},
$$
so the answer is (E).


::: pf-proof

There are $21$ favorable residents by step [](#s1-3){.pf-ref}, and the resident is chosen uniformly from all $600$ residents.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested probability.

:::

:::

:::
