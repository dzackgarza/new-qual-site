---
schema: qual/card@1
id: P-AGH434RATIONALNORMALCURVE
kind: problem
title: The rational normal curve of degree $d$ in $\PP^d$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Very Ample Divisors
  - Genus
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.4 together with the d-uple embedding from I.2.12 and
    the degree/genus comparison referenced in II.7.8.5. The proof below
    independently proves projective normality and quadratic generation by a
    monomial straightening argument, then proves the minimal-degree
    classification from h^0(L) <= deg L + 1 without invoking a stronger
    classification theorem.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Printed exercise read again for this pass: Hartshorne, Algebraic Geometry
    (1977), IV.3.4, printed p. 315 (PDF p. 330 of the checked-in extraction
    tmp/sources/hartshorne-1977-algebraic-geometry.md), parts (a) and (b) with
    the two sentences that follow (b), which the card's statement carries. The
    published solution named in the brief was read at the cited place in its text
    version: Chin-Lung Wang's Algebraic Geometry II (NTU, 2020 Spring), Chapter
    IV homework, section 3 Exercise 4 by Yu-Chi Hou,
    tmp/sources/ntu-ag2-chapter4.md; part (a) is on printed pp. 8--9 and parts
    (b), (c), (d) on printed p. 10, page positions fixed on
    tmp/sources/ntu-ag2-chapter4.pdf, whose printed folio is its PDF page. The
    brief names part (a) only; (b) is proved there too, at p. 10, and is
    transcribed with it.

    What the source proves and what it does not: its division of the ideal by the
    quadrics g_ij is complete, but the degree count that closes its
    integral-closure argument is garbled as printed (p. 8: "mn = m(n-1) +
    dk_{n-1} + ... = m + dk_1 = dk_0. Hence, m = dk_{n-1} => d | m", with n and
    d interchanged in the indices of the next display) and its toric restatement
    at pp. 8--9 gives a monoid that is not the one of the d-uple embedding. Both
    are recorded in COMPLAINTS.md under this date. What this pass did not do: it
    did not re-read Egbert, whose citation is that of an earlier event and stands
    unchanged.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the transcription of Hou's solution, one step per
    published argument, each step naming part and printed page: s1 and s8's
    identification S(X) = k[t_0^d,...,t_1^d] (Hou (a), printed p. 8, from I Ex
    2.12), s2 the integral-closure argument (p. 8; its garbled degree count
    replaced by the reason the conclusion follows, which is s1), s3 and s4 the
    quadrics (p. 9), s5--s8 part (b) (p. 10), s9 and s10 the degree-2 and
    degree-3 consequences (p. 10). The monomial count in s1, and the expansions
    of Hou's three compressed sentences -- that dim|D| = n is completeness of
    the system, that g(X)=0 gives X = P^1 and O_X(1) = O_{P^1}(d), and that the
    t_1-exponent ranges in s4 meet only at the multiples of n -- are marked in
    the text as the card's own where they replace the source's word; the
    mathematics they supply is a definition or a citation of IV.1.3.5 and IV
    Ex 1.5 in each case. The parts of the statement the source treats only by
    citation are (a)'s projective normality, whose proof is the source's
    integral-closure argument, and (b)'s final identification with nu_d, which
    the source states in one sentence. Checked against the book: (a)'s two
    assertions, (b)'s hypotheses d <= n and nondegeneracy, and the two "in
    particular" sentences, printed p. 315.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    #121 reader's report on this round, and the two events of this date
    restored. The step names s1--s10 in the restored events above are those of
    the card as it stood that day, before it was given named steps; the two
    steps this event changes are #strict-inequality and #genus-zero.
    Part (b)'s degree and genus are printed in Egbert, so they are
    transcribed rather than redone: steps #strict-inequality and #genus-zero now
    give A. Egbert, Solutions to Hartshorne's Algebraic Geometry (2013),
    IV.3.4(b), printed p. 220, his chain "l(D) = n+1 <= deg(D)+1 = d+1 <= n+1.
    Thus n = d. Since deg(D) = dim(D), and d != 0, then by exc IV.1.5, g = 0",
    and the identification in his closing sentence. The proof written earlier
    today, from h^0 <= e+1 by induction and then a degree-one map to P^1, is
    withdrawn: the same chain is printed, so the source governs. Two slips of
    his are named on the card, not copied: l(D) = n+1 is what nondegeneracy
    gives as l(D) >= n+1, and "deg(D) = dim(D)" compares the degree with the
    dimension of the linear system, where what the citation needs is
    deg D = dim|D|. The reader named the page as printed p. 219; part (a) is on
    that page and the proof of (b) is on the next, whose printed folio is 220.
    The restored source-checked event says Hou's (b) at printed p. 10 "is
    transcribed with it": Hou's (b) states dim|D| = n and does not establish it,
    and what the card takes from Hou in part (b) is the closing sentence of his,
    not the degree and genus. Three further corrections on this card: the
    solution's opening sentence said the whole solution was the transcription
    of Hou, where four of its ten steps are the card's own; the expansion of
    Hou's closing sentence said a divisor of degree d on P^1 "is d times a
    point", where a divisor of degree d is linearly equivalent to dP; and the
    remark's Egbert sentence said he checks the surjectivity of the restriction
    maps and identifies the quadrics Q_ij as generators, where printed p. 219
    asserts both halves of (a) in one sentence each and proves neither and names
    no Q_ij. The remark also called IV.1.3.5 an exercise, where it is an Example
    of the text; it is cited as one. The text-version paths that stood in the
    rendered solution's opening sentence and in both remark paragraphs are out of
    them and recorded here. Where and how the sources were read:
    Egbert in tmp/sources/hartshorne-solutions-egbert.md, section 4.3.6 for
    printed p. 219 and the section headed "4.3.7 b. x g" for printed p. 220, the
    page positions read off the folios of
    tmp/sources/hartshorne-solutions-egbert.pdf, whose printed folio is its PDF
    page; Hou in tmp/sources/ntu-ag2-chapter4.md, (a) on printed pp. 8--9 and
    (b)--(d) on printed p. 10, positions fixed on
    tmp/sources/ntu-ag2-chapter4.pdf; and the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, IV.3.4 on printed p. 315
    and IV.1.3.5 in the Examples of §IV.1. Not read in this pass: Egbert's
    IV.3.5, IV.3.6 and IV.3.7, which cite IV.3.4(b), and any search outside the
    brief's three sources for part (a)'s projective normality, which remains the
    card's own proof from Exercise II.5.14(d). The two events of this date above
    were rewritten in place by e4872b53d6; they are restored to the text they
    carried when written, and this event is the correction.
