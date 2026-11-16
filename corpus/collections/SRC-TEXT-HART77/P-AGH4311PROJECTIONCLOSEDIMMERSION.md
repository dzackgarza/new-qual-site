---
schema: qual/card@1
id: P-AGH4311PROJECTIONCLOSEDIMMERSION
kind: problem
title: Projection embeds a smooth $r$-fold into $\PP^{n-1}$ when $n>2r+1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Very Ample Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.11 together with the projection/linear-system
    criterion II.7.3 and the Veronese construction II.7.7. Part (a) uses
    separate secant and embedded-tangent-space incidence bounds. Part (b)
    reduces each secant to the plane conic obtained from the corresponding
    line in P^2 and checks the lower dimension bound for the secant variety by
    an explicit four-rank local parametrization, valid in every
    characteristic.
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
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), IV.3.11(a),
    printed p. 309. The closed-embedding criterion the last step invokes is
    stated in R. Vakil, The Rising Sea: Foundations of Algebraic Geometry,
    21 October 2025 version, as Theorem 19.1.1, printed p. 536, text version `tmp/sources/vakil-rising-sea-2025-10-21.md`, with the
    hypotheses "injective on closed points" and "injective on tangent vectors at
    closed points" and no other; he reduces it at 19.1.3, printed p. 537, to
    Theorem 19.1.2 and proves that at 19.1.4, but the reduction's last step is
    Exercise 19.1.D, "Show that the degree of pi is at most 1 at all closed
    points of Y", left to the reader and the only place where the tangent-vector
    hypothesis enters. Step s6 cites Vakil with that limit recorded and rests on
    Hartshorne II.7.3 (T-DIVMAPPN), which is the same statement. What is not in
    Vakil is the existence of the centre:
    the secant and tangent loci are closed of dimension at most 2r+1, so a point O
    outside them exists when n > 2r+1, and that count is the card's own. Egbert's
    entry for (a) is a citation to Shafarevich, and Shafarevich was not consulted.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Named the text version of Vakil's book at the citation of Theorem 19.1.1 in
    the remark on 2026-11-16, where it cited the PDF alone: it is
    tmp/sources/vakil-rising-sea-2025-10-21.md. No page or claim changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Part (a) has a complete published proof, located for this batch, and the
    printed exercise was read with it: Hartshorne, Algebraic Geometry (1977),
    IV Ex. 3.11(a), printed p. 316 -- not printed p. 309, which the event of
    2026-11-15 above gives for it; the exercise stands on PDF p. 331 of the
    text version tmp/sources/hartshorne-1977-algebraic-geometry.md, where
    printed p. N is PDF p. N+15. Read at its cited places in the text version
    tmp/sources/shafarevich-2013-basic-algebraic-geometry-1-pp129-138.md:
    Theorem 2.25 on printed p. 134, the lemma on isomorphic embeddings on
    printed pp. 134-135, Corollary 2.7 on printed p. 135, and the proof of
    Theorem 2.25 on printed pp. 135-136, whose folios were checked against the
    PDF (PDF p. 149 is printed p. 133, so printed p. N is PDF p. N+16 in that
    copy). Checked against the book: Shafarevich's Theorem 2.25 is stated for a
    nonsingular projective n-dimensional variety in P^N with N > 2n+1 and
    concludes an isomorphic embedding into P^{N-1}, which is assertion (a) of
    the exercise with N = n and n = r; the closed immersion follows since a
    projective X has closed image. Not checked: Shafarevich's Theorem 1.15,
    which Corollary 2.7 cites for the finiteness of the projection, and
    Theorem 1.25, which the dimension count cites; the retained copy holds
    printed pp. 129-138 only, so neither statement was read, and the card says
    so at the step that uses 1.15. For (b) the published treatment located is
    Egbert's entry 4.3.21, printed p. 223, which argues the clause for a
    general point of a secant line and not for every point of every secant
    line.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Part (a) is now the transcription of Shafarevich's proof, one step per
    published step, each naming the numbered statement and printed page, with
    his sentences quoted at the steps that carry his argument: steps secants
    and tangent-locus for the two incidence varieties and their dimensions,
    step centre for the choice of the point, step lemma-criterion for the lemma
    on isomorphic embeddings with its Nakayama proof, and step corollary for
    Corollary 2.7 and the conclusion of (a). Part (b) keeps its steps, now
    labelled veronese-conic, infinitely-many-secants, secant-dim-upper,
    secant-dim-lower, secant-dim and closed-immersion-b, and its last step now
    cites step corollary, which is the criterion it uses, instead of the three
    former steps of (a). What left the card with the former steps s1-s6 is the
    card's own secant and tangent dimension count, of which step centre now
    quotes Shafarevich's; the Vakil citation and the paragraph on Exercise
    19.1.D leave the card with them, and so does the remark's statement that
    part (a) has no complete published solution in the retained sets, which
    Shafarevich's Theorem 2.25 answers. Nothing in the problem statement
    changes.
