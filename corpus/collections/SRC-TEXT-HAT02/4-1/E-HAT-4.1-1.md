---
schema: qual/card@1
id: E-HAT-4.1-1
kind: problem
title: "Alternative sum of maps and abelian $\\pi_n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct. The interchange law is checked region by region: with `+` using the
    first coordinate and `+'` the second, the two composites `(f+g)+'(h+k)` and `(f+'h)+(g+'k)` put
    `f, g, h, k` on the same four half-size sub-cubes of `I^n` and send the same separating faces to
    `x_0`, so the maps agree on the nose, not merely up to homotopy. The two deductions are right and
    use the constant map as a two-sided identity up to homotopy relative to the boundary: with
    `g = h = 0` the interchange law gives `f +' k ~ f + k` in `pi_n`, and with `f = k = 0` it gives
    `g +' h ~ h + g`, which combined with the agreement of the two sums gives
    `[g] + [h] = [g] +' [h] = [h] + [g]`. The dimension restriction `n >= 2` is exactly what makes two
    coordinates available. No correction was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.1 Exercise 1, printed p. 358; the statement
    matches the print. The proof is now written out rather than sketched: the sum formulas in both
    coordinates are displayed, the interchange identity is checked on each of the four quarters of
    $I^n$ with the value on each quarter named, the two-sided unit laws are given by explicit
    stretching homotopies that are stationary on $\partial I^n$, and the two deductions (agreement of
    the sums, and abelianness) are read off the interchange identity with $g=h=0$, respectively
    $f=k=0$. The case $n\ge2$ is stated and the passage from the second coordinate to an arbitrary
    coordinate is justified by permuting coordinates. No published solution of this exercise is in
    the retained sets — Sam's §4.1 covers 2, 3, 5, 10-15 and 19, DeMason's covers 2, 8 and 11, and
    Li's §4.1 Exercise 4.1.1 is blank — recorded in COMPLAINTS.md.
review: draft
---

::: {.problem}
Suppose a sum $f +' g$ of maps $f, g: (I^n, \partial I^n) \to (X, x_0)$ is defined using a coordinate of $I^n$ other than the first coordinate as in the usual sum $f + g$.
Verify the formula $(f + g) +' (h + k) = (f +' h) + (g +' k)$, and deduce that $f +' k \simeq f + k$ so the two sums agree on $\pi_n(X, x_0)$, and also that $g +' h \simeq h + g$ so the addition is abelian.
:::

::: {.solution}
Here $n\ge2$, since for $n=1$ there is no coordinate other than the first. Write $s=(s_1,\dots,s_n)\in I^n$ and let $+$ use the first coordinate and $+'$ the second, as in Hatcher's formulas on pp. 340--341:
$$
(f+g)(s)=\begin{cases}f(2s_1,s_2,\dots,s_n),&s_1\le\tfrac12,\\ g(2s_1-1,s_2,\dots,s_n),&s_1\ge\tfrac12,\end{cases}
\qquad
(f+'g)(s)=\begin{cases}f(s_1,2s_2,\dots,s_n),&s_2\le\tfrac12,\\ g(s_1,2s_2-1,\dots,s_n),&s_2\ge\tfrac12.\end{cases}
$$
An argument for the second coordinate gives the statement for every other coordinate, since permuting the coordinates of $I^n$ (fixing the first) is a homeomorphism of pairs that carries one sum formula to the other.

*The interchange formula.* Split $I^n$ into the four quarters according to $s_1\lessgtr\tfrac12$ and $s_2\lessgtr\tfrac12$. On the quarter $s_1\le\tfrac12,s_2\le\tfrac12$ the left side $(f+g)+'(h+k)$ takes the value $(f+g)(s_1,2s_2,\dots)=f(2s_1,2s_2,\dots)$, while the right side $(f+'h)+(g+'k)$ takes the value $(f+'h)(2s_1,s_2,\dots)=f(2s_1,2s_2,\dots)$. On $s_1\le\tfrac12,s_2\ge\tfrac12$ the left side is $(h+k)(s_1,2s_2-1,\dots)=h(2s_1,2s_2-1,\dots)$ and the right side is $(f+'h)(2s_1,s_2,\dots)=h(2s_1,2s_2-1,\dots)$. On $s_1\ge\tfrac12,s_2\le\tfrac12$ both sides are $g(2s_1-1,2s_2,\dots)$, and on $s_1\ge\tfrac12,s_2\ge\tfrac12$ both are $k(2s_1-1,2s_2-1,\dots)$. So the two maps of $I^n$ into $X$ agree everywhere, on the boundary included:
$$
(f+g)+'(h+k)=(f+'h)+(g+'k).
$$

*The constant map is a two-sided unit for either sum.* Let $0$ denote the constant map at $x_0$. The map $f+0$ equals $f$ on $s_1\le\tfrac12$ and is constant at $x_0$ on $s_1\ge\tfrac12$; stretching the first half back to the whole cube, by
$$
H_t(s)=f(2s_1/(1+t),s_2,\dots,s_n)\quad\text{for } s_1\le (1+t)/2,\qquad H_t(s)=x_0\quad\text{otherwise},
$$
is a homotopy from $f+0$ to $f$ through maps of pairs $(I^n,\partial I^n)\to(X,x_0)$; at $s\in\partial I^n$ both maps take the value $x_0$. The same construction with the second coordinate gives $f+'0\simeq f$, and the two left unit laws $0+f\simeq f$ and $0+'f\simeq f$ are the same computation with the halves exchanged.

*The two sums agree.* Put $g=0$ and $h=0$ in the interchange formula:
$$
(f+0)+'(0+k)=(f+'0)+(0+'k).
$$
The left side is homotopic to $f+'k$, because $f+0\simeq f$ and $0+k\simeq k$ through maps of pairs and the sum of homotopic maps is homotopic; the right side is homotopic to $f+k$ for the same reason. Hence $f+'k\simeq f+k$ through maps of pairs, and the two operations agree on $\pi_n(X,x_0)$.

*Abelianness.* Put $f=0$ and $k=0$ instead:
$$
(0+g)+'(h+0)=(0+'h)+(g+'0).
$$
The left side is homotopic to $g+'h$ and the right side to $h+g$. Since the two sums agree on homotopy classes, $[g]+[h]=[g+'h]=[h+g]=[h]+[g]$ in $\pi_n(X,x_0)$, which is therefore abelian for $n\ge2$.
:::
