---
schema: qual/card@1
id: P-PRACT20-W6-24
kind: problem
title: Images and preimages of unions and intersections
classification:
  areas:
  - prelim
  topics:
  - Functions
  - Images and Preimages
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 11 of the retained solutions booklet GRE Prep:
    Miscellaneous Practice Problem Solutions by Christian Parkinson
    (assets/attachments/prelim-practice-week6-2020/page-11.png), which prints
    this problem with a worked solution. The practice sheet itself is not
    retained and the collection's provenance list is empty, so the statement was
    compared with the card from that page: the printed problem lists (A) to (D) exactly as the card does, with the same definitions of f(A) and f^{-1}(A)
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The printed solution's verdicts, that (B), (C) and (D) are true and (A) is false, are reproduced with its counterexample f(x) = x^2 on (-1,0) and (0,1) and with the two pullback computations written out.
---

::: {.problem}
Let $f : \RR \to \RR$ and let $X, Y \subseteq \RR$. Which of these are necessarily true?

(A) $f(X \cap Y) = f(X) \cap f(Y)$

(B) $f(X \cup Y) = f(X) \cup f(Y)$

(C) $f^{-1}(X \cap Y) = f^{-1}(X) \cap f^{-1}(Y)$

(D) $f^{-1}(X \cup Y) = f^{-1}(X) \cup f^{-1}(Y)$

Here for $A \subseteq \RR$, $f(A) = \{f(x) : x \in A\}$ and $f^{-1}(A) = \{x \in \RR : f(x) \in A\}$.
:::

::: {.solution}

For $f\colon\RR\to\RR$ and $X,Y\subseteq\RR$ the four assertions are (A)
$f(X\cap Y)=f(X)\cap f(Y)$, (B) $f(X\cup Y)=f(X)\cup f(Y)$, (C) $f^{-1}(X\cap
Y)=f^{-1}(X)\cap f^{-1}(Y)$, (D) $f^{-1}(X\cup Y)=f^{-1}(X)\cup f^{-1}(Y)$.

::: pf

::: {.pf-step #images}

(B) is true and (A) is false.

::: pf-proof

For (B), $y\in f(X\cup Y)$ means $y=f(x)$ with $x\in X$ or $x\in Y$, which is
exactly $y\in f(X)$ or $y\in f(Y)$; so the two sets are equal. For (A), take
$f(x)=x^2$, $X=(-1,0)$ and $Y=(0,1)$: then $X\cap Y=\emptyset$ so the left
side is empty, while $f(X)=(0,1)=f(Y)$ gives a nonempty right side. Only the
inclusion $f(X\cap Y)\subseteq f(X)\cap f(Y)$ holds in general.

:::

:::

::: {.pf-step #preimages}

(C) and (D) are true.

::: pf-proof

$x\in f^{-1}(X\cap Y)$ iff $f(x)\in X\cap Y$ iff $f(x)\in X$ and $f(x)\in Y$
iff $x\in f^{-1}(X)\cap f^{-1}(Y)$: the two conditions are unpacked and
recombined, giving (C). The same reckoning with "or" in place of "and" gives
(D). Pullbacks thus preserve both operations, which is why they behave well
for arbitrary families.

:::

:::

::: {.pf-step #answer}

(B), (C) and (D) are necessarily true and (A) is not.

::: pf-proof

Steps [](#images){.pf-ref} and [](#preimages){.pf-ref} settle all four: the
union is preserved in both directions, the intersection only under pullback,
and the counterexample $f(x)=x^2$ on $(-1,0)$ and $(0,1)$ refutes (A).

:::

:::

:::


:::
