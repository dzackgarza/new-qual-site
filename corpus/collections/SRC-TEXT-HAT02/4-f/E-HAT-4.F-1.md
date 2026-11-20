---
schema: qual/card@1
id: E-HAT-4.F-1
kind: problem
title: "Direct limit axiom vs. wedge sum axiom"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.F, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §4.F Exercise 1, printed p. 455, both halves matching the printed text. The collection's provenance is the book, and no retained solution set covers the exercise; the argument is the card's own beyond the two results it cites from the book: that axioms (1) and (2) give the wedge sum axiom for finite wedges (p. 160), and the definition of the direct limit axiom over finite subcomplexes (p. 455). Checked: a finite subcomplex of a wedge lies in a finite subwedge; filtered colimits commute with fixed direct sums; the telescope is homotopy equivalent to $X$; $1-s_*$ is injective on the direct sum by the first-nonzero-coordinate argument; and exactness identifies $\widetilde h_n(T)$ with the colimit.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 464 carries the running head 455, so
    the printed page is the one the card's earlier event claimed. The durable part of the locator is
    that printed page; the file path names this machine's copy and `tmp/sources` does not survive a VM
    reset. No mathematics changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, §4.F Exercise 1, the axioms for a reduced homology theory in §4.F, the
    direct limit axiom as that section states it (over the finite subcomplexes), the wedge-sum
    splitting for two summands from the axioms for homology in §2.3, and Mayer--Vietoris as a
    consequence of the exactness axiom. The mathematics is right in both directions. Two repairs.
    The step concluding $\widetilde h_n(T)\cong\operatorname{coker}(1-s_*)$ used the injectivity of
    $1-s_*$ without saying in which degree: the connecting map out of $\widetilde h_n(T)$ is
    followed by $1-s_*$ on $\bigoplus\widetilde h_{n-1}(X_i)$, so it vanishes only because that map
    is injective, and the step now says so and derives the surjectivity onto
    $\widetilde h_n(T)$. And the colimit in the second direction was over one exhaustion, while the
    axiom asks for the direct limit over all finite subcomplexes; the step now identifies the two,
    every finite subcomplex lying in some member of a countable exhaustion. The text cited pages for
    Hatcher's two remarks and for the direct limit axiom; by the owner's correction of this date it
    cites §2.3 and §4.F and no page. No statement changed. Not checked: no certificate; the
    Mayer--Vietoris decomposition of the telescope is a citation of the standard argument and was
    not rebuilt from the axioms in this pass.

- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    The Mayer--Vietoris step the previous pass left as a citation is now written out from Hatcher's
    numbered statements, and one index slip is repaired. The step named the sequence with
    $1-s_*$ and gave the cover in one sentence without identifying the two subcomplexes, their
    intersection or the maps. It is now three steps: a Mayer--Vietoris lemma derived from axioms
    (1) and (2) (the ladder of the pairs $(X,A)$ and $(B,A\cap B)$ with $X/A=B/(A\cap B)$ and the
    algebraic lemma of §2.2 Exercise 38, which is how §2.3 derives the sequence);
    the even/odd cylinder decomposition with the proof that the two subcomplexes cover $T$, that
    each is the one-point union of the mapping cylinders of its parity and so has the homology of the
    wedge of the corresponding $X_i$ by axioms (1) and (3), and that the intersection is the
    one-point union of the copies of the $X_i$ at the shared levels — this is Hatcher's own
    decomposition in the proof of Theorem 3F.8, in the reduced form stated there; and the resulting
    exact sequence with the map $\varphi(g)_i=(-1)^{i-1}(g_i-\rho(g_{i+1}))$ that Hatcher writes in
    that proof, reduced to $1-s_*$ by the sign change he describes, with $\partial$ identified as the
    boundary of the pair $(T,T_1)$. The injectivity step now takes the shift to act by
    $(s_*g)_i=\rho(g_{i+1})$, matching that formula, and reads off the largest index of the support
    rather than the least; with the opposite convention the same step would need the largest index,
    so the old sentence was wrong in its index while its conclusion was not. The telescope step now
    says why a countable CW complex has a finite-subcomplex exhaustion (closure finiteness) and
    cites Lemma 2.34 and Theorem 3F.8 for the deformation retraction instead of naming a section.
    No statement changed. Not checked: no certificate. The second direction's use of the direct
    limit over all finite subcomplexes, and the injectivity of $1-s_*$ in every degree, are as before.

