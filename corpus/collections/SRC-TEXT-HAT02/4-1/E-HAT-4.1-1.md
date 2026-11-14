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
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 358. The published argument is Hatcher's printed treatment of the sum in $\pi_n$, pp. 340--341: the sum uses only the first coordinate, and the homotopy $f+g\simeq g+f$ is obtained by shrinking the two domains to disjoint subcubes of $I^n$, sliding them past each other using the remaining coordinates, and enlarging them again. The card's proof is that argument written with the coordinate bookkeeping made explicit: the same sliding homotopy with the pair of coordinates $(s_1,s_2)$ gives the interchange law $(f+g)+'(h+k)=(f+'h)+(g+'k)$, and specialising it ($h$ and $g$ constant) gives $f+'k\simeq f+k$ and $g+'h\simeq h+g$. Checked against the book: the printed definition of $+$ on p. 340, the printed commutativity homotopy and its remark that only $s_1$ and $s_2$ are needed, and the converse conventions for the relative groups on p. 343. Not claimed: that the book prints this exercise; it prints the homotopy the exercise asks to verify.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The proof is now the source's: tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics,
    2008), §4.3, printed pp. 87--88 — the composition laws $+_i$ on $[\Sigma^kX,Y]_0$ with their
    formula on p. 87, the commutation rule stated on p. 88 and left there to "unravel the
    definitions", and Proposition (4.3.1) with its proof on p. 88, which is the published proof of
    both deductions of the exercise. The four-quarter verification of the commutation rule is written
    out on the card, and the card says that this is the one step the source does not print. The
    previous route to the deductions — specialising the commutation rule at $g=h=0$ and at $f=k=0$
    and using the unit laws — is replaced by (4.3.1), which additionally gives the associativity the
    exercise does not ask for and the coincidence of all $n$ laws under relabelling. The stretching
    homotopy for the neutral element is kept, and the card says why: (4.3.1) takes the neutral
    elements as given and the source records the group axioms in one sentence on p. 87. Checked
    against Hatcher (2002), §4.1 Exercise 1, printed p. 358, quoted on the card, with Hatcher's $+$
    the first-coordinate sum of p. 340 and his commutativity homotopy on p. 341 a different argument
    for the last deduction. Not claimed: that tom Dieck states Hatcher's exercise.
review: draft
---

::: {.problem}
Suppose a sum $f +' g$ of maps $f, g: (I^n, \partial I^n) \to (X, x_0)$ is defined using a coordinate of $I^n$ other than the first coordinate as in the usual sum $f + g$.
Verify the formula $(f + g) +' (h + k) = (f +' h) + (g +' k)$, and deduce that $f +' k \simeq f + k$ so the two sums agree on $\pi_n(X, x_0)$, and also that $g +' h \simeq h + g$ so the addition is abelian.
:::

::: {.solution}
Throughout $n\ge2$: for $n=1$ there is no coordinate other than the first. For $1\le i\le n$ define, on maps of pairs $(I^n,\partial I^n)\to(X,x_0)$,
$$
(f+_i g)(s)=\begin{cases}f(s_1,\dots,s_{i-1},2s_i,s_{i+1},\dots,s_n),&s_i\le\tfrac12,\\[2pt] g(s_1,\dots,s_{i-1},2s_i-1,s_{i+1},\dots,s_n),&s_i\ge\tfrac12.\end{cases}
$$
These are the group laws of tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), §4.3, printed p. 87, on $[\Sigma^kX,Y]_0$ in the cube model $\pi_n(X,x_0)=[I^n/\partial I^n,X]_0=[\Sigma^nS^0,X]_0$. The law $+_1$ is Hatcher's $+$ (printed pp. 340--341) and the exercise's $+'$ is $+_2$. A homotopy of representatives through maps of pairs induces a homotopy of $+_i$-sums, so each $+_i$ is well defined on the set $\pi_n(X,x_0)$, and the class of the constant map at $x_0$ is a two-sided unit: $f+_i0\simeq f$ by the stretching homotopy
$$
H_t(s)=f\Bigl(s_1,\dots,\frac{2s_i}{1+t},\dots,s_n\Bigr)\ \text{for } s_i\le\frac{1+t}{2},\qquad H_t(s)=x_0\ \text{otherwise},
$$
which is stationary on $\partial I^n$; the source records the group axioms in one sentence on printed p. 87 and omits this homotopy.