---

::: {.problem}
(a) If $X$ is a nonsingular variety of dimension $r$ in $\PP^n$, and if $n>2r+1$, show that there is a point $O \notin X$, such that the projection from $O$ induces a closed immersion of $X$ into $\PP^{n-1}$.

(b) If $X$ is the Veronese surface in $\PP^5$, which is the 2-uple embedding of $\PP^2$ (I, Ex.
2.13), show that each point of every secant line of $X$ lies on infinitely many secant lines.
Therefore, the secant variety of $X$ has dimension 4, and so in this case there is a projection which gives a closed immersion of $X$ into $\PP^4$ (II, Ex.
7.7).

A theorem of Severi states that the Veronese surface is the only surface in $\PP^5$ for which there is a projection giving a closed immersion into $\PP^4$.
Usually one obtains a finite number of double points with transversal tangent planes.
:::


::: {.solution}

Let $X\subseteq\PP^n$ be nonsingular of dimension $r$.
Part (a) is transcribed from I. R. Shafarevich, *Basic Algebraic Geometry 1*, third edition (2013), §5.4 "Projective Embedding of Nonsingular Varieties", printed pp. 134--136, text version `tmp/sources/shafarevich-2013-basic-algebraic-geometry-1-pp129-138.md`, in which printed p. $N$ is PDF p. $N+16$ of the copy; his $N$ and $n$ are this card's $n$ and $r$, and each step names the numbered statement and printed page it transcribes.
Part (b) is not from that source: its steps say so where they are proved, and the remark at the end of the card records what the published treatments of (b) do.

::: pf

