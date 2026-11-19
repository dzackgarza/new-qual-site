---
schema: qual/card@1
id: P-AGH29PROJCLOSURE
kind: problem
title: Projective closure of an affine variety, and the twisted cubic curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Closure
  - Twisted Cubic
  - Homogeneous Ideals
relations:
- kind: uses
  target: P-AGHTWCUBIC
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Compared the card's statement in full with the printed Exercise 2.9 (scan
    page 27 of the retained PDF), tails included: hypotheses, every lettered
    part and the closing clauses. Agrees; the card states the identification
    and the comparison map in the book's sense.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.2.9,
    printed p. 12 (PDF p. 27 of the checked-in extraction). Part (b)'s second
    request, generators of I(bar Y) for the twisted cubic, now has a complete
    published proof: Georges Elencwajg's accepted answer to Mathematics Stack
    Exchange question 160924, read in
    tmp/sources/mse-160924-ideal-of-the-twisted-cubic.md (the page itself
    serves a Cloudflare challenge to automated requests, so the text was taken
    through api.stackexchange.com/2.3 with `withbody`). Checked his argument
    against the card's own: his lemma P = R(a,d) + S(a,d)b + T(a,d)c + i with
    i in I is the card's reduction "F is congruent mod Q to A + xB + yC with
    A, B, C in k[w,z]", and his vanishing of R, S, T by exponents modulo 3 is
    the card's separation of the s-exponents into the three classes 0, 2, 1
    mod 3. Not checked: his other two answers on the same question (the
    prime-ideal one, which does not prove generation, and the Maple
    computation, which is not an argument).
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Two repairs, from the local reader's report. (1) The event above called
    the prime-ideal and Maple answers "his": only 161648 and 160964 are
    Elencwajg's, and 160932 is sebigu's, as the text version's own headers
    record; corrected. (2) The Troiani quote was checked against the page
    rather than the text version, because the text version loses the display
    it quotes: tmp/sources/hartshorne-solutions-troiani.md, line 214, reads
    "It remains to find generators for IY but I think $-$ works", the formula
    having been dropped in extraction, while PDF p. 5 of
    tmp/sources/hartshorne-solutions-troiani.pdf prints
    "I think I(Y) = (wy - x^2, xz - y^2, xy - zw) works". The card's quote is
    the page's; the remark now says so. The card's proof of I(Y-bar) = Q was
    checked again and is unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Third-pass reader's report on this card, checked against the text version
    of the question. The event of 2026-11-16 above was rewritten in place by
    68e411a312, which inserted an attribution into it; a dated event is not
    edited, so its text at its date is restored here and the attribution is
    stated in this event instead. The inserted sentence also contradicted
    itself, as the reader says: it called the other two answers "neither of
    them his" and then named "Elencwajg's own answer 160964". The text
    version's own headers, tmp/sources/mse-160924-ideal-of-the-twisted-cubic.md
    lines 15, 35 and 47, give answer 161648, score 19, accepted, to Georges
    Elencwajg; answer 160964, score 9, to Georges Elencwajg; and answer 160932,
    score 2, to sebigu. So the restored phrase "his other two answers" is
    itself inaccurate as to the Maple computation, which is sebigu's: the
    correct count is two Elencwajg answers, one of them the proof, and one
    answer by sebigu. The remark, the Troiani item of the event above and the
    proof of I(Y-bar) = Q are unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The Borcherds page on this card was wrong, and the reader did not name it:
    Exercise 2.9 is on PDF p. 2 of
    tmp/sources/hartshorne-solutions-borcherds.pdf, whose page carries 2.1 to
    2.11, not on p. 3, which begins at 2.11; the remark now says p. 2. The
    event above says the remark is unchanged, which holds of the attribution it
    is about and not of this page. COMPLAINTS.md's entry on I.3.16(c),
    I.3.19(a) and I.3.20 had the same table off by one at the other end ---
    "PDF p. 5 carries 3.13--3.14" --- where 3.13 is on p. 4 with 3.1--3.13 and
    p. 5 carries 3.14; corrected there too.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The remark and the claim in the body described a Mathematics Stack Exchange
    answer as a "published proof". An answer on that site is a user post and not
    a publication, and issue #121's acceptance asks for a published source with
    its printed page, so the words were false of the source and are corrected:
    the reduction is marked as the card's own, the answer is named as a user
    post with no printed page cited for it, and the remark records that no
    publication located prints the equality $I(\bar Y)=Q$. Checked in this pass:
    the text version of the answer at answer 161648, and the exercise as printed
    at Hartshorne I.2.9, printed p. 12 (PDF p. 27 of the checked-in extraction).
    Not checked in this pass: no publication was opened or re-read, and the
    searches of the three Chapter I sets were not repeated; COMPLAINTS.md
    carries them and records this card as owing a published argument for part
    (b).

- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The remark's closing sentence was false in its first clause and is
    corrected. It read "the sets of this corpus that reach I.2.9 are Borcherds
    and Troiani and neither proves it", and four retained sets reach the
    exercise: Yang Pi-Yeh's Solution 1.2.9, which writes the projective closure
    and proves both inclusions of part (a) and then exhibits the cubic
    wz^2 - y^3 in I(Ybar) outside (yw - x^2, zw^2 - x^3); Egbert's entry headed
    "1.2.15 I.2.9", which proves part (a) and leaves part (b) as the printed
    statement; and Borcherds and Troiani, as the remark already said. None of
    the four proves the equality I(Ybar) = Q, so the remark's conclusion stands
    and only its census was wrong. Read in this pass:
    tmp/sources/lfwin-hartshorne-solutions.md at Solution 1.2.9 and
    tmp/sources/hartshorne-solutions-egbert.md at the entry for Exercise I.2.9,
    both in the text versions; and the printed exercise at Hartshorne I.2.9,
    printed p. 12 (PDF p. 27, folio read), whose part (a) asks for the identity
    I(Ybar) = (beta(I(Y))) and whose part (b) asks for generators of I(Y) and
    I(Ybar) and for the failure of the homogenized ones. The proof on the card
    was read again in this pass and is unchanged: part (a) through F = x_0^e F'
    with x_0 not dividing F', and part (b) through the normal form A + xB + yC
    modulo Q, the substitution, the three residue classes modulo 3 and the
    degree-two count that separates J from Q. Not checked in this pass: no
    search was made for a publication printing the equality, and the printed
    pages of Yang's and Egbert's sets were not read, so the remark cites neither.
---

::: {.problem}
Let $Y \subseteq \AA^n$ be an affine variety, and identify $\AA^n$ with the open set $U_0 \subseteq \PP^n$ by the homeomorphism $\phi_0$.
The closure $\bar{Y}$ of $Y$ in $\PP^n$ is called the \dfn{projective closure} of $Y$.

Write $S \coloneqq k[x_0,\ldots,x_n]$, and let
$$
\alpha: S^h \to k[y_1,\ldots,y_n], \quad f \mapsto f(1, y_1, \ldots, y_n),
\qquad
\beta: k[y_1,\ldots,y_n] \to S^h, \quad g \mapsto x_0^{\deg g} \, g\qty{\frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0}} .
$$

(a) Show that $I(\bar{Y})$ is the ideal generated by $\beta(I(Y))$.

(b) Let $Y \subseteq \AA^3$ be the twisted cubic $Y = \theset{(t,t^2,t^3) \st t \in k}$.
Its projective closure $\bar{Y} \subseteq \PP^3$ is called the \dfn{twisted cubic curve}. Find generators for $I(Y)$ and for $I(\bar{Y})$, and use this example to show that if $f_1,\ldots,f_r$ generate $I(Y)$, then $\beta(f_1),\ldots,\beta(f_r)$ need not generate $I(\bar{Y})$.
:::

::: {.solution}
**Part (a).** Embed $\AA^n$ in $\PP^n$ as $U_0 = \theset{x_0 \neq 0}$ by $(b_1,\ldots,b_n) \mapsto \thevector{1 : b_1 : \cdots : b_n}$.
Then $\bar Y \intersect U_0 = Y$, because $Y$ is closed in $U_0$.

