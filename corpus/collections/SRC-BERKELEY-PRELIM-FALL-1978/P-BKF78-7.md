---
schema: qual/card@1
id: P-BKF78-7
kind: problem
title: Left and right cosets and a nonnormal subgroup of the square group
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the deterministic MinerU Flash extraction. Flash renders the inequality in part 2 as “xH 6= Hx”; the card restores $xH\ne Hx$.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Set inversion sends each left coset gH to the right coset Hg^{-1}
    and is involutive, giving a bijection. For the square group
    D_4=<r,s>, the reflection subgroup H=<s> and quarter-turn x=r
    satisfy rH={r,rs} while Hr={r,sr}, with rs distinct from sr.
---

::: {.problem}
Let $H$ be a subgroup of a finite group $G$.

1. Show that $H$ has the same number of left cosets as right cosets.

2. Let $G$ be the group of symmetries of the square.
   Find a subgroup $H$ and an element $x\in G$ such that
\[
xH\ne Hx.
\]
:::

::: {.solution}
<1>1. The map
$$
gH\longmapsto Hg^{-1}
$$
is a bijection from the set of left cosets of $H$ to the set of right
cosets of $H$.

::: {.proof}
For every $g\in G$,
$$
(gH)^{-1}
=
\{(gh)^{-1}:h\in H\}
=
\{h^{-1}g^{-1}:h\in H\}
=
Hg^{-1},
$$
because inversion permutes the elements of the subgroup $H$.
Therefore the displayed assignment is simply set inversion applied to
a left coset. Since inversion of subsets is an involution, this
assignment is bijective.
:::

<1>2. The subgroup $H$ has the same number of left cosets as right
cosets.

::: {.proof}
This follows immediately from the bijection in step <1>1.
:::

<1>3. For part 2, write the symmetry group of the square as
$$
G
=
\langle r,s:r^4=s^2=1,\ srs=r^{-1}\rangle,
$$
where $r$ is rotation through $90^\circ$ and $s$ is a reflection, and
take
$$
H=\langle s\rangle=\{1,s\}.
$$

::: {.proof}
The element $s$ has order $2$, so $H=\{1,s\}$ is a subgroup of $G$.
The displayed presentation records the standard relation between a
quarter-turn and a reflection of the square.
:::

<1>4. With $x=r$,
$$
\boxed{rH\ne Hr}.
$$

::: {.proof}
We have
$$
rH=\{r,rs\},
\qquad
Hr=\{r,sr\}.
$$
From $srs=r^{-1}$ and $s^2=1$,
$$
sr=r^{-1}s=r^3s.
$$
If $rs=sr$, then multiplying on the right by $s$ would give
$$
r=r^{-1},
$$
hence $r^2=1$, contradicting that $r$ is a quarter-turn of order $4$.
Thus $rs\ne sr$, so the two displayed cosets are different.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>2 proves part 1, and steps <1>3 and <1>4 give the requested
example for part 2.
:::
:::
