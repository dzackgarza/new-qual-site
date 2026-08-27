Existence of Lefschetz ﬁbrations on Stein and Weinstein
domains
Emmanuel Giroux
John Pardon
17 July 2015; Revised 7 April 2016
Abstract
We show that every Stein or Weinstein domain may be presented (up to deforma-
tion) as a Lefschetz ﬁbration over the disk. The proof is an ap plication of Donaldson’s
quantitative transversality techniques.
1 Introduction
In this paper, we prove the existence of Lefschetz ﬁbrations (certain singular ﬁbrations with
Morse-type singularities) on Stein domains (from complex geometry) and on Weinstein
domains (from symplectic geometry). These two results are linked (in fact, logically so)
by the close relationship between Stein and Weinstein structures es tablished in the book
by Cieliebak–Eliashberg [
CE12] building on earlier work of Eliashberg [ Eli90]. Nevertheless,
they can be understood independently from either a purely complex geometric viewpoint or
from a purely symplectic viewpoint.
1.1 Lefschetz ﬁbrations on Stein domains
We begin by explaining our results for Stein domains.
Deﬁnition 1.1. A real-valued function φ on a complex manifold V is called J-convex (or
strictly plurisubharmonic ) iﬀ ( id′d′′φ)(v, Jv ) > 0 for every nonzero (real) tangent vector v.
Deﬁnition 1.2. A Stein manifold is a complex manifold V which admits a smooth exhaust-
ing J-convex function φ : V → R.
Deﬁnition 1.3. A Stein domain is a compact complex manifold with boundary V which
admits a smooth J-convex function φ : V → R with ∂V = {φ = 0} as a regular level set.
(For us, a complex manifold with boundary (or corners) shall mean o ne equipped with
a germ of (codimension zero) embedding into an (open) complex manif old. A holomorphic
function on a complex manifold with boundary (or corners) is one whic h extends holomor-
phically to an open neighborhood in the ambient (open) complex manifo ld.)
1

For example, if V is a Stein manifold with smooth exhausting J-convex function φ : V →
R with {φ = 0} as a regular level set, then V := {φ ≤ 0} is a Stein domain. In fact, it is not
hard to see that every Stein domain is of this form.
Deﬁnition 1.4. Let D2 ⊆ C denote the closed unit disk. A Stein Lefschetz ﬁbration is a
holomorphic map π : V → D2 where V is a compact complex manifold with corners, such
that:
• (Singular ﬁbration) The map π is a (smooth) ﬁbration with manifold with boundary
ﬁbers, except for a ﬁnite number of critical points crit( π) in the interior of V .
• (Non-degenerate critical points) Near each critical point p ∈ crit(π), there are local
holomorphic coordinates in which π is given by (z1, . . . , zn) ↦→π(p)+∑ n
i=1 z2
i (according
to the complex Morse lemma, this holds iﬀ the complex Hessian at p is non-degenerate).
Furthermore, all critical values are distinct.
• (Stein ﬁbers) There exists a J-convex function φ : V → R with ∂hV = {φ = 0 } as a
regular level set, where ∂hV := ⋃
p∈D2 ∂(π−1(p)) denotes the “horizontal boundary” of
V .
Note that the boundary of V is the union of the horizontal boundary ∂hV and the “vertical
boundary” ∂vV := π−1(∂D 2), whose intersection ∂hV ∩ ∂vV is the corner locus.
The total space V of any Stein Lefschetz ﬁbration may be smoothed out to obtain a St ein
domain V sm, unique up to deformation. Speciﬁcally, for any function g : R<0 → R satisfying
g′ > 0, g′′ > 0, and lim x→0− g(x) = ∞, the function Φ g := g(|π|2 − 1) + g(φ) is an exhausting
J-convex function on V ◦. Moreover, the critical locus of Φ g stays away from ∂V as g varies
in any compact family (this follows from the obvious inclusion crit(Φ g) ⊆ ⋃
p∈D2 crit(φ|π−1(p))
and the fact that the latter is a compact subset of V \ ∂hV ). As a result, the sublevel set
{Φ g ≤ M} is a Stein domain which, up to deformation, is independent of the choic e of g and
the choice of M larger than all critical values of Φ g. We denote this (deformation class of)
Stein domain by V sm, which, of course, depends not only on V , but also on π.
The simplest (and weakest) version of our existence result is the fo llowing.
Theorem 1.5. Let V be a Stein domain. There exists a (Stein) Lefschetz ﬁbration π : V ′ →
D2 with (V ′)sm deformation equivalent to V .
Deformation is meant in the sense of a real 1-parameter family of St ein domains. The
nature of the deformation required is made explicit by considering th e following stronger
version of our existence result.
Theorem 1.6. Let V be a Stein domain. For every suﬃciently large real number k, there
exists a holomorphic function π : V → C such that:
• For |π(p)| ≥ 1, we have d log π(p) = k · d′φ(p) + O(k1/2).
• For |π(p)| ≤ 1 and p ∈ ∂V , we have dπ(p)|ξ ⁄= 0.
We may, in addition, require that π−1(D2) contain any given compact subset of V ◦.
2

Theorem 1.5 follows from Theorem 1.6 by smoothing out the deformation of Stein do-
mains {π−1(D2
r )}1≤r<∞ (this argument is given in detail in §5). Theorem 1.6 is a corollary
of the following, which is the main technical result of the paper.
Theorem 1.7. Let
V be a Stein manifold, equipped with a smooth exhausting J-convex
function φ : V → R. For every suﬃciently large real number k, there exists a holomorphic
function f : V → C such that:
• | f (p)| ≤ e
1
2 kφ(p) for p ∈ {φ ≤ 1}.
• | f (p)| + k−1/2|d f(p)|ξ| > η for p ∈ {φ = 0} (d fmeasured in the metric induced by φ).
where ξ denotes the Levi distribution on {φ = 0 } ⊆ V , and η > 0 is a constant depending
only on the dimension of V .
To prove Theorem 1.6 (for V := {φ ≤ 0}) from Theorem 1.7, we take π to be (a small
perturbation of) η−1 · f , which works once k is suﬃciently large (the details of this argument
are given in §5). To prove Theorem 1.7, we use methods introduced by Donaldson [ Don96]
(this proof occupies §2–4). A closely related result was obtained by Mohsen [ Moh13] also
using Donaldson’s techniques.
1.2 Lefschetz ﬁbrations on Weinstein domains
Next, we turn to our result for Weinstein domains.
Deﬁnition 1.8. A Weinstein domain is a compact symplectic manifold with boundary
(W, ω) equipped with a 1-form λ satisfying dλ = ω and a Morse function φ : W → R which
has ∂W = {φ = 0 } as a regular level set and for which Xλ (deﬁned by ω(Xλ, ·) = λ) is
gradient-like.
Deﬁnition 1.9. An abstract Weinstein Lefschetz ﬁbration is a tuple
W = (W0; L1, . . . , Lm)
consisting of a Weinstein domain W 2n−2
0 (the “central ﬁber”) along with a ﬁnite sequence of
exact parameterized
1 Lagrangian spheres L1, . . . , Lm ⊆ W0 (the “vanishing cycles”).
From any abstract Weinstein Lefschetz ﬁbration W = (W0; L1, . . . , Lm), we may construct
a Weinstein domain |W | (its “total space”) by attaching critical Weinstein handles to the
stabilization W0 × D2 along Legendrians Λ j ⊆ W0 × S1 ⊆ ∂(W0 × D2) near 2 πj/m ∈ S1
obtained by lifting the exact Lagrangians Lj. We give this construction in detail in §6.
We will prove the following existence result.
Theorem 1.10. Let W be a Weinstein domain. There exists an abstract Weinstein Le fschetz
ﬁbration W ′ = (W0; L1, . . . , Lm) whose total space |W ′| is deformation equivalent to W .
1Parameterized shall mean equipped with a diﬀeomorphism Sn− 1 ∼
− →L deﬁned up to precomposition
with elements of O(n).
3

Deformation is meant in the sense of a 1-parameter family of Weinste in domains, but
where the requirement that φ be Morse is relaxed to allow birth death critical points. The-
orem 1.10 is deduced from Theorem 1.5 using the existence theorem for Stein structures
on Weinstein domains proved by Cieliebak–Eliashberg [ CE12, Theorem 1.1(a)]. The main
step is thus to show that a Stein Lefschetz ﬁbration π : V → D2 naturally gives rise to an
abstract Weinstein Lefschetz ﬁbration whose total space is defo rmation equivalent to V sm
(the details of this argument are given in §6).
In current work in progress, we hope to apply Donaldson’s techniqu es directly in the
Weinstein setting to produce on any Weinstein domain W an approximately holomorphic
function f : W → C satisfying conditions similar to those in Theorem 1.7, and thus give a
proof of Theorem 1.10 which does not appeal to the existence of a compatible Stein struct ure.
Given Theorem 1.10, it is natural to ask whether every deformation equivalence betwe en
the total spaces of two abstract Weinstein Lefschetz ﬁbrations is induced by a ﬁnite sequence
of moves of some simple type. Speciﬁcally, applying any of the following operations to an
abstract Weinstein Lefschetz ﬁbration preserves the total spa ce up to canonical deformation
equivalence, and it is natural to ask whether they are enough.
• (Deformation) Simultaneous Weinstein deformation of W0 and exact Lagrangian iso-
topy of ( L1, . . . , Lm).
• (Cyclic permutation) Replace ( L1, . . . , Lm) with ( L2, . . . , Lm, L1).
• (Hurwitz moves) Let τL denote the symplectic Dehn twist around L, and replace
(L1, . . . , Lm) with either ( L2, τL2L1, L3, . . . , Lm) or ( τ −1
L1 L2, L1, L3, . . . , Lm).
• (Stabilization) For a parameterized Lagrangian disk Dn−1֒→W0 with Legendrian
boundary Sn−2 = ∂D n−1֒→∂W0 such that 0 = [ λ0] ∈ H 1(Dn−1, ∂Dn−1), replace W0
with ˜W0, obtained by attaching a Weinstein handle to W0 along ∂D n−1, and replace
(L1, . . . , Lm) with ( ˜L, L1, . . . , Lm), where ˜L ⊆ ˜W0 is obtained by gluing together Dn−1
and the core of the handle.
It would be very interesting if the methods of this paper could be bro ught to bear on this
problem as well.
Remark 1.11. The reader is likely to be familiar with more geometric notions of symplec -
tic Lefschetz ﬁbrations (e.g., as in Seidel [
Sei08b, §15d] or Bourgeois–Ekholm–Eliashberg
[BEE12, §8.1] and the references therein), and may prefer these to the no tion of an abstract
Weinstein Lefschetz ﬁbration used to state Theorem 1.10. We believe, though, that the
reader wishing to construct a symplectic Lefschetz ﬁbration in the ir preferred setup with the
same total space as a given abstract Weinstein Lefschetz ﬁbratio n will have no trouble doing
so (e.g., see Seidel [ Sei08b, §16e]).
Seidel [ Sei08b, Sei08a, Sei09, Sei12] has developed powerful methods for calculations in
and of Fukaya categories coming from Lefschetz ﬁbrations, in par ticular relating the Fukaya
category of the total space to the vanishing cycles and the Fukay a category of the central
ﬁber. Our existence result shows that these methods are applicab le to any Weinstein domain.
We should point out, however, that, while our proof of existence of Lefschetz ﬁbrations is
in principle eﬀective, it does not immediately lead to any practical way o f computing a
Lefschetz presentation of a given Weinstein manifold.
4

