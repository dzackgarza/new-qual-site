---
schema: qual/card@1
id: P-CASP05A
kind: problem
title: "Counting roots of z^5(z-2) = w in the unit disk and in B(2,1)"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
For $w \in \mathbb{D}$, consider the equation in $z$: $$(*)\quad z^5(z - 2) = w.$$

(a) Show that (*) has 5 roots in $\mathbb{D}$ (possibly with multiplicity).
Show that for $w \in \mathbb{D} \setminus \{0\}$ the 5 roots are distinct.

(b) Show that (*) has exactly one simple root in $B(2, 1)$.
:::

::: {.solution}
Write
\[
F_w(z)=z^5(z-2)-w=z^6-2z^5-w.
\]
On $|z|=1$,
\[
|z^6-w|\le 1+|w|<2=|-2z^5|.
\]
Hence Rouché's theorem shows that $F_w$ and $-2z^5$ have the same number of
zeros in $\mathbb D$, namely five, counted with multiplicity.

If $w\ne0$ and a zero of $F_w$ were multiple, then it would also be a zero of
\[
F_w'(z)=2z^4(3z-5).
\]
Such a zero is either $0$ or $5/3$. The first cannot solve $F_w=0$ when
$w\ne0$, and the second is outside $\mathbb D$. Thus the five roots in
$\mathbb D$ are distinct.

For part (b), on $|z-2|=1$ one has $|z|\ge1$, and in fact
\[
|z^5(z-2)|=|z|^5\ge1>|w|.
\]
Rouché therefore shows that $F_w$ and $z^5(z-2)$ have the same number of zeros
in $B(2,1)$. The latter has exactly the one zero $z=2$ there, so $F_w$ has
exactly one zero in $B(2,1)$.

That zero is simple. Indeed, the only critical points of $z^5(z-2)$ are
$0$ and $5/3$, and
\[
\left|\left(\frac53\right)^5\left(\frac53-2\right)\right|
=\frac{3125}{729}>1>|w|,
\]
so neither critical point can solve $F_w=0$ for $w\in\mathbb D$.
:::
