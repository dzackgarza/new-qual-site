---
schema: qual/card@1
id: P-AGH512HILBPOLY
kind: problem
title: Hilbert polynomial of an embedded surface in terms of a hyperplane section
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Adjunction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.2, the retained Egbert companion derivation, the
    cohomological Hilbert-polynomial definition, surface Riemann--Roch,
    adjunction, and the repository's degree/intersection definitions. The
    source statement needs no correction. The proof below compares
    Riemann--Roch for nH directly with the Hilbert polynomial, then uses a
    smooth member of |H| only to rewrite the linear coefficient by adjunction.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 5.1.2, printed p. 100,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne V.1.2, printed p. 366, which the card's earlier events record as
    read at a 110 dpi render of the text-layerless page; this pass did not reopen
    it, and the comparison is against the statement the card carries. Recomputed
    the Hilbert polynomial P(n) = (1/2)n^2 H^2 - (1/2)n H.K + 1 + p_a and the two
    coefficient identities that follow from it. Not checked: Yang's Solutions outside printed pp. 100-107; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 5.1.2 at printed
    p. 100 beside Egbert's entry, with the slips its text carries.
    No step, statement or hypothesis of the card changes.
---

::: {.problem}
Let $H$ be a very ample divisor on the surface $X$, corresponding to a projective embedding $X \subseteq \PP^N$.
If we write the Hilbert polynomial of $X$ (III, Ex.
5.2) as
$$
P(z)=\frac{1}{2} a z^2+b z+c
$$
show that $a=H^2$, $b=\frac{1}{2} H^2+1-\pi$, where $\pi$ is the genus of a nonsingular curve representing $H$, and $c=1+p_a$.
Thus the degree of $X$ in $\PP^N$, as defined in (I, §7), is just $H^2$.
Show also that if $C$ is any curve in $X$, then the degree of $C$ in $\PP^N$ is just $C . H$.
:::

::: {.solution}
Let $K_X$ be a canonical divisor on $X$.

::: pf