---

::: {.problem}
Let $X$ be the $d$-uple embedding (I, Ex.
2.12) of $\PP^1$ in $\PP^d$, for any $d \geq 1$.
We call $X$ the \dfn{rational normal curve} of degree $d$ in $\PP^d$.

(a) Show that $X$ is projectively normal, and that its homogeneous ideal can be generated by forms of degree 2.

(b) If $X$ is any curve of degree $d$ in $\PP^n$, with $d \leq n$, which is not contained in any $\PP^{n-1}$, show that in fact $d=n$, $g(X)=0$, and $X$ differs from the rational normal curve of degree $d$ only by an automorphism of $\PP^d$.
Cf.
(II, 7.8.5).

In particular, any curve of degree 2 in any $\PP^n$ is a conic in some $\PP^2$.

A curve of degree 3 in any $\PP^n$ must be either a plane cubic curve, or the twisted cubic curve in $\PP^3$.
:::

::: {.solution}
Each step names the published argument it transcribes, or says that it is the card's own. The transcription is Chin-Lung Wang's Algebraic Geometry II (National Taiwan University, 2020 Spring), Chapter IV homework, §3 Exercise 4 by Yu-Chi Hou — part (a) on printed pp. 8--9 and parts (b)--(d) on printed p. 10 — and, for the degree and the genus of part (b), A. Egbert's *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.4(b), printed p. 220. Four of the ten steps are the card's own.

