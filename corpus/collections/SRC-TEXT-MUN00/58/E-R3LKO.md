---
schema: qual/card@1
id: E-R3LKO
kind: problem
title: When the inclusion induces an isomorphism on fundamental groups
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 7, printed p. 366,
    with Theorem 58.7, Theorem 58.3 and Corollary 58.5. Parts (a) and (b) are the two sufficient conditions, and the card's counterexample for the converse is $D^2$ with $A=S^1$ and a constant map, where $j_*:\ZZ\to0$ is not an isomorphism. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    Part (b) now has a published source: UC Riverside Math 205A, Fall 2014, Solutions Part 7, the
    sheet's solution of Hatcher's Exercise 0.4, its p. 5, read in the MinerU extraction
    tmp/sources/ucr-math205A-2014-solutions07.md, together with Hatcher's Proposition 1.18 on
    printed p. 37 of *Algebraic Topology* (2002), the homotopy invariance of $\pi_1$ that the sheet
    applies. The solution transcribes the sheet's argument: the hypothesis that $H$ maps $A\times
    I$ into $A$ lets $H$ be read as a homotopy inside $A$ from $f\circ j$ to the identity, so $f$
    and $j$ are homotopy inverse and $j_*$ is an isomorphism. The sheet is correct and needed no
    repair. Parts (a) and (c) have no located published source, and the card says so: (a) uses
    Lemma 58.4 with $h=\operatorname{id}_X$ and $k=j\circ f$ for surjectivity and $f\circ j=
    \operatorname{id}_A$ for injectivity, and (c) uses $X=B^2$, $A=S^1$ and a constant $f$, where
    $\pi_1(A)=\ZZ$ and $\pi_1(X)$ is trivial. Checked against the book: the exercise on printed
    p. 366, the definition of homotopy inverse on printed p. 363, Lemma 58.4 on printed p. 363,
    Theorem 58.7 on printed p. 364, Theorem 54.5 on printed p. 345, and the triviality of
    $\pi_1(B^2)$ used in Theorem 55.2 on printed p. 348. Not claimed: that the sheet treats parts
    (a) or (c) -- it solves Hatcher's Exercise 0.4, which is part (b).
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the sourced part
    and the unsourced parts labelled in its own text.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Parts (a) and (c) now have a published source, in place of the sentences in the 2026-11-11 and
    2026-11-14 events recording that none was located among the sets searched then. Both are
    transcribed from the answer of JacobsonRadical (user 502975) to "Question from Munkres algebraic
    topology section 58: retractions", Math StackExchange question 848636, answer 3426310, posted
    2019-11-07, read 2026-11-15 at
    https://math.stackexchange.com/questions/848636/question-from-munkres-algebraic-topology-section-58-retractions
    and kept at tmp/sources/mse-848636-munkres-58-7.md, its (a) beginning at line 61 and its (c) at
    line 84. Its (a): f o j = id_A together with j o f ~ id_X makes f and j homotopy inverse, so j
    is a homotopy equivalence, and j_* is an isomorphism by Theorem 58.7, which is stated for a map
    f with f(x_0) = y_0 and needs no base-point-fixing homotopy (j(a) = a because j is an
    inclusion). Its (c): X = R^2, A = S^1, f the constant map at c in A and H(x,t) = tx + (1-t)c,
    where j_* : pi_1(S^1) = Z -> pi_1(R^2) = 0 is not an isomorphism, pi_1(S^1) being computed by
    Theorem 54.5. The accepted answer 848727 in that thread was also read and is not the source: it
    argues surjectivity for both parts by saying that the homotopy H gives a loop in A representing
    the same class, which is only true if H fixes the base point, and the exercise does not assume
    that; its counterexample is an annulus rather than the disc. Checked against the book: the
    exercise is §58 Exercise 7 on printed p. 366, read on the page image of
    tmp/sources/munkres-2000-topology.pdf (printed page = PDF page - 15), where Exercises 1 to 8
    print; this corrects the "printed p. 367" that the 2026-11-14 event and the solution text
    carried, Exercise 10 being the exercise of §58 that prints on p. 367. Also checked on their
    printed pages: the definition of a retraction and Theorem 55.2 on p. 348, Lemma 58.4 and the
    definition of homotopy inverse on p. 363, Theorem 58.7 on p. 364, Theorem 54.5 on p. 345.
    Not claimed: that the answer proves (b) -- the Riverside sheet remains that part's source.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Parts (a) and (c) were replaced by the transcription described in the preceding event; part (b)
    is unchanged and keeps its Riverside transcription. Part (a) no longer argues through Lemma
    58.4: the source reaches the same conclusion by exhibiting f as a homotopy inverse of j and
    applying Theorem 58.7, and the card records the reason the exercise's homotopy need not fix the
    base point, and why part (b) needs its extra hypothesis, since a reader who has just used a free
    homotopy in (a) will ask. Part (c) now takes X = R^2 with base point 1, as the source does, in
    place of the closed ball of the earlier proof, and computes pi_1(R^2) from convexity. The
    closing sentence of (c), that H(A x {t}) is not contained in A, is the card's own observation
    about this example and not the source's; it is what keeps (c) from contradicting (b).