1.3 Remarks about the proof
We outline brieﬂy the proof of Theorem
1.7 (the main technical result of the paper), which
occupies §2–4. As mentioned earlier, the proof is an application of Donaldson’s quan titative
transversality techniques, ﬁrst used to construct symplectic div isors inside closed symplectic
manifolds [ Don96] (somewhat similar ideas appeared earlier in Cheeger–Gromov [ CG91]).
The J-convex function φ : V → R determines a positive line bundle L on V . We consider
the high tensor powers Lk of this positive line bundle. Using L2-methods of H¨ ormander
[H¨ or65] and Andreotti–Vesentini [ A V65], one may construct “peak sections” of Lk, that is,
holomorphic sections s : V → Lk which are “concentrated” over the ball of radius k−1/2
centered at any given point p0 ∈ V := {φ ≤ 0} and have decay |s(p)| = O(e−ǫ·k·d(p,p0)2
) for
p ∈ {φ ≤ 1}.
Donaldson introduced a remarkable method to, given enough localize d holomorphic sec-
tions, construct a linear combination s : V → Lk which satisﬁes, quantitatively, any given
holomorphic transversality condition which is generic. The key techn ical ingredient for Don-
aldson’s construction is a suitably quantitative version of Sard’s the orem, and this step was
simpliﬁed considerably by Auroux [ Aur02]. The function f asserted to exist in Theorem 1.7
is simply the quotient of such a quantitatively transverse section s : V → Lk by a certain
tautological section “1” : V → Lk.
We take advantage of the fact that we are in the holomorphic categ ory by working
with genuinely holomorphic functions, instead of the approximately h olomorphic functions
which are the standard context of Donaldson’s techniques. This allo ws us to use simpliﬁed
arguments at various points in the proof, and this is the reason for our passage from the
Weinstein setting to the Stein setting. It is not clear whether one sh ould expect to be able
to generalize our arguments to apply directly to Weinstein manifolds.
Note that in most applications of quantitative transversality techn iques in symplec-
tic/contact geometry, the result in the integrable case requires o nly generic transversal-
ity, and the passage from integrable to non-integrable J is what necessitates quantitative
transversality. Here, quantitative transversality is needed in bot h the integrable and non-
integrable settings (although indeed, one would need more quantita tive transversality in the
non-integrable case).
Besides Donaldson’s original paper [ Don96], which is the best place to ﬁrst learn the
methods introduced there, let us mention a few other papers wher e approximately holomor-
phic techniques have been used to obtain results similar to Theorem 1.10. In addition to
constructing symplectic divisors [ Don96], Donaldson also constructed Lefschetz pencils on
closed symplectic manifolds [ Don99]. Auroux [ Aur97, Aur00] further generalized and reﬁned
Donaldson’s techniques to 1-parameter families of sections and to h igh twists E ⊗ Lk of
a given Hermitian vector bundle E. In particular, he showed that Donaldson’s symplec-
tic divisors are all isotopic for ﬁxed suﬃciently large k, and that symplectic four-manifolds
can be realized as branched coverings of CP 2. Ibort–Mart ´ ınez-Torres–Presas [IMTP00] ob-
tained analogues for contact manifolds of Donaldson’s and Auroux’s results, and these were
used in [ Gir02] to construct open books on contact manifolds in any dimension. Mo hsen
[Moh01, Moh13] extended the techniques of Donaldson and Auroux to construct sections
whose restrictions to a given submanifold satisfy certain quantitat ive transversality condi-
tions. He also showed that this result implies both the uniqueness the orem of Auroux on
5

symplectic divisors and the contact theorem of Ibort–Mart ´ ınez– Presas. His main observa-
tion is that the quantitative Sard theorem applies to real (not just to complex) polynomials.
This plays an important role in the present work; it makes it possible to obtain quantitative
transversality for the restriction of a holomorphic section to a rea l hypersurface.
1.4 Acknowledgements
We wish to thank Yasha Eliashberg, Jean-Paul Mohsen, and Paul Se idel for helpful discus-
sions and encouragement. We thank Sylvain Courte for pointing out an error in an earlier
version of the proof of Lemma
6.6, and we thank the referee for their careful reading.
This collaboration started after E. G. visited Stanford University in April 2014, and he
is very grateful to the Department of Mathematics for its hospita lity and ﬁnancial support.
J. P. subsequently visited the ´Ecole normale sup´ erieure de Lyon in July 2014, and he thanks
the Unit´ e de math´ ematiques pures et appliqu´ ees for its hospitality and ﬁnancial support.
This work was supported by the LABEX MILYON (ANR–10–LABX–007 0) of Universit´ e
de Lyon, within the program “Investissements d’Avenir” (ANR–11– IDEX–0007) operated
by the French National Research Agency (ANR). J. P. was partially supported by an NSF
Graduate Research Fellowship under grant number DGE–1147470.
2 Review of complex geometry
We now provide for the reader a review of some classical results in co mplex geometry which
we need. Our speciﬁc target is the solution of the d′′-operator on Stein manifolds via the L2
methods of H¨ ormander [
H¨ or65] and Andreotti–Vesentini [ A V65]. This will be used later to
construct the localized “peak sections” necessary for Donaldson ’s construction. The reader
may refer to [ Don96, Proposition 34] for an analogous discussion in the case of compact
K¨ ahler manifolds.
2.1 K¨ ahler geometry
For a complex vector bundle E with connection d over a complex manifold M, we denote
by d′ : E ⊗ Ω p,q → E ⊗ Ω p+1,q and d′′ : E ⊗ Ω p,q → E ⊗ Ω p,q+1 the complex linear and
complex conjugate linear parts of the exterior derivative d : E ⊗ Ω k → E ⊗ Ω k+1. When M
is equipped with a K¨ ahler metric and E is equipped with a Hermitian metric, we let d′∗ and
d′′∗ denote the formal adjoints of d′ and d′′ respectively, and we let ∆ ′ := d′∗d′ + d′d′∗ and
∆ ′′ := d′′∗d′′ + d′′d′′∗ denote the corresponding Laplacians.
Recall that on any holomorphic vector bundle with a Hermitian metric, there exists a
unique connection compatible with the metric and the holomorphic str ucture, called the
Chern connection.
Lemma 2.1 (Bochner–Kodaira–Nakano identity). Let E be a holomorphic Hermitian vector
bundle over a K¨ ahler manifold. Then we have
∆ ′′
E = ∆ ′
E + [iΘ( E), Λ] (2.1)
where Θ( E) is the curvature of E and Λ is the adjoint of L := · ∧ ω.
6

For a holomorphic Hermitian vector bundle E over a K¨ ahler manifold, there is an induced
Hermitian metric on E ⊗ Ω 0,q. The operator d′ : E ⊗ Ω 0,q → E ⊗ Ω 1,q = E ⊗ Ω 0,q ⊗ Ω 1,0
further equips E ⊗ Ω 0,q with an anti-holomorphic structure. Together these induce a Cher n
connection on E ⊗ Ω 0,q. We denote this connection by ∇ = ∇′ + ∇′′, where ∇′ = d′, and
we denote the corresponding Laplacians by □ ′ and □ ′′, where □ ′ = ∆ ′. Applying ( 2.1) to
E ⊗ Ω 0,q gives
□ ′′
E⊗Ω 0,q = □ ′
E⊗Ω 0,q + [iΘ( E ⊗ Ω 0,q), Λ] . (2.2)
Now since □ ′
E⊗Ω 0,q = ∆ ′
E operating on E ⊗ Ω 0,q, we may combine (
2.1) and ( 2.2) to produce
the following Weitzenb¨ ock formula
∆ ′′
E = □ ′′
E⊗Ω 0,q + Λ iΘ( E ⊗ Ω 0,q) − Λ iΘ( E) (2.3)
operating on E⊗Ω 0,q. We remark, for clarity, that the ﬁrst composition is of maps E⊗Ω 0,q ⇄
E ⊗ Ω 0,q ⊗ Ω 1,1 and the second composition is of maps E ⊗ Ω 0,q ⇄ E ⊗ Ω 1,q+1. We have
followed Donaldson [
Don90, p36] in the derivation of this identity.
Lemma 2.2 (Morrey–Kohn–H¨ ormander formula). Let E be a holomorphic Hermitian vector
bundle over a K¨ ahler manifold M. For any u ∈ C ∞
c (M, E ⊗ Ω 0,q), we have
∫
|d′′u|2 + |d′′∗u|2 =
∫
|∇′′u|2 +
∫
⟨u, Λ iΘ( E ⊗ Ω 0,q)u⟩ − ⟨u, Λ iΘ( E)u⟩. (2.4)
Proof. By the deﬁnition of the adjoint, integrating by parts gives
∫
|d′′u|2 + |d′′∗u|2 =
∫
⟨u, ∆ ′′u⟩. (2.5)
The same integration by parts with ∇ in place of d gives
∫
|∇′′u|2 =
∫
⟨u, □ ′′u⟩. (2.6)
Now we take the diﬀerence of these two identities and use ( 2.3) to obtain ( 2.4).
2.2 L2 theory of the d′′-operator
The L2 theory that we review here is due to H¨ ormander [ H¨ or65] and Andreotti–Vesentini
[A V65].
Lemma 2.3. Let E be a holomorphic Hermitian vector bundle over a complete K¨ a hler man-
ifold M. We consider sections u of E ⊗ Ω p,q.
• If u, d′′u ∈ L2 (in the sense of distributions), then there exists a sequenc e ui ∈ C ∞
c
such that (ui, d′′ui) → (u, d′′u) in L2.
• If u, d′′u, d′′∗u ∈ L2 (in the sense of distributions), then there exists a sequenc e ui ∈ C ∞
c
such that (ui, d′′ui, d′′∗ui) → (u, d′′u, d′′∗u) in L2.
7

Proof. This is essentially a special case of Friedrichs’ result [ Fri44] which applies more gen-
erally to any ﬁrst order diﬀerential operator. We outline the argum ent, which is also given
in H¨ ormander [H¨ or65, Proposition 2.1.1] and Andreotti–Vesentini [ A V65, Lemma 4, Propo-
sition 5].
We prove the ﬁrst statement only, as the proof of the second is ide ntical. Let u be
given. Composing the distance function to a speciﬁed point in M with the cutoﬀ function
x ↦→max(1 − ǫx, 0), we get a function fǫ : M → R with sup |fǫ| ≤ 1 and sup |d fǫ| ≤ ǫ, so
that fǫ → 1 uniformly on compact subsets of M as ǫ → 0. Using these properties, it follows
that fǫu → u in L2 and that d′′(fǫu) → d′′u in L2. Since M is complete, fǫ is compactly
supported. Hence we may assume without loss of generality that u is compact supported.
Since u is compactly supported, we may use a partition of unity argument to reduce
to the case when u is supported in a given small coordinate chart of M. Now in a small
coordinate chart, choosing trivializations of the bundles in question , the operator d′′ is a ﬁrst
order diﬀerential operator D with smooth coeﬃcients. It can now be checked (and this is the
key point) that ‖D(u ∗ ϕǫ) − Du ∗ ϕǫ‖2 → 0, where ϕǫ := ǫ−nϕ(x/ǫ) is a smooth compactly
supported approximation to the identity. It follows that the convo lutions u ∗ ϕǫ give the
desired approximation of u by smooth functions of compact support.
Proposition 2.4. Let E be a holomorphic Hermitian vector bundle over a complete K¨ a hler
manifold M. Fix q, and suppose that for all u ∈ C ∞
c (M, E ⊗ Ω 0,q), we have
∫
|u|2 ≤ A
∫
|d′′u|2 + |d′′∗u|2. (2.7)
Then for any u ∈ L2(M, E ⊗ Ω 0,q) satisfying d′′u = 0 , there exists ξ ∈ L2(M, E ⊗ Ω 0,q−1)
satisfying d′′ξ = u and ∫
|ξ|2 ≤ A
∫
|u|2 (2.8)
(d′′ is taken in the sense of distributions).
Proof. We follow an argument from notes by Demailly [ Dem96, p33, (8.4) Theorem].
We wish to ﬁnd ξ such that d′′ξ = u, or, equivalently,
∫
⟨d′′∗ϕ, ξ⟩ =
∫
⟨ϕ, u⟩ for all
ϕ ∈ C ∞
c (M, E ⊗ Ω 0,q). We claim that the existence of such a ξ with
∫
|ξ|2 ≤ B is equivalent
to the estimate ⏐
⏐
⏐
⏐
∫
⟨ϕ, u⟩
⏐
⏐
⏐
⏐
2
≤ B
∫
|d′′∗ϕ|2 (2.9)
for all ϕ ∈ C ∞
c (M, E ⊗Ω 0,q). Indeed, given (
2.9), the map d′′∗ϕ ↦→
∫
⟨ϕ, u⟩ on d′′∗(C ∞
c (M, E ⊗
Ω 0,q)) is well deﬁned and L2 bounded, and thus it is of the form
∫
⟨d′′∗ϕ, ξ⟩ for a unique ξ
in the closure of d′′∗(C ∞
c (M, E ⊗ Ω 0,q)) ⊆ L2(M, E ⊗ Ω 0,q−1) satisfying
∫
|ξ|2 ≤ B. Thus we
are reduced to showing ( 2.9) for B = A
∫
|u|2.
To prove (2.9), argue as follows. Since L2 convergence implies distributional convergence,
the kernel (in the sense of distributions) ker d′′ ⊆ L2(M, E ⊗Ω 0,q) is a closed subspace. Hence
for any ϕ ∈ C ∞
c (M, E ⊗Ω 0,q), we may write ϕ = ϕ1+ϕ2 where ϕ1 ∈ ker d′′ and ϕ2 ∈ (ker d′′)⊥.
Now since u ∈ ker d′′, we have
⏐
⏐
⏐
⏐
∫
⟨ϕ, u⟩
⏐
⏐
⏐
⏐
2
=
⏐
⏐
⏐
⏐
∫
⟨ϕ1, u⟩
⏐
⏐
⏐
⏐
2
≤
∫
|u|2 ·
∫
|ϕ1|2. (2.10)
8

