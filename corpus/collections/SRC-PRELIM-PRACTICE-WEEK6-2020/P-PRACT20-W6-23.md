---
schema: qual/card@1
id: P-PRACT20-W6-23
kind: problem
title: Negating bijectivity of a function
classification:
  areas:
  - prelim
  topics:
  - Logic
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the opening quotation mark misread as a superscript 66, checked against Week6_solns.pdf (Problem 23).
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
    on the card: the statement was read and the three sentences P, Q, R transcribed: P is totality and single-valuedness, Q is surjectivity, R is failure of injectivity, so the negation is not-P or not-Q or R
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The reading of each of the three statements, the identification of bijectivity with P and Q and not R, and De Morgan's law
---

::: {.problem}
Let $f : X \to Y$. Write the negation of “$f$ is bijective” in terms of the following statements:

P: For each $x \in X$, there is $y \in Y$ such that $f(x) = y$

Q: For each $y \in Y$, there is $x \in X$ such that $f(x) = y$

R: There exist $x_1, x_2 \in X$ with $x_1 \neq x_2$ and $f(x_1) = f(x_2)$
:::

::: {.solution}

With $P$, $Q$, $R$ as stated, $f$ is bijective exactly when $P$ and $Q$ hold
and $R$ fails, so the negation is
$$
\boxed{(\text{not }P)\ \text{or}\ (\text{not }Q)\ \text{or}\ R.}
$$

::: pf

::: {.pf-step #reading}

$P$ says $f$ is defined and single-valued on all of $X$; $Q$ says $f$ is
surjective; $R$ says $f$ is not injective.

::: pf-proof

$P$ is the statement that for each $x$ there is an image $f(x)$, which is the
property that a function with domain $X$ has; $Q$ is exactly surjectivity,
that every $y\in Y$ is hit; and $R$ is the existence of two distinct points
with the same image, which is the negation of injectivity.

:::

:::

::: {.pf-step #bijective}

$f$ is bijective iff $P$ holds, $Q$ holds and $R$ does not.

::: pf-proof

A bijection is injective and surjective. Surjectivity is $Q$; injectivity is
the failure of $R$, that is: there do not exist $x_1\ne x_2$ in $X$ with equal
images. Together with $P$, which makes $f$ a function on $X$ with values in
$Y$, these are exactly the two defining properties, so bijective $=$ ($P$ and
$Q$ and not $R$).

:::

:::

::: {.pf-step #negation}

The negation is $(\text{not }P)$ or $(\text{not }Q)$ or $R$.

::: pf-proof

De Morgan's laws turn the negation of the conjunction $P\wedge Q\wedge\neg R$
into $\neg P\vee\neg Q\vee\neg(\neg R)$, and $\neg\neg R$ is $R$; so the
negation is $\neg P\vee\neg Q\vee R$. In words: $f$ fails to be defined
somewhere, or some element of $Y$ is missed, or two points share an image.
This is not the same as "not injective and not surjective", since one failure
already suffices.

:::

:::

:::


:::
