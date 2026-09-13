---
schema: qual/card@1
id: P-BKF03-7B
kind: problem
title: Berkeley Fall 2003 prelim problem 7B
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the centralizer sum by conjugacy classes and the seven partition types in S_5.
---

::: {.problem}
(a) Let G be a finite group and let X be the set of pairs of commuting elements of $G \mathrm { : }$

$$
X = \{ ( g , h ) \in G \times G : g h = h g \} .
$$

Prove that $| X | = c | G |$ where c is the number of conjugacy classes in G.

(b) Compute the number of pairs of commuting permutations on five letters.
:::
\n\n::: {.solution}\n<1>1. For each $g\in G$, the number of elements commuting with $g$ is $|C_G(g)|$.\n::: {.proof}\nBy definition,\n\[\nC_G(g)=\{h\in G:hg=gh\}.\n\]\nThus for fixed $g$, exactly $|C_G(g)|$ pairs in $X$ have first coordinate $g$. Consequently\n\[\n|X|=\sum_{g\in G}|C_G(g)|.\n\]\n:::\n\n<1>2. Each conjugacy class contributes exactly $|G|$ to this sum.\n::: {.proof}\nLet $K$ be the conjugacy class of an element $g$. Centralizer size is constant on conjugacy classes, so\n\[\n\sum_{x\in K}|C_G(x)|=|K|\,|C_G(g)|.\n\]\nBy the orbit-stabilizer theorem for the conjugation action,\n\[\n|K|=[G:C_G(g)],\n\]\nand hence\n\[\n|K|\,|C_G(g)|=|G|.\n\]\n:::\n\n<1>3. If $c$ is the number of conjugacy classes of $G$, then\n\[\n|X|=c|G|.\n\]\n::: {.proof}\nPartition the sum in <1>1 by conjugacy classes. By <1>2 each of the $c$ classes contributes $|G|$, giving the formula.\n:::\n\n<1>4. For $G=S_5$, there are $840$ commuting ordered pairs.\n::: {.proof}\nConjugacy classes in $S_5$ are determined by cycle type, hence by partitions of $5$. The seven partitions are\n\[\n5,\ 4+1,\ 3+2,\ 3+1+1,\ 2+2+1,\ 2+1+1+1,\ 1+1+1+1+1.\n\]\nThus $c=7$. Since $|S_5|=5!=120$, <1>3 gives\n\[\n|X|=7\cdot120=\boxed{840}.\n\]\n:::\n:::\n