Since ϕ2 ⊥ ker d′′ ⊇ im d′′, it follows that ϕ2 ∈ ker d′′∗ (in the sense of distributions). Hence
∫
|d′′ϕ1|2 + |d′′∗ϕ1|2 =
∫
|d′′∗ϕ|2. (2.11)
Combining (2.10) and ( 2.11), we see that to prove ( 2.9) with B = A
∫
|u|2, it suﬃces to show
that ∫
|ϕ1|2 ≤ A
∫
|d′′ϕ1|2 + |d′′∗ϕ1|2. (2.12)
This is true by hypothesis ( 2.7) for ϕ1 ∈ C ∞
c (M, E ⊗ Ω 0,q), and hence by Lemma 2.3 it holds
given just that ϕ1, d′′ϕ1, d′′∗ϕ1 ∈ L2.
2.3 Stein manifolds and solving the d′′-operator
Let V be a Stein manifold or a Stein domain. A smooth J-convex function φ : V → R
induces a symplectic form ωφ := id′d′′φ and a Riemannian metric gφ(X, Y ) := ωφ(X, JY )
(so hφ := gφ − iωφ is a Hermitian metric) whose distance function we denote by dφ(·, ·). The
function φ also gives rise to a holomorphic Hermitian line bundle Lφ over V , namely the
trivial complex line bundle C equipped with its standard holomorphic structure d′′
C and the
Hermitian metric |·|Lφ := e− 1
2 φ |·|C. The resulting Chern connection on Lφ is given by
dLφ = dC − d′φ (2.13)
with curvature Θ( Lφ) = d′d′′φ = −iωφ. (Equivalently, Lφ is the trivial complex line bundle
equipped with its standard Hermitian metric and the holomorphic stru cture d′′
C + 1
2d′′φ,
with resulting Chern connection dC + 1
2 iJ ∗dφ. This is equivalent to the ﬁrst deﬁnition via
multiplication by e
1
2 φ.)
The following result (due to H¨ ormander [H¨ or65] and Andreotti–Vesentini [ A V65]) allows
us to produce many holomorphic sections of Lφ for suﬃciently J-convex φ.
Proposition 2.5. For every Stein manifold V with complete K¨ ahler metricg, there exists a
continuous function c : V → R>0 with the following property. Let φ : V → R be J-convex and
satisfy gφ ≥ c · g (pointwise inequality of quadratic forms). Then for any u ∈ L2(V, Lφ ⊗ Ω 0,q)
(q > 0) satisfying d′′u = 0, there exists ξ ∈ L2(V, Lφ ⊗ Ω 0,q−1) satisfying d′′ξ = u and
∫
|ξ|2 ≤
∫
|u|2. (2.14)
Proof. By Proposition 2.4, it suﬃces to show the estimate
∫
|d′′u|2 + |d′′∗u|2 ≥
∫
|u|2 (2.15)
for all u ∈ C ∞
c (V, L ⊗ Ω 0,q). Applying the Morrey–Kohn–H¨ ormander identity ( 2.4) to the
left hand side, it suﬃces to show the following pointwise curvature es timate
⟨u, Λ iΘ( L ⊗ Ω 0,q)u⟩ − ⟨u, Λ iΘ( L)u⟩ ≥ |u|2. (2.16)
9

Expanding Θ( L ⊗ Ω 0,q) = Θ( L) ⊗ idΩ 0,q +idL ⊗ Θ(Ω 0,q), it suﬃces to show that
⟨u, Λ i(Θ( L) ⊗ id)u⟩ − ⟨u, Λ iΘ( L)u⟩ ≥ (1 + |Λ | |Θ(Ω 0,q)|)|u|2. (2.17)
We remark for clarity that the ﬁrst composition is of maps L⊗Ω 0,q ⇄ L⊗Ω 0,q ⊗Ω 1,1 and the
second composition is of maps L⊗Ω 0,q ⇄ L⊗Ω 1,q+1. Let α1, . . . , αn denote the scaling factors
associated to a simultaneous diagonalization of g and gφ, meaning that |vi|2
gφ = αi|vi|2
g for a
simultaneous orthogonal basis v1, . . . , vn. We may now calculate (see Voisin [
Voi02, Lemma
6.19])
Λ i(Θ( L) ⊗ id)u =
( n∑
i=1
αi
)
u. (2.18)
The operator Λ iΘ( L) has an orthonormal basis of eigenvectors with eigenvalues ∑
i∈I αi for
all I ⊆ { 1, . . . , n} with |I| = n − q. Thus to ensure ( 2.17), it suﬃces to have q min αi ≥
1 + |Λ | |Θ(Ω 0,q)|, which can be achieved by choosing c = 1 + |Λ | |Θ(Ω 0,q)| since q > 0.
Lemma 2.6. Let φ : ( Cn, 0) → R be a germ of a smooth J-convex function. For all ǫ > 0,
there exists a germ of a holomorphic function u : (Cn, 0) → C satisfying
⏐
⏐
⏐
⏐Re u(z) −
[
φ(z) − 1
2 dφ(z, 0)2
] ⏐
⏐
⏐
⏐ ≤ ǫ · dφ(z, 0)2 (2.19)
in a neighborhood of zero.
Proof. The statement depends only on φ up to second order, so we may assume without
loss of generality that φ is a real degree two polynomial on Cn. Any real polynomial on Cn
may be expressed uniquely as a polynomial in zi and ¯zi with coeﬃcients ci1,...,ik,¯i1,...,¯iℓ ∈ C
satisfying ci1,...,ik,¯i1,...,¯iℓ =
ci1,...,iℓ,¯i1,...,¯ik,. In the case of degree two, we thus have
φ(z) = a +
∑
i
Re aizi +
∑
i,j
Re aijzizj +
∑
i,j
bijzi ¯zj (2.20)
where a ∈ R, ai, aij, bij ∈ C, and bij = bji. The statement is also unaﬀected by adding the
real part of a holomorphic function to φ, so we may assume that a = ai = aij = 0. Finally,
the statement is unaﬀected by precomposing φ with a germ of biholomorphism of Cn near
zero, so we may apply an element of GL n(C) so that the positive deﬁnite Hermitian matrix
(bij) becomes the identity matrix. Hence we have without loss of genera lity that φ(z) = |z|2,
for which we may take u ≡ 0.
3 Donaldson’s construction
We now prove Theorem
1.7.
Let us begin by ﬁxing some notation/terminology. We ﬁx a Stein manifo ld V and a
smooth exhausting J-convex function φ : V → R. We let V := {φ ≤ 0}, so ∂V = {φ = 0 }.
We denote by g := gφ the induced metric on V , with associated distance function d := dφ.
We denote by L := Lφ the associated line bundle. For any positive real number k, we let
gk := gkφ = kg, dk := dkφ = k1/2d, and Lk := Lkφ.
10

In what follows, we treat k as a ﬁxed real parameter, and most statements (in particular,
the notations O(·) and o(·)) are meant in the limit k → ∞ (i.e. for k suﬃciently large). Most
implied constants are independent of ( V , φ) (unless stated otherwise), however how large k
must be may (and almost always will) depend on ( V , φ).
Near any point p0 ∈ V , there exists a holomorphic coordinate chart Ψ : ( U, 0) → (V , p0),
where U ⊆ Cn is an open subset containing zero, and a holomorphic function u : Ψ( U) → C,
satisfying:
• B(r) ⊆ U for r−1 = O(1).
• Ψ ∗φ = a Re z1 + O(|z|2) if p0 ∈ ∂V , where a = |dφ(p0)|.
• Ψ ∗g = gCn + O(|z|).
• φ(p) − 3
4d(p, p0)2 ≤ Re u(p) ≤ φ(p) − 1
4d(p, p0)2.
(for the existence of u, we appeal to Lemma 2.6). There exists such a triple ( U, Ψ , u) for
which the implied constants above are bounded as p0 varies over any compact subset of V .
It is convenient to also have at our disposal the rescaled coordinat es Ψ k : (B(2), 0) → (V , p0)
deﬁned by Ψ k(·) = Ψ( k−1/2·) and the rescaled function ku (for suﬃciently large k), which
satisfy:
• Ψ ∗
kφ = ak−1/2 Re z1 + O(k−1|z|2) if p0 ∈ ∂V , where a = |dφ(p0)|.
• Ψ ∗
kgk = gCn + O(k−1/2|z|).
• kφ(p) − 3
4dk(p, p0)2 ≤ Re ku(p) ≤ kφ(p) − 1
4 dk(p, p0)2.
Now the section σ := e
1
2 ku of Lk satisﬁes
e− 3
8 dk(p,p0)2
≤ |σ(p)| ≤ e− 1
8 dk(p,p0)2
(3.1)
over its domain of deﬁnition Ψ( U). This “reference section” provides a convenient local
holomorphic trivialization of Lk over Ψ k(B(2)). We also need holomorphic sections of Lk
deﬁned on all of V which satisfy a decay bound similar to ( 3.1) over {φ ≤ 1} and which
approximate σ over Ψ k(B(2)). That such sections exist is the content of the following lemma.
Lemma 3.1. Let (V , φ) be as above. Fix p0 ∈ { φ = 0 } and consider the associated coor-
dinates Ψ and reference section σ as above. There are holomorphic sections ˜σ, ˜σ1, . . . ,˜σn :
V → Lk satisfying:
• | ˜σ(p)| ≤ e− 1
9 dk(p,p0)2
+ e−ǫk over {φ ≤ 1}.
• | ˜σr(p)| ≤ e− 1
9 dk(p,p0)2
+ e−ǫk over {φ ≤ 1} for r = 1, . . . , n.
•
⏐
⏐˜σ
σ ◦ Ψ k − 1
⏐
⏐ ≤ e−ǫk over B(2).
•
⏐
⏐˜σr
σ ◦ Ψ k − zr
⏐
⏐ ≤ e−ǫk over B(2) for r = 1, . . . , n.
for some ǫ > 0 depending on (
V , φ) and suﬃciently large k.
11