*The commutation rule.* Split $I^n$ into the four quarters according to $s_1\lessgtr\tfrac12$ and $s_2\lessgtr\tfrac12$. On the quarter $s_1\le\tfrac12,s_2\le\tfrac12$ the left side $(f+g)+'(h+k)$ takes the value $(f+g)(s_1,2s_2,\dots)=f(2s_1,2s_2,\dots)$, and the right side $(f+'h)+(g+'k)$ takes the value $(f+'h)(2s_1,s_2,\dots)=f(2s_1,2s_2,\dots)$. On $s_1\le\tfrac12,s_2\ge\tfrac12$ the left side is $(h+k)(s_1,2s_2-1,\dots)=h(2s_1,2s_2-1,\dots)$ and the right side is $(f+'h)(2s_1,s_2,\dots)=h(2s_1,2s_2-1,\dots)$. On $s_1\ge\tfrac12,s_2\le\tfrac12$ both sides are $g(2s_1-1,2s_2,\dots)$, and on $s_1\ge\tfrac12,s_2\ge\tfrac12$ both are $k(2s_1-1,2s_2-1,\dots)$. The two maps of $I^n$ into $X$ therefore agree everywhere, on the boundary included, so
$$
(f+g)+'(h+k)=(f+'h)+(g+'k)
$$
on the nose, not merely up to homotopy. tom Dieck states exactly this on printed p. 88, as $(a+_1b)+_2(c+_1d)=(a+_2c)+_1(b+_2d)$ for the two laws attached to two coordinates, and leaves it to "unravel the definitions", printing no proof; the four-quarter verification above is written out here, and it is the only step of the argument the source does not print.

*The source's proposition.* (tom Dieck (4.3.1), printed p. 88.) Suppose the set $M$ carries two composition laws $+_1$ and $+_2$ with neutral elements $e_i$, and suppose the commutation rule $(a+_1b)+_2(c+_1d)=(a+_2c)+_1(b+_2d)$ holds. Then $+_1=+_2=+$, $e_1=e_2=:e$, and $+$ is associative and commutative. The proof is the book's chain of equalities:
$$
a=a+_2e_2=(a+_1e_1)+_2(e_1+_1e_2)=(a+_2e_1)+_1(e_1+_2e_2)=(a+_2e_1)+_1e_1=a+_2e_1,
$$
so $e_1$ is a right unit for $+_2$; in the same way $e_1$ is a left unit for $+_2$ and $e_2$ is a left and right unit for $+_1$. Hence $e_1=e_1+_2e_2=e_2$. Then
$$
a+_2b=(a+_1e)+_2(e+_1b)=(a+_2e)+_1(e+_2b)=a+_1b
$$
shows $+_1=+_2=+$; then
$$
b+c=(e+b)+(c+e)=(e+c)+(b+e)=c+b
$$
is commutativity, and
$$
a+(b+c)=(a+e)+(b+c)=(a+b)+(e+c)=(a+b)+c
$$
is associativity.

*The exercise's two deductions.* The commutation rule holds in $M=\pi_n(X,x_0)$ with $+_1=+$ and $+_2=+'$, because it holds for representatives. So (4.3.1) applies and gives $+_1=+_2=+$, $e_1=e_2$, and commutativity. Therefore
$$
[f+'k]=[f]+_2[k]=[f]+_1[k]=[f+k],
$$
that is $f+'k\simeq f+k$ through maps of pairs, so the two sums agree on $\pi_n(X,x_0)$; and
$$
[g+'h]=[g]+_2[h]=[g]+[h]=[h]+[g]=[h]+_1[g]=[h+g],
$$
that is $g+'h\simeq h+g$, so the addition is abelian. The proposition also gives the associativity of the sum, which the exercise does not ask for. The same verification with the pair of coordinates $(i,j)$ in place of $(1,2)$ gives $+_i=+_j$ for all $i,j$, which is the book's conclusion on p. 88 that all the laws coincide and that they are abelian for $n\ge2$.

Checked against Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 1, printed p. 358: "Suppose a sum $f+'g$ of maps $f,g:(I^n,\partial I^n)\to(X,x_0)$ is defined using a coordinate of $I^n$ other than the first coordinate as in the usual sum $f+g$. Verify the formula $(f+g)+'(h+k)=(f+'h)+(g+'k)$, and deduce that $f+'k\simeq f+k$ so the two sums agree on $\pi_n(X,x_0)$, and also that $g+'h\simeq h+g$ so the addition is abelian." Hatcher's $+$ is the first-coordinate sum of printed p. 340 and his commutativity homotopy on p. 341 is a different argument for the last deduction than the route taken here.
:::

::: {.remark title="Published solution"}
tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), §4.3, printed pp. 87--88: the composition laws $+_i$ on $[\Sigma^kX,Y]_0$ and their formula on p. 87, the commutation rule on p. 88 with the words "unravel the definitions" in place of a proof, and Proposition (4.3.1) with its proof on p. 88, which is the published proof of both deductions of the exercise. The verification of the commutation rule is written out above because the source does not print it. Hatcher prints the exercise as Exercise 1 of §4.1, p. 358, and proves commutativity directly on p. 341.
:::
