---
schema: qual/card@1
id: P-AGH468BASEPOINTFREENONSPECIAL
kind: problem
title: A base-point-free nonspecial divisor of positive degree $d$ exists iff $d \geq g+1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Genus
  - Riemann-Roch
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.8, the retained Egbert companion notes, and the
    repository's Jacobian/symmetric-product results. The printed statement has
    one boundary exception: on a genus-zero curve the zero divisor has degree
    zero, is nonspecial, and has base-point-free complete linear system. The
    corrected assertion is the printed equivalence for positive degree, or
    equivalently the printed equivalence with the single extra case
    (g,d)=(0,0). The proof below establishes this corrected statement directly
    from Riemann--Roch and dimension estimates in Pic^d(X).
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Hartshorne IV.6.8 prints the equivalence for every degree d, which fails for the zero divisor on P^1 (g=d=0). The statement now assumes d>0.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    The gap in step s3 is closed by numbered statements, and the citation that did not carry it is
    gone. s3 asserted that Pic^0(X) = Jac(X) is an irreducible variety of dimension g, citing the
    internal card T-CRVJACFUN; that card's own citations are a definition of the Picard functor and
    Riemann-Roch, and neither gives existence, completeness or the dimension, so the step was
    resting on an unproved result. Hartshorne states the Jacobian by a universal property in
    IV.4.10 and proves existence only for genus one, in Theorem IV.4.11.

    The step now cites Milne, *Jacobian Varieties*, Chapter VII of *Arithmetic Geometry*: Theorem
    1.1 for existence and representability of Pic^0, with Corollary 4.3 and the closing paragraph
    of its section 4 for the construction and for the morphism C^(r) -> J that steps s4 and s5 take
    images of; Proposition 2.1 for the tangent space H^1(C, O_C) and hence dim J = g; and
    Proposition 7.4 with Theorem 7.6 for completeness. Irreducibility is that of a variety, and the
    genus is dim_k H^1(X, O_X) by Hartshorne's Proposition IV.1.1. Smoothness of the Jacobian is not
    used by this card and is not claimed: it appears in the sources only as prose or through a
    separate representability theorem, and the dimension count here needs no tangent space of
    Pic^d beyond its dimension.

    What was checked and what was not. The numbered statements were read in Milne's own TeX file
    (jmilne.org/math/xnotes/JVs.pdf), whose abstract states that the numbering is unchanged from the
    published chapter; the published scan is image-only and was not OCR'd. Theorem 1.1, Corollary
    4.3, Proposition 2.1, Proposition 7.4 and Theorem 7.6 were each opened at their numbers. Not
    checked: the printed volume itself, and Boschi-Lutkebohmert-Raynaud, whose Chapter 9 supplies the
    same facts as Proposition 3 of 9.2 and Theorem 3 of 8.4 and which is retained here but was not
    needed once Milne's statements did the work.

    Unchanged and still correct: s1 (the only-if direction), s2, s4, s5, s6 and s7, which were read
    in this pass; Riemann-Roch is Theorem IV.1.3 and Serre duality Theorem III.7.6, cited by their
    numbers. No page, PDF page or page offset appears on this card.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The "if" direction is now proved from Riemann-Roch alone, and the Jacobian is gone from the
    proof. The previous version reached existence through the Picard variety: step s3 asserted that
    Pic^d(X) is an irreducible variety of dimension g, s4 and s5 counted dimensions inside it, and s6
    chose a line bundle outside two proper closed subsets. That argument is correct given the
    Jacobian, and the card cited Milne's *Jacobian Varieties*, Theorem 1.1, Proposition 2.1 and
    Proposition 7.4 with Theorem 7.6 for it, but it rested on an existence theorem the book states
    and does not prove.

    The replacement uses two numbered statements only: Riemann-Roch, Theorem IV.1.3, and the
    criterion of Proposition IV.3.1 with its exact sequence. s3 is that criterion: P is a base point
    of |D| exactly when h^0(D-P)=h^0(D), which by subtracting the two Riemann-Roch formulas is
    exactly h^0(K-D+P)=h^0(K-D)+1. s4 is Hartshorne's own greedy construction from the proof of
    Corollary IV.4.10.9: take P_i not a base point of |K-P_1-...-P_{i-1}|, so that after g steps
    h^0(K-E)=0 for E=P_1+...+P_g; every effective D of degree at least g containing E is then
    nonspecial. s5 chooses one further point Q outside a finite set and shows D=E+Q is nonspecial
    with no base points: the set of Q for which some h^0(K-D+R) is nonzero is finite, because for
    S in the support of E the system |K-E+S| has h^0 at most 1 by the same dimension count, hence
    consists of at most one divisor of degree g-1, and the three cases R=Q, R off the support of E
    and R in the support of E are each excluded. s6 adds points one at a time, which preserves both
    properties, and covers every d>=g+1; g=0 is step s2, unchanged.

    What this removes: no Jacobian variety, no Picard scheme, no symmetric product, no
    irreducibility or dimension count on a parameter space, and no Clifford. What it keeps: Serre
    duality, Theorem III.7.6, for h^1 = 0, and Gauss's genus as dim_k H^1 by Proposition IV.1.1
    through Proposition IV.3.1.

    Not checked: the numerical check a review made of the finite bad set on a plane quartic over a
    finite field, which is evidence for the case analysis rather than a proof of it; the case
    analysis itself was read line by line in all three cases.

