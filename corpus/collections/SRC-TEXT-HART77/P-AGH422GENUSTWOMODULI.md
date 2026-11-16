---
schema: qual/card@1
id: P-AGH422GENUSTWOMODULI
kind: problem
title: Curves of genus $2$ correspond to six branch points on $\PP^1$ modulo $\Sigma_6$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Riemann-Hurwitz
  - Hyperelliptic Curves
  - Canonical Divisor
relations: []
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), IV.2.2, printed
    p. 304 (PDF p. 319 of the checked-in extraction). Published treatment located
    outside the twelve retained sets, with the page ranges corrected after
    re-reading the text: R. Vakil, The Rising Sea: Foundations of Algebraic
    Geometry, 21 October 2025 version, Sections 19.5--19.6, printed pp. 546--551,
    read in tmp/sources/vakil-rising-sea-2025-10-21.md. Theorem 19.5.1, printed
    p. 546, is the hyperelliptic Riemann--Hurwitz formula; Proposition 19.5.2 with
    its proof runs over printed pp. 546--547 and constructs the double cover
    branched at a prescribed even set of points as the normalization of
    y^2 = f(x), f the product of the linear factors; 19.5.4, printed pp. 547--548,
    computes its genus as r/2 - 1, which for r = 6 is 2; Proposition 19.5.6,
    printed p. 548, identifies the hyperelliptic cover with the canonical one for
    g >= 2, and Proposition 19.5.7, whose proof is on printed p. 549, proves that a
    curve of genus at least 2 admits at most one double cover of P^1; 19.6.2,
    printed p. 550, assembles the bijection between genus 2 curves and double
    covers branched at six points. What Vakil does not supply is part (c): the
    three-transitivity of Aut P^1 is Exercise 15.5.B there, an exercise and not a
    proof, so step s6 keeps the card's own argument. Parts (d) and (e), the
    explicit Sigma_6 action on triples and the resulting correspondence, are not
    in Vakil either: he states the bijection between curves and six-point sets
    modulo PGL_2 and stops short of the action
    argument.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Wording corrected in the body and the published-solution remark: (a) and (b)
    were described as "following" Vakil with the steps giving "those arguments in
    Hartshorne's terms", which reads as a transcription. Steps s1, s2 and s4 are
    the card's own -- Riemann--Hurwitz for the six branch points and for g(X)=2,
    Riemann--Roch for the uniqueness of the degree-two map -- and Vakil's 19.5.4
    computes the same genus by a Cech computation on the two affine charts of the
    cover, which the body now says. His propositions are cited for the statements
    the two proofs share, and nothing in steps s1--s5 reproduces his text.
    Unchanged: parts (c), (d) and (e) have no published proof in Vakil, (c) being
    his Exercise 15.5.B.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Attributed counts corrected on a reader's report of issue #121, and the page
    ranges re-read in the whole-book extraction tmp/sources/vakil-rising-sea-2025-10-21.md
    with the pages checked in tmp/sources/vakil-rising-sea-2025-10-21.pdf, whose
    printed folios are its PDF pages. 19.5.1 is the theorem that a double cover
    has 2g+2 branch points, printed p. 546; it is proved by 19.5.2 (printed
    pp. 546--547) and 19.5.4 (printed pp. 547--548, ending "g = r/2 - 1, from
    which Theorem 19.5.1 follows"), not read off from omega. It is 19.6.2,
    printed p. 550, where omega_C of degree 2 with two sections gives the double
    cover, and there the count 2g+2 = 6 is quoted from 19.5.1. The earlier events
    gave 19.5.2 as pp. 546--548 and said the count was "restated as 19.6.2 ... who
    reads it off from omega_X"; both are corrected in the body, which now says
    which proposition is which.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Attribution and page correction, on a reader's report of issue #121: the
    published-solution remark still carried the form the events above correct.
    It gave Proposition 19.5.2 as printed pp. 546--548, and it called the count
    g = r/2 - 1 "his 19.5.4 statement". Read on the printed folios of
    tmp/sources/vakil-rising-sea-2025-10-21.pdf, which are its PDF pages:
    Theorem 19.5.1 is stated on printed p. 546, Proposition 19.5.2 runs over
    printed pp. 546--547, and 19.5.4, printed pp. 547--548, is the paragraph in
    which that theorem is proved and the genus computed. The remark now gives
    19.5.2 as pp. 546--547, names the count as Theorem 19.5.1, and says that
    19.5.4 is where it is proved.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Named the text version of Vakil's book at the five citations of 19.5 and
    19.6 in the remark on 2026-11-16, where they cited the PDF alone: it is
    tmp/sources/vakil-rising-sea-2025-10-21.md. No page or claim changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Printed exercise read again for this pass: Hartshorne, Algebraic Geometry
    (1977), IV.2.2, printed p. 304 (PDF p. 319 of the checked-in extraction
    tmp/sources/hartshorne-1977-algebraic-geometry.md), five parts (a)--(e),
    the card's statement keeping the book's wording. The three published
    solutions named in the brief were read at the cited places in their text
    versions: B. Reiser, Hartshorne Solutions (15 February 2022), Exercise
    IV.2.2, printed pp. 352--354, which is PDF pp. 353--355 of
    tmp/sources/reiser-hartshorne-solutions-pp351-358.md, the printed folio
    being one less than the PDF page; Chin-Lung Wang's Algebraic Geometry II
    (NTU, 2020 Spring), Chapter IV homework, section 2 Exercise 2 by Yu-Chi
    Hou, printed pp. 4--6 of tmp/sources/ntu-ag2-chapter4.md; and D.
    Gruenewald, Computing Humbert Surfaces, section 2, printed p. 2 of
    tmp/sources/gruenewald-2007-computing-humbert-surfaces.md. Part (a) is on
    Reiser p. 352 and Hou p. 4, (b) on Reiser p. 353 and Hou pp. 4--5, (c) on
    Reiser p. 353 and Hou p. 6, (d) on Reiser p. 354 and Hou p. 6, (e) on
    Reiser p. 354, the single word "Yup!", and on Hou p. 6. Page positions
    were fixed on the PDFs, by reading the printed folio of each page.

    Two defects of the sources were found while checking them, and are
    recorded in COMPLAINTS.md under this date: Hou's parts (d) and (e) name the
    group of the action S_3 while defining the permutation of the six-tuple
    followed by renormalization, which is the Sigma_6 action of the exercise,
    and Hou's part (b) prints h^0(X, O_X(K_X - 2P)) = 2 where its own
    Riemann-Roch line gives 1. What this pass did not do: it did not re-read
    Vakil sections 19.5--19.6 or Egbert, whose citations are those of the
    2026-11-15 events and stand unchanged.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the transcription of those sources, one step per
    published argument, each step naming source, numbered part and printed
    page: s1 (Reiser IV.2.2(a) printed p. 352; Hou 2(a) p. 4), s2 (Reiser
    IV.2.2(b) p. 353 with II Ex 7.2, and Reiser's p. 352 sentence), s3
    (Reiser p. 353; Hou pp. 4--5), s4 (Reiser p. 353; Hou p. 5), s5 (Hou
    p. 5), s6 (Reiser IV.2.2(c) p. 353; Hou 2(c) p. 6), s7 (Hou 2(e) p. 6),
    s8 (Reiser IV.2.2(d) p. 354, whose device is the cross-ratio), s10 and
    s11 (Hou 2(e) p. 6; Gruenewald section 2 p. 2). Step s9 is the card's own
    and is labelled as such, because Reiser's (e) is the word "Yup!", Hou's
    (e) proves well-definedness and existence but not that a separable
    degree-two cover of P^1 is determined by its branch divisor, and
    Gruenewald states the quotient without proof; its statement is Vakil
    Proposition 19.5.2, printed pp. 546--547, as the remark says. The earlier
    steps s1--s5 proved (a) and (b) by Riemann-Hurwitz and Riemann-Roch for
    Vakil's statements; the same two tools now appear where Reiser and Hou use
    them, and the Vakil page references that were in the steps moved to the
    remark. Checked against the book after the transcription: (a)'s "ramified
    at exactly 6 points, with ramification index 2 at each one" and its
    uniqueness clause, (b)'s three assertions, (c)'s uniqueness of the
    normalization, and (d)'s Sigma_6 action as printed. Not checked: the
    sources' own citations of the book (IV.1.7, II.7.2, I.6.6, IV.1.2) beyond
    the statements they quote from it.

review: draft
---

::: {.problem}
Fix an algebraically closed field $k$ of characteristic $\neq 2$.

(a) If $X$ is a curve of genus 2 over $k$, the canonical linear system $\abs{K}$ determines a finite morphism $f: X \to \PP^1$ of degree 2 (Ex.
1.7). Show that it is ramified at exactly 6 points, with ramification index 2 at each one.
Note that $f$ is uniquely determined, up to an automorphism of $\PP^1$, so $X$ determines an (unordered) set of 6 points of $\PP^1$, up to an automorphism of $\PP^1$.

(b) Conversely, given six distinct elements $\alpha_1, \ldots, \alpha_6 \in k$, let $K$ be the extension of $k(x)$ determined by the equation $z^2=(x-\alpha_1) \cdots (x-\alpha_6)$.
Let $f: X \to \PP^1$ be the corresponding morphism of curves.
Show that $g(X)=2$, the map is the same as the one determined by the canonical linear system, and $f$ is ramified over the six points $x=\alpha_i$ of $\PP^1$, and nowhere else.
(Cf.
(II, Ex.
6.4).)

(c) Using (I, Ex.
6.6), show that if $P_1, P_2, P_3$ are three distinct points of $\PP^1$, then there exists a unique $\varphi \in \Aut \PP^1$ such that $\varphi(P_1)=0, \varphi(P_2)=1, \varphi(P_3)=\infty$.
Thus in (a), if we order the six points of $\PP^1$, and then normalize by sending the first three to $0,1,\infty$ respectively, we may assume that $X$ is ramified over $0,1,\infty, \beta_1, \beta_2, \beta_3$, where $\beta_1, \beta_2, \beta_3$ are three distinct elements of $k$, $\neq 0,1$.

(d) Let $\Sigma_6$ be the symmetric group on 6 letters.
Define an action of $\Sigma_6$ on sets of three distinct elements $\beta_1, \beta_2, \beta_3$ of $k$, $\neq 0,1$, as follows: reorder the set $0,1,\infty, \beta_1, \beta_2, \beta_3$ according to a given element $\sigma \in \Sigma_6$, then renormalize as in (c) so that the first three become $0,1,\infty$ again.
Then the last three are the new $\beta_1', \beta_2', \beta_3'$.

(e) Summing up, conclude that there is a one-to-one correspondence between the set of isomorphism classes of curves of genus 2 over $k$, and triples of distinct elements $\beta_1, \beta_2, \beta_3$ of $k$, $\neq 0,1$, modulo the action of $\Sigma_6$ described in (d). In particular, there are many non-isomorphic curves of genus 2. We say that curves of genus 2 depend on three parameters, since they correspond to the points of an open subset of $\AA_k^3$ modulo a finite group.
:::

::: {.solution}
Every step below is the published argument and names the source it transcribes: B. Reiser, *Hartshorne Solutions* (15 February 2022), Exercise IV.2.2, printed pp. 352--354, text version `tmp/sources/reiser-hartshorne-solutions-pp351-358.md`, whose printed folio is one less than its PDF page; Chin-Lung Wang's Algebraic Geometry II (National Taiwan University, 2020 Spring), Chapter IV homework, §2 Exercise 2 by Yu-Chi Hou, printed pp. 4--6, text version `tmp/sources/ntu-ag2-chapter4.md`; and D. Gruenewald, *Computing Humbert Surfaces*, §2, printed p. 2, text version `tmp/sources/gruenewald-2007-computing-humbert-surfaces.md`. Parts (a)--(d) are Reiser's and Hou's; the correspondence of part (e) is Hou's, except for the one step marked as the card's own, which neither source proves.

::: pf

::: {.pf-step #canonical-degree-two}

The canonical linear system of a curve $X$ of genus $2$ determines a finite
morphism
$$
f:X\longrightarrow\PP^1
$$
of degree $2$, ramified at exactly six points, with ramification index $2$ at
each.

::: pf-proof

Reiser, Exercise IV.2.2(a), printed p. 352: the existence and the degree are
[[P-AGH417HYPERELLIPTIC|Exercise IV.1.7]], and because
$\characteristic k\ne2$ the morphism is separable, so Hurwitz's formula applies
in the form
$$
2\cdot2-2=2\,(0-2)+\deg R,
$$
that is, $\deg R=6$. A finite flat morphism of degree $2$ over an algebraically
closed field has two points counted with multiplicity in every fibre, so
$e_P=2$ exactly at the ramification points and $e_P=1$ elsewhere; since
$\deg R=\sum_P(e_P-1)$, there are exactly six of them, each of index $2$.

Hou, §2 Exercise 2(a), printed p. 4, computes $\deg R=6$ in the same line from
Riemann--Hurwitz, records that $\characteristic k\ne2$ makes every ramification
point tame so that $R=\sum_P(e_P-1)$ with $\deg R=6$, and concludes that $f$ is
ramified at exactly six points.

:::

:::

::: {.pf-step #degree-two-is-canonical}

Every finite morphism
$$
h:X\longrightarrow\PP^1
$$
of degree $2$ from a curve $X$ of genus $2$ is the canonical morphism, up to an
automorphism of $\PP^1$.

::: pf-proof

Reiser, Exercise IV.2.2(b), printed p. 353: it is enough to show that
$h^*\mco_{\PP^1}(1)\cong\omega_X$. Write $h^*\mco_{\PP^1}(1)=\mcl(D)$. Then
$$
\deg D=2,
\qquad
\ell(D)=h^0\bigl(\mcl(D)\bigr)=2,
$$
the second because $h^*\mco_{\PP^1}(1)$ has the two-dimensional space of global
sections of $\mco_{\PP^1}(1)$. Riemann--Roch on a curve of genus $2$ gives
$$
\ell(D)-\ell(K-D)=\deg D+1-g=2+1-2=1,
$$
hence $\ell(K-D)=1$, and
$$
\deg(K-D)=0.
$$
A nonzero section of $K-D$ has an effective zero divisor of degree $0$, so
$K-D\sim0$ by Lemma IV.1.2. Therefore
$$
K\sim D,
$$
and the pencil defining $h$ is the complete canonical pencil. Two sets of
sections spanning the same subspace of the two-dimensional $H^0(X,K)$ give
morphisms that differ by an automorphism of $\PP^1$ (II, Ex. 7.2), which is the
sentence "we may see that $f$ is uniquely determined by exercise II.7.2" at
Reiser, printed p. 352.

:::

:::

::: {.pf-step #kummer-cover-ramification}

Let $K=k(x)(z)$ with
$$
z^2=\prod_{i=1}^{6}(x-\alpha_i),
$$
$\alpha_1,\ldots,\alpha_6$ distinct, and let
$$
f:X\longrightarrow\PP^1
$$
be the corresponding morphism of curves. Then $f$ has degree $2$ and is
ramified over exactly the six points $x=\alpha_i$, and nowhere else.

::: pf-proof

Reiser, Exercise IV.2.2(b), printed p. 353. The field extension $K/k(x)$ has
degree $2$, so $f$ has degree $2$. At a finite closed point $x_0\in\AA^1$ the
fibre of
$$
\Spec k[x,z]\big/\bigl(z^2-\textstyle\prod_i(x-\alpha_i)\bigr)
\longrightarrow
\Spec k[x]
$$
is
$$
\Spec k[z]\Big/\Bigl(z^2-\textstyle\prod_i(x_0-\alpha_i)\Bigr),
$$
which is two distinct reduced points when $x_0\ne\alpha_i$, since
$\characteristic k\ne2$, and one point when $x_0=\alpha_i$. So $f$ is ramified
with $e_P=2$ over the six $\alpha_i$ and at no other finite point.

For the point at infinity Reiser argues by parity of $\deg R$: the number
$$
\deg R=2g(X)-2+2\deg f
$$
is even whatever $g(X)$ is, the six finite points already account for
$6$, so $e_\infty-1$ is even, while $e_\infty\le2$ because the degree is
$2$; hence $e_\infty=1$ and $f$ is unramified at infinity.

Hou, §2 Exercise 2(b), printed pp. 4--5, checks the same point in the explicit
chart: with $y=1/x$ and $\tilde z=x^{-3}z$ the equation reads
$\tilde z^2=\prod_i(1-\alpha_i y)$, whose value at $y=0$ is $1$, so infinity is
not a branch point; the printed account writes the transformed equation as
$\tilde z^2=\alpha_1\cdots\alpha_6\tilde h(y)$ with
$\tilde h(y)=\prod_i(1/\alpha_i-y)$ and separates out the case in which one of
the $\alpha_i$ is $0$, at printed p. 6 of the extraction, before drawing the
same conclusion.

:::

:::

::: {.pf-step #genus-two}

The curve $X$ of step [](#kummer-cover-ramification){.pf-ref} has genus $2$.

::: pf-proof

Reiser, printed p. 353: "by an application of Hurwitz's formula, we have
$g(X)=2$", that is,
$$
2g(X)-2=2\,(0-2)+6=2,
$$
so
$$
\boxed{g(X)=2}.
$$
Hou, §2 Exercise 2(b), printed p. 5, computes the same
$2g(X)-2=2(0-2)+6=2$ and the same conclusion.

:::

:::

::: {.pf-step #same-as-canonical}

The morphism $f$ of step [](#kummer-cover-ramification){.pf-ref} is the
morphism determined by the canonical linear system, up to an automorphism of
$\PP^1$.

::: pf-proof

It has degree $2$ by construction and its source has genus $2$ by step
[](#genus-two){.pf-ref}, so step [](#degree-two-is-canonical){.pf-ref} applies.

Hou, §2 Exercise 2(b), printed p. 5, reaches the same sentence directly: at a
branch point $P$ with $f(P)=Q$ one has $f^*P=2P$, hence
$f^*\mco_{\PP^1}(Q)=f^*\mco_{\PP^1}(1)=\mco_X(2P)$; Riemann--Roch gives
$$
h^0\bigl(\mco_X(2P)\bigr)-h^0\bigl(\mco_X(K_X-2P)\bigr)=\deg(2P)-g(X)+1=1
$$
with $h^0(\mco_X(2P))=h^0(\PP^1,\mco_{\PP^1}(1))=2$, so
$h^0(\mco_X(K_X-2P))=1$, and $\deg(K_X-2P)=0$ forces $K_X\sim2P$; therefore
$f^*\mco_{\PP^1}(1)=K_X$. The printed line "h^0(X,\mco_X(K_X-2P))=2" in that
computation is a slip for $1$.

:::

:::

::: {.pf-step #normalize-three-points}

For three distinct points $P_1,P_2,P_3$ of $\PP^1$ there is a unique
$$
\varphi\in\Aut\PP^1=\PGL_2(k)
$$
with
$$
\varphi(P_1)=0,
\qquad
\varphi(P_2)=1,
\qquad
\varphi(P_3)=\infty.
$$

::: pf-proof

Reiser, Exercise IV.2.2(c), printed p. 353: write $P_i=[p_i:q_i]$ and let
$\varphi$ be given by $[x:y]\mapsto[ax+by:cx+dy]$. The condition
$\varphi(P_1)=0$ forces $[a:b]=[q_1:-p_1]$, and the condition
$\varphi(P_3)=\infty$ forces $[c:d]=[q_3:-p_3]$, so $\varphi$ has the matrix
$$
\begin{pmatrix}q_1&-p_1\\ kq_3&-kp_3\end{pmatrix}
$$
for some $k$. The condition $\varphi(P_2)=1$ reads
$$
q_1p_2-p_1q_2=k\,(q_3p_2-p_3q_2),
$$
whose two sides are nonzero because $P_2$ differs from $P_1$ and from $P_3$;
this fixes $k$ and with it the matrix, whose determinant
$k(p_1q_3-q_1p_3)$ is nonzero because $P_1\ne P_3$. So $\varphi$ exists and is
unique, and it lies in $\PGL_2(k)=\Aut\PP^1$ by (I, Ex. 6.6).

Hou, §2 Exercise 2(c), printed p. 6, writes the transformation down:
$$
\varphi(z)=\frac{z-a}{z-c}\cdot\frac{b-c}{b-a}
$$
for $P_1=[a:1]$, $P_2=[b:1]$, $P_3=[c:1]$, and $\varphi(z)=\frac{b-c}{z-c}$ when
$P_1=\infty$; uniqueness is read off from $\Aut(\PP^1)=\PGL(2)$ there.

:::

:::

::: {.pf-step #normal-form}

After ordering the six branch points of a curve of genus $2$ and applying the
automorphism of step [](#normalize-three-points){.pf-ref} to the first three,
the branch set has the form
$$
0,\ 1,\ \infty,\ \beta_1,\ \beta_2,\ \beta_3,
$$
where the $\beta_i$ are distinct and different from $0$ and $1$.

::: pf-proof

The six branch points are distinct by step
[](#canonical-degree-two){.pf-ref}, and an automorphism of $\PP^1$ is a
bijection, so the last three images are distinct from each other and from
$0$, $1$, $\infty$. Being different from $\infty$ they are elements of $k$, and
they are $\ne0,1$. This is the normal form used at Hou, §2 Exercise 2(e), printed
p. 6: "we send $P_1\mapsto0$, $P_2\mapsto1$, $P_3\mapsto\infty$,
$P_i\mapsto\beta_{i-3}$".

:::

:::

::: {.pf-step #sigma-six-action}

The rule of part (d) --- reorder $(0,1,\infty,\beta_1,\beta_2,\beta_3)$ by
$\sigma\in\Sigma_6$, then renormalize so that the first three entries are
$0,1,\infty$ again --- defines an action of $\Sigma_6$ on
$$
U=\bigl\{(\beta_1,\beta_2,\beta_3)\in\AA^3_k:\ \beta_i\ne0,1,\ \
\beta_i\ne\beta_j\ (i\ne j)\bigr\}.
$$

::: pf-proof

Reiser, Exercise IV.2.2(d), printed p. 354. All six entries are distinct, so any
three of them may be sent to $0,1,\infty$ by step
[](#normalize-three-points){.pf-ref}, uniquely, and the remaining three are
again distinct and different from $0,1,\infty$: the rule is a well-defined map
$U\to U$.

For the group law Reiser uses the cross-ratio
$$
(z_1,z_2,z_3,z_4)=\frac{(z_1-z_2)(z_3-z_4)}{(z_1-z_4)(z_3-z_2)},
$$
the image of $z_1$ under the fractional linear transformation sending
$z_2\mapsto0$, $z_3\mapsto1$, $z_4\mapsto\infty$; for $z_1\notin\{z_2,z_3,z_4\}$
it recovers $z_1$. For $T(z)=\frac{az+b}{cz+d}$ one has
$$
T(x)-T(y)=\frac{(ad-bc)(x-y)}{(cx+d)(cy+d)},
$$
so
$$
(Tz_1,Tz_2,Tz_3,Tz_4)=(z_1,z_2,z_3,z_4):
$$
the cross-ratio is invariant under $\PGL_2(k)$. Hence for any ordered quadruple
of elements of $(0,1,\infty,\beta_1,\beta_2,\beta_3)$ the cross-ratio is the
same whether the quadruple is read off after reordering by $g$ and $h$ in turn,
or after reordering once by $hg$: the second reading transforms an already
normalized tuple by an element of $\PGL_2(k)$, which the cross-ratio does not
see. Since a point is recovered from its cross-ratio with $0,1,\infty$, the
normalized last three entries agree in the two readings, which is the group
law.

:::

:::

::: {.pf-step #cover-determined-by-branch}

A separable degree-two cover of $\PP^1$ over $k$ is determined, up to
isomorphism over $\PP^1$, by its branch divisor.

::: pf-proof

This step is the card's own. None of the three sources above proves it: Reiser's
part (e), printed p. 354, is the single word "Yup!", Hou's part (e), printed
p. 6, proves well-definedness and existence but not this uniqueness, and
Gruenewald, printed p. 2, states the resulting quotient without proof. The
argument below is the one this card has carried since its first version, and
the statement is
R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025
version [@Vak25, Proposition 19.5.2], text version
`tmp/sources/vakil-rising-sea-2025-10-21.md`, printed pp. 546--547, where the
double cover branched at a prescribed set of points is constructed as the
normalization of $y^2=f(x)$ and is unique.

Let $F=k(\PP^1)=k(x)$ and let $L_1/F$ and $L_2/F$ be the function-field
extensions of two such covers with the same branch locus. Since
$\characteristic k\ne2$, each quadratic extension has Kummer form
$$
L_i=F(\sqrt{d_i})
$$
for some $d_i\in F^\times$, determined modulo $F^{\times2}$.

For a place $P$ of $F$, the extension $F(\sqrt{d_i})/F$ is ramified at $P$
exactly when $v_P(d_i)$ is odd. Equality of the branch loci therefore implies
that
$$
v_P(d_1/d_2)
$$
is even for every $P\in\PP^1$. Hence
$$
\div(d_1/d_2)=2D
$$
for an integral divisor $D$ of degree $0$ on $\PP^1$. Every degree-zero divisor
on $\PP^1$ is principal, so $D=\div(g)$ for some $g\in F^\times$, and
$$
\div\!\left(\frac{d_1}{d_2g^2}\right)=0,
$$
so $\frac{d_1}{d_2g^2}=c$ for some $c\in k^\times$. Because $k$ is
algebraically closed, $c=a^2$ for some $a\in k^\times$, so
$d_1=d_2(ag)^2$ and
$$
F(\sqrt{d_1})=F(\sqrt{d_2}).
$$
The two nonsingular projective curves are consequently isomorphic over $\PP^1$.

:::

:::

::: {.pf-step #bijection}

There is a bijection
$$
\left\{
\begin{array}{c}
\text{isomorphism classes of}\\
\text{genus-$2$ curves over }k
\end{array}
\right\}
\longleftrightarrow
U/\Sigma_6.
$$

::: pf-proof

Hou, §2 Exercise 2(e), printed p. 6, gives the two halves that do not use step
[](#cover-determined-by-branch){.pf-ref}. First, a genus-$2$ curve $X$ gives its
canonical map, six distinct branch points by step
[](#canonical-degree-two){.pf-ref}, and after an ordering and the normalization
of step [](#normalize-three-points){.pf-ref} a triple in $U$ by step
[](#normal-form){.pf-ref}; changing the ordering changes the triple by exactly
the action of step [](#sigma-six-action){.pf-ref}, so $X$ determines a
well-defined element of $U/\Sigma_6$. Hou's sentence for that is "We then get an
equivalence class $[\beta_1,\beta_2,\beta_3]$". For an isomorphism
$\varphi:X\to X'$ it argues from $\varphi^*K_{X'}\sim K_X$: the complete linear
system of $\varphi^*K_{X'}$ gives a morphism to $\PP^1$ which differs from the
one given by $\abs{K_X}$ by a $\psi\in\Aut(\PP^1)$, so the two branch sets
differ by an automorphism of $\PP^1$, the two six-tuples are normalized to the
same triple, and isomorphic curves give the same orbit. Second, for a prescribed triple, steps
[](#kummer-cover-ramification){.pf-ref}, [](#genus-two){.pf-ref} and
[](#same-as-canonical){.pf-ref} construct a genus-$2$ curve whose canonical map
is branched over the prescribed six points, which is Hou's "also, (b) implies
that starting from six points of $\PP^1$, one can construct a genus two curve":
the map on isomorphism classes is onto.

It remains that two curves in the same orbit are isomorphic, and that is step
[](#cover-determined-by-branch){.pf-ref}: if the canonical maps of $X$ and $Y$
have branch divisors $D$ and $\tau(D)$, then $\tau^{-1}\circ f_Y$ is a
separable degree-two cover of $\PP^1$ with branch divisor $D$, so it is
isomorphic to $f_X$ over $\PP^1$ and $X\cong Y$. Together the three paragraphs
give the bijection.

:::

:::

::: {.pf-step #parameters}

The parameter space of step [](#bijection){.pf-ref} is an open subset of
$\AA^3_k$ modulo a finite group, and it has infinitely many points.

::: pf-proof

Explicitly,
$$
U=\AA^3_k\setminus\Bigl(\bigcup_{i=1}^3\{\beta_i=0\}\cup
\bigcup_{i=1}^3\{\beta_i=1\}\cup\bigcup_{1\le i<j\le3}\{\beta_i=\beta_j\}\Bigr),
$$
so $U$ is open in $\AA^3_k$, and $\Sigma_6$ has order $720$, which is finite.

Hou, §2 Exercise 2(e), printed p. 6, states the correspondence in this form, as
the triples modulo the permutation action. Gruenewald, §2, printed p. 2, states
the global form of the same quotient: the points of the moduli space
$\mathcal M_2(2)$ are the triples $(\lambda_1,\lambda_2,\lambda_3)$ of elements
that are all distinct and different from $0$ and $1$, and the forgetful morphism
$\mathcal M_2(2)\to\mathcal M_2$ is a Galois covering of degree
$720=\cardinality{\Sigma_6}$, in which $\Sigma_6$ acts on the Weierstrass
six-tuple by permutations, followed by renormalizing the first three coordinates
to $(0,1,\infty)$ --- the action of step [](#sigma-six-action){.pf-ref}.

Since $k$ is algebraically closed it is infinite: fixing two admissible distinct
values of $\beta_1$ and $\beta_2$ leaves infinitely many choices of $\beta_3$,
while every $\Sigma_6$-orbit is finite. Hence $U/\Sigma_6$ is infinite and there
are infinitely many isomorphism classes of curves of genus $2$ over $k$.

:::

:::

::: pf-qed

Steps [](#canonical-degree-two){.pf-ref} and
[](#degree-two-is-canonical){.pf-ref} prove part (a), steps
[](#kummer-cover-ramification){.pf-ref}, [](#genus-two){.pf-ref} and
[](#same-as-canonical){.pf-ref} prove part (b), steps
[](#normalize-three-points){.pf-ref} and [](#normal-form){.pf-ref} prove part
(c), step [](#sigma-six-action){.pf-ref} proves part (d), and steps
[](#cover-determined-by-branch){.pf-ref}, [](#bijection){.pf-ref} and
[](#parameters){.pf-ref} prove part (e).

:::

:::

:::


::: {.remark title="Published solution"}
R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025 version [@Vak25, §§19.5--19.6], text version `tmp/sources/vakil-rising-sea-2025-10-21.md`, printed pp. 546--550, proves parts (a) and (b) by a different route: Theorem 19.5.1 (printed p. 546) is the count $2g+2$ of branch points, proved in 19.5.2 (printed pp. 546--547), which constructs the double cover branched at a prescribed even set of points as the normalization of $y^2=f(x)$ and is unique, and in 19.5.4 (printed pp. 547--548), which computes its genus as $r/2-1$ from the \v{C}ech complex of the two affine charts; Proposition 19.5.7 (printed pp. 548--549) shows that a curve of genus at least $2$ admits at most one double cover of $\PP^1$; and 19.6.2 (printed p. 550) assembles the bijection between genus-$2$ curves and double covers branched at six points. His 19.5.2 is the published statement of the one step of part (e) that Reiser's and Hou's solutions do not prove.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.2.2, printed p. 210, text version `tmp/sources/hartshorne-solutions-egbert.md`, classifies genus-2 curves by the six branch points of the canonical double cover, with Hurwitz $2g-2=2(-2)+6$ fixing the count.
:::