::: {.pf-step #secants}

The union of the secant lines of $X$ is the image $U_1$ of a closed subset $\Gamma\subseteq\PP^n\times X\times X$, and
$$
\dim U_1\le2r+1 .
$$

::: pf-proof

Shafarevich, proof of Theorem 2.25, printed pp. 135--136: "In $\PP^N\times X\times X$ consider the set $\Gamma$ of triples $(a,b,c)$ with $a\in\PP^N$, $b,c\in X$ such that $a,b,c$ are collinear. $\Gamma$ is obviously a closed subset of $\PP^N\times X\times X$. The projections of $\PP^N\times X\times X$ to $\PP^N$ and to $X\times X$ define regular maps $\varphi:\Gamma\to\PP^N$ and $\psi:\Gamma\to X\times X$. Obviously if $y\in X\times X$ with $y=(b,c)$, and $b\ne c$ then $\psi^{-1}(y)$ consists of points $(a,b,c)$ where $a$ is any point of the line through $b$ and $c$. Hence $\dim\psi^{-1}(y)=1$ and it follows by Theorem 1.25 that $\dim\Gamma=2n+1$. By definition $U_1=\varphi(\Gamma)$, and the same theorem gives $\dim U_1\le\dim\Gamma=2n+1$."
With $X$ of dimension $r$ in $\PP^n$, that is $\dim U_1\le2r+1$, and $U_1$ is the union of the secant lines.
The triples with $b=c$ are the extra ones in $\Gamma$: there $a$ ranges over $\PP^N$ and $(b,b)$ over the diagonal copy of $X$, so they form a closed subset of dimension $n+r$, which is at most $2n+1$ and does not raise the bound; the secant locus itself is the image of the triples with $b\ne c$, on which the fibre computation above is made.

:::

:::

::: {.pf-step #tangent-locus}

The union of the embedded projective tangent spaces $T_PX$ of $X$ is the image $U_2$ of a closed subset $\Gamma'\subseteq\PP^n\times X$, and
$$
\dim U_2\le2r .
$$

::: pf-proof

Shafarevich, proof of Theorem 2.25, printed p. 136: "In a similar way, to study the set $U_2$ we consider in $\PP^N\times X$ the set $\Gamma'$ consisting of points $(a,b)$ such that $a\in\Theta_b$. In exactly the same way we have projections $\psi:\Gamma'\to X$ and $\varphi:\Gamma'\to\PP^N$. For $b\in X$ we have $\dim\psi^{-1}(b)=n$ since $X$ is nonsingular, and hence $\dim\Gamma'=2n$, and since $U_2=\varphi(\Gamma')$, also $\dim U_2\le2n$."
Here $\Theta_b$ is the embedded tangent space $T_bX\subseteq\PP^N$, which is a linear subspace of dimension $n$ of the ambient $\PP^N$ when $X$ has dimension $n$ and is nonsingular at $b$; with this card's letters, $\dim T_PX=r$ and the fibre over $P$ has dimension $r$.

:::

:::

::: {.pf-step #centre}

If $n>2r+1$ there is a point $\xi\in\PP^n$ which lies on no secant line of $X$, in no embedded tangent space $T_PX$, and not on $X$.

::: pf-proof

Shafarevich, proof of Theorem 2.25, printed p. 136, concludes: "We see that $\dim U_1\le\dim\Gamma=2n+1$ and $\dim U_2\le2n$; therefore if $N>2n+1$ then $U_1\cup U_2\ne\PP^N$, which was what we wanted."
Steps [](#secants){.pf-ref} and [](#tangent-locus){.pf-ref} identify $U_1$ and $U_2$ and bound their dimensions by $2r+1$ and $2r$; both bounds are strictly below $n$ under the hypothesis $n>2r+1$, and $\dim X=r<n$, so the union $U_1\cup U_2\cup X$ is a proper closed subset of the irreducible $\PP^n$, and its complement is the nonempty open set of admissible centres.

:::

:::

::: {.pf-step #lemma-criterion}

Shafarevich, Lemma, printed p. 134: a finite map $f$ from a variety $X$ is an isomorphic embedding if and only if it is one-to-one and $d_xf$ is an isomorphism of the tangent space $\Theta_x$ for every $x\in X$. The proof, printed pp. 134--135, is a Nakayama argument.

::: pf-proof

The proof is Shafarevich's, printed pp. 134--135, and runs as follows, with its own notation.
"Set $f(X)=Y$ and $\varphi=f^{-1}$. The lemma will be proved if we show that $\varphi$ is a regular map. The assertion is local in nature. For $y\in Y$, let $x\in X$ be such that $f(x)=y$. Write $U$ and $V$ for affine neighbourhoods of $x$ and $y$ with $f(U)=V$ and such that $k[U]$ is integral over $k[V]$, and continue to write $f:U\to V$ for the restriction of $f$. It is enough to prove that $f$ is an isomorphism for suitable choice of $U$ and $V$."

"The second hypothesis of the lemma is that $f^*:\mathfrak m_y/\mathfrak m_y^2\to\mathfrak m_x/\mathfrak m_x^2$ is surjective. In other words, if $\mathfrak m_y=(u_1,\ldots,u_k)$, then the elements $f^*(u_i)+\mathfrak m_x^2$ generate $\mathfrak m_x/\mathfrak m_x^2$. We apply Nakayama's lemma (Proposition A.11) to $\mathfrak m_x$ as an $\mathcal O_x$-module. It then follows from this that $\mathfrak m_x=(f^*(u_1),\ldots,f^*(u_k))$, or in other words
$$
\mathfrak m_x=f^*(\mathfrak m_y)\mathcal O_x. \tag{2.40}
$$"

"We check that $\mathcal O_x$ is a finite module over $f^*(\mathcal O_y)$. Since $k[U]$ is a finite $k[V]$-module, it is enough to prove that each element of $\mathcal O_x$ can be expressed in the form $\xi/f^*(a)$ with $\xi\in k[U]$ and $a\notin\mathfrak m_y$. For this, it is enough to check that for $\alpha\in k[U]$ with $\alpha\notin\mathfrak m_x$ there exists an element $a\in k[V]$ with $a\notin\mathfrak m_y$ such that $f^*(a)=\alpha\beta$ with $\beta\in k[U]$. By Theorem 1.12 the set $f(V(\alpha))$ is closed, and since $f$ is one-to-one, $y\notin f(V(\alpha))$. Hence there exists a function $c\in k[V]$ such that $c=0$ on $f(V(\alpha))$ and $c(y)\ne0$. Then $f^*(c)=0$ on $V(\alpha)$ and $f^*(c)(x)\ne0$. By the Nullstellensatz, $f^*(c)^n=\alpha\beta$ for some $n>0$ and $\beta\in k[U]$. We can set $a=c^n$."

"Now we can apply Nakayama's lemma to $\mathcal O_x$ as a $f^*(\mathcal O_y)$-module. The equality (2.40) shows that $\mathcal O_x/f^*(\mathfrak m_y)\mathcal O_x=\mathcal O_x/\mathfrak m_x=k$, and hence is generated by the single element $1$. It now follows by Nakayama's lemma that $\mathcal O_x=f^*(\mathcal O_y)$."

"Let $u_1,\ldots,u_l$ be a basis of $k[U]$ as a module over $k[V]$. By what we have proved, $u_i\in\mathcal O_x=f^*(\mathcal O_y)$. Write $V'=V\setminus V(h)$ for a principal affine neighbourhood of $y$ such that all $(f^*)^{-1}(u_i)$ are regular in $U'=U\setminus V(f^*(h))$. Then $k[U']=\sum f^*k[V']u_i$. By assumption $u_i\in f^*(k[V'])$, and it follows that $k[U']=k[V']$, which means that $f:U'\to V'$ is an isomorphism. The lemma is proved."

:::

:::

::: {.pf-step #corollary}

Shafarevich, Corollary 2.7, printed p. 135: let $X\subseteq\PP^N$ be a variety and $\xi\in\PP^N\setminus X$; if every line through $\xi$ intersects $X$ in at most one point and $\xi$ is not contained in the tangent space to $X$ at any point, then the projection from $\xi$ is an isomorphic embedding $\overline X\hookrightarrow\PP^{N-1}$. Applied to the point $\xi$ of step [](#centre){.pf-ref} it gives a closed immersion of $X$ into $\PP^{n-1}$, which proves (a).

::: pf-proof

The statement is Corollary 2.7, printed p. 135, and its proof there is one sentence: "It is enough to apply the lemma, together with Theorem 1.15."
By step [](#centre){.pf-ref} the point $\xi$ lies on no secant line of $X$, so every line through $\xi$ meets $X$ in at most one point, and $\xi\notin T_PX$ for every $P\in X$; the two hypotheses of the corollary are therefore met.
The lemma of step [](#lemma-criterion){.pf-ref} needs the projection $X\to\PP^{n-1}$ to be finite, and that is what the cited Theorem 1.15 supplies; the copy at `tmp/sources/shafarevich-2013-basic-algebraic-geometry-1-pp129-138.md` retains printed pp. 129--138 only, so the statement of Theorem 1.15 is not in it and is not quoted here.
The conclusion is that the projection restricts to an isomorphism of $X$ onto its image in $\PP^{n-1}$; that image is closed, because $X$ is projective and a morphism from a projective variety is proper, so the isomorphism onto the image is a closed immersion.
This is assertion (a) of the exercise.

:::

:::
::: {.pf-step #veronese-conic}

Now let
$$
\nu_2:\PP^2\longrightarrow X\subseteq\PP^5
$$
be the quadratic Veronese embedding. Every secant line to $X$ is contained
in the plane of a Veronese conic.

::: pf-proof

Let a secant line join the two distinct points
$$
\nu_2(P),\nu_2(Q),
\qquad
P,Q\in\PP^2.
$$
Let
$$
\ell=\overline{PQ}\subseteq\PP^2.
$$
The restriction
$$
\nu_2\restrict_\ell:\ell\cong\PP^1\longrightarrow\PP^5
$$
is the complete quadratic Veronese embedding of $\PP^1$.
Its image
$$
C=\nu_2(\ell)
$$
is a nonsingular plane conic spanning a plane
$$
\Pi\cong\PP^2.
$$
Both endpoints of the secant lie on $C$, so their joining line lies in
$\Pi$.

:::

:::

::: {.pf-step #infinitely-many-secants}

Every point of every secant line of $X$ lies on infinitely many
secant lines of $X$.

::: pf-proof

Let
$$
O
$$
be a point of the secant line in step [](#veronese-conic){.pf-ref}. Then
$$
O\in\Pi.
$$
Consider the pencil of all lines in $\Pi$ through $O$.

If $O\in C$, every member except the unique tangent line at the smooth point
$O$ meets $C$ in $O$ and one further distinct point.

Suppose $O\notin C$. Projection from $O$ gives a finite morphism
$$
C\longrightarrow\PP^1
$$
of degree $2$, where the target is the pencil of lines through $O$.
The original secant line from step [](#veronese-conic){.pf-ref} is one fibre containing two distinct
points. Hence this degree-two morphism is generically separable: a purely
inseparable degree-two map would be radicial and could not have such a
fibre. Therefore the geometric generic fibre consists of two distinct
points, and the same holds over a nonempty open subset of the pencil.

In either case infinitely many lines through $O$ are secants of the conic
$C$. Since
$$
C\subseteq X,
$$
they are also secant lines of the Veronese surface $X$.

:::

:::

::: {.pf-step #secant-dim-upper}

The secant variety of the Veronese surface has dimension at most $4$.

::: pf-proof

Let
$$
\mathcal J
=
\{(P,Q,O):
P,Q\in X,\ P\ne Q,\ O\in\overline{PQ}\}.
$$
Since
$$
\dim X=2,
$$
one has
$$
\dim\mathcal J=2+2+1=5.
$$
Its image in $\PP^5$ is dense in the secant variety
$$
\operatorname{Sec}(X).
$$

By step [](#infinitely-many-secants){.pf-ref}, every point of this image lies on infinitely many secant lines.
Thus every fibre of
$$
\mathcal J\longrightarrow\operatorname{Sec}(X)
$$
over a point of the dense image has infinitely many closed points.
A zero-dimensional finite-type scheme over an algebraically closed field has
only finitely many closed points, so these fibres have dimension at least
$1$.
The fibre-dimension inequality therefore gives
$$
\dim\operatorname{Sec}(X)
\le
5-1
=4.
$$

:::

:::

::: {.pf-step #secant-dim-lower}

The secant variety has dimension at least $4$.

::: pf-proof

Use the standard coordinates
$$
\nu_2([x:y:z])
=
[x^2:y^2:z^2:xy:xz:yz].
$$
Near
$$
P_0=[1:0:0],
\qquad
Q_0=[0:1:0],
$$
write
$$
P(a,b)=[1:a:b],
\qquad
Q(c,d)=[c:1:d].
$$
Restrict to the four-parameter family with $c=0$ and consider
$$
\Psi(a,b,d,t)
=
[\nu_2(P(a,b))+t\,\nu_2(Q(0,d))].
$$
On the target chart where the $x^2$-coordinate is nonzero, normalize that
coordinate to $1$. The image coordinates are then
$$
\begin{aligned}
A&=a^2+t,\\
B&=b^2+td^2,\\
C&=a,\\
D&=b,\\
E&=ab+td.
\end{aligned}
$$
On the open subset
$$
t\ne0,
$$
these equations recover the four parameters rationally:
$$
a=C,
\qquad
b=D,
\qquad
t=A-C^2,
\qquad
d=\frac{E-CD}{A-C^2}.
$$
Thus $\Psi$ is generically one-to-one onto its image on this four-dimensional
open set. Its image therefore has dimension $4$.
Since that image is contained in the secant variety,
$$
\dim\operatorname{Sec}(X)\ge4.
$$

:::

:::

::: {.pf-step #secant-dim}

The secant variety of the Veronese surface has dimension exactly
$$
\boxed{4}.
$$

::: pf-proof

Steps [](#secant-dim-upper){.pf-ref} and [](#secant-dim-lower){.pf-ref} give the opposite inequalities
$$
\dim\operatorname{Sec}(X)\le4
\qquad\text{and}\qquad
\dim\operatorname{Sec}(X)\ge4.
$$
Therefore equality holds.

:::

:::

::: {.pf-step #closed-immersion-b}

There is a projection
$$
X\hookrightarrow\PP^4
$$
which is a closed immersion.

::: pf-proof

By step [](#secant-dim){.pf-ref},
$$
\operatorname{Sec}(X)
\subsetneq
\PP^5.
$$
Choose
$$
O\in\PP^5\setminus\operatorname{Sec}(X).
$$
The closure of the secant variety contains the embedded tangent spaces of
the smooth surface $X$: every tangent direction is a limit of secant
directions, and the projective tangent plane is the union of its tangent
lines through the point.
Thus $O$ lies on neither a secant line nor an embedded tangent plane of $X$.

The criterion of step [](#corollary){.pf-ref} needs exactly that $O$ lie on no secant line and in no embedded tangent space, and both hold here; since $X$ is projective, projection from $O$ is therefore a closed immersion
$$
\boxed{X\hookrightarrow\PP^4}.
$$
This is the projection asserted in (b).

:::

:::

::: pf-qed

Steps [](#secants){.pf-ref}, [](#tangent-locus){.pf-ref}, [](#centre){.pf-ref}, [](#lemma-criterion){.pf-ref} and [](#corollary){.pf-ref} prove (a): a point outside the secant locus, the tangent locus and $X$ exists when $n>2r+1$, and projection from it is a closed immersion.
Steps [](#veronese-conic){.pf-ref} and [](#infinitely-many-secants){.pf-ref} prove that each point of every secant line of the Veronese surface lies on infinitely many secant lines, steps [](#secant-dim-upper){.pf-ref}, [](#secant-dim-lower){.pf-ref} and [](#secant-dim){.pf-ref} compute the dimension of its secant variety, and step [](#closed-immersion-b){.pf-ref} gives the closed immersion into $\PP^4$ that (b) asks for.

:::

:::

:::

::: {.remark title="Published solution"}
Part (a) is I. R. Shafarevich, *Basic Algebraic Geometry 1*, third edition (2013), §5.4, printed pp. 134--136: Theorem 2.25, printed p. 134, is the statement, the lemma on isomorphic embeddings and Corollary 2.7 on the projection are printed on pp. 134--135, and the dimension count that produces the centre is on pp. 135--136.
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.11, printed p. 223, text version `tmp/sources/hartshorne-solutions-egbert.md`, gives (a) in entry 4.3.20 as "This is Shafarevich Algebraic Geometry 1, theorem 9, page 136", which is the numbering of an earlier edition of Shafarevich; in the 2013 edition the theorem is 2.25, its statement is on printed p. 134 and the proof that supplies the centre runs to printed p. 136.

His entry 4.3.21, printed p. 223, argues (b) for a general point of a secant line: "If $r\in\PP^5$ is a general point on a secant line $\overline{v(P)v(Q)}$ of $X$, then $\overline{pq}$ maps to a conic $C$ in $X$ and $r$ then lies on the plane spanned by $C$. Any other line on the plane passing through $r$ is also a secant line to $C$ and thus to $X$. Thus a general point on a secant line to $X$ lies on a one-dimensional family of secant lines to $X$. Since we are in $\PP^5$ at any rate, then the secant variety has dimension at most $4$. On the other hand, the secant variety clearly has dimension at least $4$."
That is the clause for a general point of a secant line; the exercise asks it for every point of every secant line, and for those points the conic of the plane through the point is the one the argument above uses.
:::
