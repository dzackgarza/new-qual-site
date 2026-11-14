---
schema: qual/card@1
id: E-WRMSX
kind: problem
title: Antipode-separating maps of the sphere are surjective
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
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
    Checked line by line against Munkres, Topology (2000), Section 57 Exercise 2, printed p. 359,
    with Theorem 57.3 and the book's hint that $S^2-p$ is homeomorphic to $\RR^2$. The card composes $g$ with a homeomorphism $S^2-p\to\RR^2$ off a point missed by $g$ and applies Borsuk-Ulam, so the injectivity of that homeomorphism gives $g(x)=g(-x)$. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Math StackExchange question 1250275, answer 1250354
    by Michael Albanese (2015), held at tmp/sources/mse-1250275.md, a forum answer and cited as
    one. The solution is that answer transcribed, with the injectivity of stereographic projection
    written out in full, which the answer uses in the word "therefore". The answer is correct and
    needed no repair. Checked against the book: the exercise text and its hint on printed p. 359,
    and Theorem 57.3 (Borsuk-Ulam for $S^2$) on printed p. 358, the only theorem the proof uses
    beyond the homeomorphism the hint supplies. The answer's second paragraph, that $\varphi\circ g$
    need not be surjective and that the theorem applies to maps into $\RR^2$ that are not
    surjective, is stated in the card's opening paragraph; the proof does not use surjectivity of
    $\varphi\circ g$ anywhere. Not claimed: peer review of the source -- it is a forum answer, and
    its correctness is established here by the check against the book, not by its provenance.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the source and its
    pages named in its own text and the stereographic formula and its injectivity supplied. The
    earlier proof was the same argument in one paragraph and was removed because the card is to
    carry the published one.
---

::: {.exercise}

Show that if $g: S^2 \to S^2$ is continuous and $g(x) \neq g(-x)$ for all $x$, then $g$ is surjective.
[Hint: If $p \in S^2$, then $S^2 - \theset{p}$ is homeomorphic to $\RR^2$.]
:::

::: {.solution}
The exercise is §57 Exercise 2, printed p. 359, whose hint is that $S^2-p$ is
homeomorphic to $\RR^2$. The proof is transcribed from a forum answer: Math
StackExchange question 1250275, answer 1250354 by Michael Albanese (2015), held
at `tmp/sources/mse-1250275.md`, and cited as a forum answer. It is a proof by
contraposition, and it uses only the Borsuk--Ulam theorem (Theorem 57.3,
printed p. 358) together with the injectivity of the homeomorphism the hint
supplies. The answer also records a point about the theorem that a first
reading gets wrong: $\varphi\circ g$ need not be surjective, and the
Borsuk--Ulam theorem applies to every continuous map of $S^2$ into $\RR^2$,
surjective or not.

::: pf

::: {.pf-step #not-surjective}
If $g$ is not surjective, then $g(S^2)\subseteq S^2-\theset{p}$ for some
$p\in S^2$.

::: pf-proof
Choose $p\notin g(S^2)$, possible because $g$ is not surjective. Then every
value of $g$ lies outside $\theset{p}$, which is the assertion.
:::

:::

::: {.pf-step #stereographic}
There is a continuous injective map $\varphi:S^2-\theset{p}\to\RR^2$.

::: pf-proof
After composing with a rotation of $S^2$, which is a homeomorphism of $S^2$ and
carries $S^2-\theset{p}$ onto $S^2-\theset{N}$ with $N=(0,0,1)$ the north pole,
it is enough to treat $p=N$. Stereographic projection from $N$,
$$
\varphi(x)=\frac{1}{1-x_3}(x_1,x_2),
$$
is defined and continuous on $S^2-\theset{N}$, and it is injective: if
$\varphi(x)=\varphi(y)=z$ with $x\ne N$, then $x_1=(1-x_3)z_1$ and
$x_2=(1-x_3)z_2$, and $x_1^2+x_2^2+x_3^2=1$ gives
$(1-x_3)^2\norm z^2=(1-x_3)(1+x_3)$, so that, since $x_3\ne1$,
$1-x_3=2/(1+\norm z^2)$ and $x_3=({\norm z^2-1})/({\norm z^2+1})$; the same
computation returns $y_3=x_3$, and then $y_1=x_1$ and $y_2=x_2$. Hence
$\varphi(x)=\varphi(y)$ implies $x=y$.
:::

:::

::: {.pf-step #borsuk-ulam}
$\varphi\circ g:S^2\to\RR^2$ is defined and continuous, so there is
$x\in S^2$ with $(\varphi\circ g)(x)=(\varphi\circ g)(-x)$.

::: pf-proof
By step [](#not-surjective){.pf-ref} the image of $g$ is contained in
$S^2-\theset{p}$, so the composite is defined; it is continuous, $g$ being
continuous and $\varphi$ continuous by step [](#stereographic){.pf-ref}. The
Borsuk--Ulam theorem for $S^2$ (Theorem 57.3, printed p. 358) applies to every
continuous map of $S^2$ into $\RR^2$ and gives such a point $x$.
:::

:::

::: {.pf-step}
$g(x)=g(-x)$ for some $x\in S^2$, so $g$ is surjective.

::: pf-proof
By step [](#borsuk-ulam){.pf-ref} there is $x$ with
$\varphi(g(x))=\varphi(g(-x))$, and $\varphi$ is injective by step
[](#stereographic){.pf-ref}, so $g(x)=g(-x)$. Thus a continuous
$g:S^2\to S^2$ that satisfies $g(x)\ne g(-x)$ for every $x$ cannot fail to be
surjective, which is the assertion of the exercise.
:::

:::

:::
:::