- event: solution-reviewed
  by: claude
  date: 2026-11-15
  note: >-
    All three parts of the rewritten solution were read against their sources and the book: (a) and
    (c) against the MSE answer named above and (b) against the Riverside sheet, checking that each
    transcribed statement is the exercise's and each cited result is the one the book states on the
    page named. Not checked: any part of the answer's own (b), which is not used.
---

::: {.exercise}

Let $A$ be a subspace of $X$; let $j: A \to X$ be the inclusion map, and let $f: X \to A$ be a continuous map.
Suppose there is a homotopy $H: X \times I \to X$ between the map $j \circ f$ and the identity map of $X$.

(a) Show that if $f$ is a retraction, then $j_*$ is an isomorphism.

(b) Show that if $H$ maps $A \times I$ into $A$, then $j_*$ is an isomorphism.

(c) Give an example in which $j_*$ is not an isomorphism.
:::

::: {.solution}
The exercise is §58 Exercise 7, printed p. 366; the base point is a point
$x_0\in A$, and $j_*$ is the homomorphism $\pi_1(A,x_0)\to\pi_1(X,x_0)$ induced
by the inclusion.

Parts (a) and (c) are transcribed from the answer of JacobsonRadical to
"Question from Munkres algebraic topology section 58: retractions", Math
StackExchange question 848636, answer 3426310 of 2019-11-07, read 2026-11-15 at
https://math.stackexchange.com/questions/848636/question-from-munkres-algebraic-topology-section-58-retractions
and kept at `tmp/sources/mse-848636-munkres-58-7.md`, where (a) begins at line
61 and (c) at line 84. Part (b) is transcribed from UC Riverside Math 205A, Fall
2014, Solutions Part 7, the sheet's solution of Hatcher's Exercise 0.4, its p. 5,
read in `tmp/sources/ucr-math205A-2014-solutions07.md`. Its point is that the
hypothesis that $H$ maps $A\times I$ into $A$ lets $H$ be read as a homotopy
inside $A$, so that $f$ and $j$ become homotopy inverse, and the conclusion
follows from the homotopy invariance of $\pi_1$: Hatcher, *Algebraic Topology*
(2002), Proposition 1.18, printed p. 37, which in this book is Theorem 58.7,
printed p. 364.

::: pf

