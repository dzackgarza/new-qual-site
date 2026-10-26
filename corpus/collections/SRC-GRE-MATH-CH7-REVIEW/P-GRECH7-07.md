---
schema: qual/card@1
id: P-GRECH7-07
kind: problem
title: Which standard set is not countably infinite
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 7 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Which of the following sets is NOT countably infinite?

(A) $\mathbb{Q}$, the set of rational numbers
(B) $\mathbb{Z}$, the set of all integers
(C) $\mathbb{Q}^c$, the set of all irrational numbers
(D) $\mathbb{Z}^+$, the set of positive integers
(E) $E$, the set of positive even integers
:::

::: pf

::: pf-step

The sets $\ZZ^+$, $E$, $\ZZ$, and $\QQ$ are countably infinite.


::: pf-proof

The set $\ZZ^+$ is countably infinite by definition. The map
$$
n\longmapsto 2n
$$
is a bijection $\ZZ^+\to E$. The integers can be enumerated as
$$
0,1,-1,2,-2,3,-3,\ldots,
$$
so $\ZZ$ is countably infinite. Finally, every rational number has a representation $a/b$ with $a\in\ZZ$ and $b\in\ZZ^+$; hence $\QQ$ is the image of the countable set $\ZZ\times\ZZ^+$ under $(a,b)\mapsto a/b$. Thus $\QQ$ is countable, and it is infinite because it contains $\ZZ$.

:::

:::

::: pf-step

The set $\QQ^c=\RR\setminus\QQ$ of irrational numbers is uncountable.


::: pf-proof

Cantor's diagonal argument shows that $\RR$ is uncountable. If $\QQ^c$ were countable, then
$$
\RR=\QQ\cup\QQ^c
$$
would be a union of two countable sets and therefore countable, contradicting Cantor's theorem. Hence $\QQ^c$ is uncountable.

:::

:::

::: pf-step

Therefore the set that is not countably infinite is
$$
\boxed{\QQ^c},
$$
so the answer is (C).


::: pf-proof

Step <1>1 proves that choices (A), (B), (D), and (E) are countably infinite, while step <1>2 proves that choice (C) is uncountable.

:::

:::

::: pf-qed

Step <1>3 gives the required choice.

:::

:::