Proof. Fix a smooth cutoﬀ function β : V → [0, 1] supported inside Ψ( U) which equals 1 in
a neighborhood of p0. Now ‖d′′(βσ)‖2 ≤ e−ǫk in the ﬁxed metric g for suﬃciently large k
and some ǫ > 0 depending on ( V , φ).
Fix a smooth exhausting J-convex function φ1 : V → R which coincides with φ over
{φ ≤ 2} and for which gkφ1 ≥ c · g for suﬃciently large k (for c as in Proposition 2.5). We
apply Proposition 2.5 to (V , g, kφ1) and conclude that there exists a section ξ of Lk for which
βσ + ξ is holomorphic and ‖e
1
2 k·(φ−φ1)ξ‖2 ≤ ‖d′′(βσ)‖2 ≤ e−ǫk.
Let us now show that ˜ σ := βσ + ξ satisﬁes the desired properties. Over the set where
β = 1, the section ξ is holomorphic. In particular, the function ξ
σ ◦ Ψ k is holomorphic
over B(3) (for suﬃciently large k). We have ‖ ξ
σ ◦ Ψ k‖B(3),2 ≤ e−ǫk, from which it follows
that | ξ
σ ◦ Ψ k| ≤ e−ǫk over B(2) (for a possibly smaller ǫ > 0 and larger k) since ξ
σ ◦ Ψ k is
holomorphic. Thus we have
⏐
⏐˜σ
σ ◦ Ψ k − 1
⏐
⏐ ≤ e−ǫk over B(2).
Now let p ∈ { φ ≤ 1} and consider the associated coordinates Ψ ′ and reference section
σ′ as above. We have ‖ ˜σ
σ′ ◦ Ψ ′
k‖B(3),2 = O(e− 1
8 dk(p,p0)2
+ e−ǫk), from which it follows that
|˜σ(p)| = O(e− 1
8 dk(p,p0)2
+ e−ǫk) (since ˜σ
σ′ ◦ Ψ ′
k is holomorphic), which gives the desired decay
bound on ˜σ.
The argument for {˜σr}1≤r≤n is identical, with ( zr ◦ Ψ −1
k ) · σ in place of σ.
It is helpful to rephrase Theorem 1.7 as follows in terms of the line bundle Lk and the
rescaled metric gk on V .
Theorem 3.2. Let V be a Stein manifold, equipped with a smooth exhausting J-convex
function φ : V → R. For every suﬃciently large real number k, there exists a holomorphic
section s : V → Lk such that:
• | s(p)| ≤ 1 for p ∈ {φ ≤ 1}.
• | s(p)| + |ds(p)|ξ| > η for p ∈ {φ = 0} (ds measured in the metric induced by kφ).
where ξ denotes the Levi distribution on {φ = 0 } ⊆ V , and η > 0 is a constant depending
only on the dimension of V .
Proof. The proof follows Donaldson [ Don96, §3], as simpliﬁed by Auroux [ Aur02].
Part I. Fix a maximal collection of points p1, . . . , pN ∈ ∂V whose pairwise dk-distances
are ≥ 1. Since this collection is maximal, the unit dk-balls Bi centered at the pi’s cover ∂V .
The dk-balls of radius 1 /2 centered at the pi’s are disjoint, so by volume considerations, the
total number of points satisﬁes N = O(V ,φ)(k2n−1), where n is the complex dimension of V .
We now specify the form of the section s : V → Lk we will construct. For each pi, we
will deﬁne a holomorphic section si : V → Lk satisfying the bound
|si(p)| ≤ e− 1
9 dk(p,pi)2
+ e−ǫk for p ∈ {φ ≤ 1} (3.2)
(for some ǫ > 0 depending on ( V , φ)) and we will let
s :=
N∑
i=1
si. (3.3)
12

Let us observe immediately that this bound on |si| implies that
|s(p)| ≤
N∑
i=1
e− 1
9 dk(p,pi)2
+ e−ǫk ≈
∫
∂V
e− 1
9 dk(p,p0)2
dgk(p0) + O(V ,φ)(k2n−1e−ǫk) = O(1)
for p ∈ { φ ≤ 1}. In particular, this ensures the ﬁrst condition |s(p)| ≤ 1 (after dividing by
a constant factor depending only on n = dim V ).
Remark 3.3 ( C 0-bounds imply C ∞-bounds for holomorphic functions) . For a holomorphic
function f deﬁned on B(1 + ǫ) ⊆ Cn, we have
‖f ‖Cℓ(B(1)) ≤ cn,ℓ
(
1 + 1
ǫℓ
)
‖f ‖C0(B(1+ǫ)). (3.4)
(Indeed, we have |Dℓf (0)| ≤ cn,ℓ supB(1) f by the Cauchy integral formula, and applying this
to balls of radius ǫ > 0 along with the maximum principle yields the above estimate).
For simplicity of notation, we have stated the upper bounds in ( 3.1), Lemma 3.1, ( 3.2),
and (3.5) below only in the C 0-norm, though of course we will often need to use the resulting
bounds on higher derivatives implied by ( 3.4). If we were working in the approximately
holomorphic setting, we would need to explicitly bound the higher deriv atives up to some
appropriate ﬁxed ﬁnite order.
Deﬁnition 3.4. A section s : V → Lk will be called η-transverse at p ∈ ∂V iﬀ |s(p)| +
|ds(p)|ξ| > η . The property of being η-transverse is obviously stable under C 1-perturbation,
and for holomorphic sections it is in fact stable under C 0-perturbation by (
3.4) with ℓ = 1
as long as the perturbation is deﬁned in a ﬁxed neighborhood of p.
Remark 3.5. This particular quantitative transversality condition was ﬁrst cons idered by
Mohsen [ Moh13], and is closely related to those used by Donaldson and Auroux. Dona ldson
[Don96] called a section s : V → Lk η-transverse at p iﬀ either |s(p)| ≥ η or |ds(p)| ≥ η (this is
equivalent, up to a constant, to requiring |s(p)| + |ds(p)| ≥ η). Mohsen [ Moh13] generalized
this notion to quantitative transversality relative to a given subman ifold Y . Speciﬁcally,
he called a section η-transverse relative to Y iﬀ either |s(p)| ≥ η or ds(p)|T Y has a right
inverse of norm ≤ η−1. In the case of the submanifold ∂V ⊆ V and an (approximately)
holomorphic section s, this condition is equivalent, up to a constant, to our formulation
|s(p)| + |ds(p)|ξ| > η (see [Moh13, §2]). Thus, Theorem 3.2 can be regarded as a holomorphic
version of Mohsen’s transversality theorem for hypersurfaces.
Part II. Our goal is to construct sections si satisfying the decay bound ( 3.2) so that s
is η-transverse over ∂V for some η > 0 depending only on n.
We will deﬁne the sections si in a series of steps, at each step achieving (quantitative)
transversality over some new part of ∂V , while maintaining (quantitative) transversality over
the part of ∂V already dealt with. The most naive version of this procedure, choos ing si to
achieve transversality over Bi while maintaining transversality over B1, . . . , Bi−1, runs into
trouble, essentially due to the rather large number of steps. Inst ead, we ﬁrst construct a
suitable coloring of the pi’s, and then in the inductive procedure we choose the si’s for the
pi’s of a particular color simultaneously (so there is one step per color) . For this to work, we
must ensure that points of the same color are suﬃciently far apart .
13

Let D < ∞ be a (large) positive real number, to be ﬁxed (depending only on n) at the end
of the proof. We color the pi’s so that the dk-distance between any pair of points of the same
color is at least D. More precisely, we construct such a coloring by iteratively choosin g a
maximal collection of yet uncolored points pi with pairwise distances ≥ D and then coloring
this collection with a new color. Because each color was chosen from a maximal collection
of yet uncolored points, it follows that the ball of radius D centered at any point colored
with the ﬁnal color contains points of every other color. Hence by v olume considerations, it
follows that the total number of colors M is O(D2n−1). Let us denote the coloring function
by c : {1, . . . , N} → { 1, . . . , M}.
Part III. Let p < ∞ and A < ∞ be (large) positive real numbers, to be ﬁxed (depending
only on n) later in the proof. To be precise, we must ﬁrst choose A (depending on n), then
choose p (depending on n and A), and ﬁnally choose D (depending on n, A, and p).
It suﬃces to construct sections si so that:
• For all j ∈ {1, . . . , M} and c(i) = j, we have
|si(p)| ≤ 1
Aηj−1
[
e− 1
9 dk(p,pi)2
+ e−ǫk
]
for p ∈ {φ ≤ 1}. (3.5)
• For all j ∈ {1, . . . , M}, we have
sj :=
N∑
i=1
c(i)≤j
si is ηj-transverse over Xj :=
N⋃
i=1
c(i)≤j
Bi. (3.6)
Here 1
4 = η0 > η 1 > · · · > η M > 0 are deﬁned by ηj = ηj−1 |log ηj−1|−p (the reason for this
particular choice will become apparent later).
We construct such sections si by induction on j. More precisely, it suﬃces to suppose
that sections si are given for c(i) ≤ j − 1 (satisfying the above in the range {1, . . . , j − 1})
and to construct sections si for c(i) = j (satisfying the above in the range {1, . . . , j}).
Part IV. As a ﬁrst step, let us ﬁx an index i with c(i) = j, and construct a section
si satisfying ( 3.5) so that sj−1 + si is ηj−1 |log ηj−1|−p-transverse over Bi (for some p < ∞
depending on n and A).
Fix a triple ( U, Ψ , u) based at pi ∈ ∂V (as discussed at the beginning of this section),
with rescaling Ψ k and reference section σ = e
1
2 ku. We will use the local coordinates Ψ k and
the reference section σ to measure the transversality of sj−1 + si over Bi. Precisely, we claim
that it suﬃces to construct si satisfying ( 3.5) so that
sj−1 + si
σ ◦ Ψ k (3.7)
is ηj−1 |log ηj−1|−p-transverse over B(3/2) ∩Ψ −1
k (∂V ). Indeed, σ is bounded above and below
by ( 3.1), so using ( 3.4) with ℓ = 1 this implies that sj−1 + si is 1
C ηj−1 |log ηj−1|−p-transverse
over Bi for some constant C < ∞ depending only on n (which we can absorb into the last
factor by increasing p).
Now as k → ∞, the real hypersurface B(3/2)∩Ψ −1
k (∂V ) approaches B(3/2)∩{Re z1 = 0}
in C ∞, uniformly over the choice of pi ∈ ∂V . Since ( 3.7) is bounded uniformly over B(2),
14

