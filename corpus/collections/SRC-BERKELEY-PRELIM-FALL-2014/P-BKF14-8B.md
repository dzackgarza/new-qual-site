---
schema: qual/card@1
id: P-BKF14-8B
kind: problem
title: Finite groups with exactly three conjugacy classes
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet: conjugacy
    class-size divisibility reduces the possibilities to orders 3, 4, and 6,
    and the order-4 case is impossible.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the odd- and even-order bounds, the divisibility argument
    forcing a nontrivial class size to divide 2, and the uniqueness of the
    nonabelian group of order 6.
---

::: {.problem}
Determine, up to isomorphism, all finite groups G such that G has exactly three conjugacy classes.
:::

::: {.solution}
Let
$$
|G|=g,
$$
and let the three conjugacy classes have sizes
$$
1,\qquad r,\qquad s.
$$
Thus
$$
g=1+r+s.
$$

<1>1. Both $r$ and $s$ are proper divisors of $g$.

::: {.proof}
For any $x\in G$, the size of its conjugacy class is
$$
|G:C_G(x)|,
$$
so it divides $g$. A conjugacy class of a nonidentity element cannot
have size $g$, since its centralizer contains at least the identity and
the element itself. Hence $r,s<g$.
:::

<1>2. If $g$ is odd, then
$$
g=3.
$$

::: {.proof}
When $g$ is odd, every proper divisor of $g$ is at most $g/3$.
Therefore step <1>1 gives
$$
r,s\le\frac g3.
$$
Using $g=1+r+s$,
$$
g
\le
1+\frac{2g}{3},
$$
so $g\le3$. A group with three nonempty conjugacy classes has at least
three elements, hence $g=3$.
:::

<1>3. The unique odd-order possibility is
$$
C_3.
$$

::: {.proof}
Every group of prime order $3$ is cyclic. The group $C_3$ is abelian,
so each element is its own conjugacy class and it has exactly three
conjugacy classes.
:::

<1>4. Suppose $g$ is even. Then one of $r,s$ equals $g/2$.

::: {.proof}
By step <1>1, $r$ and $s$ are proper divisors of the even integer $g$,
so
$$
r,s\le\frac g2.
$$
If both were strictly less than $g/2$, then, since they are integers,
$$
r,s\le\frac g2-1.
$$
Consequently
$$
g=1+r+s\le g-1,
$$
a contradiction. Thus one class has size $g/2$.
:::

<1>5. In the even-order case,
$$
g\in\{4,6\}.
$$

::: {.proof}
Relabel if necessary so that
$$
s=\frac g2.
$$
Then
$$
g=1+r+\frac g2,
$$
hence
$$
g=2r+2.
$$
Since $r$ is a conjugacy-class size, step <1>1 gives $r\mid g$. Thus
$$
r\mid(g-2r)=2,
$$
so $r=1$ or $r=2$. These give $g=4$ and $g=6$, respectively.
:::

<1>6. The case $g=4$ is impossible.

::: {.proof}
Every group of order $p^2$ is abelian; in particular every group of
order $4$ is abelian. An abelian group of order $4$ has four singleton
conjugacy classes, not three.
:::

<1>7. If $g=6$, then
$$
G\cong S_3.
$$

::: {.proof}
A group of order $6$ with only three conjugacy classes cannot be
abelian, since an abelian group has one conjugacy class per element.

Let $N$ be a Sylow $3$-subgroup. The number of Sylow $3$-subgroups
divides $2$ and is congruent to $1$ modulo $3$, so $N$ is unique and
hence normal. Write
$$
N=\langle a\rangle\cong C_3.
$$
Let $b$ generate a Sylow $2$-subgroup. Conjugation by $b$ induces an
automorphism of $N$. Since $N\cap\langle b\rangle=\{1\}$, the product
$N\langle b\rangle$ has $6$ elements, so $a$ and $b$ generate $G$.
If conjugation by $b$ fixed $a$, then $a$ and $b$ would commute and
$G$ would be abelian. Hence
$$
bab^{-1}=a^{-1}.
$$
Thus
$$
G
\cong
\langle a,b\mid a^3=b^2=1,\ bab^{-1}=a^{-1}\rangle
\cong
S_3.
$$
:::

<1>8. The group $S_3$ has exactly three conjugacy classes.

::: {.proof}
Its conjugacy classes are
$$
\{1\},
\qquad
\{\text{three transpositions}\},
\qquad
\{\text{two }3\text{-cycles}\}.
$$
Thus their sizes are $1,3,2$.
:::

<1>9. Therefore the complete list is
$$
\boxed{C_3\ \text{and}\ S_3}.
$$

::: {.proof}
Steps <1>2--<1>6 exhaust all possible group orders, while steps <1>3,
<1>7, and <1>8 identify and verify the two surviving groups.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required classification.
:::
:::