---

::: {.problem}
Let $d>0$. A curve $X$ of genus $g$ has a nonspecial divisor $D$ of degree $d$ such that $\abs{D}$ has no base points if and only if $d \geq g+1$.
:::

::: {.solution}
Write
$$
L=\OO_X(D).
$$

::: pf

::: {.pf-step #s1}

If $D$ is nonspecial and $\abs{D}$ is base-point free, then either
$$
(g,d)=(0,0)
$$
or
$$
d\ge g+1.
$$

::: pf-proof

Nonspeciality means
$$
h^1(X,L)=0.
$$
Hence Riemann--Roch gives
$$
h^0(X,L)=d+1-g.
$$

Suppose first that
$$
h^0(X,L)=1.
$$
Because $\abs{D}$ has no base points, its unique nonzero section vanishes
nowhere.  It therefore trivializes $L$, so
$$
L\cong\OO_X,
\qquad
d=0.
$$
Nonspeciality now says
$$
0=h^1(X,\OO_X)=g,
$$
so $(g,d)=(0,0)$.

Outside this exceptional case one has
$$
h^0(X,L)\ge2.
$$
Using Riemann--Roch again,
$$
d+1-g=h^0(X,L)\ge2,
$$
and therefore
$$
d\ge g+1.
$$

:::

:::

::: {.pf-step #s2}

If $g=0$ and $d\ge1$, then there is a nonspecial base-point-free
divisor of degree $d$.

::: pf-proof

For a smooth projective genus-zero curve over the algebraically closed ground
field,
$$
X\cong\PP^1.
$$
Take
$$
L=\OO_{\PP^1}(d).
$$
For $d\ge0$ this line bundle is generated by its global sections, so its
complete linear system has no base points.  Also
$$
h^1(\PP^1,\OO(d))=0
$$
for $d\ge-1$, hence in particular for $d\ge1$.  Any divisor $D$ with
$\OO_X(D)\cong L$ has the required properties.

:::

:::

::: {.pf-step #s3}

A point $P$ is a base point of $\abs{D}$ exactly when
$$
h^0(X,\OO_X(D-P))=h^0(X,\OO_X(D))
\iff
h^0(X,\OO_X(K-D+P))=h^0(X,\OO_X(K-D))+1 .
$$

::: pf-proof

The first equivalence is the one of Proposition IV.3.1 and its proof: the
evaluation map $H^0(X,\OO_X(D))\to\OO_X(D)\otimes k(P)\cong k$ has kernel
$H^0(X,\OO_X(D-P))$, so $P$ is a base point exactly when this map is zero,
that is, when $h^0(D-P)=h^0(D)$.

Riemann--Roch, Theorem IV.1.3, applied to $D$ and to $D-P$ gives
$$
h^0(D)-h^0(K-D)=d+1-g,
\qquad
h^0(D-P)-h^0(K-D+P)=d-g,
$$
and subtracting the two shows
$$
h^0(D-P)-h^0(D)=-1+\bigl(h^0(K-D+P)-h^0(K-D)\bigr).
$$
So $h^0(D-P)=h^0(D)$ exactly when
$h^0(K-D+P)=h^0(K-D)+1$.

:::

:::

::: {.pf-step #s4}

There are points $P_1,\dots,P_g\in X$ with
$$
h^0(X,\OO_X(K-P_1-\cdots-P_g))=0 .
$$
Consequently every effective divisor $D$ of degree $d\ge g$ that contains
$P_1+\cdots+P_g$ is nonspecial, and
$$
h^0(X,\OO_X(D))=d+1-g .
$$

::: pf-proof

Start with $E_0=0$, where $h^0(K-E_0)=h^0(K)=g$ by Proposition IV.1.1.
Suppose $h^0(K-E_i)=g-i\ge1$, so that $\abs{K-E_i}$ is nonempty; its base
locus is a proper closed subset of the irreducible curve $X$, so there is a
point $P_{i+1}$ which is not a base point of $\abs{K-E_i}$. By Proposition
IV.3.1, $h^0(K-E_{i+1})=h^0(K-E_i)-1$. After $g$ steps
$h^0(K-E_g)=0$. This is the construction Hartshorne carries out in the proof
of Corollary IV.4.10.9.

If $D\ge E_g$ then $K-D\le K-E_g$, so $h^0(K-D)\le h^0(K-E_g)=0$, and
Riemann--Roch, Theorem IV.1.3, gives $h^0(D)=d+1-g$.

:::

:::

::: {.pf-step #s5}

Let $E=P_1+\cdots+P_g$ be as in step [](#s4){.pf-ref} and let
$$
Z=\bigcup_{S\in\operatorname{Supp}E}\ \bigcup_{A\in\abs{K-E+S}}\operatorname{Supp}A .
$$
Then $Z$ is finite, and for every point $Q\in X\setminus Z$ the divisor
$D=E+Q$ has degree $g+1$, is nonspecial, and satisfies
$h^0(K-D+R)=h^0(K-D)$ for every $R\in X$.

::: pf-proof

$Z$ is finite. Fix $S\in\operatorname{Supp}E$. Since $K-E+S=(K-E)+S$ and
adding a point raises $h^0$ by at most one,
$$
h^0(K-E+S)\le h^0(K-E)+1=1
$$
by the argument of Proposition IV.3.1; so $\abs{K-E+S}$ is empty or consists
of a single divisor, of degree $\deg K-\deg E+1=g-1$ by Example IV.1.3.3.
Its support is therefore finite, and $Z$ is a finite union of finite sets. As
$X$ is an irreducible curve it has infinitely many points, so $Q\notin Z$
exists.

$D=E+Q$ is nonspecial because $K-D\le K-E$ gives $h^0(K-D)\le h^0(K-E)=0$;
its degree is $g+1$, and $h^0(D)=2$ by Riemann--Roch.

Suppose that $h^0(K-D+R)\ge1$ for some $R$. Then
$K-D+R$ is linearly equivalent to an effective divisor, so there is an
effective canonical divisor $K'$ with
$$
K'\ge D-R=E+Q-R .
$$
If $R=Q$, then $K'\ge E$, so $K'-E$ is effective and $h^0(K-E)\ge1$, contrary
to step [](#s4){.pf-ref}. If $R\ne Q$ and $R\notin\operatorname{Supp}E$, then
comparing coefficients at $Q$, at the points of $\operatorname{Supp}E$ and at
all other points shows $K'\ge E$, again contradicting step [](#s4){.pf-ref}.
If $R\in\operatorname{Supp}E$ with $R\ne Q$, then $K'-E+R\ge Q$ is an effective
divisor in $\abs{K-E+R}$, so $Q$ lies in the support of its unique member,
contrary to $Q\notin Z$.

Hence $h^0(K-D+R)=0=h^0(K-D)$ for every $R$, and step [](#s3){.pf-ref} gives
that $\abs{D}$ has no base points.

:::

:::

::: {.pf-step #s6}

If $g\ge1$ and $d\ge g+1$, there exists a nonspecial line bundle
$L$ of degree $d$ whose complete linear system has no base points.

::: pf-proof

Take $D_0=E+Q$ as in step [](#s5){.pf-ref}: it has degree $g+1$, it is
nonspecial, and $\abs{D_0}$ has no base points.

If $d>g+1$, add $d-g-1$ further points one at a time. Adding a point
preserves both properties: if $h^0(K-D)=0$ and $h^0(K-D+P)=0$ for every $P$,
then $K-D-R\le K-D$ gives $h^0(K-D-R)=0$ and $K-D-R+P\le K-D+P$ gives
$h^0(K-D-R+P)=0$, so step [](#s3){.pf-ref} applies to $D+R$.

Let $D$ be the resulting divisor. Then $\deg D=d$,
$h^1(X,\OO_X(D))=0$ by Serre duality, Theorem III.7.6, and $\abs{D}$ has no
base points. Taking $L=\OO_X(D)$ gives the claim.

:::

:::

::: {.pf-step #s7}

For positive degree $d$, a nonspecial divisor of degree $d$ with
base-point-free complete linear system exists if and only if
$$
\boxed{d\ge g+1}.
$$

::: pf-proof

For the forward implication, positive degree rules out the exceptional case
in step [](#s1){.pf-ref}, so that step gives $d\ge g+1$.

For the reverse implication, step [](#s2){.pf-ref} proves existence when $g=0$, and
step [](#s6){.pf-ref} proves it when $g\ge1$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the statement.

:::

:::

:::
