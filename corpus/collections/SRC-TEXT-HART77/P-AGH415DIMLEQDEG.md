---
schema: qual/card@1
id: P-AGH415DIMLEQDEG
kind: problem
title: $\dim \abs{D} \leq \deg D$ for an effective divisor, with equality iff $D=0$ or $g=0$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Riemann-Roch
  - Genus
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Hartshorne IV.1.5 and independently derived the proof before comparing it with the retained solution transcription; cross-checked the linear-series and genus-zero bounds against Stacks Tags 0CCS and 0C6T.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), IV.1.5, printed
    p. 298 (PDF p. 313 of tmp/sources/hartshorne-1977-algebraic-geometry.pdf, text version `tmp/sources/hartshorne-1977-algebraic-geometry.md`).
    Published proof located: the Stacks Project, Chapter 53, Section 53.3
    and Section 53.10, tag by tag, read in
    tmp/sources/stacks-tags/0CCS.md and tmp/sources/stacks-tags/0C6T.md, which
    are the site's build from stacks-project commit
    a04446e57ec1fbc252a871afcec7752fb2807b14 (28 July 2026); the printed pages
    below are those of the retained compiled book of version ed88ff78, compiled
    14 July 2026 (tmp/sources/stacks-project-book.pdf), and are cited as that
    book's folios, not as a text read: the whole compiled book has no text
    version, so every quotation here is from
    tmp/sources/stacks-tags/0CCS.md and its companions. Lemma 53.3.5 (tag 0CCS), printed
    pp. 4436--4437, states exactly the exercise's first claim and half of its
    second: for a proper curve with H^0(O_X) = k, having a g^r_d forces r <= d,
    and equality forces H^1(X, O_X) = 0, i.e. genus 0. Its proof is the divisor
    sequence 0 -> O_X -> L -> L|D -> 0 with dim H^0(D, L|D) = deg D, which is
    step s2 here; for the equality case it doubles the line bundle and then
    passes to a large even power with vanishing H^1, where the card uses
    Riemann--Roch and l(P) = 2 instead (steps s5--s7). The converse, g = 0 giving
    equality, is Lemma 53.10.2(1) (tag 0C6T), printed p. 4450: dim H^0 = d+1 for
    d > 0. The earlier note's claim of a cross-check against these two tags is
    what this entry turns into a citation in the body; the tags are the right
    ones. Checked: that Hartshorne's "curve" (nonsingular projective over an
    algebraically closed field) satisfies the lemma's hypotheses, H^0(X, O_X) = k
    holding because X is connected, proper and reduced. Not checked: nothing in
    Stacks was needed for the case D = 0, which is trivial.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Correction, on a reader's report of issue #121. The event above states
    0CCS's equality clause as the exercise's equality half without its missing
    hypothesis. As printed (Stacks, Chapter 53, Lemma 53.3.5, tag 0CCS, pp.
    4436--4437) the lemma carries no d > 0 condition, and its equality clause is
    then false at d = 0: (O_X, H^0(O_X)) is a g^0_0 on every curve, and r = d = 0
    holds on a curve of genus g > 0 without g = 0. The printed proof needs the
    hypothesis where it passes to a power of L with vanishing H^1, using that L
    is ample; O_X is not ample. The card's body now cites 0CCS for D != 0 only,
    names the missing hypothesis and why it is needed, and proves D = 0 in step
    s3 (dim |0| = 0 = deg 0). The same reading was taken of 0C6T, Lemma
    53.10.2(1) of the same chapter, printed p. 4450, which states dim H^0 = d + 1
    for d > 0 and whose d = 0 case is again step s3. The inequality r <= d is
    unaffected: it holds at d = 0 as well.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Re-read against the replaced text versions: 0CCS and 0C6T are now files of
    their own, tmp/sources/stacks-tags/0CCS.md and 0C6T.md, holding the tag
    page's statement and proof with its LaTeX, from the site's build of
    stacks-project commit a04446e57ec1fbc252a871afcec7752fb2807b14 (28 July
    2026). The earlier events' reference to one compiled text file and their
    version are replaced accordingly; their printed pages were re-checked in the
    retained compiled book and are right. Against the new files both readings
    above hold: 53.3.5's printed statement has no d > 0 hypothesis and its
    equality proof passes to a large even power "since L is ample", which O_X is
    not; 53.10.2 assumes deg L = d > 0. Nothing else on the card rested on the
    truncated text.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.1.5, printed p. 84,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.1.5, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed
    dim|D| = l(D) - 1 = deg D - g + l(K-D), the bound l(K-D) <= l(K),
    and the value l(K) = g that the conclusion needs. Not checked: Yang's Solutions outside printed pp. 84-85; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.1.5 at printed
    p. 84 beside the entry already there. No step, statement or
    hypothesis of the card changes.
