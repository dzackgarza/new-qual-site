---
schema: qual/card@1
id: P-TIE-F15-13
kind: problem
title: Roots of $z^4-6z+3$ in $|z|<1$ and $1<|z|<2$
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 13.
---

::: {.problem}
Find the number of roots of $z ^ { 4 } - 6 z + 3 = 0$ in $| z | < 1$ and $1 < | z | < 2$ respectively.
:::

::: {.solution}
Let
$$
P(z)\coloneqq z^4-6z+3.
$$

<1>1. The polynomial $P$ has exactly one zero in $\abs{z}<1$, counted with multiplicity.

::: {.proof}
On $\abs{z}=1$,
$$
\abs{z^4+3}
\le
\abs{z}^4+3
=4,
$$
while
$$
\abs{-6z}=6.
$$
Hence
$$
\abs{z^4+3}<\abs{-6z}
$$
on the unit circle. By Rouché's theorem, $P(z)=-6z+(z^4+3)$ and $-6z$ have the same number of zeros in $\abs{z}<1$. The polynomial $-6z$ has exactly one zero there, namely $0$ with multiplicity one. Thus $P$ has exactly one zero in the unit disk.
:::

<1>2. The polynomial $P$ has exactly four zeros in $\abs{z}<2$, counted with multiplicity.

::: {.proof}
On $\abs{z}=2$,
$$
\abs{-6z+3}
\le
6\abs{z}+3
=15,
$$
while
$$
\abs{z^4}=16.
$$
Hence
$$
\abs{-6z+3}<\abs{z^4}
$$
on the circle $\abs{z}=2$. By Rouché's theorem, $P(z)=z^4+(-6z+3)$ and $z^4$ have the same number of zeros in $\abs{z}<2$. The polynomial $z^4$ has four zeros there counted with multiplicity, so $P$ also has four.
:::

<1>3. The number of zeros in the annulus $1<\abs{z}<2$ is
$$
\boxed{3}.
$$

::: {.proof}
Step <1>2 gives four zeros in $\abs{z}<2$, while step <1>1 gives one zero in $\abs{z}<1$. The strict Rouché inequalities also imply that $P$ has no zeros on either boundary circle. Therefore the annulus contains exactly
$$
4-1=3
$$
zeros counted with multiplicity.
:::

<1>4. Hence the requested counts are
$$
\boxed{
\#\{\abs{z}<1\}=1,
\qquad
\#\{1<\abs{z}<2\}=3.
}
$$

::: {.proof}
This is the combination of steps <1>1 and <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives both requested numbers of roots.
:::
:::