using (3.4) with ℓ = 2 we see that η-transversality over B(3/2)∩{Re z1 = 0} implies (η−o(1))-
transversality over B(3/2) ∩ Ψ −1
k (∂V ) (of course, the condition of η-transversality over a real
hypersurface is with respect to its own Levi distribution). Since th e number of colors M
is bounded independently of k, it follows that ηj−1 is bounded away from zero as k → ∞ .
Hence it suﬃces to show that ( 3.7) is ηj−1 |log ηj−1|−p-transverse over B(3/2) ∩ {Re z1 = 0}
(we again lose a constant on the transversality estimate, but as be fore it can be absorbed
into the exponent p).
For any vector w = (w0, w2, . . . , wn) ∈ Cn, we consider the holomorphic function on B(2)
given by
sj−1
σ ◦ Ψ k + w0 + w2z2 + · · · + wnzn. (3.8)
A quantitative transversality theorem, Proposition 4.1 (whose proof we defer to later) says
that for 1
3 > η > 0, there exists a vector w = ( w0, w2, . . . , wn) ∈ Cn with |w| ≤ η so that
(3.8) is η |log η|−p-transverse over B(3/2) ∩ {Re z1 = 0} (for some p < ∞ depending only on
n). This fact that with a perturbation of size η we can achieve η |log η|−p-transversality is
what forces the choice of recursion ηj = ηj−1 |log ηj−1|−p declared above.
Let ˜σ and {˜σr}1≤r≤n denote the “peak sections” based at p0 = pi from Lemma 3.1. We
deﬁne si := w0˜σ + w2˜σ2 + . . . + wn˜σn (for w to be determined), so now ( 3.7) equals
sj−1
σ ◦ Ψ k + w0
˜σ
σ ◦ Ψ k + w2
˜σ2
σ ◦ Ψ k + · · · + wn
˜σn
σ ◦ Ψ k. (3.9)
There is a constant C < ∞ (depending only on n) such that for |w| ≤ 1
A·C ηj−1, the section
si satisﬁes the decay bound ( 3.5). By Proposition 4.1, there exists |w| ≤ 1
A·C ηj−1 for which
(3.8) is ηj−1 |log ηj−1|−p-transverse over B(3/2) ∩ { Re z1 = 0 } (absorbing constants into
p). It follows that ( 3.9) (and hence ( 3.7)) is ( ηj−1 |log ηj−1|−p − O(e−ǫk))-transverse over
B(3/2) ∩ {Re z1 = 0}, which is enough.
Part V. We have constructed sections si for c(i) = j with the property that sj−1 + si
is ηj−1 |log ηj−1|−p-transverse over Bi (for some p < ∞ depending on n and A). Now let us
argue that with this choice of sections, sj is ηj-transverse over Xj (for some possibly diﬀerent
p < ∞ depending on n and A).
We know that sj diﬀers from sj−1 over Xj−1 by O( 1
Aηj−1) and that sj−1 is ηj−1-transverse
over Xj−1. It follows that sj is (1 − O( 1
A))ηj−1-transverse over Xj−1, which gives ηj-
transversality over Xj−1 once A and p are large.
We know that sj diﬀers from sj−1 + si over Bi by O(ηj−1e− 1
9 D2
) and that sj−1 + si is
ηj−1 |log ηj−1|−p-transverse over Bi. It follows that sj is ( ηj−1 |log ηj−1|−p − O(ηj−1e− 1
9 D2
))-
transverse over Bi. This gives ηj-transversality over Bi (increasing p to make up for the lost
constant factor) as long as we have
e− 1
9 D2
≤ 1
B |log ηj−1|−p (3.10)
for some constant B < ∞ depending only on n.
Hence we conclude that the entire construction succeeds as long a s ( 3.10) holds for
j = 1 , . . . , M. It is elementary to observe that the recursive deﬁnition of ηj yields rough
15

