---
schema: qual/card@1
id: P-AGH2315GEOMIRRED
kind: problem
title: Geometric irreducibility, reducedness, and integrality after base change
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Irreducibility
  - Reduced Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.15 statement and the standard separable-closure/perfect-closure tests for geometric irreducibility and reducedness.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the Stacks Project Lemma 33.8.9 (tag 038I) and Lemma 33.6.4 (tag
    035X) in full: the first lists geometric irreducibility, irreducibility
    after every finite separable extension, and irreducibility of X over a
    separable algebraic closure as equivalent; the second lists geometric
    reducedness, reducedness after every field extension, after every finite
    purely inseparable extension, after k^{1/p}, after k^{perf} and after
    the algebraic closure. Those are exactly the three conditions of each
    part with k_s and k_p in place. Rechecked the card's own steps: the
    purely inseparable base change being a homeomorphism, Lemma 10.47.2 for
    the minimal prime over an algebraically closed field, and injectivity of
    A tensor k_p to A tensor kbar.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Tag correction, on a reader's report of issue #121: Lemma 33.6.4 is tag
    035X, not 035U; 035U is Section 33.6 (Geometrically reduced schemes) and
    035X is its Lemma 33.6.4. Corrected here and in the remark, and the
    remark now also lists the lemma's item (7) instead of implying that its
    list stops at the closures. The reason for the citation is unchanged:
    items (2), (5) and (6) of 035X are the three conditions of part (b), and
    the proof was read in tmp/sources/stacks-tags/035X.md.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Both parts are now the Stacks Project's proof transcribed rather than
    cited: step affine-irreducibility-tfae is Algebra Lemma 10.47.3 (tag
    037K, printed pp. 544--545), steps xbark-irred-implies-xk-irred and
    xks-irred-implies-xbark-irred are the proof of Lemma 33.8.9 (tag 038I,
    printed pp. 2832--2833), step affine-reducedness-tfae is the first two
    paragraphs of the proof of Lemma 33.6.4 (tag 035X, printed p. 2821), and
    step purely-inseparable-reducedness-tests is Algebra Lemma 10.44.4
    (tag 030V, printed pp. 537--538). Pages are those of the retained
    compiled book tmp/sources/stacks-project-book.pdf, whose PDF page is its
    printed page; each page was read in that PDF. Read against the book:
    Hartshorne II Ex. 3.15 on printed p. 93 asks exactly the three closures
    and the perfect closure that 038I and 035X list, and its X is of finite
    type over k, which no step uses beyond the definitions. Not checked:
    the examples in part (c), which are the card's own and not in the
    source; and Algebra Lemma 10.44.4's own cited lemmas 10.43.4, 10.42.4,
    10.43.6, 10.43.7 and 10.44.2 were read as statements at the pages given,
    not transcribed.
---

::: {.problem}
Let $X$ be a scheme of finite type over a field $k$, not necessarily algebraically closed.
Here $\fiberprod{X}{k}{K}$ abbreviates $\fiberprod{X}{\Spec k}{\Spec K}$.

(a) Show that the following three conditions are equivalent, in which case we say that $X$ is **geometrically irreducible**:

    - $\fiberprod{X}{k}{\bar{k}}$ is irreducible, where $\bar{k}$ denotes the algebraic closure of $k$;
    - $\fiberprod{X}{k}{k_s}$ is irreducible, where $k_s$ denotes the separable closure of $k$;
    - $\fiberprod{X}{k}{K}$ is irreducible for every extension field $K$ of $k$.

(b) Show that the following three conditions are equivalent, in which case we say $X$ is **geometrically reduced**:

    - $\fiberprod{X}{k}{\bar{k}}$ is reduced;
    - $\fiberprod{X}{k}{k_p}$ is reduced, where $k_p$ denotes the perfect closure of $k$;
    - $\fiberprod{X}{k}{K}$ is reduced for all extension fields $K$ of $k$.

(c) We say that $X$ is **geometrically integral** if $\fiberprod{X}{k}{\bar{k}}$ is integral.
Give examples of integral schemes which are neither geometrically irreducible nor geometrically reduced.
:::