::: {.pf-step #s1}

For every integer $n$,
$$
P(n)
=
\chi\bigl(\OO_X(nH)\bigr)
=
\chi(\OO_X)
+\frac12 n^2H^2
-\frac12 n(H\cdot K_X).
$$

::: pf-proof

Because the embedding is defined by the very ample divisor $H$, its twisting
sheaf is
$$
\OO_X(1)\cong\OO_X(H).
$$
The cohomological description of the Hilbert polynomial in [[D-COHEULER]]
therefore gives
$$
P(n)=\chi\bigl(\OO_X(nH)\bigr).
$$

Apply surface Riemann--Roch [[T-COHRRS]] to the divisor $nH$:
$$
\begin{aligned}
\chi\bigl(\OO_X(nH)\bigr)
&=
\chi(\OO_X)
+\frac12(nH)\cdot(nH-K_X)\\
&=
\chi(\OO_X)
+\frac12 n^2H^2
-\frac12 n(H\cdot K_X).
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

Comparing coefficients with
$$
P(z)=\frac12az^2+bz+c
$$
gives
$$
a=H^2,
\qquad
b=-\frac12H\cdot K_X,
\qquad
c=\chi(\OO_X)=1+p_a(X).
$$

::: pf-proof

Step [](#s1){.pf-ref} is a polynomial identity in $n$, so comparison of its quadratic,
linear, and constant coefficients gives the first two formulas and
$$
c=\chi(\OO_X).
$$

Since $X$ is a surface, the definition of arithmetic genus in
[[D-COHEULER]] is
$$
p_a(X)
=
(-1)^2\bigl(\chi(\OO_X)-1\bigr)
=
\chi(\OO_X)-1.
$$
Thus
$$
c=1+p_a(X).
$$

:::

:::

::: {.pf-step #s3}

If $H_0\in\abs{H}$ is a nonsingular curve of genus $\pi$, then
$$
H\cdot K_X=2\pi-2-H^2.
$$

::: pf-proof

Because $H$ is very ample, Bertini's theorem [[T-BERTINI]] gives a
nonsingular member
$$
H_0\in\abs H.
$$
Its divisor class is $H$.  The adjunction formula [[T-SRFADJ]] gives
$$
2\pi-2
=
H_0\cdot(H_0+K_X)
=
H^2+H\cdot K_X.
$$
Rearranging proves the formula.

:::

:::

::: {.pf-step #s4}

The linear coefficient is
$$
\boxed{
b=\frac12H^2+1-\pi
}.
$$

::: pf-proof

Substitute step [](#s3){.pf-ref} into the expression for $b$ from step [](#s2){.pf-ref}:
$$
\begin{aligned}
b
&=-\frac12(2\pi-2-H^2)\\
&=\frac12H^2+1-\pi.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

The degree of the embedded surface is
$$
\boxed{\deg X=H^2}.
$$

::: pf-proof

For a projective scheme of dimension $2$, the leading coefficient of its
Hilbert polynomial is
$$
\frac{\deg X}{2!}
$$
by [[D-L6ERW]].  Step [](#s2){.pf-ref} says that the leading coefficient here is
$$
\frac12H^2.
$$
Therefore
$$
\deg X=H^2.
$$

:::

:::

::: {.pf-step #s6}

If $C\subseteq X$ is any curve, then
$$
\boxed{\deg_{\PP^N}C=C\cdot H}.
$$

::: pf-proof

The hyperplane bundle of the given embedding restricts to
$$
\OO_C(1)
\cong
\OO_X(H)\restrict_C.
$$
The degree of the embedded curve $C\subseteq\PP^N$ is the degree of this
hyperplane line bundle.  By the definition of the surface intersection
pairing [[D-SRFINT]],
$$
\deg_C\bigl(\OO_X(H)\restrict_C\bigr)=C\cdot H.
$$
Hence
$$
\deg_{\PP^N}C=C\cdot H.
$$

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s4){.pf-ref} give the three coefficients of the Hilbert polynomial,
step [](#s5){.pf-ref} identifies the degree of $X$, and step [](#s6){.pf-ref} proves the degree
formula for every curve $C\subseteq X$.

:::

:::

:::

::: {.remark title="Published solution"}
The exercise stands on printed p. 366 of Hartshorne, the second of the EXERCISES opening §V.1, read off that page of `tmp/sources/hartshorne-1977-algebraic-geometry.pdf` (printed p. $N$ is PDF p. $N+15$; the pages of §V.1 carry no text layer and were read as a 110 dpi render, folio 366 in the footer); the statement above is that page's text, which prints the polynomial as $F(z)$ and the embedding as $X\subseteq\PP^n$, both rendered here with the card's letters.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.1.2: by surface Riemann--Roch, $\chi(nH)=\frac12(nH)\cdot(nH-K_X)+1+p_a$, so $a=H^2$ and $c=1+p_a$; adjunction on a nonsingular member of $\abs{H}$ gives $H\cdot K_X=2\pi-2-H^2$, which is the linear coefficient; "by I.7, the degree is $\dim(X)!$ times the first coefficient, so it's $H^2$". For the degree of a curve he plugs the two exact sequences $0\to\OO_X(-C)\to\OO_X\to\OO_C\to0$ and $0\to\OO_X(-C-H)\to\OO_X(-H)\to\OO_C(-H\restrict_C)\to0$ back into exercise V.1.2 itself, so that paragraph argues in a circle. Step [](#s6){.pf-ref} obtains $\deg C=C\cdot H$ from $\OO_C(1)\cong\OO_X(H)\restrict_C$. Matches on the two coefficients and the degree of $X$; the degree formula is supplied here.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 5.1.2, is the same computation: $\chi(nH)=\frac12(nH)\cdot(nH-K)+1+p_a$ makes $P(n)=\frac12n^2H^2-\frac12n\,H\cdot K+1+p_a$ for $n\gg0$, so $a=H^2$ and $c=1+p_a$; adjunction $H\cdot(H+K)=2\pi-2$ gives $H\cdot K=2\pi-2-H^2$ and $b=\frac12H^2+1-\pi$; and for a curve $C$ on $X$, a hyperplane meeting both $C$ and $X$ transversally gives $C\cdot H=\#(C\cap X\cap S)=\deg C$ by Bézout, which is the degree statement.
:::