asymptotics ηj ≈ e−c·j log j (c depending on p). Thus it suﬃces to ensure that
e− 1
9 D2
≤ 1
B′ (M log M)−p (3.11)
for some B′ < ∞ depending on n and p. We observed earlier that M = O(D2n−1), so this
inequality is satisﬁed once D is suﬃciently large.
Remark 3.6. A common theme in h-principle arguments ` a la Gromov, in which we want to
construct some structure globally on a given manifold X, is to extend the desired structure
to larger and larger subsets · · · ⊆ Xj−1 ⊆ Xj ⊆ · · · in a series of steps. This reduces
the desired result to an extension problem from Xj−1 to Xj (see for example Eliashberg–
Mishachev [ EM02]). For example, Xj is usually taken to be (an open neighborhood of)
the j-skeleton of X (under a ﬁxed triangulation), the point being that now the topology
governing the extension from Xj−1 to Xj is easy to understand. Donaldson’s method, used
in the proof above, employs a similar inductive procedure, but where one instead controls
the geometry governing the extension from Xj−1 to Xj (the key point being that we can do
local modiﬁcations independently at any collection of points which are suﬃciently far away
from each other).
4 Quantitative transversality theorem
We now prove the quantitative transversality theorem (Propositio n
4.1) which was the key
technical ingredient in Donaldson’s construction as used in the proo f of Theorem 3.2. The
statement and proof are similar to Auroux [ Aur00, §2.3]; see also [ Aur02]. A key ingredient
is an upper bound on the volume of tubular neighborhoods of real alg ebraic sets (Lemma
4.4) due to Wongkew [ Won93].
Proposition 4.1. Let B(1) ⊆ B(1+ ǫ) ⊆ Cn be the balls centered at zero. Fix a holomorphic
function f : B(1 + ǫ) → C with |f | ≤ 1. For a vector w = (w0, w2, . . . , wn) ∈ Cn, we deﬁne
fw := f + w0 + w2z2 + · · · + wnzn. (4.1)
For all 1/3 > η > 0, there exists a vector w ∈ Cn satisfying |w| ≤ η |log η|p such that:
• | fw(z)| + |d fw(z)|ξ| > η for z ∈ B(1) with Re z1 = 0.
where ξ denotes the Levi distribution of {z ∈ B(1) : Re z1 = 0}, and p < ∞ depends only on
the dimension n and ǫ > 0.
Remark 4.2. A stronger version of Proposition 4.1 (a true quantitative Sard theorem where
we only perturb f by a constant, i.e. w2 = · · · = wn = 0 above) is due to Donaldson
[Don96, Don99] and Mohsen [ Moh13] with a rather more diﬃcult proof. Mohsen’s result
could be used in §3 in place of Proposition 4.1, resulting in a simpler deﬁnition si := w0˜σ,
eliminating the need for the remaining ˜ σ2, . . . ,˜σn. We have chosen instead to present the
argument following Auroux’s observation that the weaker Proposit ion 4.1, whose proof is
more elementary, is suﬃcient for the argument in §3.
16

Proof. For a given z ∈ B(1) with Re z1 = 0, the quantity |fw(z)| + |d fw(z)|ξ| vanishes for
exactly one value of w. The function F : {z ∈ B(1) : Re z1 = 0 } → Cn which associates
to a given z this unique w is the restriction of a holomorphic function F : B(1 + ǫ) → Cn.
Explicitly
F (z) =
(
−f + z2
∂f
∂z2
+ · · · + zn
∂f
∂zn
, − ∂f
∂z2
, . . . ,− ∂f
∂zn
)
. (4.2)
In fact, the quantity |fw(z)| + |d fw(z)|ξ| is bounded below by (a constant depending only
on n, times) the distance from w to F (z). Hence it suﬃces to show that B(δ) \ Nη(F ({z ∈
B(1) : Re z1 = 0})) is nonempty for δ = η |log η|O(1).
We may approximate F to within error ≤ η on B(1) by a polynomial ˜F of degree
O(|log η|). Indeed, the error in the degree m Taylor approximation of F is exponentially
small in m, uniformly over B(1), since F is holomorphic and bounded eﬀectively on B(1 + ǫ
2)
by ( 3.4) with ℓ = 1. To see this, observe that (by the U(n) symmetry) it is enough to prove
an eﬀective exponential upper bound on the error over B(1) ∩ (C × {0}n−1), and this is just
the well-known single-variable case (proved using the Cauchy integr al formula).
It thus suﬃces to show that B(δ) \ N2η( ˜F ({z ∈ B(1) : Re z1 = 0 })) is nonempty for
δ = η |log η|O(1). Since ˜F is a polynomial of degree O(|log η|), a pigeonhole principle argument
(Lemma 4.3 below) implies that its image is contained in a real algebraic hypersurfa ce
X ⊆ Cn of degree ≤ | log η|O(1). Hence it suﬃces to show that B(δ) \ N2η(X) is nonempty
for δ = η |log η|O(1) and any real hypersurface X ⊆ Cn of degree ≤ |log η|O(1).
Wongkew’s estimate [Won93] (Lemma 4.4 below) on the volume of a tubular neighbor-
hood of a real algebraic variety gives
vol2n(N2η(X) ∩ B(δ)) = δ2n · O
(η
δ |log η|O(1)
)
. (4.3)
For δ = η |log η|O(1), this is less than the total volume of B(δ), which is enough.
Lemma 4.3 (Auroux [ Aur00, p565]) . Let F : Rn → Rm be a real polynomial map of degree
≤ d where n < m . Then the image of F is contained in a real algebraic hypersurface of
degree D ≤
⌈
( m!
n! dn)1/(m−n)⌉
.
Proof. The space of real polynomials G of degree ≤ D on Rm has dimension
(m+D
m
)
. The
composition G◦F has degree ≤ dD. Hence there exists a nonzero G for which the composition
is zero provided
(m+D
m
)
>
(n+dD
n
)
, or equivalently (D+1)···(D+m)
(dD+1)···(dD+n) > m!
n! . The left hand side is
bounded below by Dm
(dD)n , and so there exists a suitable G as long as Dm−n ≥ m!
n! dn.
Lemma 4.4 (Wongkew [Won93]). Let X ⊆ Rn be a real algebraic variety of codimension m
deﬁned by polynomials of degree ≤ d. Then we have the following estimate
voln(Nǫ(X) ∩ [0, 1]n) = O((ǫd)m) (4.4)
where the implied constant depends only on n.
It can be seen via simple examples that this bound is sharp, up to the im plied constant.
For completeness, we reproduce Wongkew’s argument below.
17

Proof. We proceed by induction on n, the case n = 0 being clear. All implied constants
depend only on n. We assume for convenience that ǫ ≤ 1 (otherwise the desired estimate is
clear).
Let H be the collection of hyperplanes H ⊆ Rn given by constraining any one of the
coordinates to lie in [ −2ǫ, 1 + 2 ǫ] ∩ (ǫZ + δ), where δ is chosen so that X intersects each
H ∈ H properly (i.e. X ∩ H has codimension m inside H). Such a δ exists by Bertini’s
theorem. Clearly # H = O(ǫ−1). This set of hyperplanes partitions Rn into some unbounded
components and some cubes of side length ǫ. We denote the set of such cubes by C.
We call a cube C ∈ C exceptional iﬀ X intersects the interior of C but not its boundary.
The number of exceptional cubes is clearly bounded by dim H0(X), which by a result of
Milnor [ Mil64] is bounded by d(2d − 1)n−1 = O(dn).
It is straightforward to check that
Nǫ(X) ∩ [0, 1]n ⊆
[
N(1+√n)ǫ
(
X ∩
⋃
H∈H
H
)
∩ [0, 1]n
]
∪
[ ⋃
C∈C
C exceptional
Nǫ(C)
]
. (4.5)
Indeed, suppose p ∈ [0, 1]n and d(p, X) ≤ ǫ. There exists x ∈ X with d(p, x) ≤ ǫ, and x ∈ C
for some (closed) cube C ∈ C. If C is exceptional, then p lies in the second term above.
If C is not exceptional, then X ∩ ∂C is nonempty. It thus follows that d(p, ∂C ∩ X) ≤
ǫ + d(x, ∂C ∩ X) ≤ ǫ + ǫ√n, and so p lies in the ﬁrst term above.
Now the inclusion ( 4.5) implies the following inequality on volumes
voln(Nǫ(X) ∩ [0, 1]n) ≤
∑
H∈H
2(1 + √n)ǫ voln−1(N(1+√n)ǫ(X ∩ H) ∩ H ∩ [0, 1]n)
+
∑
C∈C
C exceptional
(3ǫ)n.
If m = n, then the ﬁrst term vanishes (each X ∩ H is empty by assumption), and Milnor’s
bound on the second term gives the desired result. If m ≤ n−1, then we apply the induction
hypothesis to the ﬁrst term and Milnor’s result to the second term. The result is:
voln(Nǫ(X) ∩ [0, 1]n) = O((ǫd)m + (ǫd)n). (4.6)
This implies the desired estimate for ǫd ≤ 1, and for ǫd ≥ 1 the desired estimate is trivial.
5 Lefschetz ﬁbrations on Stein domains
We now show how the function f guaranteed to exist by Theorem
1.7 gives rise to a Lefschetz
ﬁbration. To be precise, we will show that Theorem 1.7 implies Theorem 1.6 and that
Theorem 1.6 implies Theorem 1.5.
Proof of Theorem 1.6 from Theorem 1.7. Fix an embedding֒→ V of the Stein domain V
into a Stein manifold V of the same dimension, and ﬁx an exhausting J-convex function
φ : V → R with V = {φ ≤ 0}.
By Theorem 1.7, there exists (for suﬃciently large k) a holomorphic function f : V → C
such that:
18

• | f (p)| + k−1/2|d f(p)|ξ| > η for p ∈ ∂V .
• | f (p)| ≤ e
1
2 kφ(p) for p ∈ {φ ≤ 1}.
We claim that the bound |f (p)| ≤ e
1
2 kφ(p) implies:
• | d f(p) − k · f (p) · d′φ(p)| = O(k1/2e
1
2 kφ(p)) for p ∈ V .
To see this, argue as follows. Fix a point p ∈ V and choose a holomorphic function u deﬁned
in a neighborhood of p such that Re u(q) = φ(q)+ O(d(p, q)2). It follows that f (q)·e− 1
2 ku(q) =
O(1) for d(p, q) = O(k−1/2), and hence it follows that d(f · e− 1
2 ku)(p) = O(k1/2). Expanding
the left hand side and using the fact that du(p) = 2 d′ Re u(p) = 2 d′φ(p), the claim follows.
Now we take π := η−1 · f , which satisﬁes the desired properties.
Proof of Theorem 1.5 from Theorem 1.6. By Theorem 1.6, there exists (for suﬃciently large
k), a holomorphic function π : V → C such that:
• For |π(p)| ≥ 1, we have d log π(p) = k · d′φ(p) + O(k1/2).
• For |π(p)| ≤ 1 and p ∈ ∂V , we have dπ(p)|ξ ⁄= 0.
Note that these conditions together imply that the critical locus of π is contained in the
interior of π−1(D2). Both conditions are preserved under small perturbations of π, hence we
may perturb π so that:
• All critical points of π on V are nondegenerate and have distinct critical values.
Indeed, the existence of such a perturbation follows from the sta ndard fact that global
holomorphic functions on any Stein manifold V generate OV and Ω 1
V at every point (this
follows from Cartan’s Theorems A and B, or by properly embedding V in CN ).
Now π : π−1(D2) → D2 is a Stein Lefschetz ﬁbration, so it suﬃces to construct a
deformation of Stein domains from V to π−1(D2)sm. Let g : R<0 → R satisfy g′ > 0, g′′ > 0,
and lim x→0− g(x) = ∞. Consider the family {π−1(D2
r )}1≤r<∞, and consider its smoothing
{r−3g(|π|2 − r2) + g(φ) ≤ M}1≤r<∞ for some large M < ∞. Since π−1(D2
r ) is cut out by the
inequalities φ ≤ 0 and Re log π ≤ log r, this smoothing gives the desired deformation as long
as for every point p ∈ V with |π(p)| ≥ 1, the diﬀerentials dφ(p) and Re d log π(p) are either
linearly independent or positively proportional. Since d log π(p) = k · d′φ(p) + O(k1/2), this
condition is clearly satisﬁed for suﬃciently large k.
6 Lefschetz ﬁbrations on Weinstein domains
We now show how the existence of Lefschetz ﬁbrations on Stein dom ains (Theorem
1.5) may
be used to deduce the same for Weinstein domains (Theorem 1.10). For this implication, we
use the result of Cieliebak–Eliashberg [ CE12, Theorem 1.1(a)] that every Weinstein domain
may be deformed to carry a compatible Stein structure. The main st ep (Proposition 6.2)
is thus to show that for any Stein Lefschetz ﬁbration π : V → D2, there exists an abstract
Weinstein Lefschetz ﬁbration whose total space is deformation eq uivalent to V sm.
19

6.1 From Stein structures to Weinstein structures
We give a very brief review of the relationship between Stein and Weins tein structures (for
a complete treatment, the reader may consult [
CE12, §1]). Let ( V, φ) be a pair consisting
of a Stein domain V and a smooth J-convex function φ : V → R with ∂V = {φ = 0 } as
a regular level set. If φ is Morse (which can be achieved by small perturbation), then it
induces the structure of a Weinstein domain on V , namely taking the 1-form λφ := −J ∗dφ
and the function φ itself. This Weinstein domain is denoted W(V, φ). For any deformation
of Stein domains ( Vt, φt)t∈[0,1] where every φt is generalized Morse (any {φt}t∈[0,1] may be
perturbed to satisfy this condition), the associated family W(Vt, φt)t∈[0,1] is a deformation
of Weinstein domains. In particular, the deformation class of W(V, φ) is independent of φ,
so we may denote it by W(V ). Now a decisive result is the following (we state a simpliﬁed
version which is suﬃcient for our purpose).
Theorem 6.1 (Cieliebak–Eliashberg [
CE12, Theorem 1.1(a)]) . Every deformation class of
Weinstein domain is of the form W(V ) for a Stein domain V .
6.2 From Stein Lefschetz ﬁbrations to abstract Weinstein Le f-
schetz ﬁbrations
Theorem 1.10 follows from Theorem 1.5, Theorem 6.1, and the following proposition.
Proposition 6.2. Let π : V → D2 be a Stein Lefschetz ﬁbration. There exists an abstract
Weinstein Lefschetz ﬁbration W = ( W0; L1, . . . , Lm) whose total space |W | is deformation
equivalent to W(V sm).
The abstract Weinstein Lefschetz ﬁbration associated to a Stein L efschetz ﬁbration may
be described as follows. The “central ﬁber” W0 is the Weinstein domain associated to a
regular ﬁber π−1(p) of π : V → D2, and the “vanishing cycles” L1, . . . , Lm are the images
of the critical points of π under symplectic parallel transport along a set of disjoint paths
from the critical values of π to the regular value p. Hence the content of the proposition is
that (as a Weinstein manifold) V sm may be described as a small product neighborhood of a
regular ﬁber with Weinstein handles attached along the vanishing cyc les.
We now give a detailed deﬁnition of the total space of an abstract We instein Lefschetz
ﬁbration.
Deﬁnition 6.3. Let W = (( W0, λ0, φ0); L1, . . . , Lm) be an abstract Weinstein Lefschetz
ﬁbration. Its total space |W | is deﬁned as follows. We equip W0 × C with the Liouville form
λ0 − J ∗d( 1
2|z|2) and the Morse function φ0 + |z|2 for which the resulting Liouville vector ﬁeld
Xλ0 + 1
2 (x ∂
∂x + y ∂
∂y ) is gradient-like. Fix Legendrian lifts Λ j ⊆ (W0 × S1, λ0 + N dθ) of the
exact Lagrangians Lj ⊆ W0 such that Λ j projects to a small interval around 2 πj/m ∈ S1
(here we choose N < ∞ suﬃciently large so that these intervals are disjoint). Now the
embedding S1֒→C as the circle of radius
√
N pulls back the Liouville form −J ∗d( 1
2|z|2) to
the contact form N dθ. Hence we may think of Λ j as lying inside W0 × C as a Legendrian
on the level set {|z| =
√
N }. The downward Liouville ﬂow applied to Λ j gives rise to a map
Λ j × R≥0 → W0 × C, which intersects the level set {φ0 + |z|2 = 0} in a Legendrian Λ ′
j (here
20

we choose N < ∞ so that the projection of {φ0 + |z|2 ≤ 0} to C is contained inside the disk
of radius
√
N). The total space |W | is deﬁned as the result of attaching Weinstein handles
([Wei91]) to the Weinstein domain {φ0 + |z|2 ≤ 0} along the Legendrians Λ ′
j (marked via
the maps Sn−1 → Lj
∼
− →Λ j
∼
− →Λ ′
j). It is easy to see that |W | is well-deﬁned up to canonical
deformation (we will remark in detail on the well-deﬁnedness of Weins tein handle attachment
in Lemma
6.6).
We now introduce a variant of the above construction, which will be u sed in the proof of
Proposition 6.2.
Deﬁnition 6.4. Let W = ( π : V → D2, φ, g; L1, . . . , Lm) consist of a Stein Lefschetz ﬁbra-
tion π : V → D2, a J-convex function φ : V → R with ∂hV = {φ = 0} as a regular level set,
a function g : R<0 → R with g > 0, g′ > 0, g′′ > 0, and lim x→0− g(x) = ∞, and a collection
of exact parameterized Lagrangian (with respect to λg(φ)) spheres Lj ⊆ Vpj := π−1(pj) for
distinct points p1, . . . , pm ∈ S1 = ∂D 2, ordered counterclockwise. We deﬁne its total space
|W | as follows. We consider the J-convex function ǫg(φ) + 1
2|π|2 on V . The induced contact
form on π−1(∂D 2) may be written as ǫλg(φ) + dθ. Let us center the S1-coordinate at pj ∈ S1,
rescale it by ǫ−1, and rescale the contact form by ǫ−1. In the limit ǫ → 0, this rescaling
of π−1(∂D 2) converges to the contact manifold ( Vpj × R, λg(φ) + dt). In Vpj × R, there is
a unique (up to translation) Legendrian Λ j projecting to Lj. During the deformation of
Vpj × R back to π−1(∂D 2) for small ǫ > 0, there clearly exists a simultaneous Legendrian
isotopy Λ ǫ
j ⊆ π−1(∂D 2) starting at Λ 0
j = Λ j. Now the downward Liouville ﬂow applied to Λ ǫ
j
intersects {ǫg(φ) + 1
2(|π|2 − 1) = 0 } in a Legendrian Λ ǫ′
j . The total space |W | is deﬁned as
the result of attaching Weinstein handles to the Weinstein domain {ǫg(φ) + 1
2(|π|2 − 1) ≤ 0}
along these Legendrians. This total space is independent of the ch oice of suﬃciently small
ǫ > 0 and the family {Λ ǫ
i}ǫ≥0 up to canonical deformation.
Deﬁnition
6.4 reduces to Deﬁnition 6.3 in the special case of a product ﬁbration, in the
sense that there is a canonical deformation equivalence
⏐
⏐(V0 × D2 → D2, φ0, g; L1 × {α1}, . . . , Lm × {αm})
⏐
⏐ =
⏐
⏐(W(V0, g(φ0)); L1, . . . , Lm)
⏐
⏐, (6.1)
where φ0 : V0 → R is J-convex with ∂V0 = {φ0 = 0 } as a regular level set, L1, . . . , Lm ⊆ V0
are exact parameterized Lagrangian spheres with respect to λg(φ0), and α1, . . . , αm ∈ S1 =
∂D 2 are ordered counterclockwise. The right hand side of (
6.1) is a slight abuse of notation,
as we should really write W({g(φ0) ≤ M}, g(φ0)) for suﬃciently large M.
Proof of Proposition 6.2. We assume that 0 ∈ D2 is a regular value of π and that each
critical value of π has a distinct complex argument (this may be achieved by post-comp osing
π with a generic Schwarz biholomorphism D2 → D2).
Fix a smooth J-convex function φ : V → R with ∂hV = {φ = 0 } as a regular level set
(as is guaranteed to exist by Deﬁnition 1.4). We let V0 := π−1(0) denote the central ﬁber,
and we assume that φ0 := φ|V0 is Morse (this can be achieved by a small perturbation of φ).
By Lemma 6.5 below, there exists a smooth function g : R<0 → R satisfying g > 0, g′ > 0,
g′′ > 0, and lim x→0− g(x) = ∞, such that the symplectic connection on π : V \ ∂hV → D2
induced by ωg(φ) is complete. Fix one such g.
21

We consider parallel transport along radial paths in D2 with respect to the symplectic
connection induced by ωg(φ). Under this parallel transport, each critical point of π sweeps
out a Lagrangian disk called a Lefschetz thimble (to see this, apply the stable manifold
theorem to the Hamiltonian vector ﬁeld XIm log π, and recall that the critical values of π
have distinct complex arguments). The ﬁber over 0 ∈ D2 of a Lefschetz thimble is an exact
Lagrangian sphere called a vanishing cycle . Let L1, . . . , Lm ⊆ V0 denote the vanishing cycles
of all the critical points of π, ordered by angle. As stable manifolds of the vector ﬁeld
XIm log π, they come equipped with parameterizations Sn−1 → Lj, which are well-deﬁned in
Diﬀ( Sn−1, Lj)/O(n) up to contractible choice.
Now W := ( W(V0, g(φ0)); L1, . . . , Lm) is an abstract Weinstein Lefschetz ﬁbration, and
it remains to show that its total space |W | is deformation equivalent to W(V sm).
We consider the J-convex function ǫg(φ) + h( |π|
δ ) on V \ ∂hV for small ǫ, δ > 0, where
h(r) :=
{
log r r ≥ 1
1
2 (r2 − 1) r ≤ 1. (6.2)
We claim that for ( ǫ, δ) → (0, 0), the sublevel set
{
ǫg(φ) + h
(|π|
δ
)
≤ log 1
δ
}
⊆ V (6.3)
is deformation equivalent to V sm. Indeed, consider the ≤ log 1
δ sublevel set of the linear in-
terpolation between ǫg(φ) + h( |π|
δ ) and ǫg(φ) + ǫg(|π|2 − 1). As ( ǫ, δ) → (0, 0), the boundary
of this deformation stays arbitrarily close to ∂V , and the critical locus of the linear interpo-
lation stays away from ∂V (note that this critical locus is always contained in the ﬁberwise
critical locus of φ). Thus ( 6.3) is deformation equivalent to V sm as claimed.
As ( ǫ, δ) → (0, 0), the critical points of ǫg(φ) + h( |π|
δ ) over D2 \ D2
δ are in bijective
correspondence with crit( π) (note that the critical locus is contained in the ﬁberwise critical
locus of φ). Over D2 \D2
δ , the stable manifolds of these critical points approach the Lefsch etz
thimbles as ǫ → 0 and δ > 0 is ﬁxed. Indeed, h is harmonic over D2 \ D2
δ , and hence the
Liouville vector ﬁeld of ǫg(φ) + h( |π|
δ ) is given by Xg(φ) + ǫ−1XIm log π over D2 \ D2
δ , where
Xg(φ) is the Liouville vector ﬁeld of g(φ) and XIm log π is the Hamiltonian vector ﬁeld with
respect to ωg(φ) of Im log π.
Let us denote by ¯Λ ǫ,δ
j ⊆ π−1(∂D 2
δ ) the intersections of the stable manifolds of ǫg(φ)+h( |π|
δ )
with π−1(∂D 2
δ ). Thus ¯Λ ǫ,δ
j is Legendrian with respect to the contact form ǫλg(φ) + dθ. Denote
by Lδ
j the intersections of the Lefschetz thimbles with π−1(∂D 2
δ ). Thus as ǫ → 0 and δ > 0
is ﬁxed, we have ¯Λ ǫ,δ
j → Lδ
j in C ∞. Now we claim that ¯Λ ǫ,δ
j is in fact (Legendrian isotopic
to) the Legendrian lift Λ ǫ,δ
j of Lδ
j (as in Deﬁnition
6.4) for suﬃciently small ǫ > 0. In the
rescaled limit as ǫ → 0, the projection of ¯Λ ǫ,δ
j to Vpj approaches Lδ
j in C ∞, and this is enough
to show that it converges (up to translation) to Λ 0,δ
j as ǫ → 0. Hence the claim is valid, so
we conclude that W(V sm) is deformation equivalent to
⏐
⏐(π : π−1(D2
δ ) → D2
δ ; Lδ
1, . . . , Lδ
m)
⏐
⏐. (6.4)
We have used Lemma
6.6 below to show that the Weinstein cobordism {0 ≤ ǫg(φ) +h( |π|
δ ) ≤
log 1
δ } is a Weinstein handle attachment.
22

In the limit δ → 0, rescaling D2
δ to D2, clearly ( 6.4) converges to
⏐
⏐(V0 × D2 → D2; L1 × {α1}, . . . , Lm × {αm})
⏐
⏐ (6.5)
where αj ∈ S1 = ∂D 2 are the angles of the critical points of π. Hence using (
6.1), we have
shown the desired deformation equivalence between W(V sm) and |(W(V0, g(φ0)); L1, . . . , Lm)|.
Lemma 6.5. Let π : V → D2 be a Stein Lefschetz ﬁbration, and let φ : V → R be J-convex
with ∂hV = {φ = 0 } as a regular level set. There exists a smooth function g : R<0 → R
satisfying g′ > 0, g′′ > 0, and limx→0− g(x) = ∞, such that the symplectic connection on
π : V \ ∂hV → D2 induced by ωg(φ) is complete, in the sense that parallel transport along a
smooth path in the base D2 gives rise to a diﬀeomorphism between the corresponding ﬁbe rs
(away from the critical points of π).
Proof. We will in fact show that there exists a natural contractible family of functions g
which satisfy the desired conclusion for all ( V, φ).
Let g : R<0 → R satisfy g′ > 0, g′′ > 0, and lim x→0− g(x) = ∞. Let ⊥φ (resp. ⊥g(φ))
denote orthogonal complement with respect to ωφ (resp. ωg(φ)), so the horizontal distribution
of the symplectic connection induced by ωg(φ) is (ker dπ)⊥g(φ).
Our ﬁrst goal is to show that in a neighborhood of ∂hV , every horizontal vector ﬁeld X
satisﬁes
|Xφ| = O
( g′(φ)
g′′(φ)
)
· |π∗X| (6.6)
as long as g′(φ)
g′′(φ) is suﬃciently small. Note that in a neighborhood of ∂hV , there is a direct
sum decomposition
T V = (ker dπ ∩ ker d′φ) ⊕ (ker dπ ∩ ker d′φ)⊥φ ∩ ker dπ
⊕ (ker dπ ∩ ker d′φ)⊥φ ∩ ker d′φ (6.7)
into subspaces of real dimension 2 n − 4, 2, 2, respectively. Now suppose that X = X1 ⊕
X2 ⊕ X3 ∈ T V is horizontal, i.e. X ⊥g(φ) ker dπ. Note the explicit form
ωg(φ) = g′(φ) · ωφ + g′′(φ) · id′φ ∧ d′′φ. (6.8)
We may choose a vector v ∈ (ker dπ ∩ ker d′φ)⊥φ ∩ ker dπ with |v|gφ = 1 such that |(id′φ ∧
d′′φ)(v, X2)| ≍ | X2|gφ (where gφ denotes the metric induced by φ). Now since v ∈ ker dπ, it
pairs to zero with X under ωg(φ), so we have
0 = g′(φ) · ωφ(v, X2 + X3) + g′′(φ) · (id′φ ∧ d′′φ)(v, X2) (6.9)
It follows from this that |X2|gφ = O
(g′(φ)
g′′(φ)
)
· |X3|gφ for g′(φ)
g′′(φ) suﬃciently small. This implies
the desired estimate ( 6.6) since |π∗X| ≍ | X3|gφ and |Xφ| ≍ | X2|gφ.
It now follows that the connection is complete as long as
lim sup
x→0−
g′(x)
|x|g′′(x) < ∞. (6.10)
23

Indeed, by ( 6.6) this condition guarantees that the derivative of log( −φ) is bounded along
the horizontal lift of a smooth curve in the base D2.
We now just need to exhibit a function g : R<0 → R satisfying g′ > 0, g′′ > 0,
limx→0− g(x) = ∞, and ( 6.10), which we may write as
lim inf
x→0−
(log g′(x))′|x| > 0. (6.11)
For example, we may take
g(x) :=
∫ x
−∞
e−t2−t−1
dt. (6.12)
Moreover, the space of such functions is contractible, since the m ap g ↦→(g(−1), log g′) gives
a bijection with a convex set.
6.3 Uniqueness of Weinstein handle attachment
We record here a proof of the fact that an elementary Weinstein co bordism is “the same” as a
Weinstein handle attachment (the precise statement is Lemma
6.6), as was used in the proof
of Proposition 6.2. We were unable to ﬁnd a precise reference for this standard fact , though it
is of course implicit in Weinstein’s original paper [ Wei91], as well as in Cieliebak–Eliashberg
[CE12].
Recall that a Weinstein cobordism ( W, λ, φ) is called elementary iﬀ there is no trajectory
of X = Xλ between any two critical points. For a critical point p ∈ W , we denote by
T ±
p W the positive/negative eigenspaces of dpX : TpW → TpW , and we denote the stable
manifold by W −
p . For an elementary cobordism, each stable manifold W −
p intersects the
negative boundary ∂−W in an isotropic sphere Λ p ⊆ ∂−W ; note that Λ p = ( W −
p \ p)/R via
the Liouville ﬂow. A choice of exponential coordinates exp p : T −
p W → W −
p and a small
sphere centered at zero in T −
p W determines a diﬀeomorphism ( W −
p \ p)/R = (T −
p W \ 0)/R.
We thus obtain a diﬀeomorphism ρp ∈ Diﬀ(( T −
p W \ 0)/R, Λ p) which is well-deﬁned up to
contractible choice.
Lemma 6.6. Let (Y 2n−1, λ) be a contact manifold with contact form, let Λ 1, . . . ,Λ m ⊆ Y be
disjoint Legendrian spheres, and let σj ∈ Diﬀ( Sn−1, Λ j)/O(n). The following space is weakly
contractible:







Elementary Weinstein cobordism (W 2n, λ, φ) with critical points pj
and stable manifolds Vpj .
Isomorphism i : (∂−W, λ)
∼
− →(Y, λ) sending Vpj ∩ ∂−W to Λ j.
Path q between σj and the image of ρpj in Diﬀ( Sn−1, Λ j)/O(n).







in the sense that for all k ≥ 0, any family of such objects (W, i, q) over ∂D k can be extended
to a family over Dk.
There is also a version of Lemma
6.6 for any critical points of any index, though it is
more complicated to state since subcritical handle attachment req uires an additional piece
of data (a framing of the symplectic normal bundle of the attaching sphere). In this paper,
we only need the case of critical handle attachment, so we omit the m ore general statement
and its proof. We thank Ya. Eliashberg for useful discussions rega rding the proof.
24

Proof. Let a family over ∂D k be given ( k ≥ 0).
We ﬁrst equip the family with local Darboux charts near the critical p oints, and homotope
it so that the Liouville vector ﬁeld coincides with a certain standard mo del in these charts.
We phrase this part of the argument as if there is just a single triple ( W, i, q) and a single
critical point p, but it is clear that each step also works in families and for multiple critic al
points. The details are as follows.
Fix a local symplectomorphism (Darboux chart) exp p : (TpW, 0) → (W, p) whose deriva-
tive at zero is the identity. On the symplectic vector space TpW , the vector ﬁeld dpX :
TpW → TpW is Liouville (this is just the linearization of the Liouville structure of W near
p); it follows that the positive/negative eigenspaces T ±
p W of dpX are Lagrangian [ CE12,
Proposition 11.9].
We ﬁrst homotope the function φ so that
exp∗
p φ = φstd near zero (6.13)
where φstd : TpW → R is given by φstd(v) := |v+|2 − |v−|2. Here we ﬁx positive deﬁnite
quadratic forms on T ±
p W such that the Liouville vector ﬁeld exp ∗
p X is gradient-like for
φstd near zero. Note that the space of such quadratic forms is clearly o pen and convex,
and it is seen to be non-empty by considering quadratic forms which a re diagonal with
respect to a basis which puts dpX into Jordan normal form. Now we consider the homotopy
{φ+(φstd−φ)tχ}t∈[0,1] for some smooth compactly supported cutoﬀ function χ : TpW → [0, 1]
which equals 1 in a neighborhood of zero. Its diﬀerential equals (1 −tχ)dφ+tχdφstd +t(φstd −
φ)dχ. We have φstd − φ = O(|v|2), so to ensure that exp ∗
p X is gradient-like throughout the
homotopy, it suﬃces to choose χ so that |dχ| is much smaller than |v|−1. Such a cutoﬀ
function exists (supported in any given neighborhood of zero) sinc e
∫ 1
0 r−1dr diverges. Thus
we have achieved (
6.13).
We next homotope the Liouville vector ﬁeld X so that
exp∗
p X = Xstd near zero (6.14)
where Xstd : TpW → TpW acts by − id on T −
p W and by 2 id on T +
p W (observe that this is
indeed a Liouville vector ﬁeld). Note that both vector ﬁelds exp ∗
p X and Xstd are gradient-
like with respect to exp ∗
p φ = φstd near zero. Write the Liouville form for exp ∗
p X as λ, write
the Liouville form for Xstd as λstd, and write λstd − λ = d f for a function f vanishing at
zero. We consider the homotopy {λ + d(tχf )}t∈[0,1] for χ as above. We may write this as
(1 − tχ)λ + tχλstd + tf dχ. We have f = O(|v|2), so in order to guarantee that the resulting
Liouville vector ﬁeld remains gradient-like for exp ∗
p φ = φstd, it is again enough to choose χ
so that |dχ| is much smaller than |v|−1, which exists as before. This achieves (
6.14).
We have now homotoped X and φ near p so that they coincide via the chosen Darboux
chart exp p : ( TpW, 0) → (W, p) with Xstd and φstd as above near zero. Since exp ∗
p X = Xstd
in a neighborhood of zero, there is an induced diﬀeomorphism ρ : (T −
p W \ 0)/R>0 → Λ.
Now Diﬀ( Sn−1, Λ) /O(n) classiﬁes vector bundles V along with a ﬁberwise diﬀeomorphism
from the sphere bundle S(V ) := ( V \ 0)/R>0 to Λ. Hence the data of q determines an
extension of the vector bundle T −
p W from ∂D k to Dk (also denoted T −
p W ), an extension of
the ﬁberwise diﬀeomorphism ρ : (T −
p W \0)/R>0 → Λ to Dk, and an extension of q itself from
∂D k to Dk. We may also extend T +
p W from ∂D k to Dk by observing that T +
p W = (T −
p W )∗
25

over ∂D k (by virtue of the symplectic form) and thus deﬁning T +
p W := ( T −
p W )∗ over Dk.
Hence TpW := T −
p W ⊕ T +
p W is a symplectic vector bundle over Dk. We conclude that it
suﬃces to extend W from ∂D k to Dk so that it has the chosen tangent spaces TpW , has
exponential charts exp p satisfying ( 6.13) and ( 6.14) above, and so that it induces the chosen
diﬀeomorphisms ρ : (T −
p W \ 0)/R>0 → Λ.
Over any point in Dk, we have a co-oriented contact manifold ( TpW \ T +
p W )/R (quotient
by the Liouville ﬂow), and a Legendrian submanifold ( T −
p W \ 0)/R>0 (quotient by dilation,
which coincides with the Liouville ﬂow). Over any point in ∂D k, the Liouville ﬂow on W
determines a germ of co-orientation preserving contactomorphis m ˜ρ between a neighborhood
of this Legendrian submanifold and a neighborhood of Λ p ⊆ Y , restricting to ρ. Conversely,
a neighborhood of W −
p in W is determined by TpW = T −
p W ⊕ T +
p W and the germ of
co-orientation preserving contactomorphism ˜ ρ. Note that W always deforms down to a
neighborhood of ∂−W ∪ W −
p . Thus it suﬃces to extend ˜ ρ from ∂D k to Dk such that it
restricts to ρ (such an extension determines for us an extension of W from ∂D k to Dk).
To show that ˜ρ extends to Dk, it suﬃces to show that for any closed manifold M, the
restriction map from germs of co-orientation preserving contact omorphisms of J 1M mapping
the zero section to itself to diﬀeomorphisms of M is a weak homotopy equivalence (we will
apply this to M = Sn−1). Equivalently, it suﬃces to show that the space of germs of co-
orientation preserving contactomorphisms of J 1M ﬁxing the zero section pointwise is weakly
contractible. Write J 1M = T ∗M ×R with contact form λ−ds, and write ht for the ﬂow of the
contact vector ﬁeld Xλ + s ∂
∂s . Fix any germ of co-orientation preserving contactomorphism
f : J 1M → J 1M ﬁxing the zero section pointwise, and we will deﬁne a canonical path
from f to the identity (clearly this is enough). We ﬁrst consider the limit as t → ∞ of the
conjugation ht ◦ f ◦ h−1
t , which is nothing other than the vertical projection of the derivat ive
of f along the zero section. We are thus reduced to considering a co-or ientation preserving
contactomorphism f0 : J 1M → J 1M which is a linear map of bundles over M. Now a general
such linear map has the form
(α, g) ↦→(Aα + Bg, Cα + Dg) (6.15)
where A : M → End(T ∗M), B : M → T ∗M, C : M → T M, D : M → R are sections over
M. As a contactomorphism, f0 preserves the Legendrian sections ( dg, g) of J 1M over M,
which means that
A(dg) + gB = d(Cg ) + gdD + Ddg (6.16)
for all functions g : M → R. Since d(Cg ) is the only second-order term, we conclude that
C ≡ 0. Comparing ﬁrst-order terms shows that A = D · id, and ﬁnally we may solve for
B = dD. Thus f0 : J 1M → J 1M is given by ( α, g) ↦→(D · α + g · dD, D · g) for some function
D : M → R. Since f0 is a diﬀeomorphism, D is non-vanishing, and since f0 is co-orientation
preserving, D > 0 everywhere. Finally, we may connect f0 to the identity using the obvious
linear homotopy from D to the constant function 1.
References
[Aur97] D. Auroux, Asymptotically holomorphic families of symplectic subman ifolds,
Geom. Funct. Anal. 7 (1997), no. 6, 971–995. MR 1487750 (99b:57069)
5
26

[Aur00] Denis Auroux, Symplectic 4-manifolds as branched coverings of CP2, Invent.
Math. 139 (2000), no. 3, 551–602. MR 1738061 (2000m:53119) 5, 16, 17
[Aur02] D. Auroux, A remark about Donaldson ’s construction of symplectic subm anifolds,
J. Symplectic Geom. 1 (2002), no. 3, 647–658. MR 1959060 (2004i:53121) 5, 12,
16
[A V65] Aldo Andreotti and Edoardo Vesentini, Carleman estimates for the Laplace-
Beltrami equation on complex manifolds , Inst. Hautes ´Etudes Sci. Publ. Math.
(1965), no. 25, 81–130. MR 0175148 (30 #5333) 5, 6, 7, 8, 9
[BEE12] Fr´ ed´ eric Bourgeois, Tobias Ekholm, and Yasha Eliashberg , Eﬀect of Legendrian
surgery, Geom. Topol. 16 (2012), no. 1, 301–389, With an appendix by Sheel
Ganatra and Maksim Maydanskiy. MR 2916289 4
[CE12] Kai Cieliebak and Yakov Eliashberg, From Stein to Weinstein and back , American
Mathematical Society Colloquium Publications, vol. 59, American Math ematical
Society, Providence, RI, 2012, Symplectic geometry of aﬃne comp lex manifolds.
MR 3012475 1, 4, 19, 20, 24, 25
[CG91] Jeﬀ Cheeger and Mikhael Gromov, Chopping Riemannian manifolds , Diﬀerential
geometry, Pitman Monogr. Surveys Pure Appl. Math., vol. 52, Long man Sci.
Tech., Harlow, 1991, pp. 85–94. MR 1173034 (93k:53034) 5
[Dem96] Jean-Pierre Demailly, L2 estimates for the ¯∂-operator on complex manifolds, Notes
de cours, Ecole d’´ et´ e de Math´ ematiques (Analyse Complexe), Institut Fourier,
Grenoble, Juin 1996. 8
[Don90] S. K. Donaldson, Yang-Mills invariants of four-manifolds , Geometry of low-
dimensional manifolds, 1 (Durham, 1989), London Math. Soc. Lect ure Note
Ser., vol. 150, Cambridge Univ. Press, Cambridge, 1990, pp. 5–40. MR 1171888
(93f:57040) 7
[Don96] , Symplectic submanifolds and almost-complex geometry , J. Diﬀerential
Geom. 44 (1996), no. 4, 666–705. MR 1438190 (98h:53045) 3, 5, 6, 12, 13, 16
[Don99] , Lefschetz pencils on symplectic manifolds , J. Diﬀerential Geom. 53
(1999), no. 2, 205–236. MR 1802722 (2002g:53154) 5, 16
[Eli90] Yakov Eliashberg, Topological characterization of Stein manifolds of dimens ion
> 2, Internat. J. Math. 1 (1990), no. 1, 29–46. MR 1044658 (91k:32012) 1
[EM02] Y. Eliashberg and N. Mishachev, Introduction to the h-principle, Graduate Studies
in Mathematics, vol. 48, American Mathematical Society, Providenc e, RI, 2002.
MR 1909245 (2003g:53164) 16
[Fri44] K. O. Friedrichs, The identity of weak and strong extensions of diﬀerential op er-
ators, Trans. Amer. Math. Soc. 55 (1944), 132–151. MR 0009701 (5,188b) 8
27

[Gir02] Emmanuel Giroux, G´ eom´ etrie de contact: de la dimension trois vers les dimen -
sions sup´ erieures, Proceedings of the International Congress of Mathematicians,
Vol. II (Beijing, 2002), Higher Ed. Press, Beijing, 2002, pp. 405–4 14. MR 1957051
(2004c:53144) 5
[H¨ or65] Lars H¨ ormander, L2 estimates and existence theorems for the ¯∂ operator, Acta
Math. 113 (1965), 89–152. MR 0179443 (31 #3691) 5, 6, 7, 8, 9
[IMTP00] A. Ibort, D. Mart ´ ınez-Torres, and F. Presas, On the construction of contact sub-
manifolds with prescribed topology, J. Diﬀerential Geom. 56 (2000), no. 2, 235–283.
MR 1863017 (2003f:53158) 5
[Mil64] J. Milnor, On the Betti numbers of real varieties , Proc. Amer. Math. Soc. 15
(1964), 275–280. MR 0161339 (28 #4547) 18
[Moh01] Jean-Paul Mohsen, Transversalit´ e quantitative et sous-vari´ et´ es isotropes, Ph.D.
thesis, ENS-Lyon, 2001. 5
[Moh13] , Transversalit´ e quantitative en g´ eom´ etrie symplectique : sous-vari´ et´ es et
hypersurfaces, Arxiv Preprint arXiv:1307.0837v1 (2013), 1–34. 3, 5, 13, 16
[Sei08a] Paul Seidel, A∞-subalgebras and natural transformations , Homology, Homotopy
Appl. 10 (2008), no. 2, 83–114. MR 2426130 (2010k:53154) 4
[Sei08b] , Fukaya categories and Picard-Lefschetz theory , Zurich Lectures in Ad-
vanced Mathematics, European Mathematical Society (EMS), Z¨ u rich, 2008. MR
2441780 (2009f:53143) 4
[Sei09] , Symplectic homology as Hochschild homology , Algebraic geometry—
Seattle 2005. Part 1, Proc. Sympos. Pure Math., vol. 80, Amer. Ma th. Soc.,
Providence, RI, 2009, pp. 415–434. MR 2483942 (2010c:53129) 4
[Sei12] , Fukaya A∞-structures associated to Lefschetz ﬁbrations. I , J. Symplectic
Geom. 10 (2012), no. 3, 325–388. MR 2983434 4
[Voi02] Claire Voisin, Hodge theory and complex algebraic geometry. I , Cambridge Studies
in Advanced Mathematics, vol. 76, Cambridge University Press, Cam bridge, 2002,
Translated from the French original by Leila Schneps. MR 1967689 ( 2004d:32020)
10
[Wei91] Alan Weinstein, Contact surgery and symplectic handlebodies , Hokkaido Math. J.
20 (1991), no. 2, 241–251. MR 1114405 (92g:53028) 21, 24
[Won93] Richard Wongkew, Volumes of tubular neighbourhoods of real algebraic variet ies,
Paciﬁc J. Math. 159 (1993), no. 1, 177–184. MR 1211391 (94e:14073) 16, 17
28