*The inclusion $\generators{\beta(I(Y))} \subseteq I(\bar Y)$.* Let $g \in I(Y)$.
Then $\beta(g)$ is homogeneous and $\beta(g)(1, b_1, \ldots, b_n) = g(b_1,\ldots,b_n) = 0$ for every $b \in Y$.
So $Z(\beta(g))$ is a closed set containing $Y$, hence containing $\bar Y$, and $\beta(g) \in I(\bar Y)$.

*The inclusion $I(\bar Y) \subseteq \generators{\beta(I(Y))}$.* The ideal $I(\bar Y)$ is homogeneous, so it is enough to treat a nonzero homogeneous $F \in I(\bar Y)$ of degree $d$.
Put $f = \alpha(F) = F(1, y_1, \ldots, y_n)$.
It vanishes on $Y = \bar Y \intersect U_0$, so $f \in I(Y)$.
Write $F = x_0^e F'$ with $x_0 \nmid F'$.
Then $\alpha(F') = f$ and $\deg f = \deg F'$, since the terms of $F'$ of top degree in $x_1,\ldots,x_n$ survive the substitution $x_0 = 1$.
Hence $\beta(f) = x_0^{\deg F'} F'(1, x_1/x_0, \ldots, x_n/x_0) = F'$, and
$$
F = x_0^e \, \beta(f) \in \generators{\beta(I(Y))} .
$$

**Part (b).** By [[P-AGHTWCUBIC]], $I(Y) = \generators{y - x^2, z - x^3}$ in $k[x,y,z]$.
Homogenize with a new variable $w$ in $k[w,x,y,z]$:
$$
\beta(y - x^2) = wy - x^2, \qquad \beta(z - x^3) = w^2 z - x^3 .
$$
Put $J = \generators{wy - x^2,\ w^2 z - x^3}$ and $Q = \generators{wy - x^2,\ wz - xy,\ xz - y^2}$.

*Claim: $I(\bar Y) = Q$.* Each generator of $Q$ vanishes at $\thevector{1 : t : t^2 : t^3}$, so vanishes on $Y$, hence on $\bar Y$; so $Q \subseteq I(\bar Y)$.
Conversely, let $F \in I(\bar Y)$ be homogeneous of degree $d$.
Modulo $Q$ one may replace $x^2$ by $wy$, $y^2$ by $xz$ and $xy$ by $wz$; each replacement lowers the total degree in $x, y$, so $F \equiv A + xB + yC \pmod Q$ with $A, B, C \in k[w,z]$.
This reduction is the card's own, and it is the lemma of the answer quoted in the remark below, Mathematics Stack Exchange question 160924, answer 161648, where it is stated as $P=R(a,d)+S(a,d)b+T(a,d)c+i$ with $i\in Q$. That answer is a user post and not a publication, so no printed page is cited for it.
Since $F$ vanishes on $Y$, the polynomial $F(s^3, s^2 t, s t^2, t^3) = s^{3d} F(1, t/s, (t/s)^2, (t/s)^3)$ vanishes for all $s \neq 0$ and all $t$, so it is zero; the same holds for $A + xB + yC$, as the generators of $Q$ vanish under this substitution.
This gives
$$
A(s^3, t^3) + s^2 t \, B(s^3, t^3) + s t^2 \, C(s^3, t^3) = 0 .
$$
The three terms involve only monomials whose $s$-exponent is $0$, $2$ and $1$ modulo $3$, respectively, so each term is zero.
Since $s^3$ and $t^3$ are algebraically independent, $A = B = C = 0$, and $F \in Q$.

*The homogenized generators do not suffice.* The degree-two part of $J$ is spanned by $wy - x^2$, because the other generator has degree $3$.
The degree-two part of $Q = I(\bar Y)$ contains the three linearly independent quadrics $wy - x^2$, $wz - xy$, $xz - y^2$.
So $J \neq I(\bar Y)$: the generators $y - x^2$, $z - x^3$ of $I(Y)$ have homogenizations that do not generate $I(\bar Y)$.
:::

::: {.remark title="Published sources, and the located proof of part (b)"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 2.9, PDF p. 2, text version `tmp/sources/hartshorne-solutions-borcherds.md`: for (a) he takes $h$ homogeneous in $I(\bar Y)$ and writes $h=\beta g$ where $g=h(1,x_1,\ldots,x_n)$, and gets both inclusions; for (b) he homogenizes the two generators of $I(Y)$ to $x_0x_2-x_1^2$ and $x_0^2x_3-x_1^3$ and shows $I(\bar Y)$ contains $x_1x_3-x_2^2$, which is not in the ideal they generate.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 2.9, PDF p. 5, text version `tmp/sources/hartshorne-solutions-troiani.md`: for (a) the same construction, again writing $f=\beta(f(1,x_1,\ldots,x_n))$ for a homogeneous $f$; for (b) he constructs $xy-wz$ in the ideal generated by the homogenized pair, shows it is outside the pair, and writes "It remains to find generators for $I(\bar Y)$ but I think $I(\bar Y)=(wy-x^2,xz-y^2,xy-zw)$ works". That quotation is the page's: the text version loses the display in that sentence, reading "It remains to find generators for $I \bar Y$ but I think $-$ works" at its line 214, while PDF p. 5 carries the three quadrics.
The only complete argument located for the equality $I(\bar Y)=Q$, and so for part (b), is the accepted answer of Georges Elencwajg to Mathematics Stack Exchange question 160924, *Ideal of the twisted cubic*, text version `tmp/sources/mse-160924-ideal-of-the-twisted-cubic.md`, answer 161648, score 19; that answer is a user post and not a publication, so no printed page is cited for it. His argument, quoted: "Any homogeneous polynomial $P(a,b,c,d)\in k[a,b,c,d]$ can be written $P(a,b,c,d)=R(a,d)+S(a,d)b+T(a,d)c+i(a,b,c,d)$ for some polynomials $R,S,T\in k[a,d]$ and a polynomial $i\in I$"; then, for $P\in I(X)$, "$0=P(x^3,x^2y,xy^2,y^3)=R(x^3,y^3)+S(x^3,y^3)x^2y+T(x^3,y^3)xy^2+0$. By considering exponents modulo $3$ for $x$ and $y$, we see that no cancellation occurs, hence that $R=S=T=0$ and thus $P=i\in I$." His $I$ is the card's $Q$ in the variables $(a,b,c,d)=(w,x,y,z)$. The lemma's "easy proof is by induction on the degree of $P$", which he leaves to the reader and which the card's body carries out with the substitutions $x^2\mapsto wy$, $y^2\mapsto xz$, $xy\mapsto wz$; and the passage from $R(x^3,y^3)=S(x^3,y^3)=T(x^3,y^3)=0$ as polynomials in his two variables to $R=S=T=0$ uses that the monomials $s^{3i}t^{3j}$ are linearly independent, that is that $s^3$ and $t^3$ are algebraically independent, which the card states.

The proof above separates the content $x_0^e$ that both published arguments divide out without saying so, and for (b) it proves the equality $I(\bar Y)=Q$ with the three quadrics rather than exhibiting one element outside the homogenized ideal.
Agree on (a) with Borcherds and Troiani; for (b) neither of those two sets proves that the three quadrics generate, and Elencwajg's answer does. No publication located prints the equality $I(\bar Y)=Q$. Four retained sets of this corpus reach I.2.9 --- Borcherds, Troiani, Yang (Solution 1.2.9) and Egbert --- and none of them proves it: all four carry part (a); Borcherds, Troiani and Yang each exhibit one element of $I(\bar Y)$ outside the ideal generated by the homogenized pair, a quadric in the first two and the cubic $wz^2-y^3$ in Yang's; and Egbert's part (b) is the printed statement alone. The searches outside these four sets are recorded in `COMPLAINTS.md`.
:::