---

::: {.problem}
For an effective divisor $D$ on a curve $X$ of genus $g$, show that $\dim \abs{D} \leq \deg D$.
Furthermore, equality holds if and only if $D=0$ or $g=0$.
:::

::: {.solution}
The Stacks Project, Chapter 53 (Curves), Lemma 53.3.5 (tag 0CCS), printed pp. 4436--4437 of the retained compiled book of version ed88ff78 compiled 14 July 2026 and read in `tmp/sources/stacks-tags/0CCS.md` (the site's build from stacks-project commit a04446e57ec1fbc252a871afcec7752fb2807b14, 28 July 2026), is the inequality together with the equality case for $D\ne0$: if a proper curve $X$ with $H^0(X,\OO_X)=k$ has a $g^r_d$, then $r\le d$, and if equality holds with $d>0$ then $H^1(X,\OO_X)=0$, that is $g=0$. A $g^r_d$ is exactly a linear system $\abs{D}$ of degree $d$ and dimension $r$. The hypothesis $d>0$ is not in the printed statement and is needed for its equality clause: at $d=0$ the pair $(\OO_X,H^0(X,\OO_X))$ is a $g^0_0$ on every curve, and on a curve of genus $g>0$ it has $r=d=0$ without $g=0$; the proof's step to a large power with vanishing $H^1$ uses that $\mathcal L$ is ample, and $\OO_X$ is not. So the lemma is cited here for $D\ne0$, and the case $D=0$ is proved on this card in step [](#s3){.pf-ref}. The converse, $g=0$ giving equality for every effective $D$, is Lemma 53.10.2(1) of the same chapter (tag 0C6T), printed p. 4450 and read in `tmp/sources/stacks-tags/0C6T.md`: for $X$ of genus $0$ and $\deg L=d>0$, $\dim_k H^0(X,L)=d+1$, whose $D=0$ case is again step [](#s3){.pf-ref}. Steps [](#s2){.pf-ref} and [](#s5){.pf-ref}--[](#s7){.pf-ref} prove the two halves of 0CCS from the divisor sequence and Riemann--Roch rather than by its route through a large power with vanishing $H^1$; step [](#s4){.pf-ref} is 0C6T(1) in Riemann--Roch form.
Write
$$
d=\deg D,
\qquad
\ell(D)=h^0(X,\mco_X(D)).
$$
Since $D$ is effective, $d\ge0$ and
$$
\dim\abs{D}=\ell(D)-1.
$$

::: pf

::: {.pf-step #s1}

The divisor sequence gives
$$
0\to\mco_X\to\mco_X(D)\to\mco_X(D)\restrict_D\to0,
$$
and
$$
h^0(D,\mco_X(D)\restrict_D)=d.
$$

::: pf-proof

The first map is multiplication by the canonical section with zero divisor
$D$. The finite scheme $D$ has length $d$. Since
$\mco_X(D)\restrict_D$ is locally free of rank one on $D$, it also has length
$d$, so its space of global sections has dimension $d$.

:::

:::

::: {.pf-step #s2}

One has $\dim\abs{D}\le\deg D$.

::: pf-proof

Global sections of step [](#s1){.pf-ref} give
$$
0\to H^0(X,\mco_X)\to H^0(X,\mco_X(D))
\to H^0(D,\mco_X(D)\restrict_D).
$$
Since $h^0(X,\mco_X)=1$, step [](#s1){.pf-ref} gives
$\ell(D)\le d+1$. Therefore
$$
\dim\abs{D}=\ell(D)-1\le d=\deg D.
$$

:::

:::

::: {.pf-step #s3}

If $D=0$, then equality holds.

::: pf-proof

Here $\ell(0)=h^0(X,\mco_X)=1$, so
$$
\dim\abs{0}=0=\deg0.
$$

:::

:::

::: {.pf-step #s4}

If $g=0$, then equality holds for every effective $D$.

::: pf-proof

The case $D=0$ is step [](#s3){.pf-ref}. If $d>0$, Riemann--Roch gives
$$
\ell(D)-\ell(K-D)=d+1.
$$
Now $\deg K=-2$, so $\deg(K-D)<0$ and hence
$\ell(K-D)=0$. Thus $\ell(D)=d+1$, and therefore
$$
\dim\abs{D}=d=\deg D.
$$

:::

:::

::: {.pf-step #s5}

Conversely, suppose equality holds and $D\ne0$. Then
$\ell(K-D)=g$.

::: pf-proof

Equality means $\ell(D)=d+1$. Riemann--Roch gives
$$
\ell(D)-\ell(K-D)=d+1-g.
$$
Hence $\ell(K-D)=g$. It also gives $\ell(K)=g$.

:::

:::

::: {.pf-step #s6}

Choose a point $P$ in the support of $D$.

::: pf-proof

Because $D-P$ is effective, the section spaces for $K-D$, $K-P$, and $K$ are nested.
The first and third have dimension $g$ by step [](#s5){.pf-ref}, so the middle one also has dimension $g$. Riemann--Roch for the degree-one divisor $P$ then gives
$$
\ell(P)=2.
$$

:::

:::

::: {.pf-step #s7}

The equality $\ell(P)=2$ forces $X\cong\PP^1$, hence $g=0$.

::: pf-proof

Constants give one section of $\mco_X(P)$, so a second linearly independent section gives a nonconstant rational function
$$
f\in H^0(X,\mco_X(P)).
$$
Its pole divisor is bounded by $P$. Since every global regular function on the proper integral curve $X$ is constant, $f$ must actually have pole divisor exactly $P$.

Thus $f$ defines a finite morphism
$$
f:X\longrightarrow\PP^1
$$
whose degree is the degree of its polar divisor, namely $1$. A finite degree-one morphism between integral smooth projective curves is birational, and since $\PP^1$ is normal it is an isomorphism. Hence $X\cong\PP^1$ and $g=0$.

:::

:::

::: {.pf-step #s8}

Equality holds if and only if $D=0$ or $g=0$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove the two sufficient cases. Steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} show that equality with $D\ne0$ forces $g=0$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the inequality and step [](#s8){.pf-ref} characterizes equality.

:::

:::

:::

::: {.remark title="Published solution"}
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.1.5, printed p. 207, text version `tmp/sources/hartshorne-solutions-egbert.md`, computes $\dim\abs{D}=h^0(D)-1=\deg D-g+h^0(K-D)\le\deg D-g+h^0(K)=\deg D$ using $h^0(K)=g$, and reads off equality exactly when $h^0(K-D)=h^0(K)$, that is $D=0$ or $g=0$. Lomont, Chapter IV §1, Exercise 1.5, PDF p. 4, text version `tmp/sources/hartshorne-solutions-lomont.md`, has the same argument.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.1.5, printed p. 84, runs Riemann--Roch: $\dim\linearsystem{D}=\ell(D)-1=\deg D-g+\ell(K-D)$, and $\ell(K-D)\le\ell(K)=g$ for $D$ effective, so $\dim\linearsystem{D}\le\deg D$ with equality only for $D=0$ or $g=0$. Its display of the last input is wrong as printed: it writes $\ell(K)-\ell(K-K)=2g-2+1-g=g$, where $2g-2+1-g=g-1$ and the value $g$ comes from $\ell(K)-\ell(0)=g-1$ with $\ell(0)=1$. The conclusion uses $\ell(K)=g$, which is right.
:::
