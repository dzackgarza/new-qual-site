---
schema: qual/card@1
id: P-TIE-F15-02
kind: problem
title: Blaschke factors are involutive automorphisms of the disk
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 2.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX and restored the label (i) that the source prints as (c) in part (b), against Fall 2015, question 2, pages 8-9 of Questions_from_Tie.pdf.
---

::: {.problem}
(a) Let $z, w$ be complex numbers, such that $\bar{z}w \ne 1$. Prove that
$$
\abs{\frac{w - z}{1 - \bar{w}z}} < 1 \quad \text{if } \abs{z} < 1 \text{ and } \abs{w} < 1,
$$
and also that
$$
\abs{\frac{w - z}{1 - \bar{w}z}} = 1 \quad \text{if } \abs{z} = 1 \text{ or } \abs{w} = 1.
$$

(b) Prove that for fixed $w$ in the unit disk $\mathbb{D}$, the mapping
$$
F \colon z \mapsto \frac{w - z}{1 - \bar{w}z}
$$
satisfies the following conditions:

(i) $F$ maps $\mathbb{D}$ to itself and is holomorphic.

(ii) $F$ interchanges $0$ and $w$, namely, $F(0) = w$ and $F(w) = 0$.

(iii) $\abs{F(z)} = 1$ if $\abs{z} = 1$.

(iv) $F \colon \mathbb{D} \to \mathbb{D}$ is bijective.

Hint: Calculate $F \circ F$.
:::

::: {.remark}
The source labels the first condition of part (b) "(c)"; it is condition (i) of the list (i)–(iv).
:::