::: {.pf-step #a}
(a) If $f$ is a retraction, then $j_*$ is an isomorphism.

::: pf-proof
Let $a$ be the base point. It lies in $A$, and $j(a)=a$ because $j$ is an
inclusion, so $j$ is a map of pointed spaces $j:(A,a)\to(X,a)$ and induces
$j_*:\pi_1(A,a)\to\pi_1(X,a)$.

Since $f$ is a retraction of $X$ onto $A$ and $j$ is the inclusion,
$f\circ j=\operatorname{id}_A$ by the definition of a retraction (printed
p. 348); and the exercise's hypothesis gives
$j\circ f\simeq\operatorname{id}_X$. So each composite of $j$ and $f$ is
homotopic to the identity map of its own space, which by the definition on
printed p. 363 makes $f$ a homotopy inverse of $j$, and $j$ a homotopy
equivalence. Theorem 58.7 (printed p. 364) then makes
$j_*:\pi_1(A,a)\to\pi_1(X,a)$ an isomorphism.

Neither step asks anything more of the homotopy $H$ than the exercise assumes:
it need not fix $a$, and it need not carry $A\times I$ into $A$. Theorem 58.7 is
stated for a map $h:X\to Y$ with $h(x_0)=y_0$, a condition that holds here for
$h=j$ because $j(a)=a$, and its proof carries the general case itself: for a
homotopy inverse $g$ with $g(y_0)=x_1\ne x_0$ it composes the pointed maps
$(X,x_0)\to(Y,y_0)\to(X,x_1)\to(Y,y_1)$ and transports base points along a path
in $X$. Part (b) needs the additional hypothesis $H(A\times I)\subseteq A$
because there $f\circ j$ is not known to equal $\operatorname{id}_A$, only to be
homotopic to it, and it is the restriction of $H$ to $A\times I$ that must
supply the homotopy inside $A$.
:::

:::

::: {.pf-step #b}
(b) If $H$ maps $A\times I$ into $A$, then $j_*$ is an isomorphism.

::: pf-proof
Let $H:X\times I\to X$ be the homotopy from $j\circ f$ to $\operatorname{id}_X$,
and put $K=\restrictionof{H}{A\times I}$, read as a map $K:A\times I\to A$; this
is legitimate because $H(A\times I)\subseteq A$. For $a\in A$,
$$
K(a,0)=H(a,0)=j(f(a))=f(a),\qquad K(a,1)=H(a,1)=a,
$$
so $K$ is a homotopy from $f\circ j$ to $\operatorname{id}_A$, while $H$ itself is
a homotopy from $j\circ f$ to $\operatorname{id}_X$. By the definition on printed
p. 363, $f$ and $j$ are homotopy inverse; so $j$ is a homotopy equivalence and
$j_*$ is an isomorphism by Theorem 58.7 (printed p. 364), that is, by Hatcher's
Proposition 1.18 (printed p. 37).
:::

:::

::: {.pf-step #c}
(c) An example in which $j_*$ is not an isomorphism: $X=\RR^2$, $A=S^1$, and
$f$ the constant map at a point $c\in A$.

::: pf-proof
Let $X=\RR^2$, $A=S^1$ and let $f:X\to A$ be the constant map at $c\in S^1$.
$\RR^2$ is convex, so
$$
H(x,t)=tx+(1-t)c,\qquad 0\le t\le1,
$$
defines a continuous map $H:\RR^2\times I\to\RR^2$; and $H(x,0)=c=j(f(x))$
because $j$ is an inclusion, while $H(x,1)=x=\operatorname{id}_X(x)$. So $H$ is
a homotopy from $j\circ f$ to $\operatorname{id}_X$, and the hypothesis of the
exercise holds for this $X$, $A$ and $f$.

Take the base point $1\in S^1$. Then $j_*:\pi_1(S^1,1)\to\pi_1(\RR^2,1)$, and
$\pi_1(S^1,1)\cong\ZZ$ by Theorem 54.5 (printed p. 345), while
$\pi_1(\RR^2,1)$ is trivial: for a loop $\gamma$ in $\RR^2$ at $1$ the affine
combination $(s,t)\mapsto(1-t)\gamma(s)+t\cdot1$ is a path homotopy from
$\gamma$ to the constant loop at $1$. Hence $j_*$ is a homomorphism
$\ZZ\to0$, which is not injective and so not an isomorphism.

No contradiction with part (b) arises, because its hypothesis fails here: for
$x\in S^1$ with $x\ne c$ and $0<t<1$ the point $tx+(1-t)c$ is a strict convex
combination of two distinct points of the unit circle, so it has norm less than
$1$ and is not in $A$; thus $H(A\times\{t\})\not\subseteq A$ for every such $t$.
:::

:::

:::
:::
