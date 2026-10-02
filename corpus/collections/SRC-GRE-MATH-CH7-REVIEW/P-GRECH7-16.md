---
schema: qual/card@1
id: P-GRECH7-16
kind: problem
title: Probability of watching all three shows from overlap percentages
classification:
  areas: [prelim]
  topics: []
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

<1>1. One has
$$
n_1+n_2+n_3=600
$$
and
$$
n_2=0.18\cdot600=108.
$$

::: {.proof}
Every resident watches at least one show, so the three disjoint classes counted by $n_1,n_2,n_3$ exhaust all $600$ residents. The second equality is the stated $18\%$ of $600$.
:::

<1>2. Counting show memberships with multiplicity gives
$$
n_1+2n_2+3n_3=0.35(600)+0.40(600)+0.50(600)=750.
$$

::: {.proof}
The three individual show audiences have sizes
$$
210,\qquad240,\qquad300,
$$
whose sum is $750$. A resident who watches exactly one show contributes once to this sum, one who watches exactly two contributes twice, and one who watches all three contributes three times.
:::

<1>3. The number of residents who watch all three shows is
$$
n_3=21.
$$

::: {.proof}
From step <1>1,
$$
n_1=600-108-n_3=492-n_3.
$$
Substituting this and $n_2=108$ into step <1>2 gives
$$
(492-n_3)+216+3n_3=750,
$$
so $708+2n_3=750$ and hence $n_3=21$.
:::

<1>4. Therefore the requested probability is
$$
\boxed{\frac{21}{600}=\frac{7}{200}},
$$
so the answer is (E).

::: {.proof}
There are $21$ favorable residents by step <1>3, and the resident is chosen uniformly from all $600$ residents.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested probability.
:::
:::