Write $S(X)=k[x_0,\ldots,x_d]/I(X)$ for the homogeneous coordinate ring of
$$
X=\nu_d(\PP^1)\subseteq\PP^d,
$$
graded so that $\deg x_i=1$, and write $\theta:k[x_0,\ldots,x_d]\to k[t_0,t_1]$ for the substitution $x_i\mapsto t_0^{d-i}t_1^i$, so that $I(X)=\ker\theta$ and $S(X)=k[t_0^d,t_0^{d-1}t_1,\ldots,t_1^d]$ (I, Ex. 2.12). The degree-$m$ part of $S(X)$ is the image of $H^0(\PP^d,\mco_{\PP^d}(m))$ and is $H^0(\PP^1,\mco_{\PP^1}(md))$.

::: pf

::: {.pf-step #surjective-restriction}

For every $m\ge0$ the restriction map
$$
H^0(\PP^d,\mco_{\PP^d}(m))\longrightarrow H^0(\PP^1,\mco_{\PP^1}(md))
$$
is surjective, and $\dim\bigl(S(X)\bigr)_m=md+1$.

::: pf-proof

This step is the card's own. The identification
$S(X)=k[t_0^d,t_0^{d-1}t_1,\ldots,t_1^d]$ is (I, Ex. 2.12), and is stated at Hou,
§3 Exercise 4(a), printed p. 8; the monomial count is the card's.

The map sends $x_i\mapsto s^{d-i}t^i$ in coordinates $[s:t]$ on $\PP^1$. The
target has basis
$$
s^{md-r}t^r,\qquad 0\le r\le md.
$$
Write $r=qd+a$ with $0\le a<d$. If $q<m$, the monomial is the image of
$x_d^q x_a x_0^{m-q-1}$; if $q=m$, then $a=0$ and it is the image of $x_d^m$. So
every basis monomial is in the image, and the image has dimension $md+1$, which
is $\dim H^0(\PP^1,\mco_{\PP^1}(md))$; hence the image is the whole target.

:::

:::

::: {.pf-step #projective-normality}

$X$ is projectively normal.

::: pf-proof

This step is the card's own.

Projective normality of $X\subseteq\PP^d$ is normality of the affine cone
$V=\Spec S(X)$ over it, and $X\cong\PP^1$ is normal. By step
[](#surjective-restriction){.pf-ref} the restriction map
$$
H^0(\PP^d,\mco_{\PP^d}(m))\longrightarrow
H^0(X,\mco_X(m))=H^0(\PP^1,\mco_{\PP^1}(md))
$$
is surjective for every $m\ge0$. By
[[P-AGH2514PROJNORM|Exercise II.5.14(d)]], normality of $X$ together with the
surjectivity of these restriction maps in every degree is equivalent to
projective normality of $X$. Hence $X$ is projectively normal.

Hou's route to this, §3 Exercise 4(a), printed pp. 8--9, is integral closedness
of $S(X)$, and two statements in it are false. He takes
$\Frac S(X)=k(t_0,t_1)$; but $\Frac S(X)$ consists of the ratios of forms of
$t$-degree divisible by $d$, and for $d\ge2$ that is a proper subfield of
$k(t_0,t_1)$, the element $t_0$ not being such a ratio. He then concludes from
$f^n+a_{n-1}f^{n-1}+\cdots+a_0=0$ that $d\mid\deg f$ for $f\in k[t_0,t_1]$
integral over $S(X)$, and that is false: for $d=2$ the element $t_0$ is integral
over $S(X)=k[t_0^2,t_0t_1,t_1^2]$, being a root of $T^2-t_0^2$, while
$\deg t_0=1$ is not divisible by $2$. Neither statement is used above.

:::

:::

::: {.pf-step #quadrics-vanish}

For $0\le i<j\le d-1$ the quadric
$$
g_{ij}=x_ix_{j+1}-x_{i+1}x_j
$$
vanishes on $X$.

::: pf-proof

Hou, §3 Exercise 4(a), printed p. 9: "obviously $g_{ij}\in\ker(\theta)$". Under
$x_i\mapsto t_0^{d-i}t_1^i$ both $x_ix_{j+1}$ and $x_{i+1}x_j$ map to
$t_0^{2d-i-j-1}t_1^{i+j+1}$.

:::

:::

::: {.pf-step #quadrics-generate}

The $g_{ij}$ generate $I(X)$.

::: pf-proof

This step is the card's own. Hou states it at §3 Exercise 4(a), printed p. 9,
and proves it by division with remainder by the $g_{ij}$ in the lexicographic
order $x_0>x_1>\cdots>x_d$; his first observation about the remainder is false,
since the leading monomial of $g_{i-1,i}=x_{i-1}x_{i+1}-x_i^2$ is
$x_{i-1}x_{i+1}$, so a pure power $x_i^l$ is divisible by no leading monomial and
survives the division.

Let $J$ be the ideal generated by the $g_{ij}$, so that $J\subseteq I(X)$ by
step [](#quadrics-vanish){.pf-ref}, and let $R=k[x_0,\ldots,x_d]$. For a
degree-$m$ monomial $M=x_{i_1}\cdots x_{i_m}$, whenever two of its indices
satisfy $b-a\ge2$ the relation
$$
x_ax_b\equiv x_{a+1}x_{b-1}\pmod J
$$
replaces them by two closer indices while preserving their sum, and the sum of
the squares of the indices strictly decreases; so repeated straightening
terminates. Every degree-$m$ monomial is therefore congruent modulo $J$ to one
whose indices differ by at most $1$. If the sum of its indices is
$r=mq+a$ with $0\le a<m$, that monomial is $x_q^{m-a}x_{q+1}^{a}$, with the
evident reading $x_d^m$ when $r=md$. So $(R/J)_m$ is spanned by the $md+1$
monomials belonging to the index sums $0,\ldots,md$.

Their images in $(S(X))_m$ are the distinct monomials
$$
s^{md-r}t^r,\qquad 0\le r\le md,
$$
which are linearly independent, so those classes are a basis of $(R/J)_m$ and
$\dim (R/J)_m=md+1$. By step [](#surjective-restriction){.pf-ref},
$\dim (R/I_X)_m=\dim(S(X))_m=md+1$ as well, and $J\subseteq I_X$ makes
$(R/J)_m\to(R/I_X)_m$ surjective; equal dimensions force
$(I_X)_m=J_m$ for every $m$, hence $I_X=J$.

:::

:::

::: {.pf-step #hyperplane-divisor}

Let $X\subseteq\PP^n$ be a curve of degree $d$ not contained in any hyperplane,
and let $H$ be a hyperplane with $D=X.H$. Then
$$
\deg D=d,
\qquad
\dim\abs{D}\ge n.
$$

::: pf-proof

This step is the card's own. $\deg D=\deg(X.H)=\deg X=d$. The restriction
$H^0(\PP^n,\mco_{\PP^n}(1))\to H^0(X,\mco_X(1))$ is injective because no nonzero
linear form vanishes on $X$, so the hyperplane divisors cut on $X$ span an
$(n+1)$-dimensional subspace of $H^0(X,\mco_X(1))$ and
$$
\dim\abs{D}=h^0(X,\mco_X(1))-1\ge n.
$$
Hou, §3 Exercise 4(b), printed p. 10, states $\dim\abs{D}=n$ and justifies it by
the remark that otherwise "there exists a proper subspace
$V\subset h^0(X,\mco_X(D))$ such that $X\subset\PP(V^*)\subsetneq\PP^n$";
injectivity of the restriction gives the inequality above and not completeness,
so the equality is not established by that remark and is obtained in the next
step from the degree bound.

:::

:::

::: {.pf-step #strict-inequality}

For a curve of degree $d\le n$ in $\PP^n$ not contained in any hyperplane,
$$
d=n.
$$

::: pf-proof

This step transcribes A. Egbert, *Solutions to Hartshorne's Algebraic Geometry*
(2013), IV.3.4(b), printed p. 220: "We have
$\dim\abs{D}=n$, $\deg(D)=d$ and
$l(D)=n+1\le\deg(D)+1=d+1\le n+1$. Thus $n=d$." With step
[](#hyperplane-divisor){.pf-ref}, $d\le n$ is his last inequality and his
$l(D)\le\deg(D)+1$ is [[P-AGH415DIMLEQDEG|Exercise IV.1.5]] applied to $D$,
which reads $\dim\abs{D}\le\deg D$, with $l(D)=\dim\abs{D}+1$.

The equality he opens with is what the hypotheses give as an inequality:
$H^0(\PP^n,\mco_{\PP^n}(1))\to H^0(X,\mco_X(1))$ is injective because $X$ lies
in no hyperplane (step [](#hyperplane-divisor){.pf-ref}), so $l(D)\ge n+1$.
Read that way his chain is $n+1\le l(D)\le d+1\le n+1$ and yields the same
conclusion; printed with $l(D)=n+1$ first, as he writes it, the line asserts
what it proves. Hou, §3 Exercise 4(b), printed p. 10, writes the same equality
for the same inequality, which step [](#hyperplane-divisor){.pf-ref} names.

Hou's own route to $d=n$, §3 Exercise 4(b), printed p. 10, removes the fixed
points of $\abs{D}$ one at a time, reaching
$\dim\abs{D-P_1-\cdots-P_d}=n-d>0$ against degree $0$; that is a contradiction
only if $\dim\abs{D}=n$, which his remark there does not establish.

:::

:::

::: {.pf-step #genus-zero}

Under the hypotheses of step [](#hyperplane-divisor){.pf-ref},
$$
h^0(X,\mco_X(1))=n+1,
\qquad
g(X)=0.
$$

::: pf-proof

This step transcribes Egbert, IV.3.4(b), printed p. 220, who continues:
"Since $\deg(D)=\dim(D)$, and $d\ne0$, then by exc IV.1.5, $g=0$." Step
[](#strict-inequality){.pf-ref} gives $d=n$ and its chain gives $l(D)=n+1$, so
$\dim\abs{D}=n=\deg D$ with $D\ne0$; that is the equality case of
[[P-AGH415DIMLEQDEG|Exercise IV.1.5]], whence $g(X)=0$, and
$h^0(X,\mco_X(1))=l(D)=n+1$. His "$\deg(D)=\dim(D)$" compares the degree of $D$
with the dimension of the linear system, and what the citation needs is
$\deg D=\dim\abs{D}$, the equality the previous step leaves.

He closes, "Thus $D$ corresponds to an $(n+1)$ dimensional subspace in
$\Gamma(\PP^1,\mco(n))$", which is the identification the next step states, and
Hou, §3 Exercise 4(b), printed p. 10, states both conclusions as well: "we then
must have $g(X)=0$ and $\mco_X(H)=\mco_{\PP^1}(dH)$".

:::

:::

::: {.pf-step #is-rational-normal}

The embedding of step [](#hyperplane-divisor){.pf-ref} is the $d$-uple embedding
of $\PP^1$, up to an automorphism of $\PP^d$.

::: pf-proof

Hou, §3 Exercise 4(b), printed p. 10: "Therefore $X\cong\nu_d(\PP^1)$ up to
$\Aut(\PP^n)$." The following expansion of that sentence is the card's own.
$g(X)=0$ forces $X\cong\PP^1$ (IV.1.3.5); on $\PP^1$ a divisor of degree $d$ is
linearly equivalent to $dP$ for a point $P$, so
$\mco_X(1)=\mco_X(H)\cong\mco_{\PP^1}(d)$ and $\abs{D}$ is the complete system
$\abs{dP}$; by step
[](#genus-zero){.pf-ref} the restriction
$H^0(\PP^d,\mco_{\PP^d}(1))\to H^0(X,\mco_X(1))$ is injective between spaces of
dimension $d+1$, hence an isomorphism, so the given embedding is the one defined
by the complete system $\abs{\mco_{\PP^1}(d)}$ and differs from $\nu_d$ only by
the choice of a basis of that space, that is, by an element of
$\PGL_{d+1}(k)=\Aut\PP^d$.

:::

:::

::: {.pf-step #degree-two}

A curve of degree $2$ in any $\PP^n$ is a conic in some $\PP^2$.

::: pf-proof

Hou, §3 Exercise 4(c), printed p. 10: if $X$ is not contained in any hyperplane,
then $n=2$ by part (b) as proved in steps
[](#hyperplane-divisor){.pf-ref}--[](#is-rational-normal){.pf-ref}; if a
hyperplane $H\cong\PP^{n-1}$ contains $X$, replace $n$ by $n-1$ and repeat. So
$X$ is a plane curve of degree $2$, that is, a conic in $\PP^2$.

:::

:::

::: {.pf-step #degree-three}

A curve of degree $3$ in any $\PP^n$ is either a plane cubic or the twisted
cubic in $\PP^3$.

::: pf-proof

Hou, §3 Exercise 4(d), printed p. 10: the descent of step
[](#degree-two){.pf-ref} shows $X\subseteq\PP^3$. If $X$ is not contained in any
plane, then $X\cong\nu_3(\PP^1)$ by part (b), "and it is indeed the twisted
cubic curve up to a projective transform"; if $X$ lies in a plane, it is a plane
curve of degree $3$, hence a plane cubic. By [[P-AGH212DUPLE|Exercise I.2.12(d)]]
the image of $\nu_3$ is the twisted cubic.

:::

:::

::: pf-qed

Steps [](#surjective-restriction){.pf-ref}, [](#projective-normality){.pf-ref},
[](#quadrics-vanish){.pf-ref} and [](#quadrics-generate){.pf-ref} prove part
(a), steps [](#hyperplane-divisor){.pf-ref}, [](#strict-inequality){.pf-ref},
[](#genus-zero){.pf-ref} and [](#is-rational-normal){.pf-ref} prove part (b), and
steps [](#degree-two){.pf-ref} and [](#degree-three){.pf-ref} prove its two
consequences.

:::

:::

:::


::: {.remark title="Published solution"}
Chin-Lung Wang's Algebraic Geometry II (National Taiwan University, 2020 Spring), Chapter IV homework, §3 Exercise 4 by Yu-Chi Hou, printed pp. 8--10, solves the exercise: (a) at pp. 8--9, by integral closedness of the homogeneous coordinate ring and by division of the ideal by the quadrics $g_{ij}$, and (b) with its degree-$2$ and degree-$3$ consequences at p. 10. Three statements of its part (a) are false and are named where they would otherwise be used: $\Frac S(X)=k(t_0,t_1)$, the conclusion $d\mid\deg f$ drawn from a degree comparison (for $d=2$, $t_0$ is integral over $S(X)$ and has degree $1$), and the claim that a lexicographic remainder by the $g_{ij}$ contains no pure power $x_i^l$, whose leading monomial under $g_{i-1,i}$ is $x_{i-1}x_{i+1}$. Its part (b) states $g(X)=0$ and the identification with the $d$-uple embedding, and states $\dim\abs{D}=n$ without proving it. The card proves (a) by Exercise II.5.14(d) and by straightening monomials modulo the quadrics, and part (b)'s degree and genus from Exercise IV.1.5, with IV.1.3.5, an Example of the text, for $X\cong\PP^1$.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.4, printed pp. 219--220, asserts both halves of part (a) without proof on printed p. 219 — "Since $\PP^1$ is projectively normal, then $d$-uple is projectively normal; If $\theta$ is the corresponding ring homomorphism, then the kernel is generated by quadrics" — and proves part (b) on printed p. 220 by the chain $l(D)=n+1\le\deg(D)+1=d+1\le n+1$ and Exercise IV.1.5, with the identification in the one closing sentence quoted in step [](#genus-zero){.pf-ref}.
:::
