---
schema: qual/card@1
id: P-PRACT20-W5-12
kind: problem
title: A ring with exactly two right ideals is a division ring
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 12).
---

::: {.problem}
Let $R$ be a ring with unity. A set $I \subset R$ is said to be a right ideal of $R$ if $(I, +)$ is a subgroup of $(R, +)$ and $xr \in I$ whenever $x \in I$ and $r \in R$. Suppose $R$ has exactly two distinct right ideals. Show that every element in $R$ has a multiplicative inverse (except for the additive identity).
:::

::: {.solution}
<1>1. The two right ideals of $R$ are
\[
\{0\}
\qquad\text{and}\qquad
R.
\]

::: {.proof}
Both $\{0\}$ and $R$ are always right ideals. Since the hypothesis says
there are exactly two distinct right ideals, these must be the only ones.
:::

<1>2. If $a\in R$ is nonzero, then
\[
aR=R.
\]

::: {.proof}
The principal right ideal
\[
aR=\{ar:r\in R\}
\]
contains $a=a\cdot1$, so it is nonzero. By step <1>1, every nonzero right
ideal equals $R$.
:::

<1>3. Every nonzero $a\in R$ has a right inverse: there is $b\in R$ such that
\[
ab=1.
\]

::: {.proof}
By step <1>2, $aR=R$. In particular,
\[
1\in aR,
\]
so $1=ab$ for some $b\in R$.
:::

<1>4. The element $b$ in step <1>3 is nonzero and has a right inverse
$c\in R$:
\[
bc=1.
\]

::: {.proof}
If $b=0$, then $ab=0$, contradicting $ab=1$. Thus $b\ne0$, so step <1>3
applied to $b$ gives $c\in R$ with $bc=1$.
:::

<1>5. One has
\[
c=a.
\]

::: {.proof}
Using steps <1>3 and <1>4,
\[
a
=a\cdot1
=a(bc)
=(ab)c
=1\cdot c
=c.
\]
:::

<1>6. Hence $b$ is a two-sided inverse of $a$:
\[
\boxed{ab=ba=1}.
\]

::: {.proof}
Step <1>3 gives $ab=1$. By step <1>5,
\[
ba=bc=1.
\]
:::

<1>7. Therefore every nonzero element of $R$ is invertible.

::: {.proof}
The choice of nonzero $a$ was arbitrary, and step <1>6 constructs its
multiplicative inverse.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