::: {.solution}
The proof is the Stacks Project's, transcribed step by step below with the
printed page of the retained compiled book
(`tmp/sources/stacks-project-book.pdf`, 7655 pages, whose PDF page is its
printed page). The two lemmas that carry the two parts are
Lemma 33.8.9 (tag 038I, printed pp. 2832--2833), whose item (1) is
irreducibility after every field extension, and Lemma 33.6.4 (tag 035X,
printed pp. 2821--2822, in Section 33.6, tag 035U). They rest on
Algebra, Lemma 10.47.3 (tag 037K, printed pp. 544--545) and Algebra,
Lemma 10.44.4 (tag 030V, printed pp. 537--538) for the affine charts.

Three facts of the same work are used below in the form in which the source
uses them.

1. A nonzero ring with at most one minimal prime has irreducible spectrum:
   the nilradical is then the unique minimal prime, hence prime, and its
   vanishing locus is the whole spectrum.

2. Algebra, Lemma 10.46.7 (tag 0BRA, printed p. 541): if $\varphi:R\to S$ is
   a ring map with locally nilpotent kernel, generated as an $R$-algebra by
   elements $x$ with $x^{p^n}\in\varphi(R)$ and $p^nx\in\varphi(R)$ for some
   $n>0$ and some prime $p$, then $\varphi$ induces a homeomorphism of
   spectra, and every base change of $\varphi$ satisfies the same
   hypotheses. In particular $R\to k'\otimes_kR$ induces a homeomorphism of
   spectra for an algebraic purely inseparable field extension $k'/k$.