---

::: {.problem}
This is Exercise 1 of Section 4.F of Hatcher, *Algebraic Topology* (2002); the statement below is its wording.

Assuming the first two axioms for a homology theory on the CW category, show that the direct limit axiom implies the wedge sum axiom.
Show that the converse also holds for countable CW complexes.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, using only the first two axioms of §4.F and the definitions of the other two proved in section 4.F of Hatcher. The statement is §4.F Exercise 1.

::: pf

::: {.pf-step #axioms}
Let $\widetilde h_*$ satisfy the homotopy and exactness axioms (1) and (2) of Hatcher's list; the wedge sum axiom (3) and the direct limit axiom are the two statements to be compared.

::: pf-proof
These are the axioms as Hatcher states them: (1) homotopy invariance, (2) exactness for a CW pair, (3) $\widetilde h_n(\bigvee_\alpha X_\alpha)\cong\bigoplus_\alpha\widetilde h_n(X_\alpha)$; the direct limit axiom identifies $\widetilde h_n(X)$ with the direct limit of $\widetilde h_n$ over the finite subcomplexes of $X$, as §4.F states it.
:::
:::

::: {.pf-step #finite}
Axioms (1) and (2) already give the wedge sum axiom for finite wedge sums.

::: pf-proof
Apply exactness to the pair $(X_1\vee X_2,X_1)$: the quotient is $X_2$ and the pair is a CW pair, so the long exact sequence splits because the inclusion of $X_1$ into the wedge is a retract up to homotopy; the splitting gives $\widetilde h_n(X_1\vee X_2)\cong\widetilde h_n(X_1)\oplus\widetilde h_n(X_2)$, and induction extends this to finitely many summands. Hatcher records this in the axioms for homology in §2.3.
:::
:::

::: {.pf-step #forward}
The direct limit axiom implies the wedge sum axiom.

::: pf-proof
Let $X=\bigvee_\alpha X_\alpha$. Each finite subcomplex $K\subset X$ lies in a finite wedge $K_{\alpha_1}\vee\cdots\vee K_{\alpha_r}$ with $K_{\alpha_i}\subset X_{\alpha_i}$ finite, so by step [](#finite){.pf-ref} $\widetilde h_n(K)\cong\bigoplus_i\widetilde h_n(K_{\alpha_i})$. The finite subcomplexes of $X$ are cofinal among those of the wedge, so the direct limit axiom gives $\widetilde h_n(X)\cong\varinjlim_K\widetilde h_n(K)$, and a filtered colimit of the groups $\bigoplus_i\widetilde h_n(K_{\alpha_i})$ over varying finite index sets is the direct sum $\bigoplus_\alpha\widetilde h_n(X_\alpha)$, because each finite set of summands eventually appears and the colimit of a fixed-summand direct system is the direct sum of the colimits.
:::
:::

::: {.pf-step #telescope}
Conversely, let $X$ be a countable CW complex with an exhaustion $X_1\subset X_2\subset\cdots$ by finite subcomplexes, and let $T$ be the based mapping telescope with the basepoint track collapsed. Then $\widetilde h_*(T)\cong\widetilde h_*(X)$.

::: pf-proof
A countable CW complex has such an exhaustion: enumerate its cells and let $X_i$ be the subcomplex consisting of the first $i$ of them, which is finite because of the closure-finiteness condition in the definition of a CW complex. For the resulting telescope, $T$ is a subcomplex of $X\times[0,\infty)$ in the CW structure of Theorem 3F.8, and the argument in the proof of Lemma 2.34 — there applied to the skeleton filtration, but using only that the $X_i$ are subcomplexes with $X_i\subset X_{i+1}$ — deformation retracts $X\times[0,\infty)$ onto $T$; since $X\times[0,\infty)$ deformation retracts onto $X\times\{0\}=X$, the spaces $T$ and $X$ are homotopy equivalent, and a homotopy equivalence induces an isomorphism on any homology theory by axiom (1).
:::
:::

::: {.pf-step #mv-lemma}
Axioms (1) and (2) give Mayer--Vietoris: for a CW complex $X$ with subcomplexes $A$ and $B$ such that $X=A\cup B$, there is an exact sequence
$$\cdots\to\widetilde h_n(A\cap B)\to\widetilde h_n(A)\oplus\widetilde h_n(B)\to\widetilde h_n(X)\xrightarrow{\ \partial\ }\widetilde h_{n-1}(A\cap B)\to\cdots .$$

::: pf-proof
Axiom (2) gives the exact sequences of the CW pairs $(X,A)$ and $(B,A\cap B)$. The quotient $B/(A\cap B)$ is $X/A$, because $X=A\cup B$, so the second sequence is the first with $\widetilde h_n(A)$ replaced by $\widetilde h_n(B)$ and its quotient term identified with $\widetilde h_n(X/A)$. Writing the two sequences as the rows of a ladder, the identification of the two quotient groups makes every third vertical map an isomorphism, and the algebraic lemma that such a ladder gives a long exact sequence of the remaining terms — Exercise 38 of §2.2, which Hatcher applies in §2.3 to exactly this diagram — produces the sequence. The map $\partial$ is the boundary of the pair $(X,A)$ read through that identification, and the derivation is the same for reduced groups as for the unreduced ones Hatcher writes.
:::
:::

::: {.pf-step #telescope-cover}
The reduced telescope $T$ is the union of two subcomplexes $T_1$ and $T_2$, the images of the cylinders $X_i\times[i,i+1]$ over odd and over even $i$; then $T_1\cap T_2$ is the one-point union of the copies of the $X_i$ at the shared levels, $T_1$ is the one-point union of the mapping cylinders of the $f_i$ with $i$ odd, and $T_2$ the same with $i$ even.

::: pf-proof
The telescope is the quotient of $\coprod_i X_i\times[i,i+1]$ in which $(x,i+1)\in X_i\times\{i+1\}$ is identified with $(f_i(x),i+1)\in X_{i+1}\times\{i+1\}$, with the basepoint track $\{x_0\}\times[0,\infty)$ collapsed; it is a based subcomplex of $X\times[0,\infty)$ for the CW structure of Theorem 3F.8 that gives $[0,\infty)$ its integer points as $0$-cells. A cylinder of $T_1$ meets the rest of $T_1$ only inside $T_2$: the top end $X_i\times\{i+1\}$ of the $i$-th cylinder is attached to the copy of $X_i$ at level $i+1$, which is a level of the $(i+1)$-st cylinder, and $i$ and $i+1$ have opposite parity. So the cylinders of $T_1$ meet one another only at the collapsed basepoint track, and $T_1$ is the one-point union of those mapping cylinders. The $i$-th of them is the mapping cylinder of $f_i$, whose target end is the copy of $X_i$ at level $i+1$; a mapping cylinder deformation retracts onto its target end through the homotopy that collapses the interval coordinate, and that homotopy fixes the basepoint track, so axiom (1) identifies $\widetilde h_n(T_1)$ with the direct sum of the $\widetilde h_n(X_i)$ over odd $i$ once axiom (3) is applied to this one-point union; the same holds for $T_2$ and even $i$. The two subcomplexes cover $T$ because the cylinders of both parities fill $[0,\infty)$, and their intersection consists of the copies of $X_i$ at the levels $i+1$ that are the top of one cylinder and the bottom of the next, one copy for each $i$, so axiom (3) identifies $\widetilde h_n(T_1\cap T_2)$ with $\bigoplus_i\widetilde h_n(X_i)$ as well. This is the decomposition used in the proof of Theorem 3F.8.
:::
:::

::: {.pf-step #mv}
With $s_*$ defined by $(s_*g)_i=\rho(g_{i+1})$, $\rho$ being the map induced by the inclusion $X_i\subset X_{i+1}$, Mayer--Vietoris for $T=T_1\cup T_2$ and the wedge axiom (3) give an exact sequence
$$\bigoplus_i\widetilde h_n(X_i)\xrightarrow{\ \varphi\ }\bigoplus_i\widetilde h_n(X_i)\longrightarrow\widetilde h_n(T)\xrightarrow{\ \partial\ }\bigoplus_i\widetilde h_{n-1}(X_i),$$
where $\varphi(g)_i=(-1)^{i-1}\bigl(g_i-\rho(g_{i+1})\bigr)$; after the change of coordinates $g_i\mapsto(-1)^{i-1}g_i$ on the even summands, $\varphi$ is $1-s_*$.

::: pf-proof
Apply step [](#mv-lemma){.pf-ref} to the subcomplexes $T_1$ and $T_2$ of $T$. Steps [](#telescope-cover){.pf-ref} and axiom (3) identify $\widetilde h_n(T_1)\oplus\widetilde h_n(T_2)$ with $\bigoplus_i\widetilde h_n(X_i)$, the odd summands lying in $T_1$ and the even ones in $T_2$, and identify $\widetilde h_n(T_1\cap T_2)$ with the same direct sum after naming each shared level by the index of the copy of $X_i$ that it carries; this re-indexing is the one Hatcher uses when he writes $\coprod_i X_i$ for the intersection in the proof of Theorem 3F.8. The two maps into the intersection are then the identity and the shift, and the difference of the two restricted classes is the formula displayed for $\varphi$, which is the one Hatcher records in that proof. Multiplying the coordinates of the even summands by $-1$ is an automorphism of the direct sum and replaces $\varphi$ by $1-s_*$, exactly as Hatcher removes the signs from his $\varphi$ by inserting a minus sign in the even coordinates. The map $\partial$ out of $\widetilde h_n(T)$ is the boundary of the pair $(T,T_1)$, transported across the isomorphism $T/T_1\cong T_2/(T_1\cap T_2)$ supplied by the same lemma; it is not itself $1-s_*$, which is the map that follows it.
:::
:::

::: {.pf-step #injective}
$1-s_*$ is injective on the direct sum $\bigoplus_i\widetilde h_n(X_i)$.

::: pf-proof
Let $x$ be a finite-support element with $(1-s_*)x=0$ and let $i$ be the largest index with $x_i\neq0$, which exists because the support is finite. The $i$-th coordinate of $(1-s_*)x$ is $x_i-(s_*x)_i=x_i-\rho(x_{i+1})=x_i$, since $x_{i+1}=0$ by the choice of $i$; so that coordinate is nonzero and $(1-s_*)x\neq0$, a contradiction. Hence $x=0$.
:::
:::

::: {.pf-step #colimit}
$\widetilde h_n(X)\cong\varinjlim_i\widetilde h_n(X_i)$, and this colimit is also the colimit over all finite subcomplexes of $X$.

::: pf-proof
In the sequence of step [](#mv){.pf-ref} the connecting map out of $\widetilde h_n(T)$ is followed by $1-s_*$ on $\bigoplus_i\widetilde h_{n-1}(X_i)$, which is injective by step [](#injective){.pf-ref} applied in degree $n-1$; its image is therefore $0$, so the map $\bigoplus_i\widetilde h_n(X_i)\to\widetilde h_n(T)$ is onto and $\widetilde h_n(T)\cong\operatorname{coker}(1-s_*)$ in degree $n$. That cokernel is $\bigoplus_i\widetilde h_n(X_i)$ modulo the classes of $x-s_*x$, which is the colimit of $\widetilde h_n(X_1)\to\widetilde h_n(X_2)\to\cdots$, and with step [](#telescope){.pf-ref} it is $\widetilde h_n(X)$. For a countable CW complex the exhaustion can be taken by finite subcomplexes, and every finite subcomplex lies in one of them, so this colimit is the direct limit over all finite subcomplexes, which is the axiom's form.
:::
:::

::: {.pf-step}
The direct limit axiom implies the wedge sum axiom, and conversely for countable CW complexes.

::: pf-proof
Step [](#forward){.pf-ref} is the first implication and step [](#colimit){.pf-ref} the second.
:::
:::

:::
:::
