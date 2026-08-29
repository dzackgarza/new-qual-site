---
schema: qual/card@1
id: P-AMD-OXM52UGE
kind: problem
title: The homophony group is trivial
classification:
  areas:
  - topology
  topics:
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Prove that the homophony group is trivial.
:::

::: {.solution}
<1>1. The homophony group $H$ is the free group on the $26$ letters of the English alphabet, modulo the relations $w = v$ for every pair of homophones $w, v$ (words that sound the same but are spelled differently).
Proof: definition of the homophony group.

<1>2. "knight" and "night" are homophones, so $k = e$.
Proof: the relation $\text{knight} = \text{night}$ cancels the common suffix, leaving $k = e$.

<1>3. "write" and "right" are homophones, so $w = e$.
Proof: cancelling the common "rite" leaves $w = e$.

<1>4. "see" and "sea" are homophones, and "sea" and "c" are homophones, so $s = e$ and $c = e$.
Proof: $\text{see} = \text{sea}$ gives $e = a$ (after cancelling $s$ and $e$), and $\text{sea} = c$ gives $s \cdot e \cdot a = c$, so $s = e$ and $c = e$.

<1>5. "you" and "u" are homophones, so $y \cdot o = e$.
Proof: $\text{you} = u$ cancels the trailing $u$, leaving $y \cdot o = e$.

<1>6. "eye" and "i" are homophones, so $y = i$.
Proof: $\text{eye} = i$ gives $e \cdot y \cdot e = i$, i.e. $y = i$.

<1>7. "why" and "y" are homophones, so $h = e$.
Proof: $\text{why} = y$ gives $w \cdot h \cdot y = y$, so $w \cdot h = e$, and $w = e$ by <1>3, hence $h = e$.

<1>8. "are" and "r" are homophones, so $a = e$.
Proof: $\text{are} = r$ gives $a \cdot r \cdot e = r$, so $a = e$.

<1>9. "queue" and "q" are homophones, so $u = e$.
Proof: $\text{queue} = q$ gives $q \cdot u \cdot e \cdot u \cdot e = q$, so $u = e$.

<1>10. "jay" and "j" are homophones, so $y = e$.
Proof: $\text{jay} = j$ gives $j \cdot a \cdot y = j$, so $a \cdot y = e$, and $a = e$ by <1>8, hence $y = e$.

<1>11. "ell" and "l" are homophones, so $l = e$; "eff" and "f" are homophones, so $f = e$.
Proof: $\text{ell} = l$ gives $e \cdot l \cdot l = l$, so $l = e$; $\text{eff} = f$ gives $e \cdot f \cdot f = f$, so $f = e$.

<1>12. The remaining letters are trivial by their letter-names: "bee" $= b$, "tea" $= t$, "gee" $= g$, "pee" $= p$, "vee" $= v$, "ex" $= x$, "zee" $= z$, "em" $= m$, "en" $= n$, "oh" $= o$, "double-u" $= w$, "aitch" $= h$.
Proof: each letter-name is a homophone of the letter itself, and the extra letters in each name are already trivial by <1>2–<1>11.

<1>13. Hence every generator of $H$ is trivial, so $H$ is the trivial group.
Proof: <1>2–<1>12 cover all $26$ letters.

<1>14. Q.E.D.
Proof: <1>13.
:::