3. Lemma 33.8.8 (tag 038H, printed p. 2832): for a separably algebraically
   closed field $k$, a field extension $k'/k$ and a $k$-scheme $X$, the
   morphism $X_{k'}\to X$ induces a bijection of irreducible components.

::: pf

::: {.pf-step #affine-irreducibility-tfae}
Let $R$ be a $k$-algebra. The following are equivalent:

1. $\Spec(R\otimes_kK)$ is irreducible for every field extension $K/k$;
2. $\Spec(R\otimes_kk')$ is irreducible for every finite separable field extension $k'/k$;
3. $\Spec(R\otimes_kk_s)$ is irreducible;
4. $\Spec(R\otimes_k\bar k)$ is irreducible.

::: pf-proof
This is Algebra, Lemma 10.47.3 (tag 037K), printed pp. 544--545, and the
proof below is its proof.

$(1)\Rightarrow(2)$ is clear.

$(2)\Rightarrow(3)$: let $\mathfrak q_1,\mathfrak q_2\subseteq R\otimes_kk_s$
be minimal prime ideals, and write $k_s=\bigcup k'$ over the finite
subextensions $k'/k$, each of which is separable. For such $k'$ the ring map
$R\otimes_kk'\to R\otimes_kk_s$ is flat, so by going down for flat ring maps
(Algebra, Lemma 10.39.19, printed p. 525) the contractions
$\mathfrak p_i=(R\otimes_kk')\cap\mathfrak q_i$ are minimal primes of
$R\otimes_kk'$, and $(2)$ gives $\mathfrak p_1=\mathfrak p_2$. Since $k_s$ is
the union of the $k'$, it follows that $\mathfrak q_1=\mathfrak q_2$, so
$\Spec(R\otimes_kk_s)$ has one minimal prime and is irreducible by fact 1.

$(3)\Rightarrow(4)$: $\bar k/k_s$ is algebraic and purely inseparable, so by
fact 2 the ring map
$R\otimes_kk_s\to R\otimes_k\bar k=R\otimes_{k_s}\bar k$ induces a
homeomorphism of spectra, and irreducibility passes across it.

$(4)\Rightarrow(1)$: let $K/k$ be a field extension and choose a field $F$
containing both $K$ and $\bar k$ over $k$. Then
$$
R\otimes_kF=(R\otimes_k\bar k)\otimes_{\bar k}F,
$$
and $\bar k$ is separably closed, so by Algebra, Lemma 10.47.2 (tag 00I7,
printed p. 544) the tensor product of two $\bar k$-algebras with a unique
minimal prime has a unique minimal prime; by $(4)$ the ring $R\otimes_kF$ has
one minimal prime, hence irreducible spectrum. Finally
$R\otimes_kK\to R\otimes_kF$ is flat and injective, so every minimal prime of
$R\otimes_kK$ is the image of a minimal prime of $R\otimes_kF$ (Algebra,
Lemma 10.30.5 with going down), and $R\otimes_kK$ has one minimal prime too.
:::

:::

::: {.pf-step #xbark-irred-implies-xk-irred}
If $X_{\bar k}$ is irreducible, then $X_K$ is irreducible for every field
extension $K/k$.

::: pf-proof
This is the proof of $(3)\Rightarrow(1)$ in Lemma 33.8.9 (tag 038I), printed
p. 2832.

Let $K/k$ be a field extension. Choose a field $\bar k'$ containing $\bar k$
such that $K$ embeds in $\bar k'$ over $k$. The field $\bar k$ is separably
algebraically closed, so by fact 3 the morphism
$X_{\bar k'}\to X_{\bar k}$ induces a bijection of irreducible components, and
$X_{\bar k'}$ is irreducible.

The projection $X_{\bar k'}\to X_K$ is surjective, being the base change of
the surjective morphism $\Spec\bar k'\to\Spec K$, and the image of an
irreducible space is irreducible. Hence $X_K$ is irreducible.
:::

:::

::: {.pf-step #xks-irred-implies-xbark-irred}
If $X_{k_s}$ is irreducible, then $X_{\bar k}$ is irreducible.

::: pf-proof
The extension $\bar k/k_s$ is algebraic and purely inseparable. On an affine
open $U=\Spec R\subseteq X$ the ring map $R\otimes_kk_s\to R\otimes_k\bar k$
is of the form covered by fact 2, so
$\Spec(R\otimes_k\bar k)\to\Spec(R\otimes_kk_s)$ is a homeomorphism; these
homeomorphisms glue over an affine cover, so $X_{\bar k}\to X_{k_s}$ is a
homeomorphism.

A homeomorphism induces a bijection on irreducible closed subsets, so
$X_{k_s}$ irreducible forces $X_{\bar k}$ irreducible.
:::

:::

::: {.pf-step #irreducibility-tfae}
The three conditions of part (a) are equivalent.

::: pf-proof
If $X_{\bar k}$ is irreducible, then $X_K$ is irreducible for every $K$ by
step [](#xbark-irred-implies-xk-irred){.pf-ref}, and $X_{k_s}$ is irreducible
because $X_{\bar k}\to X_{k_s}$ is surjective, being a base change of the
surjective morphism $\Spec\bar k\to\Spec k_s$.

Conversely, $X_{k_s}$ irreducible gives $X_{\bar k}$ irreducible by step
[](#xks-irred-implies-xbark-irred){.pf-ref}, and irreducibility of $X_K$ for
every $K$ gives it for $K=\bar k$. This proves part (a).

The affine statement behind these reductions, and the only place where the
finite separable extensions occur, is step
[](#affine-irreducibility-tfae){.pf-ref}.
:::

:::

::: {.pf-step #affine-reducedness-tfae}
Let $X$ be a scheme over $k$. Then $X_K$ is reduced for every field extension
$K/k$ if and only if for every affine open $U\subseteq X$ the ring $\OO_X(U)$
is geometrically reduced over $k$.

::: pf-proof
This is the first two paragraphs of the proof of Lemma 33.6.4 (tag 035X),
printed p. 2821.

Assume $X_K$ is reduced for every $K$; the source states this as its
condition (1), that $X$ is geometrically reduced, which for it means that
for every $K$ and every point $x'\in X_K$ the local ring of $X_K$ at $x'$ is
reduced, an equivalent form since reducedness of a scheme is reducedness of
all its local rings.

Now let $U\subseteq X$ be affine open. Since $X_K$ is reduced, its open
subscheme $U_K=\Spec(\OO_X(U)\otimes_kK)$ is reduced, hence the ring
$\OO_X(U)\otimes_kK$ is reduced, a scheme affine over a field being reduced
exactly when its ring is (Properties, Section 28.3, tag 01OJ). So
$\OO_X(U)$ is geometrically reduced.

Conversely, if every $\OO_X(U)$ is geometrically reduced, then for any $K$
the scheme $X_K$ is obtained by gluing the spectra of the rings
$\OO_X(U)\otimes_kK$ over an affine cover (Schemes, Section 26.17), each of
them reduced, so $X_K$ is reduced.
:::

:::

::: {.pf-step #purely-inseparable-reducedness-tests}
Let $S$ be a $k$-algebra, and let $k_p=k^{perf}$ be the perfect closure of
$k$. The following are equivalent:

1. $k'\otimes_kS$ is reduced for every finite purely inseparable extension $k'/k$;
2. $k^{1/p}\otimes_kS$ is reduced;
3. $k_p\otimes_kS$ is reduced;
4. $\bar k\otimes_kS$ is reduced;
5. $S$ is geometrically reduced over $k$, that is $K\otimes_kS$ is reduced for every field extension $K/k$.

::: pf-proof
This is Algebra, Lemma 10.44.4 (tag 030V), printed pp. 537--538, and the
proof below is its proof. When $k$ has characteristic zero every field
extension of $k$ is separable and the assertion is Algebra, Lemma 10.43.6
(tag 030U, printed p. 534).

Every finite purely inseparable extension $k'/k$ embeds in $k_p$, and
$k^{1/p}\subseteq k_p\subseteq\bar k$. The implications
$(5)\Rightarrow(4)\Rightarrow(3)\Rightarrow(2)$ and $(3)\Rightarrow(1)$ are
therefore immediate: a reduced ring stays reduced after a base change to a
larger field containing the last one as a subfield.

$(1)\Rightarrow(5)$: let $K/k$ be a field extension; $K\otimes_kS$ is to be
reduced. By Algebra, Lemma 10.43.4 (printed p. 534) it suffices to treat
finitely generated $K$, and then Algebra, Lemma 10.42.4 (printed p. 532)
provides a diagram $k\subseteq k'\subseteq K'$, $K\subseteq K'$ with $k'/k$
and $K'/K$ finite purely inseparable and $K'/k'$ separably generated. By
$(1)$ the ring $k'\otimes_kS$ is reduced, so by Algebra, Lemma 10.43.6 the
ring
$$
K'\otimes_kS=K'\otimes_{k'}(k'\otimes_kS)
$$
is reduced, being a separably generated base extension of a reduced algebra
over $k'$. The ring $K\otimes_kS$ is a subring of it, so it is reduced.

$(2)\Rightarrow(5)$: assume $k^{1/p}\otimes_kS$ is reduced. Then $S$ is
reduced, since $S$ embeds in $k^{1/p}\otimes_kS$. For a minimal prime
$\mathfrak p$ of $S$ the ring $k^{1/p}\otimes_kS_{\mathfrak p}$ is a
localization of $k^{1/p}\otimes_kS$, hence reduced, and
$S_{\mathfrak p}$ is a field (Algebra, Lemma 10.25.1), hence geometrically
reduced by Algebra, Lemma 10.44.2 (printed p. 536), which identifies
geometric reducedness of a field extension with separability. Then $S$ is
geometrically reduced by Algebra, Lemma 10.43.7 (printed p. 535), since a
reduced algebra all of whose localizations at minimal primes are
geometrically reduced is geometrically reduced.
:::

:::

::: {.pf-step #reducedness-tfae}
The three conditions of part (b) are equivalent.

::: pf-proof
Step [](#affine-reducedness-tfae){.pf-ref} identifies reducedness of $X_K$ for
all $K$ with geometric reducedness of the rings $\OO_X(U)$ on affine opens,
and step [](#purely-inseparable-reducedness-tests){.pf-ref} gives, for each
such ring $S$, the equivalence of the four base-change tests with geometric
reducedness of $S$.

It remains to pass from the rings to the scheme. If $X_{\bar k}$ is reduced
then each $\OO_X(U)\otimes_k\bar k$ is reduced, so each $\OO_X(U)$ is
geometrically reduced by the equivalence of the previous step, and then
$X_K$ is reduced for every $K$ by step
[](#affine-reducedness-tfae){.pf-ref}. Conversely if $X_{k_p}$ is reduced then
each $\OO_X(U)\otimes_kk_p$ is reduced, so each $\OO_X(U)$ is geometrically
reduced, and again every $X_K$ is reduced, in particular $X_{\bar k}$. This
proves part (b).
:::

:::

::: {.pf-step #integral-not-geom-irreducible}
An integral scheme need not be geometrically irreducible.

::: pf-proof
Take
$$
k=\RR,
\qquad
X=\Spec\CC
$$
with its natural structure as an $\RR$-scheme.  Since $\CC$ is a field, $X$ is integral.

After base change to $\CC$,
$$
\CC\otimes_{\RR}\CC
\cong
\CC\times\CC.
$$
Thus
$$
X_\CC
\cong
\Spec\CC\amalg\Spec\CC
$$
is reducible.  Hence $X$ is not geometrically irreducible.
:::

:::

::: {.pf-step #integral-not-geom-reduced}
An integral scheme need not be geometrically reduced.

::: pf-proof
Let
$$
k=\FF_p(u)
$$
and set
$$
X=\Spec k[x]/(x^p-u).
$$
The element $u$ is not a $p$th power in $k$: its valuation at the prime $u$ is $1$, whereas a $p$th power has valuation divisible by $p$.  Hence
$$
x^p-u
$$
is irreducible over $k$, so the quotient is a field and $X$ is integral.

After adjoining $u^{1/p}$,
$$
x^p-u=(x-u^{1/p})^p.
$$
Therefore
$$
X_{k(u^{1/p})}
\cong
\Spec k(u^{1/p})[x]/(x-u^{1/p})^p
$$
is nonreduced.  Thus $X$ is not geometrically reduced.
:::

:::

::: {.pf-step #integral-neither-example}
There are integral schemes which are simultaneously neither geometrically irreducible nor geometrically reduced.

::: pf-proof
Let
$$
k=\FF_p(u,v),
$$
and let $w$ satisfy the Artin--Schreier equation
$$
w^p-w=v.
$$
This polynomial is separable because its derivative is $-1$.  It has no root in $k$: using the valuation at infinity in the variable $v$, normalized by
$$
\operatorname{ord}_\infty(v)=-1,
$$
one has
$$
\operatorname{ord}_\infty(r^p-r)
$$
either nonnegative, or a negative integer divisible by $p$, and therefore never $-1$.  An Artin--Schreier polynomial $T^p-T-v$ with no root is irreducible.  Thus
$$
L=k(w)
$$
is a finite separable extension of degree $p$.

Now put
$$
E=L(u^{1/p}),
\qquad
X=\Spec E.
$$
The element $u^{1/p}$ cannot lie in $L$: otherwise the nontrivial purely inseparable extension
$$
k(u^{1/p})/k
$$
would be a subextension of the separable extension $L/k$.  Hence
$$
[E:L]=p.
$$
Hence $E$ is a field and $X$ is integral.

Over an algebraic closure $\bar k$, the separable extension $L/k$ splits into $p$ distinct embeddings, while the purely inseparable equation becomes a $p$th power.  Consequently
$$
E\otimes_k\bar k
\cong
\prod_{j=1}^{p}
\bar k[\epsilon]/(\epsilon^p).
$$
This ring has more than one minimal prime and has nonzero nilpotents.  Therefore $X_{\bar k}$ is both reducible and nonreduced, so $X$ is neither geometrically irreducible nor geometrically reduced.
:::

:::

::: pf-qed
Step [](#irreducibility-tfae){.pf-ref} proves part (a), step [](#reducedness-tfae){.pf-ref} proves part (b), and steps [](#integral-not-geom-irreducible){.pf-ref}, [](#integral-not-geom-reduced){.pf-ref} and [](#integral-neither-example){.pf-ref} give the examples requested in part (c).
:::

:::

:::

::: {.remark}
Irreducibility of $X_K$ is weaker than reducedness, or domain-ness, of the corresponding ring.  Let $k$ be algebraically closed of characteristic $p>0$ and let
$$
A=k[x,y]/(y^p-x^p-x).
$$
Because $k$ is perfect, $k(x)^p=k(x^p)$, and $x^p+x\notin k(x^p)$ by comparing degrees in $x$; hence $y^p-x^p-x\in k(x)[y]$ is irreducible and $A$ is a domain.  Put $K=\Frac(A)=k(s)$ with $s^p=x^p+x$.  In $K[x,y]$ one has $y^p-x^p-x=(y-s)^p$, so
$$
A\otimes_k K\cong K[x,y]/((y-s)^p),
$$
in which $y-s$ is a nonzero nilpotent.  So a domain of finite type over an algebraically closed field can acquire nilpotents after a field extension, and irreducibility of $A\otimes_k K$ can be neither proved nor refuted by asking whether that ring is a domain.  What does survive is the number of minimal primes of $A\otimes_k K$, which is one here.
:::

::: {.remark title="Published solution"}
Both parts are proved in full in the Stacks Project, with the same closures that Hartshorne's list uses, and the two parts of the solution above are that proof transcribed. Part (a) is Lemma 33.8.9 (tag 038I, printed pp. 2832--2833), whose three items are "$X$ is geometrically irreducible over $k$", where geometric irreducibility is irreducibility after every field extension by definition, "$X_{k'}$ is irreducible for every finite separable field extension $k'/k$" and "$X_{\bar k}$ is irreducible, where $k\subset\bar k$ is a separable algebraic closure of $k$"; these are Hartshorne's three conditions. The proof there is the two steps `xbark-irred-implies-xk-irred` and `xks-irred-implies-xbark-irred`, and the affine statement it rests on is Algebra, Lemma 10.47.3 (tag 037K, printed pp. 544--545), carried out in step `affine-irreducibility-tfae`. Part (b) is Lemma 33.6.4 (tag 035X, in Section 33.6, which is tag 035U, printed pp. 2821--2822), which lists as equivalent: $X$ geometrically reduced; $X_{k'}$ reduced for every field extension $k'/k$; $X_{k'}$ reduced for every finite purely inseparable $k'/k$; $X_{k^{1/p}}$ reduced; $X_{k^{perf}}$ reduced; $X_{\bar k}$ reduced; and, as its item (7), geometric reducedness of the rings $\OO_X(U)$ on the affine opens $U$. The $k_p$ of the exercise is $k^{perf}$, so items (2), (5) and (6) are exactly the three conditions of part (b). The equivalence of those conditions is Algebra, Lemma 10.44.4 (tag 030V, printed pp. 537--538), transcribed in step `purely-inseparable-reducedness-tests`, and the passage from the rings on affine opens to the scheme is step `affine-reducedness-tfae`.

What the two steps do not get from the source is part (c). The three examples are the card's own: $\Spec\CC$ over $\RR$, $\Spec\FF_p(u)[x]/(x^p-u)$ over $\FF_p(u)$, and $\Spec E$ with $E=L(u^{1/p})$ over $\FF_p(u,v)$ for an Artin--Schreier extension $L=k(w)$, none of which the Stacks Project states.

Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §3, Exercise 3.15, PDF pp. 26--27, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: for (a) Kim reduces a reducible $X_K$ to an affine chart with $A\otimes_kK$ reducible, extracts non-nilpotent $f_1,f_2$ with $f_1f_2=0$, and then asserts that the resulting finitely many polynomial conditions, which have a solution over the algebraically closed field $K$, have one over a finite extension of $k$; a finite purely inseparable base change of a separably closed $k$ is a homeomorphism, which would finish the argument.
That descent is asserted rather than proved, and it fails on the natural reading: a purely inseparable extension of a separably closed but non-perfect $k$ need not have a $k$-point, so a solution over $K$ does not specialize to one over $k$.
The proof above replaces it by the cited Lemma 10.47.3 and keeps Kim's two reductions, that purely inseparable base change is a homeomorphism and that extension of scalars over an algebraically closed field preserves the set of minimal primes.
Agree on the reduction, not on the descent step.  For (b) Kim uses the trace form of a Galois extension; the proof above uses the cited Lemma 10.43.6 over the perfect closure.
:::
