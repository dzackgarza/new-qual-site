From Stein to Weinstein and Back
Symplectic Geometry of Aﬃne Complex Manifolds
Kai Cieliebak
Yakov Eliashberg
Mathematisches Institut, Ludwig-Maximilians-Universit ¨at, There-
sienstr. 39, 80333 M ¨unchen, Germany
E-mail address : kai@math.lmu.de
Department of Mathematics, Stanford University, Stanford, CA
94305, USA
E-mail address : eliash@math.stanford.edu

2010 Mathematics Subject Classiﬁcation. 32Q28, 53D35

To my parents, Snut and Hinrich. Kai
To Ada. Yasha



Contents
Preface 1
Chapter 1. Introduction 3
1.1. An overview 3
1.2. Plan of the book 8
Part 1. J-Convexity 11
Chapter 2. J-Convex Functions and Hypersurfaces 13
2.1. Linear algebra 13
2.2. J-convex functions 15
2.3. The Levi form of a hypersurface 17
2.4. Completeness 20
2.5. J-convexity and geometric convexity 21
2.6. Normalized Levi form and mean normal curvature 22
2.7. Examples of J-convex functions and hypersurfaces 24
2.8. Symplectic properties of J-convex functions 27
2.9. Computations in Cn 29
Chapter 3. Smoothing 33
3.1. J-convexity and plurisubharmonicity 33
3.2. Smoothing of J-convex functions 36
3.3. Critical points of J-convex functions 39
3.4. From families of hypersurfaces to J-convex functions 42
3.5. J-convex functions near totally real submanifolds 44
3.6. Functions with J-convex level sets 50
3.7. Normalized modulus of J-convexity 52
Chapter 4. Shapes for i-Convex Hypersurfaces 59
4.1. Main models 59
4.2. Shapes for i-convex hypersurfaces 61
4.3. Properties of i-convex shapes 67
4.4. Shapes in the subcritical case 70
4.5. Construction of special shapes 71
4.6. Families of special shapes 78
4.7. Convexity estimates 85
Chapter 5. Some Complex Analysis 91
5.1. Holomorphic convexity 91
5.2. Relation to J-convexity 92
5.3. Deﬁnitions of Stein manifolds 95
vii

viii CONTENTS
5.4. Hartogs phenomena 96
5.5. Grauert’s Oka principle 98
5.6. Coherent analytic sheaves on Stein manifolds 101
5.7. Real analytic manifolds 103
5.8. Real analytic approximations 106
5.9. Approximately holomorphic extension of maps from totally real
submanifolds 108
5.10. CR structures 110
Part 2. Existence of Stein Structures 113
Chapter 6. Symplectic and Contact Preliminaries 115
6.1. Symplectic vector spaces 115
6.2. Symplectic vector bundles 117
6.3. Symplectic manifolds 118
6.4. Moser’s trick and symplectic normal forms 119
6.5. Contact manifolds and their Legendrian submanifolds 122
6.6. Contact normal forms 125
6.7. Real analytic approximations of isotropic submanifolds 127
6.8. Relations between symplectic and contact manifolds 128
Chapter 7. The h-Principles 131
7.1. Immersions and embeddings 131
7.2. The h-principle for isotropic immersions 135
7.3. The h-principle for subcritical isotropic embeddings 136
7.4. Stabilization of Legendrian submanifolds 137
7.5. The existence theorem for Legendrian embeddings 139
7.6. Legendrian knots in overtwisted contact manifolds 141
7.7. Murphy’s h-principle for loose Legendrian embeddings 142
7.8. Directed immersions and embeddings 146
7.9. Discs attached to J-convex boundaries 150
Chapter 8. The Existence Theorem 155
8.1. Some notions from Morse theory 155
8.2. Surrounding stable discs 156
8.3. Existence of complex structures 161
8.4. Existence of Stein structures in complex dimension ⁄= 2 163
8.5. J-convex surrounding functions 167
8.6. J-convex retracts 171
8.7. Approximating continuous maps by holomorphic ones 174
8.8. Variations on a theme of E. Kallin 181
Part 3. Morse-Smale Theory for J-Convex Functions 185
Chapter 9. Recollections from Morse Theory 187
9.1. Critical points of functions 187
9.2. Zeroes of vector ﬁelds 189
9.3. Gradient-like vector ﬁelds 192
9.4. Smooth surroundings 198
9.5. Changing Lyapunov functions near critical points 200

CONTENTS ix
9.6. Smale cobordisms 202
9.7. Morse and Smale homotopies 206
9.8. The h-cobordism theorem 210
9.9. The two-index theorem 212
9.10. Pseudo-isotopies 213
Chapter 10. Modiﬁcations of J-Convex Morse Functions 215
10.1. Moving attaching spheres by isotropic isotopies 215
10.2. Relaxing the J-orthogonality condition 222
10.3. Moving critical levels 223
10.4. Creation and cancellation of critical points 224
10.5. Carving one J-convex function with another one 225
10.6. Surrounding a stable half-disc 225
10.7. Proof of the cancellation theorem 231
10.8. Proof of the creation theorem 232
Part 4. From Stein to Weinstein and Back 235
Chapter 11. Weinstein Structures 237
11.1. Liouville cobordisms and manifolds 237
11.2. Liouville homotopies 239
11.3. Zeroes of Liouville ﬁelds 241
11.4. Weinstein cobordisms and manifolds 243
11.5. From Stein to Weinstein 244
11.6. Weinstein and Stein homotopies 245
11.7. Weinstein structures with unique critical points 249
11.8. Subcritical and ﬂexible Weinstein structures 250
Chapter 12. Modiﬁcations of Weinstein Structures 253
12.1. Weinstein structures with given functions 253
12.2. Holonomy of Weinstein cobordisms 256
12.3. Liouville ﬁelds near isotropic submanifolds 258
12.4. Weinstein structures near critical points 263
12.5. Weinstein structures near stable discs 265
12.6. Morse-Smale theory for Weinstein structures 267
12.7. Elementary Weinstein homotopies 269
Chapter 13. Existence Revisited 271
13.1. Existence of Weinstein structures 271
13.2. From Weinstein to Stein: existence 273
13.3. Proof of the Stein existence theorems 275
Chapter 14. Deformations of Flexible Weinstein Structures 279
14.1. Homotopies of ﬂexible Weinstein cobordisms 279
14.2. Proof of the ﬁrst Weinstein deformation theorem 280
14.3. Proof of the second Weinstein deformation theorem 286
14.4. Subcritical Weinstein manifolds are split 288
14.5. Symplectic pseudo-isotopies 292
Chapter 15. Deformations of Stein Structures 295

x CONTENTS
15.1. From Weinstein to Stein: homotopies 295
15.2. Proof of the ﬁrst Stein deformation theorem 298
15.3. Homotopies of ﬂexible Stein structures 302
Part 5. Stein Manifolds and Symplectic Topology 305
Chapter 16. Stein Manifolds of Complex Dimension Two 307
16.1. Filling by holomorphic discs 307
16.2. Stein ﬁllings 310
16.3. Stein structures on 4-manifolds 320
Chapter 17. Exotic Stein Structures 323
17.1. Symplectic homology 323
17.2. Exotic Stein structures 325
Appendix A. Some Algebraic Topology 329
A.1. Serre ﬁbrations 329
A.2. Some homotopy groups 331
Appendix B. Obstructions to Formal Legendrian Isotopies 335
Appendix C. Biographical Notes on the Main Characters 343
C.1. Complex analysis 343
C.2. Diﬀerential and symplectic topology 348
Bibliography 353
Index 361

Preface
In Spring 1996 Yasha Eliashberg gave a Nachdiplomvorlesung (a one semester
graduate course) “Symplectic geometry of Stein manifolds” at ETH Z¨ urich. Kai
Cieliebak, at the time a graduate student at ETH, was assigned the task to take
notes for this course, with the goal of having lecture notes ready for publication by
the end of the course. At the end of the semester we had some 70 pages of typed
up notes, but they were nowhere close to being publishable. So we buried the idea
of ever turning these notes into a book.
Seven years later Kai spent his ﬁrst sabbatical at the Mathematical Sciences
Research Institute (MSRI) in Berkeley. By that time, through work of Donaldson
and others on approximately holomorphic sections on the one hand, and gluing
formulas for holomorphic curves on the other hand, Weinstein manifolds had been
recognized as fundamental objects in symplectic topology. Encouraged by the in-
creasing interest in the subject, we dug out the old lecture notes and began turning
them into a monograph on Stein and Weinstein manifolds.
Work on the book has continued on and oﬀ since then, with most progress hap-
pening during Kai’s numerous visits to Stanford University and another sabbatical
2009 that we both spent at MSRI. Over this period of almost 10 years, the con-
tent of the book has been repeatedly changed and its scope signiﬁcantly extended.
Some of these changes and extensions were due to our improved understanding of
the subject (e.g. a quantitative version of J-convexity which is preserved under ap-
proximately holomorphic diﬀeomorphisms), others due to new developments such
as the construction of exotic Stein structures by Seidel–Smith, McLean and others
since 2005, and Murphy’s h-principle for loose Legendrian knots in 2011. In fact,
the present formulation of the main theorems in the book only became clear about
a year ago. As a result of this process, only a few lines of the original lecture notes
have survived in the ﬁnal text (in Chapters 2–4).
The purpose of the book has also evolved over the past decade. Our original goal
was a complete and detailed exposition of the existence theorem for Stein structures
in [42]. While this remains an important goal, which we try to achieve in Chapters
2–8, the book has evolved around the following two broader themes. The ﬁrst one,
as indicated by the title, is the correspondence between the complex analytic notion
of a Stein manifold and the symplectic notion of a Weinstein manifold. The second
one is the extent to which these structures are ﬂexible, i.e., satisfy an h-principle.
In fact, until recently we believed the border between ﬂexibility and rigidity to
run between subcritical and critical structures, but Murphy’s h-principle extends
ﬂexibility well into the critical range.
The book is roughly divided into “complex” and “symplectic” chapters. Thus
Chapters 2–5 and 8–10 can be read as an exposition of the theory of J-convex
1

2 PREFACE
functions on Stein manifolds, while Chapters 6–7, 9 and 11–14 provide an intro-
duction to Weinstein manifolds and their deformations. However, our selection of
material on both the complex and symplectic side is by no means representative
for the respective ﬁelds. Thus on the complex side we focus only on topological as-
pects of Stein manifolds, ignoring most of the beautiful subject of several complex
variables. On the symplectic side, the most notable omission is the relationship
between Weinstein domains and Lefschetz ﬁbrations over the disc.
Over the past 16 years we both gave many lecture courses, seminars, and talks
on the subject of this book not only at our home institutions, Ludwig-Maximilians-
Universit¨ at M¨ unchen and Stanford University, but also at various other places such
as the Forschungsinstitut f¨ ur Mathematik at ETH Z¨ urich, University of Pennsyl-
vania in Philadelphia, Columbia University in New York, the Courant Institute of
Mathematical Sciences in New York, University of California in Berkeley, Wash-
ington University in St. Louis, the Mathematical Sciences Research Institute in
Berkeley, the Institute for Advanced Study in Princeton, and the Alfr´ ed R´ enyi
Institute of Mathematics in Budapest. We thank all these institutions for their
support and hospitality.
Many mathematicians and students who attended our lectures and seminars
or read parts of preliminary versions of the book provided us with valuable com-
ments and critical remarks. We are very grateful to all of them, and in particular
to M. Abouzaid, S. Akbulut, J. Bowden, V. Braungardt, J. Daniel, T. Ekholm,
C. Epstein, J. Etnyre, C. Feﬀerman, F. Forstneriˇ c, U. Frauenfelder, A. Gersten-
berger, R. Gompf, A. Huckleberry, P. Landweber, J. Latschev, L. Lempert, R. Lip-
shitz, C. Llosa Isenrich, D. McDuﬀ, M. McLean, K. Mohnke, J. Morgan, E. Mur-
phy, S. Nemirovski, L. Nirenberg, K. Nguyen, A. Oancea, N. Øvrelid, P. Ozsv´ ath,
L. Polterovich, P. Seidel, A. Stadelmaier, A. Stipsicz, D. Thurston, T. Vogel,
E. Volkov, J. Wehrheim, and C. Wendl.
We thank G. Herold, T. M¨ uller, and S. Pr¨ ufer for creating the ﬁgures.
And most of all, we thank our spouses, Suny and Ada, for their continued
support.

1
Introduction
1.1. An overview
Stein manifolds. A Stein manifold is a properly embedded complex subma-
nifold of some CN. As we show in this book, Stein manifolds have built into them
symplectic geometry which is responsible for many phenomena in complex geometry
and analysis. The goal of this book is a systematic exploration of this symplectic
geometry (the “road from Stein to Weinstein”) and its applications in the complex
geometric world of Stein manifolds (the “road from Weinstein to Stein”).
Stein manifolds are necessarily noncompact, and properly embedded complex
submanifolds of Stein manifolds are again Stein. Stein manifolds arise, e.g., from
closed complex projective manifolds X⊂ CPN: If H⊂ CPN is any hyperplane,
then the aﬃne algebraic manifold X\H is Stein. Using this construction, it is not
hard to see that every closed Riemann surface with at least one point removed is
Stein. In fact, as we will see below, any open Riemann surface is Stein. Already
this example shows that the class of Stein manifolds is much larger than the class
of aﬃne algebraic manifolds.
Stein manifolds can also be described intrinsically. The characterization most
relevant for us is due to Grauert [ 77]. Let ( V,J ) be a complex manifold, where
J denotes the complex multiplication on tangent spaces. To a smooth real-valued
function φ : V → R we can associate the 1-form dCφ := dφ◦J and the 2-form
ωφ :=−ddCφ. The function is called (strictly) plurisubharmonic or, as we prefer
to say, J-convex if gφ(v,w ) := ωφ(v,Jw ) deﬁnes a Riemannian metric. Since gφ
is symmetric, this is equivalent to saying that ωφ is a symplectic (i.e., closed and
nondegenerate) form compatible with J, i.e., Hφ =gφ−iωφ is a Hermitian metric.
A functionφ :V → R is called exhausting if it is proper (i.e., preimages of compact
sets are compact) and bounded from below.
Since the function φst(z) := |z|2 on CN is exhausting and i-convex with re-
spect to the standard complex structure i on CN, every Stein manifold admits an
exhausting J-convex function (namely the restriction of φst to V ). A combination
of theorems of Grauert [ 77] and Bishop–Narasimhan [ 18, 144 ] asserts that the
converse is also true: A complex manifold which admits an exhausting J-convex
function is Stein.
Note that the space of exhaustingJ-convex functions on a given Stein manifold
(V,J ) is convex, and hence contractible. It is also open in C2(V ), so a generic J-
convex function is a Morse function (i.e., it has only nondegenerate critical points)
and a generic path of J-convex functions consists of Morse and generalized Morse
functions, i.e., functions with only non-degenerate and birth-death type critical
points.
3

4 1. INTRODUCTION
Weinstein manifolds. A Weinstein structure on a 2n-dimensional manifold
V is a triple (ω,X,φ ), where ω is a symplectic form, φ : V → R is an exhausting
generalized Morse function, and X is a complete Liouville vector ﬁeld which is
gradient-like forφ. Here the Liouville condition means that the Lie derivative LXω
coincides with ω. The quadruple (V,ω,X,φ ) is called a Weinstein manifold. . We
will see that homotopic (for an appropriate deﬁnition of homotopy, see Section 11.6)
Weinstein manifolds are symplectomorphic. This structure was introduced in a
slightly diﬀerent form by A. Weinstein in [187] and then formalized in [ 49]. It has
since then become a central object of study in symplectic topology, see e.g. [ 32,
169, 24].
As it was explained above, after ﬁxing an exhausting J-convex generalized
Morse function φ : V → R on a Stein manifold ( V,J ) one can associate with the
triple (V,J,φ ) the symplectic form ωφ. It turns out that the gradient vector ﬁeld
Xφ :=∇gφφ of φ, computed with respect to the metric gφ which it generates, is
Liouville with respect to the form ωφ. After composing φ with a suitable function
R→ R we may further assume that the vector ﬁeld Xφ is complete. Then the
assignment
(J,φ )↦→ W(J,φ ) := (ωφ,Xφ,φ )
yields a canonical map from Stein to Weinstein structures. A diﬀerent choice of
exhausting J-convex generalized Morse function leads to a homotopic, and hence
symplectomorphic, Weinstein manifold. Note that this map forgets the most rigid
datum, the integrable complex structure J. A major theme of this book is the
reconstruction of Stein structures from Weinstein structures (the “road from Wein-
stein to Stein”).
From Weinstein to Stein. We say that two functions φ,φ′ : V → R are
target equivalent if there exists an increasing diﬀeomorphism g : R→ R such that
φ′ =g◦φ. In the following theorem we always have to allow fortarget reparametriza-
tions, i.e., replacing functions by target equivalent ones, but we suppress this trivial
operation from the notation.
Theorem 1.1. (a) Given a Weinstein structure W = (ω,X,φ ) on V , there
exists a Stein structure (J,φ ) on V such that W(J,φ ) is Weinstein homotopic to
W with ﬁxed function φ.
(b) Given a Weinstein homotopy Wt = (ωt,Xt,φt), t∈ [0, 1], on V beginning
with W0 = W(J,φ ), there exists a Stein homotopy (Jt,φt) starting at (J0,φ 0) =
(J,φ ) such that the paths W(Jt,φt) and Wt are homotopic with ﬁxed functions φt
and ﬁxed at t = 0. Moreover, there exists a diﬀeotopy ht : V → V with h0 = Id
such that h∗
tJt =J for all t∈ [0, 1].
(c) Given a Weinstein homotopy Wt = (ωt,Xt,φt), t∈ [0, 1], on V connect-
ing W0 = W(J0,φ 0) and W1 = W(J1,φ 1) with φt = φ1 for t ∈ [ 1
2, 1], there
exists a Stein homotopy (Jt,φt) connecting (J0,φ 0) and (J1,φ 1) such that the paths
W(Jt,φt) and Wt are homotopic with ﬁxed functions φt and ﬁxed at t = 0, 1.
Theorem 1.1 ﬁts in the following more global, partially conjectural picture.
To avoid discussing subtleties concerning the appropriate topologies on the spaces
of Stein and Weinstein structures, we restrict our attention here to the compact
case. Let W be a compact smooth manifold W with boundary. In the following
discussion we always assume that all considered functions on W have∂W as their
regular level set. A Stein domain structure on W is a pair ( J,φ ), where J is a

1.1. AN OVERVIEW 5
complex structure and φ : W → R is a J-convex generalized Morse function. A
Weinstein domain structure on W is a triple ( ω,X,φ ) consisting of a symplectic
form on W , a generalized Morse function φ : W→ R, and a Liouvile vector ﬁeld
X which is gradient-like for φ. Let us denote by Stein and Weinstein the spaces of
Stein and Weinstein domain structures onW , respectively. Let Morse be the space
of generalized Morse functions on W .
We have the following commutative diagram
Stein
πS
$$JJJJJJJJJ
W // Weinstein
πW
xxqqqqqqqqqq
Morse
where W(J,φ ) = (ωφ,Xφ,φ ) as above, πW(ω,X,φ ) := φ and πS(J,φ ) := φ. Con-
sider the ﬁbers Stein(φ) := π−1
S (φ) and Weinstein(φ) := π−1
W (φ) of the projections
πS and πW overφ∈ Morse.
Theorem 1.2. The map Wφ := W|Stein(φ) : Stein(φ)→ Weinstein(φ) is a
weak homotopy equivalence.
Note that (a compact version of) Theorem 1.1 (a) is equivalent to the fact that
the map Wφ induces an epimorphism on π0, while Theorem 1.1 (c) implies that
the induced homomorphism is injective on π0 and surjective on π1. Conversely, it
is easy to see that Theorem 1.1 (b) and injectivity of Wφ onπ0 imply Theorem 1.1
(c).
To put Theorem 1.1 (b) into a more global framework, let us denote by D
the identity component of the diﬀeomorphism group of W . Fix a Stein domain
structure (J,φ 0) on W (the function φ0 will play no role in what follows; the only
important fact is that it exists). For a function φ∈ Morse we introduce the spaces
DJ(φ) :={h∈D| φ ish∗J-convex},
PJ(φ) :={(h,γ )|h∈D J(φ), γ: [0, 1]→ Weinstein(φ), γ(0) = W(h∗J,φ )},
PJ :=
⋃
φ∈Morse
PJ(φ).
We denote by WeinsteinJ the connected component of W(J,φ 0) in Weinstein (for
any choice of φ0; the component is independent of this choice).
Conjecture 1.3. The projection πP :PJ→ WeinsteinJ, (h,γ )↦→ γ(1) is a
Serre ﬁbration.
Note that (a compact version of) Theorem 1.1 (b) is just the homotopy lifting
property of πP for homotopies of points, so it is a special case of Conjecture 1.3.
We believe that this conjecture can be proven by further developing techniques
discussed in this book. By an easy topological argument (see Appendix A.1),
Conjecture 1.3 combined with Theorem 1.2 would imply
Conjecture 1.4. The map W : Stein→ Weinstein is a weak homotopy equiv-
alence.
Let us emphasize that we are interested in this book in the classiﬁcation of
Stein structures up deformation, and not up to biholomorphism. The classiﬁcation
of Stein complex structures up to biholomorphism is very subtle. For example,

6 1. INTRODUCTION
C∞-small deformations of the round ball in Cn, n≥ 2, give rise to uncountably
many pairwise non-biholomorphic Stein manifolds. See e.g. [ 116] for an exposition
of this beautiful subject.
Existence of Stein structures. Theorem 1.1 reduces complex-geometric
questions about Stein manifolds to symplecto-geometric questions about Weinstein
manifolds. Our next task is to develop techniques for answering those questions.
Let us ﬁrst analyze necessary conditions for the existence of a Weinstein (or
Stein) structure on a given smooth manifold V of real dimension 2 n. Clearly,
one necessary condition is the existence of an almost complex structure J, i.e., an
endomorphism of the tangent bundle with J2 =−Id. A second necessary condition
arises from the following property of Morse functions with gradient-like Liouville
ﬁelds (see Chapter 2): their Morse indices are ≤n. By Morse theory, this implies
that V has a handlebody decomposition with handles of index at most n. This
observation of Milnor [ 139] was the result of a long development, beginning with
Lefschetz [121] and followed by Serre [ 170] and Andreotti-Frankel [7].
It turns out that for dim RV ⁄= 4 these two conditions are suﬃcient for the
existence of a Weinstein structure on V , so in combination with Theorem 1.1 (a)
we get the following existence theorem which was proved in [ 42]:
Theorem 1.5 (existence of Stein structures) . Let (V,J ) be an almost complex
manifold of dimension 2n⁄= 4 andφ :V → R an exhausting Morse function without
critical points of index > n. Then there exists an integrable complex structure ~J
on V homotopic to J for which the function φ is target equivalent to a ~J-convex
function. In particular, (V, ~J) is Stein.
We prove in this book several reﬁnements and extensions of this result, some
of which are due to Gompf [ 71, 72, 73] and Forstneriˇ c–Slapar [63].
Theorem 1.5 settles the existence question for Stein structures in dimensions
⁄= 4. In dimension 4 the situation is drastically diﬀerent. For instance, Lisca and
Matiˇ c proved in [125] thatS2×R2 does not admit any Stein complex structure. On
the other hand, Gompf proved the following topological analogue of Theorem 1.5:
Theorem 1.6 (Gompf [70]). LetV be an oriented open topological 4-manifold
which admits a (possibly inﬁnite) handlebody decomposition without handles of index
> 2. Then V is homeomorphic to a Stein surface (i.e., a Stein manifold of complex
dimension 2). Moreover, any homotopy class of almost complex structures on V is
induced by an orientation preserving homeomorphism from a Stein surface.
Let us point out that the Stein surfaces in Theorem 1.6 are usually not of ﬁnite
type, where a Stein manifold is said to be of ﬁnite type if it admits an exhausting
J-convex function with only ﬁnitely many critical points. Gompf’s result which
uses the technique of Casson handles, as well as Lisca-Matiˇ c’s theorem which uses
Seiberg-Witten theory, are beyond the scope of this book. See however Chapter 16
for some related discussion. For example, we prove that S2× R2 is not homeomor-
phic to any Stein surface of ﬁnite type.
Deformations of Stein structures. It turns out that the Weinstein prob-
lems in parts (b) and (c) of Theorem 1.1 cannot be reduced, in general, to diﬀerential
topology even when dim V > 4. On the contrary, they are tightly related to the
core problems of symplectic topology.

1.1. AN OVERVIEW 7
It is easy to see that a Weinstein structure ( ω,X,φ ) on R2n for which φ has
no other critical points besides the minimum is symplectomorphic to the stan-
dard structure on R2n. On the other hand, as we already pointed out, homotopic
Weinstein structures are symplectomorphic. Seidel–Smith [167], McLean [137] and
Abouzaid–Seidel [3] have recently constructed for each n≥ 3 inﬁnitely many “ex-
otic” Weinstein sructures on R2n which are not symplectomorphic to the standard
one and which, moreover, are pairwise non-symplectomorphic. Then Theorem 1.1
(a) allows us to transform these Weinstein structures to Stein structures which are
not Stein homotopic among each other and to Cn, in particular they do not admit
exhausting J-convex functions without critical points of positive index.
One can also reformulate this result as a failure of the following “ J-convex h-
cobordism problem”: Let W be a smooth cobordism between manifolds ∂−W and
∂+W . A Stein structure on W is a complex structure J on W which admits a
J-convex function φ : W→ R which has ∂±W as its regular level sets. Then the
above results by Abouzaid, McLean, Seidel and Smith imply that for each n≥ 3
there exists a Stein cobordism (W,J ) diﬀeomorphic to S2n−1× [0, 1] for which the
correspondingJ-convex function φ cannot be chosen without critical points.
By contrast, we prove the following uniqueness theorem in complex dimension
two (ﬁrst sketched in [47]; for the diﬀeomorphism part see [ 83, 43, 133]).
Theorem 1.7. Let (W,J ) be a minimal compact complex surface withJ-convex
boundary diﬀeomorphic toS3. Suppose that there exists a symplectic form ω taming
J, i.e., such that ω is positive on complex directions. Then W is diﬀeomorphic to
the 4-ball and admits a J-convex Morse function φ :W→ R which is constant on
∂W and has no other critical points besides the minimum.
Here a complex surface (i.e., a complex manifold of complex dimension 2) is
called minimal if it contains no embedded holomorphic spheres of self-intersection
−1. See Chapter 16 for a discussion of related uniqueness results due to McDuﬀ,
Hind, Wendl and others.
It turns out that the Weinstein problems can be reduced to diﬀerential topology
in the subcritical case when the Morse functions have no middle-dimensional critical
points. Moreover, based on work of Murphy [ 143] who discovered that in contact
manifolds of dimension > 3 there is a class of Legendrian knots which obey an h-
principle, we deﬁne a larger class of ﬂexible Weinstein manifolds for which problems
of symplectic topology can be reduced to diﬀerential topology. For example, we have
Theorem 1.8. LetV be a manifold of dimension 2n⁄= 4, Ω a homotopy class of
non-degenerate (not necessarily closed)2-forms onV , andφ :V → R an exhausting
Morse function without critical points of index >n . Then:
(a) There exists a ﬂexible Weinstein structure (ω,X,φ ) on V with ω∈ Ω, and
this structure is unique up to Weinstein homotopy.
(b) Every diﬀeomorphism of V preserving the homotopy class Ω is diﬀeotopic
to a symplectomorphism of (V,ω ).
Another application of the ﬂexible technique is the following
Theorem 1.9. Let (V,J ) be a contractible Stein manifold. Then V× C ad-
mits an exhausting J-convex Morse function with exactly one critical point, the
minimum.

8 1. INTRODUCTION
For our ﬁnal application, recall that thepseudo-isotopy problem in diﬀerentiable
topology concerns the topology of the spaceE(M) of functions onM×[0, 1] without
critical points that are constant on M× 0 and M× 1. Work of Cerf, Hatcher–
Wagoner, Igusa and Waldhausen has led to a description ofπ0E(M) for dimM≥ 7
in terms of algebraic K-theory.
Given a topologically trivial Stein cobordism (M× [0, 1],J ) one can ask about
the topology of the space E(M× [0, 1],J ) of J-convex functions without critical
points that are constant onM×0 andM×1 (provided that this space is non-empty).
Understanding of the topology of the inclusion map I :E(M× [0, 1],J )→E (M) is
the content of the J-convex pseudo-isotopy problem. We prove the following result
in this direction.
Theorem 1.10. If dim M >3 and the Stein structure J is ﬂexible, the homo-
morphismI∗ :π0E(M× [0, 1],J )→π0E(M) is surjective.
We conjecture thatI∗ is an isomorphism.
1.2. Plan of the book
This book is organized as follows.
In Chapters 2 and 3 we explore basic properties and examples ofJ-convex func-
tions and hypersurfaces. In particular, we prove Richberg’s theorem on smoothing
of J-convex functions and derive several important corollaries.
In Chapter 4 we construct special hypersurfaces that play a crucial role in
extending J-convex functions over handles.
The next two chapters contain background material which is standard but
sometimes not easy to ﬁnd in the literature. The necessary complex analytic back-
ground is discussed in Chapter 5, and the symplecto-geometric one in Chapter 6.
In Chapter 7 we review several h-principles which we use in this book. We
begin with a review of the Smale-Hirsch immersion theory and Whitney’s theory
of embeddings. We then discuss Gromov’s results about symplectic and contact
isotropic immersions and embeddings, Murphy’s h-principle for loose Legendrian
knots, and Gromov’s theory of directed embeddings and immersions with appli-
cations to totally real embeddings. We ﬁnish this chapter with an h-principle for
totally real discs with Legendrian boundaries, which we deduce from previously
discussed h-principles and which plays an important role in the proofs of the main
results of this book.
Theorem 1.5 is proved in Chapter 8. This chapter also contains several new
results concerning surrounding of subsets by J-convex hypersurfaces, with applica-
tions to holomorphic and polynomial convexity. We also prove here several reﬁne-
ments of Theorem 1.5, some of which are due to Gompf and Forstneriˇ c–Slapar.
In Chapter 9 we review Morse-Smale theory and the h-cobordism theorem.
In particular, we discuss basic facts concerning gradient-like vector ﬁelds. We
also review the “two-index theorem” of Hatcher and Wagoner and basic notions
of pseudo-isotopy theory.
In Chapter 10 we develop a Morse-Smale type theory for J-convex functions.
In particular, we show how the Morse-theoretic operations which are used in the
proof of the h-cobordism theorem – reordering of critical points, handle-slides, and
cancellation of critical points – can be performed in the class of J-convex functions.
In Chapter 11 we introduce Weinstein structures and study their basic proper-
ties. We discuss Stein and Weinstein homotopies, and we introduce the classes of

1.2. PLAN OF THE BOOK 9
subcritical and ﬂexible manifolds which play an important role for the “road from
Morse to Weinstein”.
In Chapter 12 we discuss modiﬁcations of Weinstein structures near critical
points and stable manifolds and prove Weinstein analogues of the results proven in
Chapter 10 for J-convex functions.
In Chapter 13 we prove a more precise version of Theorem 1.5 by ﬁrst con-
structing a Weinstein structure and then proving Theorem 1.1 (a).
Chapters 14 and 15 contain our main results about deformations of Weinstein
and Stein structures. In Chapter 14 we classify ﬂexible Weinstein structures up
to homotopy and show that the problem of simpliﬁcation of the Morse function
corresponding to a ﬂexible Weinstein structure can be reduced to Morse-Smale
theory. In particular, we prove Theorem 1.8.
In Chapter 15 we show that every Weinstein homotopy can be transformed to
a Stein homotopy. In particular, we prove Theorem 1.1 (b) and (c) and deduce
various corollaries including Theorems 1.9 and 1.10.
Chapter 16 concerns the situation in complex dimension 2. In particular, we
discuss the method of ﬁlling by holomorphic discs and prove Theorem 1.7. We also
discuss the classiﬁcation of Stein ﬁllings of 3-dimensional contact manifolds and
review known results about Stein surfaces.
Finally, in Chapter 17 we sketch McLean’s construction of exotic Stein struc-
tures in higher dimension and explain how they are distinguished by symplectic
homology.
Notation. Throughout this book we use the following notation: For a subset
A⊂ X of a topological space we denote by Int A and ¯A its interior resp. closure,
and A⋐B means that ¯A is a compact subset of Int B. For A closed we denote by
OpA a suﬃciently small ( but not speciﬁed) open neighborhood of A.
Manifolds are always assumed to be smooth and second countable.



Part 1
J-Convexity



2
J-Convex Functions and Hypersurfaces
In this chapter we introduce the notion of J-convexity for functions and hy-
persurfaces and discuss their relation. After considering some basic properties and
examples, we derive an explicit formula for the normalized Levi form on Cn.
2.1. Linear algebra
A complex vector space (V,J ) is a real vector space V of dimension 2n with
an endomorphism J satisfying J2 =−Id. Scalar multiplication of v ∈ V with
a +ib∈ C is then deﬁned by (a +ib)v :=av +bJv. A Hermitian form on (V,J ) is
an R-bilinear mapH :V×V → C which is C-linear in the ﬁrst variable and satisﬁes
H(X,Y ) = H(Y,X ). If H is, moreover, positive deﬁnite it is called a Hermitian
metric. We can write a Hermitian form H uniquely as
H =g−iω,
where g is a symmetric and ω a skew-symmetric bilinear form on the real vector
space V . The forms g and ω determine each other:
g(X,Y ) =ω(X,JY ), ω (X,Y ) =g(JX,Y )
for X,Y ∈ V . Moreover, the forms ω and g are invariant under J, which can be
equivalently expressed by the equation
ω(JX,Y ) +ω(X,JY ) = 0.
Conversely, given a skew-symmetricJ-invariant formω, we can uniquely reconstruct
the corresponding Hermitian form H:
(2.1) H(X,Y ) :=ω(X,JY )−iω(X,Y ).
For example, consider the complex vector space ( Cn,i ) with coordinates z1 =x1 +
iy1,...,z n =xn +iyn. It carries the standard Hermitian metric
(v,w ) :=
n∑
j=1
vj ¯wj =⟨v,w⟩− iωst(v,w ),
where⟨·,·⟩ is the Euclidean metric andωst =∑n
j=1dxj∧dyj the standard symplectic
form on Cn.
For a symmetric bilinear form Q : V×V → R we denote the corresponding
quadratic form
Q :V → R, Q (v) :=Q(v,v )
by the same letter. Recall that the symmetric bilinear form can be recovered from
the quadratic form by
Q(v,w ) = 1
2
(
Q(v +w)−Q(v)−Q(w)
)
.
13

14 2. J-CONVEX FUNCTIONS AND HYPERSURFACES
We can uniquely decompose a quadratic form on a complex vector space (V,J ) into
its complex linear and antilinear parts,
Q(v) =QC(v) + ¯QC(v),
QC(v) = 1
2
(
Q(v) +Q(Jv)
)
=QC(Jv),
¯QC(v) = 1
2
(
Q(v)−Q(Jv)
)
=− ¯QC(Jv).
The quadratic form Q is called J-convex if QC(v)> 0 for all v⁄= 0.
Example 2.1. For the quadratic form
(2.2) Q(z) =
n∑
j=1
(λjx2
j +µjy2
j )
on Cn we haveQC(z) = 1
2
∑
j(λj +µj)|zj|2. So Q is i-convex if and only if
(2.3) λj +µj > 0 for all j = 1,...,n.
Note that geometric convexity implies i-convexity but not conversely, since i-con-
vexity only requires that the average of the coeﬃcients over each complex line is
positive.
In fact, this example captures all i-convex quadratic forms:
Lemma 2.2. Every i-convex quadratic form Q: Cn → R can be put in the
form (2.2) by a complex linear change of coordinates, where the coeﬃcients λj,µj
satisfy (and are uniquely determined by) the conditions
(2.4) λj +µj = 2, λ j≥µj, µ 1≤µ2≤···≤ µn.
Proof. A general quadratic function can be uniquely decomposed into its
complex linear and antilinear parts as
Q(z) =
∑
ij
aijzi¯zj + Re

∑
ij
bijzizj

, a ij = ¯aji, bij =bji.
Under a complex linear coordinate change zi↦→∑
kcikzk the matrices A = (aij)
and B = (bij) transform as
A↦→CtA ¯C, B ↦→CtBC
for C = (cij)∈GL(n, C). Using this, we can ﬁrst transform the Hermitian matrix
A to a diagonal matrix with entries 0 or±1. Since A represents the complex linear
part QC, which is positive by hypothesis, we obtain A = Id. Now we can still
transform B according to B ↦→ CtBC for unitary matrices C (thus preserving
A = Id). By a lemma of Schur (see e.g. [ 183]), using this we can transform B to a
diagonal matrix with nonnegative real entries νi and thus Q to
Q(z) =
n∑
j=1
(
|zj|2 +νjRe (z2
j )
)
=
n∑
j=1
(
(1 +νj)x2
j + (1−νj)y2
j
)
.
□

2.2. J-CONVEX FUNCTIONS 15
Of course, using rescalings zj↦→ rjzj we can vary the form of Q, e.g. to the
following one that will be useful:
(2.5) Q(z) =
k∑
j=1
(λjx2
j−y2
j ) +
n∑
j=k+1
(λjx2
j +y2
j ), λ j > 0.
2.2. J-convex functions
An almost complex structure on a smooth manifold V of real dimension 2n is
an endomorphismJ :TV →TV satisfyingJ2 =−Id on each ﬁber. The pair (V,J )
is called an almost complex manifold . It is called a complex manifold if the almost
complex structure J is integrable, i.e., J is induced by complex coordinates on V .
By the theorem of Newlander and Nirenberg [ 149], a (suﬃciently smooth) almost
complex structure J is integrable if and only if its Nijenhuis tensor
N(X,Y ) := [JX,JY ]− [X,Y ]−J[X,JY ]−J[JX,Y ], X,Y ∈TV,
vanishes identically. An integrable almost complex structure is called a complex
structure.
In the following let (V,J ) be an almost complex manifold. To a smooth function
φ :V → R we associate the 2-form
ωφ :=−ddCφ,
where the diﬀerential operator dC is deﬁned by
dCφ(X) :=dφ(JX )
for X∈TV . The form ωφ is in general not J-invariant. However, it is J-invariant
if J is integrable. To see this, consider the complex vector space ( Cn,i ). Given a
function φ : Cn→ R, deﬁne the complex valued (1, 1)-form
∂ ¯∂φ :=
n∑
i,j=1
∂2φ
∂zi∂¯zj
dzi∧d¯zj.
Using the identities
dzj◦i =idzj, d ¯zj◦i =−id ¯zj
we compute
dCφ =
∑
j
(∂φ
∂zj
dzj◦i + ∂φ
∂¯zj
d¯zj◦i
)
=
∑
j
(
i∂φ
∂zj
dzj−i∂φ
∂¯zj
d¯zj
)
,
ddCφ =−2i
∑
i,j
∂2φ
∂zi∂¯zj
dzi∧d¯zj.
Hence
(2.6) ωφ = 2i∂ ¯∂φ
and the i-invariance ofωφ follows from the invariance of ∂ ¯∂φ.
A function φ : V → R on an almost complex manifold is called J-convex 1 if
ωφ(X,JX ) > 0 for all nonzero tangent vectors X. If ωφ is J-invariant it deﬁnes
1Throughout this book, by convexity and J-convexity we will always mean strict convexity
and J-convexity. Non-strict (J-)convexity will be referred to as weak (J-)convexity.

16 2. J-CONVEX FUNCTIONS AND HYPERSURFACES
by (2.1) a unique Hermitian form
Hφ :=gφ−iωφ, g φ :=ωφ(·,J·)
and φ is J-convex if and only if the Hermitian form Hφ is positive deﬁnite.
Example 2.3. Let f : Cn⊃ U→ C be holomorphic. Then |f|2 is weakly i-
convex. Moreover, outside the zero set of f the function log|f| satisﬁesddC(log|f|)
= 0.
From (2.6) we can derive a simple expression for the form Hφ associated to a
functionφ : Cn→ R in terms of the Hermitian matrix aij := ∂2φ
∂zi∂¯zj
. For v,w ∈ Cn
we have
ωφ(v,w ) = 2i
∑
ij
aijdzi∧d¯zj(v,w ) = 2i
∑
ij
aij(vi ¯wj−wi¯vj)
= 2i
∑
ij
(aijvi ¯wj− ¯aij¯viwj) =−4 Im
(∑
ij
aijvi ¯wj
)
,
hence
(2.7) Hφ(v,w ) = 4
n∑
i,j=1
∂2φ
∂zi∂¯zj
vi ¯wj.
The Hermitian form Hφ is related to the (real) Hessian Hessφ (given by the matrix
of real second derivatives) as follows:
Hessφ(v,w ) =
∑
ij
( ∂2φ
∂zi∂zj
viwj + ∂2φ
∂¯zi∂¯zj
¯vi ¯wj + ∂2φ
∂zi∂¯zj
vi ¯wj + ∂2φ
∂¯zi∂zj
¯viwj
)
= 2Re
∑
ij
( ∂2φ
∂zi∂zj
viwj + ∂2φ
∂zi∂¯zj
vi ¯wj
)
,
and hence
Hessφ(v,w ) + Hessφ(iv,iw ) = 4 Re
∑
ij
∂2φ
∂zi∂¯zj
vi ¯wj =gφ(v,w ).
In particular, the corresponding quadratic forms Hφ(v) =Hφ(v,v ) and Hessφ(v) =
Hessφ(v,v ) satisfy
(2.8) Hφ(v) = Hessφ(v) + Hessφ(iv),
i.e., Hφ is twice the complex average of Hess φ.
The (Morse) index of a critical point of φ is the maximal dimension of a
subspace on which the real Hessian Hessφ is negative deﬁnite. The normal form (2.5)
shows
Corollary 2.4. The Morse index of a critical point of an i-convex function
φ : Cn→ R is at most n.
This corollary is fundamental for the topology of Stein manifolds. We will give
an alternative proof in Section 2.8 and generalize it to almost complex manifolds
in Section 3.1.
The relation (2.8) generalizes to K¨ ahler manifolds, as we will explain now. We
refer to [12] for basic facts about K¨ ahler geometry. AK¨ ahler manifoldis a complex
manifold (V,J ) with a Hermitian metricH =g−iω satisfying the K¨ ahler condition

2.3. THE LEVI FORM OF A HYPERSURFACE 17
dω = 0. Alternatively, the K¨ ahler condition can be expressed as∇J = 0, i.e., the
complex structure J is parallel with respect to the Levi-Civita connection ∇ of the
metric g.
Using the metric g =⟨ , ⟩ we associate to a smooth function φ : V → R its
gradient vector ﬁeld ∇φ deﬁned by dφ =⟨∇φ,·⟩ and its (real) Hessian Hessφ :
TpV×TpV → R deﬁned by
Hess(X,Y ) :=⟨∇X∇φ,Y⟩ =X·dφ(Y )−dφ(∇XY ).
Torsion freeness of the Levi-Civita connection and d(dφ) = 0 yields the symmetry
Hess(X,Y ) = Hess(Y,X ). On a K¨ ahler manifold we use ∇J = 0 to compute for
λφ :=−dCφ:
dλφ(X,JY ) =X·λφ(JY )− (JY )·λφ(X)−λφ([X,JY ])
=X·λφ(JY )− (JY )·λφ(X)−λφ(J∇XY−∇JYX)
=X·dφ(Y ) + (JY )·dφ(JX )−dφ(∇XY )−dφ(∇JYJX )
= Hessφ(X,Y ) + Hessφ(JX,JY ).
So we have shown
Proposition 2.5. For a smooth function φ :V → R on a K¨ ahler manifold the
Hermitian form Hφ is related to the real Hessian Hessφ by
Hφ(X) = Hessφ(X) + Hessφ(JX ).
□
2.3. The Levi form of a hypersurface
Let Σ be a smooth (real) hypersurface in an almost complex manifold ( V,J ).
Each tangent space TpΣ⊂ TpV , p∈ Σ, contains a unique maximal complex sub-
space ξp⊂TpΣ which is given by
ξp =TpΣ∩JTpΣ.
These subspaces form a codimension one distribution ξ⊂ T Σ which we will refer
to as the ﬁeld of complex tangencies . Suppose that Σ is cooriented by a transverse
vector ﬁeld ν to Σ in V such that Jν is tangent to Σ. The hyperplane ﬁeld ξ can
be deﬁned by a Pfaﬃan equation {α = 0}, where the sign of the 1-form α is ﬁxed
by the condition α(Jν )> 0. The 2-form
ωΣ :=dα|ξ
is then deﬁned uniquely up to multiplication by a positive function. As in the
previous section we may ask whether ωΣ isJ-invariant. The following lemma gives
a necessary and suﬃcient condition in terms of the Nijenhuis tensor.
Lemma 2.6. Let (V,J ) be an almost complex manifold. The form ωΣ is J-
invariant for a hypersurface Σ⊂V if and only if N|ξ×ξ takes values in ξ. The form
ωΣ is J-invariant for every hypersurface Σ⊂ V if and only if for all X,Y ∈ TV ,
N(X,Y ) lies in the complex plane spanned by X and Y . In particular, this is the
case if J is integrable or if V has complex dimension 2.

18 2. J-CONVEX FUNCTIONS AND HYPERSURFACES
Proof. Let Σ⊂ V be a hypersurface and α a deﬁning 1-form for ξ. Extend
α to a neighborhood of Σ such that α(ν) = 0. For X,Y ∈ξ we have [X,Y ]∈T Σ
and therefore J[X,Y ] =aν +Z for some a∈ R and Z∈ξ. This shows that
α(J[X,Y ]) = 0
for all X,Y ∈ ξ. Applying this to various combinations of X, Y , JX and JY we
obtain
α
(
N(X,Y )
)
=α([JX,JY ])−α([X,Y ]),
α
(
JN (X,Y )
)
=α([X,JY ]) +α([JX,Y ]).
The form ωΣ is given by
ωΣ(X,Y ) = 1
2
(
X·α(Y )−Y·α(X)−α([X,Y ]
)
=−1
2α([X,Y ]).
Inserting this in the formulae above yields
−1
2α
(
N(X,Y )
)
=ωΣ(JX,JY )−ωΣ(X,Y ),
−1
2α
(
JN (X,Y )
)
=ωΣ(X,JY ) +ωΣ(JX,Y ).
Hence the J-invariance ofωΣ is equivalent to
α
(
N(X,Y )
)
=α
(
JN (X,Y )
)
= 0,
i.e., N(X,Y )∈ ξ for all X,Y ∈ ξ. This proves the ﬁrst statement and the ‘if’ in
the second statement. For the ‘only if’ it suﬃces to note that if N(X,Y ) does not
lie in the complex plane spanned by X andY for some X,Y ∈TV , then we ﬁnd a
hypersurface Σ such that X,Y ∈ξ and N(X,Y ) /∈ξ. □
A hypersurface Σ is called Levi-ﬂat if ωΣ≡ 0. This is exactly the Frobenius
integrability condition for the ﬁeld of complex tangencies ξ on Σ. Hence, on a
Levi-ﬂat hypersurface, ξ integrates to a real codimension 1 foliation.
The hypersurface Σ is called J-convex (resp. weaklyJ-convex) if ωΣ(X,JX )>
0 (resp.≥ 0) for all nonzero X∈ξ. If ωΣ isJ-invariant it deﬁnes a Hermitian form
LΣ on ξ by the formula
LΣ(X,Y ) :=ωΣ(X,JY )−iωΣ(X,Y )
forX,Y ∈ξ. The Hermitian form LΣ is called the Levi form of the (cooriented) hy-
persurface Σ. We will also use the notationLΣ(X) for the quadratic formLΣ(X,X ).
Note that Σ is Levi-ﬂat if and only if LΣ≡ 0, and J-convex if and only if LΣ is
positive deﬁnite. We will sometimes also refer to ωΣ as the Levi form. As pointed
out above, the Levi form is deﬁned uniquely up to multiplication by a positive
function.
Given aJ-convex hypersurface and a deﬁning 1-form α for the ﬁeld of complex
tangenciesξ, the 2-formdα has rank dimR Σ−1. Hence there exists a unique vector
ﬁeld R on Σ satisfying the conditions
α(R) = 1, i Rdα = 0.
If the hypersurface Σ is given as a regular level set{φ = 0} of a functionφ :V → R,
then we can choose α =−dCφ as the 1-form deﬁning ξ (with the coorientation of

2.3. THE LEVI FORM OF A HYPERSURFACE 19
Σ given by dφ). Thus the Levi form is given by
ωΣ(X,Y ) =−ddCφ(X,Y ) =ωφ(X,Y ).
This shows that regular level sets of a J-convex function φ are J-convex (being
cooriented by dφ). It turns out that the converse is also almost true (similarly to
the situation for convex functions and hypersurfaces):
Lemma 2.7. Let φ : V → R be a smooth function on an almost complex ma-
nifold without critical points such that all its level sets are compact and J-convex.
Then one can ﬁnd a convex increasing functionf : R→ R such that the composition
f◦φ is J-convex.
Proof. For a function f : R→ R we have
dC(f◦φ) =f′◦φd Cφ,
ωf◦φ =−ddC(f◦φ) =−f′′◦φdφ ∧dCφ +f′◦φω φ.
ByJ-convexity of the level sets, there is a unique vector ﬁeld R onV associated as
above to the deﬁning 1-form−dCφ for the ﬁelds of complex tangencies ξ satisfying
dφ(R) = 0, −dCφ(R) = 1, i Rωφ|ξ = 0.
Then TV = RR⊕ RJR⊕ξ and for Y ∈ξ we have
ωf◦φ(R,Y ) =ωf◦φ(R,JY ) = 0, ω f◦φ(Y,JY ) =f′◦φω φ(Y,JY )> 0.
Let us pick a J-invariant metric onTV = RR⊕ RJR⊕ξ satisfying|R| =|JR| = 1
and ωφ(Y,JY )≥| Y|2 for Y ∈ ξ. Using −dφ∧dCφ(R,JR ) = 1, we compute for
X =aR +bJR +Y ∈TV = RR⊕ RJR⊕ξ:
ωf◦φ(X,JX ) = (a2 +b2)[f′′ +f′ωφ(R,JR )] +bf′ωφ(JR,JY )
+af′ωφ(Y,JR ) +f′ωφ(Y,JY ),
where we have abbreviatedf′ =f′◦φ andf′′ =f′′◦φ. By compactness of the level
sets there exists a smooth functionh : R→ [1,∞) satisfyingh(y)≥ 2max{φ=y}|ωφ|.
Abbreviating h =h◦φ and using h2≥h, we can estimate
ωf◦φ(X,JX )≥ (a2 +b2)[f′′−h2f′]−hf′
√
a2 +b2|Y| +f′|Y|2
≥ (a2 +b2)[f′′− 3
2h2f′] + 1
2f′|Y|2.
Now solve the linear diﬀerential equationf′′(y) = 2h(y)2f′(y) with initial condition
f′(y0)> 0. The solution exists for all y∈ R and satisﬁesf′ > 0, sof◦φ isJ-convex
in view of
ωf◦φ(X,JX )≥ 1
2f′[(a2 +b2)h2 +|Y|2]> 0.
□
Remark 2.8. The proof of the preceding lemma also shows: If φ : V → R
is J-convex, then f◦φ is J-convex for any function f : R→ R with f′ > 0 and
f′′≥ 0.
Remark 2.9. Consider a hypersurface Σ in an almost complex manifold (V,J )
and an almost complex submanifold W ⊂ V transverse to Σ. Then Σ ∩W is a
hypersurface in (W,J ) with ﬁeld of complex tangencies ξ∩TW and the Levi form
of Σ∩W equals the restriction ofLΣ toξ∩TW . In particular, Σ is J-convex if and

20 2. J-CONVEX FUNCTIONS AND HYPERSURFACES
only if Σ∩W is J-convex for all almost complex submanifolds W⊂V transverse
to Σ of complex dimension 2.
2.4. Completeness
A vector ﬁeld is called complete if its ﬂow exists for all forward and backward
times. For a J-convex function φ, we deﬁne its gradient∇φφ with respect to gφ =
ωφ(·,J·) by dφ = gφ(∇φφ,·). (Note that gφ is nondegenerate but not necessarily
symmetric.) In general, ∇φφ need not be complete:
Example 2.10. The function φ(z) :=
√
1 +|z|2 on C satisﬁes
∂2φ
∂z∂ ¯z = ∂
∂z
z√
1 +|z|2 = 1
√
1 +|z|23,
so gφ = 4(1 +|z|2)−3/2⟨ , ⟩, where⟨ , ⟩ is the standard metric. In particular, φ is
i-convex. Its gradient is determined from
dφ = xdx +ydy√
1 +|z|2 = 4
√
1 +|z|23⟨∇φφ,·⟩,
thus∇φφ = 1+|z|2
4 (x ∂
∂x +y ∂
∂y ). A gradient line γ(t) with |γ(0)| = 1 is given by
γ(t) = h(t)γ(0), where h(t) satisﬁes h′ = 1+h2
4 h. This shows that γ(t) tends to
inﬁnity in ﬁnite time, hence the gradient ﬁeld ∇φφ is not complete.
However, the gradient ﬁeld ∇φφ can always be made complete by composing
φ with a suﬃciently convex function. Recall that a function φ : V → R is called
exhausting if it is proper and bounded from below.
Proposition 2.11. Let φ : V → [a,∞) be an exhausting J-convex function
on an almost complex manifold. Then for any diﬀeomorphism f : [a,∞)→ [b,∞)
such that f′′ > 0 and limy→∞f′(y) = ∞, the function f◦φ is J-convex and its
gradient vector ﬁeld is complete.
Proof. The function ψ :=f◦φ satisﬁes
ddCψ =f′′◦φdφ ∧dCφ +f′◦φdd Cφ.
In particular, ψ is J-convex if f′ > 0 and f′′ > 0. We have
gψ(X,Y ) =−ddCψ(X,JY )
= +f′′◦φ [dφ(X)dφ(Y ) +dCφ(X)dCφ(Y )] +f′◦φg φ(X,Y ).
Let us compute the gradient ∇ψψ. We will ﬁnd it in the form
∇ψψ =λ∇φφ
for a function λ :V → R. The gradient is determined by
gψ(∇ψψ,Y ) =dψ(Y ) =f′◦φdφ (Y )
for any vector Y ∈TV . Using dφ(∇φφ) =gφ(∇φφ,∇φφ) =:|∇φφ|2 anddCφ(∇φφ)
=gφ(∇φφ,J∇φφ) = 0, we compute the left hand side as
gψ(∇ψψ,Y )
=λ
{
f′′◦φ [dφ(∇φφ)dφ(Y ) +dCφ(∇φφ)dCφ(Y )] +f′◦φg φ(∇φφ,Y )
}
=λ{f′′◦φ|∇φφ|2dφ(Y ) +f′◦φdφ (Y )}.

2.5. J-CONVEXITY AND GEOMETRIC CONVEXITY 21
Comparing with the right side, we ﬁnd
λ = f′◦φ
f′′◦φ|∇φφ|2 +f′◦φ.
Since φ is proper, we only need to check completeness of the gradient ﬂow for
positive times. Consider an unbounded gradient trajectory γ : [0,T )→ V , i.e., a
solution of
dγ
dt (t) =∇φφ
(
γ(t)
)
, lim
t→T
φ
(
γ(t)
)
=∞.
HereT can be ﬁnite or +∞. The function φ maps the image of γ diﬀeomorphically
onto some interval [c,∞). It pushes forward the vector ﬁeld ∇φφ (which is tangent
to the image of γ) to the vector ﬁeld
φ∗(∇φφ) =h(y) ∂
∂y,
where t and y are the coordinates on [0,T ) and [c,∞), respectively, and
h(y) :=|∇φφ|2(
φ−1(y)
)
> 0.
Similarly,φ pushes forward∇ψψ =λ∇φφ to the vector ﬁeld
φ∗(∇ψψ) =λ
(
φ−1(y)
)
h(y) ∂
∂y = f′(y)h(y)
f′′(y)h(y) +f′(y)
∂
∂y =:v(y).
Hence completeness of the vector ﬁeld ∇ψψ on the trajectory γ is equivalent to
the completeness of the vector ﬁeld v on [c,∞). An integral curve of v satisﬁes
dy
ds =v(y), or equivalently,
ds = f′′(y)h(y) +f′(y)
f′(y)h(y) dy.
Thus completeness of the vector ﬁeld v is equivalent to
+∞ =
∫ ∞
c
f′′(y)h(y) +f′(y)
f′(y)h(y) dy =
∫ ∞
c
f′′(y)dy
f′(y) +
∫ ∞
c
dy
h(y).
The ﬁrst integral on the right hand side is equal to
∫∞
c d
(
lnf′(y)
)
, so it diverges if
and only if limy→∞f′(y) =∞. □
We will call an exhausting J-convex function completely exhausting if its gra-
dient vector ﬁeld∇φφ is complete.
2.5. J-convexity and geometric convexity
Next we investigate the relation between i-convexity and geometric convexity.
Consider Cn = Cn−1⊕ C with coordinates (z1,...,z n−1,u +iv). Let Σ ⊂ Cn be
a hypersurface which is given as a graph {u = f(z,v )} for some smooth function
f : Cn−1⊕ R→ R. Assume that f(0, 0) = 0 and df(0, 0) = 0. Every hypersurface
in a complex manifold can be locally written in this form.
The Taylor polynomial of second order of f around (0, 0) can be written as
(2.9) T2f(z,v ) =
∑
i,j
aijzi¯zj + 2 Re
∑
i,j
bijzizj +vl (z, ¯z) +cv2,

22 2. J-CONVEX FUNCTIONS AND HYPERSURFACES
where l is some linear function of z and ¯z, and aij = ∂2f
∂zi∂¯zj
(0, 0). Let Σ be
cooriented by the gradient of the function f(z,v )−u. Then the 2-form ωΣ at the
point 0 is given on X,Y ∈ξ0 = Cn−1 by
(2.10)
ωΣ(X,Y ) = 2i∂ ¯∂f (X,Y ) = 2i
∑
i,j
aijdzi∧d¯zj(X,Y )
= 2i
∑
i,j
aij(Xi ¯Yj− ¯XjYi) = 2 Re
(
2i
∑
i,j
aijXi ¯Yj
)
=−4 Im (AX,Y ),
whereA is the Hermitian (n− 1)× (n− 1) matrix with entries aij. Hence the Levi
form at 0 is
LΣ = 4(A·,·).
If the function f is (strictly) convex, then
T2f(z, 0) +T2f(iz, 0) = 2
∑
ij
aijzi¯zj
is positive for all z ⁄= 0, so the Levi form is positive deﬁnite. This shows that
geometric convexity of Σ implies i-convexity. The converse is not true, see the ﬁrst
example in Section 2.7 below. It is true, however, locally after a biholomorphic
change of coordinates.
Proposition 2.12 (Narasimhan) . A hypersurface Σ⊂ Cn is i-convex if and
only if it can be made geometrically convex in a neighborhood of each of its points
by a biholomorphic change of coordinates.
Proof. The ‘if’ follows from the discussion above and the invariance of i-
convexity under biholomorphic maps. For the converse write Σ in local coordinates
as a graph{u =f(z,v )} as above and consider its second Taylor polynomial (2.9).
Let w = u +iv and perform in a neighborhood of 0 the biholomorphic change of
coordinates ~w−~u +i~v :=w− 2∑
ijbijzizj. Then ~v =v +O(2) and
~u =
∑
aijzi¯zj +~vl (z, ¯z) +c~v2 +O(3).
After another local change of coordinates w′ =u′ +iv′ := ~w−λ~w2,λ∈ R, we have
v′ =~v +O(2) and
u′ =~u +λ(v′)2 +O(3) =
∑
aijzi¯zj +v′l(z, ¯z) + (c +λ)(v′)2 +O(3).
Forλ suﬃciently large the quadratic form on the right hand side is positive deﬁnite,
so the hypersurface Σ is geometrically convex in the coordinates ( z,w′). □
2.6. Normalized Levi form and mean normal curvature
In a general (almost) complex manifold (V,J ) the Levi formLΣ of a cooriented
hypersurface Σ is invariantly deﬁned only up to multiplication by a positive func-
tion. However, any Hermitian metric H = g−iω on (V,J ) provides a canonical
choice of deﬁning 1-form α =iνω, where ν is the unit normal vector ﬁeld along Σ
deﬁning the coorientation. In this case, we will call the form
LΣ(X) :=d(iνω)(X,JX )

2.6. NORMALIZED LEVI FORM AND MEAN NORMAL CURVATURE 23
the normalized Levi form of Σ. Note that if Σ = φ−1(0) for a function φ :V → R
with|∇φ(p)| = 1, then the 1-forms iνω and−dCφ coincide at p and thus
(2.11) LΣ(X) =−ddCφ(X,JX ), X ∈TpΣ.
In certain situations the normalized Levi form can be expressed in terms of curva-
ture, as we will now explain.
Consider ﬁrst a cooriented hypersurface Σ in Rn with the Euclidean metric
⟨ , ⟩. Its second fundamental form
IIΣ :T Σ→ R
can be deﬁned as follows. ForX∈TxΣ letγ : (−ϵ,ϵ )→ Σ be a curve withγ(0) =x
and ˙γ(0) =X. Then
IIΣ(X) :=−⟨¨γ(0),ν⟩,
whereν is the unit normal vector to Σ in x deﬁning the coorientation. The matrix
representing the second fundamental form equals the diﬀerential of the Gauss map
which associates to every point its unit normal vector. Our sign convention is
chosen in such a way that the unit sphere in Rn has positive principal curvatures
if it is cooriented by the outward pointing normal vector ﬁeld. The mean normal
curvature along a k-dimensional subspace S⊂TxΣ is deﬁned as
1
k
k∑
i=1
IIΣ(vi)
for some orthonormal basis v1,...,v k of S. If Σ is given as a graph {xn =
f(x1,...,x n−1)} with f(0) = 0 and df(0) = 0, then for X∈ Rn−1 we can choose
the curve
γ(t) :=
(
tX,f (tX)
)
in Σ. Taking the second derivative we obtain
(2.12) IIΣ(X) =
∑
ij
∂2f
∂xi∂xj
(0)XiXj = 2T2f(X),
whereT2f is the second order Taylor polynomial and Σ is cooriented by the gradient
of the function f−xn. This leads to the following geometric characterization of
i-convexity.
Proposition 2.13. The normalized Levi form of a cooriented hypersurface
Σ⊂ Cn with respect to the standard complex structurei and the standard Hermitian
metric is given at a point z∈ Σ by
(2.13) LΣ(X) =IIΣ(X) +IIΣ(iX)
for X ∈ TzΣ. Thus Σ is i-convex if and only if at every point z∈ Σ the mean
normal curvature along any complex line in TzΣ is positive.
Proof. Write Σ locally as a graph{u =f(z,v )} withf(0, 0) = 0 anddf(0, 0) =
0, and such that the gradient of φ =f−u deﬁnes the coorientation of Σ. Consider
the second Taylor polynomial (2.9) off in (0, 0). In view of (2.12) and (2.10), twice

24 2. J-CONVEX FUNCTIONS AND HYPERSURFACES
the mean normal curvature along the complex line generated by X∈ Cn−1 is given
by
IIΣ(X) +IIΣ(iX) = 2
(
T2f(X) +T2f(iX)
)
= 4
∑
ij
aijXi ¯Xj
=−ddCf(X,iX ) =−ddCφ(X,iX ) = LΣ(X).
Here the last equality follows from (2.11), since the gradient of the functionφ =f−u
has norm 1 at the point (0 , 0, 0). □
Proposition 2.13 generalizes to hypersurfaces in K¨ ahler manifolds as follows.
Consider a cooriented hypersurface Σ in a K¨ ahler manifold (V,J,ω ). Denote by ν
the outward pointing unit normal vector ﬁeld along Σ and deﬁne the vector ﬁeld
τ :=Jν tangent to Σ. Then the ﬁeld of complex tangencies ξ on T Σ is the kernel
of the 1-form
α :=g(τ,·) =iνω.
Note that the K¨ ahler condition∇J = 0 implies ∇τ = J∇ν. Using this together
with the metric compatibility d(g(X,Y )) = g(∇X,Y ) + g(X,∇Y ) and torsion-
freeness∇XY −∇ YX = [X,Y ] of the Levi-Civita connection, we compute for
vector ﬁelds X,Y tangent to ξ:
dα(X,Y ) =X·α(Y )−Y·α(X)−α([X,Y ])
=X·g(τ,Y )−Y·g(τ,X )−g(τ, [X,Y ])
=g(∇Xτ,Y )−g(∇Yτ,X ) +g(τ,∇XY−∇YX− [X,Y ])
=g(∇Xτ,Y )−g(∇Yτ,X )
=g(J∇Xν,Y )−g(J∇Yν,X )
=−g(∇Xν,JY ) +g(∇Yν,JX )
=−IIΣ(X,JY ) +IIΣ(Y,JX ),
where IIΣ(X,Y ) = g(∇Xν,Y ) is the second fundamental form of Σ. Inserting
Y =JX we obtain
Proposition 2.14. Let Σ be a cooriented hypersurface in a K¨ ahler manifold
(X,J,ω ) with second fundamental form IIΣ. Then the normalized Levi form of Σ
is given by
(2.14) LΣ(X) =IIΣ(X) +IIΣ(JX ).
In particular, Σ is J-convex if and only if at every point x∈ Σ the mean normal
curvature along any complex line in TxΣ is positive. □
2.7. Examples of J-convex functions and hypersurfaces
An important class of hypersurfaces are boundaries of tubular neighborhoods of
submanifolds. In this section we examine their J-convexity for the cases of totally
real submanifolds and complex hypersurfaces.
Totally real submanifolds. A submanifoldL of an almost complex manifold
(V,J ) is called totally real if it has no complex tangent lines, i.e.,J(TL )∩TL ={0}
at every point. This condition implies dim RL≤ dimCV . For example, the linear
subspaces Rk := {(x1,...,x k, 0,..., 0) | xi ∈ R} ⊂Cn are totally real for all
k = 0,...,n .

2.7. EXAMPLES OF J-CONVEX ... 25
If we are given a Hermitian metric on (V,J ) we can deﬁne the distance function
distL :V → R,
distL(x) := inf{dist(x,y )|y∈L}.
Proposition 2.15. Let L be a properly embedded totally real submanifold of
an almost complex manifold (V,J ). Then the squared distance function dist2
L with
respect to any Hermitian metric onV isJ-convex in a neighborhood ofL. Moreover,
L has arbitrarily small neighborhoods with smoothJ-convex boundary, and each such
neighborhood admits an exhausting J-convex function.
Proof. Let Q : TpV → R be the Hessian quadratic form of dist 2
L at a point
p∈ L. Its value Q(z) equals the squared distance of z ∈ TpV from the linear
subspace TpL⊂TpV . (This is most easily seen in geodesic normal coordinates on
the normal bundle of L). Choose an orthonormal basis e1,Je 1,...,e n,Je n of TpV
such that e1,...,e k is a basis of TpL. In this basis,
Q
( n∑
i=1
(xiei +yiJei)
)
=
n∑
j=k+1
x2
j +
n∑
i=1
y2
i,
which isJ-convex by (2.3). So dist2
L isJ-convex onL and therefore by continuity in
a neighborhood of L. If L is compact this concludes the proof because {distL≤ε}
is a tubular neighborhood of L with J-convex boundary for each suﬃciently small
ε > 0, and composition of φ with a convex diﬀeomorphism f : [0,ε )→ [0,∞)
gives an exhausting J-convex function. For noncompact L we invoke the following
argument of Grauert in [ 77].
Pick a locally ﬁnite open covering of L by coordinate neighborhoods Uj with
smooth local coordinates z =x +iy∈ Cn such that J =i alongL∩Uj ={v = 0},
where we write u = (x1,...,x k) and v = (xk+1,...,x n,y 1,...,y n}. Pick a closed
covering Wj⊂ Uj. For each point p∈ Wj∩L consider the function fp(u,v ) :=
2|v|2−|u−p|2. This function is i-convex and hence J-convex at the critical point
p. Pick a closed neighborhood W⊂⋃
jUj of L with smooth boundary such that
2|v| < dist(Wj,∂Uj) for all z = (u,v )∈ Uj∩W . This condition ensures that the
boundary of the open cone Kp :={z∈ Uj∩W | fp(z) > 0} in W is given by
{z∈Uj∩W|fp(z) = 0} for all p∈Wj∩L. To see this, suppose by contradiction
that there exists a point z = (u,v )∈Kp∩∂Uj. Then 2|v|2−|u−p|2 =fp(z)≥ 0
and the choice of W yield the contradiction
dist(Wj,∂Uj)2≤|u−p|2 +|v|2≤ 3|v|2 < dist(Wj,∂Uj)2.
Moreover, we can chooseW so small that fp isJ-convex onKp for allp∈Wj∩W .
Let φp :=g◦fp, where g(t) =e−1/t for t> 0 and 0 for t≤ 0. So the function
φp is positive andJ-convex onKp and can be extended by zero outside to a smooth
weaklyJ-convex function on W . As ⋃
p∈LKp =W\L, there exists a discrete set
of points p1,p 2,... such that ∂W ⊂⋃∞
i=1Kpi. Choose constants ci > 0 so large
that the function φ := ∑
iciφpi satisﬁes{φ < 1}⊂ W . Hence for every regular
value ε∈ (0, 1) of φ the set Wε :={φ≤ ε} is a neighborhood of L with smooth
J-convex boundary contained in W .
To ﬁnd an exhaustingJ-convex function onWε, pick an exhausting functionρ :
L→ R and extend it to V . Let dist 2
L be as above and note that for any function g :
V → R+ the product g dist2
L is stillJ-convex alongL. By choosing g appropriately
we can thus ensure thatψ :=ρ+g dist2
L isJ-convex on a neighborhoodU ofL. Let

26 2. J-CONVEX FUNCTIONS AND HYPERSURFACES
φ :Wε→ [0,ε ] be as constructed above with Wε⊂U. Pick a convex diﬀeomorpism
h : [0,ε )→ [0,∞). Since φ is weaklyJ-convex, the functionχ :=h◦φ+ψ :W→ R
(with ψ from above) is J-convex and exhausting. □
Holomorphic line bundles. A complex line bundle π : E → V over a
complex manifold V is called a holomorphic line bundle if the total space E is a
complex manifold and the bundle possesses holomorphic local trivializations. For
a Hermitian metric on E→V consider the hypersurface
Σ :={z∈E
⏐⏐⏐|z| = 1}⊂ E.
Complex multiplication U(1)× Σ → Σ, (eiθ,z ) ↦→ eiθ· z provides Σ with the
structure of a U(1) principal bundle over V . Let α be the 1-form on Σ deﬁned by
α
( d
dθ
⏐⏐⏐
0
eiθ·z
)
= 1, α |ξ = 0,
where ξ is the ﬁeld of complex tangencies on T Σ. The imaginary valued 1-form iα
deﬁnes the unique connection on the U(1) principal bundle Σ → V for which all
horizontal subspaces are J-invariant. Its curvature is the imaginary valued (1,1)-
form Ω on V satisfying π∗Ω = d(iα). On the other hand, α is a deﬁning 1-form
for the hyperplane distribution ξ⊂ T Σ, so ωΣ = dα|ξ deﬁnes the Levi form of Σ.
ThusωΣ and the curvature form Ω are related by the equation
(2.15) iωΣ(X,Y ) = Ω(π∗X,π∗Y )
forX,Y ∈ξ. The complex line bundle E→V is called positive (resp. negative) if it
admits a Hermitian metric such that the corresponding curvature form Ω satisﬁes
i
2π Ω(X,JX )> 0
(
resp. < 0
)
for all 0⁄=X∈TV . Since π is holomorphic, equation (2.15) implies
Proposition 2.16. Let E→ V be a holomorphic line bundle over a complex
manifold. There exists a Hermitian metric on E→ V such that the hypersurface
{z∈E
⏐⏐⏐|z| = 1} is J-convex if and only if E is a negative line bundle. □
If V is compact, then the closed 2-form i
2π Ω represents the ﬁrst Chern class
c1(E), [ i
2π Ω
]
=c1(E)
(see [113, Chapter 12]). Conversely, for every closed (1,1)-form i
2π Ω representing
c1(E), Ω is the curvature of some Hermitian connection iα as above [80, Chapter
1, Section 2]. So a line bundle over V is positive/negative if and only if its ﬁrst
Chern class can be represented by a positive/negative (1,1)-form. If V has complex
dimension 1 we get a very simple criterion.
Corollary 2.17. Let V be a compact Riemann surface and [V ]∈ H2(V, R)
its fundamental class. A holomorphic line bundle E → V admits a Hermitian
metric such that the hypersurface {z ∈ E
⏐⏐⏐|z| = 1} is J-convex if and only if
c1(E)· [V ]< 0.
For example, the corollary applies to the tangent bundle of a Riemann surface
of genus≥ 2.

2.8. SYMPLECTIC PROPERTIES OF J-CONVEX FUNCTIONS 27
Proof. Since H2(V, R) is 1-dimensional, c1(E)· [V ] < 0 if and only if c1(E)
can be represented by a negatively oriented area form. But any negatively oriented
area form on V is a negative (1,1)-form. □
Remark 2.18. IfE→V is just a complex line bundle (i.e., not holomorphic),
then the total space E does not carry a natural almost complex structure. Such
a structure can be obtained by choosing a Hermitian connection on E→ V and
taking the horizontal spaces as complex subspaces with the complex multiplication
induced from V via the projection. If we ﬁx an almost complex structure on the
total space E such that the projection π is J-holomorphic, then Proposition 2.16
remains valid.
Remark 2.19. Proposition 2.16 has the following generalization to a holo-
morphic vector bundle E → V : A Hermitian metric on E determines a unique
Hermitian connection with curvature form Ω ∈ Ω1,1(EndE). If the curvature is
negative in the sense that iΩ(X,JX ) is negative deﬁnite for all 0 ⁄=X∈TV , then
the function φ(z) =|z|2 onE isJ-convex outside the zero section (in particular its
level sets{|z| = const> 0} are J-convex).
2.8. Symplectic properties of J-convex functions
In this section we discuss some basic symplectic properties of J-convex func-
tions. The symplectic approach to Stein manifolds will be developed systematically
starting from Chapter 11. For more background on symplectic geometry see Chap-
ter 6.
A symplectic form on a manifold V is a 2-form which is closed ( dω = 0) and
nondegenerate in the sense that v↦→ ivω deﬁnes an isomorphism TxV → T∗
xV for
eachx∈V . A 1-form λ such that dλ =ω is symplectic is called a Liouville form .
The vector ﬁeldX that isω-dual toλ, i.e., such thatiXω =λ, is called the Liouville
ﬁeld. Note that the equation dλ =ω is equivalent toLXω =ω. If X integrates to a
ﬂowXt :V →V then (Xt)∗ω =etω, i.e., the Liouville ﬂow expands the symplectic
form. Note that
(2.16) iXλ = 0, i Xdλ =λ, L Xλ =λ,
so the ﬂow of X also expands the Liouville form, (Xt)∗λ =etλ.
The relevance of these notions comes from the following elementary observation.
Lemma 2.20. For a J-convex function φ on a complex manifold (V,J ) set
ωφ :=−ddCφ, λ φ :=−dCφ, X φ :=∇φφ.
Then ωφ is a symplectic form with Liouville ﬁeld Xφ and Liouville form λφ.
Proof. By the deﬁnition of J-convexity,ωφ is a symplectic form. Since Xφ =
∇φφ is the gradient ofφ with respect to the metric gφ :=ωφ(·,J·), for anyY ∈TV
we have
dCφ(Y ) =gφ(∇φφ,JY ) =−ωφ(∇φφ,Y ) =−iXφωφ(Y ).
Hence iXφωφ =λφ and LXφωφ =dλφ =ωφ. □
This observation has several easy but important consequences. A zero p of a
vector ﬁeld X is called hyperbolic if all eigenvalues of the linearization DpX have
nonzero real parts. In this case p has an injectively immersed stable manifold
W−
p ={x∈V | lim
t→∞
Xt(x) =p},

28 2. J-CONVEX FUNCTIONS AND HYPERSURFACES
see Section 9.2.
Lemma 2.21. Let (V,ω ) be a symplectic manifold with Liouville ﬁeld X and
Liouville form λ, and let p be a hyperbolic zero of X. Then
λ|W−
p
≡ 0.
Proof. Let x∈ W−
p and v∈ TxW−
p . Let φt : V → V be the ﬂow of X.
All eigenvalues of the linearization of X at p have negative real part on TpW−
p . It
follows that the diﬀerential Txφt : TxV → Tφt(x)V satisﬁes limt→∞Txφt(v) = 0.
Since φt(x)→p as t→∞ , this implies
etλx(v) = (φ∗
tλ)(v) =λφt(x)(Txφt·v)→ 0
as t→∞ and hence λx(v) = 0. □
In particular, the lemma implies ω|W−
p
≡ 0, i.e., the stable manifold W−(p) is
isotropic for the symplectic form ω =dλ. Since an isotropic submanifold can have
at most half the dimension of V (see Section 6.1), it follows that
dimW−
p ≤ 1
2 dimV.
If X =Xφ is the Liouville ﬁeld associated to a J-convex function φ, then dimW−
p
equals the Morse index of φ at p and we recover Corollary 2.4 (at least for non-
degenerate critical points, but the proof easily extends to the degenerate case, see
Section 11.4).
Consider next a hypersurface Σ ⊂ V transverse to the Liouville ﬁeld X of a
Liouville form λ and set α :=λ|Σ. Then α∧dαn−1 is a positive volume form on Σ
(where 2n = dimV and Σ is cooriented by X), so α is a contact form with contact
structureξ = kerα, see Section 6.5. By Lemma 2.21 the stable manifold W−
p of a
hyperbolic zero satisﬁes α|W−
p∩Σ≡ 0, so the intersection W−
p ∩ Σ is isotropic for
the contact structure ξ.
Recall from Section 2.3 that on a regular level set Σ = φ−1(c) of a J-convex
function φ the contact structure ξ = kerα deﬁned by the contact form α = (λφ)|Σ
is just the ﬁeld of complex tangencies.
We conclude this section with a notion that will play an important role in Part
II of this book.
Definition 2.22. We say that a totally real submanifold L in an almost com-
plex manifold ( V,J ) is J-orthogonal to a hypersurface Σ ⊂ V if, for each point
p∈L∩ Σ, J(TpL)⊂TpΣ and TpL⁄⊂TpΣ.
The second condition just means that L is transverse to Σ, so Λ := L∩ Σ is a
submanifold of Σ. The ﬁrst condition implies that Λ is an integral submanifold for
the ﬁeld of complex tangencies ξ on Σ. If Σ is J-convex and dimRL = dimCV =n,
then the second condition TpL⁄⊂ TpΣ follows from the ﬁrst one because integral
submanifolds of the contact structure ξ have dimension at most n− 1 (see Sec-
tion 6.5).
Remark 2.23. (a) If L is J-orthogonal to Σ⊂V and dimRL = dimCV , then
TpΣ =Tp(Λ)⊕J(TpL) forp∈ Λ =L∩Σ, so the bundleT Σ|Λ is uniquely determined
by the manifolds Λ⊂L.

2.9. COMPUTATIONS IN Cn 29
(b) A totally real submanifold L is J-orthogonal to all level sets of a J-convex
function φ (without critical points) if and only if dCφ|L≡ 0, which implies that L
is isotropic for ωφ and intersects each level set φ−1(c) in an isotropic submanifold.
IfL intersects each level set in an isotropic manifold and ∇φφ is tangent to L then
L isJ-orthogonal to all level sets of φ, and the converse holds for dimRL = dimCV
(for the last statement note that ωφ(∇φφ,v ) = dCφ(v) = 0 for all v∈ TL implies
∇φφ∈ TL for L isotropic of half dimension, see Section 6.1). In particular, the
stable manifold W−
p of a nondegenerate critical point of a J-convex function φ is
J-orthogonal to all regular level sets of φ.
Combining the preceding discussion with Morse theory (see Chapter 9), we
see that every exhausting J-convex Morse function on a complex manifold ( V,J )
provides a handlebody decomposition of V whose cells W−
p ∩{φ≥c}, where p are
critical points of φ, are attached J-orthogonally along isotropic spheres to regular
sublevel sets{φ≤ c}. In the proof of the existence theorem in Chapter 8 we will
proceed in the reverse direction: Starting from a Morse function which is J-convex
on{φ≤c}, we will make its attaching spheres in {φ =c} isotropic and the stable
manifoldsJ-orthogonal in order to extend the Stein structure over the next critical
level.
2.9. Computations in Cn
In this section we derive some explicit formulas for the normalized Levi form
of hypersurfaces in Cn, which will be used in Chapters 4 and 10.
Suppose a hypersurface Σ⊂ Cn is given by an implicit equation Ψ(x) = 0 and
cooriented by the gradient vector ﬁeld
∇Ψ = 2
(∂Ψ
∂¯z1
,..., ∂Ψ
∂¯zn
)
⁄= 0
along Σ. Recall from (2.7) and (2.8) that the real and complex Hessian forms
HessΨ, HΨ of Ψ at p∈ Cn are related by
(2.17) HΨ(X) = HessΨ(X) + HessΨ(iX) = 4
n∑
i,j=1
∂Ψ
∂zi∂¯zj
(p)Xi ¯Xj,
where X = (X1,...,X n)∈ Cn.
Lemma 2.24. The second fundamental form and the normalized Levi form of
Σ are given for p∈ Σ and X∈TpΣ resp.X∈ξp by
IIΣ(X) = HessΨ(X)
|∇Ψ(p)| , LΣ(X) = HΨ(X)
|∇Ψ(p)|.
Proof. We ﬁrst prove the formula for the second fundamental form. Consider
a curve γ : (−ε,ε )→ Σ with γ(0) = p and ˙γ(0) = X. The t-derivative of the
identity Ψ
(
γ(t)
)
= 0 yields dΨ
(
γ(t)
)
· ˙γ(t) = 0, and another derivative at t = 0
gives
0 = HessΨ(X) +⟨∇Ψ(p), ¨γ(0)⟩ = Hessp(X)−|∇ Ψ(p)|IIΣ(X).
The formula for the normalized Levi form on X∈ξp immediately follows from this
in view of
LΣ(X) =IIΣ(X) +IIΣ(iX), H Ψ(X) = HessΨ(X) + HessΨ(iX).
□

30 2. J-CONVEX FUNCTIONS AND HYPERSURFACES
The case n = 2. When n = 2 we have dim Cξ = 1 and thus LΣ(X) has
the same value for all unit vectors X∈ξ. The complex line ξ is generated by the
unit vectorT := 2
|∇Ψ|
(
−∂Ψ
∂w, ∂Ψ
∂ζ
)
. Here we denote the coordinates on Cn by (ζ,w )
instead of (z1,z 2). Hence equation (2.17) and Lemma 2.24 yield
(2.18) L0 := LΣ(T ) = 16
|∇Ψ|3
(
Ψζ ¯ζ|Ψw|2− 2Re (Ψζ ¯wΨwΨ¯ζ) + Ψw ¯w|Ψζ|2
)
.
Next let us write ζ = s +it, w = u +iv and suppose that Σ ⊂ C2 is given as a
graph Σ ={v =ψ(s,t,u )}. Then we obtain
Lemma 2.25. The normalized Levi form of the hypersurfaceΣ ={v =ψ(s,t,u )}
⊂ C2, cooriented by the gradient of the function Ψ(ζ,w ) = ψ(s,t,u )−v, is given
by L(X) = L0|X|2, X∈ξ, where
L0 = (ψss +ψtt)(1 +ψ2
u) +ψuu(ψ2
s +ψ2
t ) + 2ψsu(ψt−ψuψs)− 2ψtu(ψs +ψuψt)
(1 +ψ2s +ψ2
t +ψ2u)
3
2
.
In particular, the hypersurface Σ is i-convex if and only if
(ψss +ψtt)(1 +ψ2
u) +ψuu(ψ2
s +ψ2
t ) + 2ψsu(ψt−ψuψs)− 2ψtu(ψs +ψuψt)> 0.
Proof. The expression for L0 follows from (2.18) in view of
2Ψ¯ζ =ψs +iψt, 4Ψζ ¯ζ =ψss +ψtt, 4|Ψζ|2 =ψ2
s +ψ2
t,
2Ψw =ψu +i, 4Ψw ¯w =ψuu, 4|Ψw|2 = 1 +ψ2
u,
4Ψζ ¯w =ψsu−iψtu, 4ΨwΨ¯ζ = (ψuψs−ψt) +i(ψs +ψuψt),
16 Re (Ψζ ¯wΨwΨ¯ζ) =ψsu(ψuψs−ψt) +ψtu(ψs +ψuψt).
□
The case of general n. Now we return to the case of general n. Suppose
that Σ⊂ Cn is given as a graph Σ ={v =ψ(z,u )}, where we denote coordinates on
Cn by (z,w ) withz = (z1,...,z n−1)∈ Cn−1 andw =u+iv∈ C. Then Lemma 2.25
generalizes in a weaker form to
Lemma 2.26. Suppose that for each ﬁxed u the function ψ(·,u ) is i-convex and
denote byHmin
ψ > 0 the minimum of its complex Hessian form on the unit sphere in
Cn−1. Then the normalized Levi form of the hypersurface Σ ={v =ψ(z,u )}⊂ Cn,
cooriented by the gradient of the function Ψ(z,w ) := ψ(z,u )−v, is bounded below
by
min|X|=1LΣ(X)≥
Hmin
ψ (1 +ψ2
u)−|ψuu||dzψ|2− 2|dzψu||dzψ|
√
1 +ψ2u
(1 +ψ2u +|dzψ|2)3/2 .
Proof. Consider a unit vector X = (Z,W ) ∈ ξ(z,w) ⊂ Cn, where Z =
(Z1,...,Z n−1)∈ Cn−1 and W∈ C. Set Ψ z := (Ψz1,..., Ψzn−1)∈ Cn−1. Then X
satisﬁes 1 =|X|2 =|Z|2 +|W|2 and
0 = (X,∇Ψ
2 ) =
n−1∑
j=1
ZjΨzj +W Ψw.
This implies
(2.19) |W|| Ψw|≤| Z|| Ψz|,

2.9. COMPUTATIONS IN Cn 31
which via 1−|Z|2 =|W|2≤|Z|2|Ψz|2/|Ψw|2 yields
(2.20) |Z|2≥ |Ψw|2
|Ψw|2 +|Ψz|2 = 4|Ψw|2
|∇Ψ|2.
We further have the relations
Ψ¯zj =ψ¯zj, Ψzi¯zj =ψzi¯zj, 4|Ψz|2 =|dzψ|2,
2Ψw =ψu +i, 4Ψw ¯w =ψuu, 4|Ψw|2 = 1 +ψ2
u,
4Ψzi ¯w =ψsiu−iψtiu,
n−1∑
i=1
|4Ψzi ¯w|2 =
n−1∑
i=1
(ψ2
siu +ψ2
tiu) =|dzψu|2,
|4 Re
n−1∑
i=1
Ψzi ¯wZi ¯W|≤| dzψu||Z||W|.(2.21)
Combining all these relations we estimate
LΣ(X) = 4
|∇Ψ|


n−1∑
i,j=1
Ψzi¯zjZi ¯Zj + 2 Re
n−1∑
i=1
Ψzi ¯wZi ¯W + Ψw ¯w|W|2


≥ 1
|∇Ψ|
(
Hmin
ψ |Z|2− 2|dzψu||Z||W|−| ψuu||W|2)
≥ |Z|2
|∇Ψ|| Ψw|2
(
Hmin
ψ |Ψw|2− 2|dzψu|| Ψz|| Ψw|−| ψuu|| Ψz|2)
≥ 1
|∇Ψ|3
(
Hmin
ψ (1 +ψ2
u)− 2|dzψu||dzψ|
√
1 +ψ2u−|ψuu||dzψ|2
)
.
Here in the ﬁrst line we have used equation (2.17) and Lemma 2.24, in the second
line (2.17) and (2.21), in the third line (2.19), and in the last line (2.20) and (2.21).
Since|∇Ψ|2 = 1 +ψ2
u +|dzψ|2, this concludes the proof. □



3
Smoothing
In this chapter we develop some techniques for constructingJ-convex functions.
We begin with the well-known fact that the maximum of two J-convex functions
can be uniformly approximated by J-convex functions. For this, we extend the
notion of J-convexity to continuous functions such that it is preserved under the
maximum construction, and show that any continuous J-convex function can be
smoothed (Richberg’s theorem).
In Section 3.3 we derive a condition under which the maximum and smoothing
constructions do not lead to new critical points. In Section 3.4 we show how to
deform a family of (possible intersecting) J-convex hypersurfaces into level sets of
a J-convex function, and in Section 3.5 we modify J-convex functions near totally
real submanifolds.
3.1. J-convexity and plurisubharmonicity
A C2-function φ :U→ R on an open domain U⊂ C is i-convex if and only if
it is subharmonic 1, i.e.,
∆φ = ∂2φ
∂x2 + ∂2φ
∂y2 = 4 ∂φ
∂z∂ ¯z > 0.
A continuous function φ :U→ R is called subharmonic if it satisﬁes
∆φ≥m
for a positive continuous function m : U → R, where the Laplacian and the in-
equality are understood in the distributional sense, i.e.,
(3.1)
∫
U
φ ∆δ dxdy≥
∫
U
mδ dxdy
for any nonnegative smooth function δ : U → R with compact support. The
function
mφ := sup{m| inequality (3.1) holds}
is called the modulus of subharmonicity of the function φ. Note that to ﬁnd mφ(z)
at a pointz∈U we only need to test (3.1) for functionsδ supported nearz. If φ is a
C2-function satisfying (3.1), then choosing a sequence of functions δn converging to
the Dirac measure of a point z∈U and integrating by parts shows ∆φ(z)≥m(z),
so for a C2-function the two deﬁnitions agree and mφ = ∆φ.
1By “subharmonic” we will always mean “strictly subharmonic”. Non-strict subharmonicity
will be referred to as “weak subharmonicity”. The same applies to plurisubharmonicity discussed
below.
33

34 3. SMOOTHING
Ifz =x+iy→w =u+iv is a biholomorphic change of coordinates on U, then
(3.2) ∆ zδ dx∧dy = 2i ∂2δ
∂z∂ ¯zdz∧d¯z =−ddCδ = ∆wδ du∧dv,
so inequality (3.1) transforms into∫
U
φ(w)∆δ(w)dudv≥
∫
U
m(w)δ(w)
⏐⏐⏐dz
dw
⏐⏐⏐
2
dudv.
This shows that subharmonicity is invariant under biholomorphic coordinate chan-
ges and therefore can be deﬁned for continuous functions on Riemann surfaces.
Note, however, that the modulus of subharmonicity is not invariant under biholo-
morphic coordinate changes; it depends on the additional choice of a Riemannian
metric.
The following lemma gives a useful criterion for subharmonicity of continuous
functions.
Lemma 3.1. A continuous function φ : U→ R on a domain U⊂ C satisﬁes
∆φ≥m for a positive continuous function m :U→ R if and only if
(3.3) φ(z) +m(z)r2
4 ≤ 1
2π
∫ 2π
0
φ(z +reiθ)dθ
for all z∈U and suﬃciently small r> 0 (depending on z).
Proof. Fix a point z∈U and consider the function
ψ(w) :=φ(w)− 1
4m(z)|w−z|2.
Forr> 0 suﬃciently small, (3.3) is equivalent to
ψ(z) =φ(z)≤ 1
2π
∫ 2π
0
φ(z +reiθ)dθ− m(z)r2
4 = 1
2π
∫ 2π
0
ψ(z +reiθ)dθ
and thus to
ψ(z)≤ 1
2π
∫ 2π
0
ψ(z +reiθ)dθ.
By a standard result (see e.g. [ 103, Section 1.6]), this inequality is equivalent to
∆ψ(z)≥ 0 in the distributional sense, and therefore to ∆φ(z)≥ 1
4m(z)∆w|w−z|2 =
m(z). □
Now let (V,J ) be an almost complex manifold. A complex curve in V is a 1-
dimensional complex submanifold of (V,J ). Note that the restriction of the almost
complex structure J to a complex curve is always integrable.
Lemma 3.2. AC2-functionφ on an almost complex manifold (V,J ) isJ-convex
if and only if its restriction to every complex curve is subharmonic.
Proof. By deﬁnition, φ is J-convex if and only if −ddCφ(X,JX ) > 0 for all
0⁄= X∈ TxV , x∈ V . Now for every such X⁄= 0 there exists a complex curve
C⊂V passing throughx withTxC = spanR{X,JX} (see [152]). By formula (3.2)
above,−ddCφ(X,JX )> 0 precisely if φ|C is subharmonic in x. □
Remark 3.3. In the proof we have used the fact that the diﬀerential operator
ddC commutes with restrictions to complex submanifolds. This is true because the
exterior derivative and the composition with J both commute with restrictions to
complex submanifolds.

3.1. J-CONVEXITY AND PLURISUBHARMONICITY 35
As a consequence, we obtain the following generalization of Corollary 2.4 to
the almost complex case.
Corollary 3.4. The Morse index (i.e., the maximal dimension of a subspace
on which the real Hessian is negative deﬁnite) of a critical point of a J-convex
function on a 2n-dimensional almost complex manifold is at most n.
Proof. Letp be a critical point of aJ-convex functionφ :V → R and suppose
that its Morse index is >n . Then there exists a subspace W⊂TpV of dimension
> n on which the Hessian of φ is negative deﬁnite. Since W∩JW ⁄={0}, W
contains a complex lineL. Let C be a complex curve throughp tangent toL. Then
φ|C attains a local maximum at p. But this contradicts the maximum principle
because φ|C is subharmonic by Lemma 3.2. □
In view of Lemma 3.2, we can speak about continuous J-convex functions on
almost complex manifolds as functions whose restrictions to all complex curves
are subharmonic. Such functions are also called (strictly) plurisubharmonic . For
functions on Cn, Lemma 3.1 and the proof of Lemma 3.2 show
Lemma 3.5. A continuous function φ : Cn⊃U→ R is i-convex if and only if
its restriction to every complex line is subharmonic. This means that there exists a
positive continuous function m :U→ R such that
(3.4) φ(z) + 1
4m(z)|w|2≤ 1
2π
∫ 2π
0
φ(z +weiθ)dθ
for all z∈U and suﬃciently small w∈ Cn (depending on z).
As in the 1-dimensional case, we call the supremum of all functionsm satisfying
(3.4) the modulus of i-convexity of the function φ : Cn⊃U→ R and denote it by
mφ. Thus φ is i-convex if and only if mφ > 0. If φ is of class C2 then Lemma 3.1
and the discussion following inequality (3.1) shows
mφ(x) = min{−ddCφ(v,iv )|v∈ Cn, |v| = 1}.
More generally, for a continuous function φ on a complex manifold (V,J ) equipped
with a Hermitian metric, we deﬁne the modulus ofJ-convexitymφ via formula (3.4)
in holomorphic coordinates for which the Hermitian metric is standard at the point
z. Note that mφ depends only on J, φ and the Hermitian metric.
Remark 3.6. We will need the modulus of convexity only for integrable J.
In the case of an almost complex manifold ( V,J ) we can deﬁne the modulus of J-
convexity as follows. We ﬁx a Hermitian metric and a locally ﬁnite covering ofV by
coordinate neighborhoods Ui. According to [ 152], there exists for each p∈Ui and
unit vector v∈TpV a holomorphic disc fi,p,v : C⊃D→V with fi,p,v(0) = 0 and
dfi,p.v(1) = v. Moreover, fi,p,v can be chosen to depend continuously on ( p,v ) in
theC2-topology. Now we deﬁne mφ(p) := maxi,vmφ◦fi,p,v(0), where the maximum
is taken over all unit vectors v and all i such that p∈Ui. Remark 3.3 shows that
for a C2-function φ :V → R, the modulus of J-convexity is given by
(3.5) mφ(x) = min{−ddCφ(X,JX )|X∈TxV, |X| = 1}.
We do not know whether the deﬁnition of the modulus of J-convexity on an al-
most complex manifold depends on the chosen holomorphic discs fi,p,v. According
to Corollary 3.16 below, in the integrable case the deﬁnition coincides with the
previous one and hence does not depend on the fi,p,v.

36 3. SMOOTHING
The following lemma follows from equation (3.1) via integration by parts.
Lemma 3.7. Ifφ is a J-convex function on an almost complex manifold (V,J ),
then φ +ψ is J-convex for every suﬃciently C2-small C2-function ψ :V → R.
Our interest in continuous J-convex functions is motivated by the following
Proposition 3.8. If φ and ψ are continuousJ-convex functions on an almost
complex manifold (V,J ), then max (φ,ψ ) is again J-convex.
More generally, let (φλ)λ∈Λ be a continuous family of continuousJ-convex func-
tions, parametrized by a compact space Λ. Then φ := maxλ∈Λφλ is a continuous
function whose modulus of J-convexity satisﬁes
mφ≥ minλ∈Λmφλ.
Proof. Continuity ofφ = maxλ∈Λφλ is an easy exercise. For J-convexity we
use the criterion from Lemma 3.1. Let U⊂V be a complex disc and choose a local
coordinate z on U. By hypothesis, condition (3.3) holds for all φλ with functions
mλ =mφλ. Set m(z) := minλ∈Λmλ. At any point z∈U we haveφ =φλ for some
λ∈ Λ (depending on z). Now the lemma follows from
φ(z) + 1
4m(z)r2≤φλ(z) + 1
4mλ(z)r2≤ 1
2π
∫
φλ(z +reiθ)dθ
≤ 1
2π
∫
φ(z +reiθ)dθ.
□
Remark 3.9. If the familymφλ > 0 is continuous inλ, then minλmφλ > 0 and
thus maxλφ is J-convex. For example, by equation (3.5), this is the case if all the
J-convex functions φλ are C2 and their ﬁrst two derivatives depend continuously
on λ.
3.2. Smoothing of J-convex functions
For integrableJ, continuousJ-convex functions can be approximated by smooth
ones. The following proposition was proved by Richberg [ 161]. We give below a
proof following [59].
Proposition 3.10 (Richberg [161]). Letφ be a continuous J-convex function
on a complex manifold (V,J ). Then for every positive function h :V → R+ there
exists a smooth J-convex function ψ : V → R such that |φ(x)−ψ(x)| < h(x) for
all x∈ V . If φ is already smooth on a neighborhood of a compact subset K, then
we can achieve ψ =φ on K.
Remark 3.11. (i) A continuous weakly J-convex function (i.e., one whose
restriction to each complex curve is weakly subharmonic) cannot in general be
approximated by smooth weaklyJ-convex functions, see [59] for a counterexample.
(ii) We do not know whether Proposition 3.10 remains true for almost complex
manifolds.
The proof is based on an explicit smoothing procedure for functions on Rm.
Pick a smooth nonnegative function ρ : Rm→ R with support in the unit ball and∫
Rmρ = 1. For δ >0 set ρδ(x) :=δ−mρ(x/δ). Let U⊂ Rm be an open subset and
set
Uδ :={x∈U| ¯Bδ(x)⊂U}.

3.2. SMOOTHING OF J-CONVEX FUNCTIONS 37
For a continuous function φ : Rm⊃U→ R deﬁne the molliﬁed function φδ :Uδ→
R,
(3.6) φδ(x) :=
∫
Rm
φ(x−y)ρδ(y)dmy =
∫
Rm
φ(y)ρδ(x−y)dmy.
The last expression shows that the functions φδ are smooth for every δ >0. The
ﬁrst expression shows that if φ is of class Ck for some k≥ 0, then φδ→φ asδ→ 0
in Ck uniformly on compact subsets of U.
Proposition 3.10 is an immediate consequence of the following lemma, via in-
duction over a countable coordinate covering.
Lemma 3.12. Letφ be a continuous J-convex function on a complex manifold
(V,J ). Let A,B ⊂V be compact subsets such that φ is smooth on a neighborhood
of A and B is contained in a holomorphic coordinate neighborhood. Then for every
ε > 0 and every neighborhood W of A∪B there exists a continuous J-convex
function ψ :V → R with the following properties.
• ψ is smooth on a neighborhood of A∪B;
• |ψ(x)−φ(x)|<ε for all x∈V ;
• ψ =φ on A and outside W .
Proof. The proof follows [ 59]. First suppose that φ is i-convex on an open
setU⊂ Cn. By Lemma 3.5, there exists a positive continuous function m :U→ R
such that (3.4) holds for all z∈U2δ and w∈ Cn with|w|≤ δ. Hence the molliﬁed
function φδ satisﬁes
φδ(x) + 1
4mδ(x)|w|2 =
∫
Cn
(
φ(x−y) + 1
4h(x−y)|w|2
)
ρδ(y)d2ny
≤
∫
Cn
∫ 2π
0
φ(x−y +weiθ)dθρδ(y)d2ny
=
∫ 2π
0
φδ(x +weiθ)dθ,
so φδ is i-convex on U2δ.
Now let φ : V → R be as in the proposition. Pick a holomorphic coordinate
neighborhood U and compact neighborhoods A′⊂W of A and B′⊂B′′⊂W∩U
of B with A⊂ intA′⊂ A′⊂ W , such that φ is smooth on A′. By the preceding
discussion, there exists a smooth J-convex function φδ : B′′→ R with|φδ(x)−
φ(x)| < ε/2 for all x∈ B′′. Pick smooth cutoﬀ functions g,h : V → [0, 1] such
that g = 1 on A, g = 0 outside A′, h = 1 on B′, and h = 0 outside B′′. Deﬁne a
continuous function ~φ :V → R,
~φ :=φ + (1−g)h(φδ−φ).
The function ~φ is smooth on A′∪B′,|~φ(x)−φ(x)|<ε/ 2 for all x∈V , ~φ =φδ on
B′\A′, and ~φ = φ on A and outside B′′. Since φ is C2 on A′∩B′′, the function
(1−g)h(φδ−φ) becomes arbitrarily C2-small on this set for δ small. Hence by
Lemma 3.7, ~φ is J-convex on A′∩B′′ for δ suﬃciently small. So we can make ~φ
J-convex on A′∪B′. However, ~φ need not be J-convex on B′′\ (A′∪B′).
Pick a compact neighborhood W′⊂W of A′∪B′′. Without loss of generality
we may assume that ε was arbitrarily small. Then by Lemma 3.7 there exists
a continuous J-convex function ~ψ : V → R (which diﬀers from φ by a C2-small

38 3. SMOOTHING
function) satisfying ~ψ =φ−ε on A∪B, ~ψ =φ +ε on W′\ (A′∪B′), and ~ψ =φ
outside W . Now the function ψ := max (~φ,~ψ) has the desired properties. □
Remark 3.13. The proof of Lemma 3.12 shows the following additional prop-
erties in Proposition 3.10:
(1) Ifφλ is a continuous family ofJ-convex functions parametrized by a compact
space Λ, then the family φλ can be uniformly approximated by a continuous family
of smooth J-convex functions ψλ.
(2) If φ0≤ φ1 then the smoothed functions also satisfy ψ0≤ ψ1. This holds
because the proof only uses molliﬁcation φ↦→ φδ, interpolation and taking the
maximum of two functions, all of which are monotone operations.
Remark 3.14. For a Stein manifold (V,J ), Proposition 3.10 can alternatively
be proved as follows. Embed V as a proper submanifold in some CN. By Corol-
lary 5.27 below, there exists a neighborhood U of V in CN with a holomorphic
submersion π : U → V ﬁxed on V . After shrinking U, we may assume that the
squared Euclidean distance function dist 2
V from V is smooth on U. Given a con-
tinuous J-convex function φ :V → R, the function Φ := φ◦π + dist2
V :U→ R is
i-convex and agrees with φ on V .
For a compact subset W ⊂ V , pick δ > 0 such that the δ-ball around each
point of W is contained in U and deﬁne the smooth i-convex function Φ δ on a
neighborhood ofW by convolution in CN. The restriction φδ of Φδ toW is smooth,
J-convex and close to φ in C0(W ). If φ was already smooth near some compact
subset K ⊂ IntW , then φδ is close to φ in C2(K) and we can interpolate by a
cutoﬀ function to achieve φδ =φ on K.
To approximateφ on the whole manifoldV , pick an exhaustionW0⊂W1⊂···
of V by compact subsets with Wk ⊂ IntWk+1 and ⋃
k∈NWk = V . Using the
previous paragraph, we inductively ﬁnd smoothings φk ofφ onWk withφk =φk−1
on Wk−2. Thus the construction stabilizes and yields a smoothing of φ on V .
Proposition 3.8, Remark 3.9 and Proposition 3.10 imply
Corollary 3.15. The maximum of two smooth J-convex functions φ, ψ on a
complex manifold (V,J ) can be C0-approximated by smooth J-convex functions. If
max (φ,ψ ) is smooth on a neighborhood of a compact subset K, then we can choose
the smoothings to be equal to max (φ,ψ ) on K.
More generally, let (φλ)λ∈Λ be a continuous family of J-convex C2-functions
whose ﬁrst two derivatives depend continuously on a parameter λ varying in a
compact metric space Λ. Then maxλ∈Λφλ can be C0-approximated by smooth J-
convex functions. If maxλ∈Λφλ is smooth on a neighborhood of a compact subset
K, then we can choose the smoothings to be equal to maxλ∈Λφλ on K. □
We will denote the smoothing of a continuous function φ :V → R by
smooth(φ).
In particular, the smoothing of the maximum of φ and ψ will be written as
smooth max(φ,ψ ).
This is a slight abuse of notation because the smoothing of a function depends on
various choices. However, the notation is justiﬁed by the fact (Remark 3.13) that
the smoothing can be done continuously in families.

3.3. CRITICAL POINTS OF J-CONVEX FUNCTIONS 39
Using Proposition 3.10, we can now justify the earlier Remark 3.6 that our
deﬁnitions of the modulus of J-convexity coincide in the integrable case:
Corollary 3.16. Consider two holomorpic discs f,g : C⊃D→V in a com-
plex manifold (V,J ) with f(0) =g(0) and df(0) =dg(0). Then for any continuous
J-convex functionφ :V → R the compositionsφ◦f andφ◦g have the same modulus
of i-convexity at the origin.
Proof. Note ﬁrst that by Remark 3.3 the statement holds if φ is C2. In the
continuous case, let m = m(0) > 0 be a constant such that (3.3) holds for φ◦f
at z = 0 for all r∈ [0, 1]. For given ε >0 we pick a J-convex smoothing ψ of φ
such that|φ−ψ|<ε/ 4 on the images of f and g. Then (3.3) holds for ψ◦f, and
hence also for ψ◦g, with the same constant m and up to an error ε/2. Thus (3.3)
holds for φ◦g with the constant m up to an error ε. Letting ε→ 0 this shows that
mφ◦g(0)≥mφ◦f(0) and the converse inequality follows similarly. □
3.3. Critical points of J-convex functions
We wish to control the creation of new critical points under the construction
of taking the maximum of two J-convex functions and then smoothing. This is
based on the following trivial observation: A smooth function φ : M → R on a
manifold has no critical points if and only if there exist a vector ﬁeld X and a
positive function h with X·φ≥ h. Multiplying by a nonnegative volume form Ω
on M with compact support, we obtain∫
M
(X·φ)Ω≥
∫
M
hΩ.
Using (X·φ)Ω +φLXΩ =LX(φΩ) =d(φiXΩ) and Stokes’ theorem (assuming M
is orientable over supp Ω), we can rewrite the left hand side as
∫
M
(X·φ)Ω =−
∫
M
φLXΩ.
So we have shown: A smooth function φ : M→ R on a manifold has no critical
points if and only if there exist a vector ﬁeld X and a positive function h such that
−
∫
M
φLXΩ≥
∫
M
hΩ
for all nonnegative volume forms Ω on M with suﬃciently small compact support.
This criterion obviously still makes sense if φ is merely continuous. However, for
technical reasons we will slightly modify it as follows.
We say that a continuous function φ : M → R satisﬁes X·φ≥ h (in the
distributional sense) if around each p∈M there exists a coordinate chart U⊂ Rm
on which X corresponds to a constant vector ﬁeld such that
−
∫
U
φLXΩ≥h(p)
∫
U
Ω
for all nonnegative volume forms Ω with support in U. Writing Ω = g(x)dmx for a
nonnegative function g, this is equivalent to
(3.7) −
∫
U
φ(x)(X·g)(x)dmx≥h(p)
∫
U
g(x)dmx.
This condition ensures that smoothing does not create new critical points:

40 3. SMOOTHING
Lemma 3.17. If a continuous function φ : Rm⊃ U→ R satisﬁes (3.7) for a
constant vector ﬁeld X and a constant h = h(p) > 0, then each molliﬁed function
φδ deﬁned by equation (3.6) also satisﬁes (3.7) with the same X,h .
Proof. Let g be a nonnegative test function with support in U and 0 <
δ < dist(suppg,∂U ). Let y∈ Rm with|y| < δ. Applying (3.7) to the function
x↦→ g(x +y) and using translation invariance of X, h and the Lebesgue measure
dx :=dmx, we ﬁnd
−
∫
U
φ(x−y)X·g(x)dx =−
∫
U
φ(x)X·g(x +y)dx
≥h
∫
U
g(x +y)dx =h
∫
U
g(x)dx.
Multiplying by the nonnegative function ρδ and integrating yields
−
∫
U
φδ(x)X·g(x)dx =−
∫
U
∫
Bδ
φ(x−y)ρδ(y)X·g(x)dydx
≥h
∫
U
∫
Bδ
g(x)ρδ(y)dydx =h
∫
U
g(x)dx.
□
The next proposition shows that the condition X·φ≥ h is preserved under
taking the maximum of functions.
Proposition 3.18. Suppose the continuous functions φ,ψ : M → R satisfy
X·φ≥h, X·ψ≥h with the same X,h . Then X· max (φ,ψ )≥h.
More generally, suppose (φλ)λ∈Λ is a continuous family of functions φλ :M→
R, parametrized by a compact metric space Λ, such that all φλ satisfy X·φλ≥ h
with the same X,h . Then X· maxλ∈Λφλ≥h.
Proof. Let U⊂ Rm be a coordinate chart and X,h := h(p) be as in (3.7).
After a rotation and rescaling, we may assume that X = ∂
∂x1
. Suppose ﬁrst that
φ,ψ are smooth and 0 is a regular value of φ−ψ. Then ϑ := max (φ,ψ ) is a
continuous function which is smooth outside the smooth hypersurface Σ := {x∈
U | φ(x) = ψ(x)}. Deﬁne the function ∂ϑ
∂x1
as ∂φ(x)
∂x1
if φ(x)≥ ψ(x) and ∂ψ(x)
∂x1
otherwise. We claim that ∂ϑ
∂x1
is the weak x1-derivative of ϑ. Indeed, for any test
function g supported in U we have (orienting Σ as the boundary of {φ≥ψ})∫
U
∂ϑ
∂x1
gdmx =
∫
{φ≥ψ}
∂φ
∂x1
gdmx +
∫
{φ<ψ}
∂ψ
∂x1
gdmx
=
∫
Σ
φgdx 2··· dxm−
∫
{φ≥ψ}
φ ∂g
∂x1
dmx
−
∫
Σ
ψgdx 2··· dxm−
∫
{φ<ψ}
ψ ∂g
∂x1
dmx
=−
∫
U
ϑ ∂g
∂x1
dmx,
since φ = ψ on Σ. This proves the claim. By hypothesis we have ∂ϑ
∂x ≥ h, so the
conclusion of the lemma follows via
−
∫
U
ϑ ∂g
∂x1
dmx =
∫
U
∂ϑ
∂x1
gdmx≥h
∫
U
gdmx.

3.3. CRITICAL POINTS OF J-CONVEX FUNCTIONS 41
Next let φ,ψ : U→ R be continuous functions satisfying (3.7). By Lemma 3.17,
there exist sequences φk,ψk of smooth functions, converging locally uniformly to
φ,ψ , such that X·φk≥ h and X·ψk≥ h for all k. Perturb the φk to smooth
functions ~φk such that 0 is a regular value of ~φk−ψk, ~φk→ φ locally uniformly,
andX·~φk≥h−1/k for allk. By the smooth case above, the function max (~φk,ψk)
satisﬁes
−
∫
U
max (~φk,ψk)X·gdmx≥ (h− 1/k)
∫
U
gdmx
for any nonnegative test functiong supported inU. Since max (~φk,ψk)→ max (φ,ψ )
locally uniformly, the limit k→∞ yields the conclusion of the lemma for the case
of two functions φ,ψ .
Finally, let (φλ)λ∈Λ be a continuous family as in the lemma. Pick a dense
sequence λ1,λ 2,... in Λ. Set ψk := max{φλ1,...,φ λk} and ψ := maxλ∈Λφλ. By
the lemma for two functions and induction, the functions ψk satisfy (3.7) with the
same X,h for all k. Thus the lemma follows in the limit k→∞ if we can show
locally uniform convergence ψk→ψ.
We ﬁrst prove pointwise convergence ψk→ ψ. So let x∈ U. Then ψ(x) =
φλ(x) for some λ∈ Λ. Pick a sequence k𝓁 such that λk𝓁 → λ as 𝓁→∞ . Then
φλk𝓁
(x)→ φλ(x) = ψ(x) as 𝓁→∞ . Since φλk𝓁
(x)≤ ψk𝓁(x)≤ ψ(x), this implies
ψk𝓁(x) → ψ(x) as 𝓁 → ∞. Now the convergence ψk(x) → ψ(x) follows from
monotonicity of the sequence ψk(x).
So we have an increasing sequence of continuous functions ψk that converges
pointwise to a continuous limit function ψ. By a simple argument this implies
locally uniform convergence ψk→ψ: Let ε> 0 and x∈U be given. By pointwise
convergence there exists k such that ψk(x)≥ψ(x)−ε. By continuity of φk andψ,
there exists δ > 0 such that |ψk(y)−ψk(x)| < εand|ψ(y)−ψ(x)| < εfor all y
with|y−x|<δ . This implies ψk(y)≥ψ(y)− 3ε for all y with|y−x|<δ . In view
of monotonicity, this establishes locally uniform convergence ψk→ ψ and hence
concludes the proof of the proposition. □
Finally, we show that J-convex functions can be smoothed without creating
critical points.
Proposition 3.19. Let φ : V → R be a continuous J-convex function on a
complex manifold satisfying X·φ≥h for a vector ﬁeld X and a positive function
h : V → R. Then the J-convex smoothing ψ : V → R in Proposition 3.10 can be
constructed so that it satisﬁes X·ψ≥~h for any given function ~h<h .
Proof. The function ψ is constructed from φ in Lemma 3.12 by repeated
application of the following 3 constructions:
(1) Molliﬁcation φ↦→φδ. This operation preserves the condition X·φ≥h by
Lemma 3.17.
(2) Taking the maximum of two functions. This operation preserves the con-
dition X·φ≥h by Proposition 3.18.
(3) Adding a C2-small function f to φ. Let k : V → R be a small positive
function such that supU(X·f)(x)≥− k(p) for each coordinate chart U around p
as in condition (3.7) (for this it suﬃces that f is suﬃciently C1-small). Then we
ﬁnd
−
∫
U
f(x)(X·g)(x)dx =
∫
U
(X·f)(x)g(x)dx≥−k(p)
∫
U
g(x)dx,

42 3. SMOOTHING
so the function φ +f satisﬁes X· (φ +f)≥ h−k. In the proof of Lemma 3.12,
this operation is applied ﬁnitely many times on each compact subset of V , so by
choosing the function k suﬃciently small we can achieve that X·ψ≥~h. □
Propositions 3.18 and 3.19 together imply
Corollary 3.20. If two smoothJ-convex functionsφ,ψ on a complex manifold
V satisfy X·φ >0 and X·ψ > 0 for a vector ﬁeld X, then the smoothing ϑ of
max (φ,ψ ) can also be arranged to satisfy X·ϑ> 0. □
Remark 3.21. (a) Clearly, Proposition 3.19 and Corollary 3.20 also hold with-
out theJ-convexity condition, for functions and vector ﬁelds on a smooth manifold.
(b) Inspection of the proofs shows that Propositions 3.18 and 3.19 remain valid
if all inequalities are replaced by the reverse inequalities.
Corollary 3.22. If two smoothJ-convex functionsφ,ψ on a complex manifold
V areC1-close, then the smoothing of max (φ,ψ ) is C1-close to φ.
Proof. Let X be a vector ﬁeld and h± : V → R functions such that h−≤
X·φ,X ·ψ≤ h+. By the preceding remark, the smoothing ϑ of max (φ,ψ ) can
be constructed such that ~h−≤ X·ϑ≤~h+ for any given functions ~h− < h− and
~h+ >h +. Since X,h−,h + were arbitrary, this proves C1-closeness of ϑ to φ. □
Finally, we apply the preceding result to smoothing of J-convex hypersurfaces.
Corollary 3.23. Let (M× R,J ) be a compact complex manifold and φ,ψ :
M → R two functions whose graphs are J-convex cooriented by ∂r, where r is
the coordinate on R. Then there exists a smooth function ϑ : M → R with J-
convex graph which is C0-close to min (φ,ψ ) and coincides with min (φ,ψ ) outside
a neighborhood of the set {φ =ψ}.
Proof. For a convex increasing function f : R→ R with f(0) = 0 consider
the functions
Φ(x,r ) :=f
(
r−φ(x)
)
, Ψ(x,r ) :=f
(
r−ψ(x)
)
.
Forf suﬃciently convex, Φ and Ψ are J-convex and satisfy ∂rΦ> 0,∂rΨ> 0 near
their zero level sets. Thus by Propositions 3.18 and 3.19 the function max (Φ, Ψ) can
be smoothed, keeping it ﬁxed outside a neighborhoodU of the set{max (Φ, Ψ) = 0},
to a function Θ which is J-convex and satisﬁes∂rΘ> 0 near its zero level set. The
last condition implies that the smooth J-convex hypersurface Θ−1(0) is the graph
of a smooth functionϑ :M→ R. Now note that the zero level set{max (Φ, Ψ) = 0}
is the graph of the function min (φ,ψ ). This implies that ϑ isC0-close to min (φ,ψ )
and coincides with min (φ,ψ ) outside U. □
Remark 3.24. Note that convex functions on Cn are also J-convex. On the
other hand for any two convex functionsφ,ψ the function smooth max(φ,ψ ) is also
convex, and therefore has a unique critical point, the minimum.
3.4. From families of hypersurfaces to J-convex functions
The following result shows that a continuous family of J-convex hypersurfaces
transverse to the same vector ﬁeld gives rise to a smooth function with regular
J-convex level sets. This will be extremely useful for the construction of J-convex
functions with prescribed critical points.

3.4. FROM HYPERSURFACES TO FUNCTIONS 43
Proposition 3.25. Let (M×[0, 1],J ) be a compact complex manifold such that
M×{ 0} and M×{ 1} areJ-convex cooriented by ∂r, where r is the coordinate on
[0, 1]. Suppose there exists a smooth family (Σλ)λ∈[0,1] of J-convex hypersurfaces
transverse to∂r with Σ0 =M×{0} and Σ1 =M×{1}. Then there exists a smooth
foliation (~Σλ)λ∈[0,1] of M× [0, 1] by J-convex hypersurfaces transverse to ∂r with
~Σλ =M×{λ} for λ near 0 or 1.
Proof. The proof has two steps. In the ﬁrst step we use the maximum con-
struction to make the family of hypersurfaces weakly monotone in the parameterλ,
and in the second step we perturb it to make it strictly monotone and thus obtain
a foliation.
Step 1. Let ε >0 be so small that the hypersurfaces M×{λ} are J-convex
for λ≤ ε and λ≥ 1−ε. We ﬁrst modify the family such that Σ λ = M×{λ}
for λ≤ ε and λ≥ 1−ε. After a C2-small perturbation and decreasing ε, we
may further assume that Σλ⊂M× (ε, 1−ε) for all λ∈ (ε, 1−ε). Pick a smooth
family of surjectiveJ-convex functionsφλ :Op Σλ→ [−1, 1] 2 with regular level sets
φ−1
λ (0) = Σλ, and extendφλ by the values±1 to a continuous functionM×[0, 1]→
[−1, 1] (which is not J-convex outside Op Σλ). After composing each φλ with a
suitable convex function R→ R, shrinking the neighborhoodsOp Σλ and extending
as before by ±1, we may assume that φλ≥ φµ for all λ≤ µ with either λ≤ ε or
µ≥ 1−ε.
By Proposition 3.8, the continuous functions
ψλ := maxν≥λφν
are J-convex on Uλ :=ψ−1
λ ([− 1
2, 1
2]). By construction, they satisfy
(3.8) ψλ≥ψµ for λ≤µ,
andψλ =φλ forλ≤ε andλ≥ 1−ε. By Proposition 3.18, the ψλ satisfy∂r·ψλ≥h
(in the distributional sense) on Uλ for a positive function h :M× [0, 1]→ R.
Next use Proposition 3.10 to approximate the ψλ by smooth functions ˆψλ that
are J-convex on ˆUλ := ˆψ−1
λ ([− 1
4, 1
4]). By Remark 3.13, the resulting family ˆψλ is
continuous inλ and still satisﬁes (3.8). By Proposition 3.19, the smoothed functions
satisfy ∂r· ˆψλ≥h/2> 0 on ˆUλ, hence the level sets ˆΣλ := ˆψ−1
λ (0) are regular and
transverse to ∂r. We can modify the smoothing construction to achieve ˆψλ = φλ
near λ = 0 and 1, still satisfying J-convexity, transversality of the zero level to ∂r,
and (3.8). Note that as a result of the smoothing construction the functions ˆψλ,
and hence their level setsˆΣλ, depend continuously on the parameterλ with respect
to the C2-topology.
Step 2. Since ˆΣλ is transverse to ∂r, we can write it as the graph {r =fλ(x)}
of a smooth function fλ : M→ [0, 1]. By construction, the functions fλ depend
continuously onλ with respect to theC2-topology,fλ≤fµ forλ≤µ, andfλ(x) =λ
for λ≤ ε and λ≥ 1−ε, with some ε >0 (possibly smaller than the one above).
Note that fµ(x)−fλ(x)≥µ−λ for λ≤µ≤ε and 1−ε≤λ≤µ. Pick a function
g : [0, 1]→ [0, 1] satisfying g(λ) = 0 for λ≤ε/2 and λ≥ 1−ε/2, g′(λ)≥− 1 +γ
for ε/2≤ λ≤ ε and 1−ε≤ λ≤ 1−ε/2, and g′(λ)≥ γ for ε≤ λ≤ 1−ε, with
some γ > 0, see Figure 3.1. For g suﬃciently small, the graphs of the functions
2Recall that for a closed subset A⊂ X of a topological space, Op A denotes a suﬃciently
small but not speciﬁed open neighborhood of A.

44 3. SMOOTHING
g(λ)
ǫ
ǫ
2
λ
11 − ǫ
1 − ǫ
2
Figure 3.1. The function g.
ˆfλ(x) := fλ(x) +g(λ) are still J-convex, ˆfλ(x) = λ for λ≤ ε/2 and λ≥ 1−ε/2,
and
ˆfµ(x)− ˆfλ(x)≥γ(µ−λ)
for all λ≤µ. Now mollify the functions ˆfλ(x) in the parameter λ to
~fλ(x) :=
∫
R
ˆfλ−µ(x)ρδ(µ)dµ,
with a cutoﬀ function ρ : R→ R as in equation (3.6). Since the functions fλ−µ are
C2-close to fλ forµ∈ suppρδ andδ small, the graph of ~fλ isC2-close to the graph
of fλ and hence J-convex. Moreover, for λ′≥λ the ~fλ still satisfy
~fλ′(x) =
∫
R
ˆfλ′−µ(x)ρδ(µ)dµ≥
∫
R
ˆfλ−µ(x)ρδ(µ)dµ +γ(λ′−λ) = ~fλ(x) +γ(λ′−λ).
Modify the ~fλ such that ~fλ(x) = λ for λ≤ ε/2 and λ≥ 1−ε/2, and so that
their graphs are still J-convex and ~fµ(x)− ~fλ(x)≥ γ(µ−λ) for all λ≤ µ. The
last inequality implies that the map ( x,λ )↦→
(
x,fλ(x)
)
is an embedding, thus the
graphs of ~fλ form the desired foliation ~Σλ. □
3.5. J-convex functions near totally real submanifolds
In this section we discuss modiﬁcations of J-convex functions near totally real
submanifolds. The following is the main result.
Proposition 3.26. LetL be a totally real submanifold of a complex manifold
(V,J ) andK⊂L a compact subset. Suppose that two smooth J-convex functionsφ,
ψ coincide along L together with their diﬀerentials, i.e., φ(x) =ψ(x) and dφ(x) =
dψ(x) for all x∈ L. Then, given any neighborhood U of K in V , there exists a
J-convex function ϑ with the following properties.
(a) ϑ coincides with φ outside U and with ψ in a smaller neighborhood U′⊂U
of K.
(b) ϑ and φ coincide along L together with their diﬀerentials.
(c) ϑ can be chosen arbitrarily C1-close to φ, with modulus of J-convexity
uniformly bounded from below.
(d) Assume in addition that φ,ψ are Morse and at each critical point p on K
the stable and unstable spaces for ∇φφ and∇ψψ satisfy E−
p (φ) = E−
p (ψ)⊂ TpL
and E+
p (φ) = E+
p (ψ), and TpL is isotropic with respect to the symplectic form
ωφ =−ddCφ. Then there exists a vector ﬁeld X on V which is gradient-like for
bothφ and ψ.

3.5. J-CONVEX FUNCTIONS NEAR TOTALLY REAL SUBMANIFOLDS 45
(e) Assume in addition that on some neighborhoodN ofK inL we have∇ψψ =
λ∇φφ for a positive function λ :N→ R+. Then ∇ϑϑ =µ∇φφ on L for a positive
function µ :L→ R+
(f) Assume in addition that r∂rφ≥µr2 andr∂rψ≥µr2, wherer is the distance
fromL with respect to some Hermitian metric and µ> 0 a constant. Then we can
arrange that r∂rϑ≥µr2/2.
Remark 3.27. (i) In the notation of Proposition 3.26,φ andϑ can be connected
by the family ofJ-convex functionsφt := (1−t)φ+tϑ,t∈ [0, 1], satisfying properties
(b-f).
(ii) If L is Lagrangian and ∇φφ and∇ψψ are tangent to L, then so is ∇ϑϑ.
This follows from the observation that tangency of ∇φφ to L for L Lagrangian is
equivalent to vanishing ofdφ◦J onL, which is preserved under convex combinations.
The proof of Proposition 3.26 is based on 3 lemmas.
Lemma 3.28. Let φ,ψ : V → R be smooth J-convex functions on an almost
complex manifold (V,J ) and set ϑ := (1−β)φ +βψ for a smooth function β :V →
[0, 1].
(a) Suppose that
|φ(x)−ψ(x)||ddC
xβ| + 2|dxβ||dx(φ−ψ)|< min
(
mφ(x),mψ(x)
)
for all x∈V (with respect to some Hermitian metric). Then ϑ is J-convex.
(b) Suppose that at some point x∈ V we have φ(x) = ψ(x), dφ(x) = dψ(x),
and∇φφ(x) = λ∇ψψ(x) for some λ > 0. Then ∇ϑϑ(x) = µ∇φφ(x) for some
µ> 0.
Proof. (a) Adding up
ddC(βψ) =βdd Cψ +dβ∧dCψ +dψ∧dCβ +ψdd Cβ
and the corresponding equation for (1 −β)φ at any point x∈V , we ﬁnd
−ddCϑ =−(1−β)ddCφ−βddCψ +dβ∧dC(φ−ψ)
+d(φ−ψ)∧dCβ + (φ−ψ)ddCβ
≥ min (mφ,mψ)− 2|dβ||d(φ−ψ)|−| φ−ψ||ddCβ|
> 0.
(b) At the point x the terms φ−ψ and dφ−dψ vanish, so the computation in (a)
shows−ddCϑ =−(1−β)ddCφ−βddCψ. Hence at the pointx we havedϑ =dφ =dψ
and the associated metrics satisfy
gϑ = (1−β)gφ +βgψ.
Now at x we make the ansatz∇ϑϑ =µ∇φφ =µλ∇ψψ and compute
gϑ(∇ϑϑ,·) = (1−β)µgφ(∇φφ,·) +βµλgψ(∇ψψ,·)
= (1−β)µdφ +βµλdψ =µ(1−β +βλ)dϑ,
which yields the correct equation if µ = (1−β +βλ)−1. □
Lemma 3.29. For any constants a > 0 and 0 < δ < εthere exists a smooth
function f : [0,ε ]→ R≥0 with the following properties (see Figure 3.2):
(i) f(x) =ax near 0 and f(x) = 0 nearε;
(ii) −δ≤f′(x)≤a and xf′′(x)≥−δ for all x∈ [0,ε ].

46 3. SMOOTHING
f (x)
ax
b b ε
ε
−δ
a
h(x)
c
x x
k(x)
g(x) =f ′(x)
Figure 3.2. Construction of the function f.
Proof. We need to ﬁnd a function g (=f′) satisfying
(i) g(x) =a near 0 and g(x) = 0 near ε;
(ii) −δ≤g(x)≤a and xg′(x)≥−δ for all x∈ [0,ε ];
(iii)
∫ε
0 g(x)dx = 0 and
∫y
0 g(x)dx≥ 0 for all y∈ [0,ε ].
For a constant c∈ (0,ε ) (which will be determined later) consider the function
h(x) :=−δ ln(x/c)−δ. It satisﬁes xh′(x) =−δ and h(c) =−δ. Let b∈ (0,c ) be
determined byh(b) =a. Let k : [0,ε ]→ R be the continuous function which agrees
with h on [b,c ], equals a on [0,b ] and−δ on [c,ε ]. See Figure 3.2. We estimate its
integral by
∫ ε
0
k(x)dx =
∫ c
0
k(x)dx +
∫ ε
c
k(x)dx≤ac−δ(ε−c)< 0
forc suﬃciently small. Now the function g is obtained by smoothing k, connecting
it to 0 near ε, and increasing its integral to make it zero. □
Next we prove Proposition 3.26 in the special case that ψ =φ +a dist2
L, where
a > 0 and dist L is the distance from L with respect to some Hermitian metric.
Note that according to Proposition 2.15, this function is J-convex near L.
Lemma 3.30. LetL be a totally real submanifold of a complex manifold (V,J )
and K ⊂ L a compact subset. Let φ be a smooth J-convex function and U a
neighborhood ofK in V . Then there exists a Hermitian metric on V such that for
any constant a> 0 there exist a J-convex function ¯φ with the following properties.
(a) ¯φ coincides withφ outsideU and with φ+a dist2
L in a smaller neighborhood
U′⊂U of K.
(b) ¯φ and φ coincide along L together with their diﬀerentials.

3.5. J-CONVEX FUNCTIONS NEAR TOTALLY REAL SUBMANIFOLDS 47
(c) ¯φ can be chosen arbitrarily C1-close to φ, with modulus of J-convexity
uniformly bounded from below.
(d) Assume in addition that φ is Morse and at each critical point p on K the
stable space E−
p for∇φ satisﬁes E−
p ⊂ TpL, and TpL is isotropic with respect to
the symplectic form ωφ =−ddCφ. Then there exists a vector ﬁeld X on V which is
gradient-like for both φ and ¯φ.
(e) Assume in addition that r∂rφ≥ µr2, where r is the distance from L with
respect to the Hermitian metric and µ >0 a constant. Then we can arrange that
r∂r ¯φ≥µr2/2.
Proof. Fix a compact neighborhood W ofK inV on which dist2
L isJ-convex.
Set
~φ :=φ +f(ρ), ρ := dist2
L,
where f : [0,ε ]→ R is the function from Lemma 3.29, with constants 0 <δ <ε to
be determined later. Then ~φ coincides with φ on{ρ≥ε} and with φ +aρ near L.
Let us show that ~φ is J-convex on W . Indeed,
ddC~φ =ddCφ +f′′(ρ)dρ∧dCρ +f′(ρ)ddCρ.
By Proposition 2.15, there exist constants mL,ML such that
mL|v|2≤−ddCρ(v,Jv )≤ML|v|2
for v∈TxW , x∈W . Moreover, on W we have|dρ|≤ CL
√ρ, where the constant
CL depends only on the geometry of L∩W . Thus for v∈TxW ,x∈W ,|v| = 1 we
have
−ddC~φ(v,Jv ) =−ddCφ(v,Jv ) +f′′(ρ)
(
dρ(v)2 +dρ(Jv)2
)
−f′(ρ)ddCρ(v,Jv )
≥mφ− max{0,−f′′(ρ)}CLρ− max{0,−f′(ρ)}ML
≥mφ−CLδ−MLδ≥µ/2
for δ suﬃciently small, where µ := minWmφ.
Note that~φ is arbitrarilyC1-close toφ forε small. Fix a cutoﬀ function β with
support in W and equal to 1 on a neighborhood W′⊂W of K. The function
¯φ := (1−β)φ +β~φ
satisﬁes ¯φ = φ outside W and ¯φ = φ +aρ near K. Moreover, since the estimates
mφ ≥ µ and m ~φ ≥ µ/2 are independent of ε and δ (provided δ is suﬃciently
small), Lemma 3.28 implies that ¯φ is J-convex ifε and δ are suﬃciently small. By
construction, ¯φ has properties (a-c).
Suppose now that φ satisﬁes the assumptions of (d). Consider a critical point
p∈ K of index 𝓁≤ k = dimL. We ﬁrst construct nice coordinates near p. Con-
sider the Hermitian vector space ( TpV,J,ω φ). Since by assumption E−
p ⊂ TpL
are isotropic subspaces of TpV , we ﬁnd a unitary isomorphism Φ : ( Cn,i,ω st)→
(TpV,J,ω φ) mapping R𝓁 to E−
p and Rk to TpL. Let F : Rk⊃O p (0)→ L be a
smooth embedding with d0F = Φ|Rk. If k < nextend F to a smooth embedding
Rn⊃O p (0)→ L with d0F = Φ|Rn. Using Proposition 5.55, we can extend F to
a smooth embedding F : Cn⊃O p (0)→V such that F∗J agrees with i to second
order along Rn. In particular, it satisﬁes d0F = Φ. We pull back all data under F

48 3. SMOOTHING
and denote them by the same letters. Consider the standard complex coordinates
zj =xj +iyj on Cn and write z = (u,v,w ) with
u := (x1,...,x 𝓁), v = (x𝓁+1,...,x k), w := (xk+1,...,x n,y 1,...,y n).
By construction, u are coordinates on E−
p and (u,v ) are coordinates on L. More-
over, the metricgφ coincides with the standard metric on Cn in these coordinates at
the point p = 0, and thus (v,w ) are coordinates on E+
p . We choose the Hermitian
metric near p = 0 so that it coincides with the standard metric on Cn to second
order along Rk (this is possible because J and i agree to second order along Rk),
and thus ρ(z) =|w|2 +O(|w|3). We deﬁne the vector ﬁeld
X(u,v,w ) := (−u,v,w )
near p = 0. Since the splitting TpV =E−
p ⊕E+
p is orthogonal with respect to the
Hessian Hpφ, and the Hessian is positive resp. negative deﬁnite on E+
p resp. E−
p ,
we have
dφ·X(z) =Hpφ(z,X (z)) +O(|z|3)
=−Hpφ(u, 0, 0) +Hpφ(0,v,w ) +O(|z|3)≥γ|z|2
for some constant γ >0. On the other hand, dρ·X(z) = 2|w|2 +O(|w|3) implies
|w|2≤dρ·X(z)≤ 3|w|2 and hence
d~φ·X(z)≥γ|z|2− 3 max{0,−f′(ρ)}|w|2≥γ(|u|2 +|v|2) + (γ− 3δ)|w|2≥ γ
2|z|2
provided that δ≤γ/6. This shows that X is gradient-like for φ and ~φ (and hence
for ¯φ) near p = 0. Outside a neighborhood of the critical points of φ, its gradient
vector ﬁeld∇φφ is also gradient-like for ¯φ if the functions are suﬃciently C1-close
(which can be arranged by making ε,δ small). The gradient-like vector ﬁeld for φ
and ¯φ is now obtained by interpolation betweenX near the critical points and∇φφ
outside.
Finally, we prove (e). Using f′≥−δ we estimate for ~φ =φ +f(ρ):
r∂r~φ =r∂rφ + 2f′(ρ)r2≥ (µ− 2δ)r2≥ 3
4µr2
forδ suﬃciently small. Next, using|φ−~φ|≤ Br2 for some constantB, we estimate
for ¯φ = (1−β)φ +β~φ:
r∂r ¯φ = (1−β)r∂rφ +βr∂r~φ + (~φ−φ)r∂rβ≥ 3
4µr2−Br2|r∂rβ|≥ µr2/2,
provided we can make |r∂rβ| arbitrarily small. For this, we write β as a product
β1β2. Here β1 =h◦π for the projectionπ :V →L alongr∂r andh a cutoﬀ function
on L, so r∂rβ1 = 0. The second function is of the form β2 = g(r) for a function
g : [0,ε ]→ [0, 1] which equals 1 near 0 and 0 near 1. The proof of Lemma 3.29
shows that we can ﬁnd such a function g with|∂rβ1| =|rg′(r)|≤ δ for arbitrarily
small δ. □
Proof of Proposition 3.26. Fix a compact neighborhood ~K⊂L∩U ofK
in L containing no critical points outside K. Take a Hermitian metric on ( V,J )
as in Lemma 3.30 and consider the function ρ := dist2
L, square of the distance to

3.5. J-CONVEX FUNCTIONS NEAR TOTALLY REAL SUBMANIFOLDS 49
LA
Sε(A)
Dε(∂A)
Figure 3.3. The tube Dε(A) around A.
0 φ ρ
γ
δ ε
φ +aρ
ˆφ
ψ
¯φ
Figure 3.4. Construction of the function ˆϑ.
L, deﬁned on a tubular neighborhood of L. According to Proposition 2.15, this
function is J-convex near L. Hence, after shrinking U,
φa :=φ +aρ
is J-convex on U for any a≥ 0.
For small ε> 0 denote by πε :Dε(L) :={ρ≤ε}→ L the projection onto the
nearest point. For a subset A⊂L set
Dε(A) :=π−1
ε (A), S ε(A) :=Dε(A)∩∂Dε(L),
see Figure 3.3.
Since φ and ψ agree up to ﬁrst order along L, there exists an a> 0 and ε> 0
such that
φa >ψ on Dε(~K)\L.
By Lemma 3.30 we ﬁnd a J-convex function ¯φ : Dε(~K)→ R which agrees with φ
near Sε(~K) and with φa on Dδ(~K) for some δ∈ (0,ε ), so ¯φ > ψon Dδ(~K)\L.
Next pick a cutoﬀ function α(ρ) which equals 0 for ρ≥δ and 1 for ρ≤δ/2. The
function
ˆφ := ¯φ−µα
is J-convex for µ> 0 suﬃciently small. Moreover, it satisﬁes
ˆφ<ψ on Dγ(~K), ˆφ>ψ near Sδ(~K), ˆφ =φ near Sε(~K)
for some γ∈ (0,δ ), see Figure 3.4. So the function
ˆϑ :=
{
smooth max(ψ,ˆφ) on Dδ(~K),
ˆφ on Dε(~K)\Dδ(~K)

50 3. SMOOTHING
coincides with ψ on Dγ(~K) and with φ near Sε(~K). Moreover, since ˆφ is C1-close
to φ by construction and Lemma 3.30, ˆϑ is C1-close to φ by Corollary 3.22.
It remains to interpolate between ˆϑ and φ near Dε(∂~K). For this, we ﬁx a
cutoﬀ function β :L→ R which equals 1 near K and 0 on L\ ~K and extend it to
Dε(~K) via the projection πε. By Lemma 3.28, the function
ϑ := (1−β)φ +βˆϑ
isJ-convex if we chooseˆϑ suﬃcientlyC1-close toφ. Since ψ agrees withφ together
with their diﬀerentials along L, the same holds for ϑ and φ. So ϑ has properties
(a-c).
For property (d), let X be the gradient-like vector ﬁeld for φ and ¯φ from
Lemma 3.30. The assumptions on ψ ensure that X is also gradient-like for ψ near
K. The function ˆφ is C1-close to ¯φ and diﬀers from ¯φ only by a constant near the
critical points, so X is gradient-like for ˆφ. Since the function ˆϑ is obtained by the
maximum construction and smoothing and agrees with ψ near the critical points,
X is gradient-like for ˆϑ by Corollary 3.20. Finally, X is gradient-like for ϑ because
ϑ is C1-close to ˆϑ and equals ˆϑ near the critical points.
Property (e) follows from Lemma 3.28, assuming that ∇φφ = λ∇ψψ at the
points of L where dβ ⁄= 0. Property (f) follows from Lemma 3.28 and the fact
that this property is preserved under the maximum construction (which is obvious)
and under the interpolation ϑ := (1−β)φ +βˆϑ (which was shown in the proof of
Lemma 3.28). This concludes the proof of Proposition 3.26. □
The corresponding result for J-convex hypersurfaces is
Corollary 3.31. Let Σ, Σ′ be J-convex hypersurfaces in a complex manifold
(V,J ) that are tangent to each other along a totally real submanifold L. Then
for any compact subset K⊂ L and neighborhood U of K, there exists a J-convex
hypersurface Σ′′ that agrees with Σ outside U and with Σ′ near K. Moreover, Σ′′
can be chosen C1-close to Σ and tangent to Σ along L.
Proof. Pick smooth functions φ,ψ with regular level sets Σ = φ−1(0) and
Σ′ = ψ−1(0) such that dφ = dψ along L. By Lemma 2.7, after composing φ
and ψ with the same convex function, we may assume that φ,ψ are J-convex
on a neighborhood W⊂ U of K. Let ϑ : W→ R be the J-convex function from
Proposition 3.26 which coincides withψ nearK and withφ outside a compact subset
W′⊂W . Since ϑ is C1-close to φ, it has 0 as a regular value and Σ ′′ :=ϑ−1(0) is
the desired J-convex hypersurface. □
3.6. Functions with J-convex level sets
According to Lemma 2.7, a function φ with compact regular J-convex level
sets can be made J-convex by composing it with a suﬃciently convex function
f : R→ R. Motivated by this, we now introduce a class of functions from which
we can recoverJ-convex functions, but which gives us greater ﬂexibility. This class
of functions will be used throughout the remainder of this book.
Let (V,J ) be a complex manifold. We call a continuous function φ : V → R
a function with J-convex level sets , or J-lc function (where “lc” stands for “level-
convex”) if g◦φ is J-convex for some smooth function g : R→ R with g′ > 0 and
g′′≥ 0.

3.6. FUNCTIONS WITH J-CONVEX LEVEL SETS 51
The following proposition shows that the main properties ofJ-convex functions
carry over to J-lc functions.
Proposition 3.32. Let (V,J ) be a complex manifold.
(a) If φ :V → R is J-lc then so is h◦φ for every smooth function h : R→ R
with h′ > 0.
(b) A proper C2-function φ : V → R is J-lc if and only if it is J-convex near
its critical points and its level sets are J-convex outside the critical points.
(c) Let φλ : V → R, λ∈ Λ be a compact continuous family of J-lc functions
such that gλ◦φλ areJ-convex for a continuous family of convex functions gλ : R→
R. Then maxλ∈Λφλ is J-lc.
(d) Every continuous J-lc function can be C0-approximated by smooth J-lc
functions.
(e) Letφ :V → R be a smoothJ-lc function andg1,g 2 : R→ R be weakly convex
functions such that ψi =gi◦φ are J-convex for i = 1, 2. Then ∇ψ1ψ1 =h∇ψ2ψ2
for a positive function h :V → R.
Here we call a function f : R→ R convex (resp. weakly convex) if f is an
increasing diﬀeomorphism and f′′ > 0 (resp. f′′≥ 0).
Remark 3.33. For aJ-lc functionφ we will write∇φφ for the gradient∇ψψ of
someJ-convex functionψ =g◦φ. In view of Proposition 3.32 (e), this is well-deﬁned
up to multiplication by a positive function. In particular, we can unambiguously
speak of the stable manifold of a critical point of a J-lc function.
The proof of Proposition 3.32 uses the following lemma.
Lemma 3.34. For every increasing diﬀeomorphism g : R→ R there exists a
smooth convex function f : R→ R such that f◦g is convex. More generally, for
every compact smooth family of increasing diﬀeomorphisms gλ : R→ R, λ∈ Λ,
there exists a smooth family of convex functions fλ : R→ R, λ∈ Λ, such that the
functions fλ◦gλ, λ∈ Λ, are all equal and convex.
Proof. We have
(f◦g)′ =f′◦g·g′, (f◦g)′′ =f′′◦g·g′2 +f′◦g·g′′.
So f◦g is convex if and only if
f′′(y)>h (y)f′(y), h (y) := max
{
0,− g′′◦g−1(y)
(
g′◦g−1(y)
)2
}
.
This inequality can obviously be solved by making h slightly larger and integrating
f′(y) :=e
∫y
0 h(x)dx to obtain f.
In the case of a family gλ : R→ R, λ∈ Λ, ﬁx some λ0∈ Λ. We need to ﬁnd
a convex function fλ0 such that fλ := fλ0◦gλ0◦g−1
λ is convex for all λ. By the
computation above, with f :=fλ0 and~gλ :=gλ0◦g−1
λ this is equivalent to
f′′(y)>h (y)f′(y), h (y) := max
{
0, max
λ∈Λ
−~g′′
λ◦~g−1
λ (y)
(
~g′
λ◦~g−1
λ (y)
)2
}
,
which again has a smooth solution f. □

52 3. SMOOTHING
Proof of Proposition 3.32. (a) Let φ be J-lc and g : R→ R be a convex
function such that g◦φ is J-convex. Then f◦g◦φ = (f◦g◦h−1)◦ (h◦φ) is
J-convex for every convex function f : R→ R. By Lemma 3.34, we ﬁnd f such
that f◦g◦h−1 is convex, which shows that h◦φ is J-lc.
(b) Assume ﬁrst that φ is J-convex near its critical points and its level sets
are J-convex outside the critical points. Note that the same properties then hold
for g◦φ for any smooth function g : R→ R with g′ > 0: J-convexity of the level
sets is clearly preserved, and at a critical point we have ddC(g◦φ) =f′◦φ·ddCφ,
which shows J-convexity ofg◦φ near critical points. Now by Lemma 2.7 (applied
outside a neighborhood of the critical points), we ﬁnd g such thatg′′ > 0 and g◦φ
is J-convex.
Conversely, let φ be J-lc and g : R→ R be a convex function such that g◦φ
isJ-convex. Then by the preceding observation, φ =g−1◦ (g◦φ) is J-convex near
its critical points and its level sets are J-convex outside the critical points.
(c) Let φλ :V → R and gλ : R→ R be as in the proposition such that gλ◦φλ
are J-convex. By Lemma 3.34, there exists a smooth family of convex functions
fλ : R→ R such that the functionsfλ◦gλ are all equal to the same convex function
g. Thus g◦φλ = fλ◦gλ◦φλ is J-convex for all λ, and by Proposition 3.8 so is
maxλg◦φλ. Then (a) implies that g−1◦ maxλg◦φλ = maxλφλ is J-lc.
(d) Let φ be J-lc and g : R→ R be a smooth convex function such that g◦φ
is J-convex. Let smooth( g◦φ) be a J-convex smoothing as in Section 3.2. Then
by (a) a smooth J-lc function approximating φ is given by g−1smooth(g◦φ).
(e) follows from the proof of Proposition 2.11, writing ψ1 = (g1◦g−1
2 )◦ψ2. □
3.7. Normalized modulus of J-convexity
Consider a K¨ ahler manifold (V,J,ω ). In this subsection we will derive condi-
tions on the modulus of J-convexity (of a function or a hypersurface) that ensure
K-convexity for complex structures K that are C2-close to J.
Given a quadratic form Q and a metric on a vector space we deﬁne
M(Q) := max
||T||=1
|Q(T )|, m (Q) := min
||T||=1
Q(T ),
where we will consider the second quantity only if Q is positive deﬁnite.
We begin with the case of a smooth J-convex functionφ :V → R. Recall from
Proposition 2.5 that the Hermitian form Hφ =−ddCφ is related to the real Hessian
Hessφ by
(3.9) Hφ(X) = Hessφ(X) + Hessφ(JX ).
Recall also that m(Hφ) : V → R+ is the modulus of J-convexity. We deﬁne the
normalized modulus of J-convexity by
(3.10) µ(φ) := m(Hφ)
max{M(Hessφ),|∇φ|} :V → R+.
Next we consider a J-convex hypersurface Σ in a K¨ ahler manifold. Recall that
its normalized Levi form is related to the second fundamental form by LΣ(X) =
IIΣ(X) +IIΣ(JX ). We call the ratio
(3.11) µ(Σ) := m(LΣ)
max{M(IIΣ), 1} : Σ→ R+
the normalized modulus of J-convexity of the hypersurface Σ.

3.7. NORMALIZED MODULUS OF J-CONVEXITY 53
In the following we will sometimes write M(φ),M(Σ),m(φ) and m(Σ) instead
of M(Hessφ), M(IIΣ), m(Hφ) and m(LΣ), respectively.
The main motivation for these deﬁnitions is the fact that a lower bound onµ(φ)
ensuresJ-convexity ofφ◦f for diﬀeomorphisms f :V →V suﬃcientlyC2-close to
the identity:
Lemma 3.35. (a) Let φ be a function on a K¨ ahler manifold (V,J,ω ) with
µ(φ)≥ ε > 0. Then m(φ◦f)≥ m(φ)/2 (in particular, φ◦f is J-convex) for
any diﬀeomorphism f :V →V with‖f− Id‖C2(V )≤ε/20.
(b) Let Σ be a cooriented hypersurface in a K¨ ahler manifold (V,J,ω ) with
µ(Σ)≥ ε > 0. Then m
(
f(Σ)
)
≥ m(Σ)/2 (in particular, f(Σ) is J-convex) for
any diﬀeomorphism f :V →V with‖f− Id‖C2(V )≤ε/20.
Proof. (a) By the chain rule, the Hessian Hess φ of the function φ changes
under composition with f by
Hessφ◦f− Hessφ =Df· Hessφ·Dft +D2f·∇φ− Hessφ
=Df· Hessφ· (Df− Id)t + (Df− Id)· Hessφ +D2f·∇φ.
Forδ :=‖f− Id‖C2≤ 1/2 this implies the estimate
‖Hessφ◦f− Hessφ‖≤ 5δ max{M(Hessφ),|∇φ|}.
For|X| = 1 and δ≤µ(φ)/20 we obtain using (3.9):
Hφ◦f(X)≥Hφ(X)− 10δ max{M(Hessφ),|∇φ|}
≥m(Hφ)
(
1− 10δ
µ(φ)
)
≥ 1
2m(Hφ).
(b) Let us ﬁrst compute how the second fundamental form at a point p on
a hypersurface Σ in Rm (with respect to the standard Euclidean metric) changes
under a diﬀeomorphism f : Rm → Rm. After applying a rigid motion we may
assume that p = 0 and Σ is the graph y = g(x) of a function g : Rm−1→ R with
g(0) = 0 and dg(0) = 0. After composing f with a rigid motion, we may assume
that ~Σ := f(Σ) is again the graph ~y = ~g(~x) of a function ~g : Rm−1→ R with
~g(0) = 0 and d~g(0) = 0. Writing ~z = (~x,~y) = f(x,y ) = f(z), the last condition is
equivalent to~xj(0) =~y(0) = ∂ ~y
∂xi
(0) = 0. So the Taylor expansion of f at the origin
is
~y =by + 1
2⟨x,Cx⟩ +O(y|z| +|x|3),
~x =Bx + ∂~x
∂yy +O(|z|2),
where
B =
(∂~xj
∂xi
)
, b = ∂~y
∂y, C =
( ∂~y
∂xi∂xj
)
.
The equation y =g(x) = 1
2⟨x,Ax⟩ +O(|x|3) for Σ is thus equivalent to
~y = 1
2b⟨x,Ax⟩ + 1
2⟨x,Cx⟩ +O(y|z| +|x|3)
= 1
2b⟨B−1~x,AB−1~x⟩ + 1
2⟨B−1~x,CB−1~x⟩ +O(~y|~z| +|~x|3),

54 3. SMOOTHING
and therefore the equation for ~Σ =f(Σ) is ~y =~g(~x) = 1
2⟨~x, ~A~x⟩ +O(|~x|3) with
~A =b(B−1)tAB−1 + (B−1)tCB−1.
Since A, ~A are the matrices of the second fundamental forms of Σ ,~Σ at the origin,
this yields as in (a) the estimate
‖IIf(Σ)−IIΣ‖ =‖~A−A‖≤ 5δ max{M(IIΣ), 1}.
The estimate m
(
f(Σ)
)
≥m(Σ)/2 if‖f− Id‖C2(V )≤µ(Σ)/20 follows from this as
in (a). □
The preceding lemma implies persistence of J-convexity under perturbations
of the complex structure in view of the following result.
Lemma 3.36. There exist constants Cn depending only on n ∈ N with the
following property. If J,K are two integrable complex structures on the unit ballB⊂
Cn, then there exists a biholomorphism h : (U,J )→ (V,K ) between neighborhoods
of 0 ﬁxing 0 and satisfying
‖h− Id‖C2(U)≤Cn‖J−K‖C2(B).
Proof. Suppose‖J−K‖C2(B) = δ. There exist linear isomorphisms S,T
with‖S−T‖≤ Cnδ, for a constant Cn depending only on n, such that S∗J =
T∗K =i at 0. The proof of the Newlander-Nirenberg Theorem 5.7.4 in [ 103] yields
a biholomorphism f : (U,S∗J)→ (U′,i ) between neighborhoods of 0, ﬁxing 0,
with a bound ‖f− Id‖C2(U)≤ C‖J−K‖C2(B). Let g : (V,T∗K)→ (V′,i ) be
the corresponding map for T∗K. Then h := T◦g−1◦f◦S−1 (between suitable
neighborhoods) has the desired properties. □
Corollary 3.37. Let φ be a function on an n-dimensional K¨ ahler manifold
(V,J,ω ) with µ(φ)≥ ε >0. Then the moduli of convexity (measured with respect
to the same reference metric) satisfy m(φ,K )≥m(φ,J )/4> 0 (in particular φ is
K-convex) for any complex structure K on V with‖J−K‖C2(V )≤ ε
20Cn
, where
Cn is the constant from Lemma 3.36.
Proof. Let δ :=‖J−K‖C2(V ). By Lemma 3.36, in a neighborhood of any
point p∈ Σ there exists a biholomorphism h : (Opp,J )→ (Opp,K ) ﬁxing p with
‖h−Id‖C2≤Cnδ. Then m(φ,K ) =m(φ◦h,J ) if measured with respect to metrics
g and h∗g, and m(φ,K )≥ 1
2m(φ◦h,J ) if both are measured with respect to the
same reference metric andδ is suﬃciently small. On the other hand, by Lemma 3.35
we havem(φ◦h,J )≥ 1
2m(φ,J ) if‖h−Id‖≤ Cnδ≤ε/20, from which the corollary
follows. □
The following result relates the moduli of convexity of functions and hypersur-
faces.
Proposition 3.38. Let Σ⊂ Cn be a compact J-convex hypersurface (possibly
with boundary). Then there exists a J-convex function ψ :Op Σ→ R such that
Σ⊂{ψ = 0} and at every point of Σ we have
|∇ψ| = 1, m (ψ)≥ m(Σ)
2 , M (ψ)≤ 6M(Σ)2
m(Σ) , µ (ψ)≥ µ(Σ)2
12 .

3.7. NORMALIZED MODULUS OF J-CONVEXITY 55
The proof is based on the following linear algebra lemma. Consider Cn ∼=
Cn−1⊕ R⊕iR with coordinates (z,u +iv). For a quadratic form Q : Cn−1× R→ R
deﬁne QC : Cn−1→ R, QC(z) =Q(z) +Q(iz), and for λ> 0 deﬁne
Qλ : Cn→ R, (z,u +iv)↦→Q(z,u ) +λv2.
Lemma 3.39. Suppose QC is positive deﬁnite. Then there exists λ > 0 such
that
m(QC
λ)≥ 1
2m(QC), M (Qλ)≤ 6M(Q)2
m(QC) .
Proof. Set M :=M(Q) and m :=m(QC). Then
|Qλ(z,u +iv)|≤| Q(z,u )| +λv2≤ max{M,λ}(|z|2 +u2 +v2)
and hence M(Qλ)≤ max{M,λ}. To estimate QC
λ we write Q(z,u ) = P (z) +
𝓁(z)u +au2 for a linear form 𝓁 : Cn−1→ R anda∈ R. By deﬁnition of M we have
|a|≤ M and 𝓁(z)u|≤ 2M|z||u|. Thus
QC
λ(z,u +iv) =Qλ(z,u +iv) +Qλ(iz,−v +iu)
=P (z) +P (iz) + (a +λ)(u2 +v2) +𝓁(z)u−𝓁(iz)v
≥m|z|2 + (λ−M)(u2 +v2)− 2M|z|(|u| +|v|).
The last line is ≥ m
2 (|z|2 +u2 +v2) if and only if
m
2|z|2 + (λ−M− m
2 )(u2 +v2)− 2M|z|(|u| +|v|)≥ 0,
which is easily seen to be the case for λ = 6M2/m. As noted above, for this choice
of λ we haveM(Qλ)≤ 6M2/m (recall that m≤M by deﬁnition). □
Proof of Proposition 3.38. Consider the metric decomposition U = Σ×
[−ε,ε ] of a tubular neighborhood U⊃ Σ, so that the coordinate t corresponding
to the second factor is the Euclidean distance from a point to Σ = {t = 0}. We
assume that Σ is cooriented by−∂t. We will ﬁnd the desired function ψ of the form
ψ(x,t ) =−t + 1
2λ(x)t2
for a suitable functionλ : Σ→ R+. Then clearly|∇ψ| = 1 along Σ. Let us compute
explicitly the function ψ. Take a point p ∈ Σ and choose unitary coordinates
(x1 +ix2,...,x 2n−3 +ix2n−2,x 2n−1 +iy) centered at p such that the hypersurface
Σ is given by an equation y =f(x), x = (x1,...,x 2n−1), and df(0) = 0. Because
the computation involves only the 2-jet of f we can assume that f is a quadratic
form. Let us introduce new coordinates u = (u1,...,u 2n−1),t , wheret is the signed
distance to Σ (assuming that Σ is cooriented by ∂
∂y ) and u is the x-coordinate of
the projection of the point to Σ. The coordinates are related by the formula
(x,y ) = (u,f (u)) + t√
1 +|∇f(u)|2 (−∇f(u), 1)
(see Figure 3.5), i.e.,
x =u− t√
1 +|∇f(u)|2∇f(u), y =f(u) + t√
1 +|∇f(u)|2.
The implicit function formulas for the ﬁrst and second derivatives of t with
respect to x and y involve only ﬁrst and second derivatives of the right-hand side

56 3. SMOOTHING
y = f (x)
f (u)
x u
t
Figure 3.5. The coordinate change from (x,y ) to (u,t ).
with respect to ( x,y,u,t ), and hence to compute the derivatives at the origin we
can ignore all the terms of higher degree than 2 with respect to these variables. We
will continue the computation systematically dropping terms of higher order than
2. Thus, writing f(u) = 1
2⟨u,Au⟩ we have
x =u−t∇f(u) =u−tAu, y =f(u) +t = 1
2⟨u,Au⟩ +t.
Solving for t and u (and again ignoring higher order terms) we get u = (1 +tA)x
and t =y−f(x), hence
ψ(x,y ) =−y +f(x) + 1
2λ(p)y2.
Note that Q = 2f is the second fundamental form of Σ and Q(x) +λ(p)y2 the
Hessian of ψ at p. So the estimates for m(ψ) and M(ψ) follow from the preceding
lemma, and they easily imply the estimate for µ(ψ) (distinguish the cases M≥ 1
and M <1). This proves Proposition 3.38. □
For a K¨ ahler manifold (V,J,ω ) and a continuous function φ : V → R we
introduce the quantity
m(φ;ε) := inf
‖f−Id‖C2≤ε
m(φ◦f).
Lemma 3.40. (a) For a continuous familyφλ,λ∈ Λ, over a compact parameter
space Λ we have
m(maxλ∈Λφλ;ε)≥ minλ∈Λm(φλ;ε).
(b) If m(φ;ε)> 0 the function φ can be smoothed to a function ~φ satisfying
m(~φ;ε/2)≥m(φ;ε)/2.
Proof. (a) By Proposition 3.8 we have m(maxλφλ)≥ minλm(φλ). Using
this and (max λφλ)◦f = maxλ(φλ◦f) we deduce
m(maxλφλ;ε) = inf
f
m
(
maxλ(φλ◦f)
)
≥ inf
f
minλm(φλ◦f) = minλm(φλ;ε).
(b) Consider ﬁrst the smoothing φδ of a function φ : Cn → R deﬁned by the
convolution formula (3.6). For a diﬀeomorphism f with‖f− Id‖≤ ε/2 andy∈ Cn

3.7. NORMALIZED MODULUS OF J-CONVEXITY 57
with|y|≤ δ≤ ε/2 the function fy(x) := f(x)−y satisﬁes‖fy− Id‖≤ ε and we
obtain
1
2π
∫ 2π
0
φδ◦f(z +weiθ)dθ =
∫
Cn
1
2π
∫ 2π
0
φ◦fy(z +weiθ)dθρδ(y)dy
≥
∫
Cn
[
φ◦fy(z) +m(φ;ε)(z)|w|2
]
ρδ(y)dy
=φδ◦f(z) +m(φ;ε)(z)|w|2.
This shows that m(φδ;ε/2)≥ m(φ;ε) for δ≤ ε/2, from which the result for the
smoothing ~φ easily follows. □
Now we can prove the main result of this section.
Proposition 3.41. There exist constants cn depending only on the dimension
n with the following property. Let M be a compact manifold (possibly with boundary)
of dimension 2n−1 and (J,ω ) a K¨ ahler structure onV =M× R. Let gλ :M→ R,
λ∈ Λ, be a C2-family of functions, parametrized over a compact manifold (possibly
with boundary) Λ. Denote by Σλ the graph of gλ, cooriented from below. Suppose
that the normalized moduli of convexity with respect to (J,ω ) satisfy µ(Σλ)≥ε> 0
for all λ∈ Λ. Then there exists a smoothing g of the function minλ∈Λgλ whose
graph Σ is K-convex for every complex structure K on V with‖K−J‖C2≤cnε2.
Proof. In the proof, all moduli of convexity are with respect to J.
By Proposition 3.38 there exists a smooth family of J-convex functions ψλ :
Op Σλ → R such that Σ λ ={ψλ = 0} and along Σ λ we have |∇ψλ| = 1 and
µ(ψλ)≥ε2/12.
By Lemma 3.35, we havem(ψλ;ε2/240)≥ε2/24 for allλ. By Lemma 3.40, the
function maxλψλ can be smoothed to a function ψ satisfyingm(ψ;ε/480)≥ε2/48.
Thus it follows from Lemma 3.36 and the deﬁnition of m(ψ;ε) that ψ is K-convex
for every complex structure K with‖K−J‖C2≤ ε2
480Cn
.
By Propositions 3.18 and 3.19, we have ∂r·ψ >0. Hence Σ = ψ−1(0) is the
graph of a smooth function g : M → R, and it is K-convex for every complex
structure K with‖K−J‖C2≤ cnε2, where cn := 1
480Cn
and Cn is the constant
from Lemma 3.36. □



4
Shapes for i-Convex Hypersurfaces
4.1. Main models
A crucial ingredient in the proof of the Existence Theorem 1.5 is the bending
of a J-convex hypersurface such that it “surrounds” the core disc of a handle as
shown in Figure 8.1. The main goal of this chapter is the proof of the following two
theorems which assert the existence of the necessary models in Cn.
Let us ﬁx integers 1 ≤k≤n. Viewing Cn as a real vector space with coordi-
nates (x1,...,x n,y 1,...,y n), let us deﬁne
R :=
vuu√
k∑
j=1
y2
j, r :=
vuu√
n∑
j=1
x2
j +
n∑
j=k+1
y2
j.
Theorem 4.1. For any a> 1 and γ∈ (0, 1) there exists an i-convex hypersur-
face Σ⊂ Cn with the following properties (see Figure 4.1):
(i) Σ is given by an equation Ψ(r,R ) = −1, and cooriented by ∇Ψ, for a
function Ψ(r,R ) satisfying ∂Ψ
∂r > 0 and ∂Ψ
∂R≤ 0;
(ii) in the domain {r≥ γ} the hypersurface Σ coincides with {ar2−R2 =
−1};
(iii) in the domain {R≤ 1} the hypersurface Σ coincides with {r = δ} for
some δ∈ (0,γ );
(iv) Σ is J-convex for any complex structure J which satisﬁes the estimate
(4.1) ‖J−i‖C2≤c(a,n )γ12,
wherec(a,n ) is a positive constant depending only ona and the dimension
n.
The hypersurface Σ divides Cn into two domains:
Cn = Ωext∪ Ωint, Ωext∩ Ωint = Σ,
where Ω int is the domain which contains the subspace {r = 0} which will later
correspond to the core disc of a handle. The second theorem provides an i-lc
function Ψ on the exterior domain Ω ext which agrees with the standard function
Ψst(r,R ) = ar2−R2 for r≥ γ and has Σ as a level set. Taking the maximum of
a given i-lc function with Ψ and extending it by Ψ st for r≥ γ will later allow us
to implant given functions near {r = 0} into a complex manifold and thus deform
J-lc functions near totally real discs. A ﬁrst example of this construction appears
in the proof of Corollary 4.4 below.
Theorem 4.2. For any a > 1 and γ ∈ (0, 1) there exists an i-lc function
Ψ : Ωext→ R with the following properties (see Figure 4.1):
(i) Ψ is of the form Ψ(r,R ) with ∂Ψ
∂r > 0 and ∂Ψ
∂R≤ 0;
59

60 4. SHAPES FOR i-CONVEX HYPERSURFACES
R
1
{Ψ = − 1 − σ}
Σ = {Ψ = − 1}
Ωext
δ γ r
Figure 4.1. The hypersurface Σ and the function Ψ.
(ii) Ψ(r,R ) =ar2−R2 in Ωext∩{r≥γ};
(iii) Ψ ≡− 1 on Σ;
(iv) Ψ is J-lc for any complex structure J which satisﬁes estimate (4.1) from
Theorem 4.1.
The proof of these two theorems will occupy the remainder of this chapter.
Properties (i-iii) of Theorem 4.1 will be proved at the end of Section 4.5, properties
(i-iii) of Theorem 4.2 at the end of Section 4.6, and property (iv) for both theorems
at the end of Section 4.7.
Let us formulate two corollaries of Theorem 4.2 that will be useful in later
chapters.
Corollary 4.3. For a > 1, γ ∈ (0, 1) and J as in Theorem 4.1 and any
suﬃciently small σ > 0 there exists an open subset Ω⊂ Cn and a J-lc function
Ψ : Ω→ (−1−σ,∞) with the following properties (see Figure 4.1):
(i) Ψ is of the form Ψ(r,R ) with ∂Ψ
∂r > 0 and ∂Ψ
∂R≤ 0;

4.2. SHAPES FOR i-CONVEX HYPERSURFACES 61
(ii) Ψ(r,R ) =ar2−R2 on Ω∩{r≥γ};
(iii) there exists a diﬀeomorphism f : (−1−σ,−1]→ (0,δ ] such that f◦
Ψ(r,R ) =r on the set {r≤δ, R≤ 1}.
Proof. Let us ﬁxa> 1 andγ∈ (0, 1). We apply Theorem 4.1 with parameters
a and tγ, t∈ (0, 1]. The corresponding hypersurfaces Σ t can be chosen to depend
smoothly ont so that on{R≤ 1} they coincide with{r =ρ(t)} for a diﬀeomorphism
ρ : (0, 1]→ (0,δ ]. We perturb the Σ t such that on {r≥ γ} they coincide with
{ar2−R2 =−1− (1−t)σ}. Using Proposition 3.25, we can then modify the Σ t on
the set{r≤γ, R≥ 1} to a foliation. Now deﬁne Ψ|Σt :=−1− (1−t)σ and extend
it over the domain Ω ext bounded by Σ = Σ 1 by the function in Theorem 4.2. □
Corollary 4.4. Fora> 1, γ∈ (0, 1) and J as in Theorem 4.1 there exists a
smooth family ofJ-lc functions Ψt : Cn→ R,t∈ [0, 1], with the following properties
(see Figure 4.2):
(i) Ψt is of the form Ψt(r,R ) with ∂Ψt
∂r > 0 and ∂Ψt
∂R ≤ 0;
(ii) Ψ 0(r,R ) =ar2−R2, and Ψt(r,R ) =ar2−R2 on{r≥γ}∪{R≥ 1 +γ};
(iii) Ψt is target equivalent to ar2−R2 near{r = 0};
(iv) Ψ 1≡− 1 on Σ from Theorem 4.1.
Proof. Let Ψ : Cn⊃ Ω→ (−1−σ,∞) be the function from Corollary 4.3.
After repeating the construction for smaller γ, we may assume that Ω∩{r≤γ}⊂
{R< 1+γ}. In particular, we then have 1+σ <(1+γ)2. Set Ψ st(r,R ) :=ar2−R2
and note that max {r≤γ,R≤1+γ}Ψst = aγ2 and min{r≤γ,R≤1+γ}Ψst =−(1 +γ)2.
Pick numbers−1−σ <b<c< −1 and smooth increasing functions g,h : R→ R
with the following properties:
• g(x)≤x, g(x) =x for x≤c and g(aγ2)<−1;
• h(x)≤x, h(x) =x for x≥b and h(−1−σ)<−(1 +γ)2.
Then the function Ψ 1 := smooth max(g◦ Ψst,h◦ Ψ) has the desired properties
for t = 1. Now the homotopy smooth max( ar2−R2, Ψ1 +t) connects ar2−R2
for very negative t to smooth max(ar2− R2, Ψ1) at t = 0, and the homotopy
smooth max(ar2−R2−t, Ψ1) connects the latter to Ψ 1 for large t. □
4.2. Shapes for i-convex hypersurfaces
We now derive the conditions under which a “shape function”R =φ(r) deﬁnes
an i-convex hypersurface in Cn. In this and the following section we ﬁrst consider
the critical case k =n. In Section 4.4 we will see that the same shapes also work
for the subcritical case k<n .
Consider the map
π : Cn→ R2, z ↦→ (r,R ) := (|x|,|y|)
for z =x +iy, x,y∈ Rn. The image of the map π is the quadrant
Q :={(r,R )|r,R≥ 0}⊂ R2.
A curve C⊂ Q deﬁnes a hypersurface Σ := π−1(C) in Cn. We call C the shape
of Σ. Our goal in this section is to determine conditions on C which guarantee
i-convexity of Σ.

62 4. SHAPES FOR i-CONVEX HYPERSURFACES
R
1
1 + γ
{Ψ1 = − 1 − σ}
Σ = {Ψ1 = − 1}
δ γ r
Figure 4.2. The function Ψ 1.
As a preliminary, let us compute the second fundamental form of a surface of
revolution. Consider Rk⊕ Rl with coordinates (x,y ) and Rk⊕ R with coordinates
(x,R =|y|). To a function Φ : Rk⊕ R→ R we associate the surface of revolution
ΣΦ :={(x,y )∈ Rk⊕ Rl| Φ(x,|y|) = 0}.
We coorient ΣΦ by the gradient∇Φ of Φ (with respect to all variables). Denote by
ΦR = ∂Φ
∂R the partial derivative.
Lemma 4.5. At every z = (x,y )∈ ΣΦ the splitting
TzΣΦ =
(
TzΣΦ∩ (Rk⊕ Ry)
)
⊕
(
TzΣΦ∩ (Rk⊕ Ry)⊥
)
is orthogonal with respect to the second fundamental form II . The second subspace
is an eigenspace of II with eigenvalue ΦR/|∇Φ|R.
Proof. The unit normal vector to Σ Φ at z = (x,y ) is
ν(z) = 1
|∇Φ|(∇xΦ, ΦR
R y),

4.2. SHAPES FOR i-CONVEX HYPERSURFACES 63
where∇xΦ denotes the gradient with respect to the x-variables. For Y⊥y we get
Dν(z)· (0,Y ) = 1
|∇Φ|(0, ΦR
R Y ) +µν
for some µ∈ R. From⟨ν(z),Dν (z)· (0,Y )⟩ = 0 we deduce µ = 0, so TzΣΦ∩ (Rk⊕
Ry)⊥ is an eigenspace of II with eigenvalue ΦR/|∇Φ|R. From this it follows that
II
(
(0,Y ), (X,λy )
)
=⟨Dν· (0,Y ), (X,λy )⟩ = 0
for (X,λy )∈TzΣΦ∩ (Rk⊕ Ry). □
Reduction to the case n = 2. Now let C⊂ Q be a curve. At a point
z =x +iy∈ Σ =π−1(C) consider the subspace Λxy⊂ Rn generated by the vectors
x,y∈ Rn and its complexiﬁcation
ΛC
xy := Λxy +iΛxy.
Let Λ⊥ be the orthogonal complement of Λ xy in Rn and Λ C
⊥ its complexiﬁcation
(which is the orthogonal complement of Λ C
xy in Cn). Note that Λ C
⊥ is contained
in TzΣ and thus in the maximal complex subspace ξz. So the maximal complex
subspace splits into the orthogonal sum (with respect to the metric)
(4.2) ξz =~Λ⊕ ΛC
⊥ =~Λ⊕ Λ⊥⊕iΛ⊥,
where ~Λ =ξz∩ ΛC
xy.
Lemma 4.6. The splitting (4.2) is orthogonal with respect to the second funda-
mental form II , and Λ⊥ and iΛ⊥ are eigenspaces with eigenvalues λr = Φr/|∇Φ|r
and λR = ΦR/|∇Φ|R, respectively.
Proof. Note that Σ can be viewed as a surface of revolution in two ways,
either rotating in the x- or the y-variables. So by Lemma 4.5, the splittings
(
ξz∩ (Rx⊕iRn)
)
⊕
(
ξz∩ (Rx⊕iRn)⊥
)
,
(
ξz∩ (Rn⊕iRy)
)
⊕
(
ξz∩ (Rn⊕iRy)⊥
)
are both orthogonal with respect to II and the right-hand spaces are eigenspaces.
In particular, Λ⊥ =ξz∩ (Rx⊕iRn)⊥ andiΛ⊥ =ξz∩ (Rn⊕iRy)⊥ are eigenspaces
orthogonal to each other with eigenvalues Φ r/|∇Φ|r and ΦR/|∇Φ|R. Since Λ C
xy is
the orthogonal complement of Λ⊥⊕iΛ⊥ in Cn, the lemma follows. □
It follows that the restriction of II to ΛC
⊥ = Λ⊥⊕iΛ⊥ has matrix
(
λr 0
0 λR
)
and by Proposition 2.13 the restriction of the normalized Levi form LΣ to Λ C
⊥ is
given by
LΣ(X) = (λr +λR)|X|2.
Now suppose thatC is given near the pointπ(z) by the equationR =φ(r), and
the curve is cooriented by the gradient of the function Φ( r,R ) = φ(r)−R. Since

64 4. SHAPES FOR i-CONVEX HYPERSURFACES
|∇Φ| =
√
Φ2r + Φ2
R =
√
1 +φ′(r)2, the eigenvalues λr on Λ⊥ and λR on iΛ⊥ equal
λr = Φr
|∇Φ|r = φ′(r)
r
√
1 +φ′(r)2,
λR = ΦR
|∇Φ|R =− 1
φ(r)
√
1 +φ′(r)2.
Hence the preceding discussions shows
Lemma 4.7. Let Σ = π−1(C) be the hypersurface given by the curve C =
{φ(r)−R = 0}, cooriented by the gradient of φ(r)−R. Then the restriction of the
normalized Levi form LΣ to ΛC
⊥ is given by
LΣ(X) = 1√
1 +φ′(r)2
(φ′(r)
r − 1
φ(r)
)
|X|2.
This restriction is positive deﬁnite if and only if
L⊥(φ) := φ′(r)
r − 1
φ(r) > 0.
In particular, if φ′(r)≤ 0 the restriction is always negative deﬁnite.
Lemma 4.7 reduces the question about i-convexity of Σ to positivity of L⊥(φ)
and the corresponding question about the intersection Σ∩ΛC
xy. When dim C ΛC
xy = 1,
this intersection is a curve which is trivially i-convex, hence Σ is i-convex if and
only if L⊥(φ) > 0. The remaining case dim C ΛC
xy = 2 just means that we have
reduced the original question to the case n = 2, which we will now consider.
The case n = 2. We denote complex coordinates in C2 by z = (ζ,w ) with
ζ =s +it, w =u +iv. The hypersurface Σ ⊂ C2 is given by the equation
√
t2 +v2 =R =φ(r) =φ(
√
s2 +u2).
We want to express the coeﬃcient L0 of the normalized Levi form LΣ(X) = L0|X|2
at a point z∈ Σ in terms of φ. Suppose that r,R > 0 at the point z. After a
unitary transformation
ζ↦→ζ cosα +w sinα, w ↦→−ζ sinα +w cosα
which leaves Σ invariant we may assumet = 0 andv >0. Then near z we can solve
the equation R =φ(r) for v,
v =
√
φ(
√
s2 +u2)2−t2 =:ψ(s,t,u ).
According to Lemma 2.25, the coeﬃcient of the normalized Levi form of the hyper-
surface Σ ={v =ψ(s,t,u )} is given by
L0 = 1
(1 +ψ2s +ψ2
t +ψ2u)
3
2
(
(ψss +ψtt)(1 +ψ2
u) +ψuu(ψ2
s +ψ2
t )
+ 2ψsu(ψt−ψuψs)− 2ψtu(ψs +ψuψt)
)
.

4.2. SHAPES FOR i-CONVEX HYPERSURFACES 65
Note that at the point z we havet = 0 and ψ(s, 0,u ) =φ(r) =φ(
√
u2 +s2). Using
this, we compute the derivatives at z:
ψs = φ′s
r , ψ ss = φ′′s2
r2 + φ′u2
r3 , ψ u = φ′u
r , ψ uu = φ′′u2
r2 + φ′s2
r3 ,
ψsu = φ′′su
r2 − φ′su
r3 , ψ t = 0, ψ tt =− 1
φ, ψ tu = 0.
Inserting this in the above expression for L0, we obtain
(1 +φ′2)3/2L0 =
(φ′′s2
r2 + φ′u2
r3 − 1
φ
)(
1 +φ′2u2
r2
)
+
(φ′′u2
r2 + φ′s2
r3
)φ′2s2
r2 − 2
(φ′′su
r2 − φ′su
r3
)φ′2su
r2
= φ′′s2
r2 + φ′u2
r3 + φ′3
r − 1
φ
(
1 +φ′2u2
r2
)
.
We say that the curveC is cooriented from aboveif it is cooriented by the gradient of
the functionφ(r)−R. Equivalently (sincet = 0 atz), the hypersurface Σ =π−1(C)
is cooriented by the gradient of
√
φ(
√
s2 +u2)
2
−t2−v, which is the coorientation
we have chosen above. The opposite coorientation will be called coorientation from
below. The preceding discussion leads to
Proposition 4.8. Let LΣ be the normalized Levi form of the hypersurface
Σ ={R =φ(r)}, cooriented from above, and suppose r> 0.
(a) The restriction of LΣ to ΛC
⊥ is given by
LΣ(X) = 1√
1 +φ′(r)2
(φ′(r)
r − 1
φ(r)
)
|X|2.
(b) The coeﬃcient L0 of the restriction of LΣ to ΛC
xy is given in suitable unitary
coordinatesζ =s +it,w =u +iv with r2 =s2 +u2 and R2 =t2 +v2 by
L0 = 1
(1 +φ′2)3/2
(φ′′s2
r2 + φ′u2
r3 + φ′3
r − 1
φ
(
1 +φ′2u2
r2
))
.
(c) The maximal absolute value M(II ) := max{|II (X)|;X∈T Σ,|X| = 1} of the
normal curvature of Σ equals
M(II ) = max
(
|φ′′|
(1 +φ′2)
3
2
, |φ′|
r
√
1 +φ′2, 1
φ
√
1 +φ′2
)
.
If Σ is J-convex, then φ′ > 0 and
M(II ) = max
(
|φ′′|
(1 +φ′2)
3
2
, φ′
r
√
1 +φ′2
)
.
Proof. Parts (a) and (b) follow from Lemma 4.7 and the preceding discussion.
For (c), we write Σ as the zero set of the function Φ( r,R ) =φ(r)−R. Assume
ﬁrst that x,y are linearly independent. Recall from Lemma 4.6 that the splitting
at z = (x,y )∈ Σ,
TzΣ = (TzΣ∩ ΛC
xy)⊕ Λ⊥⊕iΛ⊥,

66 4. SHAPES FOR i-CONVEX HYPERSURFACES
r
φ(r)
1
φ′
r
Figure 4.3. The normal curvature of the circle of radius r.
is orthogonal with respect to II and Λ⊥, iΛ⊥ are eigenspaces with eigenvalues
λr = Φr
|∇Φ|r = φ′(r)
r
√
1 +φ′(r)2, λ R = ΦR
|∇Φ|R =− 1
φ(r)
√
1 +φ′(r)2.
It remains to compute the eigenvalues on the 3-dimensional space TzΣ∩ ΛC
xy. De-
note by x⊥,y⊥ the unit vectors in Λ xy orthogonal to x,y such that (x/r,x⊥) and
(y/R,y⊥) are orthonormal bases deﬁning the same orientation as ( x,y ). Note that
the circle actions by rotation of the x resp. y coordinates leave Σ invariant and
are generated by x⊥ resp. y⊥. So by Lemma 4.5, these circle actions lead to a
II -orthogonal splitting
TzΣ∩ ΛC
xy = Rx⊥⊕TzΣ∩ (Rx⊕iRy)⊕iRy⊥.
The eigenvalue on TzΣ∩ (Rx⊕iRy) equals the curvature of the curve γ(r) =
(r,φ (r)), which is given (with the correct sign) by
λ =
√
|γ′|2|γ′′|2−⟨γ′′,γ′⟩2
|γ′|3 =
√
(1 +φ′2)φ′′2−φ′2φ′′2
(1 +φ′2)3/2 = φ′′
(1 +φ′2)3/2.
The eigenvalue on Rx⊥ equals the normal curvature of the circle of radius r in the
(x,y )-plane. This circle has curvature 1/r and normal projection amounts to multi-
plication by the factorφ′/
√
1 +φ′2 (see Figure 4.3), so the normal curvature equals
φ′/r
√
1 +φ′2 =λr. Similarly, the eigenvalue on iRy⊥ equals−1/φ
√
1 +φ′2 =λR
and the formula for M(II ) follows.
If x,y are linearly dependent, then TzΣ∩ ΛC
xy = TzΣ∩ (Rx⊕ iRy) is 1-
dimensional with eigenvalue λ and we obtain the same formula for M(II ).
If Σ is i-convex when cooriented from above, then the positivity of the expres-
sion in (a) implies that φ′
r > 1
φ > 0, so the third term in the formula for M(II ) is
dominated by the second term. □
Remark 4.9. The discussion in the preceding proof leads to an alternative
derivation of the normalized Levi form by computing the mean normal curvature.
The ﬁeld of complex tangencies ξz⊂TzΣ∩ ΛC
xy is spanned by the vectors
φ′x⊥ +iy⊥, i (φ′x⊥ +iy⊥) =−y⊥ +iφ′x⊥.

4.3. PROPERTIES OF i-CONVEX SHAPES 67
The spaceTzΣ∩ (Rx⊕iRy) is spanned by the vectorv :=x/r +iφ′(r)y/R. Denote
byτ the oriented angle from x to y in Λxy. Then
−y⊥ +iφ′x⊥ =− cosτx⊥ +iφ′ cosτy⊥ + sinτv,
and since x⊥,iy⊥,v are eigenvectors of II and|v|2 = 1 +φ′2 we obtain
II (φ′x⊥ +iy⊥) +II (−y⊥ +iφ′x⊥)
=φ′2λr +λR + cos2τλr +φ′2 cos2τλR + sin2τ(1 +φ′2)λ
= 1√
1 +φ′2
(φ′3
r + cos2τφ′
r − 1
φ(1 +φ′2 cos2τ) +φ′′ sin2τ
)
.
Dividing by|φ′x⊥ +iy⊥|2 = 1 +φ′2 and setting s = sinτr , u = cosτr , this yields
the coeﬃcient L0 in Proposition 4.8 (b) for the normalized Levi form LΣ(X) =
II (X) +II (iX) on Λ C
xy.
4.3. Properties of i-convex shapes
The precise expressions for the normalized Levi form LΣ in Proposition 4.8
will become important in Section 4.7. For now, we will only be interested in the
conditions for positivity LΣ which we restate in the following proposition.
Proposition 4.10. The hypersurface Σ ={R = φ(r)} is i-convex cooriented
from above at r> 0 if and only if φ satisﬁes the following two conditions:
(4.3) L⊥(φ) := φ′(r)
r − 1
φ(r) > 0,
(4.4) L2(φ) := φ′′s2
r2 + φ′u2
r3 + φ′3
r − 1
φ
(
1 +φ′2u2
r2
)
> 0
for all (s,u ) with s2 +u2 =r2. It is i-convex cooriented from below if and only if
the reverse inequalities hold.
The following corollary gives some useful suﬃcient conditions for i-convexity.
Corollary 4.11. (a) If φ> 0, φ′ > 0, φ′′≤ 0 and
(4.5) φ′′ + φ′3
r − 1
φ(1 +φ′2)> 0,
then Σ is i-convex cooriented from above.
(b) If φ> 0, φ′≤ 0, φ′′≥ 0 and
φ′′ + φ′3
r − 1
φ < 0,
then Σ is i-convex cooriented from below.
Proof. (a) If φ′ > 0 and φ′′≤ 0 we get
L2(φ)≥φ′′ + φ′3
r − 1
φ(1 +φ′2).
So positivity of the right hand side implies condition (4.4). Condition (4.3) is also
a consequence of φ′′ + φ′3
r − 1
φ(1 +φ′2)> 0.

68 4. SHAPES FOR i-CONVEX HYPERSURFACES
φ(r)
rεε−δ
ε
ε−δ
Figure 4.4. A quarter circle is an i-convex shape cooriented from below.
(b) If φ′≤ 0 and φ′′≥ 0 we get
L2(φ)≤φ′′ + φ′3
r − 1
φ.
So negativity of the right hand side implies the reverse inequality (4.4). The reverse
inequality (4.3) is automatically satisﬁed. □
As a ﬁrst application of Corollary 4.11 we have
Lemma 4.12. For any 0<δ <ε<
√
2δ the quarter circle
φ(r) :=ε−
√
δ2− (ε−r)2, r ∈ [ε−δ,ε ]
deﬁnes ani-convex hypersurface{R =φ(r)} cooriented from below (see Figure 4.4).
Proof. Fix 0<δ <ε<
√
2δ. Forr∈ [ε−δ,ε ] sets :=
√
δ2− (ε−r)2∈ [0,δ ].
We have
φ′(r) =−ε−r
s , φ ′′(r) = δ2
s3,
φ′′ + φ′3
r − 1
φ = 1
s3
(
δ2− (ε−r)3
r − s3
ε−s
)
.
Set t :=ε−r. Then we need to prove that
(4.6) F (t) := t3
ε−t + s3
ε−s >δ 2
for all t∈ [0,δ ], where s =
√
δ2−t2. We have
F′(t) =t
(t(3ε− 2t)
(ε−t)2 − s(3ε− 2s)
(ε−s)2
)
.
A short computation shows that the function G(t) := t(3ε−2t)
(ε−t)2 is strictly increasing
on [0,δ ]. It follows that the function F′(t)
t = G(t)−G(s) has a unique zero when
t =s, i.e.,t = δ√
2, is negative on [0, δ√
2) and positive on ( δ√
2,δ ]. Hence the function
F (t) attains its minimum at the point δ√
2. We compute F ( δ√
2) = δ3
√
2ε−δ , so the
condition ε<
√
2δ implies F ( δ√
2)>δ 2 and hence inequality (4.6). □

4.3. PROPERTIES OF i-CONVEX SHAPES 69
For the remainder of this chapter we will only be interested in hypersurfaces
{R =φ(r)} that arei-convex cooriented from above. We will call the corresponding
function φ satisfying the conditions of Proposition 4.10 an i-convex shape. The
following lemma lists some elementary properties of i-convex shapes.
Lemma 4.13 (Properties of i-convex shapes) . (a) If φ is an i-convex shape
then so is φ +c for any constant c≥ 0 (i-convexity from above is preserved under
upwards shifting).
(b) If φ is an i-convex shape at r >0, then the function φλ(r) := λφ(r/λ) is
an i-convex shape at λr for each λ> 0.
(c) If φ,ψ arei-convex shapes for r≤r0 resp.r≥r0 such that φ(r0) =ψ(r0)
and φ′(r0) =ψ′(r0), then the function
ϑ(r) :=
{
φ(r) for r≤r0,
ψ(r) for r≥r0
can beC1-perturbed to a smoothi-convex shape which agrees withϑ outside a neigh-
borhood ofr0.
(d) If φ,ψ arei-convex shapes, then the function
ϑ := max (φ,ψ )
can beC0-perturbed to a smoothi-convex shape which agrees withϑ outside a neigh-
borhood of the set {φ =ψ}.
Proof. (a) Ifφ satisﬁes one of the inequalities (4.3), (4.4) and (4.5), thenφ+c
satisﬁes the same inequality for any constant c≥ 0.
(b) can be seen by applying the biholomorphism z ↦→ λz on Cn, or from
Proposition 4.10 as follows: The function φλ has derivatives φλ(λr) = λφ(r),
φ′
λ(λr) =φ′(r), φ′′
λ(λr) =φ′′(r)/λ, and the replacement r↦→λr, φ↦→λφ, φ′↦→φ′,
φ′′↦→φ′′/λ leaves both conditions in Proposition 4.10 unchanged.
(c) follows from the fact that for given r,φ,φ′, the set of φ′′ such that condi-
tion (4.4) holds is convex.
(d) AfterC2-perturbing φ we may assume that the graphs of φ andψ intersect
transversely. Consider an intersection pointr0 such thatφ(r0) =ψ(r0) andφ′(r0)<
ψ′(r0), so near r0 we have
ϑ(r) =
{
φ(r) for r≤r0,
ψ(r) for r≥r0
.
We claim that for any δ,M > 0 there exist r− <r 0 <r + with|r+−r−|<δ and a
quadratic function χ : [r−,r +]→ R with the following properties:
• χ′′≡m≥M;
• χ(r−) =φ(r−), χ′(r−) =φ′(r−);
• χ(r+) =ψ(r+), χ′(r+) =ψ′(r+).
To see this, take for every suﬃciently closer− <r 0 a linear function a +br tangent
toφ atr− and add a quadratic term m(r−r−)2/2 to make it tangent to ψ at some
r+ >r 0, and note that r+→r0 and m→∞ as r−→r0.
We make χ smooth by decreasing χ′′ from m to φ′′(r−) near r− and from m
to ψ′′(r+) near r+.
It remains to show i-convexity of χ. Condition (4.3) holds for χ because it
holds for φ,ψ and up to an error of order δ for r ∈ [r−,r +] we have r ≈ r0,

70 4. SHAPES FOR i-CONVEX HYPERSURFACES
χ(r)≈ φ(r0) = ψ(r0) and χ′(r)∈ [φ′(r0),ψ′(r0)]. Next note that condition (4.4)
for s = 0 becomes (χ′
r − 1
χ
)
(1 +χ′2)> 0,
which is satisﬁed in view of condition (4.3). Since χ′′(r) is uniformly bounded from
below independently of δ, there exists a constant σ >0 independent of δ such that
χ satisﬁes condition (4.4) for all|s|≤ σ. Moreover, near r− resp.r+ condition (4.4)
holds for χ because it holds for φ,ψ and χ′′ is larger than φ′′ resp. ψ′′. So it
remains to consider the region where χ′′≡ m in the case |s|≥ σ. In this region
r,χ,χ′ are bounded independently of m. On the other hand, the term χ′′s2/r2
becomes arbitrarily large as m→∞ , so condition (4.4) holds for m suﬃciently
large. □
4.4. Shapes in the subcritical case
The following lemma extendsi-convex shapes to the subcritical case. Fork≤n
we set
r :=
√
x2
1 +··· +x2n +y2
k+1 +··· +y2n, R :=
√
y2
1 +··· +y2
k.
Lemma 4.14. Letφ(r) be an i-convex shape with φ′ > 0. Then:
(a) Σ :={R =φ(r)} is an i-convex hypersurface cooriented from above.
(b) Σ intersects the subspace iRn i-orthogonally in the sense that i(iRn) =
Rn⊂TiyΣ for any iy∈iRn∩ Σ.
(c) Σ is transverse to the vector ﬁeld
(4.7) X =
k∑
i=1
(
xi
∂
∂xi
−yi
∂
∂yi
)
+
n∑
j=k+1
(
xj
∂
∂xj
+yj
∂
∂yj
)
.
Proof. (a) Set ¯r :=
√
x2
1 +··· +x2n and ¯R :=
√
y2
1 +··· +y2n. By assump-
tion, the hypersurface ¯Σ := { ¯R = φ(¯r)} is i-convex cooriented from above. By
Lemma 2.7 there exists a convex increasing function f : R→ R withf(0) = 0 such
that the function
¯ψ : Cn→ R, ¯ψ(z) :=f
(
φ(¯r)− ¯R
)
is i-convex on the neighborhood ¯U := ¯ψ−1(
(−1, 1)
)
of ¯Σ.
Let us write z = (z′,z′′)∈ Cn = Ck⊕ Cn−k with z′ := (z1,...,z k) and z′′ :=
(zk+1,...,z n). The unitary group U(n−k) acts on Cn by rotation in the second
factor, gz = (z′,gz′′) for g∈U(n−k). Note that the functions ψg(z) := ¯ψ(gz) are
i-convex on the sets Ug :=ψ−1
g
(
(−1, 1)
)
=g−1( ¯U). Deﬁne
ψ : Cn→ R, ψ (z) := maxg∈U(n−k) ¯ψ(gz).
Since φ is increasing, the function
g↦→φ
(√
|Rez′|2 +|Re (gz′′)|2)
−
√
|Imz′|2 +|Im (gz′′)|2
for ﬁxed (z′,z′′) attains its maximum for Im (gz′′) = 0, so Re (gz′′) =z′′ and
ψ(z) =f
(
φ
(√
|Rez′|2 +|z′′|2)
−| Imz′|
)
=f
(
φ(r)−R
)
.
In particular, ψ is smooth with regular level set ψ−1(0) = Σ.

4.5. CONSTRUCTION OF SPECIAL SHAPES 71
We claim that ψ is i-convex near Σ. To see this, consider a point z∈ Σ. By
deﬁnition we have ψg(z)≤ 0 for all g∈U(n−k). Set
A :={g∈U(n−k)|ψg(z)≥− 1/2}.
Since A and U(n−k)\A are compact, there exists a neighborhood B of z on
which ψg >−1 for all g∈ A and ψg ≤− 1/4 for all g∈ U(n−k)\A. Thus
B′ := B∩ψ−1(
(−1/4, 1/4)
)
is a neighborhood of z on which ψ = max g∈Aψg∈
(−1/4, 1/4) and ψg∈ (−1, 1/4) for all g∈A. Since ψg is i-convex on B′⊂Ug for
all g∈ A, Proposition 3.8 implies i-convexity of ψ on B′. This shows that ψ is
i-convex near Σ, hence its level set Σ is also i-convex.
(b) is clear from the deﬁnition of Σ, and (c) follows from the computation
X·
(
φ(r)−R
)
=φ′(r)
( n∑
i=1
xi
∂r
∂xi
+
n∑
i=k+1
yi
∂r
∂yi
)
+
k∑
j=1
yj
∂R
∂yj
=φ′(r)r +R> 0.
□
4.5. Construction of special shapes
We will now construct special i-convex shapes satisfying the diﬀerential in-
equality in Corollary 4.11 (a). One such solution with the desired properties has
been constructed in [ 42]. The following simpliﬁed construction was pointed out to
us by M. Struwe. We will ﬁnd the function φ as a solution of Struwe’s diﬀerential
equation
(4.8) φ′′ + φ′3
2r = 0
withφ′ > 0 and hence φ′′ < 0. Then the inequality in Corollary 4.11 (a) reduces to
(4.9) φ′3
2r − 1
φ(1 +φ′2)> 0.
Lemma 4.15. For anyd,K,δ,λ> 0 satisfyingK≥e4/d2
and 4Kδ≤ (lnK)−3/2
there exists a solution φ : [λδ,Kλδ ]→ R of (4.8) with the following properties (see
Figure 4.5):
(a) φ′(λδ) = +∞ and λ +dλδ≤φ(λδ)<λ +dKλδ;
(b) φ(Kλδ) =λ +dKλδ and φ′(Kλδ)≤d;
(c) φ satisﬁes (4.9) and hence is the shape of an i-convex hypersurface coori-
ented from above.
Proof. First note that if φ satisﬁes equation (4.8) and inequality (4.9), then
so does the rescaled function λφ(r/λ). Thus it suﬃces to consider the case λ = 1.
The diﬀerential equation (4.8) is equivalent to
( 1
φ′2
)′
=−2φ′′
φ′3 = 1
r,
thus 1/φ′2 = ln(r/δ) for some constant δ >0, or equivalently,φ′(r) = 1/
√
ln(r/δ).
By integration, this yields a solution φ for r≥ δ which is strictly increasing and
concave and satisﬁes φ′(δ) = +∞. Note that
∫Kδ
δ φ′(r)dr =δK1 with
K1 :=
∫ K
1
du√
lnu
<∞.

72 4. SHAPES FOR i-CONVEX HYPERSURFACES
φ
rδ Kδ
φ(r)
1 + rd
1
1 + dδ
1 + dKδ
(λ = 1)
Figure 4.5. A solution of Struwe’s diﬀerential equation.
Fix the remaining free constant in φ by setting φ(Kδ) := 1 +dKδ, thus
φ(δ) = 1 +dKδ−K1δ.
Estimating the logarithm on [1,K ] from below by the linear function with the same
values at the endpoints,
lnu≥ lnK
K− 1(u− 1),
we obtain an upper estimate for K1:
(4.10) K1≤
∫ K
1
du√
lnK
K−1(u− 1)
=
√
K− 1
lnK
∫ K−1
0
du√u = 2(K− 1)√
lnK
.
By hypothesis we have
√
lnK≥ 2/d, hence K1≤d(K− 1). This implies
φ(δ)≥ 1 +dKδ−d(K− 1)δ = 1 +dδ.
Concavity ofφ impliesφ(r)≥ 1+dr for allr∈ [δ,Kδ ], and in particularφ′(Kδ)≤d.
Clearly φ(δ) < 1 + dKδ because φ is increasing. So it only remains to check
inequality (4.9). Denoting by ∼ equality up to a positive factor, we compute
(4.11)
φ′3
2r − 1
φ(1 +φ′2)≥ φ′3
2r − 1
1 +dr (1 +φ′2)
∼ φ′3
r (1 +dr)− 2− 2φ′2
∼ 1
r +d− 2 ln(r/δ)3/2− 2 ln(r/δ)1/2.

4.5. CONSTRUCTION OF SPECIAL SHAPES 73
The function on the right hand side is decreasing in r. So its minimum is achieved
for r =Kδ and has the value
1
Kδ− 2(lnK)3/2− 2(lnK)1/2 +d> 1
Kδ− 4(lnK)3/2≥ 0
by hypothesis. Here we have used the inequality 2(lnK)1/2 <d +2(lnK)3/2, which
follows for all d > 0 from the hypothesis K ≥ e4/d2
(arguing separately for the
cases d≤ 2 and d> 2). □
Remark 4.16. The proof of Lemma 4.15 shows that for given δ,K > 0 and
c∈ R the diﬀerential equation (4.8) has a unique solution φ satisfying φ′(δ) =∞
andφ(Kδ) =c, and this solution depends smoothly on δ,K,c . Indeed, the solution
φ is given by
φ(r) =c +
∫ r
Kδ
1√
ln(s/δ)
ds.
To obtain a shape for a hypersurface as in Theorem 4.1, we need to interpolate
between the function φ(r) in Lemma 4.15 (for λ = 1) near r =δ and the standard
function S(r) =
√
1 +ar2 near r = γ, for some given a >1 and γ∈ (0, 1). This
interpolation will occupy the remainder of this section. Since it is rather involved,
let us take a moment to explain why it needs to be so complicated.
The straightforward approach would be the following. Given a,γ let us try to
ﬁndd,K,δ > 0 as in Lemma 4.15 such thatKδ≤γ and the corresponding function
φ satisﬁesφ(Kδ)≤S(Kδ). Then the graphs of φ andS would intersect at a point
betweenδ and Kδ and a smoothing of max (φ,S ) would yield the desired shape.
Now the condition φ(Kδ) = 1 +dKδ≤S(Kδ) =
√
1 +a(Kδ)2 implies aKδ≥
2d +d2Kδ≥ 2d and thus 2d/a≤ Kδ≤ γ. This shows that d needs to be small
for ﬁxed a> 1 and small γ >0. On the other hand, the conditions K≥e4/d2
and
4Kδ≤ (lnK)−3/2 in Lemma 4.15 yield
2d
a ≤Kδ≤ 1
4(lnK)3/2≤ 1
4(4/d2)3/2 = d3
32
and thus d2≥ 64/a, which contradicts the inequality 2d/a≤γ for small γ. Hence
this approach fails.
Geometrically, the preceding computation shows that for small γ the graph of
φ will intersect that of the linear function L(r) = 1 +dr before it meets the graph
of S. The next attempt would be to follow φ from δ to the intersection with L,
then L up to the intersection with S, and then S up to γ. The problem with this
is that L is only i-convex for small r and the part of L used in the interpolation
fails to be i-convex. This forces us to introduce a further shape, the quadratic
function Q deﬁned below. The desired i-convex shape will then be constructed by
interpolating from φ to L to Q to S.
For numbersλ,a,b,c,d ≥ 0 consider the following functions:
• Sλ(r) =
√
λ2 +ar2 (standard function),
• Qλ(r) =λ +br +cr2/2λ (quadratic function),
• Lλ(r) =λ +dr (linear function).
Let us ﬁrst determine in which ranges they satisfy the inequalities (4.3) and (4.4).
Lemma 4.17. (a) The function Sλ(r) is the shape of an i-convex hypersurface
for λ≥ 0, a> 1 and r> 0.

74 4. SHAPES FOR i-CONVEX HYPERSURFACES
(b) The function Qλ(r) is the shape of an i-convex hypersurface for λ > 0,
b≥ 0, c> 1 and r> 0.
(c) The function Qλ(r) is the shape of an i-convex hypersurface for λ > 0,
b = 4−c, 0≤c≤ 4 and 0<r ≤ 2λ.
(d) The function Lλ(r) is the shape of an i-convex hypersurface for λ≥ 0,
d> 1 and r> 0.
(e) The function Lλ(r) is the shape of an i-convex hypersurface for λ > 0,
d> 0, and 0<r<λd 3.
Proof. First note that by Lemma 4.13 (b) we only need to prove the state-
ments for λ = 1. Set S :=S1, Q :=Q1, L :=L1. We denote by ∼ equality up to
multiplication by a positive factor.
(a) This holds because R =S(r) describes a level set of the i-convex function
φ(r,R ) =ar2−R2 for a> 1.
(b) Condition (4.3) follows from
Q′(r)Q(r)−r = (b +cr)(1 +br + cr2
2 )−r≥b +cr−r =b + (c− 1)r> 0,
and condition (4.4) from
L2(Q)≥ c(r2−u2)
r2 + (b +cr)u2
r3 + (b +cr)3
r − 1− (b +cr)2u2
r2
∼cr(r2−u2) + (b +cr)u2 +r2(b +cr)3−r3−r(b +cr)2u2
= (c− 1)r3 +bu2 +r2(b +cr)3−ru2(b +cr)2
≥ (c− 1)r3 +r2(b +cr)3−r3(b +cr)2
= (c− 1)r3 +r2(b +cr)2(
b + (c− 1)r
)
> 0.
(c) Condition (4.3) follows as in (b) from
Q′(r)Q(r)−r≥b +cr−r = 4−c(1−r)−r≥ 4− 4(1−r) = 4r−r> 0.
For condition (4.4) it suﬃces, by (b), to show that
A := (c− 1)r + (b +cr)2(
b + (c− 1)r
)
= (c− 1)r +
(
4−c(1−r)
)2(
4−c(1−r)−r
)
> 0.
Forc> 1 this follows from (b). Forc≤ 1 we have 4−c(1−r)≥ 3 and 4−c(1−r)−r≥
3−r, hence
A≥−r + 9(3−r) = 27− 10r> 0
for r≤ 2.
(d) Condition (4.3) follows from
L′(r)L(r)−r =d(1 +dr)−r =d + (d2− 1)r> 0,
and condition (4.4) from
L2(L) = du2
r3 + d3
r − 1
1 +dr
(
1 +d2u2
r2
)
∼ (1 +dr)du2 +d3r2(1 +dr)−r3−d2ru2
=du2 +d3r2 + (d4− 1)r3 > 0.

4.5. CONSTRUCTION OF SPECIAL SHAPES 75
(e) We will only use the weaker assumptionr(1−d4)<λd 3 instead ofr<λd 3.
Condition (4.3) follows from r(1−d2)<d 3/(1 +d2) via
L′(r)L(r)−r =d + (d2− 1)r≥d− d3
1 +d2 = d
1 +d2 > 0,
and condition (4.4) as in (d) from
L2(L) =du2 +d3r2 + (d4− 1)r3≥r2(
d3 + (d4− 1)r
)
> 0.
□
Lemma 4.18. (a) For λ,c > 0 and d > b >0 the functions Qλ(r) and Lλ(r)
intersect at a unique point λrQL > 0, where rQL = 2(d−b)/c.
(b) For λ > 0 and a > d2 > 0 the functions Lλ(r) and Sλ(r) intersect at a
unique point λrSL > 0, where rSL = 2d/(a−d2).
(c) For λ,b> 0, a>c ≥ 0 and 2b2(a +c)2 < (a−c)3 the functions Sλ(r) and
Qλ(r) intersect at precisely two pointsλrSQ,λr′
SQ satisfying 0<r SQ < 4b/(a−c)<
r′
SQ. Moreover, the points rSQ and r′
SQ depend smoothly on a,b,c .
See Figure 4.6.
Proof. (a) and (b) are simple computations, so we only prove (c). Again, by
rescaling it suﬃces to consider the caseλ = 1. First observe that forx> 0 andµ< 1
we have√1 +x> 1 +µx/2 provided that 1 +x> 1 +µx +µ2x2/4, or equivalently,
x< 4(1−µ)/µ2. Applying this to x =ar2, we ﬁnd thatS(r)> 1+µar2/2 provided
that
(4.12) r2 < 4(1−µ)
aµ2 .
Hence if
1 +µar2
2 =Q(r) = 1 +br + cr2
2
for some r >0 and µ <1 satisfying (4.12), then S(r) > Q(r). Assuming µa > c,
we solve the last equation for r = 2b/(µa−c). Inequality (4.12) becomes
r2 = 4b2
(µa−c)2 < 4(1−µ)
aµ2 ,
or equivalently,
(4.13) ab2µ2 < (1−µ)(µa−c)2.
Now pickµ := (a+c)/2a. The hypothesis a>c impliesµ< 1 andµa = (a+c)/2>
c. With µa−c = (a−c)/2 and 1−µ = (a−c)/2a, inequality (4.13) becomes
ab2
(a +c
2a
)2
< a−c
2a
(a−c
2
)2
,
or equivalently,
2b2(a +c)2 < (a−c)3.
Assume this inequality holds, so S(r+)>Q (r+) at the point
r+ = 2b
µa−c = 4b
a−c.
Now f(r) := Q(r)2−S(r)2 is a polynomial of degree 4 satisfying f(0) = 0 and
f(r)→ +∞ as r→±∞ . Since b >0, we have f(r) > 0 for r >0 close to zero

76 4. SHAPES FOR i-CONVEX HYPERSURFACES
1 1
1
L(r)
S(r)
Q(r)
L(r)
S(r)
Q(r)
L(r)
S(r)Q(r)
r
r
r
(a) (b)
(c)
rQL rSL rSQ r′
SQr′
SQ rQLrSLrSQ
rQL rSLrSQ r′
SQ
Figure 4.6. Intersections of the standard, linear and quadratic shapes.
and f(r) < 0 for r < 0 close to zero, so f(r−) = 0 for some r− < 0. By the
preceding discussion we have f(r+) > 0, so f has two more zeroes rSQ,r′
SQ with
0<r SQ <r + <r′
SQ. Since the 4 zeroes off are distinct they are all nondegenerate,
which implies smooth dependence on the parameters a,b,c . □
Now we combine Lemma 4.17 and Lemma 4.18 to show
Lemma 4.19. For every a > 1 and γ > 0 there exists d∈ (0, 1) and an in-
creasingi-convex shapeψ(r) which agrees with S(r) =
√
1 +ar2 forr≥γ and with
L(r) = 1 +dr for r close to 0.
Proof. Pick anyc∈ (1,a ). Pick b∈ (0, 1) such that 2b2(a+c)2 < (a−c)3 and
4b<γ (a−c). By Lemma 4.18 (c), thei-convex shapesS(r) andQ(r) = 1+br+cr2/2
intersect at a point 0 < rSQ < 4b/(a−c) < γ. Now pick d∈ (b, 1) such that
rQL = 2(d−b)/c satisﬁes rQL < rSQ and rQL < d3. By Lemma 4.18 (a), the
functions Q(r) and L(r) intersect at the point rQL, so we are in the situation of
Figure 4.6 (a). By Lemma 4.17 (e) the function L(r) is i-convex forr≤rQL. Now

4.5. CONSTRUCTION OF SPECIAL SHAPES 77
γδ
1
√
1 + aγ2
1 + √aγ
χ
r
χ(r)
√
1 + ar2
Figure 4.7. The i-convex shape χ cooriented from above.
the desired function is a smoothing of the function which equals L(r) for r≤rQL,
Q(r) for rQL≤r≤rSQ and S(r) for r≥rSQ. □
Remark 4.20. The proof of Lemma 4.19 uses only the criteria for i-convexity
of the functions Sλ, Qλ and Lλ given in Lemma 4.17 (a), (b) and (e). Given
constantsa> 1 andγ >0, the constantsc := (1+a)/2 andb :=γ(a−1)/16 satisfy
the conditions in the proof of Lemma 4.19 for γ suﬃciently small (which we may
assume without loss of generality). With this choice, the constant d in Lemma 4.19
satisﬁes γ(a− 1)/16<d< 1.
Now we are ready to prove the main result of this section.
Proposition 4.21. For every a >1 and γ >0 there exists δ∈ (0,γ ) and an
i-convex shape χ(r) cooriented from above which agrees with S(r) =
√
1 +ar2 for
r≥γ and satisﬁes χ′(δ) = +∞ and 1<χ (δ)< 1 +γ (see Figure 4.7).
Proof. By Lemma 4.19, there exists an increasing i-convex shapeψ(r) which
agrees with S(r) =
√
1 +ar2 for r≥γ and with L(r) = 1 +dr for r≤β, for some
d∈ (0, 1) and β∈ (0,γ ). Let φ : [δ,Kδ ]→ R+ be the i-convex shape provided by
Lemma 4.15, where K,δ >0 satisfy the conditions in Lemma 4.15 (with λ = 1 and
our given d) and in addition Kδ < β. Now the desired shape χ is a smoothing of
the function which equals φ for r≤Kδ and ψ for r≥Kδ. Note that property (a)
in Lemma 4.15 yields
1<χ (δ)< 1 +dKδ <1 +γ.
□
Remark 4.22. The proofs of Lemmas 4.15 and 4.19 show that the i-convex
shape χ in Proposition 4.21 can be chosen to depend smoothly on the parameters
a> 1, γ >0 and the suﬃciently small δ∈ (0,γ ). Let us choose a smooth function

78 4. SHAPES FOR i-CONVEX HYPERSURFACES
dδ
2dδ
δ 2δ r
dr
φ(r)
φ(r)+ c
(c < 0)
Figure 4.8. Another solution of Struwe’s diﬀerential equation.
(a,γ )↦→ δ(a,γ ), decreasing in γ, such that δ(a,γ )∈ (0,γ ) is suﬃciently small in
the sense of Proposition 4.21 (in particular δ(a,γ )→ 0 as γ→ 0 for any a). Then
we obtain a smooth family of increasing i-convex shapes χa,γ : [δ(a,γ ),∞)→ R,
a> 1, γ >0 with the properties in Proposition 4.21.
Proof of Theorem 4.1 (i-iii). With the shapeχ(r) in Proposition 4.21, the
desiredi-convex hypersurface Σ is given by{χ(r)−R = 0}∪{r =δ, R≤χ(δ)}. □
4.6. Families of special shapes
In this section we construct a family of i-convex shapes interpolating between
the function in Proposition 4.21 and the standard functions Sλ.
We begin by constructing another family of solutions to Struwe’s diﬀerential
equation (4.8).
Lemma 4.23. For any δ >0 and d≥ 4 there exists a solution φ : [δ, 2δ]→ R
of (4.8) with the following properties (see Figure 4.8):
(a) φ′(δ) = +∞ and φ(δ)≥dδ;
(b) φ(2δ) = 2dδ and φ′(2δ)≤d;
(c) φ satisﬁes (4.9) and hence is an i-convex shape.
Proof. The proof is similar to the proof of Lemma 4.15. By rescaling, it
suﬃces to consider the case δ = 1. Deﬁne the solution φ by φ′(r) := 1/
√
lnr and
φ(2) := 2d, thus
φ(1) = 2d−
∫ 2
1
du√
lnu
.
Estimating the integral as in (4.10) and using d≥ 4, we ﬁnd
φ(1)≥ 2d− 2√
ln 2
≥d + 4− 2√
ln 2
≥d,
since
√
ln 2≥ 1/2. Concavity of φ implies φ(r)≥ dr for all r ∈ [1, 2], and in
particular φ′(2)≤d. So it only remains to check inequality (4.9). Denoting by ∼

4.6. FAMILIES OF SPECIAL SHAPES 79
equality up to a positive factor, we compute
φ′3
2r − 1
φ(1 +φ′2)≥ φ′3
2r − 1
dr (1 +φ′2)
∼dφ′3− 2− 2φ′2
∼d− 2(lnr)3/2− 2(lnr)1/2.
The function on the right hand side is decreasing in r. So its minimum is achieved
for r = 2 and has the value
d− 2(ln 2)3/2− 2(ln 2)1/2 > 4− 2− 2 = 0,
since d≥ 4 and
√
ln 2< 1. □
Remark 4.24. Forφ as in Lemma 4.23 and any constant c≤ 0, the part of
the function φ +c that lies above the linear function dr isi-convex, see Figure 4.8.
Indeed, the last part of the proof applied to φ+c estimates the quantity in inequal-
ity (4.9) by d− 2(lnr1)3/2− 2(lnr1)1/2, where r1 is the larger intersection point of
φ +c and dr. Since r1≤ 2, this is positive.
Extend the standard function to λ< 0 and a> 1 by
Sλ(r) :=
√
ar2−λ2, r ≥|λ|/√a.
Note that Sλ is the shape of an i-convex hypersurface because its graph is a level
set of the i-convex function φ(r,R ) =ar2−R2.
We say that a family of i-convex shapes φλ : [δ,β ]→ R+ with φ′
λ(δ) = ∞
is (piecewise) smooth if their graphs {R = φλ(r)}, extended by the vertical line
below
(
δ,φλ(δ)
)
, form a (piecewise) smooth family of smooth curves in the positive
quadrantQ⊂ R2.
Lemma 4.25. Let Lλ(r) = λ +dλr, 0 < r≤ β, 0≤ λ≤ 1, be an increasing
smooth family of i-convex shapes, where λ↦→ dλ is decreasing with d0 = 8 and
0 < d1≤ 1. Then for any suﬃciently small δ∈ (0,β/ 4) there exists a piecewise
smooth family of increasing i-convex shapes φλ : [δ,β ]→ R,−8δ≤λ≤ 1, with the
following properties (see Figure 4.9):
(a) φ−8δ(r) =
√
64r2− 64δ2 for all r≥δ;
(b) φλ(r) =
√
64r2−λ2 for−8δ≤λ≤ 0 and r≥β/2;
(c) φλ(r) =Lλ(r) for 0≤λ≤ 1 and r≥β/2;
(d) φ′
λ(δ) =∞ for all λ;
(e) 1 <φ 1(δ)< 1 +β.
Proof. Step 1. For eachλ∈ (0, 1], set Kλ :=e4/d2
λ. Pick a smooth family
of constants δλ > 0 such that λδλ increases with λ and
4Kλδλ≤ (lnKλ)−3/2, K λλδλ <β/ 2.
By Lemma 4.15, there exist i-convex solutions φλ : [λδλ,Kλλδλ] → R of (4.8)
satisfying
• φ′
λ(λδλ) = +∞ and φλ(λδλ)≥λ +dλλδλ;
• φλ(Kλλδλ) =λ +dλKλλδλ and φ′
λ(Kλλδλ)≤dλ.

80 4. SHAPES FOR i-CONVEX HYPERSURFACES
1
1
2
ββ
2δ
r
L0
L1
L 1
2
φ0
φ1
φ 1
2
φ−8δ
Figure 4.9. Bending down linear shapes.
Step 2. Fromd0 = 8 and d1 < 1 we conclude K0 = e1/16 < 2 and K1≥
e4 > 2. Hence there exists a 0 < ¯λ <1 with K¯λ = 2. Set ¯δ := ¯λδ¯λ < β/4. By
Lemma 4.23 (with d = 8), there exists an i-convex solution ¯φ : [¯δ, 2¯δ]→ R of (4.8)
satisfying
• ¯φ′(¯δ) = +∞ and ¯φ(¯δ)≥ 8¯δ;
• ¯φ(2¯δ) = 16¯δ and ¯φ′(2¯δ)≤ 8.
By Lemma 4.13 (a), the functions
¯φλ := ¯φ(r) +Lλ(2¯δ)−L0(2¯δ)≥ ¯φ(r)
arei-convex for 0≤λ≤ ¯λ and ¯δ≤r≤ 2¯δ. Note that the functions φ¯λ and ¯φ¯λ have
the same value atr = 2¯δ and derivative∞ atr = ¯δ. Since they both solve the second
order diﬀerential equation (4.8), according to Remark 4.16 they coincide on [ ¯δ, 2¯δ].
Thus the families constructed above ﬁt together to a continuous family ( ˆφλ)λ∈[0,1]
with ˆφλ = φλ : [λδλ,Kλλδλ]→ R+ for λ≥ ¯λ, and ˆφλ = ¯φλ : [ ¯δ, 2¯δ]→ R+ for
λ≤ ¯λ. Set ¯δλ :=λδλ for λ≥ ¯λ and ¯δλ := ¯δ for λ≤ ¯λ and deﬁne ~φλ : [¯δλ,β ]→ R+
by
~φλ(r) :=
{ˆφλ(r) for r≤Kλδλ,
Lλ(r) for r≥Kλδλ.
After smoothing, the family ~φλ is i-convex and agrees with Lλ for r≥β/2.
Step 3. For−8¯δ≤τ≤ 0 consider the functions ¯φτ := ¯φ +τ : [¯δ, 2¯δ]→ R+.
By Remark 4.24, the portion of ¯φτ above the linear function L0 is i-convex. Thus
for 0 < δ <¯δ/2 suﬃciently small, the portion of ¯φτ above the function S−8δ is
i-convex. Here Sλ(r) =
√
64r2−λ2 is the standard function deﬁned above with

4.6. FAMILIES OF SPECIAL SHAPES 81
a = 64 and λ∈ [−8δ, 0]. For−8δ≤λ≤ 0 deﬁne ~φλ : [¯δ,β ]→ R+ by
~φλ(r) :=
{¯φ(r) +Sλ(2¯δ)−S0(2¯δ) for r≤ 2¯δ,
Sλ(r) for r≥ 2¯δ.
SinceSλ(r)−S0(r) is increasing inr forλ> 0, the condition ¯φ(¯δ)≥ 8¯δ ensures that
~φλ lies above Sλ. Thus after smoothing, the family ~φλ isi-convex for−8δ≤λ≤ 1
and agrees with Lλ (if λ ≥ 0) resp. Sλ (if λ ≤ 0) for r ≥ β/2. Now deﬁne
~ψλ : [δ,β ]→ R+ by
~φλ(r) :=
{
S−8δ(r) for r≤ ¯δλ,
~φ(r) for r≥ ¯δλ.
After smoothing, the family ~ψλ isi-convex for−8δ≤λ≤ 1 and satisﬁes conditions
(b-d).
Step 4. To arrange condition (a), note that ~ψ−8δ = max (S−8δ, ¯φ¯τ) for some
¯τ < 0. By the discussion above, the functions max ( S−8δ, ¯φτ) are i-convex for
−8¯δ≤ τ ≤ 0. For δ suﬃciently small, we have max ( S−8δ, ¯φ−8¯δ) = S−8δ. After
rescaling in the parameter λ, this yields a family ~ψλ satisfying conditions (a-d).
Step 5. To arrange condition (e), set δt := (2−t)δ1 + (t− 1)δ for t∈ [1, 2]
and let φt : [δt,K 1δt]→ R be the i-convex shape from Lemma 4.15 with λ = 1 and
δ replaced by δt. For λ∈ [1, 2] deﬁne ~ψλ : [δ,β ]→ R+ by
~φλ(r) :=



S−8δ(r) for r≤δλ,
φλ(r) for δλ≤r≤δ1,
L1(r) for r≥δ1.
Forλ = 1 this matches the previous family ~ψλ, so rescaling in λ yields the desired
family φλ. □
The following result is a family version of Lemma 4.19.
Lemma 4.26. For any γ >0 there exists a constant 0 < β < γand a smooth
family of increasing i-convex shapes ψλ : R+→ R+, λ∈ [0, 1], with the following
properties (see Figure 4.10):
(a) ψ0(r) = 8r for all r;
(b) ψλ(r) = λ +dλr for r≤ β and all λ, where λ↦→ dλ is decreasing with
d0 = 8 and 0<d 1≤ 1;
(c) ψλ(r) =
√
64r2 +λ2 for r≥γ and all λ.
Proof. Set a := 64 and c := 2. With this choice and λ∈ (0, 1] we consider
the functions
Sλ(r) =
√
λ2 +ar2, Q b,λ(r) =λ +br +cr2/2λ, L d,λ(r) =λ +dr
as above. Here the constants b,d will vary in the course of the proof but always
satisfy the condition
(4.14) 0 <b<d ≤b +b3 < 8.
Then the numerical condition in Lemma 4.18 (c), 2b2(64+2) 2 < (64−2)3, holds be-
causeb< 4. Hence all the numerical conditions in Lemma 4.18 are satisﬁed, so the

82 4. SHAPES FOR i-CONVEX HYPERSURFACES
1
1
2
β γ r
S0 =ψ0
S 1
2
S1
ψ1
ψ 1
2
Figure 4.10. Interpolation between standard and linear shapes.
functions Sλ,Qb,λ,Ld,λ intersect at points λrQL(b,d ),λrSL(d),λrSQ(b) satisfying
rQL(b,d ) = 2(d−b)
c , r SL(d) = 2d
a−d2, 0<r SQ(b)< 4b
a−c.
By condition (4.14) we have
rQL(b,d )≤b3 <d 3,
so the numerical condition in Lemma 4.17 (e) is satisﬁed for r≤ λrQL(b,d ). It
follows that the shape functionsSλ(r) andQb,λ(r) arei-convex for allr, andLd,λ(r)
is i-convex for r≤λrQL(b,d ). For each triple (b,d,λ ) we consider the function
ψb,d,λ := max (Sλ,Qb,λ,Ld,λ) =λψb,d,1(·/λ).
This function will be i-convex provided that the region where it coincides with
Ld,λ(r) is contained in the interval [0,λrQL(b,d )]. We say that ψb,d,λ is of type
(a) if rQL(b,d )≤rSL(d)≤rSQ(b);
(b) if rSQ(b)≤rSL(d)≤rQL(b,d );
(c) if rSQ(b)≤rQL(b,d )≤rSL(d);
see Figure 4.6 (where we have dropped the parameters b,d,λ ). Thus the function
ψb,d,λ is i-convex for types (a) and (b), but not necessarily for type (c).
After these preparations, we now construct the family ψλ in 4 steps.
Step 1. Consider λ = 1. Pick a pair (b1,d 1) satisfying (4.14) and such that
rQL(b1,d 1) = 2(d1−b1)
c <r SQ(b1)< 4b1
a−c <γ.
Then the shape function ψb1,d1,λ is of type (a) and therefore i-convex for all λ> 0,
and it agrees with Sλ for r≥β. Note that in particular we have rSL(d1)<γ .

4.6. FAMILIES OF SPECIAL SHAPES 83
Step 2. Fix a parameter 0 < λ∗ < γ/8. This condition ensures that for any
pair (b,d ) satisfying (4.14) we have λ∗rQL(b,d ),λ∗rSQ(b) < γ. We may assume
thatb1 in Step 1 is chosen so small that b2
1 <c/ (a−b2) for all b∈ [0,b 1]. Then for
anyb∈ [0,b 1] such that (b,d 1) satisﬁes (4.14) we have
rQL(b,d 1) = 2(d1−b)
c ≤ 2b3
c < 2b
a−b2 < 2d1
a−d2
1
=rSL(d1)<γ.
Let b∗
1∈ (0,b 1] be the solution of b∗
1 + (b∗
1)3 =d1. We claim that for all b∈ [b∗
1,b 1]
the function ψb,d1,λ∗ is of type (a) and therefore i-convex. Indeed, by Step 1 this
holds for b = b1. Since rSQ(b) depends smoothly on b, if ψb,d1,λ∗ changes its type
there must exist a b∈ [b∗
1,b 1] for which rSQ(b) = rSL(d1). But this implies also
rQL(b,d 1) =rSL(d1), contradicting the preceding inequality.
Step 3. Forb> 0 consider the function
f(b) := rQL(b,d )
rSL(d)
⏐⏐⏐
d=b+b3
= (d−b)(a−d2)
cd
⏐⏐⏐
d=b+b3
= b2(
a− (b +b3)2)
c(1 +b2) .
A short computation shows that f(0) = 0, f(1)> 1 and f′(b)> 0 for all b∈ (0, 1).
Thus there exists a uniqueb∗
2∈ (0, 1) withf(b∗
2) = 1, i.e.,rQL(b,b +b3) =rSL(b+b3)
precisely forb =b∗
2. Since b∗
1 <b∗
2, the functionψb,b+b3,λ∗ is of type (a) and therefore
i-convex for all b∈ [b∗
1,b∗
2]. For b∈ [b∗
2, 1] we have rQL(b,b +b3)≥ rSL(b +b3),
so the function ψb,b+b3,λ∗ is of type (b) and therefore also i-convex. Combining
this, we see that the function ψb,b+b3,λ∗ is i-convex for all b∈ [b∗
1, 1]. Moreover,
λ∗rSL(b +b3)<γ for all b∈ [b∗
1, 1], so ψb,b+b3,λ∗(r) =S∗
λ(r) for r≥γ.
Step 4. The previous step leads for b = 1 and d =b +b3 = 2 to the function
ψ1,2,λ∗. For d∈ [2, 8] deﬁne bd,λd by the conditions
bd +b3
d =d, λ drSL(d) =γ,
so
λd = γ(a−d2)
2d .
Note that b2 = 1, λ2 > λ∗, and ψ1,λ,2 is i-convex for all λ∈ [λ∗,λ 2] and agrees
with Sλ for r≥ γ. The same holds for the functions ψbd,d,λd for all d∈ [2, 8]. In
the limit d→ 8 we ﬁnd λ8 = 0 and thus the linear function
ψb8,8,0(r) = 8r.
Now we combine the homotopies ofi-convex functionsψb,d,λ in Steps 1-4: Start-
ing from (b1,d 1, 1) we ﬁrst decrease λ to (b1,d 1,λ∗) (Step 1), then decrease b to
(b∗
1,d 1,λ∗) (Step 2), next increase ( b,d ) simultaneously do (1, 2,λ∗) (Step 3), and
ﬁnally increase (b,d ) and decrease λ simultaneously to (b8, 8, 0). By construction,
each function ψb,d,λ during this homotopy coincides with the corresponding stan-
dard functionSλ forr≥γ and with the linear functionLλ forr≤β for some small
β >0. Moreover, during the homotopy λ is non-increasing andd is non-decreasing.
Smooth the functions ψb,d,λ and perturb the homotopy such that λ is strictly de-
creasing from 1 to 0 and d is strictly increasing from d1≤ 1 to 8. The resulting
homotopy, parametrized byλ∈ [0, 1], is the desired family ψλ. □
Now we are ready to prove the main result of this section. Recall that
Sλ(r) =
{√
64r2−λ2 : λ< 0,√
64r2 +λ2 : λ≥ 0.

84 4. SHAPES FOR i-CONVEX HYPERSURFACES
1
1
2
δ γ r
S0
S 1
2
S1
S−8δ = χ−8δ
χ1
χ 1
2
χ0
Figure 4.11. The family χλ of i-convex shapes cooriented from above.
Proposition 4.27. For every γ >0 and any suﬃciently small δ∈ (0,γ ) there
exists a piecewise smooth family of increasing i-convex shapes χλ : [δ,∞)→ R,
−8δ≤λ≤ 1, with the following properties (see Figure 4.11):
(a) χ−8δ(r) =
√
64r2− 64δ2 for all r≥δ;
(b) χλ(r) =Sλ(r) for r≥γ and all λ;
(c) χ′
λ(δ) =∞ for all λ;
(d) 1<χ 1(δ)< 1 +γ.
Proof. Let (ψλ)λ∈[0,1] be the family of i-convex shapes from Lemma 4.26
which agree with the standard functions Sλ(r) =
√
64r2−λ2 for r≥ γ and with
the linear functions λ +dλr for r≤ β, for some β∈ (0,γ ) and some decreasing
family λ↦→ dλ with d0 = 8 and 0 < d1≤ 1. On the other hand, Lemma 4.25
provides us with a family (φλ)λ∈[−8δ,1] which agrees with λ +dλr for r≥β/2 and
λ∈ [0, 1], and with Sλ(r) =
√
64r2−λ2 forr≥β/2 and λ∈ [−8δ, 0], for the given
β,dλ and suﬃciently small δ∈ (0,β/ 4). Since ψ0(r) = 8r = S0(r), we can deﬁne
the required family χλ : [δ,∞)→ R,−8δ≤λ≤ 1, by
χλ(r) :=



φλ(r) : r∈ [δ,β/ 2],λ∈ [−8δ, 1],
ψλ(r) : r>β/ 2,λ∈ [0, 1],
Sλ(r) : r>β/ 2,λ∈ [−8δ, 0].
□
Remark 4.28. The proofs of Lemmas 4.25 and 4.26 show that the family χλ
in Proposition 4.27 can be chosen to depend smoothly on the parameters γ > 0
and the suﬃciently small δ∈ (0,γ ). Let us choose a smooth decreasing function

4.7. CONVEXITY ESTIMATES 85
γ↦→δ(γ) such thatδ(γ)∈ (0,γ ) is suﬃciently small in the sense of Proposition 4.27
(in particular δ(γ)→ 0 as γ→ 0). Then we obtain a smooth family of increasing
i-convex shapes χλ,γ : [δ(γ),∞)→ R,−8δ(γ)≤ λ≤ 1, γ >0 with the properties
in Proposition 4.27.
According to Proposition 3.41, the family of i-convex hypersurfaces {R =
χλ(r)} in Proposition 4.27 can be turned into a foliation. The following reﬁne-
ment of Proposition 3.41 shows that this can be done within the class of shapes.
Corollary 4.29. If the hypersurfaces Σλ in Proposition 3.41 are all given by
shapesR =φλ(r) in Cn, then so is Σ.
Proof. Note that a hypersurface is given by a shape if and only if it is in-
variant under the group of rotations G = O(k)×O(2n−k) and transverse to
the vector ﬁeld R∂R. The latter property is clearly preserved during the proof of
Proposition 3.41. For the ﬁrst property, note that the function ψ constructed in
Proposition 3.38 depends only on M(Σ) and the Euclidean distance from Σ, both
of which areG-invariant if Σ is. Clearly G-invariance is preserved under taking the
maximum. According to Remark 3.14, the smoothing on Cn can be done by convo-
lution followed by interpolation. Convolution preserves G-invariance if we choose
the smoothing kernel G-invariant, and the interpolation can be done in the class of
G-invariant functions. □
Proof of Theorem 4.2 (i-iii). We ﬁrst apply Proposition 3.26 to the i-con-
vex functionsφ(r) =ar2−R2 andψ(r,R ) = 64r2−R2 which coincide to ﬁrst order
along the totally real submanifold {r = 0} and have a nondegenerate critical point
at the origin. So we ﬁnd an i-convex function ϑ : Cn→ R with a unique critical
point at the origin which coincides with ar2−R2 on{r≥γ} and with 64r2−R2
on{r≤ γ′}, for some γ′∈ (0,γ ). Thus the level sets ϑ = c≥− 1 coincide along
{r =γ′} with the shapes χλ from Proposition 4.27 (extended by Sλ for λ< −8δ).
By Proposition 3.25 we can modify the hypersurfaces Σ λ ={R =χλ(r)}, keeping
them ﬁxed near r = γ′ and near λ = 1, to a foliation of the region {r≤ γ′,R ≤
χ1(r)} by i-convex hypersurfaces ~Σλ. By Corollary 4.29 we can arrange that the
~Σλ are again given by shapes. The function ϑ on{γ′≤r≤γ} extends canonically
to a function Ψ on {r≤γ,R ≤χ1(r)} with regular i-convex level sets ~Σλ. □
4.7. Convexity estimates
The i-convex hypersurfaces on Cn constructed in the previous sections can
be transplanted to complex manifolds by holomorphic embeddings, providing J-
convex surroundings for real analytic totally real submanifolds. In this section we
derive quantitative estimates on the normalized modulus of i-convexity of these
hypersurfaces which ensure that they remain J-convex under “approximately holo-
morphic” embeddings. This provides J-convex surroundings for smooth totally real
submanifolds, and simpliﬁes many subsequent arguments by avoiding real analytic
approximations.
We will only consider i-convex shapes φ(r) for 0 <r ≤ 1 and with 0 <φ ≤ 2.
By Proposition 4.8 this implies φ′ >r/φ ≥r/2 and
M(IIΣ)≥ φ′
r
√
1 +φ′2≥ 1/2√
1 +r2/4
≥ 1/2√
1 + 1/4
≥ 1
3.

86 4. SHAPES FOR i-CONVEX HYPERSURFACES
Thus the normalized modulus of i-convexityµ(Σ) (see Section 3.7) satisﬁes
3µ(Σ) = 3m(LΣ)
max{M(IIΣ), 1}≥ 3m(LΣ)
max{3M(IIΣ), 1} = m(LΣ)
M(IIΣ) =: ¯µ(Σ).
Therefore, in the following it will suﬃce to estimate ¯µ(Σ) from below. One advan-
tage of ¯µ overµ is that the former is invariant under rescaling ( r,R )↦→ (λr,λR ).
We will also refer to ¯µ as the normalized modulus of convexity.
Our point of departure is the following consequence of Proposition 4.8.
Proposition 4.30. Suppose a hypersurface Σ⊂ Cn is given by the shape R =
φ(r), cooriented from above, and that r >0, φ′ > 0. Then the inequality ¯µ(Σ) >
ε> 0 for the normalized modulus of i-convexity of Σ is equivalent to the following
system of inequalities, stronger than (4.3) and (4.4):
(4.15) L⊥
ε,1(φ) :=−ε |φ′′|
1 +φ′2 + φ′
r − 1
φ > 0,
(4.16) L⊥
ε,2(φ) := (1−ε)φ′
r − 1
φ > 0,
(4.17) L2
ε,1(φ) := s2φ′′
r2 −ε|φ′′| + φ′u2
r3 + φ′3
r − 1
φ
(
1 +φ′2u2
r2
)
> 0,
(4.18) L2
ε,2(φ) := φ′′s2
r2 + φ′u2
r3 + φ′3
r − 1
φ
(
1 +φ′2u2
r2
)
− εφ′
r (1 +φ′2)> 0
for all (s,u ) with s2 +u2 =r2. If φ′ > 0,φ′′≤ 0 and 0<ε< 1 then the following
inequality implies ¯µ(Σ)>ε :
(4.19) φ′′ + (1−ε)φ′3
r − 1
φ(1 +φ′2)− εφ′
r > 0.
In particular, if φ′ > σ >0,φ′′≤ 0 and 0 < ε≤ min (1
8, σ2
8 ), then the following
inequality is suﬃcient for ¯µ(Σ)>ε :
(4.20) φ′′ + 3φ′3
4r − 1
φ(1 +φ′2)> 0.
Proof. By Proposition 4.8, the condition ¯µ(Σ)>ε is equivalent to
min
(
1√
1 +φ′2
(φ′
r − 1
φ
)
, L0
)
>ε max
(
|φ′′|
(1 +φ′2)
3
2
, |φ′|
r
√
1 +φ′2
)
,
where L0 is given by
L0 = 1
(1 +φ′2)3/2
(φ′′s2
r2 + φ′u2
r3 + φ′3
r − 1
φ
(
1 +φ′2u2
r2
))
.
Expanding this condition yields the four inequalities (4.15) to (4.18).
If φ′′ ≤ 0 inequality (4.19) clearly implies (4.18) for all ε. To see that it
implies (4.17), we divide (4.19) by 1 −ε and drop the last term to obtain
φ′′
1−ε + φ′3
r − 1
(1−ε)φ(1 +φ′2)> 0.

4.7. CONVEXITY ESTIMATES 87
Since 1/(1−ε)> 1 +ε this implies (4.17). For (4.16) note that
0<φ′′ + (1−ε)φ′3
r − 1
φ(1 +φ′2)− εφ′
r <φ′2
((1−ε)φ′
r − 1
φ
)
,
and henceL⊥
2,ε = (1−ε)φ′
r − 1
φ > 0. Furthermore, we have
(1 +φ′2)L⊥
1,ε =εφ′′ + (1 +φ′2)
(φ′
r − 1
φ
)
>εφ′′ +φ′2
(φ′
r − 1
φ
)
>φ′′ +φ′2
(φ′
r − 1
φ
)
>φ′′ + (1−ε)φ′3
r − 1
φ(1 +φ′2)− εφ′
r > 0,
and hence (4.19) implies (4.15).
Finally, the derivative bound φ′ > σ implies that εφ′
r < φ′3
8r for ε≤ σ2
8 , and
hence (4.20) implies (4.19) for ε≤ min (1
8, σ2
8 ) . □
The following is a quantitative version of Lemma 4.15.
Lemma 4.31. For anyd,K,δ,λ> 0 satisfyingK =e4/d2
and 8Kδ≤ (lnK)−3/2
there exists a solution φ : [λδ,Kλδ ]→ R of (4.8) which satisﬁes properties (a) and
(b) from Lemma 4.15. In addition, φ satisﬁes (4.20) for r∈ [λδ,Kλδ ), and hence
the corresponding hypersurface Σ satisﬁes ¯µ(Σ)> min (1
8, d2
32).
Proof. By rescaling we need only consider the case λ = 1. We deﬁne φ as in
the proof of Lemma 4.15, so it satisﬁes (a) and (b). Moreover, K = e4/d2
implies
φ′(Kδ) = 1/
√
lnK = d/2. Since φ is concave, this shows that φ′(r)≥ d/2 for all
r∈ [δ,Kδ ]. Hence according to Proposition 4.30 (iv) withσ =d/2, inequality (4.20)
is suﬃcient for ¯µ(Σ) > ε = min ( 1
8, d2
32). Using that φ is a solution of (4.8), this
reduces to the inequality
φ′3
4r − 1
φ(1 +φ′2)> 0.
Arguing as in (4.11) we conclude that the bound 8 Kδ ≤ (lnK)−3/2 yields this
inequality. □
The next lemma is a quantitative version of Lemma 4.17.
Lemma 4.32. (a) The functionSλ(r) forλ∈ R,a> 1 andr> max{0,−λ/√a}
satisﬁes ¯µ = (a− 1)/a.
(b) The function Qλ(r) for λ > 0, b > 0, c > 1 and r > 0 satisﬁes ¯µ≥
min{1− 1/c,b 2/(1−b2)}.
(c) The function Qλ(r) forλ> 0, b = 4−c, 0≤c≤ 1 and 0<r ≤ 2λ satisﬁes
¯µ≥ 1/5.
(d) The function Lλ(r) for λ≥ 0, d> 1 and r> 0 satisﬁes ¯µ≥ d2−1
d2(d2+1).
(e) The function Lλ(r) for λ > 0, d > 0 and 0 < r < λd3 satisﬁes ¯µ ≥
min (d6, 1)/4.
Proof. (a) The Hessian and the complex Hessian of the function Ψ( r,R ) =
1
2(ar2−R2) deﬁning Σ are
HessΨ = diag(a,...,a, −1,..., −1), H Ψ = diag(a− 1,...,a − 1).

88 4. SHAPES FOR i-CONVEX HYPERSURFACES
Thusm(HΨ) =a− 1, M(HessΨ) = 1, and Lemma 2.24 yields
¯µ(Σ) = m(HΨ)
M(HessΨ) = a− 1
a .
For properties (b-e) note that rescaling ( r,R )↦→ (λr,λR ) preserves ¯µ(Σ) =
m(Σ)/M(Σ), hence we can in the following assume that λ = 1.
(b) We haveL⊥
ε,1(Q)> Q′
r − 1
Q > 0 and
L⊥
ε,2(Q) = (1−ε)b +cr
r − 1
Q(r) > (1−ε)c− 1≥ 0
if ε≤ 1− 1/c. Note that since Q′′≥ 0 the inequality L2
ε,1(Q) > 0 is weaker than
L2(Q)> 0 and hence satisﬁed according to Lemma 4.17. Arguing as in Lemma 4.17
we get
r3L2
ε,2(Q)
= (c− 1)r3 +bu2 +r2(b +cr)3−ru2(b +cr)2−εr2(b +cr)(1 + (b +cr)2)
> (c− 1)r3 + (1−ε)r2(b +cr)3−r3(b +cr)2−εr2(b +cr)
= (c− 1−cε)r3 +r2(b +cr)2[(1−ε)b + (c− 1−cε)r]−εbr2 =:A.
The assumption ε≤ 1− 1/c ensures that c− 1−cε >0 and dropping the corre-
sponding terms we get
A≥r2b2(1−ε)b−εbr2 =br2[(1−ε)b2−ε]≥ 0
if ε≤b2/(1 +b2).
(c) The inequalities L⊥
ε,1(Q) > 0 and L2
ε,1 > 0 follow exactly as in (b). The
inequalityL⊥
ε,2(Q)> 0 follows from r≤ 2, b = 4−c and c≤ 1 via
rL⊥
ε,2(Q)> (1−ε)(b +cr)−r = (1−ε)b + (c− 1−cε)r
≥ (1−ε)(4−c)− 2(c− 1−cε) = (1−ε)(4−c− 2c) + 2
≥ 1−ε + 2> 0.
To show that L2
ε,2 > 0 we ﬁrst note that b +cr = 4−c(1−r)≥ 3 due to our
assumptions. Using this and r≤ 2, we estimate the term A from (b) by
A≥ (c− 1−cε)r3 + 9r2[3(1−ε)−r]−ε(4−c)r2
≥−r3 + 27(1−ε)r2− 9r3− 4εr2∼ 27− 31ε− 10r≥ 7− 31ε> 0
if ε≤ 1/5< 7/31.
(d) Since L′′ = 0 inequalities (4.15) and (4.17) are the same as (4.3) and (4.4),
and are veriﬁed in Lemma 4.17. For condition (4.16) we compute
rL(r)L⊥
ε,2(L) = (1−ε)L′(r)L(r)−r = (1−ε)d(1 +dr)−r
= (1−ε)d +
[
(1−ε)d2− 1
)
]r = (1−ε)d +Br

4.7. CONVEXITY ESTIMATES 89
with B := (1−ε)d2− 1, which is positive if ε <1− 1
d2 . For condition (4.18) we
compute
L2
ε,2(L) = du2
r3 + (1−ε)d3−εd
r − 1
1 +dr
(
1 +d2u2
r2
)
∼ (1 +dr)du2 +d3(1−ε)r2(1 +dr)−εdr2−εd2r3−r3−d2ru2
=du2 + [d3(1−ε)−εd]r2 + [d4(1−ε)− 1−εd2]r3
≥ [d3(1−ε)−εd]r2 + [d4(1−ε)− 1−εd2]r3
∼ [d3(1−ε)−εd] + [d4(1−ε)− 1−εd2]r
=:Cr +D.
Now D > 0 if and only if ε <1− 1
d2 , which holds by assumption, and C > 0 if
and only if ε < d2/(1 +d2), which also follows from the assumption on ε because
d2/(1 +d2)< 1− 1/d2 for all d> 1.
(e) Inequalities (4.15) and (4.17) hold as in (d). For condition (4.18) it suﬃces
to showCr +D> 0, where C,D are the expressions deﬁned in (d). We distinguish
two cases.
Case 1: D> 0. This implies d> 1 and ε< 1− 1/d2 and thus C >0 as in (d).
Case 2: D≤ 0. Then using r<d 3 we estimate
Cr +D≥ [d3(1−ε)−εd] + [d4(1−ε)− 1−εd2]d3
=d7−ε(d +d3 +d5 +d7)> 0
for ε< min (d6, 1)/4.
For condition (4.16) we need to show (1−ε)d+Br> 0, whereB = (1−ε)d2−1
is the expression deﬁned in (d). Again we distinguish two cases.
Case 1: B >0. This implies d> 1 and ε< 1− 1/d2 < 1 and thus (1−ε)d> 0 as
well.
Case 2: B≤ 0. Then using r<d 3 and ε< 1/2 we estimate
(1−ε)d +Br≥ (1−ε)d +
[
(1−ε)d2− 1
)
]d3
∼ (1−ε)(1 +d4)−d2 > (1 +d4)/2−d2
∼ (1−d2)2≥ 0.
This concludes the proof of Lemma 4.32. □
The following result is a quantitative version of Proposition 4.21.
Proposition 4.33. For every a > 1 and γ > 0 there exists δ∈ (0,γ ) and
an i-convex shape χ(r) which agrees with S(r) =
√
1 +ar2 for r≥γ and satisﬁes
χ′(δ) = +∞ and 1 < χ(δ) < 1 +γ (see Figure 4.7). Moreover, the corresponding
hypersurface is J-convex for every complex structure J on Cn with‖J−i‖C2 ≤
c(a,n )γ12, where c(a,n ) is a constant depending only on a and the dimension n.
Proof. Let us recall that the required shape χ(r) in Proposition 4.21 is con-
structed by smoothing the maximum of four functions: S(r) =
√
1 +ar2, Q(r) =
a +br +cr2/2, L(r) = 1 + dr and a solution φ of Struwe’s equation (4.8). By
construction the function φ satisﬁes φ′ >d , and according to Remark 4.20 we can
choosec = (a + 1)/2 and b =γ(a− 1)/16<d< 1. Then Lemma 4.31 ensures that

90 4. SHAPES FOR i-CONVEX HYPERSURFACES
the modulus of convexity of the φ-part of the hypersurface satisﬁes
¯µ> d2
32 >γ 2 (a− 1)2
29 .
Now note that the hypotheses in Lemma 4.32 (a), (b) and (e) are identical with
those in Lemma 4.17 (a), (b) and (e). Hence in view of Remark 4.20, the S- , Q-,
andL-parts in the construction satisfy the bounds on the moduli of convexity given
by Lemma 4.32 (a), (b) and (e):
¯µ = (a− 1)/a,
¯µ≥ min
{
1− 1
c, b2
1−b2
}
≥ min
{a− 1
a + 1, (a− 1)2γ2
162− (a− 1)2γ2
}
,
¯µ≥ min{d6, 1}
4 ≥γ6 (a− 1)6
229 .
Thus for all parts we have µ≥ ¯µ/3≥caγ6, where ca is a constant depending only
on a. Now we apply Corollary 4.29 to smooth the maximum of the four functions.
By Proposition 3.41, the resulting shape hypersurface is then J-convex for every
complex structure J on Cn with‖J−i‖C2≤cn(caγ6)2. □
Similarly, one proves the following quantitative version of Proposition 4.27.
Proposition 4.34. Letχλ, λ∈ [−8δ, 1], be the family constructed in Proposi-
tion 4.27. Then all the level sets of these functions are J-convex for every complex
structureJ on Cn with‖J−i‖C2≤c(a,n )γ12, wherec(a,n ) is a constant depending
only on a and the dimension n.
Proof of Theorems 4.1 (iv) and 4.2 (iv). This follows from the estimates
in Propositions 4.33 and 4.34. □

5
Some Complex Analysis
In this chapter we collect some deﬁnitions and results from the theory of
functions of several complex variables. Mostly, we have restricted ourselves to
those facts that are directly relevant for this book, so this chapter presents by no
means an adequate exposition of the rich and beautiful subject of several com-
plex variables. For such expositions consult one of the many excellent books such
as [89, 103, 78, 116, 93, 160, 36, 60 ].
In particular, we review the notion of holomorphic convexity and its relation
with J-convexity (the Levi problem and its generalizations), Grauert’s Oka prin-
ciple and its applications, and the holomorphic ﬁlling problem for J-convex CR
manifolds. The one subject discussed in greater detail is real analytic approxima-
tion because it is important for the purposes of this book.
5.1. Holomorphic convexity
To a subsetK⊂V of a complex manifold we associate its holomorphic hull in
V :
ˆKV :={x∈V
⏐⏐|f(x)|≤ maxK|f| for all holomorphic functions f :V → C}.
Note that this notion depends on the manifold V . If U ⊂ V is an open subset
containing K then we have ˆKU ⊂ ˆKV . In the case V = Cn we can equivalently
replace holomorphic functions by polynomials in the deﬁnition and ˆKCn is also
called the polynomial hull. A subset with ˆKCn =K is called polynomially convex.
Example 5.1. (a) Let K⊂ Cn be a compact convex set. Then ˆKCn = K.
Indeed, for any point z /∈K there exists a complex linear function l : Cn→ C such
that Re (l(z))> max
w∈K
Re (l(w)). Hence,|el(z)|> max
w∈K
⏐⏐el(w)⏐⏐.
(b) Given holomorphic functionsf1,...,f N :V → C the setP =P (f1,...,f N)
:={|f1|≤ 1,..., |fN|≤ 1}⊂ V is called an analytic polyhedron if it is compact.
Clearly, for any analytic polyhedron P we have ˆPV =P .
(c) If C⊂V is a compact complex curve with boundary ∂C, then C⊂ ˆ∂CV .
Indeed, for any holomorphic function f : V → C the maximum principle yields
maxC|f|≤ max∂C|f|.
A complex manifold V is called holomorphically convex if ˆKV is compact for
all compact subsets K⊂V .
Example 5.2. (a) Any open convex subset Ω⊂ Cn is holomorphically convex.
Indeed, Ω can be exhausted by compact convex sets Ki⊂ IntKi+1, i = 1, 2,...
and we have Ki⊂ ˆKi
Ω⊂ ˆKi
Cn =Ki.
91

92 5. SOME COMPLEX ANALYSIS
(b) The interior of any analytic polyhedron is holomorphically convex. Indeed
IntP (f1,...,f N) can be exhausted by analytic polyhedra P
(
(1 + ε)f1,..., (1 +
ε)fN
)
, ε> 0.
(c) IfV is holomorphically convex andW⊂V is a properly embedded complex
submanifold, then W is also holomorphically convex.
Let us call a compact set K⊂V holomorphically convex if it can be presented
as an intersection of holomorphically convex open domains in V . In other words,
K is holomorphically convex if it has arbitrarily small holomorphically convex open
neighborhoods. 1
Note that if a compact set K⊂V satisﬁes ˆKV =K then it is holomorphically
convex. Indeed, for any neighborhood U of K a simple compactness argument
provides an analytic polyhedron P (f1,...,f N) which contains K and is contained
in U. The converse statement is not true, see Corollary 5.14 below.
Example 5.3. Suppose that a compact subset K ⊂ V admits a continuous
family of compact complex curves Cs⊂ V with ∂Cs⊂ K for all s∈ [0, 1], C0⊂
K, and C1⁄⊂ K. Then K is not holomorphically convex. Indeed, otherwise K
would have a holomorphically convex open neighborhood U ⊂ V with C1⁄⊂ U.
Set σ := sup{s∈ [0, 1]| Cs ⊂ U}∈ (0, 1). Then by Example 5.2 (c) we have⋃
s∈[0,σ)Cs⊂ ˆKU and hence ˆKU is not compact.
Polynomially convex sets can be characterized by an approximation property
(see e.g. [160]):
Theorem 5.4 (Oka–Weil). A holomorphically convex compact subset K⊂ Cn
is polynomially convex if and only if every holomorphic function on OpK can be
approximated uniformly on K by polynomials.
5.2. Relation to J-convexity
The notion of holomorphic convexity is intimately related to that ofJ-convexity.
We remind the reader that in this book “ J-convexity” without further speciﬁcation
always means “strict J-convexity”.
The following remark will be used repeatedly in the sequel to replace continuous
weaklyJ-convex functions by smooth strict ones.
Remark 5.5. SupposeV admits a (not necessarily exhausting) J-convex func-
tion (this holds e.g. for open subsets of Cn, or more generally of a Stein manifold).
Then any exhausting continuous weakly J-convex function φ : V → R can be
turned into an exhausting smooth (strictly)J-convex function. Indeed, we can ﬁrst
add a J-convex function to φ to make it (strictly) J-convex and then smooth it
using Proposition 3.10, keeping it exhausting. On general complex manifolds such
smooth approximations need not exist [ 59].
The relation between holomorphic convexity and J-convexity is given in the
following theorem.
Theorem 5.6. For an open set U⊂ Cn the following are equivalent:
(a) U is holomorphically convex;
1Warning: There are other deﬁnitions of holomorphic convexity for compact sets in the
literature, e.g. in [ 179].

5.2. RELATION TO J-CONVEXITY 93
(b) the continuous function − log dist∂U is weakly i-convex in U;
(c) U admits an exhausting i-convex function.
For the proof of Theorem 5.6 see e.g. [ 103]. Note that the implication ( b) =⇒
(c) follows directly from Remark 5.5. The implication (c) =⇒ (a) (and also (b) =⇒
(a)) was known as the Levi problem. It was solved by Oka in the case of C2, and
independently by Oka, Bremermann and Norguet for general Cn. Grauert proved
in [77] a generalization to complex manifolds (see Theorem 5.17 below), which can
be stated in slightly stronger form as follows [ 103, Theorem 5.2.10]:
Theorem 5.7. Suppose the complex manifold (V,J ) admits an exhausting J-
convex function φ :V → R. Then all sublevel sets of φ satisfy
ˆ{φ≤c}V ={φ≤c}.
In particular, (V,J ) is holomorphically convex.
The following two lemmas allow us to construct exhausting J-convex functions
on bounded domains. The ﬁrst one is elementary:
Lemma 5.8. LetV be a complex manifold which possesses a J-convex function,
and let W⊂V be a compact domain with smooth J-convex boundary. Then there
exists a J-convex function φ : W → R which is constant on ∂W . In particular,
IntW admits an exhausting J-convex function.
Proof. Take aJ-convex function ψ :V → R and choose a J-convex function
ρ deﬁned on a neighborhoodU⊃∂W which is constant on∂W . Let us assume that
φ|∂W =c andU′ :={c−ε≤ψ≤c}⊂ U. There exists a function σ : [c−ε,c ]→ R
such that σ◦ρ is J-convex on U′, σ(c−ε)< minφ|{ψ=c−ε} and σ(c)> maxφ|∂W .
Then the functionφ := smooth max(σ◦ρ,ψ ) onW has the required properties. □
For the proof of the following lemma see [ 93, Theorem 1.5.14].
Lemma 5.9. Let Σ be a locally closed weakly i-convex smooth hypersurface in
Cn. Let U⊂ Cn be an open tubular neighborhood of Σ such that U\ Σ =U+∪U−,
whereU−∪Σ has Σ as its weakly i-convex boundary. Then, for U suﬃciently small,
the function− log distΣ is weakly i-convex on U−.
Corollary 5.10. Any compact domain W⊂ Cn with smooth weakly i-convex
boundary admits an exhausting i-convex function on its interior.
Proof. By Lemma 5.9 there exists a collar neighborhood [ −ε, 0]×∂W of
0×∂W = ∂W such that the function φ :=− log dist∂W is weakly i-convex on
[−ε, 0)×∂W . Pick any i-convex function ψ : Cn→ R. Then ~φ := φ +ψ is i-
convex on [−ε, 0)×∂W . Pick c∈ R such that ψ +c >~φ on{−ε}× ∂W . Then
smooth max(~φ,ψ +c) deﬁnes an exhausting i-convex function on IntW . □
Remark 5.11. Lemma 5.9 also has the following global version (see e.g. [103]):
Let W ⊂ Cn be a compact domain with smooth weakly i-convex boundary ∂W .
Then the continuous function− log dist∂W is weakly i-convex on IntW .
Plurisubharmonic hull. In analogy with the holomorphic hull, one can
deﬁne the plurisubharmonic hull of a compact set K⊂V in a complex manifold as
ˆKpsh
V :={x∈V
⏐⏐φ(x)≤ maxKφ for all continuous
weaklyJ-convex functions φ :V → R}.

94 5. SOME COMPLEX ANALYSIS
K
U3 U2 U1 U0
ψ1
ψ
ψ2
ψ3
Figure 5.1. Construction of the function ψ.
Proposition 5.12. SupposeV admits an exhausting J-convex function. Then
ˆKpsh
V = ˆKV for every compact subset K⊂V .
Proof. The inclusion ˆKpsh
V ⊂ ˆKV is trivial because|f|2 is weaklyJ-convex for
every holomorphic function f. To show ˆKV ⊂ ˆKpsh
V takex /∈ ˆKpsh
V . By deﬁnition,
there exists a continuous weaklyJ-convex functionφ :V → R withφ(x)> maxKφ.
After adding a small multiple of an exhaustingJ-convex function and smoothing we
may assume that φ is exhausting, smooth and (strictly) J-convex. Pick a regular
valuec ofφ with maxKφ<c<φ (x). By Theorem 5.7, ˆKV ⊂ ˆ{φ≤c}V ={φ≤c}
does not contain x. □
The following proposition provides weakly J-convex deﬁning functions for sets
with ˆKpsh
V =K.
Proposition 5.13. Suppose (V,J ) admits an exhausting J-convex function.
Then a compact subset K⊂ V satisﬁes ˆKpsh
V = K if and only if there exists an
exhausting smooth weakly J-convex function ψ : V → R≥0 such that ψ−1(0) = K
and ψ is (strictly) J-convex outside K.
Proof. Existence of ψ clearly implies ˆKpsh
V = K. Conversely, suppose that
ˆKpsh
V = K. First note that for every open set U and compact set W with K⊂
U⊂W there exists an exhausting J-convex function φ :V → R with φ|K < 0 and
φ|W\U > 0. Indeed, by deﬁnition we ﬁnd for every x∈W⊂U a weakly J-convex
function φx :V → R with φ|K < 0 and φ(x)> 0. After adding a small exhausting
J-convex function we may assume that φx is exhausting and (strictly) J-convex.
Since φx > 0 on a neighborhood Nx of x and ﬁnite many such neighborhoods Nxi
coverW\U, a smoothing of max i{φxi} gives the desired function.
Using this, we inductively construct a sequence of relatively compact open
subsets V ⋑ U0⋑ U1⋑ U2⋑··· with⋂
kUk = K, and a sequence of exhausting
J-convex functions φk :V → R, k≥ 1, satisfying
φk| ¯Uk+1 < 0, φ k| ¯Uk−1\Uk > 0.
Pick a decreasing sequence of positive numbers εk→ 0 such that the ψk := εkφk
satisfy max∂Ukψk+1 < min∂Ukψk, see Figure 5.1.
Pick 0<ε< min ¯U0\U1ψ1 and set
ψ :=



0 on K,
max{ψk,ψk+1} on Uk\Uk+1,
max{ψ1,ε} on V\U1.

5.3. DEFINITIONS OF STEIN MANIFOLDS 95
Note that ψ is smooth along ∂Uk because max{ψk,ψk+1} =ψk = max{ψk,ψk−1}
there. Moreover, ψ≥ 0 and ψ−1(0) =K. By choosing the sequence εk to decrease
suﬃciently fast we can achieve thatψ(x)≤e−1/d(x,K), whered is the distance with
respect to some Riemannian metric, which implies smoothness of ψ at K. So a
smoothing of the max constructions yields the desired function. □
The following corollary illustrates the diﬀerence between holomorphic and poly-
nomial convexity.
Corollary 5.14. For a closed totally real submanifold L⊂ Cn the following
hold.
(a) L is holomorphically convex.
(b) If dimL =n it is not polynomially convex.
Proof. (a) By Proposition 2.15, the squared distance function dist 2
L is i-
convex on some neighborhood U of L, so by Theorem 5.7 ˆLU = L and L is holo-
morphically convex.
(b) is a special case of a theorem by Andreotti and Narasimham [ 8], according
to which polynomal convexity of L would imply the contradiction Hn(L; Z2) = 0.
Alternatively, this can be proved using symplectic geometry as follows. SupposeL is
polynomially convex. Let ψ : Cn→ R≥0 be the exhausting function with ψ−1(0) =
L provided by Proposition 5.13. After replacingψ nearL by smooth max(ψ,ε dist2
L)
for small ε> 0 we may assume that ψ is (strictly) i-convex. Moreover, we can use
Proposition 2.11 to make ψ completely exhausting. Then by Proposition 11.22
below the symplectic form −ddCψ is diﬀeomorphic to the standard form on Cn.
Now L is exact Lagrangian for −ddCψ, i.e., −dCφ|L ≡ 0. But this contradicts
Gromov’s theorem in [ 83] that there are no closed exact Lagrangian submanifolds
for the standard symplectic form on Cn. □
5.3. Deﬁnitions of Stein manifolds
There exist a number of equivalent deﬁnitions of a Stein manifold. We have
already encountered two of them.
Aﬃne deﬁnition. A complex manifold V is Stein if it admits a proper holo-
morphic embedding into some CN .
J-convex deﬁnition. A complex manifold V is Stein if it admits an exhaust-
ing J-convex function f :V → R.
The classical deﬁnition rests on the concept of holomorphic convexity.
Classical deﬁnition. A complex manifold V is Stein if it has the following 3
properties:
(i) V is holomorphically convex;
(ii) for every x∈ V there exist holomorphic functions f1,...,f n : V → C
which form a holomorphic coordinate system at x;
(iii) for any x⁄= y∈ V there exists a holomorphic function f : V → C with
f(x)⁄=f(y).2
Clearly, the aﬃne deﬁnition implies the other two (holomorphic convexity was
shown in Example 5.2). The classical deﬁnition immediately implies that every
compact subset K ⊂ V can be holomorphically embedded into some CN. The
implication “classical =⇒ aﬃne” is the content of
2In fact, properties (i) and (ii) imply (iii), and (i) and (iii) imply (ii), see [ 88, Section M].

96 5. SOME COMPLEX ANALYSIS
Theorem 5.15 (Bishop [ 18], Narasimhan [ 144]). A Stein manifold V in the
classical sense of complex dimension n admits a proper holomorphic embedding into
C2n+1.
Remark 5.16. A lot of research has gone into ﬁnding the smallestN such that
every n-dimensional Stein manifold embeds into CN. After intermediate work of
Forster, the optimal integer N = [3n/2] + 1 was ﬁnally established by Eliashberg-
Gromov [50] and Sch¨ urmann [166].
The implication “J-convex =⇒ classical” was proved by Grauert in 1958:
Theorem 5.17 (Grauert [77]). A complex manifold which admits an exhausting
J-convex function is Stein in the classical sense.
It is clear from any of the deﬁnitions that properly embedded complex subma-
nifolds of Stein manifolds are Stein. We will refer to them as Stein submanifolds .
Many results from Cn generalize to Stein manifolds. For example, the Oka–Weil
Theorem 5.4 generalizes to (see [ 103])
Theorem 5.18. A holomorphically convex compact subset K of a Stein mani-
fold V satisﬁes ˆKV =K if and only if every holomorphic function on OpK can be
approximated uniformly on K by holomorphic functions on V .
Remark 5.19. Corollary 5.29 below allows us to generalize Theorem 5.18 to
sections of any holomorphic vector bundle over a Stein manifold V .
5.4. Hartogs phenomena
An important new phenomenon in complex dimension n >1 is the existence
of open sets Ω⊂ Cn with the property that all holomorphic functions on Ω extend
to some larger set. The ﬁrst such example was described by Hartogs.
Example 5.20 (Hartogs). The domain Ω := IntB4(1)\B4(1/2)⊂ C2 has the
holomorphic hull ˆΩ = Int B4(1) (in particular, Ω is not holomorphically convex).
To see this, let f : Ω→ C be a holomorphic function. For ﬁxed z∈ C,|z|< 1, the
function w↦→f(z,w ) on the annulus (or disc) Az :={w∈ C
⏐⏐ 1/4−|z|2 <|w|2 <
1−|z|2} has a Laurent expansion
f(z,w ) =
∞∑
k=−∞
ak(z)wk.
The coeﬃcients ak(z) are given by
ak(z) = 1
2πi
∫
|ζ|=r
f(z,ζ )
ζk+1 dζ
for any r > 0 with 1 /4−| z|2 < r2 < 1−| z|2. In particular, ak(z) depends
holomorphically on z with|z| < 1. Since Az is a disc for |z| > 1/2, we have
ak(z) = 0 for k < 0 and |z| > 1/2, hence by unique continuation for all z with
|z| < 1. Thus the Laurent expansion deﬁnes a holomorphic extension of f to the
ball IntB4(1).
Generalizing this example, we have (see [ 103] for a simple proof)

5.4. HARTOGS PHENOMENA 97
y1
U ′
U
Σ
z
Dz
x1, z2, . . . , zn−1
w = zn
H
Figure 5.2. Holomorphic functions deﬁned near Σ extend holo-
morphically to the region U between Σ and the hyperplane H.
Theorem 5.21 (Hartogs). Let Ω be an open subset of Cn,n> 1, and K⊂ Ω be
compact with Ω\K connected. Then every holomorphic function on Ω\K extends
uniquely to a holomorphic function on Ω.
Remark 5.22. An open subset U ⊂ Cn is called a domain of holomorphy if
there is no larger unramiﬁed domain over Cn containingU to which all holomorphic
functions from U extend holomorphically. It turns out (see e.g. [ 103]) that U is a
domain of holomorphy if and only if it is holomorphically convex.
As preparation for a further generalization of Example 5.20, let us consider the
following model situation in Cn with coordinates z = (z1,...,z n−1) and w = zn.
Let Σ ⊂{ y1≥ 0}⊂ Cn be a geometrically convex hypersurface with boundary
∂Σ⊂H :={y1 = 0}, see Figure 5.2.
Denote by U the region between H and Σ and by U′ its projection to Cn−1 =
{w = 0}. Then for each z∈U′ the setDz :={w∈ C| (z,w )∈U} is biholomorphic
to the unit disc, ∂Dz⊂ Σ, and Dz⊂O p (Σ) for z near the point in ¯U′ wherey1 is
maximal. So the same reasoning as in Example 5.20 shows:
Every holomorphic function deﬁned on Op Σ extends holomorphically to U.
From this we easily derive the following classical extension result (see e.g. [ 89,
Section VII D, Corollary 5]).
Theorem 5.23. Let (V,J ) be a Stein domain of complex dimension n≥ 2 with
J-convex boundary ∂V . Then every holomorphic function Op (∂V )→ C extends
uniquely to a holomorphic function V → C.
Proof. Pick aJ-convex Morse functionφ with regular level set ∂V =φ−1(c).
Let f be a holomorphic function deﬁned on a neighborhood U of ∂V . Consider a
level set Σ = φ−1(b)⊂U, b<c .

98 5. SOME COMPLEX ANALYSIS
By Proposition 2.12, each point p∈ Σ has a neighborhood Vp⊂ U such that
Σ∩Vp is biholomorphic to a geometrically convex hypersurface Σ p in Cn. By the
preceding discussion, f can be extended to any region Up bounded by Σ p and a
hyperplane. Moreover, the proof of Proposition 2.12 shows that the curvature of
Σp and hence the size of the region Up can be uniformly bounded below in terms of
an upper bound on the second derivatives of φ and a lower bound on its gradient
and its modulus of J-convexity.
Performing this for all points on φ−1(b), we holomorphically extend f to{φ≥
a} for some a < b, where b−a is bounded below in terms of an upper bound on
the second derivatives of φ and a lower bound on its gradient and its modulus of
J-convexity on φ−1(b). Continuing this way, we can thus holomorphically extend
f to{φ > a}, where a is the highest critical value of φ. Now we perturb φ to
a J-convex function ψ = φ◦h , where h is a small diﬀeomorphism which equals
the identity on {φ≥ b} and maps all critical points of φ on level a to φ−1(a′)
for some a′ > a. So all critical points of φ on level a lie on the regular level set
ψ−1(a′). By the preceding argument applied to ψ we holomorphically extend f to
the set{ψ > a} containing all critical points of φ. Then we switch back to φ and
holomorphically extend f to the next lower critical level of φ, and so on until we
have extended f to all of V . □
Remark 5.24. Kohn and Rossi [ 114] prove the following generalization of
Theorem 5.23 (under the same assumptions on V ): Every function f : ∂V →
C satisfying the tangential Cauchy-Riemann equations extends to a holomorphic
function on V . Moreover, instead of J-convexity they only assume that the Levi
form has at least one positive eigenvalue at each point of ∂V . On the other hand,
some convexity assumption is clearly necessary: For any closed complex manifold
X, V = ¯D×X is a compact complex manifold with Levi-ﬂat boundary and the
function f(z,w ) = 1/z deﬁned near ∂V has no holomorphic extension to V .
Corollary 5.25. LetV be a Stein domain of complex dimension n≥ 2.
(a) Every holomorphic map f :Op (∂V )→W to a Stein manifold W extends
uniquely to a holomorphic map F :V →W .
(b) Every biholomorphism f :Op (∂V )→O p (∂W ), where W is a Stein do-
main, extends uniquely to a biholomorphism F :V →W .
Proof. For (a) pick a proper holomorphic embedding W ⊂ CN. By Theo-
rem 5.23,f extends uniquely to a holomorphic mapF :V → CN. Since F (Op (∂V ))
⊂ W and every connected component of V meets ∂V , unique continuation yields
F (V )⊂ W . For (b) simply apply (a) to f−1 :Op (∂W )→O p (∂V ) to ﬁnd an
inverse of F . □
5.5. Grauert’s Oka principle
We discuss in this section some consequences of Grauert’s Oka principle:
Theorem 5.26 (Grauert [ 76]). Let G be a complex Lie group and H⊂ G a
closed complex analytic subgroup. Let P → V be a holomorphic ﬁbration over a
Stein manifold V with structure group G and ﬁber G/H. Then any continuous
sections :V →P is homotopic to a holomorphic one.

5.5. GRAUERT’S OKA PRINCIPLE 99
Corollary 5.27 (Docquier-Grauert [ 38]). LetV be a Stein submanifold of a
Stein manifold W . Then there exists a neighborhood U of V in W and a holomor-
phic submersion U→V ﬁxed on V .
Proof. One can view W as a submanifold of Cn. The restriction to W of a
submersion deﬁned onOpV ⊂ Cn is automatically a submersion on the intersection
of this neighborhood with W if the neighborhood is chosen small enough. Hence,
it is suﬃcient to consider the case W = Cn. Consider the holomorphic vector
bundles A = TW|V = V× Cn, B = TV and C = A/B over V , the holomorphic
GL(n, C)-principal bundle E = Iso(B⊕C,A ) and its subbundle F→V consisting
of isomorphisms which restrict to the identity onB. The bundle F is also principal:
If dimV =k then the structure group of F is the subgroup of GLn(C) preserving
Ck ⊂ Cn. The bundle F admits a smooth section s : F → E. By Grauert’s
Theorem 5.26 the section s is homotopic to a holomorphic section, which can be
interpreted as a holomorphic ﬁberwise injective bundle homomorphism Φ : C→A
transverse to the subbundle TV ⊂ A. This yields a holomorphic map Φ from the
total space of the bundle C (which we will still denote by C) to Cn which sends a
vector X in the ﬁber Cp over a point p∈ V to p + Φ(X)∈ Cn. The diﬀerential
of Φ is an isomorphism along the zero section V ⊂ C, so by the implicit function
theorem Φ is a biholomorphism between neighborhoods of the zero section in C
and of V in Cn. The bundle projection π :C→V carried by this biholomorphism
toOpV ⊂ Cn has the required properties. □
Remark 5.28. Note that the previous argument shows, in particular, that
if V ⊂ W is a Stein submanifold of a Stein manifold W then the holomorphic
bundle N = TW|V/TV admits a holomorphic homomorphism N→ TW|V which
is transverse to the subbundle TV ⊂TW|V .
Another useful consequence is the following
Corollary 5.29. Every holomorphic vector bundle E→V over a Stein ma-
nifold V is holomorphically isomorphic to a subbundle, as well as to a quotient
bundle, of the trivial vector bundle V× CN, for suﬃciently large N.
Proof. Consider the holomorphic ﬁbrationP→V of injective complex bundle
mapsE→ CN. Its ﬁber is the complex Stiefel manifold GL(N; C)/GL(N−k, C) of
k-frames in CN, wherek is the rank of E, and its structure group is GL(N, C). For
large N the bundle P has a continuous section, which by Grauert’s Theorem 5.26
is homotopic to a holomorphic section. The resulting injective holomorphic bundle
homomorphism E → V × CN maps E onto a subundle of V × CN. Similarly,
Grauert’s Theorem yields a surjective holomorphic bundle homomorphism V ×
CN→E, which exhibits E as a quotient bundle of V× CN. □
Proposition 5.30. Let K ⊂ V be a compact subset with smooth J-convex
boundary in a Stein manifold V . Then for every holomorphic vector bundle π :
E→ V there exists a compact domain W ⊂ E, contained in an arbitrarily small
neighborhood ofK inE, with smoothJ-convex boundary such thatW∩V =π(W ) =
K (where we identify V with the zero section in E).
Proof. We use Corollary 5.29 to holomorphically embed E as a subbundle in
V× CN. Pick a J-convex function ψ : K→ R with K ={ψ≤ 0} and regular
level set ∂K ={ψ = 0}. For each C > 0 the compact domain W′ :={(x,z )∈

100 5. SOME COMPLEX ANALYSIS
K× CN|ψ(x)+C|z|2≤ 0}⊂ V× CN has smoothJ-convex boundary and satisﬁes
W′∩V = π1(W′) = K, where π1 : V× CN→ V is the projection onto the ﬁrst
factor. Moreover, W′ is arbitrarily close to K for large C. Hence W :=E∩W′ is
the desired domain in E. □
Corollary 5.27 together with Proposition 5.30 implies
Corollary 5.31. For any Stein submanifold V ⊂ CN, any compact domain
K⊂V with smooth J-convex boundary and any neighborhood U of K in CN there
exists an arbitrarily small compact domain W ⊂ U ⊂ CN with smooth J-convex
boundary such that W∩V =π(W ) =K. Here π is a holomorphic submersion from
a neighborhood of V in CN onto V as constructed in Corollary 5.27.
In particular, K admits arbitrarily small neighborhoods in CN with smooth J-
convex boundary.
We also get as a corollary the following analogue of Corollary 5.10 for domains
with weakly J-convex boundary in an arbitrary Stein manifold.
Corollary 5.32. LetV be a Stein manifold. Then any compact domain W⊂
V with smooth weakly J-convex boundary admits an exhausting J-convex function
on its interior.
Proof. Let us view V as a submanifold of CN. Hence TV is a holomorphic
subbundle of the trivial bundle V× CN = T (CN)|V . Denote by N the quotient
bundle T (CN)|V/TV . According to Remark 5.28, the bundle N can be realized as
a holomorphic subbundle of the trivial bundle V× CN transverse to TV .
Arguing as in the proof of Corollary 5.27, we construct a biholomorphism Φ
of a neighborhood Ω of V in N onto a neighborhood Ω of V in CN. Denote by
Σ the total space of the bundle N|∂W . Note that Σ is a weakly pseudo-convex
hypersurface in N. Then Σ := Φ(Σ∩ Ω) is a weakly i-convex hypersurface in
Ω. Hence, by Lemma 5.9 the function φ :=− log distΣ is weakly i-convex on the
convex side U− of a suﬃciently small tubular neighborhood U of Σ in Ω. Then
the restriction φ|W∩U− is weakly J-convex and tends to inﬁnity near ∂W . As in
the proof of Corollary 5.10 we now combine this function with an i-convex function
V → R to obtain an exhausting i-convex function on IntW . □
Remark 5.33. Remark 2.19 provides an alternative proof of Proposition 5.30.
It uses some basic facts about curvatures of holomorphic vector bundles, see e.g. [80].
Pick an exhausting J-convex function φ : V → R. Then eφ( , )st deﬁnes a Her-
mitian metric on the trivial line bundle V× C with negative curvature form−∂ ¯∂φ.
The product metric on the trivial vector bundle V × CN then also has negative
curvature, and so does every subbundle of V× CN. Thus, by Corollary 5.29, the
bundle π :E→V carries a Hermitian metric || of negative curvature. According
to Remark 2.19, the function s(e) =|e|2 onE isJ-convex outside the zero section.
Now let ψ : K→ R be a J-convex function such that K ={ψ≤ 0} and dψ⁄= 0
along ∂K. Then the function Φ := Cs +ψ◦π : π−1(K)→ R is J-convex and
W :={Φ≤ 0}⊂ E is the desired domain for large C >0.
Let us remark that Grauert’s Oka principle was signiﬁcantly generalized by
M. Gromov in [ 85] and then further extended by F. Forstneriˇ c, F. L´ arusson and
others, see [61] for a survey of the subject.

5.6. COHERENT ANALYTIC SHEAVES ON STEIN MANIFOLDS 101
5.6. Coherent analytic sheaves on Stein manifolds
Two fundamental results about Stein manifolds are Cartan’s Theorems A and
B. They are formulated in the language of sheaves, see [27, 36] for the relevant deﬁ-
nitions and properties. LetV be a complex manifold andO the sheaf of holomorphic
functions on V . For a nonnegative integer p, let Op be the sheaf of holomorphic
maps to Cp. An analytic sheaf is a sheaf of O-modules. A sheaf homomorphism
f :F→G between analytic sheaves is called analytic if it is anO-module homomor-
phism. An analytic sheaf F is called coherent if everyx∈V has a neighborhood U
such thatFU equals the cokernel of an analytic sheaf homomorphismf :Op
U→O q
U,
for some nonnegative integers p,q .
Oka’s coherence theorem [154] states that a subsheaf F ofOp is coherent if
and only if it is locally ﬁnitely generated, i.e., for every point x∈V there exists a
neighborhood U of x and ﬁnitely many sections fi ofFU that generate Fy as an
Oy-module for every y∈U.
Example 5.34. (1) Let W⊂V be a properly embedded complex submanifold
of a complex manifold V and d≥ 0 an integer. For an open subset U ⊂ V , let
IU be the ideal of holomorphic functions on U whosed-jet vanishes at all points of
U∩W . This deﬁnes an analytic sheaf I on V . We claim that I is coherent. To
see this, let x∈ V . If x /∈ W we ﬁnd a neighborhood U of x with U∩W = ∅
(since W⊂V is closed), hence IU =OU. If x∈W we ﬁnd a small open polydisc
U∼= Int
(
B2(1)×···× B2(1)
)
⊂V aroundx with complex coordinates (z1,...,z n)
in which W∩U ={z1 =··· = zk = 0}. Then the ideal IU is generated as an
OU-module by the monomials of degree (d+1) in z1,...,z k, so by Oka’s Coherence
Theorem [154],I is coherent.
(2) In the situation of (1), ﬁx in addition an integere≥d and a properly embed-
ded complex submanifold Z⊂W . For U⊂V letJU be the ideal of holomorphic
functions onU whosed-jet vanishes at all points ofU∩W and whosee-jet vanishes at
points ofU∩Z. In complex coordinates as above in which Z ={z1 =··· =z𝓁 = 0},
𝓁≥k, the idealJU is generated as anOU-module by the monomials of degree (e+1)
in z1,...,z 𝓁 which have degree at least ( d + 1) in z1,...,z k. So again, by Oka’s
theorem, this deﬁnes a coherent analytic sheaf J on V .
Remark 5.35. The coherence of the sheavesI andJ in the preceding example
can also be proved without Oka’s theorem as follows. As above, let ( z1,...,z n) be
complex coordinates on a polydisc U in which W∩U ={z1 =··· =zk = 0}. We
claim that every f∈I U has a unique representation
f(z) =
∑
I
fI(z)zI,
where the summation is over all I = (i1,...,i k) with i1 +··· +ik = d + 1 and
zI =zi1
1 ...z ik
k , and the coeﬃcient fI is a holomorphic function of z𝓁,...,z n, where
1≤𝓁≤k is the largest integer with i𝓁⁄= 0.
We ﬁrst prove the claim for d = 0 by induction over k. The case k = 1 is
clear, so let k >1. The function ( zk,...,z n)↦→ f(0,..., 0,zk,...,z n) vanishes at
zk = 0, thus (as in the case k = 1) it can be uniquely written as zkfk(zk,...,z n)
with a holomorphic function fk. Since the function ( z1,...,z n)↦→f(z1,...,z n)−
zkfk(zk,...,z n) vanishes at z1 =··· =zk−1 = 0, by induction hypothesis it can be
uniquely written asz1f1(z1,...,z n)+··· +zk−1fk−1(zk−1,...,z n) with holomorphic

102 5. SOME COMPLEX ANALYSIS
functionsf1,...,f k−1. This proves the cased = 0. The general cased> 0 follows by
induction overd: Using the case d = 0, we writef(z) uniquely asz1f1(z1,...,z n)+
··· +zkfk(zk,...,z n). Now note that the functions f1,...,f k must vanish to order
d− 1 atz1 =··· =zk = 0 and use the induction hypothesis. This proves the claim.
By the claim, IU is the direct sum of copies of the rings F𝓁
U of holomorphic
functions of z𝓁,...,z n for 1≤𝓁≤k. Since F𝓁
U is isomorphic to the cokernel of the
homomorphismO𝓁−1
U →O U, (f1,...,f 𝓁−1)↦→ z1f1 +··· +z𝓁−1f𝓁−1, this proves
coherence ofI. For coherence ofJ , note thatf∈J U has a representation as above
with coeﬃcients fI(z) vanishing to order e along{z1 =··· = z𝓁 = 0} and apply
the same argument to represent fI as a sum over monomials.
Now we can state Cartan’s Theorems A and B. Denote by Hq(V,F) the co-
homology with coeﬃcients in the sheaf F. In particular, H0(V,F) is the space of
sections inF. Every subsheaf G⊂F induces a long exact sequence
···→ Hq(V,G)→Hq(V,F)→Hq(V,F/G)→Hq+1(V,G)→··· .
Theorem 5.36 (Cartan’s Theorems A and B [ 27]). LetV be a Stein manifold
andF a coherent analytic sheaf on V . Then
(A) for every x∈V , H0(V,F) generatesFx as anOx-module;
(B) Hq(V,F) ={0} for all q >0.
In Section 5.8 we will use the following two consequences of Cartan’s Theorem
B.
Corollary 5.37. LetZ⊂W⊂V be Stein submanifolds of a Stein manifold
V and let d be a nonnegative integer. Then for every holomorphic function f :
W∪O p (Z)→ C there exists a holomorphic function F : V → C with F|W = f
whose d-jet coincides with that of f at points of Z.
Proof. LetI be the analytic sheaf of holomorphic functions on V that vanish
on W and whose d-jet vanishes at points of Z. By Example 5.34, I is coherent.
Thus by Cartan’s Theorem B, H1(V,I) = 0, so by the long exact sequence the
homomorphism H0(V,O)→ H0(V,O/I) is surjective. Now Ox/Ix ={0} for x /∈
W , and for x∈ W\Z elements ofOx/Ix are germs of holomorphic functions on
W and for x∈ Z elements ofOx/Ix are d-jets of germs of holomorphic functions
alongZ. So f deﬁnes a section inO/I and we conclude that f is the restriction of
a section F inO. □
Corollary 5.38. Every Stein submanifold W of a Stein manifold V is the
common zero set of a ﬁnite number (at most (dimCV + 1)(codim CW + 1)) of
holomorphic functions fi : V → C such that for all x ∈ W the diﬀerentials
dxfi :TxV → C satisfy⋂
i kerdxfi =TxW .
Proof. The argument is given in [28]. It uses some basic properties of analytic
subvarieties, see e.g. [ 80, 36]. An analytic subvariety of a complex manifold V is
a closed subset Z ⊂ V that is locally the zero set of ﬁnitely many holomorphic
functions. Z is a stratiﬁed space Z = Z0∪···∪ Zk, where Zi is a (non-closed)
complex submanifold of dimension i. Deﬁne the (complex) dimension of Z as the
dimension k of the top stratum. If Z′⊂ Z are analytic subvarieties of the same
dimension, then Z′ contains a connected component of the top stratum Zk of Z.

5.7. REAL ANALYTIC MANIFOLDS 103
Now let W ⊂ V be a Stein submanifold of a Stein manifold V . Pick a set
S1⊂ V containing one point on each connected component of V\W . Since S1
is discrete, W∪S1 is a Stein submanifold of V . By Corollary 5.37, there exists a
holomorphic function f1 :V → C which equals 0 on W and 1 on S1. The zero set
W1 :={f1 = 0} is an analytic subvariety of V , containing W , such that W1\W
has dimension≤n− 1, where n = dimCV . Pick a set S2⊂W1\W containing one
point on each connected component of the top stratum of W1 that is not contained
in W . Since each compact set meets only ﬁnitely many components of W1, the set
S2 is discrete, soW∪S2 is a Stein submanifold ofV . By Corollary 5.37, there exists
a holomorphic function f2 : V → C which equals 0 on W and 1 on S2. The zero
set W2 :={f1 = f2 = 0} is an analytic subvariety of V , containing W , such that
W2\W has dimension≤n−2. Continuing this way, we ﬁnd holomorphic functions
f1,...,f n+1 :V → C such thatW⊂Wn+1 :={f1 =··· =fn+1 = 0} andWn+1\W
has dimension≤− 1. Thus Wn+1\W = ∅ and W ={f1 =··· =fn+1 = 0}.
Finally, we will add more functions to arrange the condition ⋂
i kerdxfi =
TxW for all x∈ W . Pick a (discrete) set S1⊂ V containing one point on each
connected component ofW . By Corollary 5.37 we ﬁnd holomorphic functions on V
which vanish on W with prescribed complex derivatives at points of S1. Choosing
these derivatives to be linearly independent, we thus ﬁnd holomorphic functions
g1,...,g k :V → C which vanish on W such that⋂
i kerdxgi =TxW for all x∈S1.
Now W1 :={x∈ W|⋂
i kerdxfi⁄= TxW} is an analytic subvariety of W and we
continue inductively as above until the dimension becomes negative. □
5.7. Real analytic manifolds
In order to holomorphically attach handles, we need to approximate smooth
objects by real analytic ones. In this section we collect the relevant results.
A functionf :U→ Rm on an open domainU⊂ Rn is called real analytic if it is
locally near each point given by a convergent power series. A real analytic manifold
is a manifold with an atlas such that all transition functions are real analytic. A
submanifold is called real analytic if it is locally the transverse zero set of a real
analytic function. Real analytic bundles and sections are deﬁned in the obvious
way.
Remark 5.39. As a special case of the Cauchy-Kovalevskaya theorem (see
e.g. [58]), the solution of an ordinary diﬀerential equation with real analytic coef-
ﬁcients depends real analytically on all parameters.
Complexiﬁcation. There is a natural functor, called complexiﬁcation, from
the real analytic to the holomorphic category. First note that any real analytic
function f : U → Cm, deﬁned on an open domain U ⊂ Rn, can be uniquely
extended to a holomorphic function f C :U C→ Cm on some open domain U C⊂ Cn
with U C∩ Rn =U. More generally, we have
Lemma 5.40. LetV,W be complex manifolds and M⊂V a real analytic totally
real submanifold with dimRM = dimCV . Then any real analytic map f :M→W
extends uniquely to a holomorphic map f C :OpM → W on a suﬃciently small
neighborhood ofM in V .
If dimCV = dimCW andf is a real analytic diﬀeomorphism ofM onto a totally
real submanifoldN⊂W , then the extension f C is a biholomorphism betweenOpM
andOpN.

104 5. SOME COMPLEX ANALYSIS
Proof. Consider a point p∈ M. Pick a real analytic coordinate chart φ :
Rn ⊃ U1 → M and a holomorphic coordinate chart ψ : Cn ⊃ U2 → V , both
mapping 0 to p. Complexify ψ−1◦φ to a biholomorphic map ~Φ : Cn⊃U C
1 → Cn.
Then Φ =ψ◦~Φ : Cn⊃U→V is a holomorphic coordinate chart mapping U∩ Rn
to M.
Pick a holomorphic coordinate chart Ψ : Cm⊃ U′→ W near f(p) and com-
plexify Ψ−1◦f◦ Φ : U∩ Rn → Cm to a holomorphic map ~F : U → Cm. So
F = Ψ◦ ~F◦ Φ−1 is a holomorphic extension of f to a neighborhood of p in V .
By uniqueness of holomorphic extensions, this extension does not depend on the
chosen coordinate charts on V and W , and extensions around diﬀerent points of
M ﬁt together to the desired holomorphic extension of f.
The ﬁnal statement follows from the implicit function theorem and the observa-
tion that the complexiﬁcation of a real isomorphism is a complex isomorphism. □
The following is the fundamental result on complexiﬁcations of real analytic
manifolds.
Theorem 5.41 (Bruhat–Whitney [ 25]). Any real analytic manifold M has a
complexiﬁcation, i.e., a complex manifold M C with dimCM C = dimRM which con-
tains M as a real analytic totally real submanifold. The germ of a complexiﬁcation
M C is unique in the following sense: If V,W are complex manifolds, containing M
as real analytic and totally real submanifolds, with dimCV = dimCW = dimRM,
then some neighborhoods of M in V and W are biholomorphic.
Here is a sketch of the proof, see [ 25] for details. Pick a locally ﬁnite covering
ofM by countably many real analytic coordinate charts φi : Rn⊃Ui→M, so the
transition functions
φij :=φ−1
j ◦φi :Uij :=φ−1
i
(
φi(Ui)∩φj(Uj)
)
→Uji
are real analytic diﬀeomorphisms. Now construct open subsets U C
i ⊂ Cn with
U C
i ∩ Rn = Ui and U C
ij ⊂ U C
i with U C
ij∩ Rn = Uij such that the φij extend to
biholomorphic maps φC
ij :U C
ij→U C
ji satisfying the following cocycle conditions:
(i) φC
ji = (φC
ij)−1 and φC
ii = Id on U C
ii =U C
i ;
(ii) φC
ij maps U C
ijk =U C
ij∩U C
ik biholomorphically onto U C
jik and φC
jk◦φC
ij =
φC
ik :U C
ijk→U C
kij.
Deﬁne M C as the quotient of the disjoint union ∐
iU C
i by the equivalence relation
zi∼ zj if and only if zi∈ U C
ij and zj = φC
ij(zi)∈ U C
ji. (This is an equivalence
relation because of the cocycle conditions). The inclusions U C
i ↪→ ∐
jU C
j induce
coordinate charts U C
i ↪→ M C with biholomorphic transition functions. A careful
choice of the open sets U C
i and U C
ij ensures that M C is Hausdorﬀ. Finally, the
uniqueness statement in Theorem 5.41 follows from Lemma 5.40.
Note that as a real manifold, a (suﬃciently small) complexiﬁcation M C is dif-
feomorphic to the tangent bundle TM .
Complexiﬁcation has the obvious functorial properties. For example, if N⊂M
is a real analytic submanifold of a real analytic manifold M, then the (suﬃciently
small) complexiﬁcation N C is a complex submanifold of M C.
The crucial observation, due to Grauert [ 77], is that complexiﬁcations of real
analytic manifolds are in fact Stein.

5.7. REAL ANALYTIC MANIFOLDS 105
Proposition 5.42. Let M C be a complexiﬁcation of a real analytic manifold
M. Then M possesses arbitrarily small neighborhoods in M C which are Stein.
Proof. By Proposition 2.15, M possesses arbitrary small neighborhoods with
exhausting J-convex functions. By Grauert’s Theorem 5.17, these neighborhoods
are Stein. □
A complexiﬁcation M C which is Stein is called a Grauert tube of M. Now
the basic results about real analytic manifolds follow via complexiﬁcation from
corresponding results about Stein manifolds.
Corollary 5.43. Every real analytic manifold admits a proper real analytic
embedding into some RN.
Proof. By Theorem 5.15, a Grauert tube M C of M embeds properly holo-
morphically into some CN. Then restrict this embedding to M. □
Corollary 5.44. LetP⊂N⊂M be properly embedded real analytic subma-
nifolds of a real analytic manifold M and let d be a nonnegative integer. Then for
every real analytic function f :N∪Op (P )→ R there exists a real analytic function
F :M→ R with F|N =f whose d-jet coincides with that of f at points of P .
Proof. Let M C be a Grauert tube of M. After possibly shrinking N C and
M C, we may assume that a complexiﬁcations are properly embedded complex sub-
manifold P C ⊂ N C ⊂ M C, and f complexiﬁes to a holomorphic function f C :
N C∪O p (P C)→ C. Corollary 5.37 provides a holomorphic function G :M C→ C
with GC|N C = f C and whose d-jet agrees with that of f C at points of P C. Then
the restriction of the real part of G to M is the desired function F . □
Corollary 5.45. Every properly embedded real analytic submanifold N of
a real analytic manifold M is the common zero set of a ﬁnite number (at most
2(dimRM + 1)(codimRN + 1)) of real analytic functions fi :M→ R such that for
all x∈N the diﬀerentials dxfi :TxM→ C satisfy⋂
i kerdxfi =TxN.
Proof. Complexify N to a properly embedded submanifold N C⊂ M C of a
Grauert tube M C. By Corollary 5.38, N C is the zero set of at most (dim RM +
1)(codimRN + 1) holomorphic functions Fi : M C→ C satisfying the diﬀerential
condition. The restrictions of Re Fi and Im Fi to M yield the desired functions
fi. □
Remark 5.46. H. Cartan [ 28] takes a slightly diﬀerent route to prove Corol-
laries 5.44 and 5.45: Deﬁne coherent analytic sheaves on real analytic manifolds
analogously to the complex analytic case. Cartan proves that for every coherent
analytic sheafF onM, there exists a coherent analytic sheafF C on a complexiﬁca-
tionM C such thatF C|M =F⊗ C. From this he deduces the analogues of theorems
A and B in the real analytic category, which imply the corollaries as in the complex
analytic case.
We conclude this section with the following extension of Lemma 5.40 to the
non-totally real case that will be needed in Chapter 16.
Corollary 5.47. LetU,V,W be complex manifolds andM⊂V a real analytic
totally real submanifold with dimRM = dim CV . Then any real analytic map f :
U×M→ W whose restriction to U×m is holomorphic for all m∈ M extends
uniquely to a holomorphic map f C :U×V ⊃O p (U×M)→W .

106 5. SOME COMPLEX ANALYSIS
Proof. Arguing as in the proof of Lemma 5.40, it suﬃces to consider the case
of the open unit ballsU⊂ Ck,V ⊂ C𝓁,W⊂ Cn andM =V∩R𝓁. Then U is foliated
by the totally real balls Ut =U∩{ Imu =t},t∈U∩ Rk. For each t, the restriction
off to the totally real subspaceUt×M⊂ (Rk +it)×R𝓁⊂ Ck×C𝓁 extends uniquely
to a holomorphic map f C
t : Zt→ W on a neighborhood Zt of Ut×M in U×V .
Form∈M consider the two holomorphic maps f, fC
t :Zt∩ (U×m)→W . Since
they agree on the half-dimensional totally real subspace Ut×m⊂ Zt∩ (U×m),
unique continuation yields f = f C
t on Zt∩ (U×m) for all m, and thus f = f C
t
on Zt. Again by unique continuation, the extensions f C
t :Zt→W ﬁt together for
diﬀerentt to the desired extension f C. □
5.8. Real analytic approximations
Corollary 5.43 combined with a theorem of Whitney implies that every Ck-
function on a real analytic manifold M can be Ck-approximated by real analytic
functions. To state the result, equip M with a metric and connection so that we
can speak of k-th (covariant) derivatives of functions on M and their norms. We
denote by Dkf the vector of derivatives up to order k of a function f :M→ R.
Proposition 5.48. Letf :M→ R be a Ck-function on a real analytic mani-
fold. Then for every positive continuous function h : M→ R+ there exists a real
analytic function g :M→ R such that|Dkg(x)−Dkf(x)|<h (x) for all x∈M.
Proof. EmbedM real analytically into some RN. Extend f to a Ck-function
F : RN → R and h to a continuous function H : RN → R+. By a theorem of
Whitney [189, Lemma 6], there exists a real analytic function G : RN→ R such
that|DkG(x)−DkF (x)|< H(x) for all x∈ RN. Let g be the restriction of G to
M. □
Proposition 5.48 clearly generalizes to sections in real analytic ﬁber bundles
E→ M. For this, view the total space of the bundle as a real analytic manifold
and note that the image of a map M→E that is suﬃciently C1-close to a section
is again the graph of a section. Thus we have
Corollary 5.49. Letf :M→E be aCk-section of a real analytic ﬁber bundle
E → M over a real analytic manifold M. Then for every positive continuous
function h : M → R+ there exists a real analytic section g : M → E such that
|Dkg(x)−Dkf(x)|<h (x) for all x∈M.
Example 5.50. By Corollary 5.49, every Riemannian metric on a real analytic
manifold can be Ck-approximated by a real analytic metric. By Remark 5.39, the
exponential map of a real analytic metric is real analytic. Now the standard proof
yields real analytic tubular resp. collar neighborhoods of compact real analytic
submanifolds resp. boundaries. In particular, this allows us to extend any compact
real analytic manifold with boundary to a slightly larger open real analytic manifold.
Corollary 5.49 provides a rather general approximation result. On the other
hand, Corollary 5.44 shows that every real analytic function on a properly embedded
real analytic submanifoldN of a real analytic manifoldM can be extended to a real
analytic function on M, with prescribed d-jet along a real analytic submanifold P .
It is the goal of this section to combine the approximation and extension results.
We begin by introducing some notation. Consider a real vector bundle E→N
and ﬁx an integer d≥ 0. The d-jet bundle of E is the bundle JdE→ N whose

5.8. REAL ANALYTIC APPROXIMATIONS 107
ﬁber at x∈N consists of all polynomials of degree d on Ex. Thus a Ck-section of
JdE is a Ck-function F :E→ R whose restriction to each ﬁber Ex is polynomial
of degreed. Note that J0E =N andJ1E =E∗. By taking the Taylor polynomials
of degree d on the ﬁbers, every Ck+d-functionf :E→ R induces a Ck-sectionJdf
ofJdE which we call the ﬁberwised-jet of f. Note that for d≤e we have a natural
projection JeE→ JdE. Note also that if the bundle E is real analytic then so is
JdE.
Lemma 5.51. Consider a real analytic vector bundle E→N, integers k≥d≥
0, and a continuous function h : E→ R+. Let f : E→ R be a smooth function
whose ﬁberwise d-jet Jdf is real analytic. Then there exists a smooth function
g : E→ R and arbitrarily small open neighborhoods U ⊂ V of N in E with the
following properties:
(i) jdg =jdf along N;
(ii)|Dkg(x)−Dkf(x)|<h (x) for all x∈E;
(iii) g is real analytic on U and g =f outside V .
Proof. Consider the real analytic bundle Jk,dE→ N whose ﬁber at x∈ N
consists of all sums of monomials on Ex of degrees between d + 1 and k. Let
Jk,df =Jkf =Jdf be the section of Jk,dE deﬁned by f. By Corollary 5.49 there
exists a real analytic section F ofJk,dE with|DkF (x)−DkJk,df(x)|<h (x) for all
x∈N. So G :=Jdf +F :E→ R is a real analytic function with JdG =Jdf and
|DkG(x)−Dkf(x)|<h (x) for all x∈N. Since the estimate continues to hold on a
neighborhood of N inE, we can interpolate G tof outside a smaller neighborhood
to obtain the desired function g. □
Next consider a properly embedded real analytic submanifold N of a real ana-
lytic manifold M. Pick a real analytic Riemannian metric on M. Its exponential
map yields a real analytic diﬀeomorphism Φ between a neighborhood of the zero
section in the normal bundle E→ N and a neighborhood of N in M. We deﬁne
the normal d-jet Jdf along N of a function f : M→ R as the ﬁberwise d-jet of
f◦ Φ. Replacing real-valued functions by sections in a bundle, Lemma 5.51 thus
yields
Corollary 5.52. Consider a real analytic ﬁber bundle E→ M, a properly
embedded real analytic submanifold N⊂M, integers k≥d≥ 0, and a continuous
function h : M → R+. Let f : M → E be a smooth section whose normal d-jet
Jdf along N is real analytic. Then there exists a smooth section g : M → E
and arbitrarily small open neighborhoods U ⊂ V of N in M with the following
properties:
(i) jdg =jdf along N;
(ii)|Dkg(x)−Dkf(x)|<h (x) for all x∈M;
(iii) g is real analytic on U and g =f outside V .
Theorem 5.53. Consider a real analytic ﬁber bundle E → M, a properly
embedded real analytic submanifold N⊂M, integers k≥d≥ 0, and a continuous
function h :M→ R+. Let f :M→E be a smooth section whose normal d-jet Jdf
along N is real analytic. Then there exists a real analytic section F :M→E with
the following properties:
(i) jdF =jdf along N;
(ii)|DkF (x)−Dkf(x)|<h (x) for all x∈M.

108 5. SOME COMPLEX ANALYSIS
Proof. Step 1. As before, it suﬃces to consider the case of a real valued
function f : M→ R. After Ck-approximating f by a smooth function, ﬁxing its
normal d-jet along N, we may assume that f is smooth. After applying Corol-
lary 5.52, we may assume that f is real analytic in a neighborhood of N.
Pick any 𝓁≥ k≥ d. By Corollary 5.44 there exists a real analytic function
H :M→ R whose 𝓁-jet coincides with that of f at points of N. Then g :=f−H
vanishes to order𝓁 alongN. Suppose that we ﬁnd a real analytic sectionG :M→ R
that vanishes to order d along N and satisﬁes |DkG(x)−Dkg(x)| < h(x) for all
x∈ M. Then the real analytic function F := G +H : M → R is the desired
approximation f: Its normal d-jet along N satisﬁes JdF = JdH = Jdf, and
|DkF−Dkf| =|DkG +DkH−Dkf| =|DkG−Dkg|<h on M.
Step 2. By Step 1 it suﬃces to prove the theorem under the additional
hypothesis that f : M → R vanishes to order 𝓁 := 2d +k + 1 along N. By
Corollary 5.45, there exist real analytic functions f1,...,f m : M → R such that
N ={φ1 =··· = φm = 0} and ⋂
i kerdxfi = TxN for all x∈ N. Then φ :=
φ2
1 +··· +φ2
m :M→ R is real analytic and N =φ−1(0). Moreover, the Hessian of
φ at x∈N is positive deﬁnite in directions transverse to N, so φ≥ dist2
N for the
distance from N with respect to some Riemannian metric on M. Now note that in
a neighborhood of each point p∈ N we have an estimate |f(x)|≤ Cpdist(M,x )𝓁
and hence|f(x)||φ(x)|−d≤Cpdist(M,x )𝓁−2d =Cpdist(M,x )k+1. This shows that
g := fφ−d deﬁnes a Ck-function on M. By Proposition 5.48 there exists a real
analytic function G : M→ R such that|DkG−Dkg| < h/(1 +φd) on M. Then
the real analytic function F := Gφd : M→ R satisﬁes|DkF−Dkf| < hφd/(1 +
φd) < hon M and vanishes to order d along N, so F is the desired real analytic
approximation. □
Theorem 5.53 also has a version with parameters.
Corollary 5.54. Consider a real analytic ﬁber bundle E→M, a real analytic
manifold T with real analytic boundary, and a continuous family of functions ht :
M→ R+, t∈T . Let ft :M→E, t∈T , be a Ck-family of Ck-sections. Suppose
that the ft are real analytic for t∈ ∂T and depend real analytically on t∈ ∂T .
Then there exists a family of real analytic sections Ft : M → E, depending real
analytically on t∈T , with the following properties:
(i) Ft =ft for t∈∂T ;
(ii)|DkFt(x)−Dkft(x)|<h t(x) for all (t,x )∈T×M.
Proof. By Example 5.50, we can include T in a larger open real analytic
manifold ~T . Extend ft to a Ck-family ~ft over ~T and view ~ft as a Ck-section in
the bundle E→ ~T×M. Now apply Theorem 5.53 to this section, the function
(t,x )↦→ht(x), and the properly embedded real analytic submanifold ∂T×M. □
5.9. Approximately holomorphic extension of maps from totally real
submanifolds
Any real homomorphism Φ : E1→ E2 between two complex vector bundles
(Ei,Ji) can be canonically presented as a sum Φ = Φ + + Φ−, where Φ+ is complex
linear, i.e., Φ+◦J1 =J2◦Φ+, and Φ− is complex antilinear, i.e., Φ−◦J1 =−J2◦Φ−.
Indeed, we have Φ+ = 1
2(Φ−J2◦ Φ◦J1), Φ− = 1
2(Φ +J2◦ Φ◦J1). Given a smooth
map (V,J )→ (~V, ~J) between two complex manifolds we set∂f := (df)−. Of course,

5.9. APPROXIMATELY HOLOMORPHIC EXTENSIONS 109
when the complex manifolds coincide with Cn and Cm, then ∂f is the Cm-valued
(0, 1)-form ∂f =
n∑
1
∂f
∂zj
dzj.
The following proposition is a Ck-version of Lemma 5.40.
Proposition 5.55. Let (V,J ) and (~V, ~J) be two complex manifolds of complex
dimensions n and m, respectively. Suppose that (~V, ~J) is Stein. Let L⊂ V be
a totally real n-dimensional submanifold (not necessarily real analytic) and let f :
L→ ~V be a smooth map. Then for any integer k >0 there exists a smooth map
F :OpL→ ~V such that F|L =f and ∂F vanishes along L together with its k-jet.
Ifm =n andf is a diﬀeomorphism of L onto a totally real submanifold ~L⊂ ~V
then F is a diﬀeomorphism between OpL andOp~L and the complex structures ~J
and F∗J coincide along ~L together with their k-jets.
Proof. Step 1. Let us ﬁrst consider the case when ( V1,J 1) and (V2,J 2)
coincide with the standard Cn resp. Cm andL = Rn⊂ Cn. We deﬁne an extension
F of f to Cn by the formula
(5.1) F (x +iy) :=
∑
|I|≤k+1
1
I!
∂|I|f
∂xI (x)i|I|yI,
where I = (i1,...,i n) is a multi-index, |I| = i1 +··· +in, I! = i1!...i n!, and
yI =yi1
1 ...y in
n . Note that
∂F
∂xj
=
∑
|I|≤k+1
1
I!
∂|I|+1f
∂xI∂xj
(x)i|I|yI,
∂F
∂yj
=
∑
|I|≤k
1
I!
∂|I|+1f
∂xI∂xj
(x)i|I|+1yI,
∂F
∂xj
+i∂F
∂yj
=
∑
|I|=k+1
1
I!
∂|I|+1f
∂xI∂xj
(x)i|I|yI =O(|y|k+1),
and hence ¯∂F vanishes along Rn together with its k-jet.
Step 2. Consider now the case of general complex manifolds ( V,J ) and
(~V, ~J). Consider on L a real analytic structure compatible with its smooth struc-
ture. By Corollary 5.43, there exists a proper real analytic embeddingL↪→ RN. By
Lemma 5.40, this embedding extends to a holomorphic embedding LC ↪→ CN of a
complexiﬁcation of L into CN. We identify L,L C with the corresponding subset in
RN resp. CN. Since ~V is Stein, by Theorem 5.15 we can view it as a proper complex
submanifold of some CM. Extend f to a smooth map ~f : RN→ ~V ⊂ CM and then
extend ~f by formula (5.1) to a smooth map ~F : CN→ CM. Note that the image
of ~F need not be contained in ~V . However, by Corollary 5.27 there exists a neigh-
borhood ~U of ~V in CM which admits a holomorphic projection ~π : ~U→ ~V . After
shrinking LC we may assume that ~F (LC)⊂ ~U. Then the composition G :=~π◦ ~F
is an extension of f to a smooth map G :LC→ ~V such that ¯∂G vanishes along L
together with its k-jet.
Step 3. If L⊂ V is already real analytic, then LC is biholomorphic to a
neighborhood of L in V and G from Step 2 is the desired extension. For general
smooth L, it remains to ﬁnd an appropriate diﬀeomorphism H :LC→O pL⊂V .

110 5. SOME COMPLEX ANALYSIS
By Proposition 2.15, the totally real submanifold L has a Stein neighborhood in
V and hence we can assume that ( V,J ) is Stein. Now we apply the construction
of Step 2 to the inclusion h : L ↪→ V . This yields an extension of h to a smooth
diﬀeomorphism H :LC→O pL⊂V such that ¯∂H vanishes along L together with
its k-jet. Then G◦H−1 :OpL→ ~V is the desired extension of f.
The ﬁnal statement of the proposition follows from the implicit function theo-
rem. □
5.10. CR structures
We deﬁne aCR structure on an odd-dimensional manifoldM2n−1 as a germ of a
complex structureJ onOp (0×M)⊂ R×M. The maximal J-invariant distribution
on 0×M deﬁnes a hyperplane distribution ξ onM with complex structure ¯J =J|ξ
and the integrability of J implies
(5.2) X,Y ∈ξ =⇒ [ ¯JX, ¯JY ]− [X,Y ] = ¯J([ ¯JX,Y ] + [X, ¯JY ])∈ξ
(see e.g. [108]). We call the CR structure J-convex if 0×M is a J-convex hyper-
surface. In this case, ξ is a contact structure, the function φ(r,x ) = r is J-convex
onOp (0×M), and α :=−dCφ|0×M is a deﬁning contact form for ξ such that J|ξ
is compatible with dα|ξ.
Remark 5.56. (1) Usually (see e.g. [108]) a CR structure is deﬁned as a hyper-
plane distributionξ onM with a complex structure ¯J onξ satisfying equation (5.2).
If (M,ξ,J ) are real analytic and satisfy equation (5.2), then ¯J extends to an in-
tegrable complex structure on Op (0×M)⊂ R×M (see [108]). Note that for
dimM = 3 the condition (5.2) is vacuous. This implies, in particular, that if M is
a real analytic hypersurface in a 4-dimensional almost complex manifold (V,J ) with
real analytic J, then J can be made integrable in a neighborhood of M without
changing the induced CR structure.
(2) In general, a smooth ¯J satisfying (5.2) need not extend to a complex struc-
tureJ onOp (0×M)⊂ R×M. For example, for n = 2 there exist smooth convex
¯J which do not even extend to a neighborhood of a point in R×M ([153, 108]).
For smooth convex ¯J and n≥ 4 extension to a neighborhood of a point in R×M
is always possible ([ 118, 5 ]), while for smooth convex ¯J and n = 3 this ques-
tion remains open. In order to avoid these subtleties, we require extendibility to
Op (0×M)⊂ R×M in our deﬁnition of CR structure.
(3) In the literature “CR structure” often refers to the more general case of a
distribution ξ of arbitrary codimension; in this book by “CR structure” we always
mean the codimension one case.
Next we discuss the question of ﬁllability of CR structures. A holomorphic
ﬁlling of a closed CR manifold ( M,J ) is a compact complex manifold ( W,~J) such
that ∂W = M and ~J = J onOp (∂W ). It is called a Stein ﬁlling resp. K¨ ahler
ﬁlling if (W,~J) is Stein resp. K¨ ahler.
Remark 5.57. We deﬁne a compact complex manifold ( W,J ) with boundary
as a germ of a slightly larger complex manifold ( ~W, ~J) containing W as a smooth
submanifold with boundary such that ~J|W = J. Such an extension exists when-
ever (W,J ) is an almost complex manifold with J-convex boundary and vanishing
Nijenhuis tensor [29], but its germ need not be unique [ 94].

5.10. CR STRUCTURES 111
First we recall the following result (see [ 89] for the relevant deﬁnitions).
Theorem 5.58 (Rossi) . Given a compact complex manifold (W,J ) with J-
convex boundary ∂W , there exists a compact Stein space (W′,J′) with J′-convex
boundary and ﬁnitely many normal singularities p1,...,p k ∈ IntW′ and a holo-
morphic map f : W→ W′ such that f|W\f−1(P)→ W′\P is a biholomorphism.
Here we denote by P the set{p1,...,p k} of singular points of W′.
Proof. Theorem 4 in Section IX C of [ 89] provides a Stein space ( W′,J′)
having all the desired properties except possibly normality. Now ( W′,J′) has a
normalization (~W, ~J) such that the mapf :W→W′ factors through a holomorphic
map ~f : W → ~W [79, Chapter 8], and ( ~W, ~J) is again Stein by a theorem of
Narasimhan [145]. □
Combining this result with Hironaka’s theorem on resolution of singularities
one obtains
Theorem 5.59. For any closed convex CR manifold the notions of holomorphic
ﬁllability and K¨ ahler ﬁllability coincide.
Proof. Clearly, any K¨ ahler ﬁlling is a holomorphic ﬁlling. Conversely, ac-
cording to Theorem 5.58, a holomorphic ﬁlling of a convex CR manifold M can be
turned into a compact Stein space W with J-convex boundary and ﬁnitely many
normal singularities in its interior. By a theorem of Lempert [ 122], such a Stein
spaceW can be biholomorphically embedded into an aﬃne algebraic varietyX. By
Hironaka’s theorem [ 96], the singularities of X can be resolved. Hence we get a
realization of M as a J-convex hypersurface in a smooth projective algebraic vari-
ety ~X→X which bounds the preimage ~W of W in ~X, so ~W is the desired K¨ ahler
ﬁlling. □
In complex dimension n> 2 we have the following existence theorem for holo-
morphic ﬁllings.
Theorem 5.60 (Rossi [ 163]). For n > 2, any closed convex CR manifold
(M2n−1,J ) is holomorphically (and thus K¨ ahler) ﬁllable.
On the other hand, in general, for n> 2 a (holomorphically ﬁllable) CR struc-
ture need not be Stein ﬁllable. Indeed, there are easy homological obstructions to
Stein ﬁllability arising e.g. from the following argument which was explained to the
second author by M. Freedman.
Lemma 5.61. Let M be a closed manifold of dimension 2n− 1. Suppose that
for some coeﬃcient ring R there are cohomology classes ai∈Hdi(M;R) such that
a1∪···∪ ak⁄= 0, d i <n − 1, d 1 +··· +dk >n.
Then M is not the boundary of a Stein domain.
Proof. Suppose M = ∂W for a Stein domain W . Since W has a cell de-
composition without cells of index > n, it satisﬁes Hi(W ) = Hi(W ) = 0 for
i > n (all (co)homology is with coeﬃcients in R). Now di < n− 1 implies
Hdi+1(W,∂W ) = H2n−di−1(W ) = 0, so by the long exact sequence of the pair
(W,∂W ) the pullback mapj∗ :Hdi(W )→Hdi(∂W ) is surjective. Thus there exist
classes αi∈Hdi(W ) with j∗αi =ai and j∗(α1∪···∪ αk) =a1∪···∪ ak⁄= 0. But
on the other hand α1∪···∪ αk vanishes because Hd1+···+dk(W ) = 0, so we have a
contradiction. □

112 5. SOME COMPLEX ANALYSIS
Example 5.62. Forn >2 the real projective space RP 2n−1 admits no Stein
ﬁllable CR structures (although it inherits a CR structure fromS2n−1). This follows
from Lemma 5.61 because the cup product of 2 n− 1 classes of degree 1 (with Z2
coeﬃcients) is nonzero. Similarly, for n >2 the torus T 2n−1 does not admit any
Stein ﬁllable CR structure. In fact, it would be interesting to know whether T 2n−1,
n> 2, admits a CR structure at all.
The situation for n = 2 is drastically diﬀerent. First of all, a 3-dimensional CR
structure need not be holomorphically ﬁllable:
Example 5.63 (Rossi [ 163]). Note that for any ε∈ [0, 1) the intersection of
the quadric Qε ={z2
0 +z2
1 +z2
2 =ε}⊂ C3 with the boundary ∂B6 of the unit ball
B6⊂ C3 is diﬀeomorphic to RP 3. Let us denote by ¯Jε the convex CR structure on
RP 3 induced by this diﬀeomorphism.
Hence ( RP 3, ¯J0) is ﬁlled by the singular Stein space W0 = Q0∩B6, while
(RP 3, ¯Jε) for ε∈ (0, 1) is ﬁlled by the smooth Stein domain Wε = Qε∩B6. The
pullbacks of ¯Jε under the quotient map S3→ RP 3 yield CR structures Jε on S3
depending smoothly on ε∈ [0, 1). We claim that Jε is not Stein ﬁllable for ε> 0.
To see this, suppose thatW is a Stein ﬁlling of (S3,Jε). The quotient mapS3→
RP 3 then induces a holomorphic map Op (∂W )→O p (∂Wε). By Corollary 5.25,
this map extends to a holomorphic map F : W → Wε. Since F is a submersion
onOp (∂W ), the set Z⊂ W where the complex determinant of DF vanishes is
a compact codimension one analytic subvariety of W . Since the only compact
analytic subvarieties of a Stein manifold are zero dimensional (see e.g. Theorem 5.9
in Chapter II of [ 36]), it follows that Z is empty and hence F is a submersion. As
it is a 2-1 covering near ∂W , we see that F :W→Wε is a 2-1 covering. But Wε
is diﬀeomorphic to the unit disc cotangent bundle of S2, hence simply connected,
so it does not possess any connected 2-1 covering. Since the Stein manifold W is
connected, this gives a contradiction.
By contrast, J0 is isomorphic to the standard CR-structure on the boundary
of a ball in C2 and hence Stein ﬁllable. To see this, consider the holomorphic map
F : C2→ C3 given by the formula
F (u1,u 2) :=
(
u2
1 +u2
2,i (u2
1−u2
2), 2u1u2
)
, (u1,u 2)∈ C2.
ThenF (C2) =Q0 andF (B4) =W0 =Q0∩B6, where B4⊂ C2 denotes the ball of
radius 1/
√
2. The preimage of the origin under F is the origin, while the preimage
of any other point in Q0 is a pair of points ±(u1,u 2). Thus F induces a branched
holomorphic 2-1 covering B4→W0 and hence a holomorphic ﬁlling of ( S3,J 0) by
the ball B4. □
On the other hand, unlike the situation in complex dimension n > 2, the
following theorem shows that any holomorphically ﬁllable 3-dimensional convex CR
structure can be C∞-perturbed to a Stein ﬁllable one. Recall that a 2-dimensional
complex manifold is called minimal if it does not contain embedded holomorphic
spheres with self-intersection number −1. Any complex manifold can be made
minimal by blowing down all such spheres.
Theorem 5.64 (Bogomolov, de Oliveira [20]). Let (W,J ) be a minimal complex
manifold of complex dimension 2 with J-convex boundary. Then there exists a
deformationJt of the complex structure J0 =J such that (W,Jt) is a Stein domain
for all suﬃciently small t> 0.

Part 2
Existence of Stein Structures



6
Symplectic and Contact Preliminaries
In this chapter we collect some relevant facts from symplectic and contact
geometry. For more details see [ 136, 65].
6.1. Symplectic vector spaces
A symplectic vector space (V,ω ) is a real vector space V with a nondegenerate
skew-symmetric bilinear formω. Here nondegenerate means thatv↦→ω(v,·) deﬁnes
an isomorphism V →V∗. It follows that V has even dimension 2n. A linear map
Ψ : ( V1,ω 1)→ (V2,ω 2) between symplectic vector spaces is called symplectic if
Ψ∗ω2≡ω2(Ψ·, Ψ·) =ω1.
For any vector spaceU the spaceU⊕U∗ carries the standard symplectic struc-
ture
ωst
(
(u,u∗), (v,v∗)
)
:=v∗(u)−u∗(v).
In coordinatesqi onU and dual coordinatespi onU∗, the standard symplectic form
is given by
ωst =
∑
dqi∧dpi.
Deﬁne the ω-orthogonal complement of a linear subspace W⊂V by
Wω :={v∈V
⏐⏐ω(v,w ) = 0 for all w∈W}.
Note that dimW + dimWω = 2n, but W∩Wω need not be{0}. W is called
• symplectic if W∩Wω ={0};
• isotropic if W⊂Wω;
• coisotropic if Wω⊂W ;
• Lagrangian if Wω =W .
Note that dim W is even for W symplectic, dim W ≤ n for W isotropic,
dimW ≥ n for W coisotropic, and dim W = n for W Lagrangian. Note also
that (Wω)ω =W , and
(
W/(W∩Wω),ω
)
is a symplectic vector space.
Consider a subspace W of a symplectic vector space (V,ω ) and set N :=W∩
Wω. Choose subspaces V1⊂ W , V2⊂ Wω and an isotropic subspace V3⊂ (V1⊕
V2)ω such that
W =V1⊕N, W ω =N⊕V2, (V1⊕V2)ω =N⊕V3.
Then the decomposition
V =V1⊕N⊕V2⊕V3
induces a symplectic isomorphism
(V,ω )→ (W/N,ω )⊕ (Wω/N,ω )⊕ (N⊕N∗,ω st),
v1 +n +v2 +v3↦→
(
v1,v 2, (n,−iv3ω)
)
.(6.1)
115

116 6. SYMPLECTIC AND CONTACT PRELIMINARIES
Every symplectic vector space ( V,ω ) of dimension 2 n possesses a symplectic
basise1,f 1,...,e n,fn, i.e., a basis satisfying
ω(ei,ej) =ω(fi,fj) = 0, ω (ei,fj) =δij.
Moreover, given a subspace W⊂V , the basis can be chosen such that
• W = span{e1,...,e k+l,f 1,...,f k};
• Wω = span{ek+1,...,e n,fk+l+1,...,f n};
• W∩Wω = span{ek+1,...,e k+l}.
In particular, we get the following normal forms:
• W = span{e1,f 1,...,e k,fk} if W is symplectic;
• W = span{e1,...,e k} if W is isotropic;
• W = span{e1,...,e n,f 1,...,f k} if W is coisotropic;
• W = span{e1,...,e n} if W is Lagrangian.
This reduces the study of symplectic vector spaces to the standard symplectic space
(R2n,ω st =∑dqi∧dpi).
A pair (ω,J ) consisting of a symplectic form ω and a complex structure J on
a vector space V is called compatible if
gJ :=ω(·,J·)
is an inner product (i.e., symmetric and positive deﬁnite). This is equivalent to
saying that
H(v,w ) :=ω(v,Jw )−iω(v,w )
deﬁnes a Hermitian metric. Therefore, we will also call a compatible pair ( ω,J ) a
Hermitian structure and (V,ω,J ) a Hermitian vector space.
Lemma 6.1. (a) The space of symplectic forms compatible with a given complex
structure is nonempty and contractible.
(b) The space of complex structures compatible with a given symplectic form is
nonempty and contractible.
Proof. (a) immediately follows from the fact that the Hermitian metrics for
a given complex structure form a convex space.
(b) is a direct consequence of the following fact (see [ 136]): For a symplectic
vector space (V,ω ) there exists a continuous map from the space of inner products to
the space of compatible complex structures which maps each induced inner product
gJ to J.
To see this fact, note that an inner productg deﬁnes an isomorphismA :V →V
via ω(·,·) = g(A·,·). Skew-symmetry of ω implies AT =−A. Recall that each
positive deﬁnite operator P possesses a unique positive deﬁnite square root
√
P ,
and
√
P commutes with every operator with which P commutes. So we can deﬁne
Jg := (AAT )− 1
2A.
It follows thatJ2
g =−Id andω(·,J·) =g(
√
AAT·,·) is an inner product. Continuity
of the mappingg↦→Jg follows from continuity of the square root. Finally, ifg =gJ
for some J then A =J =Jg. □
Let us call a real subspace W⊂V of a complex vector space (V,J )
• totally real if W∩JW ={0},
• totally coreal if W +JW =V ,

6.2. SYMPLECTIC VECTOR BUNDLES 117
• maximally real if W∩JW ={0} and W +JW =V ,
• complex if JW =W .
Note that dim W≤ n if W is totally real, dim W≥ n if W is totally coreal, and
dimW =n if W is maximally real.
For a subspaceW⊂V of a Hermitian vector space (V,ω,J ) we denote by W⊥
the orthogonal complement with respect to the metric gJ =ω(·,J·). The following
lemma relates the symplectic and complex notions on a Hermitian vector space. It
follows easily from the relation Wω = (JW )⊥ =J(W⊥).
Lemma 6.2. Let (V,J,ω ) be a Hermitian vector space and W⊂V a real sub-
space. Then
(a) W isotropic⇐⇒JW ⊂W⊥ =⇒ W totally real;
(b) W coisotropic⇐⇒W⊥⊂JW =⇒ W totally coreal;
(a) W Lagrangian⇐⇒JW =W⊥ =⇒ W maximally real;
(c) W complex =⇒ W symplectic.
6.2. Symplectic vector bundles
The discussion of the previous section immediately carries over to vector bun-
dles. For this, let E→ M be a real vector bundle of rank 2 n over a manifold. A
symplectic structure on E is a smooth section ω in the bundle Λ 2E∗→ M such
that eachωx∈ Λ2E∗
x is a linear symplectic form. A pair ( ω,J ) of a symplectic and
a complex structure on E is called compatible, or a Hermitian structure, if ω(·,J·)
deﬁnes an inner product on E. Lemma 6.1 immediately yields the following facts,
where the spaces of sections are equipped with any reasonable topology, e.g. the
C∞
loc topology:
(a) The space of compatible symplectic structures on a complex vector bundle
(E,J ) is nonempty and contractible.
(b) The space of compatible complex structures on a symplectic vector bundle
(E,ω ) is nonempty and contractible.
This shows that the homotopy theories of symplectic, complex and Hermitian
vector bundles are the same. In particular, obstructions to trivialization of a sym-
plectic vector bundle (E,ω ) are measured by the Chern classes ck(E,ω ) =ck(E,J )
for any compatible complex structure J.
Remark 6.3. The homotopy equivalence between symplectic, complex and
Hermitian vector bundles can also be seen in terms of their structure groups: The
symplectic group 1
Sp(2n) :={Ψ∈GL(2n, R)| Ψ∗ω =ω} ={Ψ∈GL(2n, R)| ΨTJΨ =J}
and the complex general linear group GL(n, C) both deformation retract onto the
unitary group
U(n) =Sp(2n)∩O(2n) =O(2n)∩GL(n, C) =GL(n, C)∩Sp(2n).
We end this section with a normal form for subbundles of symplectic vector
bundles.
1Sp(2n) is not the “symplectic group” Sp(n) considered in Lie group theory. E.g., the latter
is compact, while our symplectic group is not.

118 6. SYMPLECTIC AND CONTACT PRELIMINARIES
Proposition 6.4. Let (E,ω ) be a rank 2n symplectic vector bundle andW⊂E
a rank 2k +l subbundle such that N :=W∩Wω has constant rank l. Then
(E,ω )∼= (W/N,ω )⊕ (Wω/N,ω )⊕ (N⊕N∗,ω st).
Proof. Pick a compatible complex structure J on (E,ω ). Then
V1 :=W∩JW, V 2 :=Wω∩JWω, V 3 :=JN
are smooth subbundles of E. Now the isomorphism (6.1) of the previous section
yields the desired decomposition. □
6.3. Symplectic manifolds
A symplectic manifold (V,ω ) is a manifoldV with a closed nondegenerate 2-form
ω. A map f : (V1,ω 1)→ (V2,ω 2) between symplectic manifolds is called symplec-
tic if f∗ω2 = ω1, and a symplectic diﬀeomorphism is called symplectomorphism.
The following basic result states that every symplectic manifold of dimension 2 n
is locally symplectomorphic to ( R2n,ω st). In other words, every symplectic ma-
nifold possesses a symplectic atlas, i.e., an atlas all of whose transition maps are
symplectic.
Proposition 6.5 (symplectic Darboux theorem) . Let (V,ω ) be a symplectic
manifold of dimension 2n. Then every x∈V possesses a coordinate neighborhood
U and a coordinate map φ :U→U′⊂ R2n such that φ∗ωst =ω.
The symplectic Darboux theorem is a special case of the symplectic neighbor-
hood theorem which will be proved in the next section. Now let us discuss some
examples of symplectic manifolds.
Cotangent bundles. Let T∗Q
π
→Q be the cotangent bundle of a manifold Q.
The 1-form∑pidqi is independent of coordinates qi on Q and dual coordinates pi
on T∗
qQ and thus deﬁnes the Liouville 1-form λst on T∗Q. Intrinsically,
(λst)(q,p)·v =⟨p,T (q,p)π·v⟩ for v∈T(q,p)T∗Q,
where⟨ , ⟩ is the pairing between T∗
qQ and TqQ. The 2-form ωst := dλst is
clearly closed, and the coordinate expression ωst =∑dqi∧dpi shows that it is also
nondegenerate. So ωst deﬁnes the standard symplectic form onT∗Q. The standard
form on R2n is a particular case of this construction.
Exact symplectic manifolds. Recall that a Liouville form on an even-dimen-
sional manifold V is a 1-form λ such that dλ is symplectic. The pair ( V,λ ) is then
called an exact symplectic manifold . For example, the form pdq is the standard
Liouville form on the cotangent bundle T∗L. An immersion or embedding φ :L→
V into an exact symplectic manifold (V,λ ) is called exact Lagrangian ifφ∗λ is exact.
The vector ﬁeld X dual to λ with respect to dλ, i.e., such that iXdλ =λ, is called
the Liouville ﬁeld. See Section 11.1 below for detailed discussion of these notions.
Almost complex submanifolds. A pair (ω,J ) consisting of a symplectic form
and an almost complex structure on a manifold V is called compatible if ω(·,J·)
deﬁnes a Riemannian metric. It follows that ω induces a symplectic form on every
almost complex submanifold W⊂V (which is compatible with J|W ).
J-convex functions. If (V,J ) is an almost complex manifold and φ : V → R
a J-convex function, then the 2-form ωφ =−ddCφ is symplectic. Moreover, ωφ is
compatible withJ ifJ is integrable (see Section 2.2). In particular, every J-convex
function on a Stein manifold induces a symplectic form compatible with J.

6.4. MOSER’S TRICK AND SYMPLECTIC NORMAL FORMS 119
K¨ ahler manifolds. A K¨ ahler manifold is a complex manifold (V,J ) with a
K¨ ahler metric, i.e., a Hermitian metric H =g−iω on TV such that the 2-form ω
is closed. Thus the K¨ ahler formω is a symplectic form compatible with J. Note
that every complex submanifold of a K¨ ahler manifold is again K¨ ahler.
The two basic examples of K¨ ahler manifolds areCn with the standard complex
structure and Hermitian metric, and the complex projective space CPn = (Cn+1\
0)/(C\ 0) with the induced complex structure and Hermitian metric (the latter is
deﬁned by restricting the Hermitian metric of Cn+1 to the unit sphere and dividing
out the standard circle action). Passing to complex submanifolds of Cn, we see
again that Stein manifolds are K¨ ahler. Passing to complex submanifolds of CPn,
we see that smooth projective varieties are K¨ ahler. This gives us a rich source of
examples of closed symplectic manifolds.
Remark 6.6. While cotangent bundles and K¨ ahler manifolds provide obvious
examples of symplectic manifolds, it is not obvious how to go beyond them. The
ﬁrst example of a closed symplectic manifold that is not K¨ ahler was constructed by
Thurston [184] in 1976. In 1995 Gompf [ 69] proved that every ﬁnitely presented
group is the fundamental group of a closed symplectic 4-manifold, in stark contrast
to the many restrictions on the fundamental groups of closed K¨ ahler surfaces.
Remark 6.7. A Riemannian metricg on a manifoldQ induces a natural almost
complex structureJg onT∗Q, compatible withωst, which interchanges the horizon-
tal and vertical subspaces deﬁned by the Levi-Civita connection. M. Grueneberg
(unpublished) has shown that Jg is integrable if and only if the metric g is ﬂat.
6.4. Moser’s trick and symplectic normal forms
An (embedded or immersed) submanifold W of a symplectic manifold (V,ω ) is
called symplectic (isotropic, coisotropic, Lagrangian) ifTxW⊂TxV is symplectic
(isotropic, coisotropic, Lagrangian) for every x∈W in the sense of Section 6.1. In
this section we derive normal forms for neighborhoods of such submanifolds.
All the normal forms can be proved by the same technique which we will refer
to as Moser’s trick . It is based on Cartan’s formula LXα = iXdα +diXα for a
vector ﬁeld X and a k-formα. Suppose we are given k-formsα0,α1 on a manifold
M, and we are looking for a diﬀeomorphism φ : M → M such that φ∗α1 = α0.
Moser’s trick is to construct φ as the time-1 map of a time-dependent vector ﬁeld
Xt. For this, let αt be a smooth family of k-forms connecting α0 and α1, and look
for a vector ﬁeld Xt whose ﬂow φt satisﬁes
(6.2) φ∗
tαt≡α0.
Then the time-1 map φ = φ1 solves our problem. Now equation (6.2) follows by
integration (provided the ﬂow ofXt exists, e.g. if Xt has compact support) once its
linearized version
0 = d
dtφ∗
tαt =φ∗
t ( ˙αt +LXtαt)
holds for every t. Inserting Cartan’s formula, this reduces the problem to the
algebraic problem of ﬁnding a vector ﬁeld Xt that satisﬁes
(6.3) ˙ αt +diXtαt +iXtdαt = 0.

120 6. SYMPLECTIC AND CONTACT PRELIMINARIES
Here is a ﬁrst application of this method. Here, as well as throughout the
book, by diﬀeotopy we denote a smooth family of diﬀeomorphisms φt, t∈ [0, 1],
with φ0 = Id.
Theorem 6.8 (Moser’s stability theorem). LetV be a manifold (without bound-
ary but not necessarily compact). Let ωt,t∈ [0, 1], be a smooth family of symplectic
forms onV which coincide outside a compact set and such that the cohomology class
with compact support [ωt−ω0]∈H2
c (V ; R) is independent of t. Then there exists a
diﬀeotopyφt with φt = Id outside a compact set such that φ∗
tωt =ω0.
In particular, this applies if ωt =dλt for a smooth family of 1-forms λt which
coincide outside a compact set, and in this case there exists a smooth family of
functions ft :V → R with compact support such that
φ∗
tλt−λ0 =dft.
Proof. For everyt the closed 2-form ˙ωt is trivial in cohomology with compact
support H2
c (V ; R), so there exists a 1-form βt with compact support such that
dβt = ˙ωt. The forms βt are not unique, but by an argument of Banyaga [ 13] they
can be chosen to depend smoothly on t and to be supported in a ﬁxed compact
subset. Now we can solve equation (6.3),
0 = ˙ωt +diXtωt +iXtdωt =d(βt +iXtωt)
by solvingβt +iXtωt = 0, which has a unique solutionXt due to the nondegeneracy
of ωt. Since Xt vanishes outside a compact subset, its ﬂow φt exists and gives the
desired family of diﬀeomorphisms.
In the case ωt = dλt we pick βt := ˙λt. Then the deﬁning equation for Xt
becomes ˙λt +iXtdλt = 0 and we ﬁnd
d
dtφ∗
tλt =φ∗
td(iXtλt),
which integrates to
φ∗
tλt−λ0 =d
(∫ t
0
iXsλsds
)
.
□
Corollary 6.9. Let W be a compact manifold with (possibly empty) bound-
ary ∂W . Let ωt, t∈ [0, 1], be a smooth family of symplectic forms such that the
restrictions ωt|∂W and the relative cohomology classes [ωt−ω0]∈ H2(W,∂W ; R)
are independent of t. Then there exists a diﬀeotopy φt with φt|∂W = Id such that
φ∗
tωt =ω0.
Proof. If ∂W = ∅ this is a special case of Theorem 6.8. In the case M =
∂W ⁄= ∅ we argue as follows. Consider the inclusion ι : M → R×M, x ↦→
(0,x ), and the projection π : R×M → M. Recall from [ 87] that there exists a
continuous linear mapP : Ω2(R×M)→ Ω1(R×M) satisfying the homotopy formula
dP +Pd = Id−π∗ι∗. Applying this to the forms ˙ ωt on a tubular neighborhood
[0, 1)×M ofM inW we ﬁnd a smooth family of 1-formsαt :=P ˙ωt vanishing along
∂M (this follows from the explicit formula for P in [87]) such that dαt = ˙ωt on
[0, 1)×M. Pick a cutoﬀ function f : W → [0, 1] which equals 1 near ∂W and 0
outside [0, 1)×M and extend fαt by zero over the rest of W . The closed 2-forms
˙ωt = d(fαt) have compact support in Int W and are trivial in cohomology with
compact support H2
c (IntW ; R), so by [ 13] there exists a smooth family of 1-forms

6.4. MOSER’S TRICK AND SYMPLECTIC NORMAL FORMS 121
γt with ﬁxed compact support in Int W such that dγt = ˙ωt−d(fαt). Now we
proceed as in the proof of Theorem 6.8 with the 1-forms βt :=γt +fαt. Since the
resulting vector ﬁeld Xt vanishes on ∂W , its ﬂow φt exists and gives the desired
family of diﬀeomorphisms. □
Our second application of Moser’s trick is the following lemma, which is the
basis of all the normal form theorems below.
Lemma 6.10. LetW be a compact submanifold of a manifold V , and let ω0,ω 1
be symplectic forms on V which agree at all points of W . Then there exist tubular
neighborhoodsU0,U 1 of W and a diﬀeomorphism φ :U0→U1 such that φ|W = Id
and φ∗ω1 =ω0.
Proof. Set ωt := (1−t)ω0 +ω1. Since ωt≡ ω0 along W , ωt are symplectic
forms on some tubular neighborhood U of W . By a homotopy formula similar to
the one used in the previous proof, since ˙ωt =ω1−ω0 is closed and vanishes along
W , there exists a 1-form β on U such that β = 0 along W and dβ = ˙ωt on U. As
in the proof of Theorem 6.8, we solve equation (6.3) by setting β +iXtωt = 0.
To apply Moser’s trick, a little care is needed because U is noncompact, so the
ﬂow of Xt may not exist until time 1. However, since β = 0 along W , Xt vanishes
along W . Thus there exists a tubular neighborhood U0 of W such that the ﬂow
φt(x) of Xt exists for all x∈ U0 and t∈ [0, 1], and φt(U0)⊂ U for all t∈ [0, 1].
Nowφ1 :U0→U1 :=φ1(U0) is the desired diﬀeomorphism with φ∗
1ω1 =ω0. □
Now we are ready for the main result of this section.
Proposition 6.11 (symplectic normal forms) . Letω0,ω 1 be symplectic forms
on a manifold V and W ⊂ V a compact submanifold such that ω0|W = ω1|W .
Suppose that N := ker(ω0|W ) = ker( ω1|W ) has constant rank, and the bundles
(TW ω0/N,ω 0) and (TW ω1/N,ω 1) overW are isomorphic as symplectic vector bun-
dles. Then there exist tubular neighborhoods U0,U 1 of W and a diﬀeomorphism
φ :U0→U1 such that φ|W = Id and φ∗ω1 =ω0.
Proof. By Proposition 6.4,
(TV|W,ω 0)∼= (TW/N,ω 0)⊕ (TW ω0/N,ω 0)⊕ (N⊕N∗,ω st),
and similarly for ω1. By the hypotheses, the terms on the right-hand side are
isomorphic for ω0 and ω1. More precisely, there exists an isomorphism
Ψ : (TV|W,ω 0)→ (TV|W,ω 1)
with Ψ|TW = Id. Extend Ψ to a diﬀeomorphism ψ :U0→U1 of tubular neighbor-
hoods such that ψ|W = Id and ψ∗ω1 =ω0 along W , and apply Lemma 6.10. □
The following normal forms, due to Weinstein, are easy corollaries of this result.
Corollary 6.12 (symplectic neighborhood theorem). Letω0,ω 1 be symplectic
forms on a manifold V and W ⊂ V a compact submanifold such that ω0|W =
ω1|W is symplectic, and the symplectic normal bundles (TW ω0,ω 0), (TW ω1,ω 1)
over W are isomorphic (as symplectic vector bundles). Then there exist tubular
neighborhoodsU0,U 1 of W and a diﬀeomorphism φ :U0→U1 such that φ|W = Id
and φ∗ω1 =ω0.

122 6. SYMPLECTIC AND CONTACT PRELIMINARIES
Corollary 6.13 (isotropic neighborhood theorem) . Let ω0,ω 1 be symplectic
forms on a manifold V and W ⊂ V a compact submanifold such that ω0|W =
ω1|W = 0, and the symplectic normal bundles (TW ω0/TW,ω 0), (TW ω1/TW,ω 1)
are isomorphic (as symplectic vector bundles). Then there exist tubular neighbor-
hoods U0,U 1 of W and a diﬀeomorphism φ : U0→ U1 such that φ|W = Id and
φ∗ω1 =ω0.
Corollary 6.14 (coisotropic neighborhood theorem). Letω0,ω 1 be symplectic
forms on a manifold V and W⊂V a compact submanifold such that ω0|W =ω1|W
and W is coisotropic for ω0 and ω1. Then there exist tubular neighborhoods U0,U 1
of W and a diﬀeomorphism φ :U0→U1 such that φ|W = Id and φ∗ω1 =ω0.
Corollary 6.15 (Weinstein’s Lagrangian neighborhood theorem [ 186]). Let
W⊂ (V,ω ) be a compact Lagrangian submanifold of a symplectic manifold. Then
there exist tubular neighborhoods U of the zero section in T∗W and U′ of W in V
and a diﬀeomorphism φ :U→U′ such that φ|W is the inclusion and φ∗ω =ωst.
Proof. Since W is Lagrangian, the map v ↦→ ivω deﬁnes an isomorphism
from the normal bundle TV/TW |W to T∗W . Extend the inclusion W ⊂ V to a
diﬀeomorphism ψ : U→ U′ of tubular neighborhoods of the zero section in T∗W
and ofW inV . Now apply the coisotropic neighborhood theorem to the zero section
in T∗W and the symplectic forms ωst and ψ∗ω. □
6.5. Contact manifolds and their Legendrian submanifolds
A contact structure ξ on a manifold M is a completely non-integrable tangent
hyperplane ﬁeld. According to the Frobenius condition, this means that for every
nonzero local vector ﬁeld X∈ ξ there exists a local vector ﬁeld Y ∈ ξ such that
their Lie bracket satisﬁes [ X,Y ] /∈ ξ. If α is any 1-form locally deﬁning ξ, i.e.,
ξ = kerα, this means
dα(X,Y ) =−1
2α([X,Y ])⁄= 0.
So the restriction of the 2-formdα toξ is nondegenerate, i.e., (ξ,dα|ξ) is a symplec-
tic vector bundle. This implies in particular that dim ξ is even and dimM = 2n+ 1
is odd. In terms of a local deﬁning 1-form α, the contact condition can also be
expressed as α∧ (dα)n⁄= 0.
A diﬀeomorphism f : (M1,ξ 1)→ (M2,ξ 2) between contact manifolds is called
a contactomorphism if f∗ξ1 =ξ2.
Remark 6.16. If dimM = 4k + 3 the sign of the volume form α∧ (dα)2k+1
is independent of the sign of the deﬁning local 1-form α, so a contact structure
deﬁnes an orientation of the manifold. In particular, in these dimensions contact
structures can exist only on orientable manifolds. On the other hand, a contact
structure ξ on a manifold of dimension 4k + 1 is itself orientable.
Contact structures ξ in this book will always be cooriented, i.e., they are glob-
ally deﬁned by a 1-form α. In this case the symplectic structure on each of the
hyperplanes ξ is deﬁned uniquely up to a positive conformal factor. Moreover,
associated to each deﬁning 1-form α is its Reeb vector ﬁeld Rα deﬁned by
iRαdα = 0, α (Rα) = 1.

6.5. CONTACT MANIFOLDS AND THEIR LEGENDRIAN SUBMANIFOLDS 123
Given a J-convex hypersurface M (which is by deﬁnition cooriented) in an almost
complex manifold (V,J ), the ﬁeld ξ of complex tangencies deﬁnes a contact struc-
ture on M which is cooriented by Jν , where ν is a vector ﬁeld transverse to M
deﬁning the coorientation. Conversely, any cooriented contact structure ξ arises as
a ﬁeld of complex tangencies on a J-convex hypersurface in an almost complex ma-
nifold: Just choose a complex multiplication J onξ compatible with the symplectic
form dα in the sense that dα(·,J·) is a (positive deﬁnite) inner product on ξ and
extend J arbitrarily to an almost complex structure on V :=M× (−ϵ,ϵ ).
Remark 6.17. If dimM = 3 thenJ can always be chosen integrable. However,
in dimensions≥ 5 this is not always the case, see Remark 6.28 below.
Let (M,ξ = kerα) be a contact manifold of dimension 2 n + 1. An immersion
φ : Λ→ M is called isotropic if it is tangent to ξ. Then at each point x∈ Λ we
have dφ(TxΛ)⊂ ξφ(x) and dα|dφ(TxΛ) = d
(
α|φ(Λ)
)
(x) = 0. Hence dφ(TxL) is an
isotropic subspace in the symplectic vector space ( ξx,dα ). In particular,
dim Λ≤ 1
2 dimξ =n.
Isotropic immersions of the maximal dimension n are called Legendrian.
1-jet spaces. Let L be a manifold of dimension n. The space J1L of 1-jets
of functions on L can be canonically identiﬁed with T∗L× R, where T∗L is the
cotangent bundle of L. A point in J1L is a triple (q,p,z ) where q is a point in L,
p is a linear form on TqL, and z∈ R is a real number. Let pdq =∑pidqi be the
standard Liouville form onT∗L (see Section 6.3). Then the 1-form dz−pdq deﬁnes
the standard contact structure
ξst := ker(dz−pdq )
on J1L. A function f :L→ R deﬁnes a section
q↦→j1f(q) :=
(
q,df (q),f (q)
)
of the bundle J1L→ L. Since f∗(dz−pdq ) = df−df = 0, this section is a
Legendrian embedding in the contact manifold ( J1L,ξ st). Consider the following
diagram, where all arrows represent the obvious projections:
J1L
Pfront
{{vvvvvvvvv
π

PLag
""FFFFFFFF
L× R
$$HHHHHHHHH T∗L
{{xxxxxxxxx
L
We call PLag the Lagrangian projection and Pfront the front projection. Given a
Legendrian submanifold Λ⊂J1L, consider its images
PLag(Λ)⊂T∗L, P front(Λ)⊂L× R.
The map PLag : Λ→T∗L is a Lagrangian immersion with respect to the standard
symplectic structure dp∧dq = d(pdq ) on T∗L. Indeed, the contact hyperplanes
of ξcan are transverse to the z-direction which is the kernel of the projection PLag.

124 6. SYMPLECTIC AND CONTACT PRELIMINARIES
Hence Λ is transverse to the z-direction as well and PLag|Λ is an immersion. It is
Lagrangian because
P∗
Lag(dp∧dq) =d(pdq|Λ) =d(dz|Λ) = 0.
Conversely, any exact Lagrangian immersion φ : Λ→ T∗L, i.e., an immersion for
which the form φ∗(pdq ) is exact, lifts to a Legendrian immersion ˆφ : Λ→J1L. It
is given by the formula ˆφ := (φ,H ), where H is a primitive of the exact 1-form
φ∗(pdq ) so that ˆφ∗(dz−pdq ) = dH−φ∗pdq = 0. The lift ˆφ is unique up to a
translation along the z-axis.
Let us now turn to the front projection. The image Pfront(Λ) is called the
front of the Legendrian submanifold Λ ⊂ J1L. If the projection π|Λ : Λ → L
is nonsingular and injective, then Λ is a graph {
(
q,α (q),f (q)
)
| q∈ π(Λ)} over
π(Λ)⊂ L. The Legendre condition implies that the 1-form α is given by α = df.
So
Λ ={
(
q,df (q),f (q)
)
|q∈π(Λ)}
is the graph of the 1-jet j1f of a function f : π(Λ)→ R. In this case the front
Pfront(Λ) is just the graph of the function f.
In general, the front of a Legendrian submanifold Λ ⊂ J1L can be viewed as
the graph of a multivalued function. Note that since the contact hyperplanes are
transverse to thez-direction, the singular points of the projection π|Λ coincide with
the singular points of the projection Pfront|Λ. Hence near each of its nonsingular
points the front is indeed the graph of a function.
In general, the front can have quite complicated singularities. But when the
projection π|Λ : Λ → L has only “fold type” singularities, then the front itself
has only “cuspidal” singularities along its singular locus as shown in Figure 6.1.
Let us discuss this picture in more detail. Consider ﬁrst the 1-dimensional case
Figure 6.1. A Legendrian arc in R3 whose front projection (onto
the shaded region) has a cusp.
when L = R. Then J1L = R3 with coordinates ( q,p,z ) and contact structure

6.6. CONTACT NORMAL FORMS 125
ker(dz−pdq ). Consider the curve in R3 given by the equations
(6.4) q =
(2p
3
)2
, z =
(2p
3
)3
.
This curve is Legendrian because dz = 8
9p2dp = pdq . Its front is given by (6.4)
viewed as parametric equations for a curve in the (q,z )-plane. This is the semicubic
parabola z2 =q3 shown in Figure 6.1.
Generically, any singular point of a Legendrian curve in R3 looks like this. This
means that, after aC∞-small perturbation of the given curve to another Legendrian
curve, there exists a contactomorphism of a neighborhood of the singularity which
transforms the curve to the curve described by (6.4) (see [ 11, Chapter 1 §4]). If
we want to construct just C1 Legendrian curves (and any C1 Legendrian curve
can be further C1-approximated by C∞ or even real analytic Legendrian curves,
see Corollary 6.25), then the following characterization of the front near its cusp
points will be convenient. Suppose that the two branches of the front which form
the cusp are given locally by the equations z = f(q) and z = g(q), where the
functionsf,g : [0,ϵ )→ R satisfyf≤g, see Figure 6.1. Then the front lifts to a C1
Legendrian curve if and only if
f(0) =g(0), f ′(0) =g′(0),
f′′(q)→−∞ as q→ 0, g ′′(q)→ +∞ as q→ 0.
In higher dimensions, suppose that a Legendrian submanifold Λ⊂J1L projects toL
with only “fold type” singularities. Then along its singular locus the front consists of
the graphs of two functionsf≤g deﬁned on an immersed stripS×[0,ϵ ). Denoting
coordinates on S× [0,ϵ ) by (s,t ), the front lifts to a C1 Legendrian submanifold if
and only if
f(s, 0) =g(s, 0), ∂f
∂t (s, 0) = ∂g
∂t (s, 0),
∂2f
∂t2 (s,t )→−∞ as t→ 0, ∂2g
∂t2 (s,t )→ +∞ as t→ 0.
However, in higher dimensions not all singularities are generically of fold type.
Example 6.18. Given a contact manifold ( M,ξ = kerα) and an exact sym-
plectic manifold (V,λ ), their product M×V is a contact manifold with the contact
form α⊕λ. For example, if M =J1N and V =T∗W with the canonical contact
and Liouville forms, then M×V = J1(N×W ) with the canonical contact form.
A product Λ ×L of a Legendrian submanifold Λ ⊂ M and an exact Lagrangian
submanifoldL⊂V is a Legendrian submanifold of M×V . In particular, the prod-
uct of a Legendrian submanifold Λ ⊂ J1N and an exact Lagrangian submanifold
L⊂T∗W is a Legendrian submanifold in J1(N×W ).
6.6. Contact normal forms
Let (M2n+1,ξ = kerα) be a contact manifold and Λ k⊂M, 0≤k≤n, be an
isotropic submanifold. The following result is due to Darboux in the case that Λ is
a point (see e.g. Appendix 4 of [ 10]); the extension to general Λ is straightforward
and left to the reader.

126 6. SYMPLECTIC AND CONTACT PRELIMINARIES
Proposition 6.19 (contact Darboux theorem) . Near each point on Λ there
exist coordinates (q1,...,q n,p 1,...,p n,z )∈ R2n+1 in which α =dz−∑pidqi and
Λ = Rk×{ 0}.
To formulate a more global result, recall that the form ω = dα deﬁnes a nat-
ural (i.e., independent of α) conformal symplectic structure on ξ. Denote the ω-
orthogonal on ξ by a superscript ω. Since Λ is isotropic, T Λ⊂ (T Λ)ω. So the
normal bundle of Λ in M is given by
TM/T Λ =TM/ξ⊕ξ/(T Λ)ω⊕ (T Λ)ω/T Λ∼= R⊕T∗Λ⊕CSN (Λ).
HereTM/ξ is trivialized by the Reeb vector ﬁeldRα, the bundleξ/(T Λ)ω is canon-
ically isomorphic to T∗Λ via v↦→ ivω, and CSN (Λ) := ( T Λ)ω/T Λ denotes the
conformal symplectic normal bundle which carries a natural conformal symplectic
structure induced byω. Thus CSN (Λ) has structure groupSp(2n−2k), which can
be reduced to U(n−k) by choosing a compatible complex structure.
Let (M,ξM) and (N,ξN) be two contact manifolds. A mapf :M→N is called
isocontact if f∗ξN = ξM, where f∗ξN :={v∈ TM | df·v∈ ξN}. Equivalently,
f maps any deﬁning 1-form αN for ξN to a deﬁning 1-form f∗αM for ξM. In
particular, f must be an immersion and thus dim M ≤ dimN. Moreover, df :
ξM→ξN is conformally symplectic, i.e., symplectic up to a scaling factor. We call
a monomorphism F : TM → TN isocontact if F∗ξN = ξM and F : ξM → ξN is
conformally symplectic.
Proposition 6.20 (contact isotropic neighborhood theorem [ 187]). Let (M,
ξM), (N,ξN) be contact manifolds with dimM≤ dimN and Λ⊂ M an isotropic
submanifold. Let f : Λ→ N be an isotropic immersion covered by an isocontact
monomorphism F : TM → TN . Then there exists an isocontact immersion g :
U→N of a neighborhood U⊂M of Λ with g|Λ =f and dg =F along Λ.
Remark 6.21. (a) If f is an embedding then g is also an embedding on a
suﬃciently small neighborhood. It follows that a neighborhood of a Legendrian
submanifold Λ is contactomorphic to a neighborhood of the zero section in the
1-jet space J1Λ (with its canonical contact structure).
(b) A Legendrian immersionf : Λ→ (M,ξ ) extends to an isocontact immersion
of a neighborhood of the zero section in J1Λ.
(c) Suppose that the conformal symplectic normal bundle of an isotropic sub-
manifold Λ is the complexiﬁcation of a real bundle W → Λ (i.e., the structure
group of CSN (Λ) reduces from U(n−k) to O(n−k)). Then a neighborhood of Λ
is contactomorphic to a neighborhood of the zero section in J1Λ⊕ (W⊕W∗) (with
its canonical contact structure, see Example 6.18). In this case (and only in this
case) the isotropic submanifold Λ extends to a Legendrian submanifold (the total
space of the bundle W ).
We will also need the following reﬁnement of the isotropic neighborhood the-
orem. Following Weinstein [ 187], let us denote by isotropic setup a quintuple
(V,ω,X, Σ, Λ), where
• (V,λ ) is a symplectic manifold with Liouville ﬁeld X and ω =dλ;
• Σ⊂V is a codimension one hypersurface transverse to X;
• Λ⊂ Σ is a closed isotropic submanifold for the contact structure ker(λ|Σ).
Let (T Λ)ω/T Λ⊂ξ be the symplectic normal bundle over Λ.

6.7. REAL ANALYTIC APPROXIMATIONS OF ISOTROPIC SUBMANIFOLDS 127
Proposition 6.22 (Weinstein [ 187]). Let (Vi,ωi,Xi, Σi, Λi), i = 0, 1 be two
isotropic setups. Given a diﬀeomorphism f : Λ0→ Λ1 covered by an isomorphism
Φ of symplectic normal bundles, there exists an isomorphism of isotropic setups
F : (U0,ω 0,X 0, Σ0∩U0, Λ0)→ (U1,ω 1,X 1, Σ1∩U1, Λ1)
between neighborhoodsUi of Λi in Vi inducing f and Φ.
All the properties discussed in this section also hold for families of isotropic sub-
manifolds. Moreover, any isotropic submanifold with boundary can be extended
beyond the boundary to a slightly bigger isotropic submanifold of the same dimen-
sion.
A similar homotopy argument proves Gray’s stability theorem, which states
that on a closed manifold all deformations of a contact structure are diﬀeomorphic
to the original one.
Theorem 6.23 (Gray’s stability theorem [ 75]). Let (ξt)t∈[0,1] be a smooth ho-
motopy of contact structures on a closed manifold M. Then there exists a diﬀeotopy
φt :M→M with φ0 = Id and φ∗
tξt =ξ0 for all t∈ [0, 1].
More generally, let (ξλ)λ∈Dk be a smooth family of contact structures on a
closed manifold M, parametrized by the closed k-dimensional disc Dk. Then there
exists a smooth family of diﬀeomorphisms φλ :M→M withφ0 = Id andφ∗
λξλ =ξ0
for all λ∈Dk.
Finally, let us mention the following contact version of the isotopy extension
theorem (see e.g. [ 65, Theorem 2.6.2]):
Proposition 6.24 (contact isotopy extension theorem) . Let Λt, t∈ [0, 1], be
an isotopy of compact isotropic submanifolds, possibly with boundary, in a contact
manifold (M,ξ ). Then there exists a smooth family of contactomorphisms ft :M→
M with f0 = Id such that ft(Λ0) = Λt.
6.7. Real analytic approximations of isotropic submanifolds
Using the results from Chapter 5, we now derive a result on real analytic
approximations of isotropic submanifolds that will be needed later.
Corollary 6.25. Let Λ be a closed isotropic Ck-submanifold (k≥ 1) in a
real analytic closed contact manifold (M,α ) (i.e., the manifold M and the 1-form
α are both real analytic). Then there exists a real analytic isotropic submanifold
Λ′⊂ (M,α ) arbitrarilyCk-close to Λ.
Similarly, let (Λt)t∈[0,1] be a Ck-isotopy of closed isotropic Ck-submanifolds in
(M,α ) such that Λ0 and Λ1 are real analytic. Then there exists a real analytic
isotopy of real analytic isotropic submanifolds Λ′
t, arbitrarily Ck-close to Λt, with
Λ′
0 = Λ0 and Λ′
1 = Λ1.
Proof. Let ~Λ⊂ M be a real analytic submanifold Ck-close to Λ, but not
necessarily isotropic. Then Λ = φ(~Λ) for a Ck-diﬀeomorphism φ : M→ M that
is Ck-close to the identity. The contact form φ∗α vanishes on ~Λ but need not be
real analytic. Thus φ∗α induces a Ck-section in the real analytic vector bundle
T∗M|~Λ→ ~Λ which vanishes on the real analytic subbundle T~Λ⊂ T∗M|~Λ. Let
ν→~Λ be the normal bundle to T~Λ inT∗M|~Λ with respect to a real analytic metric
and denote by (φ∗α)ν the inducedCk-section inν. Let βν be a real analytic section

128 6. SYMPLECTIC AND CONTACT PRELIMINARIES
ofν that is Ck-close to (φ∗α)ν and extend it to a real analytic section β ofT∗M|~Λ
that vanishes on T~Λ, and hence is Ck-close to φ∗α along ~Λ. Extend β to a Ck
one-form on M (still denoted by β) that is Ck-close to φ∗α. By construction, β is
real analytic along ~Λ and β|~Λ = 0.
By Theorem 5.53 (with d = 0), there exists a real analytic 1-form ~α that isCk-
close to β and coincides with β along ~Λ. In particular, ~α|~Λ = 0. By construction,
~α is Ck-close to α. Hence αt := (1−t)~α +tα is a real analytic homotopy of real
analytic contact forms. By Gray’s Stability Theorem 6.23, there exists a diﬀeotopy
φt : M → M and positive functions ft with φ∗
tα = ft~α. Now in Moser’s proof
of Gray’s stability theorem (see e.g. [ 26]), the φt are constructed as solutions of
an ODE whose coeﬃcients are real analytic and Ck-small in this case. Hence by
Remark 5.39 the φt are real analytic, Ck-close to the identity, and depend real
analytically on t. It follows that Λ ′ := φ1(~Λ) is real analytic, Ck-close to Λ, and
α|Λ′ = 0.
The statement about homotopies follows in a similar way using Corollary 5.54.
□
Remark 6.26. (1) Corollary 6.25 remains valid (with essentially the same
proof) if the submanifold Λ is not closed, providing a real analytic approximation
on a compact subset K⊂ Λ.
(2) If Λ is Legendrian, then Λ′ is Legendrian isotopic to Λ: By the Legendrian
neighborhood theorem (Proposition 6.20), Λ′ is the graph of the 1-jet of a function
f in J1Λ, and the functions tf provide the isotopy.
6.8. Relations between symplectic and contact manifolds
Symplectic and contact geometries are deeply linked with each other. We de-
scribe in this section some basic relations.
Let (M,ξ ) be a contact manifold with a cooriented contact structure. Let
Nξ⊂ T∗M be the 1-dimensional conormal bundle of ξ, i.e., the space of 1-forms
annihilating ξ, and N+
ξ its R+-subbundle consisting of forms deﬁning the given
coorientation of ξ. The non-integrability condition for ξ then can be re-interpreted
as the condition that the form ωξ =d(pdq)|N +
ξ
is nondegenerate. The symplectic
manifold Symp(M,ξ ) = (N+
ξ ,ωξ) is called the symplectization of the contact ma-
nifold ξ. Note that the form λξ =pdq|N +
ξ
is a Liouville form, and the vector ﬁeld
Xξ =p ∂
∂p is the corresponding Liouville ﬁeld. A choice of a contact formα provides
a symplectomorphism of Symp(M,ξ ) with ( R+×M,d (rα)) and identiﬁes λξ with
the 1-form rα. Sometimes it is convenient to change the variable r = es,s ∈ R
and thus identify the symplectization with
(
R×M,d (esα)
)
. In this presentation
λξ =esα and the corresponding Liouville ﬁeld is Xξ = ∂
∂s . The contact geometry
of (M,ξ ) can be reinterpreted as the symplectic geometry of Symp( M,ξ ) equivari-
ant with respect to the R-action generated by the ﬂow of the Liouville ﬁeld Xξ,
or equivalently the geometry of the Liouville manifold ( N+
ξ ,λξ). For example, the
diﬀeomorphisms of N+
ξ preserving the Liouville form λξ are precisely the lifts of
contactomorphisms of (M,ξ ).
Conversely, suppose we are given a symplectic manifold ( V,ω ). A cooriented
hypersurface M⊂ V is called locally (resp. globally) ω-convex (see [49]) if there
exists a Liouville ﬁeld X on a neighborhood of M (resp. on all of V ) which is

6.8. RELATIONS BETWEEN SYMPLECTIC AND CONTACT MANIFOLDS 129
positively transverse toM. 2 In both cases the restriction α =λ|M of the Liouville
form λ = iXω is a contact form on M. If the Liouville ﬁeld is complete we get a
Liouville embedding of the symplectization ( R×M,esα)↪→ (V,λ ) by matching the
corresponding trajectories of the Liouville ﬁelds ∂
∂s on R×M and X on V .
If dimV = 4 we call M (locally resp. globally) weakly ω-convex if it admits
a contact form α deﬁning the induced orientation such that ω|ξ = dα|ξ, where
ξ = ker α. This notion is indeed weaker than ω-convexity, e.g. ω|M need not
be exact for weakly ω-convex M. It was observed in [ 133, Lemma 2.1] that for
dimV ≥ 6 the corresponding notion of “weak ω-convexity” would be equivalent
to ω-convexity and hence not useful. Massot, Niederkr¨ uger and Wendl [130] have
recently proposed a diﬀerent notion of weakω-convexity in higher dimensions which
diﬀers from ω-convexity.
An important special case of the above discussion occurs when M = ∂V and
M is cooriented by an outward normal vector ﬁeld to V . If ∂V is globally (weakly)
ω-convex andV is compact the contact structure on M is called (weakly) symplec-
tically ﬁllable . In all dimensions there exist many examples of contact manifolds
that are not weakly symplectically ﬁllable (see e.g. [130]). On the other hand, there
exist contact structures on the 3-torus that are weakly but not strongly symplecti-
cally ﬁllable [46]. With the notion by Massot–Niederkr¨ uger–Wendl, there also exist
contact 5-manifolds that are weakly but not strongly symplectically ﬁllable [ 130],
while this question is currently open in dimensions ≥ 7.
A contact manifold ( M,ξ ) is called holomorphically ﬁllable if there exists a
compact complex manifold ( V,J ) with J-convex boundary M = ∂V such that ξ
equals the ﬁeld of complex tangencies on M. In the terminology of Section 5.10,
this means that ξ carries a holomorphically ﬁllable CR structure. So Theorem 5.59
implies
Corollary 6.27. Holomorphically ﬁllable contact structures are symplectically
ﬁllable.
Remark 6.28. Niederkr¨ uger and van Koert [151] have shown that every closed
contact manifold M carries also a contact structure ξ which is not symplectically
ﬁllable. It follows from the preceding corollary and Theorem 5.60 that if dimM≥ 5,
then ξ cannot be deﬁned by an (integrable) CR structure.
2An alternative terminology is contact type for locally symplectically convex, and restricted
contact type for globally symplectically convex, see [ 100].



7
The h-Principles
Theh-principle for a partial diﬀerential equation or inequality asserts, roughly
speaking, that a formal solution can be deformed to a genuine solution. This notion
ﬁrst appeared in [ 81] and [ 86]. General references for h-principles are Gromov’s
book [84] and the more recent [ 52].
In this chapter we discuss various h-principles that we need in this book. In
the ﬁrst three sections we collect some relevant h-principles that are available in
the literature (mostly [ 84, 52]).
The following three sections are concerned with Legendrian embeddings: In
Section 7.5 we show that a formal Legendrian embedding in a contact manifold
of dimension ≥ 5 can be deformed to a genuine Legendrian embedding in the
same formal class. In Section 7.6 we use the classiﬁcation of overtwisted contact
structures to derive an h-principle for Legendrian knots in such manifolds. In
Section 7.7 we describe an h-principle for a remarkable class of “loose” Legendrian
knots in dimension≥ 5 recently found by Murphy.
In the last two sections we combine h-principles for totally real embeddings
with those for isotropic contact embeddings to obtain h-principles for totally real
discs attached to J-convex boundaries. The resulting Theorems 7.34 and 7.36 are
essential ingredients for the existence and deformation of Stein structures discussed
in later chapters.
Throughout this chapter, a knot denotes a (parametrized) embedding of a con-
nected manifold.
7.1. Immersions and embeddings
We begin by reviewing some facts about smooth immersions and embeddings.
The h-principle for immersions. Let M,N be manifolds. A monomor-
phism F : TM → TN is a ﬁberwise injective bundle homomorphism covering a
continuous map M→ N. Any immersion f : M→ N gives rise to a monomor-
phismdf :TM →TN . We denote by Mon(TM,TN ) the space of monomorphisms,
and by Imm(M,N ) the space of immersions. Given a (possibly empty) closed sub-
set A⊂ M and an immersion h :OpA→ N, we denote by Imm( M,N ;A,h ) the
subspace of Imm(M,N ) which consists of immersions equal to h onOpA. Simi-
larly, the notation Mon(TM,TN ;A,dh ) stands for the subspace of Mon(TM,TN )
of monomorphisms which coincide with dh onOpA. Extending Smale’s theory of
immersions of spheres [171, 172], Hirsch [97] proved the following h-principle (see
also [84, 52]):
Theorem 7.1 (Smale–Hirsch immersion theorem) . For dimM < dimN and
any immersion h :OpA→ N, the map f ↦→ df deﬁnes a homotopy equivalence
131

132 7. THE h-PRINCIPLES
between the spaces Imm(M,N ;A,h ) and Mon(TM,TN ;A,dh ). In particular, we
have the following special cases:
(a) Any monomorphism F∈ Mon(TM,TN ;A,dh ) is homotopic to the diﬀer-
ential df of an immersion f :M→N which coincides with h onOpA.
(b) Given a homotopy Ft∈ Mon(TM,TN ;A,dh ), t∈ [0, 1], between the dif-
ferentialsF0 =df0 and F1 =df1 of two immersions f0,f 1∈ Imm(M,N ;A,h ), one
can ﬁnd a regular homotopy ft∈ Imm(M,N ;A,h ), t∈ [0, 1], such that the paths
Ft and dft, t∈ [0, 1], are homotopic with ﬁxed ends.
For example, if a k-dimensional manifold M is parallelizable, i.e., TM ∼=M×
Rk, the inclusion Rk ↪→ Rk+1 gives rise to a monomorphism TM = M× Rk→
T (Rk+1) = Rk+1× Rk+1, (x,v )↦→ (0,v ). Thus Theorem 7.1 implies that every
parallelizable manifold Mk can be immersed into Rk+1.
Immersions of half dimension. Next we describe results of Whitney [191]
on immersions of half dimension. Fix a closed connected manifold Mn of dimension
n≥ 2 and an oriented manifold N2n of double dimension. Let f : M→ N be an
immersion whose only self-intersections are transverse double points. Then if M is
orientable andn is even we assign to every double point z =f(p) =f(q) an integer
If(z) as follows. Pick an orientation of M. Set If(z) :=±1 according to whether
the orientations of df(TpM) and df(TqM) together determine the orientation of N
or not. Note that this deﬁnition depends neither on the order of p and q (because
n is even), nor on the orientation of M. Deﬁne the self-intersection index
If :=
∑
z
If(z)∈ Z
as the sum over all self-intersection points z. If n is odd or M is non-orientable
deﬁne If∈ Z2 as the number of self-intersection points modulo 2.
Theorem 7.2 (Whitney [ 191]). For a closed connected manifold Mn and an
oriented manifold N2n, n≥ 2, the following holds.
(a) The self-intersection index is invariant under regular homotopies.
(b) The self-intersection index of an immersion f :M→N can be changed to
any given value by a local modiﬁcation (which is of course not a regular homotopy).
(c) If n≥ 3 and N is simply connected, then any immersion f : M→ N is
regularly homotopic to an immersion with precisely |If| transverse double points
(where|If| means 0 resp. 1 for If∈ Z2).
Remark 7.3. (i) Whitney states his theorem only for N = R2n, but the proof
works without changes for general N (see e.g. [140]).
(ii) The theorem continues to hold ifM has boundary, provided that for immer-
sions and during regular homotopies no self-intersections occur on the boundary.
(iii) For n = 1 Whitney [ 191] deﬁnes a self-intersection index If ∈ Z. With
this deﬁnition, all the preceding results continue to hold for n = 1.
Since every immersion of half dimension is regularly homotopic to an immersion
with transverse self-intersections ([190], see also [ 98]), part (a) allows us to deﬁne
the self-intersection index for every immersion f :M→N. Since every n-manifold
immerses into R2n, parts (b) and (c) imply (the cases n = 1, 2 are treated by hand)
Corollary 7.4 (Whitney embedding theorem [191]). Every closedn-manifold
Mn, n≥ 1, can be embedded in R2n.

7.1. IMMERSIONS AND EMBEDDINGS 133
As we will use a similar argument below, let us sketch the proof of Theorem 7.2
(c). For details see [ 191, 140 ]. The claim is well known for n = 1, 2 so we will
assume that n≥ 3. Take an immersion f : M→ R2n which exists due to general
position arguments. Consider two transverse double points yi = f(x+
i ) = f(x−
i ),
i = 0, 1. If M is orientable and n is even we assume that If(y0) =−If(y1). Since
n≥ 3, we ﬁnd two disjoint embedded paths γ± in M from x±
0 to x±
1 not meeting
any other preimages of double points. Their images C± = f(γ±) ﬁt together to
an embedded loop C = C+∪C− in R2n+1 (with corners at y0 and y1). Denote
byM±⊂f(M) the images under f of tubular neighborhoods of γ± in M. Orient
M± arbitrarily. We arrange that the intersection numbers ofM± aty0 andy1 have
opposite signs as follows: ForM orientable andn even this holds by assumption; for
M orientable andn odd it can be achieved by interchangingx+
1 andx−
1 if necessary;
and for M non-orientable we can arrange this by concatenating, if necessary, γ+
with an orientation reversing loop in M.
Using simply-connectedness of the target we ﬁnd an embedded half-disc ∆ ⊂
R2n with ∂±∆ = C±. Here the half-disc ∆ is diﬀeomorphic to the lower half-disc
D− ={(x1,x 2)∈ R2|x2
1 +x2
2≤ 1, x2≤ 0}, see Figure 9.4 below. Using n≥ 3, we
can arrange that ∆ is transverse to f(M) along the boundary and does not meet
f(M) in its interior. Such a half-disc ∆ is called a Whitney disc . The condition
that the intersection numbers of M± at y0 and y1 have opposite signs allows us to
ﬁnd a diﬀeomorphism from a neighborhood of ∆ into R2× Rn−1× Rn−1 mapping
∆ to D−⊂ R2× 0× 0, M+ to ∂+D−× Rn−1× 0, and M− to ∂−D−× 0× Rn−1.
In this model we can now write down an explicit isotopy pulling M+ away from
M− across ∆, thus obtaining a regular homotopy of f removing the two double
points y0,y 1. Proceeding in this way we cancel all pairs of double points (with
opposite indices if M is orientable and n even) until their number equals|If|. The
elimination procedure just described is sometimes called the Whitney trick . Its
failure for n = 2 is the source of many exotic phenomena in smooth topology that
occur in dimension 4 but not in higher dimensions.
Isotopies. Finally, we discussisotopies, i.e., homotopies through embeddings.
Consider a closed connected k-manifold Mk and an oriented (2 k + 1)-manifold
N2k+1. Let ft :M→N be a regular homotopy between embeddings f0,f 1 :M ↪→
N. We deﬁne the self-intersection index I{ft} of the regular homotopy ft as the
self-intersection indexIF of the immersionF :M×I→N×I given by the formula
(x,t )↦→ft(x),x∈M,t∈I = [0, 1]. The self-intersection index I{ft} is an invariant
offt in the class of regular homotopies with ﬁxed endpointsf0,f 1. Recall that I{ft}
takes values in Z ifM is orientable andk is odd, and in Z2 otherwise. In the former
caseI{ft} remains unchanged when the orientation is switched to the opposite one.
Remark 7.5. Let us stress the point that in choosing the orientation of N×I
we wrote the intervalI as the second factor. Choosing the opposite ordering would
result (when k is odd) in switching the sign of I{ft}.
The following result is an analogue of Whitney’s Theorem 7.2 for isotopies.
Theorem 7.6. For k > 1 consider a closed connected k-manifold Mk and a
simply connected oriented (2k + 1)-manifold N2k+1. Let ft :M→N be a regular
homotopy between embeddings f0,f 1 : M ↪→ N. Then ft can be deformed through
regular homotopies with ﬁxed endpoints to an isotopy if and only if I{ft} = 0.

134 7. THE h-PRINCIPLES
In particular, this implies the following result which was proved by Wu [ 194]
and later greatly generalized by Haeﬂiger [ 90].
Corollary 7.7. For k > 1 consider a closed connected k-manifold Mk and
a simply connected oriented (2k + 1)-manifold N2k+1. Then any two homotopic
embeddingsf0,f 1 :M ↪→N are isotopic.
Proof. Pick a homotopy connecting f0 and f1 and deform it to a regular
homotopy ft. By adding new self-intersection points to this homotopy we can
arbitrarily change its self-intersection index (see [191]). In particular, we can make
I{ft} = 0 and then apply Theorem 7.6 to ﬁnd the desired isotopy. □
The proof of Theorem 7.6 uses the following standard transversality result
which is a special case of Thom’s multi-jet transversality theorem, see e.g. [ 98].
The case Λ = [0, 1] is due to Whitney [ 190].
Lemma 7.8. LetM,N, Λ be manifolds and F : Λ×M→N a smooth map. If
dim Λ + 2 dimM <dimN, then F can be C∞-approximated by a map ~F such that
~F (λ,·) is an embedding for all λ∈ Λ. Moreover, if F is already an embedding near
a compact subset K⊂ Λ×M we can choose ~F =F nearK. □
Proof of Theorem 7.6. The argument is an adjustment of the Whitney
trick [191] explained above. Take two self-intersection points Y0 = (y0,t 0),Y 1 =
(y1,t 1)∈ N× (0, 1) of the immersion F : Mk× [0, 1]→ N2k+1× [0, 1] deﬁned
above. If M is orientable and k is odd we assume that the intersection indices of
these points have opposite signs. Each of the double pointsy0,y 1 is the image of two
distinct pointsx±
0,x±
1 ∈M, i.e., we haveft0(x±
0 ) =y0 andft1(x±
1 ) =y1. As k> 1,
we ﬁnd two embedded pathsγ± : [t0,t 1]→M such thatγ±(t0) =x±
0 ,γ±(t1) =x±
1 ,
and γ+(t)⁄=γ−(t) for all t∈ [t0,t 1]. As explained above, we can choose the paths
γ± such that the (arbitrarily oriented) local branches of F (M× [0, 1]) along the
images of γ± in N× [0, 1] have opposite intersection numbers at Y0 and Y1. We
claim that there exists a smooth family of paths δt : [−1, 1]→N, t∈ [t0,t 1], such
that
• δt(±1) =ft
(
γ±(t)
)
for all t∈ [t0,t 1];
• δt0(s) =y0, δt1(s) =y1 for all s∈ [−1, 1];
• δt is an embedding for all t∈ (t0,t 1).
Indeed, a family with the ﬁrst two properties exists because N is simply connected.
Moreover, we can arrange that δt is an embedding for t⁄=t0,t 1 close to t0,t 1. Now
we can achieve the third property by Lemma 7.8 because 2 · 1 + 1< 2k + 1. Deﬁne
∆ : [t0,t 1]× [−1, 1]→N× [0, 1], (t,s )↦→
(
δt(s),t
)
.
Then ∆ is an embedding on ( t0,t 1)× [−1, 1] and ∆( t0× [−1, 1]) = Y0, ∆(t1×
[−1, 1]) = Y1. Thus ∆ serves as a Whitney disc for the elimination of the double
points Y0,Y 1 of the immersion F . Due to the special form of ∆, Whitney’s elim-
ination construction described above (see [ 191, 140]) can be performed in such a
way that the modiﬁed immersion ~F has the form ~F (x,t ) :=
(~ft(x),t
)
for a regular
homotopy ~ft : M → N such that the paths ft,~ft∈ Imm(M,N ), t∈ [0, 1], are
homotopic. Hence the repeated elimination of pairs of intersection points (of oppo-
site indices if M is orientable and k odd) of the immersion F results in the desired
isotopy between f0 and f1 if I{ft} = 0. □

7.2. THE h-PRINCIPLE FOR ISOTROPIC IMMERSIONS 135
7.2. The h-principle for isotropic immersions
The following h-principle was proved by Gromov in 1986 ([ 84], see also [ 52]).
Let (M,ξ ) be a contact manifold of dimension 2 n + 1, Λ a manifold of di-
mension k≤ n, and A⊂ Λ a closed subset. Let h :OpA→ M be an isotropic
immersion. We denote by Imm isotr(Λ,M ;A,h ) the space of isotropic immersions
Λ→ M which coincide with h onOpA, and by Mon isotr(T Λ,ξ ;A,dh ) the space
of isotropic monomorphisms T Λ→ξ which coincide with dh onOpA. In the case
k =n isotropic monomorphisms will also be called Legendrian monomorphisms and
denoted by MonLeg(T Λ,ξ ;A,dh ).
Note that if we equip ξ with a compatible complex structure, then the space
Monisotr(T Λ,ξ ;A,dh ) is a subspace of the space Monreal(T Λ,ξ ;A,dh ) of totally real
monomorphisms T Λ→ξ which coincide with dh onOpA, and the inclusion
Monisotr(T Λ,ξ ;A,dh )↪→ Monreal(T Λ,ξ ;A,dh )
is a homotopy equivalence.
Theorem 7.9 (Gromov’sh-principle for contact isotropic immersions [84, 52]).
The map d : Immisotr(Λ,M ;A,h ) ↪→ Monisotr(T Λ,ξ ;A,dh ) is a homotopy equiva-
lence. In particular, we have the following special cases:
(a) Given F∈ Monisotr(T Λ,ξ ;A,dh ) one ﬁnds f∈ Immisotr(Λ,M ;A,h ) such
that df and F are homotopic in Monisotr(T Λ,ξ ;A,dh ). Moreover, f can be chosen
C0-close to the map Λ→M covered by the homomorphism F .
(b) Given two isotropic immersions f0,f 1∈ Immisotr(Λ,M ;A,h ) and a homo-
topy Ft ∈ Monisotr(T Λ,ξ ;A,dh ), t∈ [0, 1], connecting df0 and df1 one ﬁnds an
isotropic regular homotopy ft∈ Immisotr(Λ,M ;A,h ) connectingdf0 and df1 such
that the paths Ft and dft, t∈ [0, 1], are homotopic in Monisotr(T Λ,ξ ;A,dh ) with
ﬁxed ends. Moreover, the ft can be chosen C0-close to the family of maps Λ→M
covered by the homotopy Ft.
Combining the preceding theorem with the Smale–Hirsch Immersion Theo-
rem 7.1 yields
Corollary 7.10. Let Λ,M,A,h be as in Theorem 7.9. Suppose that f0 : Λ→
M is an immersion which coincides with the isotropic immersion h onOpA andFt
is a family of monomorphisms T Λ→TM such that F0 =df0,Ft =dh onOpA for
all t∈ [0, 1], and F1∈ Monisotr(T Λ,ξ ;A,dh ). Then there exists a regular homotopy
ft : Λ→M such that
(i) f1∈ Immisotr(Λ,M ;A,h );
(ii) ft =h onOpA for all t∈ [0, 1];
(iii) there exists a homotopy Fs
t , s∈ [0, 1], of paths in Mon(T Λ,TM ;A,dh )
such that F 0
t = dft and F 1
t = Ft for all t∈ [0, 1], and Fs
0 = df0 and
Fs
1∈ Monisotr(T Λ,ξ ;A,dh ) for all s∈ [0, 1].
Proof. We ﬁrst use Theorem 7.9 to construct an isotropic immersion g2∈
Immisotr(Λ,ξ ;A,h ) and a homotopy Ft ∈ Monisotr(T Λ,TM ;A,dh ), t ∈ [1, 2],
such that F2 = dg2. Next we apply Theorem 7.1 to get a regular homotopy
gt∈ Imm(Λ,M ;A,h ), t∈ [0, 2], such that g0 =f0 and the paths dgt,Ft, t∈ [0, 2],
are homotopic with ﬁxed ends. Let
G : [0, 2]× [0, 1]→ Mon(T Λ,TM ;A,dh ), (t,s )↦→Gs
t

136 7. THE h-PRINCIPLES
s
s
1
1
df0
df0 Gs
t
F s
t
Φ
t
t1
2
dft
Ft
Ft
Monisotr(TΛ, ξ; A, dh)
Monisotr(TΛ, ξ; A, dh)
dgt
dg2
Figure 7.1. The families of monomorphisms G and F =G◦ Φ.
be this homotopy, i.e., G0
t =dgt, G1
t =Ft for all t∈ [0, 2], and Gs
0 =df0, Gs
2 =dg2
for all s∈ [0, 1]. The required paths are now deﬁned by ft :=g2t, t∈ [0, 1], and
F :=G◦ Φ : [0, 1]× [0, 1]→ Mon(T Λ,TM ;A,dh ), (t,s )↦→Fs
t,
where Φ : [0, 1]×[0, 1]→ [0, 2]×[0, 1] is any homeomorphism mapping the boundary
as follows (see Figure 7.1):
[0, 1]× 0→ [0, 2]× 0, [0, 1]× 1→ [0, 1]× 1,
0× [0, 1]→ 0× [0, 1], 1× [0, 1]→ (2× [0, 1])∪ ([1, 2]× 1).
□
7.3. The h-principle for subcritical isotropic embeddings
In this and the next two sections we upgrade, under suitable conditions, the
results of the previous section from isotropic immersions to embeddings. We begin
with the subcritical case.
Consider a contact manifold (M2n+1,ξ ) and a manifold Λk of dimensionk≤n.
A formal isotropic embedding of Λ into (M,ξ ) is a pair (f,F s), where f : Λ ↪→M
is a smooth embedding and Fs :T Λ→TM is a homotopy of monomorphisms over
f starting at F 0 = df and ending at an isotropic monomorphism F 1 : T Λ→ ξ
coveringf. In the case k =n we also call this a formal Legendrian embedding.
Any genuine isotropic embedding can be viewed as a formal isotropic embed-
ding (f,F s≡ df). We will not distinguish between an isotropic embedding and
its canonical lift to the space of formal isotropic embeddings, and we will consider

7.4. STABILIZATION OF LEGENDRIAN SUBMANIFOLDS 137
formal isotropic isotopies between genuine isotropic embeddings: two isotropic em-
beddings f0,f 1 : Λ ↪→ (M,ξ ) are called formally isotropically isotopic if they are
isotopic as formal isotropic embeddings.
We will also consider relative isotropic embeddings and their isotopies, which
are required to coincide with a ﬁxed genuine isotropic embedding on a neighborhood
of a closed subset A⊂ Λ. The space of isotropic embeddings which coincide with a
given isotropic embedding h onOpA will be denoted by Emb isotr(Λ,M ;A,h ), and
the corresponding space of formal isotropic embeddings by Mon emb
isotr(T Λ,ξ ;A,dh ).
With these notations, we have the following h-principle.
Theorem 7.11 (h-principle for subcritical isotropic embeddings [ 84, 52]).
Consider a contact manifold (M,ξ ) of dimension 2n + 1, a manifold Λ of di-
mension k<n , and a closed subset A⊂ Λ. Then the inclusion
Monemb
isotr(Λ,M ;A,h )↪→ Embisotr(T Λ,ξ ;A,dh )
is a weak homotopy equivalence. In particular, suppose that two isotropic embed-
dings f0,f 1 ∈ Embisotr(Λ,M ;A,h ) are connected by a formal isotropic isotopy
(ft,F s
t ), s,t ∈ [0, 1] relOpA. Then there exists a genuine isotropic isotopy gt
relOpA connectingg0 =f0 andg1 =f1 which is homotopic to the formal isotropic
isotopy (ft,F s
t ) through formal isotropic isotopies ﬁxed on OpA.
7.4. Stabilization of Legendrian submanifolds
The goal of this section is the proof of the following proposition which will play
a crucial role in the proof of the Existence Theorem 7.16 for Legendrian embeddings
in the next section. Recall from Section 7.1 the deﬁnition of the self-intersection
index of a smooth immersion.
Proposition 7.12. For n≥ 2 let Λ0⊂ (M2n+1,ξ = kerα) be a closed ori-
entable Legendrian submanifold and k an integer. Then there exists a Legendrian
submanifold Λ1⊂ M and a Legendrian regular homotopy Λt, t∈ [0, 1], such that
the self-intersection index of the immersion L := ⋃
t∈[0,1] Λt×{t}⊂ M× [0, 1]
equalsk (mod 2 if n is even).
Remark 7.13. By Corollary 7.7, Λ 1 is smoothly isotopic to Λ 0. We will not
use this fact, see however Section 7.7 for an elementary proof in the case k = 0.
A local construction. The proof of Proposition 7.12 for n> 1 is based on
a stabilization procedure which we will now describe, see Figure 7.2.
Consider the front projection of a (not necessarily closed) orientable Legendrian
submanifold Λ 0⊂ R2n+1. Suppose that Pfront(Λ0) intersects Bn× [−1, 2] in the
two oppositely oriented branches{z = 0} and{z = 1}. Let f :Bn→ (−1, 2) be a
function which equals zero near∂Bn and has no critical points on level 1. Replacing
the branch {z = 0} over Bn by{z = tf(q)} we obtain a family of Legendrian
immersions Λt⊂ R2n+1, t∈ [0, 1]. Note that the set {q∈ Bn| f(q)≥ 1} is a
smooth n-manifold with boundary. Denote by χ({f≥ 1}) its Euler characteristic.
Lemma 7.14. The self-intersection index of the immersion L :=⋃
t∈[0,1] Λt×
{t}⊂ M× [0, 1] equals
IL = (−1)n(n−1)/2χ({f≥ 1})
(mod 2 if n is even).

138 7. THE h-PRINCIPLES
z
q
2
1
0
−1
f
t0f
q0
{f ≥ 1}
Pfront(Λ0)
Figure 7.2. Stabilization of a Legendrian submanifold.
Proof. Perturbf such that all critical points above level 1 are nondegenerate
and lie on distinct levels. Self-intersections of L occur precisely when t0f has a
critical point q0 on level 1 for some t0 ∈ (0, 1). By the Morse Lemma, we ﬁnd
coordinates near q0 in which q0 = 0 and f has the form
f(q) =a0− 1
2
k∑
i=1
q2
i + 1
2
n∑
i=k+1
q2
i,
where a0 =f(q0) = 1/t0 and k is the Morse index of q0. The p-coordinates on the
branch{z =tf(q)} of Λt near q0 are given by
pi = ∂(tf)
∂qi
=
{
−tqi i≤k,
+tqi i≥k + 1.
Thus the tangent spaces in T (R2n+1× [0, 1]) = R2n+2 of the two intersecting
branches of L corresponding to{z = 1} and{z =t0f(q)} are given by
T1 ={p1 =··· =pn = 0,z = 0},
T2 ={pi =−t0qi for i≤k,pi = +t0qi for i≥k + 1,z =a0t}.
Without loss of generality (because the self-intersection index does not depend on
the orientation of L) suppose that the basis ( ∂q1,...,∂ qn,∂t) represents the orien-
tation of T1. Since the two branches of Λ 0 are oppositely oriented, the orientation
of T2 is then represented by the basis
(
∂q1−t0∂p1,...,∂ qn +t0∂pn,−(∂t +a0∂z)
)
.
Hence the orientation of (T1,T 2) is represented by
(∂q1,...,∂ qn,∂t,−∂p1,..., −∂pk,∂pk+1,...,∂ pn,−∂z),
which equals (−1)k+n+n(n−1)/2 times the complex orientation
(∂q1,∂p1,...,∂ qn,∂pn,∂z,∂t)
of R2n+2 = Cn+1. So the local intersection index of L at a critical point q equals
IL(q) = (−1)indf(q)+n+n(n−1)/2
(mod 2 if n is even), where indf(q) is the Morse index of q.

7.5. THE EXISTENCE THEOREM FOR LEGENDRIAN EMBEDDINGS 139
On the other hand, for a vector ﬁeldv on a compact manifoldN with boundary
which is outward pointing along the boundary and has only nondegenerate zeroes
the Poincar´ e-Hopf index theoremholds: The sum of the indices of v at all its zeroes
equals the Euler characteristic of M (see [87]). Note that if v is the gradient vector
ﬁeld of a Morse function f, then the index of v at a critical point q of f equals
(−1)indf(q). Applying the Poincar´ e-Hopf index theorem to the gradient of the Morse
function−f on the manifold {f≥ 1} ={−f≤− 1} (which is outward pointing
along the boundary because f has no critical point on level 1), we obtain
χ({f≥ 1} =
∑
q
ind∇(−f)(q) =
∑
q
(−1)ind−f(q) =
∑
q
(−1)n−indf(q)
= (−1)n(n−1)/2∑
q
IL(q) = (−1)n(n−1)/2IL.
□
Proof of Proposition 7.12. Since all Legendrian submanifolds are locally
isomorphic, a neighborhood in M of a point on Λ 0 is contactomorphic to a neigh-
borhood in R2n+1 of a point on a standard cusp z2 =q3
1. Thus the front consists of
two branches{z =±q
3
2
1} joined along the singular locus {z =q1 = 0}. Deform the
branches to{z =±ε} over a small ball disjoint from the singular locus, thus (after
rescaling) creating two parallel branches over a ball as in Lemma 7.14. Now deform
Λ0 to Λ1 as in Lemma 7.14, for some function f : Bn→ (−1, 2). Hence Proposi-
tion 7.12 follows from Lemma 7.14, provided that we can arrange χ({f≥ 1}) = k
for a given integer k if n> 1.
So it only remains to ﬁnd for n > 1 an n-dimensional submanifold-with-
boundary N⊂ Rn of prescribed Euler characteristic χ(N) = k (then write N =
{f≥ 1} for a function f :N→ [1, 2) without critical points on the boundary). Let
N+ be a ball in Rn, thus χ(N+) = +1. Let N− be a smooth tubular neighborhood
in Rn of a ﬁgure eight in R2, thus χ(N−) =−1 (here we use n≥ 2 !). So we can
arrange χ(N) to be any integer by taking disjoint unions of copies of N±. This
concludes the proof of Proposition 7.12. □
Remark 7.15. The preceding proof fails for n = 1 because a 1-dimensional
manifold with boundary always has Euler characteristic χ≥ 0. Therefore for n = 1
the local construction in Lemma 7.14 allows us only to realize positive values of the
self-intersection index IL. In Section 7.6 we will see that for overtwisted contact
structures one can get around this problem.
7.5. The existence theorem for Legendrian embeddings
The parametric h-principle of the previous section fails for Legendrian embed-
dings: For any n ≥ 1 there are pairs of Legendrian knots in R2n+1 which are
formally but not genuinely Legendrian isotopic [ 31, 40 ]. However, it turns out
that if n> 1 then, using the stabilization trick from Section 7.4 and Theorem 7.6,
the existence part (i.e., surjectivity on π0) continues to hold in the Legendrian case
k =n. For n = 1 the analogous claim is false in general, but true in the overtwisted
case, see Theorem 7.19 below.
Theorem 7.16 (existence theorem for Legendrian embeddings for n> 1).
For n≥ 2 consider a contact manifold (M,ξ ) of dimension 2n + 1, a simply
connected manifold Λ of dimension n, and a closed subset A⊂ Λ. Let (f0,F s
0 ) be

140 7. THE h-PRINCIPLES
a formal Legendrian embedding of Λ into (M,ξ ) which is genuine on OpA. Then
there exists a Legendrian embedding f1 : Λ↪→M which coincides with f0 onOpA
and can be connected with (f0,F s
0 ) by a formal Legendrian isotopy ﬁxed on OpA.
In the proof we use the following notation. Given two continuous paths γ1,γ 2 :
[0, 1]→ X into a topological space X with γ1(0) = γ2(1) we deﬁne their concate-
nation to be the path
γ1⋆γ 2(t) :=
{
γ1(2t), t ∈ [0, 1
2],
γ2(2t− 1), t ∈ [ 1
2, 1].
We will also use the following general position observation.
Lemma 7.17. Let (M,ξ ) be a contact manifold of dimension 2n + 1 and Λ a
manifold of dimension n. Then any Legendrian immersion f0 : Λ→ (M,ξ ) can be
included into a family of Legendrian immersions ft : Λ→ (M,ξ ) C∞-close to f0
such that f1 is an embedding.
Proof. Consider a Legendrian immersionf : Λ→M. By Proposition 6.20 we
can extendf to an isocontact immersion F :U→M of a neighborhood of the zero
section in the 1-jet space J1Λ. Then nearby Legendrian immersions correspond
to graphs of 1-jets of functions on Λ, hence the claim follows from Thom’s jet
transversality theorem, see e.g. [ 98]. □
Proof of Theorem 7.16. In what follows we assume that all constructions
are done relative to A and do not state this explicitly anymore. By applying
Corollary 7.10 we can satisfy all the conditions of the theorem, except that ft
will be a regular homotopy rather than an isotopy. By Lemma 7.17, after a C∞-
small isotropic regular homotopy, we may assume that f1 is a Legendrian em-
bedding. Thus, starting from a formal Legendrian embedding ( f0,F s
0 ) we have
constructed a regular homotopy ft : Λ→M,t∈ [0, 1], and a 2-parameter family of
monomorphisms Fs
t :T Λ→TM extending the family Fs
0 such that F 0
t =dft and
F 1
t ∈ Monisotr(TM,ξ ;A,dh ) for all t, and Fs
1 =df1 for all s.
We will deform the regular homotopyft to an isotopy, keeping the endf0 ﬁxed
and changingf1 via a Legendrian regular homotopy. According to Theorem 7.6, in
order to deform the pathft to an isotopy keeping both ends ﬁxed we need the equal-
ityI{ft} = 0. (Here the simple connectedness hypothesis in Theorem 7.6 is satisﬁed
because we can perform the whole construction in a tubular neighborhood of f0(Λ)
which is simply connected). On the other hand, according to Proposition 7.12,
for any Legendrian embedding g0 there exists a Legendrian regular homotopy gt
to a Legendrian embedding g1 with any prescribed value of the self-intersection
index I{gt}. Hence by concatenating ft, t∈ [0, 1], with an appropriate Legendrian
regular homotopy ft, t∈ [1, 2], we obtain a regular homotopy ft, t∈ [0, 2], with
I{ft}t∈[0,2] = 0. We extend Fs
t fort∈ [1, 2] bydft and rescale the interval [0, 2] back
to [0, 1]. After this, we may hence assume that I{ft}t∈[0,1] = 0.
Now Theorem 7.6 provides a 2-parameter family of immersions gs
t : Λ→ M,
s,t∈ [0, 1], such thatgs
0 =f0 andgs
1 =f1 for alls,g1
t =ft, andg0
t is an embedding
for allt∈ [0, 1]. For each t∈ [0, 1] letGs
t,s∈ [0, 1], be the path of monomorphisms
T Λ→ TM obtained by concatenating the paths dgs
t and Fs
t . Then ( g0
t,Gs
t) is a
formal Legendrian isotopy connecting (f0,F s
0 ) with the Legendrian knot f1. □

7.6. LEGENDRIAN KNOTS IN OVERTWISTED CONTACT MANIFOLDS 141
7.6. Legendrian knots in overtwisted contact manifolds
In dimension 3 there is a dichotomy between tight and overtwisted contact
structures, which was introduced in [41]. A contact structure ξ on a 3-dimensional
manifold M is called overtwisted if there exists an embedded disc D⊂M which is
tangent to ξ along its boundary ∂D. Equivalently, one can require the existence of
an embedded disc with Legendrian boundary∂D which is transverse toξ along∂D.
A disc with such properties is called overtwisted disc. Note that any overtwisted
disc has a neighborhood foliated by overtwisted discs. Indeed the contact structure
in a neighborhood of an overtwisted disc can be given by the normal form cosrdz +
r sinrdφ, where r,φ,z are cylindrical coordinates in R3 and the overtwisted disc is
given in these coordinates as {z = 0,r ≤ π}. One then observes that the vector
ﬁeld ∂
∂z is contact and hence all parallel discs {z =c,r≤π} are overtwisted.
Non-overtwisted contact structures are called tight. Bennequin proved in [ 16]
that the standard contact structure on R3 (orS3) is tight. More generally, (weakly)
symplectically ﬁllable contact structures are always tight [ 84, 43]. The sphere S3
admits a unique tight positive contact structure, the standard one [ 44].
Overtwisted contact structures exhibit remarkable ﬂexibility: their classiﬁca-
tion up to isotopy coincides with their homotopical classiﬁcation as plane ﬁelds.
More precisely, overtwisted contact structures satisfy the following h-principle.
Theorem 7.18 (classiﬁcation of overtwisted contact structures [ 41]).
(a) Any oriented plane ﬁeld on a closed oriented 3-manifold M is homotopic
to a positive contact structure. This contact structure is unique up to isotopy.
(b) Let ξ0 be an overtwisted contact structure on a closed connected 3-manifold
M and D⊂ (M,ξ ) be an overtwisted disc. Let Contot(M;ξ0) and Distr(M;ξ0)
denote the spaces of overtwisted contact structures resp. tangent plane ﬁelds equal
to ξ0 onOpD. Then the inclusion
Contot(M;ξ0)↪→ Distr(M;ξ0)
is a weak homotopy equivalence.
Parts (a) and (b) also hold in relative form for contact structures prescribed
near a compact set A⊂M\D.
The existence statement in part (a) of the theorem was proved by Lutz [ 126]
and Martinet [128]. Theorem 7.18 implies the following h-principle for Legendrian
knots in overtwisted contact manifolds.
Theorem 7.19 (Dymara [ 39], Eliashberg–Fraser [48]). Let (M,ξ ) be a closed
connected overtwisted contact 3-manifold, and D⊂M an overtwisted disc.
(a) Any formal Legendrian knot (f,F s) in M is formally Legendrian isotopic
to a genuine Legendrian embedding ~f :S1 ↪→M\D.
(b) Let (ft,F s
t ), s,t ∈ [0, 1], be a formal Legendrian isotopy in M connecting
two genuine Legendrian embeddings f0,f 1 : S1 ↪→ M\D. Then there exists a
Legendrian isotopy ~ft : S1 ↪→ M\D connecting ~f0 = f0 and ~f1 = f1 which is
homotopic to (ft,F s
t ) through formal Legendrian isotopies with ﬁxed endpoints.
Proof. (a) After a smooth isotopy we may assume that L :=f(S1)⊂M\D.
The homotopy F 1−t, t∈ [0, 1], can be extended to a homotopy ξt, t∈ [0, 1], of
plane ﬁelds along L connecting ξ0 = ξ|L with a plane ﬁeld ξ1 tangent to L. This
homotopy can be extended to a homotopy of contact structures onOpL. Applying
the relative form of Theorem 7.18 (a) it can be further extended to a homotopy of

142 7. THE h-PRINCIPLES
contact structures ξt on the whole manifold M with ξ0 =ξ and ξOpD =ξ. Hence,
by Gray’s Stability Theorem 6.23 there exists a diﬀeotopy ht :M→M, t∈ [0, 1],
with h0 = Id and ht|OpD = Id such that ( ht)∗ξ = ξt. Then the Legendrian
embedding h1◦f : Λ ↪→ (M,ξ ) is connected to ( f,F s) by the formal Legendrian
isotopy (ft =ht◦f, Fs
t =dht◦Fs(1−t)) in M\D.
Part (b) can be proven similarly, using Theorem 7.18 (b). Again, after a smooth
isotopy with ﬁxed endpoints we may assume that ft(S1)⊂M\D for all t∈ [0, 1].
Arguing as in (a), we can construct a 2-parameter family of contact structures
ξt,u, t,u ∈ [0, 1], such that ξt,0 = ξ0,u = ξ1,u = ξ. Gray’s Theorem 6.23 yields
a 2-parameter family of diﬀeomorphisms ht,u such that ht,0 = h0,u = h1,u = Id,
and h∗
t,uξ = ξt,u for all t,u ∈ [0, 1]. Then the Legendrian isotopy ~ft = ht,1◦ft :
Λ↪→ (M,ξ ) connects f0 andf1 and is homotopic to the formal Legendrian isotopy
(ft,F s
t ) via the path of formal Legendrian isotopies ( ft,u =ht,u◦ft, Fs
t,u =dht,u◦
Fs(1−u)
t ). □
Remark 7.20. Let us point out that, in contrast to most other h-principles
in this chapter, the Legendrian embeddings in Theorem 7.19 cannot in general be
chosen C0-close to the original smooth embeddings. The reason is that the proof
uses an overtwisted disc in an essential way and the original knots may be far from
such a disc.
7.7. Murphy’s h-principle for loose Legendrian embeddings
While in general the existence of a formal Legendrian isotopy between Legen-
drian embeddings is far from being suﬃcient for the existence of a genuine Legen-
drian isotopy (see e.g. [ 31, 40]), it turns out that there are classes of Legendrian
embeddings for which one has an h-principle: the formal condition is suﬃcient for
the existence of a Legendrian isotopy.
We have already encountered this phenomenon in Section 7.6 for Legendrian
knots in overtwisted contact 3-manifolds. It turns out that in any contact mani-
fold of dimension ≥ 5 there exists a class of Legendrian knots, called loose, which
satisfy the h-principle: any Legendrian knot Λ can be C0-approximated by a loose
Legendrian knot Λ′ in the same formal Legendrian isotopy class, and any two loose
Legendrian knots which are formally Legendrian isotopic can be connected by a
genuine Legendrian isotopy. This phenomenon was discovered by Emmy Murphy
in [143].
Remark 7.21. In [48] a Legendrian knot in a 3-dimensional contact manifold
is called loose if its complement is overtwisted. As we will see below, the higher
dimensional loose knots considered in this section exhibit a lot of similarity with
loose knots in dimension 3. However, to avoid any confusion, in this book we will
apply the term “loose” only in the sense deﬁned in this section.
In order to deﬁne loose Legendrian knots we need to describe a local model.
Throughout this section we assume n≥ 2.
Consider ﬁrst a Legendrian arcλ0 in the standard contact space (R3,dz−p1dq1)
with front projection as shown in Figure 7.3, for some a > 0. Suppose that the
slopes at the self-intersection point are±1 and the slope is everywhere in the interval
[−1, 1], so the Legendrian arc λ0 is contained in the box
Qa :={|q1|,|p1|≤ 1,|z|≤ a}

7.7. MURPHY’S h-PRINCIPLE FOR LOOSE LEGENDRIAN EMBEDDINGS 143
a
−a
1−1
z
q1
Figure 7.3. Front of the Legendrian arc λ0.
2b
< 2a
Figure 7.4. Front of the Legendrian solid cylinder Λ 0.
and∂λ0⊂∂Qa. Consider now the standard contact space (R2n+1,dz−∑n
i=1pidqi),
which we view as the product of the contact space (R3,dz−p1dq1) and the Liouville
space ( R2n−2,−
n∑
i=2
pidqi). We set q′ := (q2,...,q n} and p′ := (p2,...,p n). For
b,c> 0 we deﬁne
Pbc :={|q′|≤ b,|p′|≤ c}⊂ R2n−2,
Rabc :=Qa×Pbc ={|q1|,|p1|≤ 1,|z|≤ a,|q′|≤ b,|p′|≤ c}.
Let the Legendrian solid cylinder Λ 0⊂ (R2n+1,dz−∑n
i=1pidqi) be the product of
λ0⊂ R3 with the Lagrangian disc {p′ = 0,|q′|≤ b}⊂ R2n−2. Note that Λ 0⊂Rabc
and ∂Λ0⊂ ∂Rabc. The front of Λ 0 is obtained by translating the front of λ0 in
the q′-directions, see Figure 7.4. The pair ( Rabc, Λ0) is called a standard loose
Legendrian chart if
a<bc.
Given any contact manifold ( M2n+1,ξ ), a Legendrian submanifold Λ ⊂ M with
connected components Λ 1,..., Λk is called loose if there exist Darboux charts
U1,...,U k ⊂ M such that Λ i∩Uj = ∅ for i⁄= j and each pair ( Ui, Λi∩Ui),
i = 1,...,k , is isomorphic to a standard loose Legendrian chart ( Rabc, Λ0).
Given a closed subset A⊂M, we say that a Legendrian submanifold Λ⊂M is
loose relative to A if Λ\A is loose in M\A. A Legendrian embedding f : Λ↪→M
is called loose if its image is a loose Legendrian submanifold.
Remark 7.22. (1) Let us stress the point that a link consisting of loose Leg-
endrian knots is not necessarily a loose Legendrian link.

144 7. THE h-PRINCIPLES
Figure 7.5. Shrinking a standard loose Legendrian chart (picture
is courtesy of E. Murphy).
(2) By the contact isotopy extension theorem (Proposition 6.24), looseness is
preserved under Legendrian isotopies within a ﬁxed contact manifold. (Note, how-
ever, that if Λ t⊂ (M,ξt), t∈ [0, 1], is a family of Legendrian knots for varying
contact structures and M is not closed, then looseness of Λ 0 need not imply loose-
ness of Λ 1). Since the model Λ 0 above can be extended to a Legendrian disc in
standard R2n−1, and any two Legendrian discs are isotopic (shrink the ﬁrst one to a
neighborhood of a point, isotope it to a neighborhood of a point in the second one,
and expand again), it follows that any Legendrian disc is loose . More precisely, for
any closed Legendrian n-discD⊂ (M2n+1,ξ ),n≥ 2, its interior D\∂D is loose in
(M\∂D,ξ ).
(3) By rescaling q′ and p′ with inverse factors one can always achieve c = 1 in
the deﬁnition of a standard loose Legendrian chart. However, the inequality a<bc
is absolutely crucial in the deﬁnition. Indeed, it easily follows from Gromov’s
isocontact embedding theorem [ 83, 52] that around any point in any Legendrian
submanifold Λ one can ﬁnd a Darboux neighborhoodU such that the pair (U, Λ∩U)
is isomorphic to (R1b1, Λ0) for some suﬃciently small b> 0.
(4) Figure 7.5 taken from [ 143] shows that the deﬁnition of looseness does
not depend on the exact choice of the standard loose Legendrian chart ( Rabc, Λ0):
Given a standard loose Legendrian chart with c = 1, the condition a<b allows us
to shrink its front in the q′-directions, keeping it ﬁxed near the boundary and with
all partial derivatives in [−1, 1] (so the deformation remains in the Darboux chart
Rab1), to another standard loose Legendrian chart ( Ra′b′1, Λ′
0) with b′≥ (b−a)/2
and arbitrarily small a′ > 0. Moreover, we can arbitrarily prescribe the shape of
the cross section λ′
0 of Λ′
0 in this process. So if a Legendrian submanifold is loose
for some model (Rabc, Λ0), then it is also loose for any other model. In particular,
ﬁxing b,c we can make a arbitrarily small, and we can create arbitrarily many
disjoint standard loose Legendrian charts.
Proposition 7.23 ([143]). The stabilization construction in Proposition 7.12
withk = 0 makes any Legendrian embedding in dimension≥ 5 loose without chang-
ing its formal Legendrian isotopy class.
Proof. Let us recall the construction in Proposition 7.12. Given a Leg-
endrian embedding f0 : Λ ↪→ M we choose a Darboux chart with coordinates

7.7. MURPHY’S h-PRINCIPLE FOR LOOSE LEGENDRIAN EMBEDDINGS 145
Figure 7.6. A standard loose Legendrian chart appears in the
stabilization procedure.
(q1,...,q n,p 1,...,p n,z ) in which the front of f0(Λ) consists of two branches {z =
±q3/2
1 } joined along the singular locus {z = q1 = 0}, see Figure 7.6. Deform the
lower branch to the graph of a function φ(q) which is bigger than q3/2
1 over a do-
mainN⊂ Rn of Euler characteristic 0 (e.g. diﬀeomorphic to an annulusDn−1×S1)
disjoint from the singular locus. Performing this construction suﬃciently close to
the singular locus, we can keep the values and the diﬀerential of the function φ
arbitrarily small. Then the deformation is localized within the chosen Darboux
neighborhood, and Figure 7.6 shows that the stablilized Legendrian embedding
f1 : Λ↪→M is loose.
To show that the stabilized Legendrian embedding f1 is formally Legendrian
isotopic to the original f0 we reproduce the argument from [ 143]: Since χ(N) = 0
there exists a nowhere vanishing vector ﬁeld v on N which agrees with∇(φ−q
3
2
1 )
near∂N . Linearly interpolating the p-coordinate off1 from∇φ(q) to~v(q) =v(q)+
∇q
3
2
1 (keeping the ( q,z )-coordinates ﬁxed), then pushing the z-coordinate down
to−q3/2
1 (keeping (q,p ) ﬁxed), and ﬁnally linearly interpolating ~v(q) to −∇q3/2
1
(keeping (q,z ) ﬁxed) deﬁnes a smooth isotopy ft betweenf1 and f0. On the other
hand, the graphs of the functions tφ deﬁne a Legendrian regular homotopy from
f0 to f1, so their diﬀerentials give a path of Legendrian monomorphisms Ft from
F0 =df0 to F1 =df1. Now note that over the region N all the dft and Ft project
as the identity onto the q-plane, so linearly connecting dft and Ft yields a path of

146 7. THE h-PRINCIPLES
monomorphisms Fs
t , s∈ [0, 1], and hence the desired formal Legendrian isotopy
(ft,F s
t ) from f0 to f1. □
Remark 7.24. Let us stress the point that in dimension 3 any domain N⊂ R
has positive Euler characteristic, and hence the above stabilization construction
never preserves the formal isotopy class of the Legendrian embedding
Now we can state the main result from [143]. Note that part (a) directly follows
from Proposition 7.23 and Theorem 7.16.
Theorem 7.25 (Murphy’s h-principle for loose embeddings [ 143]).
Let (M,ξ ) be a contact manifold of dimension 2n + 1 ≥ 5 and Λ an n-
dimensional manifold.
(a) Any formal Legendrian embedding (f : Λ ↪→ M, Fs : T Λ→ TM ) can be
C0-approximated by a loose Legendrian embedding ~f : Λ↪→M formally Legendrian
isotopic to (f,F s).
(b) Any smooth isotopy ft : Λ ↪→ M, t ∈ [0, 1], which begins with a loose
Legendrian embeddingf0 can be C0-approximated by a Legendrian isotopy starting
at f0.
(c) Let (ft,F s
t ),s,t∈ [0, 1], be a formal Legendrian isotopy connecting two loose
Legendrian knots f0 and f1. Then there exists a Legendrian isotopy ~ft connecting
~f0 =f0 and ~f1 =f1 which is C0-close to ft and is homotopic to the formal isotopy
(ft,F s
t ) through formal isotopies with ﬁxed endpoints.
Theorem 7.25 also holds in relative form. In particular, if in case (c) the formal
Legendrian isotopy is genuine on a neighborhood of a closed subset A⊂ Λ and
the Legendrian knots f0 and f1 are loose relative to A, then the isotopy ~ft can be
chosen equal to ft overOpA.
7.8. Directed immersions and embeddings
In this section we formulate Gromov’s h-principle for directed immersions and
embeddings and discuss its applications, see [ 84, Section 2.4] and [ 52, Chapter
19]. Given an m-dimensional real vector space V and an integer k≤m we denote
by Gk(V ) the Grassmannian of its k-dimensional linear subspaces. A subset A⊂
Gk(V ) is called ample if for any L∈ A and any S∈ Gk−1(L) the convex hull of
each component of the set
{v∈V | span(S,v )∈A}
coincides with the whole space V .
More globally, given an m-dimensional manifold M we denote by Gk(M) the
bundle ⋃
x∈MGk(TxM) of tangent k-subspaces. A subset A⊂ Gk(M) is called
ample if it is ample ﬁberwise.
Example 7.26. (a) Let Rk =Rk(Cn)⊂ Gk(Cn), k≤ n, be the subset of
totally real subspaces. Then Rk is ample.
(b) LetV = Cn× R andRk
CR =Rk
CR(V )⊂Gk(V ),k≤n, be the subset which
consists of k-dimensional subspaces which project non-singularly onto totally real
subspaces of Cn. Then Rk
CR is ample.
(c) Let V be a symplectic vector space. Then the set of Lagrangian subspaces
is not ample, and neither is the (open) set of symplectic subspaces of some given
dimension.

7.8. DIRECTED IMMERSIONS AND EMBEDDINGS 147
One can also consider global versions of the above examples. Namely, if M is
an almost complex manifold, then one can consider the subbundle
Rk(M) =
⋃
x∈M
Rk(TxM)⊂Gk(M).
Next consider an almost CR manifold (M,ξ,J ), i.e., an odd-dimensional manifold
equipped with a hyperplane distribution ξ and a complex structure on ξ. Suppose
thatM is also equipped with a Riemannian metric. Then we obtain an orthogonal
splitting TM =ξ× R and thus a subbundle
Rk
CR(M) =
⋃
x∈M
Rk
CR(TxM)⊂Gk(M).
Given A⊂ Gk(M) and a k-dimensional manifold P , an immersion or embedding
f :P→M is calledA-directedif for eachp∈P we havedf(TpP )∈A. A monomor-
phism F :TP →TM is called A-directed if for each p∈P we have F (TpP )∈A.
For instance, if M is an almost complex manifold then totally real immersions
P → M of a k-dimensional manifold P are exactly the Rk(M)-directed immer-
sions. Given a Riemannian CR manifold M we callRk
CR(M)-directed immersions
CR totally real (and similarly for embeddings).
Given a subset A⊂Gk(M)× [0, 1] we set At :=A∩
(
Gk(M)×{t}
)
, t∈ [0, 1].
We callA⊂Gk(M)× [0, 1] ample if At is ample for each t∈ [0, 1].
Theorem 7.27 (h-principle for directed immersions [ 52, Theorem 18.4.1]) .
LetA⊂Gk(M) be an open ample set. Then the inclusion
ImmA−dir(P,M )↪→ MonA−dir(TP,TM )
ofA-directed immersions intoA-directed monomorphisms is a weak homotopy equiv-
alence. In particular, we have:
(a) Given any continuous map f :P→M covered by an A-directed monomor-
phism F :TP →TM , there exists a C0-small homotopy ft :P→M covered by a
homotopy of A-directed monomorphismsFt :TP →TM such that f0 =f,F0 =F ,
f1 is an A-directed immersion, and df1 =F1.
(b) If the diﬀerentials of two A-directed immersionsf0,f 1 :P→M are homo-
topic as A-directed monomorphisms, then there exists an A-directed regular homo-
topy C0-close to the given homotopy connecting f0 and f1.
The statement also holds in relative form ﬁxed on a neighborhood OpB of a
closed subset B⊂P .
As a special case, we obtain the followingh-principle for totally real immersions.
In this book it will only be used, via Theorem 7.38 in the next section, in the proof of
Theorem 8.11 which is a special case of the Gromov–Landweber theorem [82, 120].
Corollary 7.28 (h-principle for totally real immersions [ 84, 52]).
Let (V,J ) be an almost complex manifold of dimension 2n, and L a manifold
of dimension k≤n. Then the inclusion
Immreal(L,V )↪→ Monreal(TL,TV )
of totally real immersions into totally real monomorphisms is a weak homotopy
equivalence. In particular, any continuous map f :L→V covered by a totally real
monomorphism F : TL → TV is homotopic to a C0-close totally real immersion
g :L→V such that dg and F are homotopic through totally real monomorphisms
TL→ TV . If f is already a totally real immersion on a neighborhood OpB of a

148 7. THE h-PRINCIPLES
closed subset B⊂L and F =df on TLOpB, then the homotopy ft can be chosen
ﬁxed onOpB.
Directed embeddings. Remarkably, directed embeddings in the case of
an open ample set A also satisfy an h-principle. To formulate this, we introduce
the following terminology analogous to that in Section 7.3. A formal A-directed
embedding ofP intoM is a pair (f,F s), where f :P ↪→M is a smooth embedding
and Fs :TP →TM is a homotopy of monomorphisms over f starting at F 0 =df
and ending at an A-directed monomorphism F 1 : TP → TM covering f. Then
everyA-directed embeddingf gives rise to a formalA-directed embedding (f,F s =
df).
Theorem 7.29 (h-principle for directed embeddings [ 52, Theorem 19.4.1]) .
LetA⊂Gk(M) be an open ample set. Then the inclusion
EmbA−dir(P,M )↪→ Monemb
A−dir(TP,TM )
of A-directed embeddings into formal A-directed embeddings is a weak homotopy
equivalence. In particular, we have:
(a) Any formal A-directed embedding (f0,F s
0 ) of P into M is connected to a
genuine A-directed embeddingf1 : P ↪→ M by a path of formal A-directed embed-
dings (ft,F s
t ) such that the ft areC0-close to f0.
(b) Let A⊂ Gk(M)× [0, 1] be an open ample set. Let f0,f 1 : P ↪→ M be an
A0-directed and anA1-directed embedding connected by a path of formalAt-directed
embeddings (ft,F s
t ). Then there exists an isotopy ~ft of At-directed embeddingsC0-
close to ft, connectingf0 and f1, which is homotopic to (ft,F s
t ) as paths of formal
At-directed embeddings with ﬁxed endpoints.
The statement also holds in relative form ﬁxed on a neighborhood OpB of a
closed subset B⊂P .
In particular, we have the following special cases of this h-principle.
Corollary 7.30 (h-principle for totally real embeddings [ 84, 52]).
Let (V,J ) be an almost complex manifold of dimension 2n, and L be a manifold
of dimension k≤n. Then the inclusion
Embreal(L,V )↪→ Monemb
real (TL,TV )
of totally real embeddings into formal totally real embeddings is a weak homotopy
equivalence. In particular, we have:
(a) Any formal totally real embedding (f0,F s
0 ) ofL intoV is connected to a gen-
uine totally real embedding f1 :L↪→V by a path of formal totally real embeddings
(ft,F s
t ) such that the ft areC0-close to f0.
(b) Let Jt be a family of almost complex structures on V . Let f0,f 1 : L ↪→ V
be a J0-resp.J1-totally real embedding connected by a path of formal Jt-totally real
embeddings (ft,F s
t ). Then there exists an isotopy ~ft of Jt-totally real embeddings
C0-close to ft, connecting f0 and f1, which is homotopic to (ft,F s
t ) as paths of
formal Jt-totally real embeddings with ﬁxed endpoints.
The statement also holds in relative form ﬁxed on a neighborhood OpB of a
closed subset B⊂L.
Corollary 7.31. Let (V,J ) be an almost complex manifold and f :L↪→V a
totally real embedding. LetJt,t∈ [0, 1], be a homotopy of almost complex structures
onV withJ0 =J. Then there exists an isotopy of embeddings ft :L↪→V such that

7.8. DIRECTED IMMERSIONS AND EMBEDDINGS 149
f0 =f and ft is Jt-totally real. If the isotopy ft is already given on a neighborhood
OpB of closed subset B⊂ L such that ft|OpB is Jt-totally real, then ft can be
extended fromOpB to L.
Proof. There is a family of Js-totally real monomorphisms Fs : TL → TV
covering f with F 0 = df. Hence, we can ﬁrst apply Corollary 7.30 (a) (with the
almost complex structure J1) to ﬁnd a path of formal J1-totally real embeddings
(ft,F s
t ) connecting ( f = f0,F s) to a J1-totally real embedding ( f1,df1). After
reparametrizing Fs
t in (s,t ) we can view this as a path of formal Jt-totally real
embeddings connecting the J0-totally real embedding f0 to the J1-totally real em-
bedding f1. So we can apply Corollary 7.30 (b) to ﬁnd the desired isotopy of
Jt-totally real embeddings. □
Corollary 7.32 (h-principle for CR totally real embeddings) . Let (M,ξ,J )
be a (2n + 1)-dimensional almost CR manifold, and Λ be a manifold of dimension
k≤n. Then the inclusion
EmbCR−real(Λ,M )↪→ Monemb
CR−real(T Λ,TM )
of CR totally real embeddings into formal CR totally real embeddings is a weak
homotopy equivalence. In particular, any formal CR totally real embedding (f0,F s
0 )
of Λ into M is connected to a genuine CR totally real embedding f1 : Λ↪→M by a
path of formal CR totally real embeddings (ft,F s
t ) such that the ft areC0-close to
f0.
The statement also holds in relative form ﬁxed on a neighborhood OpB of a
closed subset B⊂ Λ.
We ﬁnish this section with an analogue of Corollary 7.28 for so-called totally
real submersions (also called complex submersions of real manifolds, see [ 120]).
This result will only be needed for one of the cases of Theorem 8.45.
A linear map A :L→V between a real vector space L and a complex vector
spaceV is called a totally real epimorphism if its complexiﬁcation AC :L⊗ C→V
is surjective. Similarly, a smooth map f : L → V of a real manifold L to an
almost complex manifold (V,J ) is called a totally real submersion if its diﬀerential
TL → TV is a ﬁberwise totally real epimorphism. A word of caution: a totally
real submersion need neither be a submersion, nor does its image have to be totally
real.
Corollary 7.33 (h-principle for totally real submersions) .
Let (V,J ) be an almost complex manifold of dimension 2n, and L a manifold
of dimension m≥n. Then the inclusion
Subreal(L,V )↪→ Epireal(TL,TV )
of totally real submersions into totally real epimorphisms is a weak homotopy equiv-
alence. In particular, any continuous map f : L→ V covered by a totally real
epimorphism F : TL→ TV is homotopic to a totally real submersion g : L→ V
such that dg and F are homotopic through totally real epimorphisms TL → TV .
If f is already a totally real submersion on a neighborhood OpB of a closed subset
B⊂L andF =df onTL|OpB, then the homotopy ft can be chosen ﬁxed onOpB.
Proof. It is suﬃcient to prove an extension statement from a neighborhood
of the boundary of a disc to the disc itself. This can be reduced to Corollary 7.28
by suspending the map f to a map ˆf :D→V× Cm−n and suspending the totally

150 7. THE h-PRINCIPLES
real epimorphismF to a totally real isomorphism ˆF :TD→TV× Cm−n, and then
projecting the constructed totally real immersion to V× Cm−n back to V . □
7.9. Discs attached to J-convex boundaries
Theorem 7.34 below, which is a combination of h-principles discussed earlier in
this chapter, will play an important role in proving the main results of this book.
Let (V,J ) be an almost complex manifold and W⊂V a domain with smooth
boundary ∂W . Let L be a (possibly non-compact) manifold with boundary. Let
f : L ↪→ V \ IntW be an embedding with f(∂L)⊃ ∂W , f(L)∩∂W = f(∂L),
and which is transverse to ∂W along ∂L. We say in this case that f transversely
attaches L to W along ∂L. We recall that f attaches L to W J-orthogonally if,
in addition, Jdf(TL|∂L)⊂ T (∂W ). Note that this implies that df(∂L) is tangent
to the distribution ξ = T (∂W )∩JT (∂W ). In particular, if ∂W is J-convex then
f(∂L) is an isotropic submanifold for the contact structure ξ.
Theorem 7.34. Suppose that (V,J ) is an almost complex manifold of real
dimension 2n, and W⊂V is a domain with smooth J-convex boundary. Suppose
that an embedding f : Dk ↪→ V , k ≤ n, transversely attaches Dk to W along
∂Dk. If k = n = 2 we assume, in addition, that the induced contact structure on
∂W is overtwisted. Then there exists an isotopy ft : Dk ↪→ V, t∈ [0, 1], through
embeddings transversely attaching Dk to W , such that f0 =f and f1 is totally real
and J-orthogonal to ∂W . Moreover, in the case k = n > 2 we can arrange that
the Legendrian embedding f1|∂Dk : ∂Dk ↪→ ∂W is loose, while for n = 2 we can
arrange that the complement ∂W\ft(∂D2) is overtwisted for all t∈ [0, 1].
The proof uses the following homotopical lemma.
Lemma 7.35. Consider f : Dk ↪→ V as in Theorem 7.34. Then there exists
a homotopy of monomorphisms Ft : TDk→ TV , t∈ [0, 1], covering f such that
F0 =df, F1 is totally real and, in addition,
(a) F1(T∂Dk)⊂ξ,
(b) Ft(T∂Dk)⊂T∂W for all t∈ [0, 1].
Proof. We write D = Dk. Let us ﬁx an outward normal vector ﬁeld r to
∂D in D and an inward pointing vector ﬁeld n along ∂W such that Jn∈ T∂W .
After an isotopy of f we may assume that df(r) = n along ∂D. Consider the
bundle Mon(TD,f ∗TV ) → D and its subbundle Mon real(TD,f ∗TV ) of totally
real monomorphisms. Similarly, over the boundary ∂D we have the bundles
Monreal(T∂D,f ∗ξ)⊂ Mon(T∂D,f ∗T∂W ).
Sending r to n deﬁnes natural inclusions
Mon(T∂D,f ∗T∂W )⊂ Mon(TD,TV )|∂D and
Monreal(T∂D,f ∗ξ)⊂ Monreal(TD,TV )|∂D.
Note that df deﬁnes a section in Mon( TD,TV ) which restricts to a section in
Mon(T∂D,f ∗T∂W ) over ∂D.
After picking a metric and orthogonalization, we may assume that the ﬁber of
the bundle Mon(TD,TV ) is the Stiefel manifold V2n,k of orthogonal k-frames in
R2n (see Appendix A.2) and its structure group isO(2n). Similarly, we may assume
that the ﬁber of the bundle Monreal(TD,TV ) is the Stiefel manifoldV C
n,k of unitary

7.9. DISCS ATTACHED TO J-CONVEX BOUNDARIES 151
k-frames in Cn and its structure group is U(n), and similarly for the bundles over
∂D.
The U(n− 1)-bundle Mon real(T∂D,f ∗ξ)→ Sk−1 is obtained by gluing two
trivial bundles via a map g : Sk−2→ U(n− 1). Since the bundle extends over D
as the U(n)-bundle Monreal(TD,TV ), g lies in the kernel of the map πk−2U(n−
1)→ πk−2U(n), which is trivial by Corollary A.10. Thus we obtain compatible
trivializations of all the bundles
Monreal(TD,f ∗TV )∼=D×V C
n,k⊂ Mon(TD,f ∗TV )∼=D×V2n,k,
Monreal(T∂D,f ∗ξ)∼=∂D×V C
n−1,k−1⊂ Mon(T∂D,f ∗T∂W )∼=∂D×V2n−1,k−1.
With these trivializations, df deﬁnes a map (Dk,∂Dk)→ (V2n,k,V 2n−1,k−1) which
we want to deform to a map ( Dk,∂Dk)→ (V C
n,k,V C
n−1,k−1). This is possible by
Corollary A.8 (a) which asserts πk(V2n,k,V 2n−1,k−1) = 0 for k≤ 2n− 2, i.e., in
particular for k≤n and n≥ 2. □
Proof of Theorem 7.34. We writeD =Dk. Let Ft be the homotopy from
Lemma 7.35. The isotopy ft is constructed in two steps.
Step 1. The restriction Ft|T(∂D) gives us a homotopy of monomorphisms
~Ft : T (∂D)→ T (∂W ) covering f|∂D such that ~F0 = df|T∂D and ~F1 : T (∂D)→ ξ
is totally real. Hence, we can apply Theorem 7.16 if n >2, and Theorem 7.19 if
n = 2, to ﬁnd an isotopy gt :∂D↪→∂W such that
(α) g0 =f|∂D,
(β) g1 is isotropic, and
(γ) the path of monomorphisms dgt : T (∂D)→ T (∂W ), t∈ [0, 1], is homo-
topic to ~Ft in the class of paths of monomorphisms beginning at dg0 and
ending at a totally real monomorphism T (∂D)→ξ.
When n >2 Theorem 7.16 allows us to make the isotopy gt C0-small and using
Theorem 7.25 we can arrangeg1(∂D) to be loose, while whenn = 2 the complement
∂W\gt(∂D) can be made overtwisted by Theorem 7.19.
We extend the isotopy gt to an isotopy ft : D ↪→ V \ IntW of smooth em-
beddings transversely attached to W such that f0 = f. Note that any subspace
of TpV , p∈ ∂W , which is transverse to ∂W and intersects ξp⊂ Tp∂W along a
totally real subspace is totally real itself. Hence, we can further deform the disc
f1(D) near f1(∂D) through totally real discs, keeping the boundary ﬁxed, to make
it J-orthogonally attached to ∂W .
Step 2. We claim that there exists a homotopy of monomorphisms Gt :
TD→TV , t∈ [0, 1] such that
a) G0 =df1 :TD→TV ,
b) G1 is totally real, and
c) Gt =df1 on TD|∂D for all t∈ [0, 1].
Indeed, consider ﬁrst the homotopy ~Gt :TD→TV ,
~Gt :=
{
df1−2t, t ∈ [0, 1
2];
F2t−1, t ∈ ( 1
2, 1].
The homotopy ~Gt satisﬁes the above conditions a) and b), but not c). However,
in view of property ( γ) the path ~Gt|T∂D is homotopic through paths with ﬁxed
ends to a path of totally real monomorphisms, and hence the homotopy ~Gt can

152 7. THE h-PRINCIPLES
t
t
s
s
Γs
t
dg1
dg1
dg0
dgt dg1
Monreal(T∂D, ξ)
Monreal(T∂D, ξ)
~Gt
⏐
⏐
T∂D
Ft
⏐
⏐
T∂D
Figure 7.7. Construction of the family of monomorphisms Γ s
t.
be modiﬁed to a homotopy Gt satisfying condition c) as well. More explicitly, ( γ)
allows us to pick a continuous family of monomorphisms Γ s
t : T (∂D)→ T (∂W ),
s,t ∈ [0, 1], such that Γ 0
t = ~Gt|T∂D , Γ 1
t = Γs
0 = df1|T∂D , and Γs
1 : T (∂D)→ ξ is
totally real for all s∈ [0, 1], see Figure 7.7.
We extend Γs
t from T (∂D) to TD∂D sending the outward normal r along ∂D
to the inward normal n along ∂W , so that it satisﬁes Γ 0
t = ~Gt, Γ1
t = Γs
0 =df1, and
Γs
1 is J-orthogonal and totally real along ∂D. After rescaling in the unit disc D
we may assume that ~Gt(x) is independent of the radius for x∈D with|x|≥ 1/2.
Then the desired homotopy Gt :TD→TV can be deﬁned by
Gt(x) :=
{~Gt(2x), |x|∈ [0, 1
2];
Γ2|x|−1
t (x), |x|∈ ( 1
2, 1].
It remains to apply Gromov’sh-principle for totally real embeddings, Corollary 7.30
(a). It provides an isotopy of embeddings ft :D→V\ IntW ,t∈ [1, 2], ﬁxed along
∂D together with its diﬀerential, such that f2 :D→V\ IntW is totally real and
J-orthogonal to ∂W . Finally, note that the isotopy provided by Corollary 7.30 (a)
can also be chosen C0-small. This concludes the proof of Theorem 7.34. □
In Section 14.3 we will need the following 1-parametric version of Theorem 7.34
in the ﬂexible situation.
Theorem 7.36. LetJt,t∈ [0, 1], be a family of almost complex structures on a
2n-dimensional manifold V . Let W⊂V be a domain with smooth boundary which
is Jt-convex for all t∈ [0, 1]. Suppose that k≤ n. Let ft : Dk ↪→ V \ IntW ,
t∈ [0, 1], be an isotopy of embeddings transversely attached to ∂W along ∂Dk.
Suppose that for i = 0, 1 the embedding fi is Ji-totally real and Ji-orthogonally
attached to ∂W along ∂Dk. Suppose that either k < n or k = n > 2 and the

7.9. DISCS ATTACHED TO J-CONVEX BOUNDARIES 153
Legendrian embeddings fi|∂D, i = 0, 1 are loose. Then there exists a 2-parameter
family of embeddings fs
t :Dk ↪→V\W with the following properties:
• fs
t is transversely attached to W along ∂Dk and C0-close to ft for all
t,s∈ [0, 1];
• f0
t =ft for all t∈ [0, 1] and fs
0 =f0, fs
1 =f1 for all s∈ [0, 1];
• f1
t is Jt-totally real and Jt-orthogonally attached to ∂W along ∂Dk for
all t∈ [0, 1].
The proof uses the following homotopical lemma.
Lemma 7.37. Considerft :Dk ↪→V\IntW as in Theorem 7.36, where we allow
the critical case k≤n. Then there exists a 2-parameter family of monomorphisms
Fs
t : TD → TV , t,s ∈ [0, 1], covering ft such that F 0
t = dft, Fs
0 = df0, Fs
1 = df1,
F 1
t is totally real and, in addition,
(a) F 1
t (T∂D )⊂ξ, and
(b) Fs
t (T∂D )⊂T∂W .
Proof. As shown in the proof of Lemma 7.35, we can trivialize the relevant
bundles of monomorphisms overD :=Dk and∂D. So Ft :=dft deﬁnes a homotopy
of maps
Ft : (D,∂D )→ (V2n,k,V 2n−1,k−1), t ∈ [0, 1]
with endpoints
F0,F 1 : (D,∂D )→ (V C
n,k,V C
n−1,k−1)
which we want to deform into ( V C
n,k,V C
n−1,k−1) with ﬁxed ends at t = 0, 1. By
Corollary A.8 (a) we have πk(V C
n,k,V C
n−1,k−1) = 0 for k≤ n and n≥ 2. After
contractingF0,F 1 it thus suﬃces to consider the case that F0≡F1≡v∈Vn−1,k−1
is constant. After a further deformation we may assume that Ft(0)≡ v for the
origin 0∈D and all t∈ [0, 1], and collapsing {0, 1}× D∪ [0, 1]×{ 0}⊂ [0, 1]×D
to a point p we obtain a map
¯F : (Dk+1,∂Dk+1,p )→ (V2n,k,V 2n−1,k−1,v )
which we need to contract to the point v. This is possible by Corollary A.8 (a)
because πk+1(V C
n,k,V C
n−1,k−1) = 0 provided that k + 1≤ 2n− 2. This condition is
satisﬁed if k≤n and n> 2, or if k<n and n = 2.
It remains to treat the case k = n = 2. Note that in the ﬁrst step of the
preceding argument we have chosen a contraction of F0 in π2(V C
2,2,V C
1,1) = 0. Two
such contractions diﬀer by an element in π3(V C
2,2,V C
1,1). So by varying the contrac-
tions we can change the resulting class [ ¯F ]∈ π3(V4,2,V 3,1) by adding classes in
π3(V C
2,2,V C
1,1). Since by Corollary A.8 (b) the map π3(V C
2,2,V C
1,1)→π3(V4,2,V 3,1) is
an isomorphism, we can arrange [ ¯F ] = 0 and thus conclude the proof. □
Proof of Theorem 7.36. With Lemma 7.37, the rest of the proof of The-
orem 7.36 is parallel to the proof of Theorem 7.34: First we apply either the h-
principle for subcritical isotropic embeddings, Theorem 7.11, if k<n or Murphy’s
h-principle for loose Legendrian embeddings, Theorem 7.25, if k =n >2 in order
to make ft|∂D an isotropic isotopy. Then we deform ft, as in the proof of 7.34,
to make it Jt-orthogonal to ∂W along ∂D. Finally, we apply the h-principle for
totally real embeddings, Corollary 7.30 (b), to make ft totally real. □

154 7. THE h-PRINCIPLES
Finally, in Section 8.3 we will need the following version of Theorem 7.34 in
which we remove the condition of J-convexity of the boundary, but obtain instead
ofJ-orthogonality the following weaker notion of “J-transversality”. Let us assume
that W is endowed with a Riemannian metric for which J acts as an orthogonal
operator and denote by n the unit outward normal vector to the boundary of W .
Then we say thatf attachesL toW J-transversely if n∈df(TL|∂L) anddf(TL|∂L)
is totally real. Note that this implies that f(∂L) is a CR totally real submanifold
of ∂W in the sense of Section 7.8 above.
Theorem 7.38. Suppose that (V,J ) is an almost complex manifold of dimen-
sion 2n and W ⊂ V a domain with smooth boundary (not necessarily J-convex).
Suppose that an embedding f : Dk→ V , k≤ n, transversely attaches Dk to W
along ∂Dk in V . Then there exists an isotopy ft : Dk ↪→ V, t∈ [0, 1], through
embeddingsC0-close to f and transversely attaching Dk to W , such that f0 = f
and f1 is totally real and J-transverse to ∂W .
Proof. The proof repeats the proof of Theorem 7.34, using Corollary 7.32
instead of Theorem 7.16. □

8
The Existence Theorem
In this chapter we prove Theorem 1.5 from the introduction on the existence
of Stein structures in complex dimension ⁄= 2. The proof combines the techniques
developed in earlier chapters: in Section 8.2 we use the i-convex model functions
from Chapter 4 to extend J-convex functions over discs, and in Section 8.3 we
use the h-principles from Chapter 7 to extend complex structures over discs. The
Existence Theorem 1.5, as well as an ambient version due to Gompf, is then proved
in Section 8.4.
Sections 8.5 to 8.7 contain various reﬁnements of results in the previous sections
that will not be used in the remainder of the book. In Sections 8.2 and 8.6 we
reﬁne theJ-convex surroundings from Section 8.2 and discuss some applications to
holomorphic convexity. In Section 8.7 we derive some holomorphic approximation
results due to Forstneriˇ c and Slapar. Finally, in Section 8.8 we prove a variant of
Kallin’s lemma which will be needed in Section 16.2.
8.1. Some notions from Morse theory
In this chapter we use the following notions from Morse theory; for more details
see Chapter 9.
Recall that a function φ : V → R is called Morse if all its critical points
are nondegenerate, and the (Morse) index of a critical point of φ is the maximal
dimension of a subspace on which the Hessian is negative deﬁnite. A vector ﬁeld
X is called gradient-like for φ if it satisﬁes
X·φ≥δ(|X|2 +|dφ|2)
for some δ >0, where|X| is the norm with respect to some Riemannian metric on
V and|dφ| is the dual norm. The stable manifold W−
p (with respect to X) of a
critical pointp ofφ is the set of all points converging top under the forward ﬂow of
X. The skeleton of a Morse function (with respect to X) is the union of all stable
manifolds.
By the Morse Lemma (see [ 139]), near a nondegenerate critical point p ofφ of
index k there exist coordinates ui in which φ has the form
φ(u) =φ(p)−u2
1−···− u2
k +u2
k+1··· +u2
m.
We will use the following easy consequence, as well as a reﬁnement given in Lemma
9.29 below.
Corollary 8.1. Letφ :V → R,φ′ :V′→ R be Morse functions with gradient-
like vector ﬁelds X,X′ and critical points p,p′ of the same index and value with
stable manifolds W−
p ,W−
p′ . Then there exists a diﬀeomorphism f : OpW−
p →
OpW−
p′ such that φ′ =φ◦f.
155

156 8. THE EXISTENCE THEOREM
Proof. By the Morse lemma there exists a diﬀeomorphism f :Opp→O pp′
such that φ′ =φ◦f. It extends uniquely to a diﬀeomorphism OpW−
p →O pW−
p′
with φ′ =φ◦f and mapping trajectories of X to trajectories of X′. □
A cobordism is a compact oriented manifold W with oriented boundary ∂W =
∂+W∐∂−W , where the orientation agrees with the boundary orientation for ∂+W
and is opposite to it for ∂−W . We allow one or both of ∂±W to be empty. A
Morse cobordism (W,φ ) is a cobordism W with a Morse function φ : W → R
having ∂±W = φ−1(c±) as regular level sets. We call a Morse cobordism ( W,φ )
elementary ifφ admits a gradient-like vector ﬁeldX such that no two critical points
ofφ are connected by an X-trajectory. In that case each stable manifold W−
p is an
embedded disc which we will refer to as the stable disc of p.
8.2. Surrounding stable discs
In this section we prove our two main results aboutJ-convex surroundings. The
ﬁrst one, Theorem 8.4, states that aJ-orthogonally attached totally real disc can be
surrounded byJ-convex hypersurfaces. It is a crucial ingredient in the proof of the
existence of Stein structures in Section 8.4. The second one, Theorem 8.5, states
that a stable disc of aJ-convex Morse function can be surrounded by deforming the
level sets of the given function. It is the basis for the holomorphic approximations
in Section 8.7 and for the deformations ofJ-convex functions studies in Chapter 10.
Let (V,J ) be a complex manifold, possibly with boundary.
Definition 8.2. Given a subset A⊂V and a neighborhood U⊂V of A, we
say that a J-convex hypersurface Σ ⊂ U surrounds A in U if it is the J-convex
boundary of a domain in U containing A. We say that A can be surrounded by
J-convex hypersurfaces if J-convex surrounding hypersurfaces exist in arbitrarily
small neighborhoods of A.
Example 8.3. In Section 2.7 we saw that the following sets can be surrounded
byJ-convex hypersurfaces:
(i) totally real submanifolds;
(ii) the zero section of a negative holomorphic line bundle, and hence any
properly embedded complex codimension one submanifold with negative
normal bundle.
Theorem 4.1 provides a solution of the surrounding problem for a more subtle
case: the set A ={ar2−R2≤− 1}∪{ r = 0}⊂ Cn can be surrounded by i-convex
hypersurfaces, where a> 1 and
r :=
√
x2
1 +··· +x2n +y2
k+1 +··· +y2n, R :=
√
y2
1 +··· +y2
k
for some ﬁxed k≤n and complex coordinates x1 +iy1,...,x n +iyn in Cn.
The following two main results of this section generalize this model case to
a solution of the surrounding problem for totally real discs suitably attached to
J-convex domains.
Theorem 8.4. Let (W,J ) be a complex manifold with compactJ-concave bound-
ary∂−W . Let ∆⊂W be a totally real disc J-orthogonally attached to ∂−W . Then
∂−W∪ ∆ can be surrounded by J-convex hypersurfaces. Moreover, if we are given

8.2. SURROUNDING STABLE DISCS 157
∂−W
p
∆
L
Figure 8.1. Surrounding a J-orthogonally attached totally real disc.
a totally real submanifold L⊃ ∆ of dimension dimL > dim ∆ which is also J-
orhogonally attached to ∂−W , then the surrounding hypersurface can be chosen
J-orthogonal to L, see Figure 8.1.
Theorem 8.5. Let (W,J ) be a complex manifold with compactJ-concave bound-
ary∂−W . Let φ :W→ R be aJ-convex Morse function which is constant on ∂−W
and has no critical points on ∂−W . Let p be a critical point of φ such that all
trajectories of∇φφ reach∂−W in backward time and denote by ∆⊂W the stable
disc of p. Then for any neighborhood U⊃ ∂−W∪ ∆ there exists a J-lc function
ψ :W→ R with the following properties (see Figure 8.2):
(a) ψ is equal to φ near∂−W and outside a neighborhood N⊂U of ∆, and
target equivalent to φ near ∆;
(b) ψ|N has the unique critical point p with stable disc ∆;
(c) some level set {ψ =c} surrounds∂−W∪ ∆ in U.
Moreover, there exists a homotopy ψt, t∈ [0, 1], of J-convex functions with prop-
erties (a) and (b) connecting ψ0 = φ and ψ1 = ψ. If we are given a totally real
manifold L⊃ ∆ of dimension dimL >dim ∆ which is J-orthogonal to all regular
level sets of φ, then the same property can be arranged for the functions ψt.
Remark 8.6. We will see in Section 10.2 that theJ-orthogonality condition in
Theorem 8.4 can be replaced by the weaker condition that ∂∆⊂∂−W is isotropic
(i.e., tangent to the ﬁeld of complex tangencies). The same remark applies to
Theorem 8.23 and Corollary 8.26 below.
Theorem 8.5 will be proved below using Corollary 4.4. Theorem 8.4 can be
proved following the same scheme using the (easier) Theorem 4.1. We have chosen
a diﬀerent approach, formally deducing Theorem 8.4 from Theorem 8.5. For this,
we need to construct a J-convex function φ which has the given disc ∆ as stable

158 8. THE EXISTENCE THEOREM
N
∆
p
ψ =φ =b
ψ =c
∂U
∂−W
Figure 8.2. Surrounding a stable disc of a J-convex function.
disc of some critical point. In particular, the gradient of φ needs to be tangent to
∆ and its regular level setsJ-orthogonal to ∆ (see Remark 2.23). The construction
is based on the following lemma which is also of independent interest.
Lemma 8.7. Let (V,J ) be a complex manifold, L⊂ V a compact totally real
submanifold (possibly with boundary), φ : V → R a smooth function, and X a
nowhere vanishing vector ﬁeld which is tangent to L and gradient-like for φ. Let
K⊂ L be a compact subset such that on OpK⊂ V the function φ is J-convex,
∇φφ =X, and L∩O pK is J-orthogonal to the level sets of φ. Then there exists
a J-convex function ~φ onOpL which agrees with φ on L∪O pK such that L is
J-orthogonal to the level sets of ~φ, and∇ ~φ
~φ =X along L.
Proof. After extending L, we may assume without loss of generality that
dimRL = dimCV =:n. After pulling back by an approximately holomorphic map
alongL provided by Proposition 5.55, it suﬃces to consider the case L =iRn⊂ Cn
andJ =i. By hypothesis, L isi-orthogonal to the level sets of φ onOpK. We can
deformφ, keeping it ﬁxed on L∪O pK, to make all its level sets i-orthogonal to L,
i.e., tangent to Rn. Then the Taylor expansion of φ at (0,y )∈L has the form
φ(x,y ) =ϑ(y) +Qy(x) +o(|x|2),
whereϑ(y) =φ(0,y ) andQy(x) is a quadratic form inx with coeﬃcients depending
on y. Let Hyϑ denote the Hessian quadratic form of ϑ at a point y. Then the
Hessian H(0,y)φ and the complex Hessian H C
(0,y)φ are given by
H(0,y)φ(x,y′) =Qy(x) +Hyϑ(y′),
H C
(0,y)φ(x,y′) =Qy(x) +Hyϑ(y′) +Qy(y′) +Hyϑ(x) =Sy(x) +Sy(y′),
whereSy(y′) =Qy(y′)+Hyϑ(y′) is the restriction ofH C
(0,y)φ toiRn. By assumption,
Sy is positive deﬁnite on a neighborhood of K in L and X is the gradient of φ|L
with respect to the metric Sy on this neighborhood. Elsewhere on L, the vector
ﬁeld X is gradient-like for φ. Let us extend the metric Sy from the neighborhood
of K to a metric ~Sy on L in such a way that X is the gradient of φ|L with respect
to the metric ~Sy. We view this metric again as a family of quadratic forms ~Sy on
Rn and deﬁne
~φ(x,y ) :=φ(x,y ) +~Sy(x)−Sy(x), (x,y )∈ Cn.
This function coincides with φ on L∪O pK. Since it agrees to ﬁrst order with φ
along L, its level sets are still i-orthogonal to L. Its complex Hessian at (0 ,y )∈L

8.2. SURROUNDING STABLE DISCS 159
is given by
H C
(0,y)~φ(x,y′) =Sy(x) +Sy(y′) +~Sy(x) +~Sy(y′)−Sy(x)−Sy(y′) = ~Sy(x) +~Sy(y′).
Hence~φ isi-convex nearL and its gradient with respect to the metricgi, ~φ coincides
with X along L. □
Remark 8.8. A similar argument can be used to prove a parametric version
of Lemma 8.7.
Corollary 8.9. Let (V,J ) be a complex manifold, L⊂ V a compact totally
real submanifold (possibly with boundary), and φ :V → R a Morse function whose
restriction to L is Morse with the same indices. Let K⊂ L be a compact subset
such that onOpK⊂V the function φ is J-convex,∇φφ is tangent to L∩O p (K),
and L∩O pK is J-orthogonal to all regular level sets of φ. Then there exists a
J-convex Morse function ~φ onOpL which agrees with φ on L∪O pK such that L
is J-orthogonal to all regular level sets of ~φ and∇ ~φ
~φ is tangent to L.
Proof. Consider a critical point p∈ L\K of index k≤ 𝓁 = dimL. Pick an
embedding f : R𝓁⊃O p 0↪→L such that
f∗φ(x1,...,x 𝓁) =−x2
1−···− x2
k + 1
2(x2
k+1 +··· +x2
𝓁).
Use Proposition 5.55 to extend f to an embedding F : Cn⊃O p 0↪→V such that
F∗J agrees with i to second order along R𝓁. Note that the gradient vector ﬁeld
∇i,ψψ of the function
ψ(z1,...,z n) =−x2
1−···− x2
k + 2(y2
1 +··· +y2
k) + 1
2(|zk+1|2 +··· +|zn|2)
with respect to the complex structure i is tangent to Rk, and hence the same holds
for the gradient ∇F∗J,ψψ with respect to the complex structure F∗J. Moreover,
Rk is i-orthogonal, and hence F∗J-orthogonal, to all regular level sets of φ. Thus
F∗ψ provides an extension of φ|L to a J-convex function on Opp whose gradient
(with respect to J) is tangent to L, and such that L is J-orthogonal to its regular
level sets. We choose such extensions near all critical points in L\K, extend the
gradient of F∗ψ to any gradient-like vector ﬁeld X for φ tangent to L, and then
apply Lemma 8.7. □
Proof of Theorem 8.4 (assuming Theorem 8.5). Pick a J-convex func-
tionφ without critical points in a tubular neighborhood of ∂−W having∂−W as a
level set such that ∆ is J-orthogonal to its level sets and tangent to ∇φφ. Using
Corollary 8.9 we can extendφ to aJ-convex Morse function on a tubular neighbor-
hood W′ of ∂−W∪ ∆ with a unique critical point p∈ ∆ of index dim ∆ and such
that∇φφ is tangent to ∆. It follows that ∆ is the stable manifold of p, so we are
in the position to apply Theorem 8.5 to the manifold W′. □
So it remains to prove Theorem 8.5. For this, let us introduce some notation
that will be used throughout the rest of this chapter. For t > 0 we denote by
Dt :={R≤t, r= 0}⊂ Rk the k-disc of radius t, and we abbreviate D =D1. For
ε> 0 we also introduce the k-handle
Hε :={R≤ 1 +ε,r≤ε}⊂ Cn
and its imaginary part Hy
ε :=Hε∩iRn. Note that for k =n we haveHy
ε =D1+ε.

160 8. THE EXISTENCE THEOREM
∂U
∂−W
{φ =c}
D ∆′
Hε Hγ
Σ
F
{ψ =c}
Figure 8.3. Implanting a model function near a stable disc.
Proof of Theorem 8.5. The strategy of the proof is to deform theJ-convex
function φ to a standard quadratic function near the disc ∆ and then implant
the family of J-convex functions from Corollary 4.4, see Figure 8.3. We split the
construction into 5 steps. Step 5 is the main step, while Steps 1-4 are preparatory.
Step 1. Recall from Lemma 2.21 that the stable disc ∆ is ωφ-isotropic. If
k < nwe extend ∆ to an n-dimensional ωφ-Lagrangian submanifold ˆ∆⊂ W . If
we were given a totally real extension L of ∆ which is J-orthogonal to the regular
level sets of φ, and hence ωφ-isotropic, then we can choose ˆ∆ such that it contains
a neighborhood of ∆ in L. Note that tangency of ∇φφ to ∆ and the Lagrangian
condition on ˆ∆ imply−dφ(Jv) = ωφ(∇φφ,v ) = 0 for all v∈Txˆ∆, x∈ ∆, so ˆ∆ is
J-orthogonal to the level sets of φ along ∆.
Step 2. Take a slightly bigger regular value c>b :=φ|∂−W such that there
are no critical values in [ b,c ] and ~W :={φ≤ c}⊂ U. Set ∆ ′ := ∆∩{φ≥ c}.
Without loss of generality we may assume thatφ(p) = 0 andc =−1. Fix any a> 1
and consider the i-convex quadratic function Q(r,R ) = ar2−R2 on the k-handle
Hε⊂ Cn.
The Morse function φ| ˆ∆ has a unique critical point of index k and value 0 and
equals b< −1 on ˆ∆∩∂−W . Hence by Corollary 8.1, for a suﬃciently small ε> 0
there exists an embedding f :Hy
ε ↪→ ˆ∆ such that f(D) = ∆′ and φ◦f =Q.
Step 3. Using Proposition 5.55, we can extend the embedding f to an
embedding F : Hε ↪→ U such that the 14-jet of the pull-back complex structure
~J = F∗J coincides with the standard complex structure i along Hy
ε . (The choice
of the order 14 will become clear in Step 5 below.) Hence, we have an estimate
(8.1) ‖~J−i‖C2≤Cr13.
This estimate implies that, after possibly shrinking ε, we may assume that both
functions φ◦F and Q are i-convex as well as ~J-convex on Hε.
Now the crucial observation is that the 1-jets of the functions F∗φ and Q
coincide along D1+ε. To see this, consider a tangent vector v∈ TzHy
ε = iRn at
z∈ D1+ε. Since F∗φ = Q on Hy
ε we have dz(F∗φ)(v) = dzQ(v). On the other

8.3. EXISTENCE OF COMPLEX STRUCTURES 161
hand,
dz(F∗φ)(iv) =dφ◦dzF (iv) =dφ
(
JdzF (v)
)
= 0,
where the second equality holds because dF is complex linear along D1+ε, and the
last equality follows from dzF (v)∈Tˆ∆ and J-orthogonality of ˆ∆ to the level sets
of φ along ∆.
Step 4. In view of the last observation, we can apply Proposition 3.26 to the
functions φ◦F and Q with the complex structure ~J and the totally real manifold
Hy
ε . It provides a ~J-convex function ~ψ onHε which coincides with φ◦F near∂Hε
and with Q on Hγ for some γ < ε. Moreover, d~ψ = d(φ◦F ) along Hy
ε , which
ensures ~J-orthogonality of Hy
ε to the levels sets of ~ψ.
Step 5. Consider now the family of functions Ψ t : Hγ→ R constructed in
Corollary 4.4. For γ suﬃciently small, estimate (8.1) implies inequality (4.1) for
the complex structure ~J, so the functions Ψ t are ~J-lc. Since Ψ t =Q =φ◦F near
∂Hγ, we can extend Ψ t◦F−1 by φ outside F (Hγ) to a family of J-lc functions
ψt :W→ R.
Since the level sets of the shape functions Ψ t are i-orthogonal, and hence
~J-orthogonal, to Hy
ε , the level sets of ψt are J-orthogonal to ~∆, and hence to
L. By construction, the functions ψt agree to ﬁrst order along ∆ with target
reparametrizations ofφ. So we can modify the ψt once more using Proposition 3.26
to make them target equivalent toφ near on a neighborhood of ∆. Then the family
ψt and the function ψ =ψ1 have the desired properties in Theorem 8.5. □
Remark 8.10. The same proofs also yield parametric versions of Theorems 8.4
and 8.5.
8.3. Existence of complex structures
In this section we prove the following result on approximation of almost complex
structure by integrable ones, which is a special case of a theorem of Gromov and
Landweber.
Theorem 8.11 (Gromov [82], Landweber [120]).
(a) Let (W,J ) be a 2n-dimensional almost complex manifold which admits an
exhausting Morse function φ without critical points of index > n. Let L be the
skeleton of φ (with respect to some gradient-like vector ﬁeld). Then J can be C0-
approximated by an the almost complex structure which coincides with J outside a
neighborhood of L and is integrable on OpL. In particular, J is homotopic to an
integrable complex structure.
(b) Let (W,J,φ ) be a 2n-dimensional almost complex Morse cobordism, where
the function φ has no critical points of index >n . Suppose that J is integrable near
∂−W . Let L be the skeleton of φ (with respect to some gradient-like vector ﬁeld).
Then J can be C0-approximated by an almost complex structure which coincides
with J onOp (∂−W ) and outside a neighborhood of L and is integrable onOp (L∪
∂−W ). In particular, J is homotopic to an integrable complex structure via a
homotopy ﬁxed on Op∂−W .
The proof is based on the following proposition.
Proposition 8.12. Let (W,J ) be an almost complex manifold of dimension 2n
with compact boundary∂−W near whichJ is integrable. Let ∆⊂W be an embedded
totally real k-disc, k≤ n, transversely attached to ∂−W along ∂∆⊂ ∂−W . Then

162 8. THE EXISTENCE THEOREM
ˆf
∂W
∂W ′
Hε
D
Uε
Figure 8.4. Holomorphically attaching a standard handle.
there exists a C0-small perturbation ~J of J which is integrable on Op (∂−W∪ ∆),
coincides with J onOp (∂−W ) and outside a neighborhood of ∆, and such that ∆
is totally real for ~J.
Proof. We use the notation introduced in Section 8.2. Namely, D stands for
the unitk-disc{R≤ 1,r = 0}⊂ Cn and we denote byD1+ε the disc{R≤ 1+ε,r =
0}⊃ D. We denote by Hε thek-handleHε ={R≤ 1 +ε,r≤ε}⊂ Cn, and by Hy
ε
its imaginary part Hε∩iRn. When k =n we haveHy
ε =D1+ε.
Pick a tubular neighborhood W′ ⊂ W of ∂−W with real analytic interior
boundary ∂+W′ such that J is integrable near W′ and the smaller disc ∆ ′ :=
∆\ IntW′ is transversely attached to W′. Pick a diﬀeomorphism f : D1+ε→ ∆
such that f(D) = ∆′. Extend f to a totally real embedding Hy
ε → W . Using
Theorem 5.53, we can ﬁnd an embedding ~f : Hy
ε ↪→ W which is C∞-close to f,
maps ∂D to ∂+W′, and is real analytic on Op (∂D)⊂ Hy
ε . In particular, ~f still
transversely attaches D to W′.
By Lemma 5.40 (after shrinking ε) we can extend ~f to an embedding ˆf :Hε ↪→
W which is biholomorphic onUε :={r≤ε, 1−ε≤R≤ 1+ε} and whose diﬀerential
is complex linear along Hy
ε , see Figure 8.4.
Thus, for ε small enough, the complex structure ˆf∗i is C0-close to J on ˆf(Hε)
and coincides with J on ˆf(Uε), where i denotes the standard complex structure on
Hε⊂ Cn. So we can deﬁne an integrable complex structure on W′∪ ˆf(Hε) by J
on W′ and by ˆf∗i on ˆf(Hε). We extend this complex structure from W′∪ ˆf(Hε)
to an almost complex structure ˆJ on the whole manifold W which is C0-close to
J and coincides with J outside a neighborhood of W′∪ˆf(Hε). By construction, ˆJ
is integrable on a neighborhood of W′∪ ~f(D) and agrees with J on W′. Finally,
pick a diﬀeomorphism g : W→ W which is C∞-close to the identity, maps ~f(D)
to f(D) = ∆′, and equals the identity near ∂−W and outside a neighborhood of
W′∪ ~f(D). Then ~J :=g∗ˆJ is the desired almost complex structure. □
Remark 8.13. A similar proof yields a parametric version of Proposition 8.12.
Combining Proposition 8.12 and Theorem 7.38, we obtain
Corollary 8.14. Let (V,J ) be an almost complex manifold of dimension 2n
with compact boundary∂−W near whichJ is integrable. Let ∆⊂V be an embedded

8.4. EXISTENCE OF STEIN STRUCTURES IN COMPLEX DIMENSION ⁄= 2 163
k-disc, k≤n, transversely attached to ∂−W along∂∆⊂∂−W . Then J can beC0-
approximated by an almost complex structure ~J which is integrable onOp (W∪ ∆),
coincides with J onOp (∂−W ) and outside a neighborhood of ∆, and for which ∆
is totally real.
Proof. Fix a neighborhood U of ∆. We ﬁrst use Theorem 7.38 to ﬁnd a C0-
small isotopy of ∆ inU through embedded discs transversely attached to∂−W to a
totally real disc ∆′. Then we apply Proposition 8.12 to ﬁnd aC0-small perturbation
J′ of J which is integrable on Op (W′∪ ∆′) and coincides with J onOpW′ and
outside U, for some slightly larger domain W′ ⊂ W . Finally, we obtain ~J by
pushing forwardJ′ under a diﬀeomorphism which is isotopic to the identity, equals
the identity near ∂−W and outside U, and maps ∆′\W′ onto ∆\W′. □
Proof of Theorem 8.11. (a) After a C∞-small perturbation of φ (keeping
the gradient-like vector ﬁeld and thus the skeleton ﬁxed) we may assume that no
two critical points have the same value. We order the critical points p0,p 1,... by
increasing value and setLj :=⋃
i≤jW−
pi. Then each Lj is compact,Lj\Lj−1 =W−
pj
is the stable manifold ofpj, and the skeleton isL =⋃
jLj. We deform J to make it
integrable near the minimum L0 ={p0}. Proceeding inductively, suppose that for
some j≥ 1 we already made J integrable onOpLj−1. Choose a compact domain
Ω with smooth boundary such that Lj−1⊂ Int Ω andJ is already integrable on Ω,
and such thatLj\Int Ω is a disc transversely attached to Ω. (Such a domain can be
obtained by picking a regular level cj between φ(pj−1) and φ(pj) and moving the
set{φ≤cj} under the backward ﬂow of the gradient-like vector ﬁeld for suﬃciently
long time). Hence we can apply Corollary 8.14 to make J integrable onOpLj.
For part (b) we move down the value φ|∂−W (without changing the skeleton)
until it is the minimum. Then we set L0 :=∂−W andLj :=L0∪⋃j
i=1W−
pi for the
critical points p1,p 2,... and proceed inductively as in part (a), starting with the
hypothesis that J is already integrable near ∂−W . □
8.4. Existence of Stein structures in complex dimension ⁄= 2
In this section we prove two of the main theorems in this book. The ﬁrst one
is equivalent to the Existence Theorem 1.5 from the introduction and was proved
in [42].
Theorem 8.15. Let V 2n be an open smooth manifold of dimension 2n⁄= 4
with an almost complex structure J and an exhausting Morse function φ without
critical points of index >n . Then V admits a Stein structure. More precisely, J is
homotopic through almost complex structures to an integrable complex structure ~J
such that φ is ~J-lc.
The second theorem concerns the realization of Stein manifolds of given topol-
ogy within a given ambient complex manifold.
Theorem 8.16 (Gompf [ 72, 73 ]). Let V 2n be an open smooth manifold of
dimension 2n ⁄= 4 with an (integrable) complex structure J and an exhausting
Morse function φ without critical points of index >n . Then J is homotopic through
(integrable) complex structures to a complex structure ~J which is Stein.
More precisely, there exists an isotopy ht : V ↪→ V with h0 = Id such that
φ◦h−1
1 is J-lc on h1(V ). In particular, h1(V ) ⊂ V is Stein with the induced

164 8. THE EXISTENCE THEOREM
V
h1
h1(V )
φ ◦ h−1
1
Figure 8.5. Constructing a Stein manifold within a given ambient
complex manifold.
complex structure J and Jt =h∗
tJ is a homotopy of complex structures on V such
that J0 =J and φ is J1-lc. See Figure 8.5.
The statements of both theorems are false for n = 2, see Chapter 16 for further
discussion. We will prove later in this chapter (Theorem 8.46) a stronger version of
Theorem 8.16 which allows us to prescribe the Stein homotopy class of the complex
manifold h1(V ) within the given almost complex homotopy class.
Theorems 8.15 and 8.16 have the following versions for cobordisms. Here a
Stein cobordism (W,J,φ ) is a Morse cobordism ( W,φ ) with a complex structure
J for which φ is J-convex. We stress the point that in the cobordism versions we
allow also the casen = 2. However, the price we have to pay here is the assumption
that the induced contact structure on ∂−W is overtwisted.
Theorem 8.17. Let (W 2n,φ ) be a Morse cobordism of dimension 2n with an
almost complex structureJ. Suppose that φ has no critical points of index >n , and
near∂−W the structureJ is integrable andφ isJ-lc. If n = 2 suppose, in addition,
that the contact structure induced by J on ∂−W is overtwisted. Then W admits a
Stein cobordism structure. More precisely, J is homotopic through almost complex
structures which agree with J near∂−W to an integrable complex structure ~J such
that φ is ~J-lc.
In the case n = 2 the above theorem implies the following version without any
assumption about ∂−W .
Corollary 8.18. Let (W,φ ) be a 4-dimensional Morse cobordism such that
the function φ has no critical points of index > 2. Let J be an almost complex
structure on W . Suppose that ∂−W ⁄= ∅. Then J is homotopic to an integrable
complex structure ~J for which the function φ is ~J-convex.
Proof. There exists an overtwisted contact structure ξ on ∂−W in the same
homotopy class of plane ﬁelds as the ﬁeld of complex tangencies induced by the
almost complex structure J, see Section 7.6. According to Remark 5.56, we can
deformJ to make it integrable near ∂−W and to induce the contact structure ξ on
∂−W . Then we apply Theorem 8.17. □
Finally, we state the ambient version of Theorem 8.17.
Theorem 8.19. Let (W 2n,φ ) be a Morse cobordism of dimension 2n with an
(integrable) complex structureJ and such that φ has no critical points of index >n

8.4. EXISTENCE OF STEIN STRUCTURES IN COMPLEX DIMENSION ⁄= 2 165
and φ is J-lc near ∂−W . If n = 2 suppose, in addition, that the contact structure
induced by J on ∂−W is overtwisted. Then J is homotopic through (integrable)
complex structures ﬁxed near ∂−W to a complex structure ~J which is Stein.
More precisely, there exists an isotopy ht : W ↪→ W ﬁxed near ∂−W with
h0 = Id such that φ◦h−1
1 is J-lc on h1(W ). In particular, h1(W )⊂ W is Stein
with the induced complex structure J and Jt = h∗
tJ is a homotopy of complex
structures on W such that J0 =J and φ is J1-lc.
We now turn to the proofs of these theorems. First note that Theorem 8.11
reduces Theorems 8.15 and 8.17 to Theorems 8.16 and 8.19, respectively. Hence,
we only need to prove the latter two theorems.
The following lemma will serve as the main inductive step for the proofs of
Theorems 8.16 and 8.19. Recall that a Morse cobordism (W,φ ) is called elementary
if φ admits a gradient-like vector ﬁeld X such that no two critical points of φ are
connected by an X-trajectory.
Lemma 8.20. Let (W,φ ) be an elementary Morse cobordism of dimension 2n
without critical points of index > n. If n = 2 we suppose, in addition, that the
contact structure induced by J on ∂−W is overtwisted. Let J be an integrable
complex structure onW such that φ isJ-lc near∂−W . Then there exists an isotopy
ht : W ↪→ W with h0 = Id and ht = Id near ∂−W for all t∈ [0, 1] such that the
function φ is h∗
1J-lc. If n = 2 then one can additionally arrange that the contact
structure induced on ∂+W by the complex structure h∗
1J is overtwisted.
Proof. Let X be a gradient-like vector ﬁeld for φ such that no two critical
points of φ are connected by an X-trajectory. Then the stable disc ∆ of each
critical point p meets no other critical points, and therefore meets the J-convex
hypersurface∂−W transversely along a sphere∂∆. By assumption we have dim ∆≤
n. The hypothesis that ∂−W is overtwisted in the case n = 2 allows us to apply
Theorem 7.34 to construct an isotopy of embedded discs ∆ t transversely attached
to ∂−W with ∆0 = ∆ and such that ∆ 1 is totally real and J-orthogonal to ∂−W .
If n = 2 one can arrange that the contact structure on ∂−W is overtwisted in
the complement of ∂∆1. Since the stable discs of diﬀerent critical points do not
intersect, we can do the above modiﬁcation independently for all stable discs. To
simplify the notation, we will assume that the cobordism contains just one critical
point p. The proof in the general case follows exactly the same scheme.
We ﬁnd a diﬀeotopy ht : W → W with h0 = Id and ht|Op∂−W) = Id and a
family of gradient-like vector ﬁelds Xt for φ◦φ−1
t starting with X0 =X for which
∆t is the stable disc of the critical point pt = φt(p). After renaming φ1,p 1, ∆1
back to φ,p, ∆ we may hence assume that the stable disc ∆ of p is totally real and
J-orthogonal to∂−W . After a further modiﬁcation of ∆ near ∂−W we may assume
in addition that ∆ is tangent to ∇φφ and J-orthogonal to the level sets of φ near
∂−W .
According to Corollary 8.9, the function φ|Op (∂−W) can be extended to a J-
convex function~φ on a neighborhood ~W of∂−W∪ ∆ havingp as its unique critical
point with stable disc ∆ (with respect to ∇ ~φ
~φ). Then we apply Theorem 8.5 to
deform ~φ to a J-lc function φ′ on a neighborhood W′ of ∂−∪ ∆ such that
• φ′ =φ onOp (∂−W );

166 8. THE EXISTENCE THEOREM
W1
W2
W ′
1
W ′
2
h(1)
1
h(2)
2
Figure 8.6. Inductive construction of the shrinking isotopy ht.
• φ′ has p as its unique critical point with stable disc ∆ (with respect to
∇φ′φ′, cf. Remark 3.33);
• φ′|∂+W′ is constant of value φ′(∂+W′) =φ(∂+W ).
(In fact, this conclusion does not really require Theorem 8.5: it can also be de-
rived from the easier Theorem 8.4 by applying the maximum construction to the
function ~φ and a suitable J-convex function having as level sets the surrounding
hypersurfaces provided by Theorem 8.4).
According to Lemma 9.29 below, there exists an isotopy ht : W ↪→ W with
h0 = Id, ht = Id near ∂−W , h1(W ) = W′, and φ′◦h1 = φ. Let us also note
that in the case n = 2 the induced contact structure on ∂+W′ is overtwisted.
Indeed (see Lemma 11.4 below), the gradient ﬂow of the function φ′ deﬁnes a
contactomorphism between ∂−W\∂∆ and ∂+W′\∂∆′, where ∆′ is the unstable
disc of p. By construction ∂−W\∂∆ is overtwisted, and hence so is ∂+W′. □
Proof of Theorem 8.16. According to Lemma 9.28 below, there exists an
increasing sequence of regular values ck→∞ of φ with c0 < infφ such that
(
Wk :=φ−1([ck−1,ck]),φ|Wk
)
is an elementary Morse cobordism for all k = 1,... . We will inductively extend the
required isotopy ht over the elementary cobordisms Wk, k = 1,....
First we apply Lemma 8.20 to construct an isotopy ht : W1→ W1, t∈ [0, 1],
such that the function φ◦h−1
1 is J-lc on W′
1 =h1(W1). We extend the isotopy ht
(keeping the same notation) to all of V such that ht|V\W2 is the identity. Set
h(1)
t :=ht|W2 :W2→W2, φ 1 :=φ◦ (h(1)
1 )−1 :W2→ R, W ′
2 :=W2∪ (W1\W′
1),
see Figure 8.6.
Next we apply Lemma 8.20 to the elementary Morse cobordism ( W′
2,φ 1) and
ﬁnd an isotopy h′
t : W′
2→ W′
2, ﬁxed on ∂−W′
2 = ∂+W′
1, such that the function
φ2 :=φ1◦ (h′
1)−1 isJ-lc. We extend h′
t (keeping the same notation) by the identity

8.5. J-CONVEX SURROUNDING FUNCTIONS 167
overW′
1. Then the isotopy
h(2)
t :=h(1)
t ◦ (h(1)
1 )−1◦h′
t◦h(1)
1 :W2→W2,
t∈ [0, 1], has the following properties:
• h(2)
0 = Id;
• h(2)
t =h(1)
t on W1;
• h(2)
1 =h′
1◦h(1)
1 and hence φ1◦ (h(2)
1 )−1 =φ2.
We extend the isotopy h(2)
t (keeping the same notation) to all of V such that
h(2)
t |V\W3 is the identity. Note that φ2 =φ◦ (h(2)
1 )−1 is J-lc on h(2)
1 (W2).
Continuing this process, we inductively construct isotopies h(k)
t : V → V ,
t∈ [0, 1], k = 1,... with the following properties:
• h(k)
0 = Id and h(k)
t = Id on V\Wk+1;
• h(k+1)
t =h(k)
t on Wk;
• φ◦ (h(k)
1 )−1 is J-lc on h(k)
1 (Wk).
In view of the second property, the sequence h(k)
t stabilizes and hence converges as
k→∞ to an isotopy ht : V → V . By the other two properties, h0 = Id and the
function φ◦h−1
1 :V → R is J-convex. □
Proof of Theorem 8.19. The proof is analogous to the preceding one but
simpler, decomposing (W,φ ) into ﬁnitely many elementary Morse cobordisms. □
8.5. J-convex surrounding functions
In this and the following section we put the results of Section 8.2 in a more
global context and discuss some applications to holomorphic convexity. These two
sections also serve as preparation for the holomorphic approximation results in
Section 8.7.
Definition 8.21. Let A⊂ V be a compact subset. A weakly J-convex ex-
hausting function φ : V → [0,∞) is called a J-convex surrounding function for A
in V if
• φ|A = 0;
• φ is (strictly) J-convex in V\A;
• φ has no critical points in U\A for some neighborhood U⊂V of A.
We say thatA admits a localJ-convex surrounding function if it admits aJ-convex
surrounding function on a neighborhood U⊂V of A.
The following result, which follows directly from Theorem 5.7, relates these
notions to notions of holomorphic convexity in Chapter 5.
Proposition 8.22. If a compact set A⊂ V admits a J-convex surrounding
function then its holomorphic hull in V satisﬁes ˆAV = A (so A is polynomially
convex in the case V = Cn). In particular, if A admits a local J-convex sur-
rounding function then it is holomorphically convex. If V is Stein and A admits a
localJ-convex surrounding function then A admits a fundamental system of Stein
neighborhoods.
In Section 2.7 we saw that the sets in Example 8.3 admit local J-convex sur-
rounding functions whenever they are compact.
We have the following improvement of Theorems 8.4 and 8.5.

168 8. THE EXISTENCE THEOREM
Theorem 8.23. (a) Under the assumptions of Theorem 8.4, the set ∂−W∪ ∆
admits a local J-convex surrounding function.
(b) Under the assumptions of Theorem 8.5, the set ∂−W∪ ∆ admits a (global)
J-convex surrounding function.
Proof. (a) Let A := ∂−W∪ ∆. By Corollary 8.9 there exists a J-convex
function ψ on a neighborhood U of A which has a unique critical point p∈ ∆
with stable disc ∆. Moreover, we can arrange ψ≥ 0 and ψ|∂−W ≡ 0. Pick any
neighborhood U1⋐ U of A. By Theorem 8.5 we ﬁnd a J-lc function ψ1 : U→ R
which equalsψ near∂−W and outsideU1, has unique critical pointp, and such that
A⊂{ψ1≤c1}⊂ U1 for somec1 > 0. Pick a smaller neighborhood U2⋐{ψ1 <c 1}
of A. Again by Theorem 8.5, we ﬁnd a J-lc function ψ2 :U→ R which equals ψ1
near ∂−W and outside U2, has unique critical point p, and such that A⊂{ ψ2≤
c2}⊂ U2 for some 0 <c 2 <c 1.
We continue this process for a sequence of neighborhoods U1⋑ U2⋑··· of
A with⋂
i∈NUi = A and a sequence of values c1 > c2 >··· converging to 0. In
the limit we obtain a smooth J-lc function U\A→ [0,∞) without critical points
which extends to a continuous function φ : U→ [0,∞) with φ|A≡ 0. According
to Proposition 8.29 below, we can make the function φ smooth on U andJ-convex
on U\A by a suitable target reparametrization.
(b) follows from the same construction, starting with the given J-convex func-
tion φ :V → R. □
The proof of Theorem 8.23 (b) also shows
Corollary 8.24. Let (W,J ) be a complex manifold with compact J-concave
boundary ∂−W . Let φ : W → [0,∞) be an exhausting J-convex Morse function
with regular level set φ−1(0) = ∂−W and ﬁnitely many critical points p1,...,p k.
Suppose that no critical points are connected by a gradient trajectory and denote
by ∆1,..., ∆k their stable discs. Then ∂−W∪ ∆1∪···∪ ∆k admits a J-convex
surrounding function ψ : W→ [0,∞) without critical points outside ∂−W∪ ∆1∪
···∪ ∆k which agrees with φ outside a neighborhood of ∆1∪···∪ ∆k.
Next, we generalize Theorem 8.23 (a) to totally real submanifolds other than
discs.
Corollary 8.25. Let (W,J ) be a complex manifold with compact J-concave
boundary ∂−W , and L ⊂ W be a compact totally real submanifold attached J-
orthogonally to∂−W along∂L. Then ∂−W∪L admits a localJ-convex surrounding
function.
Proof. Pick a Morse function φ :L→ R with regular level set ∂L =φ−1(0)
and critical points pi of values 0 < φ(p1) <··· < φ(pm) and Morse indices ki.
According to Corollary 8.9, the function φ can be extended to a J-convex Morse
function ψ on a neighborhood U ⊃ ∂−W∪L with ψ|∂−W ≡ 0 and such that L
is the union of the stable manifolds of the critical points pi of ψ for the gradient
vector ﬁeld∇ψψ.
Pick any neighborhoodU1⋐U of∂−W∪L. Inductively applying Theorem 8.5
to the pair ( U,ψ ) and the stable discs of the critical points pi we construct a J-
convex function ψ1 : U → R which equals ψ near ∂−W and outside U1, has the
same critical points as ψ, and such that one of its level sets surrounds ∂−W∪L
in U1. The important fact which allows us to proceed inductively is that in each

8.5. J-CONVEX SURROUNDING FUNCTIONS 169
application of Theorem 8.5 the manifoldL remainsJ-orthogonal to the level sets of
the new function. Now the construction of the local J-convex surrounding function
can be completed as in the proof of Theorem 8.23. □
The preceding corollary extends to totally real immersions. We say that two to-
tally real submanifoldsL1,L 2 of the same dimension in an almost complex manifold
(V,J ) intersectJ-orthogonally at p if JTpL1 =TpL2.
Corollary 8.26. Let (W,J ) be a complex manifold with compact J-concave
boundary∂−W . Let f :L→W be a totally real immersion of a compact manifold
L, with ﬁnitely many J-orthogonal interior self-intersection points andJ-orthogonal
to∂−W along∂L. Then ∂−W∪f(L) admits a localJ-convex surrounding function.
Proof. Pick any open neighborhood U⊂ W of ∂−W∪f(L). Let L1,L 2 be
the two local branches of f(L) at a self-intersection point p. By J-orthogonality
of the intersection, there exists a local holomorphic coordinate map g : B→ U
from the unit ball B in Cn mapping 0 to p, Rk1 to TpL1, and iRk2 to TpL2, where
ki is the dimension of Li near p. After precomposing g with the map z ↦→ δz
for suﬃciently small δ, we may assume that the preimages of the TpLi are C2-
close to Rk1 resp iRk2. Since Rk1 and iRk2 are i-orthogonal to ∂B, we can ﬁnd a
domainB′⊂ Cn whose boundary is C2-close to ∂B, hence i-convex, and intersects
each g−1(Li) i-orthogonally. Its image B(p) := g(B′) is contained in U, and the
boundary ∂B(p) is J-convex and intersects L1 and L2 J-orthogonally. Construct
such balls around all self-intersection points p1,...,p m, disjoint from each other
and from ∂−W . Then W′ := W\
(
B(p1)∪···∪ B(pm)
)
has compact J-concave
boundary ∂−W′ to which the totally real submanifold f(L)∩W′ is attached J-
orthogonally. Hence Corollary 8.25 provides a local J-convex surrounding function
for ∂−W∪f(L)∪⋃
iB(pi) in U. Now we proceed inductively as in the proof of
Theorem 8.23, making the neighborhood U and the balls B(pi) smaller at each
step, to ﬁnd the desired local J-convex surrounding function for ∂−W∪f(L). □
In particular, for ∂−W = ∅ we obtain
Corollary 8.27. Let (V,J ) be a complex manifold andf :L→V a totally real
immersion of a closed manifoldL with ﬁnitely manyJ-orthogonal self-intersections.
Then f(L) admits a local J-convex surrounding function.
Remark 8.28. In the case that L is real analytic near its double points, an
alternative proof of the last corollary can be given by combining the surroundings of
totally real embeddings in Proposition 2.15 with the surroundings near the double
points provided by Lemma 4.12.
It remains to prove the following technical result that was used in the proof of
Theorem 8.23.
Proposition 8.29. Let (V,J ) be a complex manifold and φ : V → R≥0 a
nonconstant continuous function such that K = φ−1(0) is compact and φ|V\K is
smooth with compact regular J-convex level sets. Then there exists a smooth func-
tionf : R→ R≥0 such that f≡ 0 on R≤0, f′ > 0 on R+, ψ =f◦φ is smooth (with
zero set K), and ψ|V\K is (strictly) J-convex.
The proof is based on two lemmas about real-valued functions.

170 8. THE EXISTENCE THEOREM
Lemma 8.30. Letg : [0, 1]→ R≥0 be a continuous function with g−1(0) ={0}.
Then there exists a smooth function f : R→ R≥0 satisfying f≡ 0 on R≤0, f′ > 0
on R+, and f≤g on [0, 1].
Proof. Forn∈ N set an := min [1/n,1]g and deﬁne a piecewise constant func-
tion h : R+→ R+ by
h(t) := min{an,e−n}, t ∈
[ 1
n, 1
n− 1
)
, n∈ N.
Smooth h to a smooth function f : R+→ R+ satisfying f′ > 0 and f≤ h≤ g,
and extend f by 0 over R≤0. Since f(t)≤h(t)≤e−1/t for t> 0, the function f is
smooth at t = 0. □
Lemma 8.31. LetV be a manifold and φ :V → R≥0 a nonconstant continuous
function such that K =φ−1(0) is compact and φ|V\K is smooth with compact level
sets. Then there exists a smooth function f : R→ R≥0 such that f≡ 0 on R≤0,
f′ > 0 on R+, and f◦φ is smooth (with zero set K).
Proof. After rescaling we may assume that [0, 1]⊂φ(V ). Pick a Riemannian
metric on V and denote by d(x,y ) the corresponding distance function. Deﬁne a
continuous function d : [0, 1]→ R≥0 by
d(t) := min{d(x,y )|x∈K,y∈φ−1(t)}.
This function satisﬁes d−1(0) = {0}. Deﬁne g : [0, 1]→ R≥0 by g(0) := 0 and
g(t) := e−1/d(t) for t > 0. Then g is continuous with g−1(0) = {0}, so by
Lemma 8.30 there exists a smooth function f : R→ R≥0 satisfying f ≡ 0 on
R≤0, f′ > 0 on R+, and f(t)≤ g(t) = e−1/d(t) for t∈ [0, 1]. It remains to show
smoothness of the function ψ :=f◦φ at points of K. So let x∈K andy∈V with
φ(y) =t∈ [0, 1]. Then d(t)≤d(x,y ) and thus
ψ(y)−ψ(x) =f(t)≤e−1/d(t)≤e−1/d(x,y),
which implies smoothness of ψ at x. □
Proof of Proposition 8.29. After applying Lemma 8.31, we may assume
that φ is smooth. Moreover, after rescaling we may assume that [0 , 1]⊂ φ(V ). A
short computation as in the proof of Lemma 2.7 shows that ψ =f◦φ is J-convex
on φ−1((0, 1]) provided that
f′′(t)‖dφ(x)‖2−f′(t)‖ddCφ(x)‖> 0
for all x∈V with φ(x) =t∈ (0, 1]. Pick smooth functions a,b : (0, 1]→ R+ with
a(t)< minφ−1(t)‖dφ‖2, b (t)> maxφ−1(t)‖ddCφ‖.
Then ψ = f◦φ is J-convex on φ−1((0, 1]) if f solves the diﬀerential equation
a(t)f′′(t) =b(t)f′(t), i.e.,
d
dt logf′(t) = b(t)
a(t) =:c(t), t ∈ (0, 1].
The solution with f′(1) = 1 satisﬁes
f′(t) =e−
∫ 1
t c(s)ds :=d(t)> 0.
By choosing the function a suﬃciently small we can ensure that c(t)→∞ ast→ 0
so fast that d(t)≤e−1/t, so d extends to a smooth function on (−∞, 1] with d≡ 0

8.6. J-CONVEX RETRACTS 171
on R≤0. Then f(t) :=
∫t
0d(t)dt is the desired function on ( −∞, 1]. Finally, we
extend f over [1,∞) by Lemma 2.7. □
8.6. J-convex retracts
Consider a compact set A⊂V which admits a J-convex surrounding function
φ :V → [0,∞) without critical points in V\A. Then pushing down along gradient
trajectories of φ yields an isotopy ht :V ↪→V , t∈ [0,∞), such that
• h0 = Id and ht|A = Id for all t∈ [0,∞);
• ⋂
t∈[0,∞)
ht(V ) =A;
• the isotopy ht maps level sets of φ to level sets, so in particular the
function φ◦h−1
t is J-lc for all t∈ [0,∞).
More generally, consider a closed (not necessarily compact) set A ⊂ V and an
exhausting weakly J-convex function φ : V → R without critical points in V\A.
We say that A⊂ V is a J-convex retract adapted to φ if there exists an isotopy
ht :V ↪→V , t∈ [0,∞), with the following properties:
• h0 = Id and ht|A = Id for all t∈ [0,∞);
• ⋂
t∈[0,∞)
ht(V ) =A;
• the function φ◦h−1
t is J-lc for all t∈ [0,∞).
Note that if A is noncompact the exhausting function φ has to be unbounded (in
particular nonconstant) on A. The example to keep in mind is the skeleton of
an exhausting J-convex Morse function. The J-convex retract A in the following
theorem may not be exactly the skeleton, but it shares many of its properties.
We say that a closed subset A⊂V admits a totally real stratiﬁcation by aﬃne
strata if A can be presented as a countable union A =⋃
i∈NAi such that each Ai
is the image of a totally real injective immersion Rki ↪→V .
Theorem 8.32. Let (V,J,φ ) be a Stein manifold with exhausting J-convex
Morse function φ :V → R.
(a) If φ has ﬁnitely many critical points, then there exists a compact subset
A⊂ V which admits a ﬁnite totally real stratiﬁcation by aﬃne strata and a J-
convex surrounding function ψ :V → [0,∞) without critical points in V\A.
(b) In general, there exists a closed J-convex retractA⊂V adapted to φ which
admits a totally real stratiﬁcation by aﬃne strata.
Proof. After adding a constant we may assume that min φ = 0. Pick an
increasing sequence c0 <c 1 <... of regular values of φ such that c0 < 0, cj→∞ ,
and each (cj,cj+1) contains at most one critical value. For simplicity we will assume
that each cobordism Wj :={cj≤φ≤cj+1} contains at most one critical point pj
of φ; the general case diﬀers only in the notation. We will also assume that φ has
a unique local minimum p0. Set Vi :=⋃i
j=0Wj, see Figure 8.7.
(a) Let us ﬁrst consider the case whenφ has ﬁnitely many critical points, so the
domain{φ≥ck+1} contains no critical points for some k. Choose a neighborhood
U0 ⊂ V0 of p0, pick ~c1 < c1 such that p0 ∈ ~V0 := {φ ≤ ~c1} ⊂U0, and set
~W1 := V1\ Int~V0 and Σ 0 :={φ =~c1}. Let ∆ 1 be the stable disc of the critical
point p1 in ~W1 for the function φ. Choose a neighborhood U1⊂ V1 of ~V0∪ ∆1
and apply Theorem 8.5 to φ|~W1
to construct a J-lc function φ1 :V → R with the
following properties:

172 8. THE EXISTENCE THEOREM
W0
W1
W2
c3
c1
c2
Σ0
Σ1
Σ2
~V0
p0
p1
p2
∆1
∆2
c′
2
h1
1
2
~V1
Figure 8.7. Constructing a J-convex retract.
• φ1 equals φ outside U1 and on ~V0;
• φ1|U1\ ~V0
has the unique critical point p1;
• some level set Σ 1 of φ1 surrounds ~V0∪ ∆1 in U1.
Denote by ~V1 the domain bounded by Σ 1 inV1. Set ~W2 :=V2\ Int~V1 and consider
the stable disc ∆ 2 of the critical point p2 in ~W2 for the function φ1. Note that
∆2∩W2 coincides with the stable disc of p2 in W2 for the function φ.
We continue this process inductively. Choose a neighborhoodU2⊂V2 of~V1∪∆2
and use Theorem 8.5 to further modify φ1 to a J-lc function φ2 one of whose level
sets Σ 2 surrounds ~V1∪ ∆2 in U2, etc. This process terminates at the k-th step
to give a J-lc function φ(1) := φk one of whose level sets Σ k bounds a domain
V (1) := ~Vk which contains all the critical points pj of φk.
Next we repeat the whole process for the domain V (1) with the function φ(1),
choosing smaller neighborhoods of the stable discs. It is important to observe that
the stable disc of the critical pointpj for the functionφ(1 inW (1)
j contains the stable
disc of the same critical pointpj for the functionφj inWj. As a result of the second
cycle we produce a J-lc function φ(2) := φ(1)
k , one of whose level sets Σ (1)
k bounds
a domain V (2) := ~V (1)
k which contains all the critical points pj of φ(2) :=φ(1)
k (the
critical points remain the same for all functions in the construction).
We continue this process inductively, each time surrounding the stable discs by
smaller neighborhoods so that their widths tends to 0. As a result, we construct a
sequence of J-lc functions φ(m) :V → R,m∈ N, and domains V ⊃V (1)⊃V (2)···
such that

8.6. J-CONVEX RETRACTS 173
(i) for each n>m the function φ(n) is equal to φ(m) on V\V (m);
(ii) all the functions φ(m) have the same critical points pj as the function φ;
(iii) each V (m) can be presented as the union V (m) =⋃k
i=1V (m)
i such that
∂V (m)
i is a regular level set of φ(m) and each cobordism W (m)
i :=V (m)
i \
IntV (m)
i−1 contains the unique critical point pi;
(iv) the stable disc ∆ (m)
i of the critical pointpi for the functionφ(m) in~W (m)
i
is contained in the stable disc ∆ (m+1)
i of pi for the function φ(m+1) in
W (m+1)
i ;
(v) the set A := ⋂∞
m=1V (m) is compact and admits a ﬁnite totally real
stratiﬁcation A = ⋃k
j=0Aj by the aﬃne strata Aj := ⋃∞
m=1 ∆(m)
j for
j >0 and A0 :={p0}.
The desired J-convex surrounding function is obtained by a target reparametriza-
tion (using Proposition 8.29) of the function which coincides with φ(m) onV (m−1)\
V (m), m = 1,... , where we set V (0) := V . This concludes the proof in the case
when the function φ has ﬁnitely many critical points.
(b) In the case of inﬁnitely many critical points our ﬁrst inductive process works
for constructing the domain V (1) :=⋃∞
k=1~Vk and for constructing the function φ(1)
on V (1) but not on V \V (1). Instead, we will construct at this step an isotopy
h(1)
t :V ↪→V with the following properties:
• h(1)
1 (V ) =V (1);
• φ◦ (h(1)
1 )−1 =φ(1);
• the function φ◦ (h(1)
t )−1 is J-lc for all t∈ [0, 1].
The isotopy is constructed as follows. Take regular values c′
k > ck of the original
function φ such that there are no critical values of φ in [ck,c′
k] and set V′
k :=
{φ≤ c′
k}. Using the notation of the above construction, consider the cobordism
~W2 = V2\ Int~V1 and the J-lc function φ1 which is constant on the boundary
components of ~W2 . There exists a diﬀeotopy h1
t : V →V , t∈ [0, 1
2], which maps
level sets of the function φ1 to level sets and such that h1
0 = Id, h1
1
2
(V2) = ~V1, and
h1
t = Id on ~V0 and outside V′
2 for all t∈ [0, 1
2].
Fork∈ N set dk :=∑k
i=1
1
2i , k = 0, 1,... . As in the construction of h1
t above,
we construct for each k≥ 2 diﬀeotopies hk
t :V′
k+1→V′
k+1, t∈ [dk−1,dk], with the
following properties:
• hk
t maps level sets of the function φk to level sets;
• hk
0 = Id and hk
dk+1(Vk+1) = ~Vk;
• hk
t = Id on ~Vk−1 and outside V′
k+1 for all t∈ [dk,dk+1].
Deﬁne the diﬀeotopyh(1)
t :V →V ,t∈ [0, 1), by the formulah(1)
t =h1
t fort∈ [0, 1
2)
and
h(1)
t =hk+1
t ◦hk
dk+1◦hk−1
dk
◦···◦ h1
1
2
, for t∈ [dk,dk+1], k≥ 1.
Note that there exists a limith(1)
1 = lim
t→1
h(1)
t because the diﬀeotopyh(1)
t stabilizes on
compact sets. However, the limit maph(1)
1 is not onto but mapsV diﬀeomorphically
to Int V (1). In other words, h(1)
t can be deﬁned for all t∈ [0, 1] as an isotopy
rather than a diﬀeotopy. Now it is clear that we can inductively continue this

174 8. THE EXISTENCE THEOREM
process for the functions φ(k),k = 1,..., and ﬁnd isotopies h(j)
t : Int V (j−1) ↪→
IntV (j−1), j = 2,..., parametrized by t∈ [j− 1,j ] and such that h(j)
j−1 = Id and
h(j)
j (IntV (j−1)) = Int V (j). Finally, we deﬁne the desired isotopy ht : V ↪→ V
inductively by h0 = Id and ht =h(j)
t ◦hj−1 for t∈ [j− 1,j ] and j∈ N. □
8.7. Approximating continuous maps by holomorphic ones
In this section we apply our previous results to problems of approximating
continuous maps by holomorphic ones. For example, we will obtain the following
holomorphic approximation theorem, proven by Forstneriˇ c and Slapar in [63] (see
also [62, 60]), as a consequence of results of H¨ ormander–Wermer and Theorem 8.4.
Theorem 8.33. Let (V,J ) be a Stein manifold, W ⊂ V a compact domain
with smooth J-convex boundary, and L⊂ V\ IntW a totally real submanifold J-
orthogonally attached to W . Then any Ck-function f : (OpW )∪L→ C which is
holomorphic onOpW can beCk-approximated uniformly onW∪L by holomorphic
functions onOp (W∪L).
Remark 8.34. (1) Let us emphasize that Theorem 8.33 provides only approx-
imations of the derivatives of f in directions tangent to L and not in the normal
directions.
(2) Corollary 5.29 allows us to generalize Theorem 8.33 to sections of any
holomorphic vector bundle over a Stein manifold V .
Corollary 8.35. Let (V,J ) be a Stein manifold with exhausting J-convex
Morse function φ : V → R. Let c be a regular value of φ, W ={φ≤ c}, and
(∆,∂ ∆)⊂ (V \ IntW,∂W ) the stable disc of a critical point of φ in V \ IntW .
Then any continuous function f :Op (W∪∆)→ C which is holomorphic onOpW
can be C0-approximated uniformly on W∪ ∆ by holomorphic functions on V .
Proof. According to Theorem 8.23 and Proposition 8.22, the set A :=W∪ ∆
satisﬁes ˆAV = A. Hence the generalized Oka–Weil Theorem 5.18 allows us to
approximate a holomorphic function onOpA by a holomorphic function on V . □
The proof of Theorem 8.33 is based on the following uniform estimate for
solutions of the ∂-equation which is a combination of results by H¨ ormander [102]
and H¨ ormander–Wermer [104].
Theorem 8.36 (H¨ ormander–Wermer). Let Ω⊂ Cn be a bounded open domain
with smooth J-convex boundary. Then given a smooth closed (0, 1)-formg onOp Ω
there exists a smooth solution f : Ω→ C of the equation ∂f =g which satisﬁes for
each integer k≥ 0 an estimate
(8.2) |Dkf(z)|≤ C
dist(z,∂ Ω)n+k||g||Ck(Ω),
for any z∈ Ω. Here the left-hand side in this inequality is the pointwise norm of
the k-jet of the function f at z, and the constant C depends only on k and the
diameter of the domain Ω.
Proof. Theorem 2.2.3 (with ϕ = 0) in [102] provides an L2-bound
||f||L2(Ω)≤C||g||L2(Ω),

8.7. APPROXIMATING CONTINUOUS MAPS BY HOLOMORPHIC ONES 175
where the constant C depends only on the diameter of Ω. On the other hand,
Lemma 4.4 in [ 104] gives a pointwise bound
|f(z)|≤ C
( 1
dist(z,∂ Ω)n||f||L2(Ω) + dist(z,∂ Ω)||g||C0(Ω)
)
.
These two bounds together with the obvious bound ||g||L2(Ω)≤ C||g||C0(Ω) imply
the estimate (8.2) for k = 0. The estimate for higher k follows from this via
Lemma 8.37 below: If we denote by Ω ε the set of points in Ω of distance ≥ε from
∂Ω, then Lemma 8.37 yields for any z∈ Ω2ε an estimate
|Dkf(z)|≤ Ck
(‖f‖C0(Ωε)
εk +‖g‖Ck(Ω)
εk−1
)
,
which combined with (8.2) for k = 0 yields (8.2) for any k. □
It remains to prove the lemma used in the proof of Theorem 8.36. Consider
the polydisc Pn
ε :={z∈ Cn || z1|,..., |zn|≤ ε} of radius ε > 0 and the torus
Tn
ε :={z∈ Cn||z1| =··· =|zn| =ε}.
Lemma 8.37. For each integerk≥ 0 there exists a constant Ck depending only
on k such that every smooth function f :OpPn
2ε→ C, 0 < ε <1, satisﬁes the
estimate
(8.3) |Dkf(0)|≤ Ck
(
‖f‖C0(Tnε )
εk +
‖∂f‖Ck(Pn
2ε)
εk−1
)
.
Proof. We ﬁrst consider the case n = 1. By the inhomogeneous Cauchy
integral formula (see e.g. [ 103]) we have
f(z) = 1
2πi
∫
|ζ|=ε
f(ζ)dζ
ζ−z + 1
2πi
∫
|ζ|≤ε
g(ζ)dζ∧d¯ζ
ζ−z =:I1(z) +I2(z)
for|z| < ε, where we have set g := ∂f
∂¯z . Let D = ∂i+j
∂zi∂¯zj be any partial derivative
of order i +j =k. Applying D to both sides of the Cauchy integral formula yields
|Df(0)|≤| DI1(0)| +|DI2(0)|. The standard estimate for the Cauchy integral I1
gives us
|DI1(0)|≤ 1
2π
∫
|ζ|=ε
k!|f(ζ)dζ|
|ζ−z|k+1≤ k!‖f‖C0(T 1ε )
εk .(8.4)
To estimate the second term we pick a smooth cutoﬀ function α : [0,∞)→ [0, 1]
which equals 1 on [0, 1] and 0 outside [0, 2) and consider the integral
I3(z) :=
∫
|ζ|≤2ε
α(|ζ|
ε )g(ζ)dζ∧d¯ζ
ζ−z =
∫
C
α(|ζ|
ε )g(ζ)dζ∧d¯ζ
ζ−z
=
∫
C
α(|z+u|
ε )g(z +u)du∧d¯u
u .
Diﬀerentiating the last integral we get an estimate
|DI3(0)|≤ C
εk‖g‖Ck(P 1
2ε)
∫
|u|≤2ε
|du∧d¯u|
|u| ≤ C
εk−1‖g‖Ck(P 1
2ε).(8.5)

176 8. THE EXISTENCE THEOREM
Diﬀerentiating the diﬀerence
I4(z) :=I3(z)−I2(z) =
∫
ε≤|ζ|≤2ε
α(|ζ|
ε )g(ζ)dζ∧d¯ζ
ζ−z
we get a similar estimate
(8.6) |DI4(0)|≤
∫
ε≤|ζ|≤2ε
C‖g‖Ck(P 1
2ε)|dζ∧d¯ζ|
|ζ−z|k+1 ≤ C
εk−1‖g‖Ck(P 1
2ε).
Combining estimates (8.4), (8.5) and (8.6) yields (8.3) in the case n = 1.
The general case follows by induction on n. For n≥ 2 consider any partial
derivativeD inz1, ¯z1,...,z n, ¯zn of orderk≥ 1. After reordering the coordinates, if
necessary, we can write D =D1D2, where D1 is a partial derivative of order k1 in
z1, ¯z1 andD2 is a partial derivative of orderk2 in the remaining variables such that
k1 +k2 = k. Applying the induction hypothesis for ﬁxed z1∈ T 1
ε to the function
f(z1,·) :Pn−1
2ε → C, we obtain the estimate
(8.7) |D2f(z1, 0,..., 0)|≤ Ck2
(
‖f‖C0(Tnε )
εk2
+
‖g‖Ck2(Pn
2ε)
εk2−1
)
,
where we have set g := ∂f = g1d¯z1 +··· +gnd¯zn. Diﬀerentiating ∂f
∂¯z1
= g1 we
obtain ∂
∂¯z1
D2f(z1, 0,..., 0) =D2g1(z1, 0,..., 0). Applying the case n = 1 with the
operator D1 to this equation we get
|D1D2f(0)|≤ Ck1
(
‖D2f(·, 0,..., 0)‖C0(T 1ε )
εk1
+
‖D2g1(·, 0,..., 0)‖Ck1(P 1
2ε)
εk1−1
)
,
which together with (8.7) yields the desired estimate. □
Remark 8.38. Theorem 8.36 can be extended to domains in an arbitrary Stein
manifold V in the following way: Embed V into some CN and measure distances
and diameters in CN. Then for any bounded open domain Ω⊂ V with smooth
J-convex boundary there exists a solution f of the equation ∂f =g which satisﬁes
estimate (8.2) with a constantC which depends only on the diameter of Ω. Indeed,
according to Corollary 5.27 there exists a neighborhoodU ofV in CN which admits
a holomorphic retraction π : U→ V . Then the (0 , 1)-form g′ := π∗g on U is ∂-
closed. Let Ω⊂V be a bounded open domain with smooth J-convex boundary. By
Corollary 5.31, there exists a bounded open domain Ω′⊂U with smooth J-convex
boundary such that π(Ω′) = Ω and diam(Ω ′)≤ 2 diam(Ω). Thus we can apply
Theorem 8.36 to the form g′ on Ω′, and then restrict the solution of the ∂-equation
back to Ω.
Proof of Theorem 8.33. First, we observe that it is suﬃcient to consider
the case V = Cn. Indeed, we can embed V in some Cn, extend the function f to a
neighborhood of V in Cn, and replace W by a neighborhood of W with J-convex
boundary in Cn. Furthermore, using induction over a handlebody decomposition
of L as in the proof of Corollary 8.25, we need only consider the case when L = ∆
is a disc.
It is suﬃcient to consider the case when f is a C∞-function. Using Proposi-
tion 5.55 we can ﬁnd a function ~f :Op (W∪ ∆)→ C which coincides with f on
(OpW )∪ ∆ and such that ∂f vanishes at points of ∆ together with its ( n + 2k)-
jet. Suppose that ~f is deﬁned on a neighborhood U ⊃ W∪ ∆ and holomorphic

8.7. APPROXIMATING CONTINUOUS MAPS BY HOLOMORPHIC ONES 177
on an open set U1⊃ W with U1⊂ U. Let us pick a slightly larger compact do-
main W1⊂ U1 with smooth J-convex boundary ∂W1 to which ∆ 1 := ∆\W1 is
J-orthogonally attached along ∂∆1.
According to Theorem 8.23, the set W1∪∆1 admits a localJ-convex surround-
ing function. In particular, there exists a family Ω ε, ε∈ (0,ε 0], of bounded open
domains with smooth J-convex boundary such that
• Ωε⊂ Ωε′ if ε<ε ′;
• ⋂
ε>0 Ωε =W1∪ ∆1;
• ∂Ωε\U1 ={z∈U| dist∆(z) =ε}\ U1.
(The last property can be extracted from the proof of Theorem 8.23, in which the
hypersurfaces ∂Ωε are deﬁned near ∆ by shapes as shown in Figure 4.1).
Set g = ∂~f. This is a closed (0 , 1)-form on U which vanishes on U1. It also
vanishes along ∆1 together with its (n + 2k)-jet, so we have
||g||Ck(Ωε) =o(εn+k).(8.8)
By construction of Ω ε, for ε suﬃciently small we have dist( z,∂ Ωε) ≥ ε for all
z ∈ W∪ ∆ (with equality if z ∈ ∆1). Hence, according to Theorem 8.36, the
equation ∂hε =g on Ωε has a solution hε which satisﬁes the estimate
||hε||Ck(W∪∆)≤ C
εn+k||g||Ck(Ωε),(8.9)
where the constant C is independent of ε. Then (8.8) and (8.9) imply that
||hε||Ck(W∪∆) →
ε→0
0.
Thus the function fε := ~f−hε is holomorphic on Ωε and satisﬁes
||~f−fε||Ck(W∪∆) =||hε||Ck(W∪∆) →
ε→0
0.
This concludes the proof of Theorem 8.33. □
In the remainder of this section we discuss applications of Theorem 8.33. The
ﬁrst one is the following approximation result. Recall that a Stein manifold ( V,J )
is said to be of ﬁnite type if it admits an exhausting J-convex function with only
ﬁnitely many critical points.
Corollary 8.39. Let (V,J ) be a Stein manifold and f :V → C a continuous
function.
(a) Suppose V is of ﬁnite type. Then for every ε> 0 there exists a sublevel set
W ={φ<c } of an exhausting J-convex function φ :V → R without critical points
in V\W , and a globally deﬁned holomorphic function g :V → C satisfying
||g−f||C0(W) <ε.
(b) For general V , any positive function ε : V → R and any exhausting J-
convex function φ : V → R there exist an isotopy ht : V ↪→ V , t∈ [0, 1], such
that h0 = Id and φ◦h−1
t is J-lc for all t∈ [0, 1], and a holomorphic function
g :W =h1(V )→ C such that
|g(x)−f(x)|<ε (x), x ∈W.

178 8. THE EXISTENCE THEOREM
Proof. Take any exhausting J-convex Morse function φ : V → R. Pick an
increasing sequence c0 < c1 <··· of regular values of φ such that c0 < minφ
and each cobordism Wi :={ci−1≤ φ≤ ci} is elementary. We will assume that
each Wi contains exactly one critical point pi of φ. The general case diﬀers only
in the notation. We will also assume that φ has a unique local minimum p0. Let
Vj =⋃j
i=1Wi.
(a) Let us ﬁrst consider the case when φ has ﬁnitely many critical points, so
that the domain {φ ≥ ck+1} contains no critical points for some k. Fix some
ε >0. Choose a holomorphic C0-approximation g0 of f near p0. By choosing the
regular valuec1 suﬃciently close to the minimum we can assume that g0 is deﬁned
onOpW0 =OpV0 and satisﬁes||f−g0||C0(V0) < ε
2. We extend g0 elsewhere on
V as a continuous function ε
2-close to f. Let ∆ 1 denote the stable disc of p1 in
W1. According to Theorem 8.33 there exists a neighborhood U1⊃W0∪ ∆1 and a
holomorphic function g1 : U1→ C such that||g1−g0||C0(U1) < ε
4. We extend the
functiong1 (after shrinking U1 is necessary) to a continuous function on the whole
manifold V satisfying the estimate||g1−g0||C0(V ) < ε
4.
Next, we apply Theorem 8.5 to construct a J-convex function φ1 : V → R
which is target equivalent to φ on a smaller neighborhood U′
1⋐U1, U′
1⊃W0∪ ∆1
and outside U1, with no critical points in U1\U′
1 and such that one of its level sets
Σ1 surrounds W0∪ ∆1 in U1. Denote by V′
1 the domain bounded in V by Σ1 and
set W′
2 := W2\ IntV′
1. Denote by ∆ 2 the stable disc of the critical point p2 for
the function φ1 in W′
2. We again apply Theorem 8.33 to construct a holomorphic
approximationg2 ofg1 on a neighborhoodU2⊃V′
1∪∆2 such that||g2−g1||C0(U2) <
ε
8. Applying Theorem 8.5 again we construct aJ-convex functionφ2 :V → R which
is target equivalent to φ1 on a smaller neighborhood U′
2⋐ U2, U′
2⊃ V′
1∪ ∆2 and
outside U2, with no critical points in U2\U′
2 and such that one of its level sets Σ 2
surrounds V′
1∪ ∆2 in U2. Now we denote by V′
2 the domain bounded in V2 by Σ2,
set W′
3 :=W3\ IntV′
2, denote by ∆ 3 the stable disc of the critical point p3 in W′
3
for φ2, and continue the process inductively.
Ifφ has ﬁnitely many critical points the process terminates at thek-th step. The
holomorphic functiongk deﬁned onOpV′
k satisﬁes the estimate||gk−f||C0(V′
k) <ε .
The setV′
k is a sublevel set of the exhaustingJ-convex function functionφk :V → R
which has no critical points in the complement of W = IntV′
k. By Theorem 5.7
the holomorphic hull of V′
k inV equalsV′
k, hence Theorem 5.18 provides a globally
deﬁned holomorphic function g :V → C satisfying||g−f||C0(V′
k) <ε .
(b) If the number of critical points of φ is inﬁnite one needs to make the
following modiﬁcation to the process. Instead of a constant ε> 0 we ﬁx a positive
function ε : V → R+ and then at each step we choose the required holomorphic
approximationgk to satisfy the estimate
||gk−gk−1||C0(V′
k) < 1
2k+1 min
V′
k
ε(x).
The required holomorphic approximation g := lim
k→∞
gk is now deﬁned on the open
setW :=⋃∞
k=1 IntV′
k⊂V . The existence of an isotopy ht :V ↪→V ,t∈ [0, 1], such
that h1(V ) = W and the function φ◦h−1
t is J-lc for all t∈ [0, 1] can be shown as
in the proof of Theorem 8.32 (b). □
Corollary 8.39 can be generalized to maps to arbitrary complex manifolds. We
will need for this the following

8.7. APPROXIMATING CONTINUOUS MAPS BY HOLOMORPHIC ONES 179
Lemma 8.40. Let (X,J ) be any complex manifold. Then for a suﬃciently large
integer N there exists a C∞-small isotopy ht : X ↪→ X× CN, t∈ [0, 1], of the
inclusion h0 :X =X× 0↪→X× CN such that h1(X) is totally real. In particular,
h1(X) has arbitrarily small Stein neighborhoods in X× CN.
Proof. In the space Hom R(Cn, CN) the set of linear maps which are complex
linear on at least one complex line, i.e., whose graph contains a complex line, is a
stratiﬁed subset of codimension N− 2n + 2. Hence, if dim CX = n, then Thom’s
transversality theorem ensures that when N >4n− 2 the graph of a generic map
X→ CN is totally real. Hence the lemma follows from Proposition 2.15. □
Corollary 8.41. Let (V,J ) be a Stein manifold, (Y,I ) any complex manifold,
and f :V →Y a continuous map.
(a) Suppose V is of ﬁnite type. Then for every ε> 0 there exists a sublevel set
W ={φ<c } of an exhausting J-convex function φ :V → R without critical points
in V\W , and a holomorphic function g :W→Y satisfying
||g−f||C0(W) <ε.
(b) For general V , any positive function ε : V → R and any exhausting J-
convex function φ : V → R there exists an isotopy ht : V ↪→ V , t∈ [0, 1], such
that h0 = Id and φ◦h−1
t is J-lc for all t∈ [0, 1], and a holomorphic function
g :W =h1(V )→ C such that
|g(x)−f(x)|<ε (x), x ∈W.
Remark 8.42. Note that, in contrast to Corollary 8.39 (a), the holomorphic
map g in Corollary 8.41 is not deﬁned globally but only on the set W .
Proof. Suppose ﬁrst that (Y,I ) is Stein. Take a proper holomorphic embed-
ding h : Y ↪→ CN and apply Corollary 8.39 to the composition h◦f : V → CN.
According to Corollary 5.27 there exists a neighborhood U of ~Y := h(Y ) in CN
which admits a holomorphic retraction π :U→ ~Y . If the holomorphic approxima-
tion g : W → CN of h◦f provided by Corollary 8.39 is good enough the image
g(W ) is contained in U and hence can be projected back to ~Y , so the desired
approximation is h−1◦π◦g.
For the case of a generalY we ﬁrst use Lemma 8.40 to ﬁnd a smooth embedding
h :Y ↪→Y×CN, which isC∞-close to the inclusionY =Y×0↪→Y×CN and such
that the imageh(Y ) has a Stein neighborhoodU. Then we construct a holomorphic
approximation g : W→ U of h◦f and project it back to Y under the projection
Y× CN→Y . □
Corollary 8.41 implies the following result, which is a stronger form of Forstneriˇ c–
Slapar’s Theorem 1.1 in [ 63].
Theorem 8.43. Let (V,J ) be a Stein manifold and (Y,I ) any other complex
manifold. Let φ : V → R be an exhausting J-convex function. Then given a
continuous map f : V → Y there exists an isotopy ht : V ↪→ V , t∈ [0, 1], with
h0 = Id, and a holomorphic map g :h1(V )→Y such that
• the function φ◦h−1
t is J-lc for all t∈ [0, 1];
• the map g is homotopic to f|h1(V ).

180 8. THE EXISTENCE THEOREM
In particular, there exists a homotopy of Stein structures Jt on V with J0 = J
for which φ is Jt-lc, and a homotopy ft : V → Y with f0 = f such that f1 is
J1-holomorphic.
Proof. Let ht : V ↪→ V be the isotopy and g : h1(V )→ Y the holomorphic
approximation provided by Corollary 8.41. Then the function φ is Jt-lc for each
of the complex structures Jt :=h∗
tJ on V . If g is suﬃciently close to f|h1(V ) they
are connected by a homotopy gt : h1(V )→ Y with g0 = f|h1(V ) and g1 = g. So
we can homotope f : V → Y via f◦ht to g◦h1 and then via gt◦h1 to the map
f1 :=g◦h1 :V →Y which is J1-holomorphic. □
Remark 8.44. Our proof of Theorem 8.43 is essentially the same as the one
given by Forstneriˇ c and Slapar in [63], with one major diﬀerence: we use as the
main technical tool Theorem 8.5, while they use a result analogous to Theorem 8.4.
A result which is essentially equivalent to Theorem 8.4 was proven in [ 42]. Theo-
rem 8.5 was ﬁrst announced in [ 47], but its proof has never been published before.
Using this stronger technical tool we can remove the unnecessary constraint n⁄= 2
in Theorem 1.1 (i) in [ 63] and also upgrade a homotopy of complex structures to a
Stein homotopy.
By using Theorem 8.5 one can similarly strengthen other results from [ 63]. In
particular, in combination with the h-principles for totally real immersions (Corol-
lary 7.28), submersions (Corollary 7.33) and embeddings (Corollary 7.30) one can
prove the following result similar to Theorem 1.4 in [ 63].
Theorem 8.45. Let (V,J,φ ) and (Y,I ) be as in Theorem 8.43.
(a) Let f :V →Y be a continuous map covered by a complex homomorphism
F : TV → TY of maximal rank. Then the holomorphic map g : (h1(V ),J )→
(Y,I ) constructed in Theorem 8.43 can be chosen to be a holomorphic immersion
or submersion withdg homotopic toF|h1(V ) in the class of complex homomorphisms
of maximal rank.
(b) If f is an embedding and F : TV → TY is a complex injective homomor-
phism covering f which is homotopic to df through real injective homomorphisms,
then g can be made a holomorphic embedding isotopic to the embedding f|h1(V ).
Proof. The proof follows the lines of the proof of Corollary 8.39 with the
following modiﬁcation: In each induction step, before applying the Approxima-
tion Theorem 8.33, we use one of the appropriate h-principles for totally real
immersions (Corollary 7.28), submersions (Corollary 7.33) or embeddings (Corol-
lary 7.30) to ﬁnd a C0-small homotopy (resp. isotopy) ﬁxed near ∂∆k of the map
gk−1|∆k to a totally real immersion/submersion (resp. embedding). Then we use
the C1-approximation provided by Theorem 8.33 to approximate gk−1 by a holo-
morphic map gk : Op (V′
k−1∪ ∆k) → Y . Since gk|∆k is a totally real immer-
sion/submersion/embedding (by C1-closeness), the map gk is a holomorphic im-
mersion/submersion/embedding. □
We will introduce later on in Section 11.6 the notion of a Stein homotopy. In
particular, a family of Stein structures ( V,Jt) which share the same exhausting
J-lc function φ is a Stein homotopy. Then Theorem 8.45 implies the following
strengthened version of Theorem 8.16.

8.8. VARIATIONS ON A THEME OF E. KALLIN 181
Theorem 8.46. Let (V,J ) be a complex manifold. Then given any Stein struc-
ture ~J homotopic to J as an almost complex structure, there exists an isotopy
ht :V ↪→V , t∈ [0, 1], with h0 = Id, such that h∗
1J is a Stein structure on V in the
same Stein homotopy class as ~J.
Indeed, to prove this one simply applies Theorem 8.45 to the identity map
(V, ~J)→ (V,J ).
8.8. Variations on a theme of E. Kallin
In this section we prove a lemma closely related to Kallin’s lemma in [109] (see
also [37]). It will only be used in Section 16.2 below.
ForC >0, consider the quadratic function QC : Cn→ R given by the formula
QC(x1,...,x n,y 1,...,y n) =
n∑
1
x2
i +
n−1∑
1
y2
j−Cy2
n.
ForC <1 the function QC is i-convex, while for C >1 it is not. However, each
level set{QC =−a}, a >0, is the union of the two convex, and hence i-convex,
hypersurfaces
yn =±
√
a +x2
1 +··· +y2
n−1
C
for any C >0 (being cooriented by ∇QC). Denote by X the vector ﬁeld
X =
n∑
1
xi
∂
∂xi
+
n−1∑
1
yj
∂
∂yj
−yn
∂
∂yn
.
Lemma 8.47. For any a,C > 0 there exists an i-convex Morse function ψ :
Cn→ R with the following properties:
(i) ψ has a unique critical point at the origin, of index 1, with stable manifold
(with respect to ∇ψψ){x1 =··· = xn = y1 =··· = yn−1 = 0} and
unstable manifold{yn = 0};
(ii) ψ has the hypersurface{QC =−a} as one of its level sets and is convex
in the region{QC≤−a};
(iii) dψ(X)> 0 outside the origin;
(iv) ψ(z1,...,z n−1,zn) =ψ(z1,...,z n−1, ¯zn).
Proof. Forn = 1, let us take any smooth function φ : C→ R with properties
(i-iv) which is equal to x2− 1
2y2 near the origin. Then after an appropriate target
reparametrization the functionφ becomesi-convex (see Lemma 2.7). In the general
case we deﬁne the required function by the formula
ψ(z) :=
n−1∑
1
|zj|2 +φ(zn).
□
Remark 8.48. The hypersurface {QC = −a} in the above lemma can be
replaced by any hypersurface of the form {|yn| = H(x1,...,x n,y 1,...,y n−1)} for
a convex function H.

182 8. THE EXISTENCE THEOREM
yn B′
B
p+ B+
I
p0
p−
B−
{QC = −a}
Figure 8.8. The i-convex function φ.
Corollary 8.49. Consider two disjoint balls B±⊂ Cn. Let I⊂ Cn be the
unique straight line segment connecting ∂B+ and ∂B− and perpendicular to both
boundaries. Then there exists an exhausting i-convex function φ : Cn→ R with the
following properties (see Figure 8.8):
• φ(z) =f(|z|2) outside a large ball containing B+∪B−;
• φ|B+∪B− is convex and has ∂B+∪∂B− as one of its level sets;
• φ has exactly three critical points: two local minima p±∈ B±, and an
index 1 critical point p0∈I with stable disc I (with respect to∇φφ).
Proof. After a unitary rotation we may assume that I ={x1 =··· = xn =
y1 =··· = yn−1 = 0,|yn|≤ b} for some b >0. Pick a ball B around the origin
containingB+∪B− in its interior, and a larger ballB′⊃B. Pick C >1 suﬃciently
large and a> 0 suﬃciently small so that B+∪B−⊂{QC <−a}, where QC is the
quadratic function deﬁned above. Moreover, we picka so small that the vector ﬁeld
X above satisﬁesX·|z|2 > 0 on the region{QC≥−a}∩ (B′\B). Let ψ : Cn→ R
be the i-convex function provided by Lemma 8.47.
Take a convex increasing function f : R→ R such that F (z) :=f(|z|2)<ψ on
B andF (z)>ψ outsideB′, and deﬁne G := smooth max(ψ,F ). As both functions
ψ and F are invariant with respect to the involution σ : Cn → Cn deﬁned by
σ(z1,...,z n) = (z1,...,z n−1, ¯zn), the function G can also be taken to be invariant
with respect to σ. Since X·ψ > 0 and X·F > 0 on {QC ≥− a}∩ (B′\B),
the function G|{QC≥−a} has a unique critical point at the origin, of index 1 and
with stable manifold contained in I. On the region {QC ≤− a} both functions
ψ and F are convex, so according to Remark 3.24 the function G|{QC≤−a} is also
convex and has exactly two critical points, the local minima in the two components
of the domain {QC≤− a}∩ B′. In particular, one of the level sets of G bounds
two convex components Ω± containing the balls B±. Hence there exists a convex

8.8. VARIATIONS ON A THEME OF E. KALLIN 183
function H : Ω−∪ Ω+→ R which has ∂B+∪∂B− and ∂Ω−∪∂Ω+ as level sets.
By reparametrizingG, if necessary, we can arrange thatG>H on∂Ω−∪∂Ω+ and
G<H onB−∪B+. Then the function φ := smooth max(G,H ) has all the required
properties provided that I is contained in the stable manifold of the origin, which
we can ensure e.g. by making the whole construction invariant under the symmetry
(x1,...,y n)↦→ (−x1,..., −yn−1,yn). □
Corollary 8.49 implies the following special case of a lemma of E. Kallin [ 109]:
Corollary 8.50. The union B+∪B− of two disjoint balls in Cn, and hence
the union of any two disjoint compact convex sets with smooth boundary in Cn, is
polynomially convex. Moreover, the union B+∪B−∪I (withI as in Corollary 8.49)
is polynomially convex.
Proof. By Corollary 8.49,B+∪B− is a sublevel set of an exhaustingi-convex
function φ : Cn→ R and hence polynomially convex by Theorem 5.7. Given two
disjoint compact convex sets with smooth boundary, we pick two disjoint balls
B±⊃ K± and modify the exhausting i-convex function φ : Cn→ R provided by
Corollary 8.49 as a convex function inside B+∪B− such that∂K+∪∂K− becomes
a level set. For the last statement we use Theorem 8.23 to deform the function
φ : Cn→ R from Corollary 8.49 to an i-convex surrounding function and apply
Proposition 8.22. □



Part 3
Morse-Smale Theory for J-Convex
Functions



9
Recollections from Morse Theory
In this chapter we recollect some results about smooth functions and vector
ﬁelds that will be needed in the second half of the book. We discuss local normal
forms of functions near critical points, and of vector ﬁelds near zeroes. A crucial
notion is that of a Lyapunov pair consisting of a function and a gradient-like vector
ﬁeld. We discuss deformations of Lyapunov pairs near critical points and prove a
smooth version of the J-convex surroundings in Chapter 8.2.
In Sections 9.6 and 9.7 we introduce the notions about cobordisms that will
play a central role in the discussion of Stein and Weinstein cobordisms in Part IV
of the book: Smale cobordisms and homotopies, elementary cobordisms, proﬁles,
and holonomy. In Section 9.8 we sketch a proof of Smale’s h-cobordism theorem,
based on four geometric lemmas for which we will later prove Stein and Weinstein
analogues in Chapters 10 and 12. Finally, we discuss the two-index theorem of
Hatcher and Wagoner and pseudo-isotopies to which we will return in Chapter 14.
Throughout this chapter, V denotes a smooth manifold and W a cobordism,
both of dimension m.
9.1. Critical points of functions
Let φ : V → R be a smooth function and p∈ V be a critical point of φ, i.e.,
dpφ = 0. The Hessian Hess pφ deﬁnes a symmetric bilinear form on TpV . The
nullity of φ at p is the dimension of ker Hesspφ :={v∈TpV | Hesspφ(v,w ) = 0 for
all w∈TpV}. The (Morse) index atp is the maximal dimension of a subspace on
which the quadratic form v↦→ Hessp(v,v ) is negative deﬁnite. The critical point p
is called nondegenerate if its nullity is zero. It is well-known (see e.g. [ 140]) that a
generic function is Morse, i.e., has only nondegenerate critical points.
Lemma 9.1 (Morse Lemma [ 139]). Near a nondegenerate critical point p of φ
of index k there exist smooth coordinates u∈ Rm mapping p to 0 in which φ has
the form
(9.1) φ(u) =φ(p)−u2
1−···− u2
k +u2
k+1··· +u2
m.
More precisely, this means that for a function φ on a neighborhood of 0 ∈ Rm
there exists a diﬀeomorphism g between neighborhoods of 0 such that g∗φ has the
form (9.1).
Remark 9.2. (1) If the functionφ on a neighborhood of 0∈ Rn already satisﬁes
φ(x1,...,x k, 0,..., 0) =φ(p)−x2
1−···− x2
k, then we can choose the diﬀeomorphism
g to satisfy g(x1,...,x k, 0,..., 0) = (x1,...,x k, 0,..., 0). To see this, apply the
proof of the Morse lemma in [ 139] to ﬁnd new coordinates u1,...,u m near 0 in
whichφ(u) = φ(p)−u2
1−···− u2
k +u2
k+1··· +u2
m. Inspection of the proof shows
that ui =xi on Rk×{ 0}.
187

188 9. RECOLLECTIONS FROM MORSE THEORY
(2) The Morse lemma also holds with parameters as follows: For a compact
manifold (possibly with boundary) K letφz :V → R,z∈K be a smooth family of
functions with a nondegenerate critical of index k at p for all z. Then there exists
a smooth family of diﬀeomorphisms gz : (U, 0) → (Vz,p ) from a neighborhood
U⊂ Rm of 0 onto neighborhoods Vz⊂V of p such that for all z∈K,
φz◦gz(u) =φz(p)−u2
1−···− u2
k +u2
k+1··· +u2
m.
The next lemma shows that near a degenerate critical point one can always
split oﬀ the nondegenerate directions.
Lemma 9.3. Near a critical pointp ofφ indexk and nullity 𝓁 there exist smooth
coordinates (x1,...,x m−k−𝓁,y 1,...,y k,z 1,...,z 𝓁)∈ Rm in which φ has the form
φ(x,y,z ) =x2
1 +··· +x2
m−k−𝓁−y2
1···− y2
k +ψ(z)
with a smooth function ψ(z).
Proof. Set B := Hesspφ and n := m−𝓁. Identify a neighborhood of p in V
with a neighborhood of 0 in Rm = Rn⊕ R𝓁 such that R𝓁 = kerB. Deﬁne a function
F on a neighborhood of 0 in Rm by
F (w,z ) := ∂φ
∂w (w,z ).
Since ∂F
∂w (0, 0) = ∂2φ
∂w 2 (0, 0) is invertible, the zero setF−1(0) is a graphw =w(z) over
R𝓁. After applying a diﬀeomorphism near 0 ∈ Rm we may assume F−1(0) = R𝓁.
Consider the smooth family of functions φz =φ(·,z ) : Rn→ R, z∈ R𝓁 near 0. By
construction, each φz has a nondegenerate critical point of index k at w = 0. Now
Lemma 9.3 follows from the parametrized Morse Lemma in Remark 9.2 □
Let us now describe the critical points that occur in a generic 1-parameter
family of functions φt :V → R,t∈ R. A critical point p of a function φ :V → R is
called embryonic if ker Hesspφ is 1-dimensional and the third derivative of f in the
direction of ker Hesspφ is nonzero. We say that a 1-parameter family of functions
φt : V → R, t∈ R, has a birth-death type critical point p∈ V at t = 0 if p is
an embryonic critical point of φ0 and (0,p ) is a nondegenerate critical point of the
function (t,x )↦→φt(x).
With a family of functions φt :V → R, t∈ R, one can associate its proﬁle (or
Cerf diagram). This is the subset C({φt})⊂ R× R such that C({φt})∩ (t× R)
is the set of critical values of the function φt. If φt is a family of Morse functions
thenC({φt}) is a collection of graphs of smooth functions. Part (b) of the following
theorem shows that birth-death points correspond to cusps of the proﬁle.
Theorem 9.4 (Whitney). (a) Near an embryonic critical point p ofφ of index
k− 1 there exist coordinates (x,y,z )∈ Rm−k⊕ Rk−1⊕ R in which φ has the form
φ(x,y,z ) =φ(p) +|x|2−|y|2 +z3
(b) Suppose that p is a birth-death type critical point of index k− 1 for the family
of functions φt : V → R, t ∈ R, at t = 0 . Then there exist families of local
diﬀeomorphismsft :Opp→O p 0⊂ Rm and gt :Opφ0(p)→O p 0⊂ R, t∈O p 0,
such that the family of functions ψt =gt◦φt◦f−1
t has the form
(9.2) ψt(x,y,z ) =|x|2−|y|2 +z3±tz
for (x,y,z )∈ Rm−k⊕ Rk−1⊕ R.

9.2. ZEROES OF VECTOR FIELDS 189
(c) Let φt,~φt :V → R be two families of functions with birth-death type critical
pointsp,~p at t = 0 of the same index and with the same proﬁle. Then there exist a
family of local diﬀeomorphisms ht :Opp→O p~p, t∈O p 0, such that ~φt◦ht =φt.
(d) A generic 1-parameter family of functions φt :V → R has only nondegen-
erate and birth-death type critical points.
In particular, part (a) shows that embryonic critical points are isolated. We
say that a birth-death type critical point p is of birth type if the sign in front of t
in formula (9.2) is minus, and of death type otherwise. Note that near a birth type
critical point a pair of nondegenerate critical points of indices k andk− 1 appears
at t = 0, and near a death type critical point such a pair disappears.
Proof. Part (d) follows from a standard transversality argument. Using
Lemma 9.3 we can reduce parts (a-c) to the case m = 1 of functions R→ R.
Form = 1 this result is essentially proved in [ 192]. In the present formulation it
can be proved as follows.
For (a), it is easy to see that every function R→ R with an embryonic point
equals z3 in a suitable coordinate z, see e.g. [ 129, Proposition III 1.2].
For (b), consider a family of functions φt : R→ R with a birth-death type
critical point p at t = 0. It follows e.g. from [ 129, Theorem IV 6.1] that there
exists a family of local diﬀeomorphisms ft :Opp→O p 0⊂ R such that
φt◦f−1
t (z) =z3±a(t)z +b(t)
with smooth functions a,b : R→ R such that a(0) = 0 and s a′(0) > 0. With
gt(y) := y−b(t) we then have ~φ(z) := gt◦φt◦f−1
t (z) = z3±a(t)z. Finally,
the diﬀeomorphisms ~ft(z) =
(
t
a(t)
)1/2
z and~gt(y) =
(
t
a(t)
)3/2
y transform ~φt into
~gt◦~φt◦ ~f−1
t (z) =z3±tz.
For (c), consider two families of functionsφt,~φt : R→ R with death type critical
points at t = 0 and equal proﬁles (the birth case is similar). By the discussion in
(b), after composing φt,~φt with suitable families of diﬀeomorphisms ft,~ft : R→ R
we may assume φt(z) = z3 +a(t)z +b(t) and ~φt(z) = z3 +~a(t)z +~b(t). Equality
of the proﬁles implies a(t) = ~a(t) and b(t) = ~b(t) for all t≤ 0, hence φt = ~φt
for t≥ 0. We look for the desired family of local diﬀeomorphisms in the form
ht(z) =z +gt(z), t∈ R, where gt≡ 0 for t≤ 0. Then ~φt◦ht =φt is equivalent to
gt(z)3 + 3zgt(z)2 +
(
3z2 +~a(t)
)
gt(z) =
(
a(t)−~a(t)
)
z +b(t)−~b(t).
Recall that ~a(0) = 0 and ~a′(0) > 0, so the coeﬃcient 3 z2 +~a(t) is positive for all
t >0. Looking at the discriminant, one sees that this third order equation has a
unique real solution gt(z) for all t≥ 0 which depends smoothly on t≥ 0 and z.
Since the right hand side vanishes to inﬁnite order at t = 0, the solution gt(z) also
vanishes to inﬁnite order att = 0 and hence extends smoothly by zero to t< 0. □
9.2. Zeroes of vector ﬁelds
LetX be a smooth vector ﬁeld on V andp∈V be a zero ofX. The diﬀerential
DpX :TpV →TpV induces a splitting into invariant subspaces
TpV =E+
p ⊕E−
p ⊕E0
p,

190 9. RECOLLECTIONS FROM MORSE THEORY
whereE+
p (resp.E−
p ,E0
p) is spanned by the generalized eigenvectors corresponding
to eigenvalues with positive (resp. negative, vanishing) real part. The dimension of
E−
p is called the (Morse) index 1 of X at p. Denote by Xs : V → V , s∈ R, the
ﬂow of X.
Theorem 9.5 (center manifold theorem [ 4]). Let p∈ V be a zero of a Cr+1-
vector ﬁeld X, r∈ N. Then there exist the following local Xs-invariant manifolds
throughp:
• W 0±
p tangent to E0
p⊕E±
p of class Cr+1;
• W±
p ⊂W 0±
p tangent to E±
p of class Cr;
• W 0
p =W 0+
p ∩W 0−
p tangent to E0
p of class Cr+1.
The W±
p are unique, and they are smooth resp. real analytic if X is.
W−
p (resp. W +
p , W 0
p , W 0−
p , W 0+
p ) are called the local stable (resp. unstable,
center, center-stable, center-unstable) manifold atp. The center, center-stable and
center-unstable manifolds are in general not unique, and they need not be smooth
even if X is. By the center manifold theorem we can choose Cr-coordinates Z =
(x,y,z )∈E+
p⊕E−
p⊕E0
p in whichW±
p andW 0±
p correspond toE±
p resp.E0
p⊕E0±
p .
In these coordinates X is of the form
(9.3) X(x,y,z ) = (A+x +O(|x||Z|),A−y +O(|y||Z|),A 0z +O(|z||Z| +|x||y|)
with linear mapsA+ (resp.A−,A0) all of whose eigenvalues have positive (resp. neg-
ative, zero) real part. (The speciﬁc form of the higher order terms follows from
tangency of X to W±
p and W 0±
p ).
A zero p of a vector ﬁeld X is called nondegenerate if all its eigenvalues are
nonzero. It is called hyperbolic ifE0
p ={0}, i.e., all eigenvalues ofDpX have nonzero
real part. In this case we have global stable and unstable manifolds characterized
by
(9.4) W±
p ={x∈V | lim
s→∓∞
Xs(x) =p}.
They are injectively immersed (but not necessarily embedded) in V . For a hyper-
bolic zero the local representation (9.3) simpliﬁes to
(9.5) X(x,y ) = (A+x +O(|x||Z|),A−y +O(|y||Z|)).
Let us call a zero p embryonic if E0
p is 1-dimensional and the restriction of X
to a center manifold W 0
p has nonvanishing second derivative at p (for some local
coordinate on W 0
p ∼= R; the deﬁnition depends neither on this local coordinate
nor on the choice of W 0
p ). It follows that in suitable coordinates Z = (x,y,z )∈
Rm−k⊗ Rk−1⊗ R near p the vector ﬁeld is of the form
(9.6)
X(x,y,z ) =
(
A+x +O(|x||Z|),A−y +O(|y||Z|),
z2 +O
(
|z| (|x| +|y| +|z|2) +|x||y|
))
with linear maps A+, A− all of whose eigenvalues have positive resp. negative real
part.
1Not to be confused with the topological index of a vector ﬁeld at an isolated zero.

9.2. ZEROES OF VECTOR FIELDS 191
U ∩ ˆW −
p
y
z
Figure 9.1. The ﬂow near an embryonic zero.
Lemma 9.6. Letp be an embryonic zero of a smooth vector ﬁeld X. Then
ˆW±
p :={x∈V | lim
s→∓∞
Xs(x) =p}
is an injectively immersed smooth manifold with boundary W±
p .
Proof. (cf. [175]). Pick coordinates Z = (x,y,z ) on a neighborhood U of p
in which X is of the form (9.6). We claim that
U∩ˆW−
p ={(x,y,z )∈U|x = 0, z≤ 0},
see Figure 9.1. Since this is a smooth submanifold of U with boundary U∩W−
p =
{(x,y,z )∈U|x =z = 0}, the claim implies the statement for ˆW−
p by invariance
under the ﬂow of X and the statement for ˆW +
p is proved analogously.
To prove the claim, consider a ﬂow line
(
x(t),y (t),z (t)
)
starting at t = 0 at
(x0,y 0,z 0) ∈ U. It follows from (9.6) that x(t) → 0 as t → ∞if and only if
x(t)≡ 0. Moreover, the second component decays exponentially, |y(t)|≤ e−λt, for
some λ >0. Inserting this in the equation for z yields the estimate (for possibly
smaller λ> 0)
(9.7) ˙ z≥z2/2−e−λt|z|.
Moreover, the equation for z in (9.6) shows that z(t) cannot change its sign.
Ifz0 > 0 inequality (9.7) yields d
dt lnz≥z/2−e−λt≥−e−λt, which integrates
to lnz(t)− lnz0≥ (e−λt− 1)/λ≥− 1/λ and hence z(t)≥z0e−1/λ > 0. Thus z(t)
does not tend to 0 as t→∞ , and hence (0,y 0,z 0) /∈ˆW−
p .
Ifz0 < 0 we have for everyt1≥ 0 the following dichotomy: Either the right hand
side of (9.7) is≥z2/4, in which casez grows likez(t)≥
(
1/z(t1)−(t−t1)/4
)−1
for
t≥t1; or the right hand side of (9.7) is≤z2/4, which means thatz(t1)≥− 4e−λt1.
This shows that z(t)→ 0 as t→∞ , and hence (0,y 0,z 0)∈ˆW−
p . □
We say that a 1-parameter family Xt, t∈ (−ε,ε ) of vector ﬁelds near p∈V is
of birth-death type if p is an embryonic zero of X0 and the section (t,Z )↦→Xt(Z)
is transverse to the zero section of the bundle TM → R×M at (0,p ). It follows
that in suitable coordinates Z = (x,y,z )∈ Rm−k⊗ Rk−1⊗ R near p the family is

192 9. RECOLLECTIONS FROM MORSE THEORY
of the form
(9.8)
Xt(x,y,z ) =
(
A+
t x +O(|x||Z|), A−
t y +O(|y||Z|),
z2±t +O
(
(|z| +|t|) (|x| +|y| +|z2±t|) +|x||y|
))
with smooth families of linear maps A±
t all of whose eigenvalues have positive
resp. negative real part. (The speciﬁc form of the higher order terms follows from
tangency of the vector ﬁeld ˆX(t,Z ) =
(
0,Xt(Z)
)
on R×M to{0}× W±
p and
R×W 0
p , plus the fact that in suitable coordinates the zero set of ˆX is the curve
{x =y =z2±t = 0}, see [175]).
We say that the family is of birth type if the sign in z2±t in (9.8) is minus,
and of death type otherwise. Note that in a birth type family a pair of hyperbolic
zeroes of indices k and k− 1 appears at t = 0 and in a death type family such a
pair disappears.
Lemma 9.7. (a) A generic vector ﬁeld has only hyperbolic zeroes.
(b) In a generic 1-parameter family of vector ﬁelds without nonconstant periodic
orbits only birth-death type degeneracies appear.
Proof. (a) follows from general transversality arguments.
(b) In a generic 1-parameter family of vector ﬁelds only two types of degenera-
cies appear (see [ 11]§§32− 33): The ﬁrst type corresponds to birth-death type;
the second type corresponds to a Hopf bifurcation in which a nonconstant periodic
orbit appears or disappears att = 0, which is excluded by the hypothesis of (b). □
9.3. Gradient-like vector ﬁelds
In the previous two subsections we have studied functions and vector ﬁelds
independently. Now we will look at them jointly. We call a smooth function φ :
V → R a Lyapunov function for X, and X gradient-like for φ, if
(9.9) X·φ≥δ(|X|2 +|dφ|2)
for some δ >0, where|X| is the norm with respect to some Riemannian metric on
V and|dφ| is the dual norm. We call φ a weak Lyapunov function for a vector ﬁeld
X, and X weakly gradient-like for φ, if zeroes of X coincide with critical points of
φ and X·φ> 0 outside the zeroes of X. A pair ( X,φ ) consisting of a vector ﬁeld
and a (weak) Lyapunov function will be called a (weak) Lyapunov pair.
By the Cauchy-Schwarz inequality, condition (9.9) implies
(9.10) δ|X|≤| dφ|≤ 1
δ|X|.
In particular, zeroes of X coincide with critical points of φ, so every Lyapunov pair
is also a weak Lyapunov pair.
Lemma 9.8. (a) If X0,X 1 are (weakly) gradient-like vector ﬁelds for φ, then
so is f0X0 +f1X1 for any nonnegative functions f0,f 1 with 0<ε ≤f0 +f1≤ 1/ε.
(b) If φ0,φ 1 are (weak) Lyapunov functions for X, then so is λ0φ0 +λ1φ1 for
any nonnegative constants λ0,λ 1 with λ0 +λ1 > 0.
In particular, the following spaces are convex cones and hence contractible:
• the space of (weak) Lyapunov functions for a given vector ﬁeld X;
• the space of (weakly) gradient-like vector ﬁelds for a given function φ.

9.3. GRADIENT-LIKE VECTOR FIELDS 193
Proof. The condition on a weak Lyapunov pair is obviously preserved under
positive combinations of the functions or vector ﬁelds. To see that condition (9.9)
is preserved under positive combinations (with changing δ) of vector ﬁelds, con-
sider two vector ﬁelds X0,X 1 satisfying Xi·φ≥δi(|Xi|2 +|dφ|2) and nonnegative
functions f0,f 1 with f0 +f1≥ ε > 0. Then the vector ﬁeld X = f0X0 +f1X1
satisﬁes (9.9) with δ := min
{
δ0
2f0
, δ1
2f1
,f 0δ0 +f1δ1
}
:
X·φ≥f0δ0|X0|2 +f1δ1|X1|2 + (f0δ0 +f1δ1)|dφ|2
≥ 2δ(|f0X0|2 +|f1X1|2) +δ|dφ|2
≥δ(|X|2 +|dφ|2).
Positive combinations of functions are treated analogously. □
Lyapunov pairs near critical points. Consider a Lyapunov pair ( X,φ )
and a (possibly degenerate) zero p of X. Then p is also a critical point of φ, so in
coordinates Z near p ={Z = 0} we have
X(Z) =AZ +O(|Z|2), φ (Z) =φ(p) + 1
2B(Z,Z ) +O(|Z|3)
with the linear map A := DpX and the symmetric bilinear form B := Hesspφ.
Gradient-likeness
X·φ(Z) =B(Z,AZ ) +O(|Z|3)≥δ
(
|AZ|2 +|B(Z,·)|2
)
+O(|Z|3)
yields
(9.11) B(v,Av )≥δ
(
|Av|2 +|B(v,·)|2
)
.
Lemma 9.9. Suppose a linear map A :V →V and a symmetric bilinear form
B :V×V → R satisfy (9.11). Then:
(a) All nonzero eigenvalues of A have nonzero real part.
(b) There exists an A-invariant splitting V =E+⊕E−⊕E0, where
E0 = kerA, E ± ={v| lim
t→∓∞
etAv = 0}.
(c) B is positive deﬁnite on E+ and negative deﬁnite on E−.
(d) A is nondegenerate if and only if B is nondegenerate. Moreover, in this
case condition (9.11) is equivalent to an inequality
B(v,Av )≥β|v|2, β > 0.
Proof. (a) Extend A C-linearly to the complexiﬁed space V⊗ C and extend
B to V⊗ C by
B(x +iy,x′ +iy′) :=
(
B(x,x′) +B(y,y′)
)
+i
(
B(y,x′)−B(x,y′)
)
.
ThusB is C-linear in the ﬁrst and C-antilinear in the second argument, B(v,w ) =
B(w,v ), and Re B(v,Av )≥δ|Av|2. Let 0 ⁄=v∈V⊗ C be an eigenvector of A to
an eigenvalueλ∈ C, i.e., Av =λv. Then
λB(v,Av ) =B(Av,Av ) =B(Av,Av ) = ¯λB(v,Av ).
Suppose now that λ⁄= 0 is purely imaginary. Then it follows that B(v,Av ) =
−B(v,Av ), so with v =x +iy, x,y∈V we ﬁnd
0 = ReB(v,Av ) =B(x,Ax ) +B(y,Ay )≥δ(|Ax|2 +|Ay|2).

194 9. RECOLLECTIONS FROM MORSE THEORY
But then Ax =Ay = 0, which implies 0 = Av =λv and hence (since λ⁄= 0)v = 0,
in contradiction to the assumption v⁄= 0.
(b) follows from Sections 22.2 and 22.3 in [ 9].
(c) The ﬂow etA preserves E± and satisﬁes d
dtφ(etAZ)≥ δ|AetAZ|2 > 0 for
0⁄=Z∈E±. For 0⁄=Z∈E+ it follows that
φ(Z)− 0 =
∫ 0
−∞
d
dtφ(etAZ)> 0,
and similarly φ(Z)< 0 for 0⁄=Z∈E−.
(d) Nondegeneracy of A orB gives an estimate B(v,Av )≥β|v|2,β >0, which
in turn implies nondegeneracy of A and B. □
Remark 9.10. Suppose that X is the gradient of φ with respect to a positive
deﬁnite but not necessarily symmetric (2, 0) tensor ﬁeld g, i.e., dφ(v) =g(X,v ) for
allv∈TV andg(v,v )> 0 for all v⁄= 0. Then X is gradient-like for φ. At a zero p
of X we have Hesspφ(v,w ) =gp(DpX·v,w ).
If g is symmetric (i.e., a Riemannian metric), then so is the bilinear form
Hesspφ(·,DpX·) =gp(DpX·,DpX·) and all eigenvalues of DpX are real.
Remark 9.11. By Lemma 9.9 (a), for a Lyapunov pair ( X,φ ) each nondegen-
erate zero of X is hyperbolic. Lemma 9.9 (d) can be rephrased as follows: For a
Lyapunov pair (X,φ ), a zero p of X is nondegenerate if and only if it is a nonde-
generate critical point of φ. Moreover, in this case gradient-likeness is equivalent
to an inequality
X·φ(Z)≥β|Z|2, β > 0
in coordinates Z near p ={Z = 0}.
We use this criterion to derive a technical result about perturbations of Lya-
punov functions.
Lemma 9.12. (a) Letp be a hyperbolic critical point for a Lyapunov pair (X,φ ).
If (Y,ψ ) is another Lyapunov pair with p as hyperbolic critical point and ψ suﬃ-
ciently C2-close to φ, then ψ is also a Lyapunov function for X nearp.
(b) Let p be an embryonic critical point for a Lyapunov pair (X,φ ). If (Y,ψ )
is another Lyapunov pair with p as embryonic critical point with the same null
direction and ψ suﬃciently C3-close to φ, then ψ is also a Lyapunov function for
X nearp.
Proof. (a) Write
X(Z) =AZ +O(|Z|2),
in coordinates near p, where all eigenvalues of A have nonzero real part. Then φ is
a Lyapunov function for X near p if and only if
φ(Z) = 1
2⟨Z,BZ⟩ +O(|Z|3), BA> 0.
This implies the assertion of the lemma because BA> 0 is a C2-open condition on
φ.
(b) Pick coordinates Z = (w,z ) near p in whichX has the form (see (9.6) with
w = (x,y ))
X(w,z ) =
(
Aw +O(|w||Z|),z 2 +O
(
z(|w| +z2) +|w|2))
.

9.3. GRADIENT-LIKE VECTOR FIELDS 195
Claim: φ is a Lyapunov function for X near p if and only if it has the form
φ(w,z ) = 1
2⟨w,Bw⟩ + 1
3cz3 + 2z2⟨d,w⟩ +O(|w|2|Z|) +O(|Z|4),
where the coeﬃcients B,c,d satisfy
(
BA A td
dtA c
)
> 0.
From this the assertion of the lemma follows because ψ has a Taylor expansion of
the same form and the positivity condition on the coeﬃcients is C3-open. To prove
the claim, let us write the general Taylor expansion up to second order of a function
φ with critical point at p:
φ(w,z ) = 1
2⟨w,Bw⟩ +az2 +z⟨b,w⟩ +O(|Z|3).
The condition X·φ > 0 restricted to {z = 0} and{w = 0} yields BA > 0 and
a = 0. If b were nonzero we could pick ( w,z ) with z⟨b,Aw⟩ < 0 and obtain the
contradiction
X·φ(t2w,tz ) =t3z⟨b,Aw⟩ +O(t4)< 0
for t >0 suﬃciently small. Thus b = 0 and the Taylor expansion of φ up to third
order has the form in the claim. Then
X·φ(w,z ) =⟨w,BAw⟩ +cz4 + 2z2⟨d,Aw⟩ +O(|w|2|Z|) +O(|w|z3) +O(|Z|5).
This is a quadratic form in the variables (w,z 2) plus terms of order 5/2 and higher,
so it is positive if and only if the quadratic form is positive, which is precisely the
positivity condition in the claim. □
Next we show that a suﬃciently nondegenerate Lyapunov pair can be put
into standard form near critical points without changing the stable and unstable
manifolds.
Proposition 9.13. Let (X,φ ) be a Lyapunov pair with nondegenerate or em-
bryonic critical points. Then there exists a homotopy of Lyapunov pairs (Xt,φt)
with the following properties:
• (Xt,φt) agrees with (X,φ ) for t = 0 and outside a neighborhood of the
critical points;
• for all t, Xt has the same nondegenerate resp. embryonic criticial points
and the same stable, unstable and center manifolds as X0;
• near each nondegenerate critical point of index k there exist coordinates
x1,...,x n in which
X1 =−
k∑
i=1
xi∂xi +
n∑
j=k+1
xj∂xj, φ 1 =−1
2
k∑
i=1
x2
i + 1
2
n∑
j=k+1
x2
j.
• near each embryonic critical point of index k− 1 there exist coordinates
x1,...,x n in which
X1 =x2
1∂x1−
k∑
i=2
xi∂xi +
n∑
j=k+1
xj∂xj, φ 1 = x3
1
3 − 1
2
k∑
i=2
x2
i + 1
2
n∑
j=k+1
x2
j.

196 9. RECOLLECTIONS FROM MORSE THEORY
Similarly, each birth-death family (Xt,φt) can be modiﬁed through birth-death fam-
ilies to one which near the birth-death point at t = 0 looks like
Xt = (x2
1±t)∂x1−
k∑
i=2
xi∂xi +
n∑
j=k+1
xj∂xj, φ t = x3
1
3 ±tx1− 1
2
k∑
i=2
x2
i + 1
2
n∑
j=k+1
x2
j.
Proof. Near a nondegenerate zero p of index k pick local coordinates Z =
(x,y )∈ R𝓁⊕ Rk, 𝓁 = m−k, in which X is given by (9.5). Note that in these
coordinates W +
p = R𝓁⊕ 0 and W−
p = 0 ⊕ Rk. The linear vector ﬁeld AZ =
(A+x,A−y) has the same stable and unstable manifolds and is also gradient-like
for φ in a suﬃciently small neighborhood of p, so by Lemma 9.8 the same holds
for the vector ﬁelds Xt(Z) :=
(
1−tρ(|Z|)
)
X(Z) +tρ(|Z|)AZ, where t∈ [0, 1] and
ρ : [0,∞)→ [0, 1] equals 0 near 0 and 1 on [ε,∞) for suﬃciently small ε> 0. After
renamingX1 back to X, we may hence assume that X(Z) =AZ nearp. A similar
argument allows us to replace φ by its quadratic part 1
2B(v,v ) (here we need to
choose the cutoﬀ function ρ more carefully such that rρ′(r)≤ 1). By Lemma 9.9
the symmetric bilinear form B satisﬁes B(Z,AZ )≥ β|Z|2 for some β >0 and its
restrictions B± to W±
p are positive resp. negative deﬁnite.
Consider the split quadratic form B1(Z,Z ) := B+(x,x ) +B−(y,y ) and the
family Bt(Z) := (1 − t)B(Z,Z ) + tB1(Z,Z ), t ∈ [0, 1]. Since B(Z,AZ ) and
B1(Z,AZ ) = B+(x,A +x) + B−(y,A−y) are both positive, so is Bt(Z,AZ ) for
all t∈ [0, 1]. This allows us (again via cutoﬀ away from p) to replace B by B1.
Now consider the family of linear maps At(Z) := (1−t)AZ +t(x,−y), which sat-
isﬁesB(Z,AtZ)> 0 for all t∈ [0, 1]. So we can replace the linear vector ﬁeld A by
the standard vector ﬁeld A1(Z) = (x,−y). Finally, we linearly interpolate for this
vector ﬁeld fromB1 to the standard quadratic form B2(Z) =|x|2−|y|2. Renaming
y = (x1,...,x k) and (x =xk+1,...,x m), the pair (A1,B 2) has the desired standard
form.
The proofs in the embryonic and birth-death case are similar and will be omit-
ted. □
The following corollary shows that a Lyapunov pair can be arbitrarily altered
near a hyperbolic or embryonic critical point. In Section 12.4 we will prove a version
of this result for Weinstein structures.
Corollary 9.14. Let p∈ V be a hyperbolic (resp. embryonic) critical point
of a Lyapunov pair (X,φ ). Let (Xloc,φ loc) be a Lyapunov pair on a neighborhood
Vloc of p such that p is a hyperbolic (resp. embryonic) critical point of φloc of value
φloc(p) =φ(p) and Morse index indp(φloc) = indp(φ). Then there exists a homotopy
of Lyapunov pairs (Xt,φt) on V with the following properties:
(i) (X0,φ 0) = (X,φ ) and (Xt,φt) = (X,φ ) outside Vloc;
(ii) Xt has a unique hyperbolic (resp. embryonic) zero at p in Vloc for all t;
(iii) (X1,φ 1) = (Xloc,φ loc) nearp;
(iv) if W−
p (Xloc) = W−
p (X) (resp. ˆW−
p (Xloc) = ˆW−
p (X)) then W−
p (Xt) =
W−
p (X) (resp.ˆW−
p (Xt) =ˆW−
p (X)) for all t.
Proof. After moving (X,φ ) by a diﬀeotopy we may assume that p has the
same stable, unstable and center manifolds with respect to X andXloc. By Propo-
sition 9.13, there exists a homotopy ( Xt,φt), t∈ [0, 1/2], with properties (i-ii) and
(iv) such that (X1/2,φ 1/2) has standard form near p. Reversing the argument in

9.3. GRADIENT-LIKE VECTOR FIELDS 197
Proposition 9.13, there exists a homotopy (Xt,φt),t∈ [1/2, 1], with properties (i-ii)
and (iv) such that (X1,φ 1) = (Xloc,φ loc) on a smaller neighborhood of p. □
From gradient-like to gradient vector ﬁelds. By Remark 9.10, imaginary
eigenvalues of DpX provide an obstruction to C1-approximating X by a gradient
vector ﬁeld. But we have the following C0-approximation result.
Lemma 9.15. Let (X,φ ) be a Lyapunov pair on V and Z the zero set of X.
Then for every neighborhood U ofZ there exists a Riemannian metric g onV such
that∇gφ agrees with X outside U and is arbitrarily C0-close to X on U. This
construction also works smoothly for families and relative to a subset where X is
already a gradient.
Proof. Pick a reference metricg0 for which condition (9.9) holds. It implies on
V\Z the uniform estimates δ|X|≤|∇ g0φ|≤| X|/δ for the lengths and cos θ≥δ2
for the angle θ between X and∇g0φ. Thus we can pick a metric g1 on V \Z
of uniformly bounded distance from g0 for which ∇g1φ = X. Modify g1 inside
U to a metric g which smoothly extends over Z and still has bounded distance
from g0. Then ∇gφ agrees with X outside U and in U it satisﬁes an estimate
|X−∇ gφ| ≤ |X| +C|dφ|, which can be made arbitrarily small by choosing U
small. □
Corollary 9.16. Let (Xλ,φλ)λ∈Λ be a smooth family of Lyapunov pairs on
V , and ψλ any family of functions Ck-close to φλ, k≥ 1. Then there exists a
family of metrics gλ such that the family (∇gλψλ,ψλ) is connected to (Xλ,φλ) by
a homotopy of families of Lyapunov pairs that is C0-small in the vector ﬁelds and
Ck-small in the functions.
Proof. First linearly homotope (with ﬁxed functions) from ( Xλ,φλ) to
(∇gλφλ,φλ), with the metrics gλ provided by Lemma 9.15, and then through gra-
dient pairs (with ﬁxed metrics) from (∇gλφλ,φλ) to (∇gλψλ,ψλ). □
Existence of Lyapunov functions. The question of existence of a (weak)
Lyapunov function for a vector ﬁeld X separates into two issues: local existence
near the zero set of X, and global existence. Assuming local existence near the
zero set, Sullivan [ 181] gives a necessary and suﬃcient criterion for the existence
of a global (weak) Lyapunov function in terms of foliation cycles. The simplest
obstruction to a weak Lyapunov function is a nonconstant periodic orbit of X.
The following lemma settles the local existence question near a hyperbolic or
birth-death type zero.
Lemma 9.17. (a) Near each hyperbolic zero a vector ﬁeld admits a Lyapunov
function.
(b) For a birth or death type family Xt nearp there exists a neighborhood U of
p and a smooth family of Lyapunov functions φt :U→ R for Xt.
Proof. (a) Consider coordinates in which X has the form (9.5). By [ 9, Theo-
rem 22.3] there exist quadratic forms Q± onE±
p which are Lyapunov for the linear
maps A±. Then φ(x,y ) :=Q+(x) +Q−(y) is a Lyapunov function for X.
(b) Consider coordinates in which Xt has the form (9.8). Let Q±
t be a smooth
family of quadratic forms on E±
p as in (a) that are Lyapunov for A±
t . Then
φt(x,y,z ) :=Q+
t (x) +Q−
t (y) + 1
3z3−tz

198 9. RECOLLECTIONS FROM MORSE THEORY
is a smooth family of Lyapunov functions for Xt. □
9.4. Smooth surroundings
In this section we discuss a smooth version of the J-convex surroundings in
Chapter 8.2.
By a ﬂow box (W,X ) we will mean a compact manifold with corners whose
boundary is a union ∂W =∂+W∪∂−W∪∂vW of three codimension one manifolds
(called the positive, negative resp. vertical boundary), together with a vector ﬁeldX
which is inward resp. outward pointing along ∂±W , and tangent to ∂vW without
zeroes on ∂vW . Note that the case ∂vW = ∅ corresponds to a cobordism. We
denote by Xt the ﬂow of X and deﬁne the skeleton
Skel(W,X ) :=
⋂
t≥0
X−t(W ) :={x∈W|Xt(x)∈W for all t≥ 0}.
Forx∈W deﬁne the ω-limit set
ω(x) :=
⋂
t≥0
X≥t(x) ={y∈W|Xtk(x)→y for some sequence tk→∞}.
For each zero p of X deﬁne
ˆW−
p :={x∈W|p∈ω(x)} ={x∈W|Xtk(x)→p for some sequence tk→∞}.
Lemma 9.18. If X admits a weak Lyapunov function φ, then ω(x)⊂ Zero(X)
for each x∈W . If in addition X has ﬁnitely many zeroes, then
Skel(W,X ) =
⋃
p∈Zero(X)
ˆW−
p .
The set ˆW−
p agrees with the stable manifold W−
p if p is hyperbolic, and with the
manifold ˆW−
p in Lemma 9.6 if p is embryonic.
Proof. Fory /∈ Zero(X) we haveX·φ≥ε> 0 on some neighborhood U ofy.
This implies that a trajectory Xt(x) passing close to y will haveφ(Xt0(x))>φ (y)
for some t0 > 0 and hence cannot get close to y for t > t0, so y /∈ ω(x). This
proves ω(x)⊂ Zero(X). The second statement follows from the equivalence of
x∈ Skel(W,X ) and ω(x)⁄= ∅, and the last statement follows from equation (9.4)
and Lemma 9.6. □
In the following, ( W,X ) is a ﬂow box with skeleton ∆ := Skel( W,X ), and
φ :W→ [a−,a +] is a function satisfying X·φ> 0 outside ∆ with constant values
φ|∂±W≡a±.
The following is a (much simpler) smooth version of Theorem 8.5, see Figure 8.2.
Proposition 9.19. Let (W,X,φ, ∆) be as above. Fix an open neighborhood U
of ∂−W∪ ∆ and a regular value c∈ (a−,a +) of the function φ such that there are
no critical values of φ in [c,a +]. Then there exists a diﬀeotopy ht :W→W with
the following properties:
• h0 = Id and ht = Id onOp (∂W∪ ∆);
• ht preserves trajectories of X;
• h1({φ≤c})⊂U.
In particular, φt :=φ◦h−1
t , t∈ [0, 1], is a family of functions satisfying X·φt > 0
outside ∆ such that the level set {φ1 =c} surrounds∂−W∪ ∆ in U.

9.4. SMOOTH SURROUNDINGS 199
Proof. Pick a smooth functionρ :W→ [0, 1] which equals 0 onOp (∂W∪∆)
and 1 on{φ≤c}\ U. Then the vector ﬁeld Y :=ρX is complete, i. e. its ﬂow Yt
is deﬁned for all t∈ R, and Yt = Id onOp (∂W∪ ∆). Moreover, by deﬁnition of
the skeleton there exists T > 0 such that Y−T ({φ≤ c})⊂ U. Hence the isotopy
ht :=Y−Tt , t∈ [0, 1], has the required properties. □
In the next section we will need a more precise version of smooth surroundings.
We call a subset A⊂ W backward invariant if Xt(A)⊂ A for all t≤ 0. For a
compact backward invariant subset A⊂W we deﬁne its exit set
∂+A :={x∈A| inf{t> 0|Xt(x) /∈A} = 0}.
Thus every forward orbit that exits A exits through ∂+A. Note that φ(x) >
min∂+Aφ for every x /∈A whose backward orbit meets A.
Lemma 9.20. Let (W,X,φ, ∆) be as above. Fix a compact backward invariant
neighborhoodA of ∆ and set c := min ∂+Aφ. Let g : [a−,a +]→ [a−,a +] be a
diﬀeomorphism which equals the identity near ∂[a−,a +] and satisﬁes g(x)≤x for
x≥c. Then for every compact neighborhood A′⊂ IntA of ∆ there exists a function
ψ :W→ R satisfying X·ψ >0 outside ∆ with the following properties:
• ψ =φ onOp∂W and outside A;
• ψ =g◦φ on A′.
Proof. Let us rescale X such that X·φ≡ 1 outside A. For t∈ [0, 1] deﬁne
diﬀeomorphismsgt(x) := (1−t)x+tg(x) on [a−,a +] and functionsft : [a−,a +]→ R,
ft
(
gt(x)
)
:= ˙gt(x) =g(x)−x.
Note thatft = 0 near∂[a−,a +] andft(x)≤ 0 forx≥c. Pick a smooth function ρ :
W→ [0, 1] which equals 1 outsideA and 0 onA′. Deﬁne a family of diﬀeomorphisms
ht :W→W as the solution of
˙ht = (ft◦φρX )(ht).
Note thatht moves backwards along trajectories ofX in the region{φ≥c}. Hence,
by deﬁnition of c,h1(x) /∈A implies that ht(x) /∈A for all t∈ [0, 1]. For such x we
haveρ◦ht(x) = 1 and thus
d
dt(φ◦ht(x) =dφ· (ft◦φX )
(
ht(x)
)
=ft◦φ◦ht(x).
Since d
dt(gt◦φ)(x) = ˙gt◦φ(x) = ft◦gt◦φ(x), the paths φ◦ht(x) and gt◦φ(x)
satisfy the same diﬀerential equation with the same initial conditionφ(x) and hence
coincide, so in particular φ◦h1(x) =g◦φ(x) wheneverh1(x) /∈A. This shows that
the function ψ :=g◦φ◦h−1
1 agrees with φ outsideA. On A′ we haveρ = 0, hence
h1 = Id and ψ =g◦φ. □
Replacing a given neighborhood by a smaller backward invariant one and choos-
ingg(max ∆φ)<b , this implies the following improved version of Proposition 9.19.
Corollary 9.21. Let (W,X,φ, ∆) be as above. Then for every neighborhood
U⊂W of ∆ and every b∈ (a−,a +) there exists a function ψ :W→ R satisfying
X·ψ >0 outside ∆ with the following properties:
• ψ =φ onOp∂W and outside U;
• ψ is target equivalent to φ near ∆;
• ψ|∆ <b . □

200 9. RECOLLECTIONS FROM MORSE THEORY
Remark 9.22. The last three results continue to hold if ∆ ⊂ W is any com-
pact backward invariant subset containing Skel(W,X ). To see this, pick a smooth
function f : W→ [0,∞) which vanishes exactly on ∆. Then ∆ is the skeleton of
the vector ﬁeld fX and fX·φ >0 outside ∆, so we can apply the results to the
quadruple (W,fX,φ, ∆).
9.5. Changing Lyapunov functions near critical points
In this section we show that a weak Lyapunov function can be put into any pre-
scribed form near a hyperbolic or birth-death type zero. The following proposition
will be used repeatedly in the manipulations of Weinstein structures in Chapter 12.
Proposition 9.23. (a) Let X be a vector ﬁeld on V with a hyperbolic or
embryonic zero p. Let φ : V → R be a weak Lyapunov function for X and φloc :
U→ R a weak Lyapunov function on a neighborhood U of p with φ(p) = φloc(p).
Then there exists a weak Lyapunov function ψ :V → R which agrees with φ outside
U and with φloc nearp.
(b) Let Xt, t∈ [−ε,ε ] be a smooth family of vector ﬁelds on V with a birth
or death type zero p. Let φt : V → R be a smooth family of weak Lyapunov
functions for Xt and φloc
t :U→ R a smooth family of weak Lyapunov functions on
a neighborhood U of p with φt(p) = φloc
t (p) for all t. Then there exists a smooth
family of weak Lyapunov functions ψt : V → R, t∈ [−ε,ε ] which agrees with φt
outside U and with φloc
t nearp.
Remark 9.24. (1) In case (a), φu := (1−u)φ +uψ, u∈ [0, 1] is a smooth
family of weak Lyapunov functions with φ0 =φ, φu =φ outside U, and φ1 =φloc
near p.
(2) By Lemma 9.17, in case (a) we can choose φloc to be Lyapunov, so ψ is
Lyapunov near p. Hence, in case (a) any weak Lyapunov function can be made
Lyapunov by a local deformation near the zeroes of X.
Analogous remarks apply to case (b).
The proof of Proposition 9.23 requires some preparation. Consider ( X,φ,φ loc)
as in the proposition with hyperbolic or embryonic zero p of valueφ(p) =b. Pick a
regular value a<b such that ∆ := W−
p ∩{φ≥a} is a smoothly embedded disc in
the hyperbolic case, and ∆ := ˆW−
p ∩{φ≥a} is a smoothly embedded half-disc in
the embryonic case, where ˆW±
p is deﬁned as in Lemma 9.6. We choose a so close
to b that ∆⊂U, so φloc is deﬁned near ∆.
We ﬁrst show that we can interpolate between φ and φloc near ∆.
Lemma 9.25. In the notation above, there exists a weak Lyapunov function
χ :N →[a,∞) on a neighborhood N of ∆ which agrees with φ nearN∩ φ−1(a)
and with φloc nearp.
Proof. Pick a suﬃciently small δ > 0. If p is hyperbolic X has no critical
points on the set ∆∩{φ≥a +δ}∩{φloc≤b−δ} and is transverse to its boundary.
Ifp is embryonicX has no critical points on the set ∆∩{φ≥a+δ}∩{φloc≤b−δ},
is transverse to the boundary components ∆∩{φ =a +δ} and ∆∩{φloc =b−δ},
and is tangent to the boundary component W−
p ∩{φ≥ a +δ}∩{ φloc≤ b−δ}.
Hence in either case we can use the ﬂow of X to construct a Lyapunov function χ
on ∆ which agrees with φ for φ≤ a +δ and with φloc for φloc≥ b−δ. Applying
the same argument to a small neighborhood of ∆ yields the desired function χ. □

9.5. CHANGING LYAPUNOV FUNCTIONS NEAR CRITICAL POINTS 201
φ = a
φ = a
∆
φ = c φ = c
Figure 9.2. The ﬂow box W near a hyperbolic zero.
Proof of Proposition 9.23. (a) We use the notation above. After applying
Lemma 9.25 and shrinking the neighborhood U of ∆, we may assume thatφ =φloc
near U∩φ−1(a).
We construct a ﬂow box W ⊂ U as in Section 9.4 as follows, see Figure 9.2
for the hyperbolic case. Pick a tubular neighborhood T− with smooth boundary
S− =∂T− of ∆∩φ−1(a) in the level set φ−1(a). Note that S−∼=Sk−1×Sm−k−1
ifp is hyperbolic of index k, and S−∼=Sm−2 ifp is embryonic. Let Σ∼= [a,c ]×S−
be the hypersurface in V obtained by ﬂowing S− underX up to some regular level
φ =c>b . Then S+ := Σ∩φ−1(c) is the boundary of a tubular neighborhood T+
of ∆∩φ−1(c) in the level set φ−1(c). The union T−∪T+∪ Σ bounds a compact
subsetW⊂V containing ∆. By choosing T− small andc close tob we can arrange
that W⊂ U. Note that W is a ﬂow box as in Section 9.4 with positive/negative
boundary ∂±W =T± and vertical boundary Σ (to which X is tangent).
In a similar way we construct smaller backward invariant compact neighbor-
hoods A′′⊂ A′⊂ A⊂ W of ∆. Pick ε >0 such that a + 2ε < b < c− 2ε and
φloc =φ on W∩{a≤φ≤a + 2ε}. Now we apply Lemma 9.20 twice to construct
the following smooth surroundings, see Figure 9.3:
• a weak Lyapunov function ψ1 : W→ R which agrees with φ outside A
and with g1◦φ on A′;
• a weak Lyapunov function ψ2 :W→ R which agrees with ψ1 outside A′
and with g2◦ψ1 =g◦φ on A′′.
Here g1,g 2,g =g2◦g1 : [a,c ]→ [a,c ] are diﬀeomorphisms which equal the identity
near ∂[a,c ] and have the following properties:
• g1(a +ε) =a +ε, g1(a + 2ε) =b + 2ε and g1(x)≥x for all x;

202 9. RECOLLECTIONS FROM MORSE THEORY
p
∆
A
A′
A′′
φ =φloc
ψ =a +ǫ
ψ =b + 2ǫ
aa +ǫa + 2ǫ
b
b +ǫb + 2ǫ
c
Figure 9.3. Smooth surroundings of a stable disc.
• g2(b +ε) =a +ε and g2(b + 2ε) =a + 2ε.
• g(b +ε) =a +ε, g(b + 2ε) =b + 2ε and g(x)≤x for all x.
(We chooseg and g1 with these properties and deﬁne g2 :=g◦g−1
1 ).
After target reparametrization above the level b we may assume max Wφloc≤
b +ε. Then near ∂A′ we haveψ2(x) =g1◦φ(x)≥φ(x) =φloc(x) if φ(x)≤a + 2ε,
and ψ2(x)≥ g1(a + 2ε) = b + 2ε > φloc(x) if φ(x)≥ a + 2ε, hence ψ2 ≥ φloc
near ∂A′. On A′′ we have ψ2(x) = g◦φ(x)≤ φ(x) = φloc(x) if φ(x)≤ a + 2ε,
and ψ2(x)≤ g(b +ε) = a +ε < φloc(x) if a +ε≤ φ(x)≤ b +ε, hence ψ2≤ φloc
on A′′∩{φ≤ b +ε}. This shows that the function max ( ψ2,φ loc) agrees with
φloc near ∆ and with φ near ∂A′, so we can extend it by φ to a function on V .
According to Remark 3.21, this function can be smoothed to a weak Lyapunov
function ψ :V → R for X with the desired properties. □
9.6. Smale cobordisms
Recall from Section 8.1 that a cobordismW is an oriented compact smooth
manifold with cooriented boundary ∂W . Its boundary splits as a disjoint union
∂W =∂−W∪∂+W where the coorientation is provided, respectively, by the inward
or outward normal vector ﬁeld.
Definition 9.26. A Lyapunov cobordism is a triple ( W,φ,X ), where W is a
cobordism,φ :W→ R is a smooth function constant on∂±W , andX is a gradient-
like vector ﬁeld for φ which points inward along ∂−W and outward along∂+W . In
particular, φ has no critical points on ∂W .
A Smale cobordism is a Lyapunov cobordism (W,φ,X ) for which the function
φ is Morse, so (W,φ ) is a Morse cobordism in the sense of Section 8.1.
A Lyapunov cobordism (W,φ,X ) is called elementary if there are noX-trajec-
tories between diﬀerent critical points of φ.
Note that if (W,φ,X ) is an elementary Smale cobordism, then the stable ma-
nifold of each critical point p is a disc D−
p which intersects ∂−W along a sphere
S−
p = ∂D−
p . We call D−
p and S−
p the stable disc resp. sphere of p. Similarly, the
unstable manifolds and their intersections with ∂+W are called unstable discs and
spheres. At an embryonic critical point, the manifolds ˆW±
p in Lemma 9.6 give rise
to (un-)stable half-discs ˆD±
p and hemispheres ˆS±
p .

9.6. SMALE COBORDISMS 203
Definition 9.27. An admissible partition of a Lyapunov cobordism (W,φ,X )
is a ﬁnite sequence m =c0 <c 1 <··· <c N =M of regular values of φ, where we
denote φ|∂−W =m and φ|∂+W =M, such that each subcobordism Wk ={ck−1≤
φ≤ck}, k = 1,...,N , is elementary.
Lemma 9.28. Any Lyapunov cobordism with only Morse or embryonic critical
points admits an admissible partition into elementary cobordisms.
Similarly, for any exhausting function φ with only Morse or embryonic critical
points and gradient-like vector ﬁeld X on a non-compact manifold V one can ﬁnd
regular values c0 < minφ<c 1 <···→∞ such that the cobordisms Wk ={ck−1≤
φ≤ck}, k = 1,..., are elementary. If φ has ﬁnitely many critical points, then all
but ﬁnitely many of these cobordisms have no critical points.
Proof. We prove the second statement, the ﬁrst one being analogous but
simpler. Critical points of φ are Morse or embryonic, hence isolated. Since φ is
also exhausting, its set of critical values is discrete and bounded below. So we can
order the critical values as a sequence infφ =d1 <d 2 <··· which is either ﬁnite or
tends to inﬁnity. Pick regular values ck such thatc0 <d 1 <c 1 <d 2 <c 2··· . Then
all critical points in the cobordism Wk ={ck−1≤φ≤ck} have valuedk, so there
are no X-trajectories between critical points and the cobordism is elementary. □
Equivalence of elementary Smale cobordisms.
Lemma 9.29. Let (W,X,φ ) be an elementary Smale cobordism with critical
points p1,...,p k and skeleton ( = union of the stable discs) ∆ = ⋃k
i=1D−
pi. Let
(W′,X′,φ′) be another Smale cobordism with the following properties:
• W′⊂W and ∂−W =∂−W′;
• (X′,φ′) has the same critical points and stable discs as (X,φ );
• φ′ = φ onOp (∂−W ), φ′(∂+W′) = φ(∂+W ), and φ′(pi) = φ(pi) for all
i = 1,...,k .
Then there exists an isotopy ht : W ↪→ W , t∈ [0, 1], with h0 = Id , ht(∆) = ∆
and ht = Id onOp (∂−W ), such that h1(W ) =W′ and φ =φ′◦h1. Moreover, the
construction can be done smoothly in families.
Proof. Step 1. Applying the Morse Lemma 9.1 and Remark 9.2 near each
critical point and extending the diﬀeomorphisms to all of W , we ﬁnd a diﬀeotopy
ht :W→W preserving ∆, ﬁxed on ∂−W , and such thatφ′◦h1 =φ on⋃k
i=1Oppi.
After renaming φ′◦h1 back to φ′ and modifying the gradient-like vector ﬁeld X′,
we may hence assume that (X′,φ′) = (X,φ ) on⋃k
i=1Oppi.
Step 2. The identity on ⋃k
i=1Oppi extends to a unique diﬀeomorphism
h1 :Op ∆→O p ∆ mapping trajectories of X to trajectories of X′ and such that
φ′◦h1 = φ onOp ∆. Following the trajectories for shorter times allows us to
connect h1 to the identity by an isotopy ht :Op ∆→O p ∆ ﬁxed on ⋃k
i=1Oppi.
Then we can adjust ht near ∂−W and extend it to a diﬀeotopy ht :W→W , ﬁxed
on⋃k
i=1Oppi∪O p (∂−W ) and preserving ∆, such that φ′◦h1 =φ onOp ∆. After
renamingφ′◦h1 back toφ′ and modifying the gradient-like vector ﬁeldX′, we may
hence assume that (X′,φ′) = (X,φ ) on a neighborhood U of ∂−W∪ ∆.
Step 3. The identity onOp (∂−W∪ ∆) extends to a unique diﬀeomorphism
h1 : W → W′ mapping trajectories of X to trajectories of X′ and such that
φ′◦h1 = φ. By Proposition 9.19, there exists an isotopy gt : W ↪→ W , ﬁxed on

204 9. RECOLLECTIONS FROM MORSE THEORY
xk
x′ = (x1, . . . , xk−1)
∂−D−
∂+D−
D−
e
E
Figure 9.4. The lower half-disc.
Op (∂−W∪∆) and preserving trajectories of X, such thatg0 = Id andg1(W )⊂U.
Similarly, there exists an isotopy g′
t : W′ ↪→ W′, ﬁxed on Op (∂−W∪ ∆) and
preserving trajectories ofX′, such thatg′
0 = Id andg′
1(W′)⊂U. As the embeddings
g1,g′
1◦h1 : W ↪→ W are both ﬁxed on Op (∂−W∪ ∆) and preserve trajectories
of X, they can be connected by an isotopy ft with the same properties by sliding
along trajectories of X. The composition of the isotopies gt, ft and the inverse of
g′
t◦ht gives the desired isotopy ht :W ↪→W from h0 = Id to h1. □
If W′ =W in Lemma 9.29 the map h1 :W→W is a diﬀeomorphism, but the
ht cannot in general be chosen to be diﬀeomorphisms. For example, this happens
if φ and φ′ have no critical points but deﬁne diﬀerent pseudo-isotopy classes, see
Section 9.10.
Cancellation pairs. We conclude this section by describing the setup for
cancellation of a pair of critical points. We will return to this setup in Chapters 10
and 13.
Let Rk = Rk−1×R be the space with coordinates (x1,...,x k) and letD⊂ Rk be
the unit disc. We denote by D− the lower half-disc D∩{xk≤ 0}, and set ∂+D− =
D−∩{xk = 0} and ∂−D− = ∂D∩D−, so that we have ∂D− = ∂−D−∪∂+D−.
See Figure 9.4. Further let e := (0,..., 0,−1/2)∈ D− and E :={(0,..., 0,xk)∈
D−|− 1/2<x k < 0}.
Consider now a Smale cobordism ( W,X,φ ) with precisely two critical points
p,q of index k andk− 1, respectively, that are connected by a unique X-trajectory
along which W +
q intersect transversely. Recall that the stable manifold of q is an
embedded disc W−
q = D−
q . Let ∆ be the closure of the stable manifold W−
p of p
in W . See Figure 9.5 (a) for a schematic and (b) for a more realistic picture with
a =φ|∂−W , b =φ(q) and c =φ(p). Note that ∆ is just the skeleton of ( W,X ).
Lemma 9.30. Suppose that near p and q the pair (X,φ ) has the standard form
from Proposition 9.13. Then ∆ is a smoothly embedded half-disc with upper bound-
ary ∂+∆ =D−
q and lower boundary ∂−∆ = ∆∩∂−W . More precisely, there exists
a smooth embedding α :D− ↪→W such that
• α(D−\∂+D−) =W−
p , α(∂+D−) =W−
q , and α(∂−D−)⊂∂−W ;

9.6. SMALE COBORDISMS 205
a
b
c
∆
∆
p
p
q
q
φ
∂−∆
∂+∆
φ = a
D−
q
(a)
(b)
Figure 9.5. A cancellation pair of critical points.
• α(0) =q, α(e) =p, and α(E) =W−
p ∩W +
q .
Proof. By hypothesis, in suitable coordinates ( x1,...,x m) near q the vector
ﬁeld X is given by
X =−
k−1∑
i=1
xi∂xi +x2
k∂xk +
m∑
j=k+1
xj∂xj.
In the following discussion, the indices i,j always range over i = 1,...,k − 1 and
j = k + 1,...,m . In these coordinates, the stable and unstable manifolds are
given by W−
q ={xk = xj = 0} and W +
q ={xi = 0}. Moreover, every trajectory
converging to q as t→−∞ is a ray emanating from the origin in W +
q . After a
rotation in W +
q , we may assume that the trajectory from q to p corresponds to
{xi = xj = 0,xk > 0} in these coordinates. By the transversality assumption,
W−
p ∩{xk = 1} can be locally written as the graph{xj =gj(xi),xk = 1} of smooth
functions gj : Rk−1→ R with gj(0) = 0. Then W−
p is the image of W−
p ∩{xk = 1}

206 9. RECOLLECTIONS FROM MORSE THEORY
under the ﬂow (xi,xk,xj)↦→ (e−txi,etxk,etxi),
W−
p ={(e−txi,et,etxj)|xj =gj(xi), t∈ R}
={(xi,xk,xj)|xj =xkgj(xkxi)|xk > 0}.
ThusW−
p is the graph{xj =Gj(xi,xk)} of the functions Gj(xi,xk) =xkgj(xkxi)
over the open half-space{xk > 0}, which obviously extends smoothly to the closed
half-space{xk≥ 0}.
The preceding discussion shows that ∆ is a smooth submanifold with boundary
W−
q nearq. Applying the backward ﬂow of X, this shows smoothness of ∆ near all
points of W−
q . On the other hand, Int ∆ = W−
p is smooth by Theorem 9.5. This
proves that ∆ is a smoothly embedded half-disc with upper boundary ∂+∆ =D−
q
and lower boundary∂−∆ = ∆∩∂−W , from which the existence of a parametrization
α with the desired properties easily follows. □
Example 9.31. If (X,φ ) is not standard nearq the set ∆ need not even beC1-
embedded. For example, suppose that dim W = 3 and in coordinates Z = (x,y,z )
near q the vector ﬁeld is given by
X =−ax∂x +by∂y +z∂z, a,b> 0.
Moreover, suppose that the trajectory fromq top corresponds to{x =y = 0,z >0}
in these coordinates. By the transversality assumption,W−
p∩{z = 1} can be locally
written as the graph{y =g(x),z = 1} of a functiong : R→ R withg(0) = 0. Then
W−
p is the image of W−
p ∩{z = 1} under the ﬂow (x,y,z )↦→ (e−atx,ebty,etz),
W−
p ={(e−atx,ebty,et)|y =g(x), t∈ R} ={(x,y,z )|y =zbg(zax)|z >0}.
For the function G(x,z ) :=zbg(zax) we compute
∂G
∂z =bzb−1g(zax) +axza+b−1g′(zax) =xza+b−1
(
bg(zax)
zax +ag′(zax)
)
.
Asz→ 0 the term in brackets tends to (b +a)g′(0), so ∂G
∂z does not extend contin-
uously to z = 0 if g′(0)⁄= 0 and a +b< 1.
9.7. Morse and Smale homotopies
Definition 9.32. A smooth family (W,φt,Xt), t∈ [0, 1], of Lyapunov cobor-
dism structures is called Smale homotopy if there is a ﬁnite set A⊂ (0, 1) with the
following properties:
• for eacht∈A the functionφt has a unique birth-death type critical point
et such that φt(et)⁄=φt(q) for all other critical points q of φt;
• for each t /∈A the function φt is Morse.
In this case we call the underlying ( W,φt) a Morse homotopy.
Remark 9.33. (a) Note the slight abuse of language because ( φt,Xt) is not a
Smale cobordism structure for t∈A.
(b) By Theorem 9.4 and Corollary 9.16, any family ( W,φt,Xt) of Lyapunov
cobordism structures such that (φ0,X 0) and (φ1,X 1) are Smale can be turned into
a Smale homotopy by a perturbation ﬁxed near t = 0, 1 (C0-small in the vector
ﬁelds and C∞-small in the functions).
(c) It will sometimes be convenient to allow the domainWt to vary by an isotopy
of submanifolds in an ambient equidimensional manifold. We can consider this a

9.7. MORSE AND SMALE HOMOTOPIES 207
homotopy with ﬁxed domain W0 by pulling back the structures under a family of
diﬀeomorphisms W0→Wt.
Definition 9.34. A Smale homotopy St = (W,Xt,φt), t∈ [0, 1] is called an
elementary Smale homotopy of type I, IIb, IId, respectively, if the following holds:
• Type I. St is an elementary Smale cobordism for all t∈ [0, 1].
• Type IIb (birth). There is t0∈ (0, 1) such that for t<t 0 the function φt
has no critical points, φt0 has a birth type critical point, and for t > t0
the function φt has has two critical points pt andqt of index i andi− 1,
respectively, connected by a unique Xt-trajectory.
• Type IId (death). There is t0∈ (0, 1) such that fort>t 0 the functionφt
has no critical points, φt0 has a death type critical point, and for t<t 0
the function φt has has two critical points pt andqt of index i andi− 1,
respectively, connected by a unique Xt-trajectory.
We will also refer to an elementary Smale homotopy of type IIb (resp. IId ) as a
creation (resp. cancellation) family.
Lemma 9.30 has the following parametric version which is proved similarly. We
use the notation introduced before Lemma 9.30.
Lemma 9.35. Let (W,Xt,φt), t∈ [−1, 1], be an elementary Smale homotopy
of type IIb with birth-type critical point p0 =q0 at t = 0 and nondegenerate critical
points pt,qt, t∈ (0, 1], with ind(pt) = k and ind(qt) = k− 1. Suppose that near
the critical points the family (Xt,φt) has the standard form from Proposition 9.13.
Then the skeletons ∆t, t∈ [0, 1], form a smooth family of embedded half-discs with
upper boundaries ∂+∆t = D−
qt and lower boundaries ∂−∆t = ∆t∩∂−W . More
precisely, there exists a smooth family of embeddings αt :D− ↪→W such that
• αt(D−\∂+D−) =W−
pt, αt(∂+D−) =W−
qt , and αt(∂−D−)⊂∂−W ;
• αt(0) =qt, α(
√
te ) =pt, and α(
√
tE ) =W−
pt∩W +
qt .
An analogous statement holds for an elementary homotopy of type IId.
Definition 9.36. An admissible partition of a Smale homotopy St = (W,Xt,
φt), t∈ [0, 1], is a sequence 0 = t0 <t 1 <··· <t p = 1 of parameter values, and for
eachk = 1,...,p a ﬁnite sequence of functions
m(t) =ck
0(t)<c k
1(t)<··· <c k
Nk(t) =M(t), t ∈ [tk−1,tk],
where m(t) :=φt(∂−W ) and M(t) :=φt(∂+W ), such that ck
j (t), j = 0,...,N k are
regular values of φt and each Smale homotopy
Sk
j :=
(
Wk
j (t) :={ck
j−1(t)≤φt≤ck
j (t)},Xt|Wk
j (t),φt|Wk
j (t)
)
t∈[tk−1,tk]
is elementary.
Lemma 9.37. Any Smale homotopy admits an admissible partition.
Proof. Let A⊂ (0, 1) be the ﬁnite subset in the deﬁnition of a Smale homo-
topy. Using Lemma 9.28, we now ﬁrst construct an admissible partition on OpA
and then extend it over [0, 1]\O pA. □
Equivalence of elementary Smale homotopies. We deﬁne the proﬁle of
a Smale homotopy St = (W,Xt,φt), t∈ [0, 1], as the proﬁle C({φt})⊂ [0, 1]× R
of the family of functions φt :W→ R as in Section 9.1. We will use the notion of
proﬁle only for elementary homotopies.

208 9. RECOLLECTIONS FROM MORSE THEORY
Lemma 9.38. Let St = (W,Xt,φt) and ~St = (W, ~Xt,~φt), t∈ [0, 1], be two
elementary Smale homotopies with the same proﬁle such that S0 = ~S0. Then there
exists a diﬀeotopy ht :W→W with h0 = Id such that φt =~φt◦ht for all t∈ [0, 1].
Moreover, if φt = ~φt near ∂+W and/or ∂−W we can arrange ht = Id near
∂+W and/or ∂−W .
Proof. Denote byCt,~Ct the critical point sets and by ∆t,~∆t the skeletons of
St,~St. We ﬁrst construct a family of diﬀeomorphisms ft :OpCt→O p ~Ct with
f0 = Id and ~φt◦ft = φt. For this, we ﬁrst use Theorem 9.4 to construct ft near
the birth-death points, and then the Morse Lemma 9.1 to extend it over the Morse
critical points.
Next we canonically extend the maps ft :OpCt→O p ~Ct to diﬀeomorphisms
ft : Ut→ ~Ut between neighborhoods of ∆ t,~∆t mapping φt to ~φt and trajectories
of Xt to trajectories of ~Xt.
Note that U−
t :=∂−W∩Ut is a neighborhood of the submanifold ∆ t∩∂−W ,
and each restriction ft|U−
t
is isotopic to the identity by following trajectories for
shorter times. Hence by the smooth isotopy extension theorem, after shrinking Ut,
the maps ft|U−
t
extend to diﬀeomorphisms gt : ∂−W → ∂−W . Moreover, since
f0 = Id we can arrange g0 = Id.
Now we extend the mapsUt∪∂−W→ ~Ut∪∂−W given byft andgt canonically
to diﬀeomorphisms ht : W → W mapping φt to ~φt and trajectories of Xt to
trajectories of ~Xt. Note that h0 = Id.
Finally, if φt = ~φt near ∂±W we undo the diﬀeotopy ht on level sets near
∂±W to arrange ht = Id onOp (∂±W ). Note that in this last step we destroy the
property that ht maps trajectories of Xt to trajectories of ~Xt. □
Lemma 9.39. Let (W,X,φ ) be an elementary Smale cobordism with φ|∂±W =
a± and critical points p1,...,p n of values φ(pi) = ci. For i = 1,...,n let ci :
[0, 1]→ (a−,a +) be smooth functions with ci(0) = ci. Then there exists a smooth
family φt, t∈ [0, 1], of Lyapunov functions for X with φ0 = φ and φt = φ on
Op∂W such that φt(pi) =ci(t).
Proof. By hypothesis there are no X-trajectories between diﬀerent critical
points, so the stable manifolds are disjoint discs. Denote by Si⊂∂−W the stable
sphere ofpi. Pick disjoint tubular neighborhoods of theSi in∂−W and denote byVi
the closures of their forward images under the ﬂow of X. Deﬁne Ui\Vi analogously
for slightly smaller neighborhoods. The ﬂow of X induces diﬀeomorphisms Vi\
IntUi∼=Ski−1×Sm−ki−1× [0, 1]× [a−,a +] in which φ(u,v,x,y ) =y and X =∂y.
Here m = dimW and ki = ind(pi).
Fix a cutoﬀ function ρ : [0, 1]→ [0, 1] which equals 1 near 0 and 0 near 1. For
diﬀeomorphisms σi : [a−,a +]→ [a−,a +] with σi = Id near a± deﬁne a function
ψσ :W→ [a−,a +] by
ψσ :=



(
1−ρ(x)
)
y +ρ(x)σi(y) on Vi\ IntUi,
σi◦φ on Ui,
φ on W\⋃
iVi.
On Vi\ IntUi we have ∂ψσ
∂y =
(
1−ρ(x)
)
+ρ(x)σ′
i(y) > 0, so ψσ is a Lyapunov
function for X. Moreover, ψσ = φ near ∂W , ψσ(pi) = σi(ci), and ψσ depends

9.7. MORSE AND SMALE HOMOTOPIES 209
smoothly on σ1,...,σ n. Now pick smooth families of diﬀeomorphisms σi,t with
σi,0 = Id and σi,t(ci) =ci(t) and set φt :=ψσt. □
Holonomy of Smale cobordisms.
Definition 9.40. Let (W,X,φ ) be a Smale cobordism such that the function
φ has no critical points. The holonomy of X is the diﬀeomorphism
ΓX :∂+W→∂−W
which maps x∈ ∂+W to the intersection of its trajectory under the ﬂow of −X
with ∂−W .
Consider now a function φ : W → R without critical points and constant on
∂−W and ∂+W . Denote by X (W,φ ) the space of all gradient-like vector ﬁelds for
φ. Note that the holonomy maps of all X∈X (W,φ ) are isotopic. We denote by
D(∂+W,∂−W ) the corresponding path component in the space of diﬀeomorphisms
from ∂+W to ∂−W . All spaces are equipped with the C∞-topology.
Recall that a continuous map p : E → B is a Serre ﬁbration if it has the
homotopy lifting property for all closed discs Dk, i.e., given a homotopy ht :Dk→
B, t∈ [0, 1], and a lift ~h0 : Dk→ E with p◦~h0 = h0, there exists a homotopy
~ht :Dk→E with p◦~ht =ht. For more background see [ 91] or Appendix A.1.
We omit the proof of the following easy lemma.
Lemma 9.41. Let (W,φ ) be a Morse cobordism without critical points. Then
the map X (W,φ )→D (∂+W,∂−W ) that assigns to X its holonomy ΓX is a Serre
ﬁbration. In particular:
(i) Given X ∈X (W,φ ) and an isotopy ht∈D (∂+W,∂−W ), t∈ [0, 1], with
h0 = ΓX there exists a path Xt∈X (W,φ ) with X0 =X such that ΓXt =ht for all
t∈ [0, 1].
(ii) Given a path Xt ∈X (W,φ ), t∈ [0, 1], and a path ht ∈D (∂+W,∂−W )
which is homotopic to ΓXt with ﬁxed endpoints, there exists a path ~Xt∈X (W,φ )
with ~X0 =X0 and ~X1 =X1 such that Γ ~Xt
=ht for all t∈ [0, 1]. □
As a consequence, we obtain
Lemma 9.42. Let Xt, Yt be two paths in X (W,φ ) starting at the same point
X0 = Y0. Suppose that for a subset A⊂ ∂+W one has ΓXt(A) = ΓYt(A) for all
t∈ [0, 1]. Then there exists a path ˆXt∈X (W,φ ) such that
(i) ˆXt =X2t for t∈ [0, 1
2];
(ii) ˆX1 =Y1;
(iii) Γ ˆXt
(A) = ΓY1(A) for t∈ [ 1
2, 1].
Proof. Consider the path γ : [0, 1]→D (∂+W,∂−W ) given by the formula
γ(t) := ΓX1◦ Γ−1
Xt◦ ΓYt.
We haveγ(0) = ΓX1 andγ(1) = ΓY1. The path γ is homotopic with ﬁxed endpoints
to the concatenation of the paths ΓX1−t and ΓYt. Hence by Lemma 9.41 we conclude
that there exists a pathX′
t∈X (W,φ ) such thatX′
0 =X1,X′
1 =Y1, and ΓX′
t =γ(t)
for all t∈ [0, 1]. Since
ΓX′
t(A) = ΓX1
(
Γ−1
Xt
(
ΓYt(A)
))
= ΓX1(A) = ΓY1(A),
the concatenation ˆXt of the paths Xt and X′
t has the required properties. □

210 9. RECOLLECTIONS FROM MORSE THEORY
9.8. The h-cobordism theorem
The topology of a manifold provides a lot of constraints on the critical points
of a Morse function on it. For instance, the Morse inequalities (see [139]) assert
that the number of index k critical points of a Morse function on a manifold V or
cobordism W (exhausting in the manifold case, with regular level sets ∂±W in the
cobordism case) is bounded below by the rank of the homology group Hk(V ; Z)
(or by the rank of the relative homology group Hk(W,∂−W ; Z) in the case of a
cobordism). Morse-Smale theory deals with the problem of simpliﬁcation of a Morse
function on a manifold, as much as the topology allows. In particular, one has the
celebrated
Theorem 9.43 (h-cobordism theorem, Smale [ 173]). Let W be a cobordism
of dimension dimW≥ 6 such that W and ∂±W are simply connected and H∗(W,
∂−W ; Z) = 0. Then W carries a Morse function without critical points and constant
on ∂±W .
More generally, a Morse function on a cobordism or manifold is called perfect if
it has the minimal number of critical points compatible with the Morse inequalities.
Then one has
Theorem 9.44 (Smale [173]). LetW be a compact manifold with boundary of
dimension dimW≥ 6 such that W and∂W are simply connected. Then W carries
a perfect Morse function with regular level set ∂W .
If W is not simply connected one has a further obstruction to the cancellation
of critical points called Whitehead torsion. An analogous result in this case, called
the s-cobordism theorem, was proved by Barden, Mazur and Stallings (see [ 112]).
The key geometric ingredients in the proof of theh-cobordism ands-cobordism
theorem are the following four geometric lemmas about modiﬁcations of Smale
cobordisms (see [140]).
The ﬁrst lemma is an immediate consequence of Lemma 9.39.
Lemma 9.45 (moving critical levels) . Let (W,X,φ ) be an elementary Smale
cobordism. Then there is a homotopy (W,X,φ t) relOp∂W of elementary Smale
cobordisms which arbitrarily changes the ordering of the critical values.
The second lemma is an immediate consequence of Lemma 9.41 and the smooth
isotopy extension theorem.
Lemma 9.46 (moving attaching spheres) . Let (W,X,φ ) be a Smale cobordism
and p∈ W a critical point whose stable manifold W−
p intersects ∂−W along a
sphere S⊂∂−W . Then given any isotopy St⊂∂−W of the sphere S =S0, there
exists a homotopy Xt rel∂W of gradient-like vector ﬁelds for φ such that X0 =X
and the stable manifold W−
p (Xt) intersects∂−W along St.
The third lemma is proved by simply implanting a model creation family near
a regular point, see [ 140, Lemma 8.2].
Lemma 9.47 (creation of critical points) . Let (W,X,φ ) be a Smale cobordism
without critical points. Then for any 1≤k≤ dimW and anyp∈ IntW there exists
a birth type Smale homotopy (W,Xt,φt), t∈ [0, 1], ﬁxed outside a neighborhood of
p with (X0,φ 0) = ( X,φ ), which creates a pair of critical points of index k− 1
and k connected by a unique trajectory of X1 along which the stable and unstable
manifolds intersect transversely.

9.8. THE h-COBORDISM THEOREM 211
The converse lemma is more diﬃcult, see [ 140, Theorem 5.4].
Lemma 9.48 (cancellation of critical points) . Suppose that a Smale cobordism
(W,X,φ ) contains exactly two critical points of index k− 1 and k which are con-
nected by a unique trajectory of X along which the stable and unstable manifolds
intersect transversely. Then there exists a death type Smale homotopy (W,Xt,φt),
t∈ [0, 1], ﬁxed on Op∂W with (X0,φ 0) = (X,φ ) which kills the critical points, so
the cobordism (W,X 1,φ 1) has no critical points.
Using the smooth surroundings provided by Proposition 9.19, one can in fact
deduce Lemma 9.48 from the following more elementary lemma (which is a special
case of [ 140, Theorem 5.4]). This deduction will be carried out in Section 10.7 in
the more diﬃcult context of J-convex functions, using the J-convex surroundings
from Chapter 4.
Lemma 9.49. Suppose that a Lyapunov pair (X,φ ) on the k-dimensional disc
Dk contains exactly two critical points of index k− 1 and k in IntDk which are
connected by a unique trajectory ofX along which the stable and unstable manifolds
intersect transversely. Then there exists a family (Xt,φt), t∈ [0, 1], of Lyapunov
pairs onDk, ﬁxed onOp∂Dk with (X0,φ 0) = (X,φ ), which kills the critical points,
so the pair (X1,φ 1) has no critical points.
Here is a sketch of the proof of theh-cobordism theorem based on Lemmas 9.45
to 9.48, see [140] for details. For W as in Theorem 9.43 pick any Morse functionφ :
W→ R having∂±W as regular level sets. Using Lemma 9.45 and a transversality
argument, φ can be made self-indexing, i.e., such that the value of each critical
point equals its Morse index.
Fork∈ N consider the regular level set Σ = φ−1(k− 1
2). Let p1,...,p s be the
critical points on level k and q1,...,q t those on level k− 1. Denote by S−
i ⊂ Σ
the stable sphere of pi and by S+
j ⊂ Σ the unstable sphere of qj, and consider the
matrix A of homological intersection numbers S−
i ·S+
j .
Next we modify the matrixA using handle slides. Namely, consider two critical
points pi and pj on level k. We ﬁrst apply Lemma 9.45 to raise pi to a slightly
higher level, and then use Lemma 9.46 to deform the vector ﬁeld X so that at
one moment during the deformation there appears a trajectory connecting pi and
pj (= the handle slide). As a result, the stable manifold of pi slides over the
stable manifold of pj, so that after the handle slide the homology class [ S−
i ] is
replaced by [S−
i ] + [S−
j ]. Thus the handle slide has the eﬀect of adding the j-th
row to thei-th row inA. Using such elementary row operations and the hypothesis
H∗(W,∂−W ; Z) = 0, we can modify the matrix A such that S−
i · S+
i = 1 for
i = 1,...,r ≤ min{s,t} and all other intersection numbers are zero.
The next task is to get rid of homologically unnecessary intersections between
S−
i and S+
j in Σ. For this, consider two transverse intersection points z± with
local intersection indices ±1. Connect them by paths in S−
i and S+
j to obtain an
embedded loop γ in Σ. Suppose for the moment that there are no critical points
of indices 0, 1,m− 1,m , where m = dimW . Then the hypotheses π1(W ) = 0 and
dimW ≥ 6 allow us to apply Whitney’s theorem [ 191] and ﬁnd a Whitney disc
∆⊂ Σ with boundary γ meeting S−
i ∪S+
j only transversely along the boundary.
Then we can eliminate the intersection points z± by pushing S−
i over ∆ using
Lemma 9.46.

212 9. RECOLLECTIONS FROM MORSE THEORY
After this elimination procedure, we are left with S−
i and S+
i for i = 1,...,r
intersecting in a unique point. This means that the critical points qi and pi are
connected by a unique X-trajectory, so we can eliminate them by Lemma 9.48.
Performing these steps on all levels, we end up with a Morse function without
critical points. This concludes the proof provided there were no critical points of
indices 0, 1,m− 1,m . To arrange this, we ﬁrst use Lemma 9.48 to cancel critical
points of index 0 and m. To get rid of a critical point p of index 1 (and similarly
for m− 1), one uses the so-called Smale trick, see [ 173], to create with the use of
Lemma 9.47 a pair of critical points q,r of indices 2, 3 in such a way that p and
q can be cancelled using Lemma 9.48. This ﬁnishes the sketch of the proof of the
h-cobordism theorem.
In Chapter 10 we will prove analogues of the four Lemmas 9.45–9.48 for J-
convex functions. These will then be used to derive h-cobordism type results for J-
convex functions as well as results on deformation of Stein structures in Chapter 15.
9.9. The two-index theorem
The following so-called “two-index theorem” of Hatcher and Wagoner ([92], see
also [107]) will be important for our applications. This theorem is a 1-parametric
version of the Smale trick which we mentioned above in our sketch of the proof of
the h-cobordism theorem.
Proposition 9.50 ([92, Chapter V Prop. 3.5], [ 107, Chapter VI Thm. 1.1]) .
Let ft :Wm→ [0, 1] be a generic one-parameter family of functions on the cobor-
dism W with regular level sets ∂−W =f−1
t (0) and ∂+W =f−1
t (1). Let i<m − 3
be the lowest index of critical points in this family. Suppose that (W,∂−W ) is
i-connected andf0,f 1 are Morse without critical points of index i. Then, by intro-
ducing new critical points of index i + 1 and i + 2, ft can be deformed rel f0,f 1 to
a family without critical points of index i.
Proof. The statement is identical with Proposition 3.5 in Chapter V of [ 92],
except that their hypothesis that W is an h-cobordism has been replaced by i-
connectivity of the pair ( W,∂−W ). Now the only place in the proof where the
hypothesis of an h-cobordism is used is the ﬁrst step in the proof of Lemma 3.3
in [92] where they consider the homotopy exact sequence of a certain triple∂−W⊂
W1⊂W ,
···→ πi(W,∂−W )→πi(W,W 1)→πi−1(W1,∂−W )→···
Here i-connectivity of (W,∂−W ) and (i− 1)-connectivity of (W1,∂−W ) together
imply i-connectivity of (W,W 1), which is the only conclusion that is needed in the
rest of the proof. □
Corollary 9.51. Letft :Wm→ [0, 1] be a one-parameter family of functions
on the cobordismW with regular level sets ∂−W =f−1
t (0) and∂+W =f−1
t (1). For
some i<m − 3, suppose that f0,f 1 are Morse without critical points of index ≤i.
Then ft can be deformed rel f0,f 1 to a family without critical points of index ≤i.
Proof. The existence of a Morse function f0 without critical points of index
≤ i implies that W is i-connected. Now the corollary follows from the preceding
proposition by induction over i. □

9.10. PSEUDO-ISOTOPIES 213
Corollary 9.52. Letft :W 2n→ [0, 1] be a one-parameter family of functions
on the cobordism W with regular level sets ∂−W =f−1
t (0) and ∂+W =f−1
t (1).
(i) Suppose that n> 2 and f0,f 1 are Morse without critical points of index
>n . Then ft can be deformed relf0,f 1 to a family without critical points
of index >n .
(ii) Supposen> 3 and f0,f 1 are Morse without critical points of index ≥n.
Then ft can be deformed rel f0,f 1 to a family without critical points of
index≥n.
Proof. Consider the cobordismW with reversed orientation and the family of
functions ¯ft :W→ [0, 1], ¯ft(x) := 1−ft(x). In case (i) the Morse functions ¯f0, ¯f1
are without critical points of index < n, and in case (ii) without critical points of
index≤n. Hence the statement follows from the preceding corollary applied to ¯ft
with m = 2n and i =n− 1 in case (i), and with i =n in case (ii). The necessary
inequality reduces to n− 1 =i<m − 3 = 2n− 3 or equivalently n> 2 in case (i),
and to n =i<m − 3 = 2n− 3 or equivalently n> 3 in case (ii). □
9.10. Pseudo-isotopies
Let us recall the basic notions of pseudo-isotopy theory, see [ 30] and [92]. For
a manifold W (possibly with boundary) and a closed subset A⊂W we denote by
Diﬀ(W,A ) the space of diﬀeomorphisms of W ﬁxed onOp (A), equipped with the
C∞-topology. For a cobordism W the restriction map to ∂+W deﬁnes a ﬁbration
Diﬀ(W,∂W )→ Diﬀ(W,∂−W )→ DiﬀP(∂+W ),
where DiﬀP(∂+W ) denotes the image of the restriction map Diﬀ( W,∂−W ) →
Diﬀ(∂+W ). For the product cobordism I×M, I = [0, 1], ∂M = ∅,
P(M) := Diﬀ(I×M, 0×M)
is the group of pseudo-isotopies of M. Denote by Diﬀ P(M) the group of diﬀeo-
morphisms of M that are pseudo-isotopic to the identity , i.e., that appear as the
restriction to 1 ×M of an element in P(M). Restriction to 1 ×M deﬁnes the
ﬁbration
Diﬀ(I×M,∂I ×M)→P (M)→ DiﬀP(M)
and thus a homotopy exact sequence
···→ π0Diﬀ(I×M,∂I ×M)→π0P(M)→π0DiﬀP(M)→ 0.
We will use the following alternative description of P(M), see [ 30]. Denote by
E(M) the space of all smooth functions f :I×M→I without critical points and
satisfying f(r,x ) =r onOp (∂I×M). We have a homotopy equivalence
P(M)→E (M), F ↦→p◦F,
wherep :I×M→I is the projection. A homotopy inverse is given ﬁxing a metric
and sendingf∈E (M) to the unique diﬀeomorphismF mapping levels off to levels
ofp and gradient trajectories of f to straight lines I×{x}. Note that the last map
in the homotopy exact sequence
···→ π0Diﬀ(I×M,∂I ×M)→π0E(M)→π0DiﬀP(M)
associates to f ∈ E(M) the ﬂow from 0 ×M to 1×M along trajectories of a
gradient-like vector ﬁeld (whose isotopy class does not depend on the gradient-like
vector ﬁeld).

214 9. RECOLLECTIONS FROM MORSE THEORY
We will discuss in Chapters 14 and 15 symplectic and Stein versions of these
notions. For the symplectic version, it will be convenient to replaceI×M by R×M
as follows: We replace E(M) by the space of functions f : R×M → R without
critical points and satisfyingf(r,x ) =r outside a compact set; Diﬀ(I×M,∂I×M)
by the space Diﬀ c(R×M) of diﬀeomorphisms that equal the identity outside a
compact set; and P(M) by the space of diﬀeomorphisms of R×M that equal the
identity near{−∞}×M and have the form (r,x )↦→ (r+f(x),g (x)) near{+∞}×M.
The last map in the exact sequence
···→ π0Diﬀc(R×M)→π0E(M)→π0DiﬀP(M)
then associates to f∈E (M) the ﬂow from{−∞}× M to{+∞}× M along trajec-
tories of a gradient-like vector ﬁeld which equals ∂r outside a compact set.
We endow the spacesP(M),E(M) and Diﬀc(R×M) with the topology of uni-
formC∞-convergence on R×M (and not the topology of uniform C∞-convergence
on compact sets), with respect to the product of the Euclidean metric on R and
any Riemannian metric on M. In other words, a sequence Fn∈P (M) converges
to F ∈ P(M) if and only if ‖Fn− F‖Ck(R×M) → 0 for every k = 0 , 1,... .
For example, consider any non-identity element F ∈P (M) and the translations
τc(r,x ) = ( r +c,x ), c∈ R, on R×M. Then the sequence Fn := τn◦F◦τ−n
does not converge as n→∞ to the identity in P(M), although it does converge
uniformly on compact sets. With this topology, the obvious inclusion maps from
the spaces on I×M to the corresponding spaces on R×M are weak homotopy
equivalences.
Remark 9.53. It was proven by Cerf in [30] thatπ0P(M) is trivial if dimM≥
5 andM is simply connected. In the non-simply connected case and for dim M≥ 6
Hatcher and Wagoner ([ 92], see also [ 107]) have expressed π0P(M) in terms of
algebraic K-theory of the group ring of π1(M). In particular, there are many
fundamental groups for which π1P(M) is not trivial.

10
Modiﬁcations of J-Convex Morse Functions
In this chapter we discuss modiﬁcations ofJ-convex Morse functions on a given
complex manifold. This parallels the h-cobordism theory for ordinary Morse func-
tions in Section 9.8. More precisely, we show how to perform the following opera-
tions:
• moving attaching spheres by isotropic isotopies (Section 10.1);
• moving critical levels (Section 10.3);
• creation and cancellation of critical points (Sections 10.4–10.8).
Section 10.2 is an aside on the J-orthogonality condition used in Chapter 8.
The proofs in this chapter rely on the techniques developed in Chapters 3 and 4.
10.1. Moving attaching spheres by isotropic isotopies
For a function φ :V → R we will use the notations
Vb :=φ−1(b), V [a,b] :=φ−1([a,b ]).
The goal in this section is to prove the following result.
Proposition 10.1. Consider a complex manifold (V,J ) and a properJ-convex
function φ : V → R without critical values in the interval [a,b ]. Let Λ⊂ Vb be
a closed isotropic submanifold and L⊂V its image under the ﬂow of −∇φφ. Let
(Λt)t∈[0,1] be an isotropic isotopy of Λ0 :=L∩Va in Va.
Then, after composing φ with a suﬃciently convex increasing function f :
[a,b ] → R, there exists a diﬀeotopy ht : V → V with the following properties
for all t∈ [0, 1], see Figure 10.1:
(i) ht = Id outside V [a,b];
(ii) φt :=φ◦ht is J-convex;
(iii) the image Lt of Λ under the ﬂow of −∇φtφt intersectsVa in Λt.
Remark 10.2. The corresponding result for ordinary functions φ is very easy:
It just states that one can realize a smooth isotopy of spheres Λ t as descending
spheres for a homotopy of gradient-like vector ﬁelds, keeping the function φ ﬁxed.
In contrast, Proposition 10.1 is more subtle because the gradient vector ﬁelds∇φtφt
are determined by the functions φt themselves.
The proof requires some preparation. The following lemma is the main technical
ingredient.
Lemma 10.3. Let Σ be aJ-convex hypersurface with ﬁeld of complex tangencies
ξ in a complex manifold (V,J ). Let X⊥ be a transverse vector ﬁeld along Σ with
JX⊥∈T Σ. Let Λ⊂ Σ be an isotropic submanifold and X be a vector ﬁeld along Λ
that is transverse to Σ. Then for any compact subset K⊂ Λ there exists a J-convex
hypersurface Σ′ with the following properties, see Figure 10.2:
215

216 10. MODIFICATIONS OF J-CONVEX MORSE FUNCTIONS
V a
V bΛ
Λ0 Λt Λ1
L Lt
L1
Figure 10.1. Moving attaching spheres by isotropic isotopies.
Σ
X
K
X ⊥
Σ′
Figure 10.2. Turning aJ-convex hypersurface along an isotropic submanifold.
(i) K⊂ Σ′ and ξ⊂T Σ′ along K;
(ii) Σ′ is transverse to X⊥ and Σ′ = Σ outside a neighborhood of K;
(iii) JX (x)∈TxΣ′ for all x∈K.
Proof. Let n = dimCV and k− 1 = dim Λ. We will only carry out the proof
in the Legendrian case k = n, the case k < nbeing analogous but notationally
more involved. Note that the case k < nformally follows from the Legendrian
case provided that the symplectic normal bundle ( T Λ)ω/T Λ of Λ in the ﬁeld of
complex tangencies ξ⊂ T Σ is trivial. Indeed, in this case a neighborhood of Λ
(after shrinking it) in Σ is contactomorphic to a neighborhood of the zero section
in J1Λ⊕ Cn−k (see Chapter 6). So we can extend Λ to a Legendrian submanifold
~Λ∼= Λ× Rn−k⊂ Σ and X to a vector ﬁeld ~X along ~Λ transversee to Σ.
After possibly changing its sign, we may assume that X⊥ is opposite to the
coorientation of Σ. The ﬂow of X⊥ extends Λ (after shrinking Λ) to a totally real
submanifold Λ× [−1, 1]⊂ V . By Proposition 5.55 the inclusion Λ × [−1, 1] ↪→ V
extends to a diﬀeomorphism of a neighborhood of Λ × [−1, 1] in Λ C⊕ C onto a
neighborhood of Λ× [−1, 1] in V such that the pullback of J (still denoted by J)
and the standard structure Jst on ΛC⊕ C coincide along Λ× [−1, 1] together with
their 7-jets. Here Λ C is the complexiﬁcation of Λ (for some real analytic structure
on Λ) and X⊥ generates the real line 0 ⊕iR. This implies that T Σ = T ΛC⊕ R
with ﬁeld of complex tangencies ξ =T ΛC along Λ. Denote coordinates on Λ C⊕ C
by (z,w ) = (x,y,u +iv), where y are coordinates on Λ and x coordinates in the

10.1. MOVING ATTACHING SPHERES BY ISOTROPIC ISOTOPIES 217
ﬁbers of Λ C. In these coordinates, Σ can be written near Λ as the graph
Σ ={v =φ(x,y,u )}
of a function φ with φ(0,y, 0) = 0 and dφ(0,y, 0) = 0. The choice of X⊥ implies
that Σ is J-convex cooriented from above. We will ﬁnd Σ ′ as the graph Σ ′ =
{v = ~φ(x,y,u )} of a function ~φ with ~φ = φ outside a neighborhood of K⊕ 0 in
ΛC⊕ R. Then Σ′ is transverse to X⊥ = ∂v. The conditions K⊂ Σ′ and ξ⊂ T Σ
along K are equivalent to ~φ(0,y, 0) = 0 and dz~φ(0,y, 0) = 0 for y∈ K. After
rescaling and possibly changing its sign, we can write the given vector ﬁeld X as
X =∂v−τ(y)∂u +Y withY tangent to ΛC andτ some given function on Λ. Then
JX∈T Σ′ along K is equivalent to ~φu(0,y, 0) =τ(y) for y∈K.
LetQ := dist2
Λ be the squared distance (with respect to some Hermitian metric
forJst) from the zero section in ΛC. By Proposition 2.15, Q is aJst-convex function.
Note that the hypersurface {v = Q(x,y )} is tangent to Σ along Λ. Its Levi form
at points of Λ is given by −ddC(
Q(x,y )−v
)
|ξ=TΛC =−ddCQ, so{v =Q(x,y )} is
Jst-convex along Λ cooriented from above. Since the Levi forms with respect to J
and Jst agree along Λ, the hypersurfaces Σ and {v = Q(x,y )} are also J-convex
near Λ. Thus by Corollary 3.31 we can modify Σ near K, preserving J-convexity
and the condition Λ⊂ Σ, such that Σ ={v =Q(x,y )} near K.
Now let a functionτ(y) be given as above. Our task is to ﬁnd a smooth function
~φ with J-convex graph such that
~φ(0,y, 0) = 0, d z~φ(0,y, 0) = 0, ~φu(0,y, 0) =τ(y)
for y∈K and ~φ(x,y,u ) =Q(x,y ) outside a neighborhood of K.
Pick a functiong(y,u ) on Λ⊕R withg(y, 0) = 0 for ally∈ Λ andgu(y, 0) =τ(y)
for y ∈ K, and such that g(y,u ) <−1 outside K′× [−1, 1] for some compact
neighborhood K′ of K in Λ. For any ε > 0 let gε(y,u ) := εg(y,u/ε ). These
functions satisfy gε(y, 0) = 0, gε
y(y, 0) = 0 and gε
u(y, 0) = τ(y) for all y∈ K, and
gε(y,u )<−ε outside K′× [−ε,ε ]. Moreover, we have
|gε(y,u )|≤ C0|u|≤ C0ε, |gε
y|,|gε
yy|≤ C0ε, |gε
u|,|gε
yu|≤ C0, |gε
uu|≤ C0/ε
for (y,u )∈K′×[−ε,ε ] with a constantC0≥ 1 not depending onε. For 0<a ≤ 1/2
and ε> 0 consider the function
ψ(x,y,u ) :=aQ(x,y ) +gε(y,u ).
Our desired function ~φ will be a smoothing of
~ψ := max (Q−ε,ψ ).
Let us ﬁrst determine the region where ψ <Q−ε, or equivalently,
(10.1) gε(y,u ) +ε< (1−a)Q(x,y ).
For|u| > εor y /∈ K′ this inequality holds because the left hand side is negative
and the right hand side is nonnegative. Moreover, 1 −a≥ 1/2 implies
gε(y,u ) +ε≤ (C0 + 1)ε≤ 2(C0 + 1)ε(1−a),
so inequality (10.1) holds if Q(x,y ) > C1ε with the constant C1 := 2(C0 + 1) not
depending on ε and a. So we have ψ <Q−ε outside the compact region
W′ :={(x,y,u )|y∈K′,|u|≤ ε,Q (x,y )≤C1ε}.

218 10. MODIFICATIONS OF J-CONVEX MORSE FUNCTIONS
On the other hand, in the region
W :={(x,y,u )|y∈K′,Q (x,y ) +C0|u|≤ ε}⊂ W′
we have the reverse estimate
gε(y,u ) +ε≥ε−C0|u|≥ Q(x,y )≥ (1−a)Q(x,y ).
Hence ψ≥Q−ε on the neighborhood W of K.
We will show below that forε =a2 suﬃciently small the graph ofψ isJ-convex
onW′. Assuming this for the moment, note that the graph ofQ−ε is alsoJ-convex.
Thus by Corollary 3.23, we can C0-approximate ~ψ by a smooth function with J-
convex graph ~Σ which agrees with ψ on W and Q−ε outside W′. (Note that in
Corollary 3.23 the minimum appears rather than the maximum because the graphs
are cooriented from below rather than above). Now on any ﬁxed (i.e., independent
of a,ε ) compact neighborhood U of K′, the function Q−ε C2-approaches Q as
ε→ 0. Hence for small ε we can modify ~Σ outside W′ so that it agrees with Σ
outside U. This yields the desired hypersurface Σ ′.
It remains to prove J-convexity of the hypersurface Σ ψ ={v = ψ(z,u )} over
W′ for small a and ε. For this, cover K′ by ﬁnitely many Jst-holomorphic coordi-
nate charts in which Λ corresponds toiRn−1. Choose ε so small that the coordinate
charts cover the region {(x,y )| y∈ K′,Q (x,y )≤ C1ε}. We will show that the
normalized modulus of Jst-convexity of Σψ satisﬁes µ(Σψ)≥ ε2 for ε = a2 suﬃ-
ciently small. On the other hand, the deﬁnition of W′ shows that the distance to
Λ is bounded above by C2
√ε on the graph of ψ over W′, for some constant C2
independent of ε. Since J andJst coincide with their 7-jets along Λ, it follows that
‖J−Jst‖C2≤C3ε5/2 on the graph ofψ overW′. Thus by Corollary 3.37, the graph
of ψ overW′ is J-convex for suﬃciently small ε> 0.
So it remains to prove the estimate µ(Σψ)≥ε2. We write Σ ψ as the zero set
of the function Ψ(x,y,u,v ) := ψ(x,y,u )−v, whose gradient is given by |∇Ψ|2 =
1 +|∇ψ|2 = 1 +ψ2
u +|dzψ|2. Using the deﬁnition (3.11) of the normalized modulus
of convexity and Lemma 2.24 we ﬁnd
µ(Σψ) = m(LΣψ)
max{M(IIΣψ), 1} = m(HΨ)
max{M(HessΨ),|∇Ψ|}
= m(Hψ)
max{M(Hessψ),
√
1 +|∇ψ|2}
.
By Lemma 2.26, m(Hψ) =|∇Ψ|m(LΣψ) satisﬁes
m(Hψ)≥
Hmin
ψ (1 +ψ2
u)−|ψuu||dzψ|2− 2|dzψu||dzψ|
√
1 +ψ2u
1 +ψ2u +|dzψ|2
≥
Hmin
ψ −|ψuu||dzψ|2− 2|dzψu||dzψ| (1 +|ψu|)
1 +ψ2u +|dzψ|2 .
So for µ(Σψ)≥ε2 it suﬃces to show
(10.2)
Hmin
ψ −|ψuu||dzψ|2− 2|dzψu||dzψ| (1 +|ψu|)
≥ε2(1 +ψ2
u +|dzψ|2)max{M(Hessψ),
√
1 +ψ2u +|dzψ|2}.
By J-convexity of the function Q, we have Hmin
Q ≥ γ for some constant γ > 0.
Moreover,|Qz| ≤C|x| and all derivatives of Q involving a u-derivative vanish.

10.1. MOVING ATTACHING SPHERES BY ISOTROPIC ISOTOPIES 219
V a
V b
L
∇ψ
∇φ
Figure 10.3. Making the gradient of aJ-convex function tangent
to a totally real submanifold J-orthogonal to its level sets.
Here and in the following C denotes a generic constant that depends on C0,C 1,γ
but not on a,ε . The estimates for gε yield
Hmin
ψ ≥γa−Cε, |ψz|≤ Ca|x| +Cε, |ψu|,|ψzu|≤ C, |ψuu|≤ C/ε
for (y,u )∈ K′× [−ε,ε ]. It follows that the left hand side in (10.2) is estimated
from below by
A :=γa−Cε−Ca|x|− Ca2|x|2/ε.
Now on W′ we haveγ|x|2≤Q(x,y )≤C1ε, and hence
A≥γa−Cε−Ca√ε−Ca2.
To estimate the right hand side from above, we ﬁrst compute
M(Hessψ)≤C(aM(Q) +|gε
yy| +|gε
yu| +|gε
uu|)
≤C(aγ +ε + 1 + 1/ε)≤C/ε,
since γ is ﬁxed and a≤ 1/2. As 1 + ψ2
u +|dzψ|2≤C, we see that the right hand
side of (10.2) is bounded from above by Cε, and therefore (10.2) is implied by
γa−Cε−Ca√ε−Ca2≥ 0.
Choosing ε =a2, this becomes
γa−Ca2≥ 0
which is satisﬁed for ε = a2 > 0 suﬃciently small. This proves the estimate
µ(Σψ)≥ε2 and hence Lemma 10.3. □
Lemma 10.4. Let φ be a proper J-convex function on the complex manifold
V without critical values in [a,b ]. Let L ⊂ V [a,b] be a totally real submanifold
that intersects each level set J-orthogonally in a compact manifold (possibly with
boundary). Then there exists a J-convex functionψ,C1-close to φ, such that ψ =φ
on L and∇ψψ is tangent to L.
Moreover, if∇φφ is already tangent to L nearV [a,a′]∪V [b′,b] for some [a′,b′]⊂
(a,b ), then we can choose ψ =φ on V [a,a′]∪V [b′,b].
See Figure 10.3.
Remark 10.5. The gradient∇ψψ will in general not be C0-close to∇φφ. This
is possible despiteψ beingC1-close toφ because the metricgψ need not beC0-close
to gφ.

220 10. MODIFICATIONS OF J-CONVEX MORSE FUNCTIONS
Proof. If dimL < dimCV we extend L to a totally real submanifold L′⊂
V [a,b] of dimension dimL′ = dimCV , still intersecting all level sets J-orthogonally.
Hence it suﬃces to consider the case dim L = dimCV .
LetX be the unique vector ﬁeld tangent to L, orthogonal (with respect to the
metricgφ) to the intersection of L with level sets of φ, with dφ(X)≡ 1. (However,
X need not be orthogonal to the level sets ofφ). By J-orthogonality,JX is tangent
to the level sets of φ. The ﬂow of X deﬁnes a diﬀeomorphism Λ×i[a,b ]∼=L, where
Λ :=L∩Va. By Proposition 5.55, this diﬀeomorphism extends to a diﬀeomorphism
from a neighborhood of Λ×i[a,b ] in Λ C× C (where ΛC is a complexiﬁcation of Λ)
onto a neighborhood of L in V , such that the pullback of J (still denoted by J)
agrees with the standard complex structure Jst on ΛC× C up to second order along
Λ×i[a,b ] (which we will again denote byL). Then the Levi forms of functions with
respect to J and Jst agree along L, so we can compute Levi forms with respect to
Jst.
Denote coordinates on Λ C by z and on C by u +iv. Under this identiﬁcation
L corresponds to Λ×i[a,b ], and X =∂v, φ =v along L. Since the level sets of φ
are J-orthogonal to L, they are tangent to T ΛC⊕ R along L. Deﬁne the function
ψ(z,u,v ) :=v +Q(z) + 1
2f(z,v )u2
on ΛC× C, where Q := dist2
Λ for some Hermitian metric on Λ C and f is a positive
function. We compute
dψ =dv +dQ +f(z,v )udu + 1
2u2df,
dCψ =du +dQ◦JΛC−f(z,v )udv + 1
2u2dCf,
ωψ =−ddCψ =ωQ +f(z,v )du∧dv along L.
In particular,ψ isJ-convex anddψ =dv =dφ alongL. Hence by Proposition 3.26,
ψ can be extended to a J-convex function on V which agrees with φ outside a
neighborhood of L. Moreover, ψ can be chosen arbitrarily C1-close to φ with
modulus of J-convexitymψ bounded from below. The gradient of ψ is determined
by the equation
ωψ(∇ψψ,Y ) =−dCψ(Y )
for all Y ∈ TV . Now dCψ = du along L implies∇ψψ = f(z,v )−1∂v along L, so
∇ψψ is tangent to L.
Finally, suppose that ∇φφ is already tangent to L near V [a,a′]∪V [b′,b]. Pick
a cutoﬀ function β :V → [0, 1] which equals 0 outside V [a′,b′] and 1 where∇φφ is
not tangent to L. Construct ψ as above and set
θ := (1−β)φ +βψ.
This function agrees with φ on V [a,a′]∪V [b′,b], and by Lemma 3.28 (since mψ is
bounded from below), θ is J-convex for ψ suﬃcientlyC1-close to φ.
It remains to show that∇θθ is tangent toL at points x with 0<β (x)< 1. By
construction, we have φ(x) = ψ(x) and dφ(x) = dψ(x). Moreover, since ∇φφ(x)
is tangent to L, the choice of X implies that X is proportional to ∇φφ at x. So
the three vector ﬁelds X,∇φφ and∇ψψ are positively proportional at x. Since
∇ψψ =f(z,v )−1X along L, we can therefore choose the positive function f in the

10.1. MOVING ATTACHING SPHERES BY ISOTROPIC ISOTOPIES 221
construction of ψ to arrange∇φφ =∇ψψ along L∩{ 0 < β <1}. Since φ and ψ
agree to ﬁrst order along L, we have
dCθ = (1−β)dCφ +βdCψ, ω θ = (1−β)ωφ +βωψ
at the point x. Hence for any Y ∈TxV ,
ωθ(∇θθ,Y ) =−dCθ(Y ) =−(1−β)dCφ(Y )−βdCψ(Y )
= (1−β)ωφ(∇φφ,Y ) +βωψ(∇ψψ,Y )
= (1−β)ωφ(∇φφ,Y ) +βωψ(∇φφ,Y )
=ωθ(∇φφ,Y ).
This shows ∇θθ =∇φφ along L. In particular, ∇θθ is tangent to L, so θ is the
desired function. □
Proof of Proposition 10.1. Let Σ := Va. The ﬂow of the vector ﬁeld
∇φ/|∇φ| deﬁnes a diﬀeomorphism
Σ× [a,b ]∼=V [a,b].
Under this identiﬁcation, φ corresponds to the function (x,r )↦→r,∇φ/|∇φ| to the
vector ﬁeld∂r,L to Λ×[a,b ], and Λt to Λt×{a}. In view of Lemma 11.13, Λt×{r}
is isotropic for the contact structure ξr on Σ×{r} for all r∈ [a,b ].
Pick aC2-functiong : [a,b ]→ [0, 1] which equals 1 on [a,a′] and 0 on [b′,b ], for
some interval [a′,b′]⊂ (a,b ). For t∈ [0, 1] deﬁne
Lt :=
⋃
r∈[a,b]
Λtg(r)×{r}⊂ Σ× [a,b ].
This is a totally real submanifold which intersects each level set Σ ×{r} in the
isotropic submanifold
Λt,r := Λtg(r)×{r}.
LetXt,r be the unique vector ﬁeld tangent to Lt along Λt,r and orthogonal to Λt,r
(with respect to the metric gφ) with dr(Xt,r) = 1. In particular, Xt,r is transverse
to the level sets Σ×{r}. Hence by Lemma 10.3 there exist J-convex hypersurfaces
Σt,r transverse to ∂r such that Λt,r⊂ Σt,r, the contact structure ξr is contained in
T Σt,r along Λt,r, and JXt,r∈T Σt,r. Note that the last two conditions say that Lt
intersects Σt,r J-orthogonally for all r. Moreover, we may choose Σ t,r = Σ×{r}
for r outside [a′,b′].
By construction, the Σt,r for ﬁxedt and varyingr form a foliation nearLt. Thus
by Proposition 3.25, we can modify the Σ t,r to a J-convex foliation, keeping them
ﬁxed nearLt and forr outside [a′,b′]. Let ψt be the function which equals r on the
new hypersurfaces ~Σr,t. Pick a suﬃciently convex increasing function f : R→ R
such that f◦ψt is J-convex for all t∈ [0, 1]. Now we apply Lemma 10.4 to the
functions f◦ψt and the totally real submanifolds Lt. We ﬁnd J-convex functions
φt, C1-close to f◦ψt and agreeing with f◦ψt onLt and for r outside [a′,b′], such
that∇φtφt is tangent to Lt. Thus Lt is the image of Λ t,b = Λ0×{b} = Λ under
the ﬂow of−∇φtφt, and by construction Lt intersects Σ×{a} in Λt,a = Λt×{a}.
This proves property (iii).
By construction, φt agrees with f◦φ for r outside [a′,b′]. Moreover, since
L0 = L, we can arrange φ0 = f◦φ. It remains to ﬁnd an isotopy ht such that
φt =f◦φ◦ht. Deﬁne diﬀeomorphisms gt :V [a,b]→V [a,b] on the level φ−1(r) by

222 10. MODIFICATIONS OF J-CONVEX MORSE FUNCTIONS
following the ﬂow of−∇φφ down to Va and then the ﬂow of∇φtφt up to the level
φ−1
t (r). Then g0 = Id and φt =f◦φ◦gt. Moreover, gt = Id on V [a,a′] and
gt :V [b′,b]∼= Σ× [b′,b ]→ Σ× [b′,b ], (x,r )↦→
(
γt(x),r
)
with γt := gt|Vb′ . Deﬁne ht on the level φ−1(r) as gtρ(r) with a smooth function
ρ : [a,b ]→ [0, 1] which equals 1 on [a,b′] and 0 near b. Then ht = Id near b and ht
is the desired isotopy. This concludes the proof of Proposition 10.1. □
10.2. Relaxing the J-orthogonality condition
This section is an aside on the J-orthogonality condition used in the surround-
ing results in Chapter 8. Namely, Lemma 10.3 allows us to relax theJ-orthogonality
condition in Theorem 8.4 to the weaker condition that∂∆⊂∂−W is isotropic (i.e.,
tangent to the ﬁeld of complex tangencies):
Corollary 10.6. Let (W,J ) be a complex cobordism. Suppose that ∂−W is
J-concave as a boundary component of W . Let (∆,∂ ∆)⊂ (W,∂−W ) be a totally
real disc transverse to ∂−W and such that JT∂ ∆⊂ T∂−W . Then ∂−W∪ ∆ can
be surrounded by J-convex hypersurfaces.
Proof. Let Σ := ∂−W , S :=∂∆. Consider a collar G =S× [0,ε ]⊂ ∆, S×
0 = ∂∆. It can be extended to a collar ˆG = Σ× [0,ε ], Σ× 0 = ∂−W such that
(Σ×t)∩ ∆ =S×t andJT (S×t)⊂T (Σ×t),t∈ [0,ε ). By continuity there exists
δ∈ (0,ε ), such that the hypersurfaces Σ t are J-convex for t∈ [0,δ ]. According to
Lemma 10.3, we can modify the family Σ ×t by a C0-small isotopy ﬁxed on ∆ to
arrange for the hypersurface Σ×δ to beJ-orthogonal to ∆. Set ~∆ := ∆\
(
S×[0,δ )).
Now let U be any neighborhood of ∂−W∪ ∆. We can assume δ so small that
Σ×δ ⊂ U. Hence, we can apply Theorem 8.4 to ﬁnd a hypersurface ~Σ which
surrounds (Σ×δ)∪~∆ in ~W :=W\
(
Σ× [0,δ )
)
. Then it also surrounds ∂−W∪ ∆
in W . □
The same argument allows us to relax the J-orthogonality condition in Theo-
rem 8.23:
Corollary 10.7. Let (W,J ) be a complex cobordism and(∆,∂ ∆)⊂ (W,∂−W )
a totally real disc transverse to ∂−W and such that JT∂−∆ ⊂ T∂−W . Then
∂−W∪ ∆ is a local J-convex retract.
Similarly, in Corollary 8.26 one can relax the condition of J-orthogonality ofL
to W by requiring instead that JT∂L ⊂T∂W .
On the other hand, the condition that ∂∆⊂∂−W is isotropic is also necessary
for existence of a J-convex surrounding:
Proposition 10.8. Let W ⊂ V be a compact domain with smooth J-convex
boundary in a complex manifold (V,J ). Let L⊂V\IntW be a totally real submani-
fold transversely attached to ∂W along a submanifold ∂L⊂∂W that is somewhere
not tangent to the ﬁeld of complex tangencies ξ⊂T∂W . Suppose that L and ∂W
are real analytic. Then W∪L is not holomorphically convex, and therefore cannot
be surrounded by J-convex hypersurfaces.
Proof. Let us extendL to a larger real analytic totally real submanifold~L⊃L
such that∂~L⊂ IntW and ~L⊂W∪L. By assumption, there exists a point p∈∂L

10.3. MOVING CRITICAL LEVELS 223
and a real line λ⊂Tp∂L such that Jλ is transverse to Tp∂W . There exists a real
analytic family of embeddings hs : [−ε1,ε 1]→~L, s∈ [−τ,τ ], such that
• h0(0) =p;
• h′
0(0)∈ λ and Jh′
0(x) is inward transverse to the boundary ∂W for all
x∈ [−ε,ε ];
• hs([−ε,ε ])⊂W for s≤ 0;
• hs(0) /∈W for s> 0.
We complexify the familyhs for someδ >0 to a real analytic family of holomorphic
embeddings Hs : P :={z = x +iy;|| x|≤ ε, |y|≤ δ} ↪→ V , s∈ [−τ,τ ]. Set
P+ :=P∩{y≥ 0}. Then for suﬃciently small σ <τ we have
• Hs(P+)⊂W for s∈ [−σ, 0];
• Hs(∂P+)⊂~L⊂W∪L for s∈ [−σ,σ ];
• Hs(P+)⁄⊂W∪L for s∈ (0,σ ].
By Example 5.3, this implies that W∪L is not holomorphically convex. □
Remark 10.9. Proposition 10.8 should remain true without the real analyticity
hypothesis.
10.3. Moving critical levels
In this section we prove the following analogue of Lemma 9.39 for J-convex
functions. Recall that a Stein cobordism ( W,J,φ ) is a Morse cobordism ( W,φ )
with a complex structure J for which φ is J-convex, equipped with the gradient
vector ﬁeld∇φφ.
Proposition 10.10. Let (W,J,φ ) be an elementary Stein cobordism withφ|∂±W
= a± and critical points p1,...,p n of values φ(pi) = ci. For i = 1,...,n let
ci : [0, 1]→ (a−,a +) be smooth functions with ci(0) = ci. Then there exists a
smooth family of J-lc Morse functions φt, t∈ [0, 1], with φ0 = φ and φt = φ
on Op∂W , such that all φt have the same critical points and stable discs and
φt(pi) =ci(t).
Proof. Step 1. Pick a family of diﬀeomorphisms ft : [a−,a +]→ [a−,a +]
such that f0 = Id and ft◦ci(t)≤ci for all i and t. If we can ﬁnd a family of i-lc
functionsψt starting at φ with critical values ψt(pi) =ft◦ci(t), then the functions
φt =f−1
t ◦ψt will have the desired critical values ci(t). So we may assume without
loss of generality that ci(t)≤ci for all i and t.
Moreover, as we will construct the functionsφt to agree withφ outside a neigh-
borhood of the stable discs, it suﬃces to consider the case with a unique critical
pointp of index k. Let c(t)≤c =φ(p),t∈ [0, 1], be the given function and denote
by ∆ the stable k-disc of p. Pick a value a with a− < a <mintc(t). We may
assume without loss of generality a =−1 and c = 0; the general case then follows
by composing all functions with the aﬃne function x↦→ (c−a)x +c.
Consider the standard handle Hε = Dk
1+ε×D2n−k
ε ⊂ Cn. Here zj = xj +
iyj are complex coordinates such that ( y1,...,y k) are coordinates on Dk
1+ε and
(x1,...,x n,yk+1,...,y n) on D2n−k
ε . As in Chapter 4, we introduce the functions
r :=
√
x2
1 +··· +x2n +y2
k+1 +··· +y2n, R :=
√
y2
1 +··· +y2
k.
After these preparations, we now turn to the actual proof.

224 10. MODIFICATIONS OF J-CONVEX MORSE FUNCTIONS
Step 2. Fix somea> 1. As in the proof of Theorem 8.5, after C1-perturbing
φ near ∆, there exists an embedding F : Hγ ↪→ W mapping Dk
1+γ to ∆ such
that F∗φ =ar2−R2, and F∗J satisﬁes the estimate ‖F∗J−i‖C2≤c(a,n )γ12 in
Theorem 4.1. Let Ψ = Ψ 1 : Cn→ R be theJ-lc function provided by Corollary 4.4.
It agrees with F∗φ near ∂Hγ and up to target reparametrization near Dk
1+γ, and
it satisﬁes Ψ(0) <−1.
The homotopy smooth max(F∗φ, Ψ−t) is ﬁxed near ∂Hγ∪Dk
1+γ, agrees with
F∗φ for large t and with smooth max(F∗φ, Ψ) at t = 0. After applying this ho-
motopy we may thus assume that F∗φ = smooth max(F∗φ, Ψ). Now the functions
Φs := smooth max(F∗φ +s, Ψ) agree with F∗φ near ∂Hγ and have critical values
Φs(0, 0) = s at the origin. Hence the J-lc functions φt := F∗Φc(t) (extended by φ
outside F (Hγ)) have critical values φt(p) =c(t). □
10.4. Creation and cancellation of critical points
In this section we state our two main results concerning the creation and can-
cellation of critical points ofJ-convex functions. For the relevant concepts in Morse
theory we refer to Chapter 9. Recall in particular that a family ( Xt,φt), t∈ [0, 1],
of functions and gradient-like vector ﬁelds is called a cancellation (resp. creation)
family if there is a t0∈ (0, 1) such that the following holds:
(i) for t>t 0 (resp. t<t 0) the function φt has no critical points;
(ii) for t<t 0 (resp. t>t 0) it has exactly two critical points of index k and
k− 1 connected by a unique trajectory of Xt along which the stable and
unstable manifolds intersect transversely;
(iii) for t =t0 it has a unique embryonic critical point.
ForJ-convex functions we always assume in addition that Xt =∇φtφt. We will
say that a deformation of functions φt : W → R, t∈ [0, 1], is weakly supported
in U ⊂ W if there exists an isotopy αt : R→ R such that on W\U we have
φt =αt◦φ0.
The following theorem describes the creation of critical points of J-convex
functions.
Theorem 10.11 (creation theorem) . Let (W,J,φ ) be a Stein cobordism such
that the J-convex functionφ has no critical points. Then given any point p∈ IntW
and an integer k = 1,...,n , there is a creation family φt of J-convex functions,
weakly supported inOpp, such that φ0 =φ and φ1 has a pair of critical points of
index k and k− 1.
Note that in ordinary Morse theory the analogue of Theorem 10.11 is rather
trivial: using an appropriate cut-oﬀ construction any local creation family can be
implanted into a globally deﬁned family, see Lemma 9.47 above. However, in the
context of J-convex functions this scheme does not seem to work. In fact, we do
not know whether the statement remains true if one drops the word “weakly” and
tries to construct a locally supported creation family.
The following theorem describes the cancellation of critical points of J-convex
functions.
Theorem 10.12 (cancellation theorem) . Let (W,J,φ ) be a Stein cobordism
such that the J-convex function φ has exactly two critical points p,q of index k
and k− 1, respectively, which are connected by a unique gradient trajectory along

10.6. SURROUNDING A STABLE HALF-DISC 225
which the stable and unstable manifolds intersect transversely. Set a− := φ|∂−W ,
b := φ(q), c := φ(p). Choose a regular value a∈ (a−,b ). Let ∆ be the closure of
the stable disc of the critical point p in{φ≥ a}. Then there exists a cancellation
family φt : W → R, t∈ [0, 1], of J-convex functions, weakly supported in Op ∆,
such that φ0 =φ and φ1 has no critical points.
The proof of these two theorems will occupy the remainder of this chapter.
10.5. Carving one J-convex function with another one
As preparation for the proofs, we describe in this section a general way to
modify one J-convex function with the help of another one.
Let φ : U → R be a J-convex function on an open set U and Σ = {φ = a}
be a regular level set. Let us denote by U− and U+ the domains {φ≤ a} and
{φ≥ a}, respectively. Let ψ : Ω→ [c−,c +] be another J-convex function deﬁned
on a compact subdomain Ω ⊂U with boundary ∂Ω =∂+Ω∪∂−Ω∪∂vΩ such that
ψ|∂±Ω =c± and ∂+Ω∪∂vΩ⊂ IntU+. See Figure 10.4 (a).
For a small ε> 0 let us denote by Ωε the domain{c− +ε≤ψ≤c+−ε}⊂ Ω,
and by Uε
− the domain {φ≤ a−ε}⊂ U−. By composing φ,ψ with increasing
weakly convex diﬀeomorphisms g,h : R→ R we can arrange that the functions
~φ =g◦φ and ~ψ =h◦ψ satisfy the following conditions:
• ~ψ >~φ on Uε
−∩ Ωε;
• ~φ> ~ψ on (U+∩ Ω)∪∂−Ω.
To see this, ﬁrst compose ψ with h such that h(c−) < min Ωφ and h(c− +ε) >
max Ωεφ, thus ~ψ >φ on Ωε and ~ψ <φ on ∂−Ω. Then compose φ with g such that
g(x) =x forx≤a−ε andg(a)> maxU+∩Ω~ψ, thus ~φ> ~ψ on (U+∩ Ω)∪∂−Ω and
~ψ >~φ on Uε
−∩ Ωε.
Take the function max (~φ,~ψ) and apply to it the smoothing procedure from
Section 3.2. We will call this operation carving the level set Σ ofφ with the function
ψ. The resulting function is shown in Figure 10.4 (b); it will be denoted by
carvψ(φ, Σ).
Though there are numerous ambiguities in the deﬁnition of this operation, it is
important that it can be done for families of functions smoothly dependent on
parameters, thatε can be chosen arbitrarily small, and the smoothing can be chosen
C0-close to max (~φ,~ψ) in the sense of Corollary 3.15. In particular, everywhere
below where we use the notation carvψ(φ, Σ) we assume thatε is chosen suﬃciently
small and the approximation is good enough.
Note that if both functions φ,ψ are transverse to the same vector ﬁeld then so
is carvψ(φ, Σ) (see Corollary 3.20), hence the carving operation does not create new
critical points. It follows that carving is well-deﬁned in the class of J-lc functions
without critical points; note that in this case we can rescale the functions to make
~φ =φ.
10.6. Surrounding a stable half-disc
The main ingredient for cancellation of critical points are J-convex surround-
ings for a stable half-disc which we construct in this section. For this, consider the
following setup as in Section 9.6.

226 10. MODIFICATIONS OF J-CONVEX MORSE FUNCTIONS
(a)
(b)
Uε
−
Ωε
a
a
a−ε
a−ε
Σ
Σ
∂+Ω ∂vΩ
∂−Ω
U+
U−
mψ(φ, Σ)
c+
c+ −ε
c− +ε
c−
ψ
φ
~φ> ~ψ ~ψ >~φ
Figure 10.4. Carving the level set Σ of φ with the function ψ.
Let Rk = Rk−1× R be the space with coordinates ( x1,...,x k). Let Dt, t> 0,
denote the disc {∑k
j=1x2
j ≤ t2} of radius t, and we write D instead of D1. We
further denote byD− the lower half-discD∩{xk≤ 0}, and set∂+D− =D−∩{xk =
0} and∂−D− =∂D∩D−, so that we have ∂D− =∂−D−∪∂+D−. See Figure 9.4.
Viewing Rk as a coordinate subspace of Cn with complex coordinates ( x1 +
iy1,...,x n +iyn) we will consider the splitting Cn = Rk× R2n−k and write z∈ Cn

10.6. SURROUNDING A STABLE HALF-DISC 227
Σ1
D
xk
p
∂+D−
∂−D−
β = −1
x1, . . . , xk−1
Figure 10.5. The function β near the lower half-disc.
as z = (x,u ), where x = (x1,...,x k) and u = (xk+1,...,x n,y 1,...,y n). Set
R =||x|| =
vuu√
k∑
1
x2
j, r =||u|| =
vuu√
n∑
k+1
x2
j +
n∑
1
y2
j,
R′ =
vuu√
k−1∑
1
x2
j, r ′ =
vuu√
n∑
k
x2
j +
n∑
1
y2
j.
For a constant A> 1 we introduce the vector ﬁelds
→
v =A ∂
∂xk
−
k−1∑
1
xj
∂
∂xj
,
→
u =
n∑
k+1
xj
∂
∂xj
+
n∑
1
yj
∂
∂yj
.
Given a compact subset K ⊂ Cn and σ > 0 we denote by Uσ(K) its open
σ-neighborhood in Cn.
Suppose we are given an i-convex function φ0 : Cn→ R of the form
φ0(x,u ) =β(x) +Ar2,
where the function β : Rk→ R satisﬁes the following conditions (see Figure 10.5):
(i) β has exactly two nondegenerate critical points: an index k− 1 critical
point of value 0 at 0, and an index k critical point p∈ IntD− of value
0<c<A − 1;
(ii) β >−1 on D−\∂+D− and β(x) =Ax2
k−R′2 onOp (∂+D−).

228 10. MODIFICATIONS OF J-CONVEX MORSE FUNCTIONS
∂+D−
∂−D−
Σ1
D
Figure 10.6. The ﬁrst surrounding hypersurface Σ 1 and the disc D.
Let us ﬁx a neighborhood U⊂ Cn of the disc{xk≤ 0, β≥− 1}⊂ Rk. We will
deform the function φ0 through i-lc functions φt : Cn→ R satisfying the following
conditions:
• φt has exactly two nondegenerate critical points at 0 and p;
• φt =φ0 outside U.
We will call such functions and deformations admissible. The desired surrounding
will be a combination of three surroundings. Set Σ 0 :={φ0 =−1}.
First surrounding. Note that φ0 =−R′2 +Ar′2 on a neighborhood U1⊂U
of the (k− 1)-disc∂+D−. So we can apply Corollary 4.4 to construct an admissible
deformationφt,t∈ [0, 1], with the following properties (see Figures 10.5 and 10.6):
• φt =φ0 outside U1;
• the regular level set Σ 1 = φ−1
1 (−1) agrees with Σ 0 outside U1 and with
{r′ =δ} in a smaller neighborhood of ∂+D−, for some δ >0;
• the k-disc D :={u = 0, φ1≥− 1,xk < 0} is attached i-orthogonally to
Σ1.
Here the last property follows from Lemma 4.14.
Second surrounding. The function φ1|D has a unique non-degenerate
maximum at p of value c and φ1|∂D≡− 1. Hence there exists a diﬀeomorphism
f :D→ D such that
φ1◦f(x) =c− (c + 1)R2.
Using Proposition 5.55, we extend f to a diﬀeomorphism F :OpD→O p D such
that the pullback complex structure F∗i agrees with i to order 7 along D. Using
Proposition 3.26, we adjust ~φ1 = F∗φ1 via a C1-small admissible deformation to
make it equal to c− (c + 1)R2 +Ar2 in a neighborhood ~U2 of D. Next we apply
Corollary 4.4 to construct an F∗i-lc deformation ~φt, t∈ [1, 2], supported in ~U2
such that the regular level set ~Σ2 = ~φ−1
2 (−1) surrounds D. So φt, t∈ [1, 2], is an
admissible i-lc deformation with the following properties:
• φt =φ1 outside a neighborhood U2 of D.

10.6. SURROUNDING A STABLE HALF-DISC 229
x
uD−
Σ0
Σ2
Figure 10.7. The dumbell-shaped cross-section of the second sur-
rounding hypersurface Σ 2.
• the regular level set Σ 2 = φ−1
2 (−1) agrees with Σ 1 outside U2 and sur-
rounds D−.
See Figure 10.7 for a cross-section of Σ 2. Before proceeding further, consider the
following property of a function φ : Cn→ R:
(10.3)
→
u·φ≥µr2 for some constant µ> 0.
Lemma 10.13. The above functions φt, t∈ [0, 2] satisfy property (10.3).
Proof. Note ﬁrst that the function φ0 satisﬁes (10.3) with constant µ = 2A.
The functions φt,t∈ [0, 1] satisfy (10.3) because on U1 they are given by shapes of
the form Ψt(R′,r′) with ∂Ψt
∂r′ > 0.
Next note that the map F above has complex linear diﬀerential along D, so it
is of the form
F (x,y,z ) =
(
f(x),Df (x)y,B (x)z
)
+O(r2),
where y = (y1,...,y k), z = (zk+1,...,z n), and B(x) is complex linear for each
x∈ D. Since the canonical vector ﬁeld
→
u is preserved by any linear map in the
u-variables, it follows that
F∗→
u =
→
u +O(r2),
and hence the pullback function ~φ1 = F∗φ1 satisﬁes (10.3) in a suﬃciently small
neighborhood ofD. By Proposition 3.26 (f), the ensuing C1-small adjustment of~φ1
nearD also preserves property (10.3). Now the functions ~φt,t∈ [1, 2] satisfy (10.3)
because on ~U2 they are given by shapes of the form Ψt(R,r ) with ∂Ψt
∂r > 0. Finally,
by the argument above the functions φt =F∗~φt, t∈ [1, 2], still satisfy (10.3). □
Third surrounding. We will now construct another i-lc function Ψ and use
the carving construction from Section 10.5 to construct our third surrounding. For
this, let us rename φ2 toφ. Pick a value a slightly below−1 such that the level set
Σ := φ−1(a) surrounds D− and its intersection with the set {R≤ 1} is contained
in{r<δ }.

230 10. MODIFICATIONS OF J-CONVEX MORSE FUNCTIONS
R
1
Ψ = δ
Ψ = 0
δ γ r
Figure 10.8. The shape function Ψ.
By Corollary 4.3 (with a =−1−σ and after a target reparametrization), there
exists an i-lc shape function Ψ : Cn⊃ Ω→ (0,δ ) without critical points and with
the following properties, see Figure 10.8:
• Ψ(r,R ) =r for r∈ (0,δ ], R≤ 1.
• Ψ(r,R ) = f(Ar2− R2) for r ≥ γ, where f : (a,−1] → (0,δ ] is an
increasing diﬀeomorphism.
Figure 10.9 shows the hypersurface Σ and the level sets of Ψ. So for any t∈ (0,δ ]
the restriction Ψt of Ψ to the set Ω t := Ψ−1([t,δ ]) together with φ, Σ satisﬁes the
hypotheses of Section 10.5. Let
φt := carvΨt(φ, Σ)
be the carving of the level set Σ of φ with the function Ψ t. Note that φδ = φ.
We claim that φt, t∈ (0,δ ], is an admissible deformation of i-lc functions with the
following properties (see Figure 10.9):
(j)
→
u·φt > 0 foru⁄= 0, and
→
v·φt > 0 on the set{u = 0, R≤ 1, 0<x k <δ};
(jj) for t suﬃciently small, some level set Σ t of φt surrounds the disc D− in
Uδ(D−) and contains the set {r =t, R≤ 1, xk≤δ/2}.
Property (jj) is clear from the construction. For property (j), note ﬁrst that the
functions φ (by Lemma 10.13) and Ψ (since it is a shape) are both transverse to
the vector ﬁeld
→
u on Ω∩{u⁄= 0}. On the other hand, the property
→
v·φt > 0 on
the set{u = 0, R≤ 1, 0<x k <δ} holds during the ﬁrst surrounding deformation
above because shapes Ψ(r′,R′) have this property, and the following deformations
are ﬁxed on this set. In view of property (j), the carving construction does not
create new critical points, so the deformation φt is admissible.

10.7. PROOF OF THE CANCELLATION THEOREM 231
x
δ
δ
Σ = φ−1(a)
Σt
u
Ψ−1(δ)
Ψ−1(t)
Figure 10.9. Carving the level set Σ of φ with the shape function Ψ t.
10.7. Proof of the cancellation theorem
After these preparations, we now prove Theorem 10.12 in three steps. The ﬁrst
two steps contain preliminary deformations not aﬀecting the critical points; the
actual cancellation happens in Step 3.
Step 1. Let (W,J,φ ) and ∆ be as in Theorem 10.12. After a C2-small
perturbation of φ near p and q, we may assume that it agrees with a standard
quadratic function as in Lemma 2.2 in suitable holomorphic coordinates near p,q .
Then Lemma 9.30 shows that ∆ is an embedded half-disc.
After rescaling φ we may assume that a =−1 and b = 0, so we have φ(p) =c,
φ(q) = 0 andφ|∂−∆≡− 1. Pick any A>c + 1. Then there exists a diﬀeomorphism
f : ~D− → ∆ from a half-disc ~D− ⊂ Rk containing D− such that the pullback
function β := φ◦f satisﬁes conditions (i-ii) in Section 10.6. Here and in the
following we use the notation from Section 10.6.
Using Proposition 5.55, we extend f to a diﬀeomorphism F :Op ~D−→O p ∆
such that the pullback complex structure F∗i agrees with i to order 7 along ~D−.
Let ~A≥ A be so large that the function β(x) + ~Ar2 on Cn is i-convex. Using
Proposition 3.26, we adjust φ◦F via a C1-small admissible deformation to make
it equal to β(x) + ~Ar2 in a neighborhood of ~D−. Now pick an increasing convex
function ξ : R+→ R+ which agrees with Ax2 near x = 0 and with ~Ax2 for x≥ε,
and modifyβ near{xk = 0} to~β(x) =ξ(xk)−R′2. Then the function ~β(x)+ ~Ar2 is

232 10. MODIFICATIONS OF J-CONVEX MORSE FUNCTIONS
stilli-convex. After renaming ~A,~β back toA,β , the functionφ0(x,u ) =β(x)+Ar2
thus satisﬁes the conditions in Section 10.6.
In the following steps we will modify φ0 through i-convex functions φt on a
neighborhood of the half-disc ~D−. The tangency condition on F∗i and Proposi-
tion 4.34 ensure that the resulting functions F∗φt on W will be J-convex.
Step 2. After the three admissible deformations in Section 10.6, we may
replaceφ0 by the function φt satisfying conditions (j-jj) at the end of Section 10.6,
for some arbitrarily small t >0. Let Σ t =φ−1
t (ct) be the level set from condition
(jj). Note that ct > c= maxD−φt. Let ψt := g◦φt with an increasing function
g : R→ R satisfying g(x)≤ x, g(x) = x for x≥ ct, and g(x) < b= minUδ(D−)φt
for x≤c′
t, for some c′
t∈ (c,ct). Then φt = max (φt,ψt).
More generally, suppose that φ is an i-lc function on Uδ(D−) satisfying the
following conditions:
(i)
→
u·φ> 0 for u⁄= 0;
(ii) φ =φt on Uδ(∂−D−)∪{u = 0, R≤ 1, δ/2<x k <δ};
(iii) b≤φ≤c.
Then smooth max(φ,ψt) is ani-lc function which coincides withφt outsideUδ(D−)
and with φ near D−. Moreover, conditions (i-ii) for φ together with condition (j)
forφt ensure that the critical points of smooth max(φ,ψ ) coincide with the critical
points of φ on the half-disc Dδ
− :={u = 0, R≤ 1, xk≤δ/2}.
Step 3. Recall that the restriction βt :=φt|Dδ
−
is a Morse function with two
critical pointsp,q of indicesk,k−1 and valuesc, 0 connected by a unique trajectory
of the vector ﬁeld Xt =∇φtφt. Moreover, Xt is inward pointing along ∂−Dδ
− and
outward pointing along ∂+Dδ
−. Hence by Lemma 9.49 there exists a cancellation
familyβs,s∈ [t, 1], ﬁxed near ∂Dδ
−, such thatβ1 has no critical points. We extend
βs byβt to{R≥ 1}.
Pick a constant B≥ A so large that the function βs(x) +Br2 is i-convex in
Uδ(D−) for all s∈ [t, 1]. Using Proposition 3.26, we modify φt such that it agrees
withβt(x) +Br2 nearDδ
−. Proposition 3.26 (f) ensures that this can be done pre-
serving the condition
→
u·φt > 0 foru⁄= 0. After replacing φt by smooth max(φt,ψt′)
as in Step 2, for suﬃciently small t′∈ (0,t ), and renaming t′ back to t, we may
hence assume that φt =βt(x) +Br2 on the set{x∈Dδ
−,r≤t}. According to Step
2, we now obtain the desired cancellation family as smooth max( βs(x) +Br2,ψt),
s∈ [t, 1]. This completes the proof of Theorem 10.12. □
10.8. Proof of the creation theorem
The proof of Theorem 10.11 follows the same steps as the proof of Theo-
rem 10.12, but it is much simpler and does not require the preparations in Sec-
tion 10.6.
Step 1. Let (W,J,φ ), p∈ IntW and 1 ≤ k≤ n be as in Theorem 10.11.
After adding a constant to φ we may assume that φ(p) = −1. Pick an isotropic
embedded (k− 1)-sphere Λ through p in the level set {φ =−1}. For some d <1
close to 1 denote by L⊂{− 1≤ φ≤− d2}⊂ IntW the image of Λ under the
gradient ﬂow of φ.
We use the notation r,R from Section 10.6. There exists a diﬀeomorphism
f :{d≤ R≤ 1, r = 0}→ L such that f∗φ(R) =−R2. Using Proposition 5.55,
we extend f for some γ >0 to an embedding F :Uγ :={d−γ≤R≤ 1 +γ, r≤

10.8. PROOF OF THE CREATION THEOREM 233
R
1
1 + γ
d
d − γ
Σ = {Ψ1 = −1}
δ γ r
Figure 10.10. The modiﬁed shape function Ψ 1.
γ} ↪→ W such that the pullback complex structure F∗i agrees with i to order 7
along{r = 0}. After applying Proposition 3.26 and shrinking γ, we may assume
that F∗φ(r,R ) =Ar2−R2 =: Ψst(r,R ) on Uγ, for any chosen constant A> 1. In
the following we will deform the function Ψst onUγ, keeping it ﬁxed near ∂Uγ, and
then implant it back into W byF to get the desired homotopy.
Step 2. A slight variation of Corollary 4.4 yields a smooth family of J-lc
functions Ψt : Cn→ R,∈ [0, 1], with the following properties (see Figure 10.10):
(i) Ψt is of the form Ψt(r,R ) with ∂Ψt
∂r > 0 and ∂Ψt
∂R ≤ 0;
(ii) Ψ 0 = Ψst and Ψt = Ψst outside Uγ;
(iii) Ψt is target equivalent to Ψ st near{r− = 0};
(iv) Ψ 1≡− 1 on the set {r =δ, d≤R≤ 1}, for some δ∈ (0,γ ).
To obtain this, we only need to replace the condition g(aγ2)<−1 in the proof of
Corollary 4.4 by the conditions g(−d2) <−1 and g
(
−(d−γ)2)
>−1. Note that
by construction we have Ψ 1 = max (Ψ1,g◦ Ψst).
Step 3. After another application of Proposition 3.26 we may assume that
Ψ1 = smooth max(Ψ1,β (x) +Ar2) on Vγ ={r≤ γ,d ≤ R≤ 1}, where β is the
restriction of Ψ to the cylinder Z ={r = 0,d ≤ R≤ 1}. Note that β has no
critical points and is constant on∂Z. By Lemma 9.47 there exists a creation family
βt, t∈ [0, 1], starting from β0 = β and creating a pair of critical points of index
k,k−1 at some timet0∈ (0, 1). Moreover, βt is ﬁxed on∂Z and we make sure that
maxβt = maxβ and minβt = minβ. We choose the constant A so large that the
functions βt(x) +Ar2 are F∗i-convex for all t∈ [0, 1]. Then the desired creation
family is the push-forward under F of smooth max(βt(x) +Ar2, Ψ1). Note that all
the deformations can be made supported in an arbitrarily small neighborhood of
the given point p. This completes the proof of Theorem 10.11. □



Part 4
From Stein to Weinstein and Back



11
Weinstein Structures
In this chapter we introduce Weinstein cobordisms and manifolds and establish
their basic properties. After a more general discussion of Liouville structures in the
ﬁrst 3 sections, we deﬁne Weinstein structures in Section 11.4.
In Section 11.5 we deﬁne the canonical map from Stein to Weinstein structures.
The construction of a homotopy inverse to this map will be the main theme of
Chapters 13 and 15.
In Section 11.6 we introduce Weinstein and Stein homotopies and show that
diﬀerent exhausting J-convex functions lead to homotopic Stein structures. In
Section 11.7 we prove that every Stein structure on Cn with a unique critical point
is homotopic to the standard structure. In the ﬁnal Section 11.8 we introduce the
classes of subcritical and ﬂexible Weinstein structures, which will be extensively
studied in Chapter 14.
11.1. Liouville cobordisms and manifolds
In this and the following two sections we discuss some basic properties of Li-
ouville structures. See [ 168, 169] for more background.
A 1-formλ on a manifoldV such thatdλ =ω is symplectic is called a Liouville
form. The vector ﬁeld X that is ω-dual to λ, i.e., such that iXω = λ, is called
the Liouville ﬁeld of λ. Note that the equation dλ =ω is equivalent to LXω =ω.
If X integrates to a ﬂow Xt : V → V then (Xt)∗ω = etω, i.e., the Liouville ﬁeld
X is (symplectically) expanding, while−X is contracting. By an exact symplectic
manifold we will mean a pair ( V,λ ) where λ is a Liouville form, or equivalently, a
triple (V,ω,X ) whereX is a Liouville ﬁeld for the symplectic formω, i.e., satisfying
LXω =ω. Note that
(11.1) iXλ = 0, i Xdλ =λ, L Xλ =λ,
so the ﬂow of X also expands the Liouville form, ( Xt)∗λ = etλ. A map ψ :
(V0,λ 0)→ (V1,λ 1) between exact symplectic manifolds is called exact symplectic if
ψ∗λ1−λ0 is exact.
A Liouville manifold is an exact symplectic manifold (V,ω,X ) such that
• the expanding vector ﬁeld X is complete, and
• the manifold is convex, see [49], in the sense that there exists an exhaus-
tionV =⋃∞
k=1Vk by compact domainsVk⊂V with smooth boundaries
along which X is outward pointing. 1
1This notion of symplectic convexity is slightly more restrictive than one given in [ 49]. How-
ever, we do not know any examples of symplectic manifolds that are convex in one sense but not
the other.
237

238 11. WEINSTEIN STRUCTURES
Note that the sets Vk are invariant under the contracting ﬂow X−t,t> 0. The set
Skel(V,ω,X ) :=
∞⋃
k=1
⋂
t>0
X−t(Vk)
is independent of the choice of the exhausting sequence of compact sets Vk and is
called the skeleton of the Liouville manifold (V,ω,X ). We have
Lemma 11.1. Int Skel(V,ω,X ) = ∅.
Proof. For each compact set Vk we have
Volume
(
X−t(Vk)
)
=e−t 1
n!
∫
Vk
ωn−→
t→∞
0,
and hence Volume
(⋂
t>0X−t(Vk)
)
= 0 for all k∈ N. □
We say that a Liouville manifold ( V,ω,X ) is of ﬁnite type if its skeleton is
compact. In this case, let W ⊂ V be a compact domain containing the skeleton
with smooth boundary Σ = ∂W along which X is outward pointing (e.g. W =Vk
for large k). Then the forward ﬂow of X starting from Σ deﬁnes a diﬀeomorphism
V\ IntW ∼= Σ× [0,∞). (For this note that for every p∈ V , X−t(p) gets close
to the skeleton as t→∞ and thus in contained in W for large t). Under this
diﬀeomorphism the Liouville form λ =iXω corresponds to etα, where t∈ R is the
parameter of the ﬂow and α :=λ|Σ. The form α is contact, and thus (V\ IntW,ω )
can be identiﬁed with the positive half of the symplectization of the contact manifold
(Σ,ξ = kerα). In fact, the whole symplectization of (Σ ,ξ ) sits in V as⋃
t∈RXt(Σ)
and this embedding is canonical in the sense that the image is independent of the
choice of Σ: its complement V\⋃
t∈RXt(Σ) is exactly the skeleton Skel(V,ω,X ).
The following useful lemma shows that for ﬁnite type Liouville manifolds we
need not distinguish between symplectomorphisms and exact symplectomorphisms.
Lemma 11.2. Any symplectomorphism f : (V,λ )→ (~V, ~λ) between ﬁnite type
Liouville manifolds is diﬀeotopic to an exact symplectomorphism.
Proof. We havef∗~λ =λ−θ for a closed 1-form θ. Let Σ be a hypersurface
in V transverse to the Liouville ﬁeld of λ and bounding a compact domain W
containing the skeleton, so the Liouville ﬂow deﬁnes a splitting V\ IntW∼= Σ×
[0,∞) as above. Since the projection π : Σ×[0,∞)→ Σ induces an isomorphism on
de Rham cohomology, we can writeθ|Σ×[0,∞) =π∗β+dF for a closed 1-formβ on Σ
and a smooth function F on Σ× [0,∞). Pick a cutoﬀ function ρ :V → [0, 1] which
equals 0 on W and 1 on Σ× [1,∞) and deﬁne the function G :=ρF and the closed
1-formη :=θ−dG onV . Since η =π∗β on Σ×[1,∞), the symplectic vector ﬁeldY
onV deﬁned byiYω =η is complete. Let h :V →V be the time 1 map of its ﬂow.
SinceLYη = 0 and LYλ =η +diYλ, it satisﬁes h∗η =η andh∗λ =λ +η +dH for
some function H on V . Then the diﬀeomorphism g :=f◦h :V → ~V is diﬀeotopic
to f and satisﬁes
g∗~λ =h∗(λ−θ) =h∗(λ−η−dG) =λ +d(H−h∗G).
□
Remark 11.3. The contact manifold (Σ ,ξ ) above is canonically determined
by the ﬁnite type Liouville manifold ( V,ω,X ). We do not know whether (Σ ,ξ )

11.2. LIOUVILLE HOMOTOPIES 239
actually depends on the Liouville form λ or only on the symplectic form ω = dλ.
The answer depends on the following open problem: Does symplectomorphism of
symplectizations imply contactomorphism of contact manifolds? We do not know
how to distinguish contact manifolds with the same symplectization by currently
known invariants.
A closely related concept is that of a Liouville cobordism (W,ω,X ). This is
a (compact) cobordism W with an exact symplectic structure ( ω,X ) such that X
points outwards along ∂+W and inwards along ∂−W . A Liouville cobordism with
∂−W = ∅ is called a Liouville domain .
For a Liouville domain (W,ω,X ), the backward ﬂow ofX yields a collar neigh-
borhood (−ε, 0]×∂W on which λ corresponds to etα, where α =λ|∂W . So we can
glue the semi-inﬁnite cylinder ([0 ,∞)×∂W to W and extend the Liouvllle form
by etα to obtain a ﬁnite type Liouville manifold which we call the completion of
(W,ω,X ). Conversely, the discussion above shows that every ﬁnite type Liouville
manifold is the completion of a Liouville domain.
We conclude this section with a brief discussion of holonomy in Liouville ma-
nifolds.
Lemma 11.4. Let Σ,~Σ be hypersurfaces in a Liouville manifold (V,ω,X ) such
that following trajectories of X deﬁnes a diﬀeomorphism Γ : Σ→ ~Σ. Then Γ is a
contactomorphism for the contact structures induced by iXω.
We call Γ the holonomy map from Σ to ~Σ.
Proof. Use the Liouville ﬂow to embed the symplectization R×Σ intoV such
that Σ corresponds to {0}× Σ, λ =erα and X =∂r, where α =λ|Σ and r is the
coordinate on R. Then ~Σ is given as the graph r = f(x) of a function f : Σ→ R
and Γ∗(λ|~Σ) =efα. □
11.2. Liouville homotopies
In this section we introduce the notion of a homotopy of Liouville domains
or manifolds. It has the important property (Proposition 11.8) that homotopic
Liouville manifolds are symplectomorphic.
A homotopy of Liouville cobordisms is simply a smooth family of Liouville
cobordisms (W,ωs,Xs), s∈ [0, 1]. However, the deﬁnition of a homotopy of Liou-
ville manifolds requires some care.
Definition 11.5. A smooth family (V,ωs,Xs),s∈ [0, 1], of Liouville manifolds
is called a simple Liouville homotopy if there exists a smooth family of exhaustions
V =⋃∞
k=1Vk
s by compact domainsVk
s ⊂V with smooth boundaries along whichXs
is outward pointing. A smooth family (V,ωs,Xs),s∈ [0, 1], of Liouville manifolds is
called a Liouville homotopy if it is a composition of ﬁnitely many simple homotopies.
See Figure 11.1 below illustrating a non-simple homotopy in the slightly more
special case of Weinstein manifolds.
Lemma 11.6. A smooth family (V,ωs,Xs), s∈ [0, 1], of Liouville manifolds
of ﬁnite type is a Liouville homotopy if the closure ⋃
t∈[0,1] Skel(V,ωs,Xs) of the
union of their skeletons is compact. In particular, the completions of a homotopy
of Liouville domains deﬁne a homotopy of Liouville manifolds.

240 11. WEINSTEIN STRUCTURES
Proof. The compactness condition implies that around each s∈ [0, 1] there
exists an open intervalIs and a compact setWs⊂V such that Skel(V,ωt,Xt)⊂Ws
andXt points out of∂Ws for allt∈ ¯Is. Finitely many such intervals cover [0, 1] and
on each ¯Is we have a simple homotopy with exhaustion Vk
s =Xk
s (Ws), k∈ N. □
The converse to Lemma 11.6 need not hold: For a homotopy of Liouville mani-
folds of ﬁnite type the closure of the union of their skeletons need not be compact.
We do not know, see the following example, whether the existence of a homo-
topy between the completions of two Liouville domains implies that the Liouville
domains themselves are homotopic.
Example 11.7. Let (V,ω,X ) be a 2 n-dimensional Liouville manifold of ﬁ-
nite type. Write V = W∪E, where ( W,ω,X ) is a Liouville domain and E =(
Σ× [0,∞),d (etα), ∂
∂t
)
a cylindrical end, and set W1 :=W∪ (Σ× [0, 1]). Suppose
that there exists a diﬀeomorphismf : Σ×[0, 1]→ Σ×[0, 1] withf(x,t ) = (x,t ) near
t = 0 and f(x,t ) = (g(x),t ) near t = 1 representing a non-trivial pseudo-isotopy
class, see Section 9.10. Let us extend f to the diﬀeomorphism ˆf : Σ× R→ Σ× R
which maps (x,t ) to (g(x),t ) fort≥ 1 and equals the identity on Σ×(−∞, 0]. Note
that ˆf is isotopic to the identity via the isotopy
ˆfs :=
{
τσ(s)◦ ˆf◦τ−σ(s) s∈ (0, 1],
Id s = 0,
where τc(x,t ) = (x,t +c) is the translation by c∈ R and σ : (0, 1]→ [0,∞) is a
decreasing diﬀeomorphism. Note that ˆf1 = ˆf and ˆfs = Id on Σ×(−∞, 0] for alls∈
[0, 1]. Denote by F :W1→W1 the diﬀeomorphism equal to Id on W andf on Σ×
[0, 1]. Similarly, we deﬁne ˆFs :V →V as equal to Id onW and ˆfs onE. Let (ˆωs :=
(ˆFs)∗ω, ˆXs := (ˆFs)∗X),s∈ [0, 1], be the push-forward Liouville manifold structure
onV , and (ω1 :=F∗ω,X 1 :=F∗X) be the push-forward Liouville domain structure
onW1. Note that (V,ˆω1, ˆX1) is the completion of (W1,ω 1,X 1). Then (V,ˆωs, ˆXs) is a
homotopy of Liouville manifolds connecting (V,ω,X ) with (V,ˆω1, ˆX1). On the other
hand, there is no obvious homotopy of Liouville domains connecting ( W1,ω,X )
and (W1,ω 1,X 1). It follows from Theorem 14.3 below that the Liouville domains
(W1,ω,X ) and (W1,ω 1,X 1) are nevertheless homotopic if n > 2. The answer is
unknown for n = 2.
Proposition 11.8. Let (V,ωs,Xs),s∈ [0, 1], be a homotopy of Liouville mani-
folds with Liouville forms λs. Then there exists a diﬀeotopy hs :V →V with h0 =
Id such that h∗
sλs−λ0 is exact for all s∈ [0, 1]. If moreover ⋃
s∈[0,1] Skel(V,ωs,Xs)
is compact (e.g. for the completion of a homotopy of Liouville domains), then we
can achieve h∗
sλs−λ0 = 0 outside a compact set.
Proof. It suﬃces to consider the case of a simple homotopy ( V,ωs,Xs). Pick
a family of exhaustions V = ⋃∞
k=1Vk
s as in Deﬁnition 11.5. Denote by Σ k
s the
boundary∂V k
s , byλs the Liouville form dual toXs, and byξk
s the contact structure
induced on Σk
s by the contact form λs|Σk
s
, s∈ [0, 1], k∈ N. By Gray’s Stability
Theorem 6.23 there are families of contactomorphisms
ψk
s : (Σk
0,ξk
0 )→ (Σk
s,ξk
s ),
so that (ψk
s )∗λs =efk
sλ0 for smooth families of functions fk
s : Σk
0→ R. (We denote
the restrictions of λs to the various hypersurfaces by the same symbol). For c∈ R

11.3. ZEROES OF LIOUVILLE FIELDS 241
set Σk,c
s :=Xc
s(Σk
s) and deﬁne the diﬀeomorphisms
ψk,c
s :=Xc
s◦ψk
s◦X−c
0 : Σk,c
0 → Σk,c
s .
By equation (11.1) we have (ψk,c
s )∗λs =efk
s◦X−c
0 λ0. For a sequence of real numbers
dk (which will be determined later) set
~Σk
s := Σk,dk
s , ~ψk
s :=ψk,dk
s , ~Vk
s :=Xdk
s (Vk
s ), ~fk
s :=fk
s◦X−dk
0 ◦ (~ψk
s )−1.
A short computation using equation (11.1) shows that the map Ψ k
s :=X− ~fk
s
s ◦~ψk
s :
~Σk
0 → V satisﬁes (Ψk
s)∗λs = λ0 and hence canonically extends to a map (still
denoted by the same symbol) Ψk
s :Op~Σk
0→O p (X− ~fk
s
s ~Σk
s), which maps trajectories
of X0 to trajectories of Xs and satisﬁes (Ψk
s)∗λs =λ0.
Now we choose the constants dk such that for each s∈ [0, 1] the hypersurfaces
~Σk
s, k ∈ N, are mutually disjoint and the hypersurfaces X− ~fk
s
s (~Σk
s), k ∈ N, are
mutually disjoint. We achieve the ﬁrst condition by choosing the dk nondecreasing.
The second condition holds if we have
minx∈~Σks
(
dk− ~fk
s (x)
)
≥ maxx∈~Σk−1
s
(
dk−1− ~fk−1
s (x)
)
for all s∈ [0, 1] and k≥ 2. So we can achieve both conditions by deﬁning the dk
inductively by d1 := 0 and
dk :=dk−1 + max
{
0, max
s,x
fk
s (x)− min
s,x
fk−1
s (x)
}
.
These conditions ensure that the Ψ k
s induce a diﬀeomorphism
Ψs :Op
(∞⋃
k=1
~Σk
0
)
→O p
(∞⋃
k=1
X− ~fk
s
s ~Σk
0
)
satisfying Ψ∗
sλs = λ0. Let us extend Ψ s in any way to a diﬀeomorphism Ψ s :
V →V . Now we apply Moser’s Stability Theorem 6.8 to each of the open domains
Int~Vk+1
0 \ ~Vk
0 and the family of exact symplectic forms Ψ ∗
sωs = d(Ψ∗
sλs) whose
primitives are s-independent near the boundary ~Σk+1
0 ∪~Σk
0. This yields a family
of diﬀeomorphisms φs : V → V which are the identity on Op
(⋃∞
k=1~Σk
0
)
and
such that the composition hs := Ψs◦φs is the required exact symplectomorphism
(V,ω 0,X 0)→ (V,ωs,Xs).
If K := ⋃
s∈[0,1] Skel(V,ωs,Xs) is compact we carry out an analogous proof
with only one set V 1 containingK. □
11.3. Zeroes of Liouville ﬁelds
Here we study some local properties of Liouville ﬁelds near zeroes. Recall from
Section 6.1 that a subspace W of a symplectic vector space ( V,ω ) (and similarly
for manifolds) is called isotropic resp. coisotropic if W ⊂ Wω resp. Wω ⊂ W ,
where Wω denotes the ω-orthogonal complement. Also recall from Section 9.2 the
deﬁnitions of the various invariant manifoldsW±
p ,... near a zero p of a vector ﬁeld
and their tangent spaces E±
p,... .
Proposition 11.9. Let (V,ω ) be a symplectic manifold with Liouville ﬁeld X,
and let p be a (possibly degenerate) zero of X. Then:
(a) The center-stable space E−
p ⊕E0
p⊂TpV is isotropic.

242 11. WEINSTEIN STRUCTURES
(b) The local stable manifold W−
p is isotropic.
(c) The local unstable manifold W +
p is coisotropic.
(d) If p is embryonic then the extended stable manifold ˆW−
p is isotropic.
In particular, dimW−
p ≤n and dimW +
p ≥n, where 2n = dimV .
Proof. Letφt :V →V be the ﬂow ofX. Recall that it expands the symplectic
form as well as the Liouville form λ =iXω, i.e., φ∗
tω =etω and φ∗
tλ =etλ.
(a) The linearization A := DpX : TpV → TpV preserves the splitting TpV =
E+
p ⊕E−
p ⊕E0
p from Lemma 9.9 (b) and its ﬂow expands the symplectic form,
etωp(v,w ) =ωp(etAv,etAw).
Forv,w ∈E−
p ⊕E0
p the right hand side is bounded for t≥ 0, so as t→∞ we ﬁnd
ωp(v,w ) = 0.
For (b-d) abbreviateW± =W±
p , soTpV =TpW +⊕TpW−⊕E0
p. All eigenvalues
of the linearization of X at p have negative real part on TpW− and positive real
part on TpW +. It follows that the diﬀerential Tpφt :TxV →Tφt(x)V satisﬁes
lim
t→∞
Txφt(v) = 0 for x∈W−,v∈TxW−,
lim
t→−∞
Txφt(v) = 0 for x∈W +,v∈TxW +.
(b) Let x ∈ W− and v ∈ TxW−. Since φt(x) → p as t → ∞, the preceding
discussion shows
etλx(v) = (φ∗
tλ)(v) =λφt(x)(Txφt·v)→ 0
as t→∞ . This implies λ(v) = 0, so λ and hence ω vanishes on W−.
(c) Let x∈ W + and v ∈ (TxW +)ω ⊂ TxV . Suppose v /∈ TxW +. Take a
sequence tk→−∞ and let xk :=φtk(x). Pick λk > 0 such that vk :=λkTxφtk·v
has norm 1 with respect to some metric on V . Note that vk∈ (TxkW +)ω for all
k. Pass to a subsequence so that vk→ v∞∈ TpV . Since Txφtk (as tk→−∞ )
exponentially contracts the component of v tangent to W + but not the transverse
component (this follows e.g. from the proof of the λ-lemma, see [ 157]), we ﬁnd
0⁄=v∞∈TpW−.
We claim that v∞∈ (TpW +)ω. Otherwise, there would exist a w∞∈ TpW +
with ω(v∞,w∞)⁄= 0. But then ω(vk,wk)⁄= 0 for k large and some wk∈TxkW +,
contradictingvk∈ (TxkW +)ω. Hence v∞ isω-orthogonal toTpW +. Since TpW−⊕
E0
p is isotropic by part (a), v∞ is also ω-orthogonal to TpW−⊕E0
p. But this
contradicts the nondegeneracy of ω because TpV =TpW +⊕TpW−⊕E0
p.
(d) Suppose now thatp is embryonic. The proof that ˆW−
p is isotropic is similar
to that of part (a). Let x∈ ˆW−, so φt(x)→ p as t→∞ . Since the eigenvalues
onTpˆW− =TpW−⊕E0
p have nonpositive real part, there exists a constant C such
that
|Txφt(v)|≤ Cet/2|v| for all v∈TxˆW−, t≥ 0.
It follows that
et|λx(v)| =|λφt(x)(Txφt·v)|≤ Cet/2|v|.
As t→∞ this implies λ(v) = 0, so λ and hence ω vanishes onˆW−. □

11.4. WEINSTEIN COBORDISMS AND MANIFOLDS 243
11.4. Weinstein cobordisms and manifolds
Definition 11.10. A Weinstein manifold (V,ω,X,φ ) is a symplectic manifold
(V,ω ) with a complete Liouville ﬁeld X which is gradient-like for an exhausting
Morse function φ : V → R. A Weinstein cobordism (W,ω,X,φ ) is a Liouville
cobordism (W,ω,X ) whose Liouville ﬁeld X is gradient-like for a Morse function
φ :W→ R which is constant on the boundary. In both cases the triple ( ω,X,φ ) is
called a Weinstein structure onV resp.W . A Weinstein cobordism with ∂−W = ∅
is called a Weinstein domain.
Thus any Weinstein manifold (V,ω,X,φ ) can be exhausted by Weinstein do-
mainsWk ={φ≤dk}, wheredk↗∞ is a sequence of regular values of the function
φ.
A Weinstein manifold ( V,ω,X,φ ) is said to be of ﬁnite type if φ has only
ﬁnitely many critical points. Note that by attaching a cylindrical end any Weinstein
domain (W,ω,X,φ ) can be completed to a ﬁnite type Weinstein manifold, called
its completion. Conversely, any ﬁnite type Weinstein manifold is the completion of
a Weinstein domain.
Remark 11.11. (i) Any Weinstein manifold (V,ω,X,φ ) has the structure of a
Liouville manifold (V,ω,X ). However, not every Liouville manifold is diﬀeomorphic
to a Weinstein manifold, see [ 133, 64].
(ii) Later on, in deformations of Weinstein structures we will also allow φ to
have embryonic (death-birth) singularities; in this section we restrict ourselves to
the Morse case.
Example 11.12. (1) Cn carries the canonical Weinstein structure
ωst =
n∑
j=1
dxj∧dyj, Xst = 1
2
n∑
j=1
(
xj
∂
∂xj
+yj
∂
∂yj
)
, φst = 1
4
n∑
j=1
(x2
j +y2
j ).
(2) An important example of a Weinstein structure is provided by the cotangent
bundle V =T∗Q of a closed manifold Q with the standard symplectic form ωst =
dλst, whereλst =pdq is the standard Liouville form. The associated Liouville ﬁeld
Xst =p ∂
∂p is gradient-like for the functionφst(q,p ) = 1
2|p|2. Since the functionφst is
not Morse, this does not yet deﬁne a Weinstein structure according to our deﬁnition
(although the deﬁnition could be without diﬃculty relaxed to allow for Morse-Bott
functions such asφst). To deﬁne a Weinstein structure, take any Riemannian metric
onQ and a Morse function f :Q→ R. Note that the Hamiltonian vector ﬁeld XF
of the function F (q,p ) := ⟨p,∇f(q)⟩ (or in more invariant notation F = λ(∇f))
coincides with ∇f along the zero section of T∗Q. Thus the vector ﬁeld X :=
p ∂
∂p +XF is Liouville and gradient-like for the Morse functionφ(q,p ) := 1
2|p|2+f(q)
if f is small enough.
(3) The product of two Weinstein manifolds (V1,ω 1,X 1,φ 1) and (V2,ω 2,X 2,φ 2)
has a canonical Weinstein structure ( V1×V2,ω 1⊕ω2,X 1⊕X2,φ 1⊕φ2). In par-
ticular, the product (V,ω,X,φ )× (R2,ω st,X st,φ st) is called the stabilization of the
Weinstein manifold (V,ω,X,φ ).
Note that in a Weinstein manifold (V,ω,X,φ ) any regular level set Σ :=φ−1(c)
carries a canonical contact structureξ deﬁned by the contact formα := (iXω)|Σ. In
particular, this applies to the boundary of a Weinstein domain. Contact manifolds

244 11. WEINSTEIN STRUCTURES
which appear as boundaries of Weinstein domains are called Weinstein ﬁllable. We
will see later (Theorem 13.5) that this is equivalent to being Stein ﬁllable .
Lemma 11.13. Let (V,ω,X,φ ) be a Weinstein manifold.
(a) The stable manifold W−
p of any critical pointp∈V ofφ satisﬁesλ|W−
p
≡ 0.
In particular, W−
p is isotropic for the symplectic structure ω, and the intersection
W−
p ∩φ−1(c) with any regular level set is isotropic for the contact structure induced
by λ on φ−1(c).
(b) Suppose φ has no critical values in [a,b ]. Then the image of any isotropic
submanifold Λa ⊂ φ−1(a) under the ﬂow of X intersects φ−1(b) in an isotropic
submanifold Λb.
Proof. (a) SinceX is tangent toW−
p andW−
p is isotropic by Proposition 11.9,
the Liouville formλ =iXω vanishes onW−
p . Part (b) is an immediate consequence
of Lemma 11.4. □
In view of Lemma 9.9, every zero p of the Liouville ﬁeld X in a Weinstein
manifold (V,ω,X,φ ) is hyperbolic. Thus the skeleton of ( V,ω,X ) is the union
of all stable manifolds, which are isotropic by Proposition 11.9. Under suitable
technical assumptions (X Morse-Smale and (X,φ ) standard near critical points),
the skeleton is in fact an isotropic embedded CW complex [ 17]. We will not use
this fact, but rather the following interpretation of Lemma 11.13:
An exhaustion of a Weinstein manifold ( V,ω,X,φ ) by regular sublevel sets
{φ≤ dk} such that each interval ( dk−1,dk) contains at most one critical value
provides a handlebody decomposition of V whose core discs (the stable discs of
critical points) are isotropic in the symplectic sense, and whose attaching spheres
are isotropic in the contact sense.
11.5. From Stein to Weinstein
Until this point, by a Stein manifold we meant a complex manifold (V,J ) which
admits an exhausting J-convex function φ :V → R. From now on, we will change
our perspective and consider the function φ as part of the data. Moreover, we will
require the function φ to be Morse, which can always be achieved by a C2-small
perturbation. The following analogue of Deﬁnition 11.10 in the Stein case will be
relevant for the remainder of this book.
Definition 11.14. A Stein manifold (V,J,φ ) is a complex manifold (V,J ) with
an exhausting J-convex Morse function φ :V → R. A Stein cobordism (W,J,φ ) is
a complex cobordism ( W,J ) with a J-convex Morse function φ : W → R having
∂±W as regular level sets. In both cases the triple ( J,φ ) is called a Stein structure
on V resp. W . A Stein cobordism with ∂−W = ∅ is called a Stein domain.
Next recall that a J-convex function φ is called completely exhausting if it is
exhausting and its gradient ﬁeld ∇φφ is complete.
Definition 11.15. To every Stein cobordism (W,J,φ ) we associate the Wein-
stein cobordism structure
W(J,φ ) := (ωφ,Xφ,φ ) := (−ddCφ,∇φφ,φ ).
on W . The same formula also associates a Weinstein manifold structure on V to
every Stein manifold (V,J,φ ) with φ a completely exhausting Morse function.

11.6. WEINSTEIN AND STEIN HOMOTOPIES 245
By Lemma 2.20, W(J,φ ) deﬁnes indeed a Weinstein structure. Note that the
contact structureξ induced on a regular level set Σ = φ−1(c) by the Liouville form
−dφC coincides with the ﬁeld of complex tangencies on the J-convex hypersurface
Σ.
Remark 11.16. The completeness condition in Deﬁnition 11.15 is necessary
because we require the Liouville ﬁeld to be complete in our deﬁnition of a Weinstein
manifold. According to Proposition 2.11, any exhausting J-convex function can be
made completely exhausting by composing it with a suﬃciently convex function
R→ R. Subsequently, whenever we speak of the Weinstein manifold structure
W(J,φ ) associated to a Stein manifold we will implicitly assume thatφ is completely
exhausting without further mentioning it .
Remark 11.17. Let (V,J,φ ) be an almost complex manifold with an exhausting
J-convex Morse functionφ :V → R. Then even if the symplectic formωφ =−ddCφ
is not compatible with J, one still gets a Weinstein structure ( ωφ,Xφ,φ ) on V
similar to the one deﬁned above. The only diﬀerence in this case is that the Liouville
ﬁeld Xφ should be deﬁned directly as ωφ-dual to−dCφ, i.e., by
−dCφ =iXφωφ.
Applying both sides to a tangent vector JZ we ﬁnd
dφ(Z) =ωφ(Xφ,JZ ),
soXφ is gradient-like forφ with respect to the positive deﬁnite (but in general non-
symmetric) (2, 0) tensor ﬁeld gφ :=ωφ(·,J·). Completeness of Xφ can be achieved
as in the integrable case by composing φ with a suﬃciently convex function.
Combined with Proposition 11.9, this yields another proof of the fact (Corol-
lary 3.4) that the indices of critical points of a J-convex Morse function on a
2n-dimensional almost complex manifold are ≤n.
Example 11.18. Not every Weinstein structure equals W(J,φ ) for some Stein
structure (J,φ ). Indeed, this fails already in a neighborhood of a critical point
p: The linearization DpX : TpV → TpV of the Liouville ﬁeld is diagonalizable if
X =∇φφ for aJ-convex functionφ, while for a general Weinstein structure it need
not be. For example, consider for ε∈ R the Liouville 1-form
λ = 1
2(xdy−ydx ) +ε(xdx +ydy )
on C satisfying dλ =dx∧dy. The corresponding Liouville ﬁeld
X = 1
2(x∂x +y∂y) +ε(y∂x−x∂y)
has eigenvalues 1/2±iε, so it is induced by a Stein structure if and only if ε = 0.
A quadratic Lyapunov function for X is e.g. given by x2 +y2.
11.6. Weinstein and Stein homotopies
Now we deﬁne Weinstein and Stein homotopies. They have the important
property that homotopic Weinstein manifolds are symplectomorphic. Moreover, we
prove that the Stein structures corresponding to two exhaustingJ-convex functions
on the same complex manifold are homotopic.

246 11. WEINSTEIN STRUCTURES
Definition 11.19. A Weinstein homotopy on a cobordism or manifold is a
smooth family of Weinstein structures (ωt,Xt,φt), t∈ [0, 1], where we allow birth-
death type degenerations, such that the associated Liouville structures ( ωt,Xt)
form a Liouville homotopy. A Stein homotopy is a smooth family of Stein structures
(Jt,φt), where we allow birth-death type degenerations, such that the associated
Weinstein structures W(Jt,φt) form a Weinstein homotopy.
Since this deﬁnition is basic for all that follows, let us recall its main fea-
tures. We begin with the case of a cobordism W . Then a Weinstein homotopy
(W,ωt,Xt,φt) induces a Smale homotopy ( W,Xt,φt) in the sense of Section 9.7.
This means that the functions φt have ∂±W as regular level sets, and they are
Morse except for ﬁnitely many t∈ (0, 1) at which a birth-death type critical point
occurs. Note again the slight abuse of language because ( ωt,Xt,φt) is not a Wein-
stein structure for such t.
In the case of a manifold V the conditions on the boundary are replaced by the
existence of a smooth family of exhaustions as in Deﬁnition 11.5 which prevents
critical points from escaping to inﬁnity. Using the functions φt, this condition can
be equivalently formulated as follows. Let φt : V → R, t∈ [0, 1], be a smooth
family of exhausting functions on a manifold V having only Morse or birth-death
type critical points. We call φt a simple Morse homotopy if there exists a sequence
of smooth functions c1 <c 2 <··· on the interval [0, 1] such that for each t∈ [0, 1],
ci(t) is a regular value of the function φt and ⋃
k{φt ≤ ck(t)} = V . A Morse
homotopy is a composition of ﬁnitely many simple Morse homotopies. A Smale
homotopy is a smooth family of Lyapunov pairs ( Xt,φt) such that the associated
functions φt form a Morse homotopy. Then a Weinstein homotopy is a family of
Weinstein structures (V,ωt,Xt,φt) (again allowing birth-death type degenerations)
such that the associated Lyapunov pairs (Xt,φt) form a Smale homotopy.
For Stein/Weinstein/Smale/Morse homotopies we will always use such exhaus-
tions by sublevel sets{φt≤ck(t)}. Figure 11.1 shows the proﬁle for a composition
of two simple Morse homotopies which is not simple: the sublevel sets {φ≤ ci}
resp.{φ≤ c′
i} provide exhaustions for the restrictions of the homotopy to the in-
tervals [0, 1/2] and [1/2, 1], while no such exhaustion exists over the whole interval
[0, 1].
Example 11.20. Consider an exhausting Morse function φ with gradient-like
vector ﬁeld X on a manifold V and a diﬀeotopy ht : V → V , t∈ [0, 1]. Then
(V,h∗
tX,h∗
tφ) is a simple Smale homotopy. Indeed, in the deﬁnition we just take
the constant functions c1 < c2 <··· on the interval [0, 1] for a sequence ck→∞
of regular values of φ.
Since a Weinstein homotopy (ωt,Xt,φt) induces a Liouville homotopy (ωt,Xt),
Proposition 11.8 implies
Corollary 11.21. If two Weinstein manifolds W0 = (V,ω 0,X 0,φ 0) and W1 =
(V,ω 1,X 1,φ 1) are Weinstein homotopic they are symplectomorphic. More precisely,
there exists a diﬀeotopyht :V →V withh0 = Id such thath∗
1λ1−λ0 is exact, where
λi =iXiωi are the Liouville forms. If W0 and W1 are the completions of homotopic
Weinstein domains, then we can achieve h∗
1λ1−λ0 = 0 outside a compact set.
The following proposition shows that the existence of a Stein homotopy con-
necting two Stein structures (J0,φ 0) and (J1,φ 1) depends only on the Stein complex

11.6. WEINSTEIN AND STEIN HOMOTOPIES 247
c1
c2
c3
c4
c5
c′
1
c′
2
c′
3
c′
4
t
11
2
Figure 11.1. A composition of two simple homotopies which is
not simple.
structures J0, J1 and not on the functions φ0, φ1. Moreover, the symplectic ma-
nifold (V,ωφ) associated to a Stein manifold ( V,J,φ ) is independent, up to exact
symplectomorphism isotopic to the identity, of the choice of a completely exhausting
J-convex Morse function φ.
Proposition 11.22 (see [49]). Letφ0,φ 1 :V → R be two exhausting J-convex
Morse functions on a complex manifold (V,J ). Then (J,φ 0) and (J,φ 1) can be con-
nected by a Stein homotopy (J,φt). In particular, if φ0,φ 1 are completely exhausting
Morse functions, then the corresponding Weinstein structures (ωφ0,Xφ0,φ 0) and
(ωφ1,Xφ1,φ 1) are Weinstein homotopic.
The proof of Proposition 11.22 is based on the following
Lemma 11.23. Let φ0,φ 1 :V → R be two exhausting J-convex functions on a
complex manifold (V,J ). Then there exist smooth functions h0,h 1 : R→ R with
h′
0,h′
1→∞ and h′′
0,h′′
1≥ 0, a completely exhausting J-convex function ψ : V →
R+, and a sequence of compact domains Vk, k = 1,..., with smooth boundaries
Σk =∂V k, such that
• Vk⊂ IntVk+1 for all k≥ 1 and⋃
kVk =V ;
• Σ2j−1 are level sets of the function φ1 and Σ2j are level sets of the func-
tion φ0 for all j≥ 1;
• ψ =h1◦φ1 onOp
(⋃∞
j=1 Σ2j−1
)
and ψ =h0◦φ0 onOp
(⋃∞
j=1 Σ2j
)
.
Proof. Let us call a diﬀeomorphism h : R→ R an admissible function if
h′′≥ 0 and h′→∞ . Take any c1 > 0 and deﬁne V 1 :={φ1≤ c1}, Σ 1 := ∂V 1.
There exists an admissible functiong1 such thatφ0|Σ1 <d 1 =g1(c1). Set ψ0 :=φ0,
ψ1 := g1◦φ1. Next, take any c2 > d1 and deﬁne V 2 :={ψ0≤ c2}, Σ 2 := ∂V 2.
Then V 1⊂ IntV 2. There exists an admissible function g2 such that g2(x) =x for
x≤ d1 and ψ1|Σ2 < d2 = g2(c2). Set ψ2 := g2◦ψ0. Continuing this process, we
take c3 > d2 and deﬁne V 3 :={ψ1≤ c3}, Σ3 := ∂V 3. There exists an admissible
function g3 such that g3(x) = x for x≤ d2 and ψ2|Σ3 < d3 = g3(c3). Set ψ3 :=
g3◦ψ1, and so on. Continuing this process, we construct compact domains Vk with
smooth boundaries ∂V k = Σk, k≥ 1, and two sequences of admissible functions
~g2j :=g2j◦g2j−2◦···◦ g2,~g2j−1 :=g2j−1◦g2j−3◦···◦ g1. Since these sequences

248 11. WEINSTEIN STRUCTURES
stabilize on compact sets, they converge to admissible functions h0 := limj→∞~g2j
and h1 := limj→∞~g2j−1. It follows that the sequences of functions ψ2j =~g2j◦φ0
andψ2j−1 =~g2j−1◦φ1 converge asj→∞ to exhausting J-convex functionsψeven
and ψodd on V . By construction, they have the following properties:
• Vk⊂ IntVk+1 for all k≥ 1 and⋃
kVk =V ;
• φ1 is constant on Σ 2j−1 and φ0 is constant on Σ 2j for all j≥ 1;
• ψeven =h0◦φ0 and ψodd =h1◦φ1;
• ψodd|Σ2j−1 >ψ even|Σ2j−1 and ψeven|Σ2j >ψ odd|Σ2j for all j≥ 1.
Smoothing the continuous J-convex function max (ψeven,ψ odd) thus yields the re-
quired smooth J-convex function ψ. □
Proof of Proposition 11.22. Leth0,h 1 andψ be the functions constructed
in Lemma 11.23. Now the required Stein homotopy is constructed as a composition
of four elementary homotopies. First, note that for any function h : R+→ R+
with h′ > 0 and h′′ ≥ 0 the linear combination hs(x) = (1 −s)x +sh(x) has
the same properties for any s∈ [0, 1]. Hence the exhausting J-convex functions
hs
i◦φi provide elementary Stein homotopies (J,hs
i◦φi) between the Stein structures
(J,φi) and (J,hi◦φi), i = 0, 1. On the other hand, for each i = 0, 1 the family
φt
i = (1−t)hi◦φi +tψ, t∈ [0, 1], consists of exhausting J-convex functions which
concide near the boundaries of an exhausting sequence of compact domains. Hence
they generate elementary Stein homotopies ( J,φt
i) between (J,hi◦φi) and (J,ψ ).
Concatenating these four elementary homotopies yields the desired Stein homotopy
(J,φt).
Now suppose φ0 andφ1 are completely exhausting Morse functions. In view of
Proposition 2.11 (by choosing thehi suﬃciently convex) we can achieve that all the
functions φt, t∈ [0, 1], are completely exhausting. Moreover, we can perturb φt to
a generic 1-parameter family of functions. Then (ωφt,Xφt,φt) provides a Weinstein
homotopy between the Weinstein structures (ωφ0,Xφ0,φ 0) and (ωφ1,Xφ1,φ 1). This
concludes the proof of Proposition 11.22. □
Remark 11.24. Without the hypothesis on the functions ck(t) the notion of
“Stein or Weinstein homotopy” would become rather trivial. For example, then all
Stein structures on Cn would be “homotopic”.
To see this, consider any Stein structure (J,φ ) on Cn. After a Stein homotopy,
we may assume that (J,φ ) agrees with the standard structure ( Jst =i,φ st =|z|2)
on the open unit ball B1. Pick a smooth family of radial diﬀeomorphisms ht :
Cn→ Cn,t∈ [0, 1), such thath0 = Id andht converges ast→ 1 inC∞
loc to a radial
diﬀeomorphism h1 : Cn→ B1. Pick a smooth family of convex diﬀeomorphisms
gt : R→ R,t∈ [0, 1), such thatg0 = Id andgt converges inC∞
loc on (−∞, 1) ast→ 1
to a convex diﬀeomorphism g1 : (−∞, 1)→ R. Then ( Jt,φt) := (h∗
tJ,gt◦φ◦ht)
would be a “Stein homotopy” from ( J,φ ) to a Stein structure ( J1,φ 1) which can
be connected to the standard structure by another radial homotopy.
Since there exist Stein structures ( J,φ ) on Cn for which ωφ is not symplec-
tomorphic to the standard symplectic structure (see Chapter 17 below), this also
shows that Corollary 11.21 would fail for this notion of “Weinstein homotopy”.
Remark 11.25. The proof of Proposition 11.22 (simply ignoring J-convexity)
also shows that any two exhausting Morse functions on the same manifold can be
connected by a Morse homotopy. Let us emphasize, however, that two exhausting
Morse functions of ﬁnite type cannot in general be connected by a Morse homotopy

11.7. WEINSTEIN STRUCTURES WITH UNIQUE CRITICAL POINTS 249
during which all critical points remain in a ﬁxed compact set. For example, let
M0,M 1 be two closed 4-manifolds that are homeomorphic but not diﬀeomorphic.
Then the 5-manifolds M0× R and M1× R are diﬀeomorphic, so the functions
Mi× R→ R, (x,t )↦→ t2, can be perturbed to two ﬁnite type exhausting Morse
functions φ0,φ 1 on the same 5-manifold. Since high level sets of φ0 andφ1 are not
diﬀeomorphic, the functions φ0 andφ1 cannot be connected by a Morse homotopy
with critical points remaining in a compact set.
The notion of Weinstein (or Stein) homotopy can be formulated in more topo-
logical terms. Let us denote by Weinstein the space of Weinstein structures on a
ﬁxed manifold V , where we allow the functions to have embryonic critical points.
For any W0 ∈ Weinstein, ε > 0, A⊂ V compact, k∈ N, and any unbounded
sequence c1 <c 2 <··· we deﬁne the set
U(W0,ε,A,k,c ) :={W = (ω,X,φ )∈ Weinstein| ‖W− W0‖Ck(A) <ε,
ci regular values of φ}.
It is easy to see that these sets are the basis of a topology on Weinstein. Note that
this topology is coarser that the C∞
loc topology, which we obtain by dropping the
condition on the regular values ci.
A smooth family of Weinstein structures Wt = (ωt,Xt,φt) deﬁnes a continuous
path [0, 1]→ Weinstein with respect to this topology if and only if there exists a
partition 0 = t0 < t1 <··· < tN = 1 and unbounded sequences ck
1 < ck
2 <··· ,
k = 1,...,N , such that ck
i is a regular value of φt for all t∈ [tk−1,tk]. Hence
Wt is a Weinstein homotopy according to our deﬁnition. Conversely, suppose that
Wt is a Weinstein homotopy. Then there exists a partition 0 = t0 < t1 <··· <
tN = 1 and unbounded sequences of smooth functions ck
1(t) < ck
2(t) <··· , t∈
[tk−1,tk], k = 1,...,N , such that ck
i (t) is a regular value of φt for all t∈ [tk−1,tk].
After a C∞-small perturbation, we may assume that ck
i (tk)⁄=ck+1
j (tk) for all i,j .
This allows us to pick a smooth family of diﬀeomorphisms gt : R→ R such that
g0 = Id and gt
(
ck
i (t)
)
is constant in t∈ [tk−1,tk] for all i∈ N and k = 1,...,N .
Then (ωt,Xt,gt◦φt) deﬁnes a continuous path [0 , 1]→ Weinstein. Hence, up to
target reparametrization φt↦→gt◦φt, continuous paths in Weinstein correspond to
Weinstein homotopies.
In view of the preceding discussion, we call a smooth k-parametric family of
Weinstein structures Wu = (ωu,Xu,φu),u∈Dk, a Weinstein family if there exists
a smooth family of diﬀeomorphisms gu : R→ R such that (ωu,Xu,gu◦φu) deﬁnes
a continuous path Dk→ Weinstein.
The preceding discussion carries over to Stein structures with one minor modi-
ﬁcation: We require the target reparametrizations gu : R→ R to be weakly convex
to ensure thatgu◦φu remainsJ-convex. This can always be achieved by composing
any family gu with a suﬃciently convex single function f : R→ R.
11.7. Weinstein structures with unique critical points
In this section we discuss Weinstein and Stein structures with a unique critical
point.
Proposition 11.26. Let (V,J,φ ) be a Stein manifold such that φ has a unique
critical point, the minimum. Then there exists a diﬀeomorphism h : Cn→V such
that the Stein structure (Cn,h∗J,h∗φ) is Stein homotopic to the standard structure

250 11. WEINSTEIN STRUCTURES
on Cn. Similarly, given a Stein domain (W,J,φ ) such that φ has a unique critical
point, there exists a diﬀeomorphism h : B2n→ V , where B2n is the closed unit
ball in Cn, such that the Stein structure (B2n,h∗J,h∗φ) is Stein homotopic to the
standard structure on B2n. Analogous results hold for Weinstein structures.
Proof. We consider ﬁrst the Stein manifold case. Assuming that the critical
value ofφ is 0, we ﬁrst modify φ near the critical point so that h∗
εφ =φst =|z|2 for
some biholomorphic map hε from the open ε-ball Bε⊂ Cn onto a neighborhood
of the minimum. Using gradient-like vector ﬁelds for φ and φst, we extend hε to a
diﬀeomorphism h : Cn→V with h∗φ =φst. Deﬁne ~J :=h∗J, so ~J|Bε =i. Pick a
smooth family of maps ft : R+→ R+, t∈ [0, 1], with the following properties:
• f0 = Id, and ft = Id near 0 for all t∈ [0, 1];
• ft deﬁnes a diﬀeomorphism R+→ [0,ε/t ) for t∈ (0, 1];
Then the smooth family of maps gt : Cn→ Cn, gt(z) :=ft(|z|) z
|z| satisﬁes
• g0 = Id, and gt = Id near z = 0 for all t∈ [0, 1];
• gt deﬁnes a diﬀeomorphism Cn→Bε/t for t∈ (0, 1].
Since φst◦gt(z) =ft(|z|)2 is g∗
t ~J-convex, the function φst is g∗
t ~J-lc for all t∈ [0, 1]
Hence (after a target reparametrization which we suppress) we can connect (~J,φ st)
on Cn by the Stein homotopy (g∗
t ~J,φ st) to (g∗
1J =g∗
1i,φ st). Since φst is also g∗
ti-lc,
the Stein homotopy (g∗
ti,φ st) on Cn connects (g∗
1i,φ st) with the standard structure
(i,φ st).
The case of a Weinstein manifold is analogous. In the case of a Stein or Wein-
stein domain, we only need to replace Cn and Bε by the closed balls B2n and
¯Bε. □
Corollary 11.27. Every Stein (resp. Weinstein) structure on Cn with a
unique critical point is Stein (resp. Weinstein) homotopic to the standard struc-
ture on Cn. An analogous statement holds for Stein (resp. Weinstein) structures
on the closed ball B2n provided that n> 2.
Proof. Any orientation preserving diﬀeomorphism h : Cn→ Cn is diﬀeotopic
to the identity via the Alexander trick
ht(z) :=
{
1
th(tz) t∈ (0, 1],
z t = 0
after adjusting h to equal the identity near 0. Hence the claim for Cn follows from
Proposition 11.26 and Example 11.20.
For the case of the closed ball and n >2 the claim follows from Cerf’s theo-
rem [30] that the group Diﬀ +(B2n) of orientation preserving diﬀeomorphisms of
B2n is connected for n> 2. □
Remark 11.28. Nothing, however, is known about the topology of Diﬀ +(B4).
We will encounter this phenomenon again in Chapter 16.
11.8. Subcritical and ﬂexible Weinstein structures
A 2n-dimensional Weinstein cobordism or manifold ( W,ω,X,φ ) is called sub-
critical if all critical points of the function φ have index<n . Similarly, one deﬁnes
subcritical Stein cobordisms and manifolds. Clearly, the stabilization (see Sec-
tion 11.4 above) of any Weinstein manifold is subcritical. The converse is also true

11.8. SUBCRITICAL AND FLEXIBLE WEINSTEIN STRUCTURES 251
due to the following theorem from [ 33] which we will prove in Section 14.4: Every
subcritical Weinstein manifold is symplectomorphic to a stabilization.
In Section 7.7 we introduced a class of loose Legendrian links in contact ma-
nifolds of dimension ≥ 5. In the 3-dimensional case a Legendrian link is called
loose if its complement is overtwisted. Recall from Sections 7.6 and 7.7 that loose
Legendrian links satisfy an h-principle. The following deﬁnition was motivated by
a talk of E. Giroux at ETH Z¨ urich on November 9, 2010.
Definition 11.29. An elementary 2n-dimensional Weinstein cobordism (W,ω,
X,φ ) is called ﬂexible if the attaching spheres of all indexn handles form in∂−W a
loose Legendrian link. A Weinstein cobordism or manifold structure (W,ω,X,φ ) is
called ﬂexible if it can be decomposed into elementary ﬂexible cobordisms. A Stein
structure is called ﬂexible if the underlying Weinstein structure is ﬂexible.
Remark 11.30. (1) In particular, any subcritical Weinstein cobordism is ﬂex-
ible.
(2) Note that a 4-dimensional Weinstein cobordism can only be ﬂexible if it
is subcritical, or if the contact structure on ∂−W is overtwisted. In particular, a
4-dimensional Weinstein manifold is ﬂexible if and only if it is subcritical .
(3) The property of a Weinstein structure being subcritical is clearly not pre-
served under Weinstein homotopies because one can always create index n critical
points. We do not know whether ﬂexibility is preserved under Weinstein homo-
topies. In fact, it is not even clear to us whether every decomposition of a ﬂexible
Weinstein cobordismW into elementary cobordisms consists of ﬂexible elementary
cobordisms. Indeed, if P1 andP2 are two partitions of W into elementary cobor-
disms and P2 is ﬁner than P1, then ﬂexibility of P1 implies ﬂexibility of P2 (in
particular the partition for which each elementary cobordism contains only one
critical value is then ﬂexible), but we do not know whether ﬂexibility of P2 implies
ﬂexibility ofP1.
We will see in Chapter 14 that, as the name suggests, ﬂexible Weinstein mani-
folds indeed exhibit a lot of ﬂexibility. In particular, we will prove:
Two ﬂexible Weinstein structures on the same manifold whose symplectic forms
are homotopic as nondegenerate 2-forms are Weinstein homotopic (Theorem 14.5).
Every diﬀeomorphism f : V1→ V2 between two ﬂexible Weinstein manifolds
(Vi,ωi,Xi,φi),i = 1, 2, such thatf∗ω2 is homotopic toω1 as nondegenerate 2-forms
is diﬀeotopic to a symplectomorphism (Theorem 14.7).



12
Modiﬁcations of Weinstein Structures
In this chapter we carry over various constructions for Morse cobordisms in
Chapter 9 to Weinstein cobordisms. In particular, we discuss holonomy of Weinstein
cobordisms (Section 12.2), modiﬁcations of Weinstein structures near critical points
(Section 12.4) and stable discs, and equivalence of elementary Weinstein homotopies
(Section 12.7). In Section 12.6 we prove the (easier) Weinstein analogues of the
modiﬁcations of Stein structures in Chapter 10.
12.1. Weinstein structures with given functions
Given a Weinstein (manifold or cobordism) structure W = (ω,X,φ ) with Liou-
ville formλ =iXω, we denote byC(W) the space of all Weinstein structures on the
same manifold with the same function φ and with Liouville form
(12.1) ~λ =fλ +gdφ
for smooth functions f,g :W→ R with f >0.
Note that all Weinstein structures ~W∈C (W) induce the same contact struc-
tures on all level sets of φ. Conversely, if this is the case then the Liouville form ~λ
has the form (12.1) outside the critical points .
Let us ﬁrst ﬁnd the conditions onf,g under which the 1-form~λ deﬁned by (12.1)
deﬁnes again a Weinstein structure with function φ.
Lemma 12.1. Let (W,ω,X,φ ) be a Weinstein cobordism with Liouville form λ.
Then for functions f,g :W→ R the following holds.
(i) The 1-form fλ deﬁnes a Weinstein structure if and only if f > 0 and
k := f +df(X) > 0; in that case, it has Lyapunov function φ and Liouville ﬁeld
f
kX.
(ii) The 1-form λ +gdφ deﬁnes a Weinstein structure if and only if k :=
1−dg(Xφ)> 0, where Xφ is the Hamiltonian vector ﬁeld of φ; in that case, it has
Lyapunov function φ and Liouville ﬁeld 1
kX− g
kXφ +Z with dφ(Z) =λ(Z) = 0.
Remark 12.2. (a) Lemma 12.1 remains true for Weinstein manifolds instead
of cobordisms if one additionally requires that the new Liouville ﬁeld is complete.
Note that this is automatic in the special case df(X)≥ 0 in (i), and it is implied
by completeness of the vector ﬁeld 1
kX in (ii).
(b) The proof of Lemma 12.1 shows that the Liouville ﬁelds of λ and ~λ are
proportional if and only if g is constant on level sets of φ.
253

254 12. MODIFICATIONS OF WEINSTEIN STRUCTURES
Proof. Recall that the Liouville ﬁeld X and the Hamiltonian vector ﬁeld Xφ
satisfy
iXω =λ, i Xφω =−dφ, dφ (Xφ) =λ(X) = 0,
dφ(X) =λ(Xφ) =:h.(12.2)
Note that we have Xφ = hR, where R is the Reeb vector ﬁeld of the form λ
restricted to the level sets of φ, i.e., iRω|{φ=const} = 0, dφ(R) = 0 and λ(R) = 1.
Consider a 1-form
~λ =fλ +gdφ
as in (12.1). Let us derive the conditions for the form
~ω =d~λ =fω +df∧λ +dg∧dφ
to be symplectic. First note that at a critical point p of φ the form equals ~ωp =
f(p)ω, so ~ω is symplectic near p if and only if f(p)> 0. Hence, in the rest of the
proof we will assume f >0 and work in the complement of the critical locus of φ.
Consider any vector ﬁeld Y and write it in the form
Y =aXφ +bX +Z, Z ∈ξ,
whereξ = kerdφ∩ kerλ is the contact structure on level sets of φ. A short compu-
tation using the relations (12.2) yields
β :=iY~ω
=a
[
df(Xφ)λ−hdf−fdφ +dg(Xφ)dφ
]
+b
[
df(X)λ−hdg +fλ +dg(X)dφ
]
+
[
df(Z)λ +fi Zω +dg(Z)dφ
]
.
ThusY ∈ ker~ω is equivalent to the three equations
β|ξ = (fi Zω−ahdf−bhdg )|ξ = 0,
β(Xφ)/h =bk +df(Z) = 0,
β(X)/h =−ak +dg(Z) = 0,
where we have set k :=f +df(X)−dg(Xφ). For k> 0 one easily sees that in both
cases (i) and (ii) these equations imply Y = 0, so ~ω is symplectic. The necessity of
the conditions f >0 and k> 0 follows in case (i) from the nonvanishing of
iX(~ωn) =nf n−1(
f +df(X)
)
λ∧ωn−1,
and in case (ii) from the nonvanishing of
iXφ(~ωn) =−n
(
1−dg(Xφ)
)
dφ∧ωn−1.
Finally, we compute the Liouville ﬁeld of ~λ. We again write it in the form ~X =
aXφ +bX +Z with Z∈ξ. Then the equation i ~X~ω =~λ is equivalent to the three
equations
β|ξ = (fi Zω−ahdf−bhdg )|ξ = 0,
β(Xφ)/h =bk +df(Z) =f,
β(X)/h =−ak +dg(Z) =g.

12.1. WEINSTEIN STRUCTURES WITH GIVEN FUNCTIONS 255
In both cases (i) and (ii) these equations imply df(Z) =dg(Z) = 0 (actually Z = 0
in case (i)) and we conclude
~X = f
kX− g
kXφ +Z, (fki Zω +ghdf−fhdg )|ξ = 0.
In particular, we see that dφ(~X) =fdφ (X)/k, so ~X is gradient-like for φ. □
Corollary 12.3. Let W = (W,ω,X,φ ) be a Weinstein cobordism with Liou-
ville form λ. Then the space C(W) of Weinstein structures (W,ω,X,φ ) with Liou-
ville forms λ =fλ +gdφ , f >0, has the following properties.
(i) If λ and fλ belong toC(W), then so does (1−t +tf)λ for all t∈ [0, 1].
(ii) If λ and λ +gdφ belong to C(W), then so does λ +ρ◦φgdφ for each
function ρ : R→ [0, 1].
(iii) The space C(W) is weakly contractible, and so is its subspace of 1-forms
that equal λ near∂−W and a positive constant multiple of λ near∂+W .
Proof. (i) By Lemma 12.1 (i), the 1-forms λ and fλ both belong to C(W) if
and only if f +df(X)> 0, where X is the Liouville ﬁeld of λ. Then 1 −t +tf +
tdf(X)> 0 for all t∈ [0, 1], so (1−t +tf)λ belongs toC(W).
(ii) By Lemma 12.1 (ii), the 1-forms λ andλ+gdφ both belong toC(W) if and
only if dg(Xφ)< 1, where Xφ is the Hamiltonian vector ﬁeld of φ with respect to
dλ. Since d(ρ◦φ)(Xφ) = 0, this implies d(ρ◦φg )(Xφ) = ρ◦φdg (Xφ)< 1 for all
ρ : R→ [0, 1], so λ +ρ◦φgdφ belongs toC(W).
(iii) The proof of weak contractibility is based on the following observation. If
(λ,φ ) is a Liouville structure on a 2 n-dimensional cobordism then
(12.3) dφ∧λ∧ (dλ)n−1 > 0.
To see this, evaluate this 2 n-form at a point on the basis ( X,Xφ,Z 1,...,Z 2n−2),
whereX is the Liouville ﬁeld of λ,Xφ is the Hamiltonian vector ﬁeld with respect
todλ, andZ1,...,Z 2n−2 is a symplectic basis of kerdφ∩kerλ. Conversely, if (λ,φ )
satisﬁes (12.3) then (eρ◦φλ,φ ) is a Liouville structure for each suﬃciently increasing
function ρ : R→ R. For this, set ~λ :=eρ◦φλ and note that
(d~λ)n =enρ◦φ(
dλn +nρ′◦φdφ∧λ∧ (dλ)n−1)
> 0
for ρ′ > 0 suﬃciently large. Finally, we observe that if ( λ,φ ) satisﬁes (12.3) then
so does ~λ = fλ + gdφ for all functions f,g : W → R with f > 0. Indeed,
d~λ =fdλ +df∧λ +dg∧dφ implies
dφ∧~λ∧ (d∧λ)n−1 =fndφ∧λ∧ (dλ)n−1 > 0.
The last observation shows that the space ~C(W) of 1-forms λ = f ¯λ +gdφ satis-
fying (12.3) with the given function φ is convex and thus contractible. Since any
compact family in ~C(W) can be lifted to a family in C(W) by multiplying the 1-
forms with eρ]◦φ for a suﬃciently increasing function ρ : R→ R, this implies weak
contractibility on C(W). For 1-forms that agree with λ near ∂−W and with Cλ
near∂+W for constants C >0 we can choose ρ to be zero near ∂−W and constant
near ∂+W . □
Corollary 12.4. For any Weinstein manifold W = (V,ω,X,φ ) and any~W =
(V,~ω, ~X,φ )∈C (W) the manifolds (V,ω ) and (V,~ω) are symplectomorphic.

256 12. MODIFICATIONS OF WEINSTEIN STRUCTURES
Proof. Corollary 12.3 provides a Weinstein homotopy Wt from W to~W with
common Lyapunov function φ. This homotopy deﬁnes a Liouville homotopy in the
sense of Section 11.2, with an exhaustion given by regular sublevel sets of φ. So
Proposition 11.8 yields a family of symplectomorphisms from W0 to Wt. □
12.2. Holonomy of Weinstein cobordisms
In this section we consider Weinstein cobordisms W = (W,ω,X,φ ) without
critical points (of the function φ). We denote by Γ W :∂+W→∂−W the holonomy
diﬀeomorphism along trajectories of X. According to Lemma 11.4, it deﬁnes a
contactomorphism
ΓW : (∂+W,ξ +)→ (∂−W,ξ−)
for the contact structures ξ± on ∂±W induced by the Liouville form λ =iXω.
We say that two Weinstein structures W = (ω,X,φ ) and~W agree up to scaling
on a subset A⊂ W if ~W|A = (Cω,X,φ ) for a constant C >0. Note that in this
case~W|A has Liouville form Cλ.
Let us ﬁx a Weinstein cobordism W = (W,ω,X,φ ) without critical points. We
denote byW(W) the space of all Weinstein structures W = (W,ω,X,φ ) with the
same function φ such that
• W coincides with W onOp∂−W and up to scaling on Op∂+W ;
• W∈C (W), i.e., W and W induce the same contact structures on level
sets of φ.
Equivalently,W(W) can be viewed as the space of Liouville forms λ = f ¯λ +gdφ
withf≡ 1 near ∂−W ,f≡C near∂+W , and g≡ 0 near ∂W , where λ denotes the
Liouville form of W.
Denote by D(W) the space of contactomorphisms ( ∂+W,ξ +) → (∂−W,ξ−),
where ξ± is the contact structure induced on ∂±W by W. Note that Γ W∈D (W)
for any W∈W (W). The following two lemmas are analogues of Lemmas 9.41
and 9.42 in the context of Weinstein cobordisms.
Lemma 12.5. Let W be a Weinstein cobordism without critical points. Then
the map W(W)→D (W) that assigns to W its holonomy ΓW is a Serre ﬁbration.
In particular:
(i) Given W∈W (W) and an isotopy ht∈D (W), t∈ [0, 1], with h0 = Γ W
there exists a path Wt∈W (W) with W0 = W such that ΓWt =ht for all t∈ [0, 1].
(ii) Given a path Wt ∈W (W), t∈ [0, 1], and a path ht ∈D (W) which is
homotopic to ΓWt with ﬁxed endpoints, there exists a path ~Wt∈W (W) with~W0 =
W0 and~W1 = W1 such that Γ~Wt
=ht for all t∈ [0, 1].
Proof. Following the ﬂowlines of X we ﬁnd a diﬀeomorphism W∼= [a,c ]× Σ
under which φ(r,x ) = r and X is a positive multiple of ∂r, hence λ = ¯gα for the
contact form α = ¯λ|∂−W and a function ¯g :W→ R+. In particular, ¯λ deﬁnes the
same contact structure ξ on each level set {r}× Σ. Let us ﬁx a cutoﬀ function
τ : [a,c ]→ [0, 1] which equals 0 near a and c, and 1 near a point b∈ (a,c ).
We will identify elements inW(W) with their Liouville forms λ and denote by
Γλ their holonomy. Suppose we are given λ∈W (W) and an isotopy ht∈D (W),
t∈ [0, 1], with h0 = Γλ. For t∈ [0, 1] we push forward λ to a 1-form λt := (Ht)∗λ
on [a,b ]× Σ under the diﬀeomorphism Ht(r,x ) := h−1
tτ(r)(x). Since Ht induces a

12.2. HOLONOMY OF WEINSTEIN COBORDISMS 257
contactomorphism on each level{r}× Σ, the form λt deﬁnes the contact structure
ξ on each level set in [a,b ]× Σ. By construction, λt has holonomy ht :{b}× Σ→
{a}× Σ.
Near{b}× Σ we have λt = h∗
tλ = gtλ for positive functions gt : Σ → R+
with g0≡ 1. Pick a family of non-decreasing functions ρt : [b,c ]→ R which equal
1 near b and constants Ct≥ 1 near c. Using these functions, we extend λt over
[b,c ]× Σ by the formula λt :=ρt(r)gtτ(r)λ. Here we choose ˙ρt suﬃciently large so
that the functionft(r,x ) :=ρt(r)gtτ(r)(x) satisﬁes ∂
∂rft≥ 0, and hencedft(X)≥ 0.
Since g0≡ 1, we may choose ρ0≡ C0 = 1. It follows from Lemma 12.1 (i) that
(λt,φ ) deﬁnes a Weinstein structure on W whose holonomy over [b,c ]× Σ equals
the identity. Hence λt deﬁnes a path of Weinstein structures in W(W) starting at
λ0 =λ and with holonomy ht.
Since the above construction can be done smoothly with respect to a parameter
in Dk, the general homotopy lifting property follows. □
The proof of the following lemma is now analogous to that of Lemma 9.42,
using Lemma 12.5 instead of Lemma 9.41.
Lemma 12.6. Let Wt, W′
t be two paths in W(W) starting at the same point
W0 = W′
0. Suppose that for a subset A⊂∂+W one has ΓWt(A) = ΓW′
t(A) for all
t∈ [0, 1]. Then there exists a path ˆWt∈W (W) such that
(i) ˆWt = W2t for t∈ [0, 1
2];
(ii) ˆW1 = W′
1;
(iii) Γ ˆWt
(A) = ΓW′
1(A) for t∈ [ 1
2, 1]. □
Finally, we discuss how to interpolate between Weinstein cobordisms without
critical points. Let us ﬁx a product cobordism W ∼= [a,d ]× Σ with function
φ(r,x ) = r. We denote by W(W,φ ) the space of Weinstein structures on W with
function φ. For a contact structure ξ on Σ we denote by W(W,ξ,φ )⊂W (W,φ )
the subspace of Weinstein structures inducing the contact structure ξ on each level
set r× Σ. For a<b<c<d we set W′ := ([a,b ]∪ [c,d ])× Σ⊂W .
Lemma 12.7. The restriction maps
W(W,φ )→W (W′,φ )
/
scaling,
W(W,ξ,φ )→W (W′,ξ,φ )
/
scaling
are Serre ﬁbrations. In particular:
(i) Given W∈W (W,φ ) and a path W′
t∈W (W′,φ ), t∈ [0, 1], with W′
0 =
W|W′ there exists a path Wt∈W (W,φ ) with W0 = W such that Wt|W′ = W′
t up
to scaling for all t∈ [0, 1].
(ii) Given a path Wt∈W (W,φ ),t∈ [0, 1], and a path W′
t∈W (W′,φ ) which is
homotopic to Wt|W′ with ﬁxed endpoints, there exists a path ~Wt∈W (W,φ ) which
is homotopic to Wt with ﬁxed endpoints such that ~Wt|W′ = W′
t up to scaling for
all t∈ [0, 1].
Analogous statements hold with ﬁxed contact structure ξ.
Proof. Let us ﬁrst consider the ﬁbration W(W,ξ,φ )→W (W′,ξ,φ )/scaling.
We again denote elements in W(W,ξ,φ ) just by their Liouville forms. Consider
λ∈W (W,ξ,φ ) with Liouville ﬁeld X and Hamiltonian vector ﬁeld Xφ, and a path

258 12. MODIFICATIONS OF WEINSTEIN STRUCTURES
λ′
t = f′
tλ +g′
tdφ∈W (W′,ξ,φ ) with λ′
0 = λ|W′. After multiplying λ′
t with eσ◦φ
for a suﬃciently increasing function σ : R→ R, we may assume that df′
t(X′
t)≥ 0,
where X′
t denotes the Liouville ﬁeld of λ′
t. We extend λ′
t to Weinstein structures
(still denoted by the same letter) λ′
t = f′
tλ +g′
tdφ ∈ W(~W,ξ,φ ), where ~W =
([a,~b]∪ [~c,d ])× Σ for some b <~b <~c < c. Fix a function ρ : [b,c ]→ [0, 1] which
equals 0 on [~b,~c] and 1 near b,c and pick functions ft :W→ R with f0≡ 1 which
agree with f′
t on ~W and satisfy dft(X)≥ 0 (this is possible after choosing the
function σ above suﬃciently increasing). We claim that
λt :=ftλ +ρ◦φg′
tdφ
deﬁnes an extension of λ′
t to a path in W(W,ξ,φ ). Indeed, on [~b,~c]× Σ the forms
λt agree with ftλ and thus deﬁne Weinstein structures by Lemma 12.1 (i). On
~W we have λt = f′
tλ +ρ◦φg′
tdφ, where f′
tλ (by the preceding argument) and
f′
tλ +g′
tdφ =λ′
t (by hypothesis) both belong to W(~W,ξ,φ ) and ρ : [b,c ]→ [0, 1],
hence λt∈W (~W,ξ,φ ) by Corollary 12.3 (ii).
Since this construction works smoothly for families, it proves the Serre ﬁbration
property forW(W,ξ,φ )→W (W′,ξ,φ )/scaling.
The case W(W,φ )→W (W′,φ )/scaling reduces to the case with ﬁxed ξ by
Gray’s stability theorem: Consider families W′
λ,t∈W (W′,φ ) and Wλ∈W (W,φ )
with W′
λ,0 = Wλ|W′ forλ∈Dk,t∈ [0, 1]. Let ξ be the contact structure induced by
W0,0 on{a}× Σ. By Gray’s Theorem 6.23 there exists a family of diﬀeomorphisms
hλ,t : W → W , λ∈ Dk, t∈ [0, 1], such that the pullbacks h∗
λ,tW′
λ,t and h∗
λ,0Wλ
induce ξ on all level sets. Let ~Wλ,t ∈ W(W,ξ,φ ) be the lift of h∗
λ,tW′
λ,t with
~Wλ,0 =h∗
λ,0Wλ. Then Wλ,t := (hλ,t)∗~Wλ,t is the desired lift of W′
λ,t. □
12.3. Liouville ﬁelds near isotropic submanifolds
In this section we discuss the construction and modiﬁcation of Liouville ﬁelds
near isotropic submanifolds. We begin with a construction to extend a vector ﬁeld
on an isotropic submanifold to a Liouville ﬁeld on a neighborhood.
Consider an isotropic submanifold L of a symplectic manifold ( V,ω ) and a
compact subset K⊂L. Assume for simplicity that the symplectic normal bundle
(TL )ω/TL is trivial (this assumption is not necessary but will be satisﬁed in our
applications). Then by the isotropic neighborhood theorem (Corollary 6.13), a
neighborhood of K in (V,ω ) is symplectomorphic to a neighborhood of K inT∗L×
C𝓁 with coordinates (q,p,z =x +iy) and the symplectic form
ωst =
k∑
i=1
dpi∧dqi +
𝓁∑
j=1
dxj∧dyj.
It has the canonical Liouville ﬁeld
p∂p + 1
2z∂z =
∑
i
pi∂pi + 1
2
∑
j
(xj∂xj +yj∂yj).
To each tangent vector ﬁeld Y on L we associate the Liouville vector ﬁeld
ˆY :=p∂p + 1
2z∂z +XH

12.3. LIOUVILLE FIELDS NEAR ISOTROPIC SUBMANIFOLDS 259
onT∗L× C𝓁, whereXH is the Hamiltonian vector ﬁeld of the Hamiltonian function
H(q,p,z ) :=⟨p,Y (q)⟩.
We extend each smooth function ψ :L→ R to a function
ˆψ(q,p,z ) :=ψ(q) +ρ(q,p,z ), ρ (q,p,z ) :=|p|2 +|z|2
on T∗L× C𝓁, for some Riemannian metric on L.
Lemma 12.8. Suppose that all eigenvalues at zeroes of Y have real part < 1.
Then the pair (ˆY, ˆψ) has the following properties.
(i) ˆY is a Liouville ﬁeld for ωst which coincides with Y alongL and satisﬁes
ˆY·ρ≥ερ nearK for some ε> 0.
(ii) The zeroes of ˆY agree with the zeroes of Y and have the same nullity and
Morse index.
(iii) If Y is gradient-like for ψ, then ˆY is gradient-like for ˆψ nearK.
(iv) Suppose that Y is the restriction of a vector ﬁeld X deﬁned on a neigh-
borhood ofL which is gradient-like for a function φ :OpL→ R. Suppose
that the zeroes of X are isolated and at each zero q∈L the center-stable
spaceE0
q⊕E−
q equalsTqL and the unstable spaceE+
q is coisotropic. Then
we can arrange that ˆY is gradient-like for the given function φ.
(v) The construction of (ˆY, ˆψ) also works if L has nonempty smooth bound-
ary.
Proof. (i) Let us write Y (q) =∑
iYi(q)∂qi in local coordinates (qi,pi), hence
H(q,p,z ) =∑
ipiYi(q) and we compute
dH =
∑
i
Yi(q)dpi +
∑
i,j
∂Yj
∂qi
pjdqi,
XH =
∑
i
Yi(q)∂qi−
∑
i,j
∂Yj
∂qi
pj∂pi,
ˆY =
∑
i
Yi(q)∂qi +
∑
i,j
(
δij− ∂Yj
∂qi
)
pj∂pi + 1
2z∂z.
This shows that ˆY = Y along L. Moreover, as the real parts of eigenvalues of
Id−DqY are bounded below by some ε∈ (0, 1) near K, we compute in geodesic
normal coordinates at q∈L:
ˆY·ρ = 2⟨p, (Id−DqY )p⟩ +|z|2≥ 2ε|p|2 +|z|2≥ερ.
(ii) The formula for ˆY shows that ˆY (q,p,z ) = 0 if and only if z = 0,Y (q) = 0, and
p∈ ker(Id−DqY ) ={0}, so the zeroes of ˆY coincide with the zeroes of Y on L.
If q is a zero for Y , then positivity of the real parts of all eigenvalues of Id −DqY
implies that (q, 0, 0) is a zero for ˆY with the same nullity and Morse index.

260 12. MODIFICATIONS OF WEINSTEIN STRUCTURES
(iii) Suppose that Y·ψ≥δ(|Y|2 +|dψ|2) for some δ >0. Using ˆY·ρ≥ερ and
|DqY|2≤C near K for some C≥ 1, we estimate at points of K:
ˆY· ˆψ≥Y·ψ +ε(|p|2 +|z|2)
≥δ(|Y|2 +|dψ|2) + ε
4C (|p|2 +|(Id−DqY )p|2 +|z|2 +|z∂z|2)
≥ min{δ,ε/ 4C}(|ˆY|2 +|dˆψ|2).
(iv) Under the hypotheses of (iv), we can choose the identiﬁcation with OpK⊂
T∗L× C𝓁 such that E+
q = T∗
qL× C𝓁 at each critical point q∈ L. Since this also
equals the unstable space with respect toˆY , and the Hessian ofφ is positive deﬁnite
on E+
p by Lemma 9.9, it follows that ˆY is gradient-like for φ near critical points
and hence near K.
(v) If L has nonempty smooth boundary, we extend L to a slightly larger
isotropic submanifold L′ with coordinates ( q1,...,q k) such that L ={q1 ≤ 0}.
Now we extend a vector ﬁeld Y on L to Y′ on L′ and deﬁne the Liouville ﬁeld ˆY′
as above, and similarly for a function ψ. Properties (i-iv) follow. □
The second result concerns interpolation between two Liouville ﬁelds tangent to
an isotropic submanifold with common Lyapunov function. Recall that a Lyapunov
pair (X,φ ) satisﬁes in particular an estimate
(12.4) |X|≤ C|dφ|.
In suitable coordinatesZ near a nondegenerate critical point we have|dφ(Z)| =|Z|,
so (12.4) (for some constant C) is equivalent to X(0) = 0. In suitable coordinates
(x,y,z ) near an embryonic point we have |dφ(x,y,z )| =|x| +|y| +|z2|, so (12.4)
is equivalent to X(0, 0, 0) = ∂X
∂z (0, 0, 0) = 0. This implies that in both cases (12.4)
carries over to families as follows: Let ( Xt,φ ) be a smooth family of Lyapunov
pairs with φ having nondegenerate or embryonic critical points. Then there exists
a constant C such that
(12.5) |Xs−Xt|≤ C|dφ||s−t| for all t∈ [0, 1].
We say that a functionφ :V → R is transversely nondegenerate along a subma-
nifold L if at each critical point x∈L the Hessian satisﬁes ker Hessxφ⊂TxL. By
Lemma 9.3, this implies that near each critical point x∈L there exist coordinates
(q,p ) in which
φ(q,p ) =ψ(q) + 1
2
𝓁∑
i=1
p2
i− 1
2
m∑
i=𝓁+1
p2
i,
whereq is the coordinate along L. It follows that |dφ(q,p )|2 =|dψ(q)|2 +|p|2, so φ
satisﬁes the estimate
(12.6) |p|≤| dφ(q,p )|≤| dφ(q,sp )| for all s≥ 1.
This estimate globalizes to a tubular neighborhood ofL for a suitable bundle metric
on the normal bundle.
Now we can state the second interpolation result.
Lemma 12.9. Let (V,ω ) be a symplectic manifold. Let L⊂ V be an isotropic
submanifold, possibly with nonempty smooth boundary, and K⊂L a compact sub-
set. Let φ : V → R be a function with nondegenerate or embryonic critical points
which is transversely nondegenerate along L. Let X and Xloc be Liouville ﬁelds for

12.3. LIOUVILLE FIELDS NEAR ISOTROPIC SUBMANIFOLDS 261
ω on V resp. on a neighborhood Vloc ⊂ V of K. Assume that both X and Xloc
are tangent to L and gradient-like for φ. Then there exists a homotopy of Liouville
ﬁelds Xt, t∈ [0, 1], on V with the following properties:
(i) Xt is tangent to L and gradient-like for φ for all t;
(ii) X0 =X, Xt =X outside Vloc and on the set L∩{Xloc =X};
(iii) Xt = (1−t)X +tXloc onOpK.
Proof. Suppose ﬁrst thatL has no boundary. Let us identify (after shrinking)
Vloc with a subset of the normal bundle to L such that the estimate (12.6) holds.
Let δ >0 be a constant such that
X·φ≥δ|dφ|2, X loc·φ≥δ|dφ|2.
Step 1. We ﬁrst prove the assertion under the additional hypothesis
(12.7) |X−Xloc|≤ α|dφ|, α :=δ/4.
The 1-form λ :=iX−Xlocω on Vloc satisﬁes dλ = 0, and λ|L = 0 because X−Xloc
is tangent to L andL is isotropic. By the relative Poincar´ e lemma (see [87]), there
exists a function H :Vloc→ R withH≡ 0 on L∩Vloc anddH =λ. It follows that
Xloc−X =XH. For each ε∈ (0, 1) choose a cutoﬀ function g : [0,ε ]→ [0, 1] with
g≡ 1 near 0, g≡ 0 near ε, and |g′(t)|≤ 2
ε for all t. Fix another cutoﬀ function
h : L→ [0, 1] with h≡ 1 near K and h≡ 0 outside a larger neighborhood of K
in L∩Vloc. Then the function f(q,p ) := h(q)g(|p|) satisﬁes f≡ 1 near K, f≡ 0
outside Vloc, and|df(q,p )|≤ 2/ε for suﬃciently small ε. Deﬁne
Ht :=tfH, X t :=X +XHt.
Note that
Xt =X +tfXH +tHXf = (1−tf)X +tfXloc +tHXf.
So the vector ﬁelds Xt are tangent to L (where H = 0) and satisfy LXtω = ω,
X0 =X,Xt =X outsideVloc (wheref≡ 0) and on the set L∩{X =Xloc} (where
H≡ 0), and X1 =Xloc onOpK (where f≡ 1). By (12.6) and (12.7) we have
|H(q,p )| =|
∫ 1
0
d
dsH(q,sp )ds|
≤
∫ 1
0
|p|| ∂H
∂p (q,sp )|ds
≤
∫ 1
0
|p||Xloc(q,sp )−X(q,sp )|ds
≤α
∫ 1
0
|p||dφ(q,sp )|ds
≤α
∫ 1
0
|p||dφ(q,p )|ds
≤α|p||dφ(q,p )|.

262 12. MODIFICATIONS OF WEINSTEIN STRUCTURES
Using this and hypothesis α =δ/4 we obtain
Xt·φ =
[
(X +tfXH) +tHXf
]
·φ
=
[
(1−tf)X +tfXloc +tHXf
]
·φ
≥δ|dφ|2−|H||df||dφ|
≥
(
δ−α|p|2
ε
)
|dφ|2
≥ (δ− 2α)|dφ|2
≥ δ
2|dφ|2.
Here we have used that the term involving |p| is not present for |p| > ε because
then df vanishes. This proves gradient-likeness and thus the assertion under the
additional hypothesis (12.7).
Step 2. For the general case (still assuming∂L = ∅), consider the vector ﬁelds
¯Xt := (1−t)X+tXloc onVloc. They all satisfyL ¯Xtω =ω and ¯Xt·φ≥δ|dφ|2. In view
of the estimate (12.5), we can pick a partition 0 = t0 <t 1 <··· <t N = 1 such that
| ¯Xti− ¯Xti−1|≤ α|dφ| for all i = 1,...,N . Apply Step 1 with (X,X loc) = (X0,Xt1)
and someε =ε0 to ﬁnd a vector ﬁeld ~X1 which equalsX0 =X for|p|≥ ε0 andXt1
for|p|≤ 2ε1 with some ε1 <ε 0. Next apply Step 1 with ( X,X loc) = (~X1,Xt2) and
ε =ε1 to ﬁnd a vector ﬁeld ~X2 which equals ~X1 for|p|≥ ε1 and Xt2 for|p|≤ 2ε2
with someε2 <ε 1. Continuing this way, we ﬁnd a Liouville ﬁeld ~XN with ~XN =X
outside Vloc and ~XN = Xloc near K. Now Xt := (1−t)X +t~XN is the desired
homotopy.
Step 3. Finally, consider the case that L has nonempty boundary. Extend
L to a slightly larger isotropic submanifold L′ with coordinates (q1,...,q k) such
that L ={q1≤ 0}. Note that the Liouville ﬁelds X,X loc are tangent to L but not
necessarily to L′. However, their components normal to L′ vanish to inﬁnite order
as q1→ 0. It follows that the closed 1-form λ = iX−Xlocω and its primitive H
vanish to inﬁnite order along L′ as q1→ 0. In particular, we have H(q, 0) =O(q6
1)
and the estimate above yields
|H(q,p )|≤ α|p||dφ(q,p )| +O(q6
1).
Forε∈ (0, 1) we pick a cutoﬀ functionf(q,p ) :=h(q)g(|p|) such thatf≡ 1 nearK,
f≡ 0 outside Vloc∩{q1≤ε,|p|≤ ε}, and|df(q,p )|≤ 2/ε. Then the last estimate
in Step 1 gets modiﬁed to
Xt·φ≥ δ
2|dφ|2− 2
ε|dφ|O(q6
1),
where the last term is only present if q1≤ε because otherwise df = 0. So we can
estimate the term O(q6
1) by cε2q4
1 with a constant c> 0 independent of ε. On the
other hand, since all critical points of φ atq1 = 0 are nondegenerate or embryonic,
it satisﬁes near{q1 = 0} an estimate|dφ|2≥γq4
1 with a constantγ >0 independent
of ε. It follows that
Xt·φ≥ δ
4|dφ|2 +
(δγ
4 − 2cε|dφ|
)
q4
1≥ δ
4|dφ|2
for ε suﬃciently small and the proof is concluded as before. □

12.4. WEINSTEIN STRUCTURES NEAR CRITICAL POINTS 263
We conclude this section with another interpolation result which will be used in
Section 12.6 for cancellation and creation of critical points of Weinstein structures.
Lemma 12.10. Let (W,ω,X,φ ) be a Weinstein cobordism and L ⊂ W an
isotropic submanifold with boundary such that L is invariant under the forward
ﬂow of −X. Let (ω,X loc,φ loc) be a Weinstein structure on a subset Wloc ⊂ W
containing L which coincides with (ω,X,φ ) near L∩∂Wloc = ∂L and such that
Xloc is tangent to L. Suppose that X, Xloc satisfy estimates
ερ≤X·ρ, Xloc·ρ≤ε−1ρ
for some ε >0 and a smooth function ρ : Wloc→ [0,∞) with ρ−1(0) = L. Then
there exists a Weinstein structure (ω,Y,ψ ) onW which agrees with (ω,X,φ ) outside
Wloc and with (ω,X loc,φ loc) nearL, and which has no critical points in Wloc\L.
Remark 12.11. Note that the restrictions of X and Xloc to L are completely
unrelated, in particular they can have diﬀerent zero sets. Note also that Lemma
12.10 does not provide a Weinstein homotopy between ( ω,X,φ ) and (ω,Y,ψ ).
Proof. As in the proof of Lemma 12.9, we ﬁnd that Xloc−X = XH for a
Hamiltonian function H on Wloc which vanishes on L. Choose γ > 0 such that
(Xloc,φ loc) = (X,φ ) on {ρ≤ γ}∩ ∂Wloc. Pick a cutoﬀ function f = f(ρ) which
equals 1 near ρ = 0 and 0 for ρ≥γ and deﬁne Y :=X +XfH . Since Xf·ρ = 0,
we obtain
Y·ρ = (1−f)X·ρ +fXloc·ρ≥ερ.
Let g =g(ρ) be another cutoﬀ function with support in the set {f = 1}. Then on
suppg we haveY =Xloc and thus
Y·
(
g(ρ)φloc
)
=g(ρ)Xloc·φloc +φlocg′(ρ)Xloc·ρ≥gδ|Xloc|2−C|g′(ρ)|ρ
for some constants δ,C >0. Choose g such that C|g′|≤ ε/2 and g(0)> 0. Then
Y·
(
g(ρ)φloc +ρ
)
≥g(ρ)δ|Xloc|2 +ερ/2> 0,
so ψloc :=g(ρ)φloc +ρ is a Lyapunov function for Y on Wloc. We can adjust ψloc
to make it agree with φ near Wloc∩∂−W .
Finally, we interpolate between the Lyapunov functions ψloc and φ for Y near
∂Wloc as follows. After adding a constant to φ we may assume that φ|∂−W = 0.
Pick b >0 so small that φ = φloc on the set L∩{g(0)φ < b}. By Corollary 9.21
there exists a Lyapunov function ϑ :W→ R for X with the following properties:
• ϑ =φ onOp∂W and outside Wloc;
• ϑ|L <b .
We claim that the function ψ := smooth max(ϑ,ψ loc) has the desired properties.
Indeed, forb andγ suﬃciently small we haveψ =ψloc on suppf, soψ is a Lyapunov
function for Y on suppf. On Wloc\ suppf the functions ϑ and ψloc =ρ are both
Lyapunov for the vector ﬁeld Y = X, hence so is ψ. Near ∂−W we have ψ = φ,
and outside Wloc∩O p∂−W we haveϑ =φ>ψ loc and thusψ =φ. This concludes
the proof of Lemma 12.10. □
12.4. Weinstein structures near critical points
In this section we prove that a Weinstein structure can be arbitrarily altered
near a hyperbolic or embryonic critical point. The precise formulation is given in
the following proposition, which is a Weinstein version of Corollary 9.14. We refer

264 12. MODIFICATIONS OF WEINSTEIN STRUCTURES
to Chapter 9 for the relevant notions concerning hyperbolic and embryonic critical
points.
Proposition 12.12. Let p be a hyperbolic (resp. embryonic) critical point of
φ in a Weinstein manifold W = (V,ω,X,φ ). Let Wloc = (ωloc,X loc,φ loc) be
a Weinstein structure on a neighborhood Vloc of p such that p is a hyperbolic
(resp. embryonic) critical point of φloc of value φloc(p) = φ(p) and Morse in-
dex indp(φloc) = ind p(φ). Then there exists a homotopy of Weinstein structures
Wt = (ωt,Xt,φt) on V with the following properties:
(i) W0 = W and Wt = W outside Vloc;
(ii) Xt has a unique hyperbolic (resp. embryonic) zero at p in Vloc for all t;
(iii) W1 = Wloc nearp;
(iv) if W−
p (Xloc) = W−
p (X) (resp. ˆW−
p (Xloc) = ˆW−
p (X)) then W−
p (Xt) =
W−
p (X) (resp.ˆW−
p (Xt) =ˆW−
p (X)) for all t.
Moreover, if ωloc = ω we can arrange ωt = ω for all t, and if φloc = φ we can
arrangeφt =φ for all t.
Since there exist Stein models for hyperbolic and embryonic critical points, we
obtain in particular
Corollary 12.13. A Weinstein structure with hyperbolic and embryonic crit-
ical points is homotopic to one which is Stein for a given complex structure near
the critical points.
Proof of Proposition 12.12. By Darboux’s theorem (Proposition 6.5), af-
ter moving W by a diﬀeotopy near p we may assume that ωloc =ω. After this, we
will keep ω ﬁxed and modify (X,φ ) near p in three steps.
Step 1. Denote by W±
p resp. ˆW−
p the stable and unstable manifolds with
respect to X. Let L := W−
p in the hyperbolic and L := ˆW−
p in the embryonic
case. By Proposition 11.9, L is isotropic (with ∂L⁄= ∅ in the embryonic case).
Denote by Lloc the corresponding isotropic submanifold for Xloc. After pulling
back (Xloc,φ loc) by a symplectic isotopy supported near p, we may assume that
Lloc =L near p and the unstable spaces E+
p (Xloc) =E+
p (X) =:E+
p agree.
So it suﬃces to consider the case that X and Xloc have a common stable
manifold L and unstable space E+
p . During the following modiﬁcations L and
E+
p will remain ﬁxed. Let us call a homotopy of Weinstein structures ( ω,Xt,φt)
admissible if it has properties (i-ii) of the proposition, Xt is tangent to L and has
unstable space E+
p for all t.
Step 2. Note that the quadruple ( L,K :={p},Y := X|L,φ ) satisﬁes the
hypotheses of Lemma 12.8 (iv). Let ˆY be the new Liouville ﬁeld obtained by
Lemma 12.8. Thus ˆY is gradient-like for φ and agrees with X on L. Since φ
is transversely nondegenerate along L, Lemma 12.9 (with K ={p}) provides an
admissible homotopy (ω,Xt,φ ) from X0 =X toX1 = ˆY . After renaming X1 back
to X, we may hence assume that X|Opp = ˆY is obtained by the construction of
Lemma 12.8 from its restriction Y := X|L. After applying Proposition 9.23, we
may further assume thatφ|Opp = ˆψ is obtained by the construction of Lemma 12.8
from its restriction ψ :=φ|L.
Step 3. By Corollary 9.14, there exists a homotopy of Lyapunov pairs (Yt,ψt)
on L∩O pp having a hyperbolic resp. embryonic critical point p from (Y0,ψ 0) =

12.5. WEINSTEIN STRUCTURES NEAR STABLE DISCS 265
(Y,ψ ) to ( Y1,ψ 1) = ( Yloc,ψ loc) := ( Xloc|L,φ loc|L). Lemma 12.8 (which works
smoothly in the parameter t) provides an extension to a homotopy of Weinstein
structures (ω,ˆYt,ˆψt) onOpp from (ˆY0,ˆψ0) = (X,φ )|Opp to (ˆY1,ˆψ1) = (ˆYloc,ˆψloc).
By Lemma 9.12 there exists a partition 0 = t0 < t1 <··· < tN = 1 such that
for all i the following hold:
• ˆψti is a Lyapunov function for ˆYt for all t∈ [ti,ti+1];
• ˆψt is a Lyapunov function for ˆYti+1 for all t∈ [ti,ti+1].
Therefore we can inductively for each i apply Lemma 12.9 to change ˆYti to ˆYti+1
nearp (ﬁxing ˆψti), and then Proposition 9.23 to change ˆψti to ˆψti+1 nearp (ﬁxing
ˆYti+1).
Renaming the new Weinstein structure resulting from this construction back
to (X,φ ), we have thus achieved that ( X,φ ) = (ˆYloc,ˆψloc) near p. Since φloc is a
Lyapunov function for both Xloc and ˆYloc by Lemma 12.8, we can use Lemma 12.9
to arrange X = Xloc near p. Finally, we apply once again Proposition 9.23 to
arrange φ =φloc near p.
The proof shows that ωloc = ω implies ωt = ω for all t. If φloc = φ, then
Lemma 9.38 yields a diﬀeotopy ht : V → V with h0 = Id such that φt◦ht = φ
for all t∈ [0, 1]. Moreover, ht = Id outside Vloc and h1 = Id on Opp, so h∗
t Wt is
the desired Weinstein homotopy with ﬁxed function φ. This concludes the proof of
Proposition 12.12. □
12.5. Weinstein structures near stable discs
Now we apply the results of the previous two sections to construct and deform
Weinstein structures near stable discs. Our ﬁrst result concerns deformations of a
given Weinstein structure.
Proposition 12.14. Consider a Weinstein manifold (V,ω,X,φ ) with a non-
degenerate critical point p of index k and an embedded k-disc ∆⊂W−
p containing
p. Let (ωloc,X loc,φ loc) be a Weinstein structure on a neighborhood Vloc of ∆ which
coincides with (ω,X,φ ) on ∆∪O p∂∆ (so in particular Xloc is tangent to ∆).
Then there exists a homotopy of Weinstein structures (ωt,Xt,φt) on V such that
(ωt,Xt,φt) = ( ω,X,φ ) outside Vloc and on the region where (ωloc,X loc,φ loc) =
(ω,X,φ ), and (ω1,X 1,φ 1) = (ωloc,X loc,φ loc) onOp ∆.
If ωloc =ω|Vloc we can achieve ωt =ω for all t∈ [0, 1].
Proof. After an application of the isotropic neighborhood theorem (Corol-
lary 6.13) and shrinking Vloc we may assume that ωloc = ω|Vloc. In the following
argument all Weinstein structures will have symplectic form ω. Let ( ˆY, ˆψ) be
the Weinstein structure obtained by Lemma 12.8 from the restriction ( Y,ψ ) :=
(X|∆,φ|∆). After applying Lemma 12.9 (with Lyapunov function φ), we may as-
sume that X = ˆY onOp ∆. Next we deform φ to ˆψ (through Lyapunov functions
for X ﬁxed outside Vloc) ﬁrst near p using Proposition 9.23, and then by interpo-
lation onOp ∆\O pp using φ|∆ = ˆψ|∆. After these deformations we may hence
assume that (X,φ ) = (ˆY, ˆψ) onOp ∆. Since (Y,ψ ) = (Xloc|∆,φ loc|∆), we can now
reverse the preceding argument to deform ( ˆY, ˆψ) to (Xloc,φ loc) near ∆. □
Remark 12.15. One can similarly prove a parametric version of Proposi-
tion 12.14.

266 12. MODIFICATIONS OF WEINSTEIN STRUCTURES
The following two lemmas concern the construction of Weinstein structures
near stable discs of Smale cobordisms. They will be used in Chapters 13 and 14
to upgrade Morse cobordisms and homotopies to Weinstein cobordisms and homo-
topies.
Lemma 12.16. Let S = (W,X,φ ) be an elementary Smale cobordism and ω a
nondegenerate 2-form on W . Let D1,...,D k be the stable discs of critical points of
φ and set ∆ :=⋃k
j=1Dj. Suppose that the discs D1,...,D k areω-isotropic and the
pair (ω,X ) is Liouville on Op (∂−W ). Then for any neighborhood U of ∂−W∪ ∆
there exists a homotopy (ωt,Xt), t∈ [0, 1], with the following properties:
(i) Xt is a gradient-like vector ﬁeld for φ and ωt is a nondegenerate 2-form
on W for all t∈ [0, 1];
(ii) (ω0,X 0) = (ω,X ), and (ωt,Xt) = (ω,X ) outsideU and on ∆∪Op (∂−W )
for all t∈ [0, 1];
(iii) (ω1,X 1) is a Liouville structure on Op (∂−W∪ ∆).
Proof. To simplify the notation, assume that φ has a unique critical point p
of index k with stable disc ∆. Let D⊂ Rn⊂ Cn be the unit k-disc and ωst the
standard symplectic structure on Cn. Since ω|∆ = 0, there exists an embedding
f :OpD ↪→ W mapping D onto ∆ such that f∗ω = ωst along D. According
to Proposition 6.22 (since λ = iXω vanishes on ∆), we can modify f such that
in addition f∗ω = ωst onOp (∂D). Thus f∗ωst and ω|Op (∂−W) ﬁt together to a
symplectic form ~ω onOp (∂−W∪ ∆) which agrees with ω along ∆∪O p (∂−W ).
The condition ~ω = ω along ∆∪O p (∂−W ) allows us to ﬁnd a homotopy ωt of
nondegenerate 2-forms on W , ﬁxed on ∆∪O p (∂−W ) and outside a neighborhood
of ∆, such that ω0 =ω and ω1|Op ∆ =~ω.
Note that the stable space E−
p equals Tp∆, but the unstable space E+
p need
not be ω1-coisotropic. After a further homotopy of symplectic 2-forms, supported
near p and keeping ∆ isotropic (but changing on TpW ), we may assume that E+
p
is ω1-coisotropic.
Next we apply Lemma 12.8 (the hypothesis on the eigenvalues is satisﬁed since
E−
p =Tp∆) to ﬁnd a Liouville ﬁeld X′ for ω1 onOp ∆ which agrees with X on ∆
and is gradient-like for φ. On Op (∂∆) we have X′ = X +XH for a function H
that vanishes together with its diﬀerential along ∆. So ~X :=X +XfH for a cutoﬀ
function f yields a Liouville ﬁeld for ω1 onOp (∂−W∪ ∆) which is gradient-like
for φ and coincides with X on ∆∪O p (∂−W ). Now we use Lemma 9.8 to extend
~X to a gradient-like vector ﬁeld for φ on W and set Xt := (1−t)X +t~X. □
Lemma 12.16 has the following version for homotopies.
Lemma 12.17. Let St = (W,Xt,φt), t∈ [0, 1], be an elementary Smale homo-
topy and ωt, t∈ [0, 1], a family of nondegenerate 2-forms on W . Let ∆t be the
skeleton of Xt and set
∆ :=
⋃
t∈[0,1]
{t}× ∆t⊂ [0, 1]×W.
Suppose that ∆t is ωt-isotropic for all t∈ [0, 1], the pair (ωt,Xt) is Liouville on
Op (∂−W ) for all t∈ [0, 1], and (ω0,X 0) and (ω1,X 1) are Liouville on all of W .
Then for any open neighborhood V = ⋃
t∈[0,1]{t}× Vt of ∆ there exists an open

12.6. MORSE-SMALE THEORY FOR WEINSTEIN STRUCTURES 267
neighborhoodU =⋃
t∈[0,1]{t}× Ut⊂ V of ∆ and a 2-parameter family (ωs
t,Xs
t ),
s,t∈ [0, 1], with the following properties:
(i) Xs
t is a gradient-like vector ﬁeld for φt andωs
t is a nondegenerate 2-form
on W for all s,t∈ [0, 1];
(ii) (ω0
t,X 0
t ) = (ωt,Xt) for all t∈ [0, 1], (ωs
0,Xs
0) = (ω0,X 0) and (ωs
1,Xs
1) =
(ω1,X 1) for all s∈ [0, 1], and (ωs
t,Xs
t ) = ( ωt,Xt) outside Vt and on
∆t∪O p (∂−W ) for all s,t∈ [0, 1];
(iii) (ω1
t,X 1
t ) is a Liouville structure on Ut for all t∈ [0, 1].
Proof. For a type I homotopy the proof is just a 1-parametric version of the
proof of Lemma 12.16. For an elementary homotopy of type IIb (the type IId case
is analogous), the proof is again analogous to the one of Lemma 12.16 with the
following modiﬁcations.
Let us parametrize the homotopy over t∈ [−1, 1] with an embryonic critical
point at t = 0. By Lemma 9.35 (cf. Figure 9.5), the skeletons ∆ t, t∈ [0, 1], form
a smooth family of embedded half-discs with upper boundaries ∂+∆t = D−
qt and
lower boundaries ∂−∆t = ∆t∩∂−W . Arguing as in the proof of Lemma 12.16,
we ﬁnd homotopies of nondegenerate 2-forms ωs
t , ﬁxed at s = 0, t = 0, t = 1 and
on ∆t∪O p (∂−W ), such that ω1
t are symplectic onOp ∆ and the unstable spaces
E+
pt,E +
qt are ωt-coisotropic. Now a 1-parametric version of Lemma 12.8 yields the
desired homotopy of gradient-like vector ﬁelds Xs
t . □
12.6. Morse-Smale theory for Weinstein structures
In this section we consider modiﬁcations of Weinstein structures analogous to
those considered in Chapter 10 for Stein structures.
The ﬁrst two lemmas have been proved in [32]; we include their easy proofs for
the sake of completeness.
Lemma 12.18. Let W = (W,ω,X,φ ) be a Weinstein cobordism structure such
thatφ has no critical points. Let Λ⊂∂+W be an isotropic submanifold and L⊂W
its image under the ﬂow of −X. Let (Λt)t∈[0,1] be an isotropic isotopy of Λ0 :=L∩
∂−W in∂−W . Then there exists a family of Weinstein structures Wt = (ωt,Xt,φ ),
t∈ [0, 1], with the following properties (see Figure 10.1):
(i) W0 = W, and Wt is ﬁxed on Op∂−W and up to scaling on Op∂+W ;
(ii) the Wt, t∈ [0, 1], induce the same contact structures on level sets of φ;
(iii) the image Lt of Λ under the ﬂow of −Xt intersects∂−W in Λt.
Proof. By the contact isotopy extension theorem (Proposition 6.24), there
exists a contact diﬀeotopyht :∂−W→∂−W withh0 = Id andht(Λ0) = Λt. Apply
Lemma 12.5 to obtain a homotopy of Weinstein structures Wt with properties
(i) and (ii) and whose holonomy equals ht◦ Γ : ∂+W → ∂−W , where Γ is the
holonomy of W. Hence the image Lt of Λ under the ﬂow of −Xt intersects ∂−W
in ht(Λ0) = Λt. □
Remark 12.19. If the isotopy Λ t in Lemma 12.18 is suﬃciently C1-small we
can keep Wt ﬁxed near ∂+W . We do not know whether in general the rescaling
near ∂+W is actually needed.
The second lemma is just a restatement of Lemma 9.45.

268 12. MODIFICATIONS OF WEINSTEIN STRUCTURES
Lemma 12.20. Let (W,ω,X,φ ) be an elementary Weinstein cobordism. Then
there is a homotopy (W,ω,X,φ t) relOp∂W of elementary Weinstein cobordisms
which arbitrarily changes the ordering of the critical values.
The following two propositions are the Weinstein analogues of Theorems 10.11
and 10.12 in the Stein case.
Proposition 12.21. Let (W,ω,X,φ ) be a Weinstein cobordism without critical
points. Then given any point p∈ IntW and integer k = 1,...,n there exists a
Weinstein homotopy (ω,Xt,φt) with the following properties:
(i) (X0,φ 0) = (X,φ ) and (Xt,φt) = (X,φ ) outside a neighborhood of p;
(ii) φt is a creation family such that φ1 has a pair of critical points of index
k and k− 1.
Proposition 12.22. Let (W,ω,X,φ ) be a Weinstein cobordism with exactly
two critical points p,q of index k and k− 1, respectively, which are connected by a
unique gradient trajectory along which the stable and unstable manifolds intersect
transversely. Let ∆ be the skeleton of (W,X ), i.e., the closure of the stable manifold
of the critical point p. Then there exists a Weinstein homotopy (ω,Xt,φt) with the
following properties:
(i) (X0,φ 0) = (X,φ ), and (Xt,φt) = (X,φ ) near ∂W and outside a neigh-
borhood of ∆;
(ii) φt has no critical points outside ∆;
(iii) φt is a cancellation family such that φ1 has no critical points.
Proof of Proposition 12.22. Pick a slightly larger embedded isotropic half-
disc ∆′ containing ∆ in its interior. Pick a gradient-like vector ﬁeld Y on ∆′ for
ψ := φ|∆′ with Y|∆ = X|∆. Let ( ω,ˆY, ˆψ) be the Weinstein structure on Op ∆′
provided by Lemma 12.8. After applying Proposition 12.14 twice and shrinking ∆′,
we may assume that (X,φ ) = (ˆY, ˆψ) onOp ∆′.
Note that Y is inward pointing along ∂−∆′ and outward pointing along ∂+∆′.
Hence Lemma 9.49 provides a cancellation family (Yt,ψt) on ∆′ which agrees with
(Y,ψ ) at t = 0 and near ∂∆′. Using Lemma 12.8 we extend it to a Weinstein
homotopy (ω,ˆYt,ˆψt) onOp ∆′ which agrees with (X,φ ) at t = 0 and on Op∂∆′.
Finally, we apply Lemma 12.10 to the pairs ( X,φ ) and ( Xloc,φ loc) = ( ˆYt,ˆψt),
t∈ [0, 1], to obtain a cancellation type Weinstein homotopy (ω,Xt,φt) onW which
agrees with (X,φ ) at t = 0 and outside a neighborhood of ∆ ′, and with (ω,ˆYt,ˆψt)
on a smaller neighborhood of ∆′. □
Proof of Proposition 12.21. The proof is similar to that of Proposition
12.22. Deﬁne the vector ﬁeld Y (x) = ∂xk and the function ψ(x) = xk on Rk and
their extensions to a Liouville ﬁeld ˆY and a function ˆψ on Cn as in Lemma 12.8.
Proposition 6.22 provides an isomorphism of isotropic setups
F : (Op 0⊂ Cn,ω st,ˆY,{ˆψ = 0}, 0)∼= (Opp⊂W,ω,X, {φ =a},p ),
where a = φ(p). We will suppress the diﬀeomorphism F and just identify the
corresponding objects.
After a homotopy of φ we may assume that φ = ˆψ on a smaller neighborhood
U of p. Lemma 9.47 provides a creation family ( Yt,ψt) on the disc ∆ := U∩ Rk
which agrees with (Y,ψ ) at t = 0 and near ∂∆. Moreover, we can arrange that all

12.7. ELEMENTARY WEINSTEIN HOMOTOPIES 269
eigenvalues of DYt at critical points have real part < 1. Lemma 12.8 provides an
extension of (Yt,ψt) to a Weinstein homotopy (ˆYt,ˆψt) onOp ∆ which agrees with
(X,φ ) att = 0 and onOp∂∆. Finally, we apply Lemma 12.10 to obtain a creation
type Weinstein homotopy (ω,Xt,φt) on W which agrees with (X,φ ) at t = 0 and
outside a neighborhood of ∆, and with ( ω,ˆYt,ˆψt) on a smaller neighborhood of
∆. □
12.7. Elementary Weinstein homotopies
A Weinstein homotopy ( W,ωt,Xt,φt) is called elementary if the underlying
Smale homotopy (W,Xt,φt) is elementary. An admissible partition for a Weinstein
homotopy is an admissible partition for the underlying Smale homotopy. According
to Lemma 9.37, any Weinstein homotopy admits an admissible partition.
Lemma 9.38 has the following analogue for elementary Weinstein homotopies.
Lemma 12.23. Let Wt = (W,ωt,Xt,φt) and~Wt = (W,~ωt, ~Xt,~φt), t∈ [0, 1], be
two elementary Weinstein homotopies with the same proﬁle such that W0 =~W0.
Then there exists a diﬀeotopy ht :W→W withh0 = Id such that φt =~φt◦ht, and
the paths of Weinstein structures Wt and h∗
t~Wt are homotopic with ﬁxed functions
φt and ﬁxed at t = 0.
Moreover, if Wt = ~Wt up to scaling near ∂±W we can arrange that ht = Id
near ∂±W and the homotopies between Wt and h∗
t~Wt are ﬁxed up to scaling near
∂±W .
Proof. The proof follows the same scheme as that of Lemma 9.38, keeping
track of the contact structures on level sets.
Denote by Ct,~Ct the critical point sets and by ∆t,~∆t the skeletons of Wt,~Wt.
We ﬁrst use Theorem 9.4 and the Morse Lemma 9.1 to construct a family of diﬀeo-
morphismsft :OpCt→O p ~Ct withf0 = Id and~φt◦ft =φt. By Proposition 12.12,
the path of Weinstein structures Wt is homotopic with ﬁxed functions φt and ﬁxed
at t = 0 to one which agrees with f∗
t~Wt onOpCt. After replacing Wt with this
new path we may hence assume that Wt =f∗
t~Wt onOpCt.
Next we canonically extend the maps ft :OpCt→O p ~Ct to diﬀeomorphisms
ft :Ut→ ~Ut between neighborhoods of ∆t mappingφt to ~φt and trajectories of Xt
to trajectories of ~Xt.
By Lemma 11.4, ft induces contactomorphisms on all level sets. Note that
U−
t := ∂−W∩Ut is a neighborhood of the isotropic submanifold ∆ t∩∂−W , and
each restrictionft|U−
t
is contact isotopic to the identity by following trajectories for
shorter times. Hence by the contact isotopy extension theorem (Proposition 6.24),
after shrinking Ut, the maps ft|U−
t
extend to contactomorphisms gt : (∂−W,ξ−)→
(∂−W,~ξ−). Moreover, since f0 = Id we can arrange g0 = Id.
Now we extend the maps Ut∪∂−W → ~Ut∪∂−W given by ft and gt canon-
ically to diﬀeomorphisms ht : W → W mapping φt to ~φt and trajectories of Xt
to trajectories of ~Xt. We have h0 = Id and, again by Lemma 11.4, ht induces
contactomorphisms on all level sets. Hence according to Corollary 12.3, the paths
of Weinstein structures Wt and h∗
t~Wt are homotopic with ﬁxed functions φt and
ﬁxed at t = 0.

270 12. MODIFICATIONS OF WEINSTEIN STRUCTURES
Finally, if Wt =~Wt up to scaling near ∂±W we undo the contact diﬀeotopy ht
on level sets near ∂±W to arrangeht = Id onOp∂±W . Then Corollary 12.3 shows
that the homotopies between Wt andh∗
t~Wt can be chosen ﬁxed up to scaling near
∂±W . Note that in this last step we destroy the property that ht maps trajectories
of Xt to trajectories of ~Xt. □

13
Existence Revisited
In this chapter we prove a more precise version of the Stein Existence Theo-
rem 1.5 by splitting it into two theorems: Theorem 13.1 on the existence of Wein-
stein structures, and Theorem 13.9 on upgrading a Weinstein structure to a Stein
structure. Moreover, we establish the homotopy equivalence between the spaces
of Stein and Weinstein structures with a given function (Theorem 1.2 from the
Introduction).
13.1. Existence of Weinstein structures
The following is the analogue of Theorem 8.17 for Weinstein cobordisms.
Theorem 13.1 (Weinstein existence theorem). Let (W,φ ) be a 2n-dimensional
Morse cobordism such that φ has no critical points of index > n. Let η be a non-
degenerate (not necessarily closed) 2-form on W and Y a vector ﬁeld near ∂−W
such that (η,Y,φ ) deﬁnes a Weinstein structure on Op∂−W . Suppose that either
n> 2, or n = 2 and the contact structure induced by the Liouville form λ =iYη on
∂−W is overtwisted. Then there exists a Weinstein structure (ω,X,φ ) on W with
the following properties:
(i) (ω,X ) = (η,Y ) onOp∂−W ;
(ii) the nondegenerate 2-forms ω and η on W are homotopic relOp∂−W .
Moreover, we can arrange that (ω,X,φ ) is ﬂexible.
Let us point out that Theorem 13.1 does not follow from the Stein Existence
Theorem 8.17 in the case n> 2 because the given Weinstein structure onOp∂−W
need not be Stein. For example, if n > 2 and the induced contact structure on
∂−W is not symplectically ﬁllable, then by Theorem 5.60 the Weinstein structure
onOp∂−W cannot be deformed to a Stein structure.
The following version for manifolds follows directly from Theorem 13.1. Note
that it is also a formal consequence of the Stein Existence Theorem 1.5.
Theorem 13.2. Let (V,φ ) be a 2n-dimensional manifold with an exhausting
Morse function φ that has no critical points of index >n . Let η be a nondegenerate
(not necessarily closed) 2-form on V . Suppose that n > 2. Then there exists a
Weinstein structure (ω,X,φ ) on V such that the nondegenerate 2-forms ω and η
on V are homotopic. Moreover, we can arrange that (ω,X,φ ) is ﬂexible.
The proof of Theorem 13.1 is based on the following special case.
Lemma 13.3. Theorem 13.1 holds for an elementary cobordism.
Proof. The proof follows the same scheme as the proof of Lemma 8.20 in the
Stein case. To simplify the notation, we will assume that φ has a unique critical
271

272 13. EXISTENCE REVISITED
P f1
g−1
1
∆′
∆ ∆1
W \ U
U
Figure 13.1. Deforming the disc ∆ to one which is totally real
and J-orthogonally attached.
pointp. The general case is similar. Let us extend Y to a gradient-like vector ﬁeld
for φ on W and denote by ∆ the stable disc of p.
Step 1. We ﬁrst show that, after a homotopy of (η,Y ) ﬁxed onOp∂−W , we
may assume that ∆ is η-isotropic.
The Liouville form λ = iYη on Op∂−W deﬁnes a contact structure ξ :=
ker(λ|∂−W ) on ∂−W . We choose an auxiliary η-compatible almost complex struc-
ture J on W which preserves ξ and maps Y along ∂−W to the Reeb vector ﬁeld
R of λ|∂−W . We apply Theorem 7.34 to ﬁnd a diﬀeotopy ft : W→ W such that
the disc ∆′ = f1(∆) is J-totally real and J-orthogonally attached to ∂−W . This
is the only point in the proof where the overtwistedness assumption for n = 2 is
needed. Moreover, according to Theorem 7.34, in the case dim ∆ = n we can ar-
range that the Legendrian sphere∂∆′ in (∂−W,ξ ) is loose (meaning that∂−W\∂∆′
is overtwisted in the case n = 2).
Next we modify the homotopy f∗
tJ to keep it ﬁxed near ∂−W . J-orthogonality
implies that ∂∆′ is tangent to the maximal J-invariant subspaceξ⊂T (∂−W ) and
thusλ|∂∆′ = 0. Since the spaces T ∆′ and span{T∂ ∆′,Y} are both totally real and
J-orthogonal to T (∂−W ), we can further adjust the disc ∆′ (keeping∂∆′ ﬁxed) to
make it tangent to Y in a neighborhood of ∂∆′. It follows that we can modify ft
such that it preserves the function φ and the vector ﬁeld Y on a neighborhood U
of ∂−W (extend ft from ∂−W to U using the ﬂow of Y ).
Hence, there exists a diﬀeotopy gt : W → W , t∈ [0, 1], which equals ft on
W\U, the identity onOp∂−W , and preservesφ (but notY !) on U. See Figure 13.1.
Then the diﬀeotopy kt :=f−1
t ◦gt equals the identity on W\U, f−1
t onOp∂−W ,
and preserves φ on all of W . Thus the vector ﬁelds Yt := k∗
tY are gradient-like
for φ = k∗
tφ and coincide with Y on (W\U)∪O p∂−W . The nondegenerate 2-
forms ηt := g∗
tη are compatible with Jt := g∗
tJ and coincide with η onOp∂−W .
Moreover, since ∆′ is J-totally real, the stable disc ∆ 1 :=k−1
1 (∆) = g−1
1 (∆′) of p
with respect to Y1 is J1-totally real and J1-orthogonally attached to ∂−W .
After renaming (η1,Y 1, ∆1) back to (η,Y, ∆), we may hence assume that ∆ is
J-totally real and J-orthogonally attached to ∂−W for some η-compatible almost
complex structure J on W which preserves ξ and maps Y to the Reeb vector ﬁeld
R along ∂−W . In particular, ∂∆ is λ-isotropic and ∆ ∩O p∂−W is η-isotropic.
Since the space of nondegenerate 2-forms compatible with J is contractible, after a
further homotopy of η ﬁxed onOp∂−W and outside a neighborhood of ∆ we may
assume that ∆ is η-isotropic.

13.2. FROM WEINSTEIN TO STEIN: EXISTENCE 273
Step 2. By Lemma 12.16 there exists a homotopy ( ηt,Yt), t∈ [0, 1], of
gradient-like vector ﬁelds for φ and nondegenerate 2-forms on W , ﬁxed on ∆ ∪
Op∂−W and outside a neighborhood of ∆, such that (η0,Y 0) = (η,Y ) and (η1,Y 1)
is Liouville onOp (∂−W∪∆). After renaming (η1,Y 1) back to (η,Y ) we may hence
assume that (η,Y ) is Liouville on a neighborhood U of ∂−W∪ ∆.
Step 3. Using Proposition 9.19 (pushing down along trajectories of Y ),
we construct an isotopy of embeddings ht : W ↪→ W , t∈ [0, 1], with h0 = Id
and ht = Id on Op (∂−W∪ ∆), which preserves trajectories of Y and such that
h1(W )⊂ U. Then ( ηt,Yt) := ( h∗
tη,h∗
tY ) deﬁnes a homotopy of nondegenerate
2-forms and vector ﬁelds on W , ﬁxed onOp (∂−W∪ ∆), from (η0,Y 0) = (η,Y ) to
the Liouville structure (η1,Y 1) =: (ω,X ). Since the Yt are proportional to Y , they
are gradient-like for φ for all t∈ [0, 1].
The Weinstein structure (ω,X,φ ) will be ﬂexible if we choose the stable sphere
∂∆ in Step 1 to be loose, so Lemma 13.3 is proved. □
Proof of Theorem 13.1. We decompose the Morse cobordism M = (W,φ )
into elementary ones, W = W1∪···∪ WN, and inductively apply Lemma 13.3 to
extend the Weinstein structure over W1,...,W N. □
13.2. From Weinstein to Stein: existence
In this section we formulate various theorems about passing from Weinstein to
Stein structures. The proofs of the two main results, Theorems 13.4 and 13.6, are
postponed to Section 13.3 below. Let us point out that all the results in this section
also hold in dimension 4 without further hypotheses.
We begin with the case of cobordisms. Our ﬁrst theorem concerns the passing
from Weinstein to Stein within an ambient complex cobordism.
Theorem 13.4 (ambient Stein existence theorem) . Let W = (W,ω,X,φ ) be a
Weinstein cobordism and J an integrable complex structure on W . Suppose that
onOp∂−W the function φ is J-convex and W coincides with W(J,φ ). Suppose
moreover that J is homotopic rel ∂−W to an almost complex structure compatible
with ω. Then, after target reparametrizing φ, there exists an isotopy ht : W ↪→
W relOp∂−W with h0 = Id such that the function h1∗φ is J-convex, and the
Weinstein structures W(h∗
1J,φ ) and W on W are homotopic rel Op∂−W with
ﬁxed function φ.
Combining this theorem with the existence of complex structures, we obtain
Theorem 13.5 (Stein existence theorem). Let W = (W,ω,X,φ ) be a Weinstein
cobordism which is Stein near ∂−W . Then, after target reparametrizing φ, the
Stein structure on Op∂−W extends to a Stein structure (J,φ ) on W such that the
Weinstein structures W and W(J,φ ) are homotopic rel Op∂−W and with ﬁxed
function φ.
Proof. By assumption W = W(~J,φ ) for a Stein structure (~J,φ ) onOp∂−W .
We extend ~J to an almost complex structure on W compatible with ω. Let L be
the skeleton of W.
By Theorem 8.11, ~J is homotopic relOp∂−W to an almost complex structure
J′ which is integrable on a neighborhoodU of∂−W∪L. By Proposition 9.19, there
exists an isotopy gt : W ↪→ W relOp (∂−W∪L) with g0 = Id and g1(W )⊂ U.
Then J′′ :=g∗
1J′ is a complex structure on W which is homotopic rel Op∂−W to

274 13. EXISTENCE REVISITED
~J. Thus we can apply Theorem 13.4 to ﬁnd a Stein structure ( h∗
1J′′,φ ) on W such
that the Weinstein structures W(h∗
1J′′,φ ) and W are homotopic rel Op∂−W and
with ﬁxed function φ. □
This theorem has the following multi-parametric version, whereDk denotes the
closed k-disc.
Theorem 13.6 (parametric Stein existence theorem). Let Wu = (W,ωu,Xu,φ ),
u∈Dk, k≥ 0, be a family of Weinstein cobordism structures which share the same
Morse functionφ. Suppose Wu is Stein near∂−W for all u, and onW foru∈∂Dk.
Then, after target reparametrizingφ, there exist a family of Stein structures (Ju,φ ),
u∈Dk, extending the given structures near ∂−W and for u∈∂Dk, and a homo-
topy of Weinstein structures Wt,u = (ωt,u,Xt,u,φ ), (t,u )∈ [0, 1]×Dk, such that
W0,u = W(Ju,φ ) and W1,u = Wu for all u∈ Dk, Wt,u = Wu near ∂−W , and
Wt,u = Wu for u∈∂Dk and all t∈ [0, 1].
In order to rephrase this theorem in a more topological way, let us ﬁx a Morse
functionφ :W→ R which has∂±W as regular level sets. We denote by Stein(W,φ )
the space of Stein structures on W with J-lc function φ, and by Weinstein(W,φ )
the space of Weinstein structures onW with functionφ which are Stein near∂−W .
Then Theorem 13.6 implies
Corollary 13.7. The map W : Stein(W,φ )→ Weinstein(W,φ ) is a weak
homotopy equivalence.
See Corollary A.4 for the purely topological argument. In fact, Corollary 13.7
is equivalent to Theorem 13.6 if we drop the condition that homotopies are ﬁxed
near ∂−W .
Corollary 13.7 continues to hold if φ is a generalized Morse function (using our
results about half-discs at embryonic critcal points). The case ∂−W = ∅ is then
Theorem 1.2 from the Introduction.
The preceding theorems have the following analogues for Weinstein/Stein ma-
nifolds, which are derived from the cobordism versions by induction over sublevel
sets as in the proof of Theorem 8.16.
Theorem 13.8. Let W = (V,ω,X,φ ) be a Weinstein manifold. Let J be an
integrable complex structure on V which is homotopic to an almost complex struc-
ture compatible withω. Then there exists an isotopy ht :V ↪→V with h0 = Id such
that the function h1∗φ isJ-convex, and the Weinstein structures W(h∗
1J,φ ) and W
on V are homotopic with ﬁxed function φ.
The following result is Theorem 1.1(a) from the Introduction.
Theorem 13.9. Let W = (V,ω,X,φ ) be a Weinstein manifold. Then there
exists a Stein structure (J,φ ) on W such that the Weinstein structures W and
W(J,φ ) are homotopic with ﬁxed function φ.
Theorem 13.10. Let Wu = (V,ωu,Xu,φ ), u∈ Dk, k ≥ 0, be a family of
Weinstein manifolds which share the same Morse function φ. Suppose Wu is Stein
for u∈ ∂Dk. Then there exist a family of Stein structures (Ju,φ ), u∈ Dk, ex-
tending the given structures for u∈ ∂Dk, and a homotopy of Weinstein struc-
tures Wt,u = (ωt,u,Xt,u,φ ), (t,u )∈ [0, 1]×Dk, such that W0,u = W(Ju,φ ) and
W1,u = Wu for all u∈Dk, and Wt,u = Wu for u∈∂Dk and all t∈ [0, 1].

13.3. PROOF OF THE STEIN EXISTENCE THEOREMS 275
The last theorem can again be formulated in a more topological way. We
ﬁx an exhausting Morse function φ : V → R and denote by Stein(V,φ ) and
Weinstein(V,φ ) the spaces of Stein resp. Weinstein structures on V with function
φ. These spaces are equipped with the topologies explained in Section 11.6. Then,
by Corollary A.4, Theorem 13.10 is equivalent to
Corollary 13.11. The map W : Stein(V,φ ) → Weinstein(V,φ ) is a weak
homotopy equivalence.
13.3. Proof of the Stein existence theorems
In this section we prove Theorems 13.4 and 13.6. The ﬁrst one will be an easy
consequence of the following proposition.
Proposition 13.12. Under the hypotheses of Theorem 13.4 there exists a ho-
motopy of Weinstein structures Wt = (ωt,Xt,φt) on W , t∈ [0, 1], and a regular
value c of the function φ1 with the following properties:
(i) W0 = W, and Wt agrees with W onOp∂−W and up to scaling on
Op∂+W ;
(ii) on W′ ={φ1≤c} the function φ1 is J-convex and W1|W′ = W(J,φ 1);
(iii) on{φ1≥c} the function φ1 has no critical points;
(iv) φt =φ◦ft for a diﬀeotopy ft :W→W ﬁxed onOp∂W with f0 = Id.
Proof. We ﬁrst consider the case of an elementary cobordism. To simplify
the notation, we will assume that there is only one critical pointp∈W ; the general
case diﬀers only in notation. Let ∆ be the stable disc of p. We will construct in 4
steps an elementary Weinstein homotopy Wt and a regular value with properties
(i-iii) such that the φt have ﬁxed values on ∂±W and p. Lemma 9.38 then ensures
the existence of a diﬀeotopy ft as in (iv).
Step 1. After applying Corollary 12.13, we may assume that near p the
function φ is J-convex and W = W(J,φ ). In the following steps we will keep W
ﬁxed onOpp.
Step 2. Choose a homotopyJt relOp (∂−W∪p) of almost complex structures
such that J1 =J and J0 is compatible with ω. Then the disc ∆ is totally real for
J0. Hence, according to Corollary 7.31, there exists a C0-small isotopy ofJt-totally
real discs ∆t, starting with ∆0 = ∆ and ﬁxed on ∆∩Op (∂−W∪p). We extend this
isotopy to a global diﬀeotopy gt :W→W ﬁxed onOp (∂W∪p). After replacing
W by (g1)∗W, we may hence assume that ∆ is totally real for J. Note that ∆ is
also J-orthogonally attached to ∂−W .
Step 3. According to Lemma 8.7, there exists a J-convex function ~φ on
Op (∂−W∪ ∆) which agrees with φ on ∆∪O p (∂−W∪{p}) and such that along ∆
the gradient vector ﬁeld∇J,~φ
~φ equalsX. Next, we use Proposition 12.14 to deform
W relOp (∂W∪p)∪ ∆ to a Weinstein structure ~W which coincides with W(J,~φ)
onOp ∆. After replacing W by~W, we may hence assume that φ is J-convex and
W = W(J,φ ) on a neighborhood U of ∂−W∪ ∆.
Step 4. Finally, we use Theorem 8.5 to construct a deformationφt ofJ-convex
functions on U with the following properties:
• φ0 =φ|U;
• φt is target equivalent to φ near ∂U , and equal to φ on a smaller neigh-
borhood N⊂U of ∂−W∪ ∆;

276 13. EXISTENCE REVISITED
• φt has no critical points besides p;
• some level set{φ1 =c} surrounds ∂−W∪ ∆ in U.
By the second property, near ∂U we have φt =gt◦φ for some increasing function
gt : R→ R. After composing gt with a suﬃciently convex function we may assume
that g′′
t ≥ 0. Moreover, we can arrange gt(x) =ctx +dt for x≥ maxUφ, for some
smooth families of constants ct > 0 and dt. Then near ∂U the Weinstein structure
W(J,φt) has Liouville form
λt =−dφt◦J =−g′
t◦φdφ◦J =ftλ, f t :=g′
t◦φ.
Note that ft satisﬁes
ft +dft(X) =g′
t◦φ +g′′
t◦φdφ (X)> 0.
According to Lemma 12.1, this ensures that ( ftλ,gt◦φ) deﬁnes an extension Wt
of the Weinstein structure W(J,φt) fromU to the whole cobordism W . Near ∂+W
we have ftλ =ctλ, so (ωt,Xt) is ﬁxed up to scaling near ∂+W . Finally, we target
reparametrize φt to make it equal to φ onOp (∂W∪ ∆). This concludes the proof
for the case of an elementary cobordism.
Consider now the case of a general cobordism W . Take an admissible partition
minφ = c0 < c1 <··· < cN = max φ. First we apply the above construction
to deform the Weinstein structure on the elementary cobordism W1 ={φ≤ c1},
keeping it ﬁxed up to scaling on W\W1, such that W1 = W(J,φ 1) onW′
1 ={φ1≤
c}, and the function φ1 has no critical points on W1\W′
1. Then we can apply
again the same construction to the restriction of W1 to the elementary cobordism
W2 ={φ≤c2}\W′
1. Continuing this process we construct the required deformation
on the whole cobordism W . □
Proof of Theorem 13.4. Let Wt = (W,ωt,Xt,φt =φ◦ft) andW′ ={φ1≤
c} be as in Proposition 13.12. Since φ1 has no critical points outside W′, pushing
down along trajectories ofX1 we ﬁnd an isotopygt :W ↪→W relOp∂−W satisfying
g0 = Id, g1(W ) =W′, and φ1◦g−1
t =αt◦φ1|gt(W) for convex increasing functions
αt : R→ R. Set ht := gt◦f−1
t : W ↪→ W . Then J-convexity of φ1|W′ implies
J-convexity ofh1∗φ =φ1◦g−1
1 =α1◦φ1|W′.
It remains to show that W(h∗
1J,φ ) is homotopic rel ∂−W with ﬁxed function
φ to W. To see this, let us write α◦ W := (ω,X,α ◦φ) for a Weinstein structure
W = (ω,X,φ ). Then W(h∗
1J,φ ) is connected to W by the following chain of
homotopies rel ∂−W with ﬁxed function φ:
W(h∗
1J,φ ) =f1∗g∗
1W(J,α 1◦φ1)∼f1∗g∗
1α1◦ W(J,φ 1)
=f1∗g∗
1α1◦ W1
f1∗g∗
tαt◦W1
∼ f∗
1 W1
ft∗Wt
∼ W.
□
Proof of Theorem 13.6. The proof is essentially a k-parametric version of
the proof of Theorem 13.5. However, some care must be taken to make the Stein
family match the given Stein structures on ∂Dk.
Assume ﬁrst that all the Wu are elementary. We reparametrize the family Wu
to make it Stein for u∈O p∂Dk. To simplify notation, let us assume that there is
exactly one critical point p∈ W of φ with Xu-stable discs ∆u. We construct the
desired Weinstein family Wu in the following 3 steps that are similar to steps 1-4
in the proof of Proposition 13.12.

13.3. PROOF OF THE STEIN EXISTENCE THEOREMS 277
Step 1. Pick a family ~Ju, u∈ Dk, of almost complex structures on W
that are compatible with ωu and agree with the given integrable structures on
Op∂−W and for u∈ Op∂Dk. Note that the discs ∆ u are ~Ju-totally real and
~Ju-orthogonally attached. Hence a k-parametric version of Proposition 8.12 yields
a family of integrable complex structures Ju onOp (∂−W∪ ∆u), restricting to the
given structures on Op∂−W and for u∈O p∂Dk, such that ∆u is Ju-totally real
and Ju-orthogonally attached.
Step 2. Next, we use k-parametric versions of Lemma 8.7 and Proposi-
tion 12.14 to deform Wu to a Weinstein family ~Wu = (W,~ωu, ~Xu,~φu), coinciding
with Wu onOp (∂W )∪ ∆u and for u∈O p∂Dk, such that onOp ∆u the function
~φu is Ju-convex and ~Wu = W(Ju,~φu). By Lemma 9.29 we have ~φu◦hu = φ for
diﬀeomorphisms hu :W→W ﬁxed on ∂W . After pulling back ~Wu under hu and
renaming it back to Wu, we may hence assume that Wu = W(Ju,φ ) on a neigh-
borhood Uu of ∂−W∪ ∆u. Since (Ju,φ ) is already Stein for u∈O p∂Dk, we may
choose Uu =W for u∈O p∂Dk.
Step 3. Finally, we use a k-parametric version of Theorem 8.5 to construct
a family ψu, u∈Dk, of Ju-convex functions on Uu with the following properties:
• ψu is target equivalent to φ for u∈∂Dk;
• ψu is target equivalent toφ near∂Uu, and equal to φ on a smaller neigh-
borhood Nu⊂Uu of ∂−W∪ ∆u;
• ψu has no critical points besides p;
• the regular level sets{ψu =c} surround∂−W∪ ∆u inUu and agree with
∂+W for u∈∂Dk.
By Lemma 9.29 there exists a family of diﬀeomorphisms hu : W →{ ψu ≤ c},
ﬁxed on Nu with hu = Id for u∈ ∂Dk, such that ψu◦hu is target equivalent to
φ. After a target reparametrization of φ the desired Stein family is thus (h∗
uJu,φ ).
Since the families of Weinstein structures Wu and W(h∗
uJu,φ ) agree onOp (∂−W∪
∆u), the homotopy rel Op∂−W with ﬁxed function φ between them follows from
Gray’s Stability Theorem 6.23 and Corollary 12.3. This concludes the proof for an
elementary family.
If the Wu are not elementary, we pick regular values
φ|∂−W =c0 <c 1 <··· <c N =φ|∂+W
ofφ such that each (ck−1,ck) contains at most one critical value. Then the restric-
tion of Wu to each cobordism Wk :={ck−1≤ φ≤ ck} is elementary. We apply
steps 1-3 to the restriction of the family Wu to W 1 to construct a Stein family
(W 1,Ju,φ ) extending the given Stein structures onOp∂−W and foru∈∂Dk such
that the Weinstein families Wu|W 1 and W(W 1,Ju,φ ) are connected by a homo-
topy Wt,u, (t,u )∈ [0, 1]×Dk, rel Op∂−W with ﬁxed function φ and ﬁxed on
∂Dk. Using the homotopy Wt,u and Lemma 12.7, we extend W(W 1,Ju,φ ) to a
Weinstein homotopy onW with the same function φ and continue inductively with
W 2,...,W N. □



14
Deformations of Flexible Weinstein Structures
In this chapter we show that ﬂexible Weinstein structures in dimension > 4
are indeed “ﬂexible”: Any Morse homotopy can be followed by a ﬂexible Wein-
stein homotopy, and two ﬂexible Weinstein structures on the same manifold whose
symplectic forms are homotopic as nondegenerate 2-forms are Weinstein homo-
topic. As applications we obtain a Weinstein version of the h-cobordism theorem
(Corollary 14.2), a realization result of isotopy classes of diﬀeomorphisms by sym-
plectomorphisms (Theorem 14.7), and a realization result of pseudo-isotopies by
symplectic pseudo-isotopies (Theorem 14.23). Moreover, in Section 14.4 we prove
the result from [33] that subcritical Weinstein manifolds split as a product with C.
Combining Theorems 13.1, 14.5, and 14.7, we obtain Theorem 1.8 from the
Introduction.
14.1. Homotopies of ﬂexible Weinstein cobordisms
The following Theorems 14.1 and 14.3 are our main results concerning defor-
mations of ﬂexible Weinstein structures.
Theorem 14.1 (ﬁrst Weinstein deformation theorem) . Let W = (W,ω,X,φ )
be a ﬂexible Weinstein cobordism of dimension 2n > 4. Let ψ : W → R be a
Morse function without critical points of index >n . Then there exists a homotopy
Wt = (W,ωt,Xt,φt), t∈ [0, 1], of ﬂexible Weinstein structures, ﬁxed on Op∂−W
and ﬁxed up to scaling on Op∂+W , such that W0 = W and φ1 =ψ.
In particular, we have the following Weinstein version of the h-cobordism the-
orem.
Corollary 14.2 (Weinstein h-cobordism theorem) . Any ﬂexible Weinstein
structure on a product cobordism W =Y× [0, 1] of dimension 2n> 4 is homotopic
to a Weinstein structure (W,ω,X,φ ), where φ : W → [0, 1] is a function without
critical points. □
Theorem 14.3 (second Weinstein deformation theorem). Let W0 = (ω0,X 0,φ 0)
and W1 = (ω1,X 1,φ 1) be two ﬂexible Weinstein structures on a cobordism W of
dimension 2n> 4 which coincide onOp∂−W . Let ηt be a homotopy relOp∂−W of
nondegenerate 2-forms on W connectingω0 and ω1. Then there exists a homotopy
Wt = (ωt,Xt,φt) of ﬂexible Weinstein structures connecting W0 and W1, ﬁxed on
Op∂−W , such that the paths ωt andηt of nondegenerate 2-forms are homotopic rel
Op∂−W with ﬁxed endpoints.
Theorems 14.1 and 14.3 will be proved in Sections 14.2 and 14.3. They have
the following analogues for deformations of ﬂexible Weinstein manifolds, which are
derived from the cobordism versions by induction over sublevel sets as in the proof
of Theorem 8.16 (using Remark 11.25 as the starting point).
279

280 14. DEFORMATIONS OF FLEXIBLE WEINSTEIN STRUCTURES
Theorem 14.4. Let W = (V,ω,X,φ ) be a ﬂexible Weinstein manifold of di-
mension 2n > 4. Let ψ : V → R be a Morse function without critical points of
index >n . Then there exists a homotopy Wt = (V,ωt,Xt,φt), t∈ [0, 1], of ﬂexible
Weinstein structures such that W0 = W and φ1 =ψ.
If the Morse functions φ andψ agree outside a compact set, then the Weinstein
homotopy Wt can be chosen ﬁxed outside a compact set.
Theorem 14.5. Let W0 = (ω0,X 0,φ 0) and W1 = (ω1,X 1,φ 1) be two ﬂexible
Weinstein structures on the same manifold V of dimension 2n > 4. Let ηt be a
homotopy of nondegenerate 2-forms on V connectingω0 and ω1. Then there exists
a homotopy Wt = (ωt,Xt,φt) of ﬂexible Weinstein structures connecting W0 and
W1 such that the paths ωt andηt of nondegenerate 2-forms are homotopic with ﬁxed
endpoints.
Remark 14.6. Theorems 14.1, 14.3, 14.4 and 14.5 remain true in dimension
2n = 4 if we assume the existence of a Morse homotopy φt connecting φ and ψ
(resp. φ0 and φ1) without critical points of index > 1, or without critical points of
index > 2 in the case that ∂−W⁄= ∅ is overtwisted in Theorems 14.1 and 14.3.
Theorem 14.5 has the following consequence for symplectomorphisms of ﬂexible
Weinstein manifolds.
Theorem 14.7. Let W = (V,ω,X,φ ) be a ﬂexible Weinstein manifold of di-
mension 2n >4, and f :V →V a diﬀeomorphism such that f∗ω is homotopic to
ω as nondegenerate 2-forms. Then there exists a diﬀeotopy ft :V →V , t∈ [0, 1],
such that f0 =f, and f1 is an exact symplectomorphism of (V,ω ).
Proof. By Theorem 14.5, there exists a Weinstein homotopy Wt connecting
W0 = W and W1 =f∗W. Thus Corollary 11.21 provides a diﬀeotopy ht :V →V
such thath0 = Id and h∗
1f∗λ−λ is exact, where λ is the Liouville form of W. Now
ft =f◦ht is the desired diﬀeotopy. □
Remark 14.8. Even if W is of ﬁnite type and f = Id outside a compact set,
the diﬀeotopy ft provided by Theorem 14.7 will in general not equal the identity
outside a compact set.
14.2. Proof of the ﬁrst Weinstein deformation theorem
By Corollary 9.52, any two Morse functions without critical points of index>n
on a cobordism of dimension 2n> 4 can be connected by a Morse homotopy without
critical points of index >n . Hence Theorem 14.1 is an immediate consequence the
following
Theorem 14.9. Let W = (W,ω,X,φ ) be a ﬂexible Weinstein cobordism of
dimension 2n. Let φt, t∈ [0, 1], be a Morse homotopy without critical points of
index>n withφ0 =φ andφt =φ near∂W . In the case 2n = 4 assume that either
∂−W is overtwisted, or φt has no critical points of index > 1. Then there exists a
homotopy Wt = (W,ωt,Xt,φt), t∈ [0, 1], of ﬂexible Weinstein structures, starting
at W0 = W, which is ﬁxed near ∂−W and ﬁxed up to scaling near ∂+W .
The proof of Theorem 14.9 is based on the following 3 lemmas.

14.2. PROOF OF THE FIRST WEINSTEIN DEFORMATION THEOREM 281
φ
cN
cj
c1
SN −
j
S1+
j
WN
VN −1
Vj
Wj
Vj−1
V1
W1
Figure 14.1. The partition of W into subcobordisms.
Lemma 14.10. Let W = (W,ω,X,φ ) be a ﬂexible Weinstein cobordism and Y
a gradient-like vector ﬁeld for φ such that the Smale cobordism (W,Y,φ ) is elemen-
tary. Then there exists a family Xt, t∈ [0, 1], of gradient-like vector ﬁelds for φ
and a family ωt, t∈ [0, 1
2], of symplectic forms on W such that
• Wt = (W,ωt,Xt,φ ), t∈ [0, 1
2], is a Weinstein homotopy with W0 = W,
ﬁxed onOp∂−W and ﬁxed up to scaling on Op∂+W ;
• X1 =Y and the Smale cobordisms (W,Xt,φ ), t∈ [ 1
2, 1], are elementary.
Proof. Step 1. Let c1 <··· < cN be the critical values of the function φ.
Set c0 :=φ|∂−W and cN+1 :=φ|∂+W . Choose ε∈ (0, min
j=0,...,N
cj+1−cj
2 ) and deﬁne
Wj :={cj−ε≤φ≤cj +ε}, j = 2,...,N − 1,
W1 :={φ≤c1 +ε}, W N :={φ≥cN−ε},
Vj :={cj +ε≤φ≤cj+1−ε}, j = 1,...,N − 1,
Σ±
j :={φ =cj±ε}, j = 1,...,N,
see Figure 14.1.
Thus we have Σ+
j =∂−Vj =∂+Wj forj = 1,...,N −1 and Σ−
j =∂+Vj =∂−Wj
for j = 2,...,N . We denote by ξ±
j the contact structure induced by the Liouville
form iXω on Σ±
j , j = 1,...,N .

282 14. DEFORMATIONS OF FLEXIBLE WEINSTEIN STRUCTURES
For k ≥ j we denote by Sk−
j the intersection of the union of the Y -stable
manifolds of the critical points on level ck with the hypersurface Σ−
j . Similarly, for
i≤ j we denote by Si+
j the intersection of the union of the Y -unstable manifolds
of the critical points on level ci with the hypersurface Σ +
j , see Figure 14.1. Set
S−
j :=
⋃
k≥j
Sk−
j , S+
j :=
⋃
i≤j
Si+
j .
The assumption that the Smale cobordism ( Y,φ ) is elementary implies that S±
j is
a union of spheres in Σ±
j .
Consider on⋃N
j=1Wj the gradient-like vector ﬁeldsYt := (1−t)Y +tX,t∈ [0, 1],
for φ. Let us pick ε so small that for all t∈ [0, 1] the Yt-unstable spheres in Σ +
j
of the critical points on level cj do not intersect the Y -stable spheres in Σ +
j of any
critical points on higher levels. By Lemma 9.8 we can extend the Yt to gradient-like
vector ﬁelds for φ on W such that Y0 =Y and Yt =Y outsideOp ⋃N
j=1Wj for all
t∈ [0, 1]. By Lemma 9.41, this can be done in such a way that the intersection of
the Yt-stable manifold of the critical point locus on level ci with the hypersurface
Σ+
j remains unchanged. This implies that the cobordisms (W,Yt,φ ) are elementary
for all t∈ [0, 1]. After renaming Y1 back toY and shrinking the Wj, we may hence
assume that Y = X onOp ⋃N
j=1Wj. Moreover, after modifying Y near ∂W we
may assume that Y =X onOp∂W .
We will construct the required homotopies Xt, t∈ [0, 1], and ωt, t∈ [0, 1
2],
separately on each Vj,j = 1,...,N − 1, in such a way that Xt is ﬁxed near ∂Vj for
all t∈ [0, 1] and ωt is ﬁxed up to scaling near ∂Vj for t∈ [0, 1
2]. This will allow us
then to extend the homotopies Xt and ωt to⋃N
j=1Wj as constant, resp. constant
up to scaling.
Step 2. Consider Vj for 1 ≤ j ≤ N− 1. To simplify the notation, we
denote the restriction of objects to Vj by the same symbol as the original objects,
omitting the indexj. Let us denote byX (Vj,φ ) the space of all gradient-like vector
ﬁelds for φ on Vj that agree with X near ∂Vj. We connect X and Y by the path
Yt := (1−t)X +tY inX (Vj,φ ).
Denote by Γ Yt : Σ−
j+1→ Σ+
j the holonomy of the vector ﬁeld Yt on Vj and
consider the isotopy gt := ΓYt|S−
j+1
: S−
j+1 ↪→ Σ+
j . Suppose for the moment that
S−
j+1⊂ Σ−
j+1 is isotropic and loose (this hypothesis will be satisﬁed below when we
perform induction on descending values of j).
Since ΓY0 = ΓX is a contactomorphism, this implies that the embedding g0
is loose isotropic. Hence, by the h-principles in Chapter 7 (Theorem 7.11 for the
subcritical case, Theorem 7.19 for the Legendrian overtwisted case in dimension 4,
and Theorem 7.25 in the Legendrian loose case in dimension 2 n >4), the isotopy
gt can be C0-approximated by an isotropic isotopy. More precisely, there exists a
C0-small diﬀeotopy δt : Σ+
j → Σ+
j with δ0 = Id such that δt◦gt, t∈ [0, 1], is loose
isotropic with respect to the contact structure ξ+
j .
The path ΓYt, t∈ [0, 1], in Diﬀ(Σ−
j+1, Σ+
j ) is homotopic with ﬁxed endpoints
to the concatenation of the paths δt◦ ΓYt (from ΓY0 to δ1◦ ΓY1) and δ−1
t ◦δ1◦ ΓY1
(from δ1◦ ΓY1 to ΓY1). Hence by Lemma 9.41 we ﬁnd paths Y′
t and Y′′
t , t∈ [0, 1],
inX (Vj,φ ) such that

14.2. PROOF OF THE FIRST WEINSTEIN DEFORMATION THEOREM 283
• Y′
0 =X, Y′
1 =Y′′
0 and Y′′
1 =Y ;
• ΓY′
t =δt◦ ΓYt and ΓY′′
t =δ−1
t ◦δ1◦ ΓY1, t∈ [0, 1].
Note that ΓY′
t|S−
j+1
is loose isotropic. Moreover, by choosingδt suﬃcientlyC0-small,
we can ensure that ΓY′′
t (S−
j+1)∩ S+
j = ∅ in Σ+
j and ΓY (S−
j+1) is loose in Σ +
j \ S+
j .
We extend the vector ﬁelds Y′
t and Y′′
t to W by setting Y′
t := (1−t)X +tY and
Y′′
t :=Y onW\Vj. The preceding discussion shows that the cobordisms (W,Y′′
t ,φ )
are elementary for all t∈ [0, 1]. Hence it is suﬃcient to prove the lemma with the
original vector ﬁeld Y replaced by Y′
1 =Y′′
0 . To simplify the notation, we rename
Y′
1 to Y and the homotopy Y′
t to Yt. The new homotopy now has the property
that the isotopy ΓYt|S−
j+1
: S−
j+1 ↪→ Σ+
j is loose isotropic and Γ Y (S−
j+1) is loose in
Σ+
j\S+
j . So the image of ΓY (S−
j+1) under the holonomy of the elementary Weinstein
cobordism (Wj,ω,X = Y,φ ) is loose isotropic in Σ −
j . Since the union S−
j of the
stable spheres of (Wj,Y ) are loose by the ﬂexibility hypothesis on W, this implies
that S−
j ⊂ Σ−
j is loose isotropic.
Now we perform this construction inductively in descending order over Vj for
j = N− 1, N− 2,..., 1, always renaming the new vector ﬁelds back to Y . The
resulting vector ﬁeld Y is then connected to X by a homotopy Yt such that the
manifolds S−
j+1⊂ Σ−
j+1 and the isotopies ΓYt|S−
j+1
: S−
j+1 ↪→ Σ+
j ,t∈ [0, 1], are loose
isotropic for all j = 1,...,N − 1.
Step 3. LetY andYt be as constructed in Step 2. Now we construct the desired
homotopies Xt and ωt separately on each Vj, j = 1,...,N − 1, keeping them ﬁxed
near ∂Vj. We keep the notation from Step 2. By the contact isotopy extension
theorem (Proposition 6.24), we can extend the isotropic isotopy Γ Yt|S−
j+1
: S−
j+1 ↪→
Σ+
j to a contact isotopy Gt : (Σ−
j+1,ξ−
j+1)→ (Σ+
j ,ξ +
j ) starting at G0 = ΓY0 = ΓX.
By Lemma 12.5 we ﬁnd a Weinstein homotopy ~Wt = (Vj,~ωt, ~Xt,φ ) beginning at
~W0 = W with holonomy Γ ~Wt
= Gt for all t∈ [0, 1]. Now Lemma 9.42 provides a
path Xt∈X (Vj,φ ) such that
(i) Xt = ~X2t for t∈ [0, 1
2];
(ii) X1 =Y1 =Y ;
(iii) ΓXt(S−
j+1) = ΓY (S−
j+1) for t∈ [ 1
2, 1].
Over the interval [0, 1
2] the Smale homotopy St = (Vj,Xt,φ ) can be lifted to the
Weinstein homotopy Wt = (Vj,ωt,Xt,φ ), where ωt :=~ω2t.
Condition (iii) implies that ΓXt(S−
j+1)∩S+
j = ∅ for allt∈ [ 1
2, 1], so the resulting
Smale homotopy on W is elementary over the interval [ 1
2, 1]. □
Lemma 14.11. Let W = (W,ω,X,φ ) be a ﬂexible Weinstein cobordism and Y a
gradient-like vector ﬁeld for φ. Suppose that the function φ has exactly two critical
points transversely connected by a unique Y -trajectory. Then there exists a family
Xt, t∈ [0, 1], of gradient-like vector ﬁelds for φ and a family ωt, t∈ [0, 1
2], of
symplectic forms on W such that
• Wt = (W,ωt,Xt,φ ), t∈ [0, 1
2], is a homotopy with W0 = W, ﬁxed on
Op∂−W and ﬁxed up to scaling on Op∂+W ;
• X1 = Y and for t∈ [ 1
2, 1] the critical points of the function φ are con-
nected by a unique Xt-trajectory.

284 14. DEFORMATIONS OF FLEXIBLE WEINSTEIN STRUCTURES
Proof. Let us denote the critical points of the function φ by p1 and p2 and
the corresponding critical values by c1 < c2. As in the proof of Lemma 14.10, for
suﬃciently small ε> 0 we split the cobordism W into three parts:
W1 :={φ≤c1 +ε}, V :={c1 +ε≤φ≤c2−ε}, W 2 :={φ≥c2−ε}.
Arguing as in Step 1 of the proof of Lemma 14.10 we reduce to the case thatY =X
onOp (W1∪W2).
On V consider the gradient-like vector ﬁelds Yt := (1−t)X +tY for φ. Let
Σ :={φ = c1 +ε} = ∂−V . Denote by St⊂ Σ the Yt-stable sphere of p2 and by
S+⊂ Σ the Y -unstable sphere of p1. Note that S+ is coisotropic, S0 is isotropic,
and S1 intersects S+ transversely in a unique point q. We deform S1 to S′
1 by
a C0-small deformation, keeping the unique transverse intersection point q with
S+, such that S′
1 is isotropic near q. Connect S0 to S′
1 by an isotopy S′
t which is
C0-close toSt. Due to the ﬂexibility hypothesis on W, the isotropic sphereS′
0 =S0
is loose. Hence by Theorems 7.11, 7.19 and 7.25 we can C0-approximateS′
t by an
isotropic isotopy ~St such that ~S0 = S′
0 = S0, and ~S1 coincides with S′
1 near q. In
particular, ~S1 has q as the unique transverse intersection point with S+. Arguing
as in Steps 2 and 3 of the proof of Lemma 14.10, we now construct a Weinstein
homotopy Wt = (V,ωt,Xt,φ ), t∈ [0, 1
2], ﬁxed near ∂−V and ﬁxed up to scaling
near ∂+V , and Smale cobordisms (V,Xt,φ ), t∈ [ 1
2, 1], ﬁxed near ∂V , such that
• W0 = W|V and X1 =Y|V ;
• the Xt-stable sphere of p2 in Σ equals ~S2t for t ∈ [0, 1
2], and ~S1 for
t∈ [ 1
2, 1].
In particular, fort∈ [ 1
2, 1] theXt-stable sphere ofp2 in Σ intersectsS+ transversely
in the unique point q, so the two critical points p1,p 2 are connected by a unique
Xt-trajectory for t∈ [ 1
2, 1]. □
The following lemma will serve as induction step in proving Theorem 14.9.
Lemma 14.12. Let W = (W,ω,X,φ ) be a ﬂexible Weinstein cobordism of di-
mension 2n. Let St = (W,Yt,φt), t∈ [0, 1], be an elementary Smale homotopy
without critical points of index > nsuch that φ0 = φ on W and φt = φ near ∂W
(but not necessarily Y0 =X!). If 2n = 4 and St is of type IIb assume that either
∂−W is overtwisted, or φt has no critical points of index > 1. Then there exists a
homotopy Wt = (W,ωt,Xt,φt), t∈ [0, 1], of ﬂexible Weinstein structures, starting
at W0 = W, which is ﬁxed near ∂−W and ﬁxed up to scaling near ∂+W .
Proof. Type I. Consider ﬁrst the case when the homotopy St is elementary
of type I. We point out that (W,X,φ ) need not be elementary. To remedy this, we
apply Lemma 14.10 to construct families Xt and ωt such that
• Wt = (W,ωt,Xt,φ ), t∈ [0, 1
2], is a Weinstein homotopy with W0 = W,
ﬁxed onOp∂−W and ﬁxed up to scaling on Op∂+W ;
• X1 =Y0 and the Smale cobordisms (W,Xt,φ ),t∈ [ 1
2, 1], are elementary.
Thus it is suﬃcient to prove the lemma for the Weinstein cobordism ( ω 1
2
,X 1
2
,φ )
instead of W, and the concatenation of the Smale homotopies ( Xt,φ )t∈[ 1
2,1] and
(Yt,φt)t∈[0,1] instead of (Yt,φt). To simplify the notation we rename the new Wein-
stein cobordism and Smale homotopy back to W = (ω,X,φ ) and (Yt,φt). So in the
new notation we now have X =Y0.

14.2. PROOF OF THE FIRST WEINSTEIN DEFORMATION THEOREM 285
According to Lemma 9.39 there exists a family ~φt, t ∈ [0, 1], of Lyapunov
functions for X with the same proﬁle as the family φt, and such that ~φ0 = φ
and ~φt = φt onOp∂W . Then Lemma 9.38 provides a diﬀeotopy ht : W → W ,
t∈ [0, 1], such that h0 = Id, ht|Op∂W = Id, and φt =~φt◦ht for all t∈ [0, 1]. Thus
the Weinstein homotopy (W,ωt = h∗
tω,Xt = h∗
tX,φt = h∗
t~φt), t∈ [0, 1], has the
desired properties. It is ﬂexible because the Xt-stable spheres in ∂−W are loose for
t = 0 and moved by an isotropic isotopy, so they remain loose for all t∈ [0, 1].
Type IId. Suppose now that the homotopy St is of type IId. Let t0∈ [0, 1]
be the parameter value for which the function φt has a death-type critical point.
In this case the function φ has exactly two critical points p and q connected by a
unique Y0-trajectory. Arguing as in the type I case, using Lemma 14.11 instead of
Lemma 14.10, we can again reduce to the case that X =Y0.
Then Proposition 12.22 provides an elementary Weinstein homotopy (W,ω, ~Xt,~φt)
of type IId starting from W and killing the critical points p and q at time t0. One
can also arrange that ( ~Xt,~φt) coincides with ( X,φ ) onOp∂W , and (by compos-
ing ~φt with suitable functions R→ R) that the homotopies ~φt and φt have equal
proﬁles. Then Lemma 9.38 provides a diﬀeotopy ht :W→W , t∈ [0, 1], such that
h0 = Id, ht|Op∂W = Id, and φt = ~φt◦ht for all t∈ [0, 1]. Thus the Weinstein ho-
motopy (W,ωt =h∗
tω,Xt =h∗
t ~X,φt =h∗
t~φt), t∈ [0, 1], has the desired properties.
It is ﬂexible because the intersections of the Xt-stable manifolds with regular level
sets remain loose for t∈ [0,t 0] and there are no critical points for t>t 0.
Type IIb. The argument in the case of type IIb is similar, except that we use
Proposition 12.21 instead of Proposition 12.22 and we do not need a preliminary
homotopy. However, the ﬂexibility ofWt fort≥t0 requires an additional argument.
Consider ﬁrst the case 2 n >4. Suppose φ1 has critical points p and q of in-
dexn andn− 1, respectively (if they have smaller indices ﬂexibility is automatic).
Then the closure ∆ of the X1-stable manifold of the point p intersects∂−W along
a Legendrian disc ∂−∆, see Figure 9.5. The boundary S−
q of this disc is the inter-
section with ∂−W of the X1-stable manifold D−
q of q. According to Remark 7.22
(2) all Legendrian discs are loose, or more precisely,∂−∆\S−
q is loose in∂−W\S−
q .
Let c be a regular value of φ1 which separates φ1(q) and φ1(p) and consider the
level set Σ :={φ1 =c}. Flowing along X1-trajectories deﬁnes a contactomorphism
∂−W\S−
q → Σ\D+
q mapping ∂−∆\S−
q onto ∆∩ Σ\{r}, where r is the unique
intersection point of ∆ and the X1-unstable manifold D+
q in the level set Σ. It
follows that ∆∩ Σ\{r} is loose in Σ \{r}, and hence ∆ ∩ Σ is loose in Σ. This
proves ﬂexibility of W1, and thus of Wt for t≥t0.
Finally, consider the case 2 n = 4. If the critical points have indices 1 and 0
ﬂexibility is automatic. If they have indices 2 and 1 and ∂−W is overtwisted we
can arrange that ∂−∆⊂ ∂−W (in the notation above) has an overtwisted disc
in its complement, hence so does the intersection of ∆ with the regular level set
{φ =c}. □
Proof of Theorem 14.9. Let us pick gradient-like vector ﬁelds Yt for φt
with Y0 = X and Yt = X near ∂W to get a Smale homotopy St = (W,Yt,φt),
t∈ [0, 1]. By Lemma 9.37 we ﬁnd an admissible partition for the Smale homotopy
St. Thus we get a sequence 0 = t0 < t1 <··· < tp = 1 of parameter values and

286 14. DEFORMATIONS OF FLEXIBLE WEINSTEIN STRUCTURES
smooth families of partitions
W =
Nk⋃
j=1
Wk
j (t), W k
j (t) :={ck
j−1(t)≤φt≤ck
j (t)}, t ∈ [tk−1,tk]
such that each Smale homotopy
Sk
j :=
(
Wk
j (t),Yt|Wk
j (t),φt|Wk
j (t)
)
t∈[tk−1,tk]
is elementary. We will construct the Weinstein homotopy (ωt,Xt,φt) on the cobor-
disms ⋃
t∈[tk−1,tk]Wk
j (t) inductively over k = 1,...,p , and for ﬁxed k over j =
1,...,N k.
Suppose the required Weinstein homotopy is already constructed on W for
t≤tk−1. To simplify the notation we rename φtk−1 toφ, the vector ﬁelds Xtk and
Ytk toX andY , and the symplectic formωtk−1 toω. We also writeN instead ofNk,
Wj and Wj(t) instead of Wk
j (tk−1) and Wk
j (t), and replace the interval [ tk−1,tk]
by [0, 1].
There exists a diﬀeotopy ft :W→W , ﬁxed onOp∂W , with f0 = Id and such
that ft(Wj) =Wj(t) for all t∈ [0, 1]. Moreover, we can choose ft and a diﬀeotopy
gt : R→ R with g0 = Id such that the function ˆφt :=gt◦φt◦ft coincides with φ
onOp∂Wj for all t∈ [0, 1], j = 1,...,N . Set ˆYt := f∗
tYt. So we have a ﬂexible
Weinstein cobordism W = (W =⋃N
j=1Wj,ω,X,φ = ˆφ0) and a Smale homotopy
(ˆYt,ˆφt), t∈ [0, 1], whose restriction to each Wj is elementary. (But the restriction
of W to Wj need not be elementary.)
Now we apply Lemma 14.12 inductively forj = 1,...,N to construct Weinstein
homotopies ˆWj
t = (Wj,ˆωt, ˆXt,ˆφt), ﬁxed near ∂−Wj and ﬁxed up to scaling near
∂+Wj, withˆWj
0 = W|Wj. Thus the Wj
t ﬁt together to form a Weinstein homotopy
ˆWt = (ˆωt, ˆXt,ˆφt) on W . The desired Weinstein homotopy on W is now given by
Wt :=
(
ft∗ˆωt,ft∗ˆXt,g−1
t ◦ˆφt◦f−1
t
)
.
□
14.3. Proof of the second Weinstein deformation theorem
Theorem 14.3 is an immediate consequence of Corollary 9.52 and the following
Theorem 14.13. Let W0 = (ω0,X 0,φ 0) and W1 = (ω1,X 1,φ 1) be two ﬂexible
Weinstein structures on a cobordism W of dimension 2n. Let φt, t∈ [0, 1], be a
Morse homotopy without critical points of index >n connectingφ0 and φ1. In the
case 2n = 4 assume that either ∂−W is overtwisted, or φt has no critical points
of index > 1. Let ηt, t∈ [0, 1], be a homotopy of nondegenerate (not necessarily
closed) 2-forms connecting ω0 and ω1 such that (ηt,Yt,φt) is Weinstein near ∂−W
for a homotopy of vector ﬁelds Yt onOp∂−W connectingX0 and X1.
Then W0 and W1 can be connected by a homotopy Wt = (ωt,Xt,φt), t∈ [0, 1],
of ﬂexible Weinstein structures, agreeing with (ηt,Yt,φt) onOp∂−W , such that the
paths of nondegenerate 2-forms t↦→ ηt and t↦→ ωt, t∈ [0, 1], are homotopic rel
Op∂−W with ﬁxed endpoints.
Let us extend the vector ﬁelds Yt fromOp∂−W to a path of gradient-like
vector ﬁelds for φt on W connecting X0 and X1. We will deduce Theorem 14.13

14.3. PROOF OF THE SECOND WEINSTEIN DEFORMATION THEOREM 287
from Theorem 14.9 and the following special case, which is just a 1-parametric
version of the Weinstein Existence Theorem 13.1.
Lemma 14.14. Theorem 14.13 holds under the additional hypothesis thatφt =φ
is independent of t∈ [0, 1] and the Smale homotopy (W,Yt,φ ) is elementary.
Proof. The proof is just a 1-parametric version of the proof of Lemma 13.3,
using Theorem 7.36 and Lemma 12.17 instead of Theorem 7.34 and Lemma 12.16.
□
Lemma 14.15. Theorem 14.13 holds under the additional hypothesis thatφt =φ
is independent of t∈ [0, 1].
Proof. Let us pick regular values
φ|∂−W =c0 <c 1 <··· <c N =φ|∂+W
such that each (ck−1,ck) contains at most one critical value. Then the restriction
of the homotopy (Yt,φ ), t∈ [0, 1], to each cobordism Wk :={ck−1≤ φ≤ ck} is
elementary.
We apply Lemma 14.14 to the restriction of the homotopy ( ηt,Yt,φ ) to W 1.
Hence W0|W 1 and W1|W 1 are connected by a homotopyW1
t = (ω1
t,X 1
t,φ ),t∈ [0, 1],
of ﬂexible Weinstein structures on W 1, agreeing with (ηt,Yt,φt) onOp∂−W , such
that the paths t↦→ω1
t and t↦→ηt, t∈ [0, 1], of nondegenerate 2-forms on W 1 are
connected by a homotopy ηs
t , s,t ∈ [0, 1] rel Op∂−W with ﬁxed endpoints. We
use the homotopy ωs
t to extend ω1
t to nondegenerate 2-forms η1
t on W such that
η1
0 =ω0,η1
1 =ω1,η1
t =ηt outside a neighborhood of W 1, and the pathst↦→η1
t and
t↦→ηt, t∈ [0, 1], of nondegenerate 2-forms on W are homotopic relOp∂−W with
ﬁxed endpoints. By Lemma 9.8, we can extend X1
t to gradient-like vector ﬁeldsY 1
t
for φ on W such that Y 1
0 = X0 and Y 1
1 = X1. Now we can apply Lemma 14.14
to the restriction of the homotopy (η1
t,Y 1
t ,φ ) to the elementary cobordism W 2 and
continue inductively to construct homotopies (ηk
t,Y k
t ,φ ) onW which are Weinstein
on Wk, so (ηN
t ,Y N
t ,φ ) is the desired Weinstein homotopy. Note that ( ηN
t ,Y N
t ,φ )
is ﬂexible because its restriction to each Wk is ﬂexible. □
Proof of Theorem 14.13. Let us reparametrize the given homotopy (ηt,Yt,
φt), t∈ [0, 1], to make it constant for t∈ [ 1
2, 1]. After pulling back ( ηt,Yt,φt)
by a diﬀeotopy and target reparametrizing φt, we may further assume that φt is
independent of t onOp∂W .
By Theorem 14.9, W0 can be extended to a homotopy Wt = (ωt,Xt,φt),
t∈ [0, 1
2], of ﬂexible Weinstein structures on W , ﬁxed onOp∂−W . We modify Wt
using Lemma 12.7 (i) to make it agree with (ηt,Yt,φt) onOp∂−W . Note that W 1
2
and W1 share the same function φ 1
2
= φ1. We connect ω 1
2
and ω1 by a path η′
t,
t∈ [ 1
2, 1] of nondegenerate 2-forms by following the path ωt backwards and thenηt
forwards. Since ωt = ηt onOp∂−W for t∈ [0, 1
2], we can modify the path η′
t to
make it constant equal to ω 1
2
= ω1 onOp∂−W . By Lemma 9.8, we can connect
X 1
2
andX1 by a homotopy Y′
t ,t∈ [ 1
2, 1], of gradient-like vector ﬁelds for φ1 which
agree with X 1
2
=X1 onOp∂−W .
So we can apply Lemma 14.15 to the homotopy ( η′
t,Y′
t,φ 1), t∈ [ 1
2, 1]. Hence
W 1
2
and W1 are connected by a homotopy Wt = (ωt,Xt,φ 1), t∈ [ 1
2, 1], of ﬂexible
Weinstein structures, agreeing with ( ω1,X 1,φ 1) onOp∂−W , such that the paths

288 14. DEFORMATIONS OF FLEXIBLE WEINSTEIN STRUCTURES
of nondegenerate 2-forms t↦→ωt and t↦→η′
t, t∈ [ 1
2, 1], are homotopic relOp∂−W
with ﬁxed endpoints. It follows from the deﬁnition of η′
t that the concatenated
path ωt, t∈ [0, 1], is homotopic to ηt, t∈ [0, 1]. Thus the concatenated Weinstein
homotopy Wt, t∈ [0, 1], has the desired properties. □
14.4. Subcritical Weinstein manifolds are split
In this section we prove the following theorem which asserts that subcritical
Weinstein manifolds split as a product with C (see Section 11.8 for the deﬁnitions).
We call two Weinstein manifolds (or cobordisms) W = (V,ω,X,φ ) and W′ =
(V′,ω′,X′,φ′) deformation equivalent if there exists a diﬀeomorphism h :V →V′
such that h∗W′ is homotopic to W. See Chapter 16 for more discussion of this
notion.
Theorem 14.16 ([ 33]). Every subcritical Weinstein manifold (V,ω,X,φ ) of
dimension 2n is deformation equivalent to the stabilization of a Weinstein manifold
(V′,ω′,X′,φ′) of dimension 2n− 2.
Remark 14.17. Theorem 14.16 implies by induction: If a 2n-dimensional Wein-
stein manifold (V,ω,X,φ ) is k-subcritical, i.e., all critical points of φ have index
≤n−k, then it is deformation equivalent to the k-fold stabilization of a Weinstein
manifold (V′,ω′,X′,φ′) of dimension 2(n−k).
Example 14.18. Consider an oriented real plane bundle V′ → S2 of even
Euler number e∈ 2Z. Then V :=V′× C∼=S2× C2 carries a subcritical Weinstein
structure with trivial ﬁrst Chern class which is unique up to homotopy. On the
other hand, V′ carries a Weinstein structure (which can be chosen to have trivial
ﬁrst Chern class) if and only if e≤− 2 ([125], see also Section 16.3 below). This
shows that not every smooth splittingV =V′×C gives rise to a Weinstein splitting,
and the diﬀeomorphism type of the manifold V′ in a Weinstein splitting ofV is not
uniquely determined.
The proof of Theorem 14.16 uses the following lemma.
Lemma 14.19. Let V be a smooth orientable manifold of dimension 2n and
V′⊂V a codimension 2 submanifold with trivial normal bundle. Let φ :V → R be
an exhausting Morse function and X a gradient-like vector ﬁeld for φ such that the
vector ﬁeldX is tangent to V′, and all critical points of φ and their stable manifolds
are contained in V′.
Then there exists a diﬀeomorphism f :V′× R2→V such that f(x′, 0) =x′ for
all x′∈V′, and φ◦f(x′,u ) =φ(x′) +|u|2 for all x′∈V′, u∈ R2.
Proof. Since V′ has trivial normal bundle, we can ﬁnd an embedding V′×
R2 ↪→ V mapping (x′, 0) to x′ for all x′∈ V′. We will view V′× R2 as a subset
of V via this embedding. We can choose the embedding such the function φ′ :
V′× R2→ R, φ′(x′,u ) := φ(x′) +|u|2 satisﬁes φ′(x′,u )≥ φ(x′,u ) for all ( x′,u ).
Fix the gradient-like vector ﬁeld X′ :=X|V′ +u∂u for φ′ on V′× R2.
By assumption, the functions φ : V → R and φ′ : V′× R2 → R have the
same critical points and stable manifolds (with respect to X resp. X′), and the
same values at critical points. Pick an unbounded sequence of regular values c0 <
minφ < c1 <··· such that the Smale cobordisms ( Wj :={cj−1≤ φ≤ cj},X,φ )
and (W′
j := {cj−1 ≤ φ′ ≤ cj},X′,φ′) are elementary. Since φ′ ≥ φ we have
V′
j :=⋃j
i=1W′
j⊂Vj :=⋃j
i=1Wj for all j.

14.4. SUBCRITICAL WEINSTEIN MANIFOLDS ARE SPLIT 289
We will inductively modify the embedding V′× R2 ↪→V such that φ′ =φ on
V′
j = Vj. For j = 1 this can be done by the Morse Lemma 9.1 and Remark 9.2.
Now suppose we already haveφ′ =φ onV′
j−1 =Vj−1. Applying Lemma 9.29 to the
cobordismsW′
j⊂Wj, we ﬁnd an isotopyht :Wj ↪→Wj,t∈ [0, 1], withh0 = Id and
ht = Id onOp (∂−Wj), such that h1(Wj) =W′
j and φ =φ′◦h1 on Wj. Moreover,
since X = X′ on V′∩Wj, the proof of Lemma 9.29 (which maps X-trajectories
to X′-trajectories) yields ht = Id on V′∩Wj. We extend ht to diﬀeomorphisms
ht : V → V which equal the identity on Vj−1 and outside a neighborhood of Vj.
Then fj := h−1
1 |V′×R2 : V′× R2 ↪→ V is the desired new embedding satisfying
φ′ =φ◦fj on Vj =fj(V′
j ).
Since the sequence of embeddings stabilizes on each V′
j , it converges as j→∞
to a diﬀeomorphism f : V′× R2→ V satisfying f(x′, 0) = x′ for all x′∈ V′ and
φ◦f =φ′. □
Using this lemma, we now prove the following purely topological analogue of
Theorem 14.16.
Proposition 14.20. Let V be a smooth orientable manifold of dimension 2n
which admits an exhausting Morse function φ without critical points of index ≥
n. Then there exists a codimension 2 properly embedded submanifold V′ ⊂ V
and a diﬀeomorphism V′× R2→ V such that f(x′, 0) = x′ for all x′∈ V′, and
φ◦f(x′,u ) =φ(x′) +|u|2 for all x′∈V′, u∈ R2.
Proof of Proposition 14.20. Let X0 be any gradient-like vector ﬁeld for
the function φ. We slice V into elementary Smale cobordisms (Wj :={cj−1≤φ≤
cj},φ|Wj,X|Wj), j∈ N, where c0 < minφ < c1 <··· are regular values of φ. We
will inductively construct codimension 2 submanifolds V′
j ⊂ Vj := ⋃j
i=1Wi and
gradient-like vector ﬁelds Xj on V for φ satisfying the following conditions:
(i) V′
j⊂Vj has trivial normal bundle;
(ii) the vector ﬁeld Xj is tangent to V′
j ;
(iii) all critical points of φ and their stable manifolds are contained in V′
j ;
(iv) the pair ( ∂Vj,∂V ′
j ) is (n− 2)-connected;
(v) V′
j∩Vj−1 =V′
j−1 and Xj|Vj−1 =Xj−1 for all j≥ 1.
Then, by the last property, the V′
j and Xj stabilize on each compact set and thus
converge to a codimension 2 submanifold V′⊂ V and a gradient-like vector ﬁeld
X for φ satisfying the hypotheses of Lemma 14.19, and the conclusion follows.
To simplify the notation, we will assume that each elementary cobordism Wj
contains exactly one critical point pj of the function φ.
By the Morse Lemma, the function φ has the form ∑n
i=1(x2
i +y2
i ) for some
local coordinates near the minimum p1. We deform X0 to a gradient-like vector
ﬁeld X1 for φ which agrees with X0 outside V1 and equals ∑n
i=1(xi ∂
∂xi
+yi ∂
∂yi
)
near p1. We deﬁne V′
1 as the union of all trajectories of X1 in V1 which near p1 lie
in the subspace{xn =yn = 0}. Then V′
1 is a codimension 2 equatorial ball in the
2n-dimensional ball V1. In particular, the pair ( ∂V1,∂V ′
1) is (n− 2)-connected.
Now suppose we already have constructedV′
j−1⊂Vj−1 andXj−1 satisfying the
above conditions. Pick a trivialization of the normal bundle of V′
j−1 inVj−1. Let k
be the index of the critical point pj∈Wj. By assumption, we have k≤n− 1. The
stable manifold of pj intersects∂Vj−1 along a sphere S of dimension k− 1≤n− 2.
Since the pair (∂Vj−1,∂V ′
j−1) is (n− 2)-connected by the induction hypothesis, the

290 14. DEFORMATIONS OF FLEXIBLE WEINSTEIN STRUCTURES
sphere S is homotopic to a sphere in ∂V′
j−1. By a general position argument using
the dimensional constraint dim S≤ n− 2 it is, in fact, isotopic to an embedded
sphere S′⊂∂V′
j−1.
In some local coordinate neighborhood U of pj the function φ has the form
−∑k
1x2
i +∑n
k+1x2
i +∑n
1y2
i . Using Lemma 9.46, we deform Xj−1 inside Wj to a
gradient vector ﬁeld Xj for φ which equals−∑k
1xi ∂
∂xi
+∑n
k+1xi ∂
∂xi
+∑n
1yi ∂
∂yi
near pj, and for which the stable disc of pj is attached to ∂Vj−1 along the sphere
S′.
Next we adjust the normal framings. For small ε > 0 consider the local hy-
persurface Σε :={∑k
1x2
i = ε, ∑n
k+1x2
i +∑n
1y2
i < ε}. Following ﬂow lines of
Xj backwards we obtain an embedding Σ ↪→ ∂Vj−1 mapping Sε :={∑k
1x2
i =
ε, ∑n
k+1x2
i +∑n
1y2
i = 0} ontoS′. Its diﬀerential Φ maps the normal (2n−k)-frame
∂xk+1,...,∂ xn,∂y1,...,∂ yn toSε in Σε onto a normal frame toS′ in∂Vj−1. Since by
Corollary A.10 the homomorphismι∗ :πk−1(SO2n−k−2)→πk−1(SO2n−k) is surjec-
tive fork≤n−1, we can deform Φ such that it maps∂xk+1,...,∂ xn−1,∂y1,...,∂ yn−1
to T (∂V′
j−1) and ∂xn,∂yn to the given normal framing to V′
j−1. Note that here we
are making a choice if the homomorphism ι∗ is not injective: we can change the
resulting normal framing of S′ in ∂V′
j−1 by any element in kerι∗.
After matching the normal framings, by further deformingXj insideWj we can
now arrange that the imageU′ ofU∩{xn =yn = 0} under the backward ﬂow ofXj
intersects∂Vj−1 in ∂V′
j−1, and the given normal framing to V′
j−1 extends over U′.
Hence the union V′
j ⊂ Vj of the unstable disc of pj in Wj with the image of V′
j−1
under the forward ﬂow of Xj is a smooth codimension 2 submanifold satisfying
conditions (i-iii) and (v).
It remains to verify that the pair (∂Vj,∂V ′
j ) is (n−2)-connected. Recall that the
pair (∂Vj,∂V ′
j ) is obtained from the pair (∂Vj−1,∂V ′
j−1) by a simultaneous surgery
of index k≤n− 1 along a (k− 1)-dimensional sphere S′⊂∂V′
j−1. Pick a tubular
neighborhood pair (N,N′) forS in (∂Vj−1,∂V ′
j−1) such thatN′ =N∩∂V′
j−1, thus
(N,N′) is diﬀeomorphic to Sk−1× (D2n−k,D 2n−k−2). We deﬁne the complement
(L,L′) := (∂Vj−1,∂V ′
j−1)\ Int (N,N′)⊂ and denote its image in (∂Vj,∂V ′
j ) under
the forward ﬂow ofXj also by (L,L′). Then (M,M′) := (∂Vj,∂V ′
j )\ Int (L,L′) is a
tubular neighborhood pair for the unstable sphere if pj in (∂Vj,∂V ′
j ) and thus dif-
feomorphic toDk×(S2n−k−1,S 2n−k−3). Hence, (M∪L,M′∪L′) = (∂Vj,∂V ′
j ) and
(M∩L,M′∩L′) is diﬀeomorphic toSk−1×(S2n−k−1,S 2n−k−3). Next observe that
the removal of (N,N′) from (∂Vj−1,∂V ′
j−1) did not aﬀect its (n− 2)-connectedness
because the codimension of S′ in ∂Vj−1 and ∂V′
j−1 is >n − 1. Therefore, the pair
(L,L′) is (n− 2)-connected. Clearly, ( M,M′) and (M∩L,M′∩L′) are (n− 2)-
connected as well. Now the relative Mayer-Vietoris sequence (see [91]) implies that
(M∪L,M′∪L′) has vanishing homology up to degree n− 2, while van Kam-
pen’s theorem implies the triviality of π1(M∪L,M′∪L′). Hence by the relative
Hurewicz theorem (see [ 91]) we conclude that ( ∂Vj,∂V ′
j ) = (M∪L,M′∪L′) is
(n− 2)-connected.
This concludes the induction step and hence the proof of Proposition 14.20. □
The ﬁnal ingredient in the proof of Theorem 14.16 is the following homotopical
lemma.

14.4. SUBCRITICAL WEINSTEIN MANIFOLDS ARE SPLIT 291
Lemma 14.21. LetV be a non-compact 2n-dimensional orientable manifold and
V′⊂V be a properly embedded orientable codimension 2 submanifold which has no
closed components. Then every nondegenerate (not necessarily closed) 2-formω on
V is homotopic to a a nondegenerate 2-form ω′ such that ω′|TV′ is nondegenerate.
Proof. A homotopically equivalent problem is making a codimension two ori-
entable submanifold V′ of an almost complex manifold an almost complex subma-
nifold by deforming the almost complex structure. This is, in turn, equivalent to
the problem of rotating the 2-dimensional normal bundle to V′ in V to a complex
1-dimensional subbundle. Note that the assumption that V′ has no closed compo-
nents implies that it has the homotopy type of a (2n−3)-dimensional cell complex.
Hence, arguing inductively over the cells of a cell decomposition of V′, we come
to the following problem. Given two vector ﬁelds e1,e 2 normal to V′ over a k-cell
D⊂V′, k≤ 2n− 3, such that Je1 =e2 over∂D, we need to homotope the vector
ﬁeld e2 relative to ∂D to the vector ﬁeld Je1, keeping it orthogonal to e1. But the
obstruction to doing this lies in πkS2n−2 = 0 for k≤ 2n− 3. □
Proof of Theorem 14.16. Suppose ﬁrst that n >3. Let W = (V,ω,X,φ )
be a subcritical Weinstein manifold of dimension 2 n. According to Proposition
14.20, the manifold V is diﬀeomorphic to a product V′× R2, where V′ admits an
exhausting function~φ without critical points of index≥n. By Lemma 14.21 we ﬁnd
a non-degenerate 2-form ω′ onV =V′× R2 which is homotopic to ω through non-
degenerate 2-forms such that ω′|TV′ is non-degenerate. Since dim V′ = 2n− 2> 4,
we can use Theorem 13.2 to construct onV′ a Weinstein structure~W = (V′,~ω, ~X,~φ)
such that~ω andω′|V′ are homotopic as non-degenerate 2-forms. Now Theorem 14.5
provides a Weinstein homotopy on V connecting the subcritical Weinstein struc-
tures W and the stabilization of the Weinstein structure ~W. Then, according to
Proposition 11.8 the underlying symplectic manifolds are symplectomorphic.
The previous argument breaks down for n = 3 because then we cannot apply
Theorem 13.2 to ﬁnd a Weinstein structure on the 4-manifold V′. Indeed, the
submanifold V′ ⊂ V provided by Proposition 14.20 may not carry a Weinstein
structure, see Example 14.18 above. However, we can ﬁnd in this case a diﬀerent
submanifold which carries a Weinstein structure. To do this, we inductively con-
struct V′⊂V together with its Weinstein structure as follows, see [ 33] for details.
Consider the extension fromV′
j−1 toV′
j in the critical casek = ind(pj) = 2 in which
we cannot apply Theorem 13.1 to extend the Weinstein structure toV′
j . The reason
is that the stabilization construction in Proposition 7.12 only provides Legendrian
regular homotopies of the attaching sphere S′ with positive self-intersection index.
Recall, however, that in the construction of V′
j in the proof of Proposition 14.20 we
have the freedom to change the normal framing ofS′ in∂V′
j−1 by an element in the
kernel of the homomorphismι∗ :πk−1(SO2n−k−2)→πk−1(SO2n−k). In the present
case n = 3, k = 2 this is the canonical projection π1(SO2)∼= Z→ π1(SO4)∼= Z2
and thus kerι∗ = 2Z. So we can change the normal framing of S′, and hence the
class of the formal Legendrian knot to which we want to apply Theorem 7.16, by
an arbitrary even integer. By decreasing this class by a large even integer and then
increasing it by stabilizations, we can thus make the obstruction in Theorem 7.16
vanish and continue as in the proof of Theorem 13.1 to extend the Weinstein struc-
ture over V′
j .

292 14. DEFORMATIONS OF FLEXIBLE WEINSTEIN STRUCTURES
Note that whenn> 3 the homotopy between the given and the split Weinstein
structure can be made subcritical, while when n = 3 this cannot be guaranteed.
Finally, consider the casen = 2. Note that any two exhausting functions which
have unique critical points of index 0 and the same number of critical points of index
1 are diﬀeomorphic. Hence, by pulling back the structure W under this diﬀeomor-
phism we can arrange that both Weinstein structures share the same Lyapunov
function. According to Remark 14.6 this implies that the two Weinstein structures
are homotopic. This concludes the proof of Theorem 14.16. □
14.5. Symplectic pseudo-isotopies
In this section we deﬁne and study symplectic analogues of the topological
notions introduced in Section 9.10.
Let us ﬁx a contact manifold (M2n−1,ξ ) and denote by (SM,λ st) its symplec-
tization with its canonical Liouville structure ( ωst =dλst,X st).
Any choice of a contact formα forξ yields an identiﬁcation ofSM with R×M
and the Liouville structure λst =erα,ωst =dλst,Xst =∂r. However, the following
constructions do not require the choice of a contact form. We will refer to the two
ends of SM as{±∞}× M.
We deﬁne the group of symplectic pseudo-isotopies of (M,ξ ) as
P(M,ξ ) :={F∈ Diﬀ(SM )|F∗ωst =ωst, F = Id near{−∞}× M,
F∗λst =λst near{+∞}× M}.
Moreover, we introduce the space
E(M,ξ ) :={(λ,φ ) Weinstein structure on SM without critical points |
dλ =ωst, (λ,φ ) = (λst,φ st) outside a compact set}
and its image ¯E(M,ξ ) under the projection ( λ,φ ) ↦→ λ. We endow the spaces
P(M,ξ ),E(M,ξ ) and ¯E(M,ξ ) with the topology of uniform C∞-convergence on
SM = R×M as explained in Section 9.10.
Lemma 14.22. The map
E(M,ξ )→ ¯E(M,ξ ), (λ,φ )↦→λ
is a homotopy equivalence and the map
P(M,ξ )→ ¯E(M,ξ ), F ↦→F∗λst
is a homeomorphism.
Proof. The ﬁrst map deﬁnes a ﬁbration whose ﬁber over λ is the contractible
space of Lyapunov functions for X which are standard at inﬁnity. The inverse of
the second map associates to λ the unique F∈ Diﬀ(SM ) satisfying F∗X =Xst on
SM and F = Id near{−∞}× M (which implies F∗λst =λ on SM ). □
Since F∈P (M,ξ ) satisﬁes F∗λst =λst near{+∞}× M, it descends there to
a contactomorphism F+ :M→M (see Section 6.8). By construction, F+ belongs
to the group DiﬀP(M) of diﬀeomorphisms that are pseudo-isotopic to the identity,
so it deﬁnes an element in
DiﬀP(M,ξ ) :={F+∈ DiﬀP(M)|F∗
+ξ =ξ}.

14.5. SYMPLECTIC PSEUDO-ISOTOPIES 293
Moreover,F+ = Id if and only if F belongs to the space
Diﬀc(SM,ω st) :={F∈ Diﬀc(SM )|F∗ωst =ωst}
of compactly supported symplectomorphisms of (SM,ω st). Thus we have a ﬁbration
Diﬀc(SM,ω st)→P (M,ξ )→ DiﬀP(M,ξ ).
The corresponding homotopy exact sequence ﬁts into a commuting diagram
(14.1)
π0Diﬀc(SM,ω st) −−−−→π0P(M,ξ ) −−−−→π0DiﬀP(M,ξ ) −−−−→0
↓
↓
↓
π0Diﬀc(R×M) −−−−→π0P(M) −−−−→π0DiﬀP(M) −−−−→0,
where the vertical maps are induced by the obvious inclusions.
The following is the main result of this section.
Theorem 14.23. For any closed contact manifold (M,ξ ) of dimension 2n−1≥
5 the map π0P(M,ξ )→π0P(M) is surjective.
Proof. By the discussion above and in Section 9.10, it suﬃces to show that the
map π0E(M,ξ )→ π0E(M) induced by the projection ( λ,φ )↦→ φ is surjective. So
letψ∈E (M), i.e.,ψ : R×M→ R is a function without critical points which agrees
with φst(r,x ) = r outside a compact set W = [a,b ]×M. We apply Theorem 14.1
to the Weinstein cobordism W = (W,ω st,X st,φ st) and the function ψ : W → R.
Hence there exists a Weinstein homotopy Wt = (W,ωt,Xt,φt), ﬁxed on Op∂−W
and ﬁxed up to scaling on Op∂+W , such that W0 = W and φ1 = ψ. Note that
λt = ctλst onOp∂+W for constants ct with c0 = 1. So we can extend Wt over
the rest of R×M by the function φst and Liouville forms of the form ft(r)λst such
that Wt = W on{r≤ a} and on {r≥ c} for some suﬃciently large c > b. By
Moser’s Stability Theorem 6.8, we ﬁnd a diﬀeotopy ht :SM→SM with h0 = Id,
ht = Id outside [a,c ]×M, and h∗
t Wt = W. Thus h∗
1W1 = (λ,φ ) with the function
φ := ψ◦h1 and a Liouville form λ which agrees with λst outside [a,c ]×M and
satisﬁes dλ =ωst. Hence (λ,φ )∈E (M,ξ ) and φ is homotopic (via ψ◦ht) to ψ in
E(M), i.e., [φ] = [ψ]∈π0E(M). □
Thus the second vertical map in the diagram (14.1) is surjective and we obtain
Corollary 14.24. Let (M,ξ ) be a closed contact manifold of dimension 2n−
1≥ 5. Then every diﬀeomorphism of M that is pseudo-isotopic to the identity is
smoothly isotopic to a contactomorphism of (M,ξ ).
Remark 14.25. Considering in the diagram (14.1) elements in π0P(M) that
map to Id∈π0DiﬀP(M), we obtain the following (non-exclusive) dichotomy for a
contact manifold (M,ξ ) of dimension ≥ 7 for which the map π0Diﬀc(R×M)→
π0P(M) is nontrivial: Either there exists a contactomorphism of ( M,ξ ) that is
smoothly but not contactly isotopic to the identity; or there exists a compactly
supported symplectomorphism of ( SM,ω st) which represents a nontrivial smooth
pseudo-isotopy class in P(M). Unfortunately, we cannot decide which of the two
cases occurs.



15
Deformations of Stein Structures
In this chapter we show that Weinstein homotopies can be lifted to Stein ho-
motopies, thus proving Theorem 1.1(b) and (c) from the introduction. As a con-
sequence, in Section 15.3 we carry over the ﬂexibility results of Chapter 14 from
Weinstein to Stein structures and deduce Theorems 1.9 and 1.10 from the Intro-
duction.
15.1. From Weinstein to Stein: homotopies
The main results of this chapter are the following two theorems. Let us point
out that all the results in this section also hold in dimension 4 without further
hypotheses.
Theorem 15.1 (ﬁrst Stein deformation theorem) . Let Wt = (W,ωt,Xt,φt) be
a homotopy of Weinstein cobordisms such that W0 = W(J,φ 0) for a Stein structure
(J,φ 0) on W . Then, after target reparametrizing the φt, there exists a diﬀeotopy
ht : W→ W relOp∂W with h0 = Id such that the functions ht∗φt are J-convex
and the paths of Weinstein structures Wt and W(h∗
tJ,φt) are homotopic with ﬁxed
functions φt and ﬁxed at t = 0.
If Wt is ﬁxed near ∂−W and/or ﬁxed up to scaling near ∂+W , then the same
can be arranged for the homotopy connecting the paths Wt and W(h∗
tJ,φt).
Theorem 15.1 will be proved in the next section. Combined with Theorem 13.6
it implies
Theorem 15.2 (second Stein deformation theorem) . Let (J0,φ 0) and (J1,φ 1)
be two Stein structures on the same cobordism W . Let Wt = (ωt,Xt,φt) be a
Weinstein homotopy connecting W0 = W(J0,φ 0) and W1 = W(J1,φ 1) which is
Stein near ∂−W . Suppose that Wt = W0 onOp∂−W for t∈ [0, 1
2], and φt = φ1
for t∈ [ 1
2, 1]. Then, after target reparametrizing the φt, the Stein structures on
Op∂−W extend to a Stein homotopy (Jt,φt) connecting (J0,φ 0) and (J1,φ 1) such
that the paths of Weinstein structures Wt and W(Jt,φt) are homotopic relOp∂−W
with ﬁxed functions φt and ﬁxed at t = 0, 1.
Proof. The proof of Theorem 15.2 follows the same scheme as that of Theo-
rem 14.13. It is based on Theorem 15.1 and the 1-parametric case in Theorem 13.6.
We will construct the Stein/Weinstein homotopies as in Figure 15.1, where the
vertical lines denote Weinstein homotopies with ﬁxed functions.
First we apply Theorem 15.1 to the Weinstein homotopy Wt, t∈ [0, 1
2], and
the Stein structure (J0,φ 0). Thus we ﬁnd a diﬀeotopy ht :W→W , t∈ [0, 1
2], rel
Op∂W with h0 = Id such that the functions ht∗φt are J0-convex and the paths
of Weinstein structures Wt and W(Jt := h∗
tJ0,φt), t∈ [0, 1
2], are homotopic rel
Op∂−W with ﬁxed functions φt and ﬁxed at t = 0.
295

296 15. DEFORMATIONS OF STEIN STRUCTURES
t0 1
2 1
(J0, φ0) (J1, φ1)
W′
t
~W 1
2
W(J1, φ1)~Wt
(h∗
t J0, φt) ( J0, φ 1
2
) (Jt, φ1)
Figure 15.1. Proof of the second Stein deformation theorem.
We connect W(J 1
2
,φ 1
2
) to W(J1,φ 1) by a Weinstein homotopy W′
t, t∈ [ 1
2, 1],
with ﬁxed function φ 1
2
= φ1 by concatenating the homotopy with ﬁxed function
from W(J 1
2
,φ 1
2
) to W 1
2
constructed in the preceding paragraph with the given ho-
motopy Wt,t∈ [ 1
2, 1]. Now we apply the 1-parametric case (k = 1) in Theorem 13.6
to the homotopy W′
t, t∈ [ 1
2, 1], to ﬁnd a Stein homotopy ( Jt,φt≡ φ1), t∈ [ 1
2, 1],
connecting (J 1
2
,φ 1
2
) and (J1,φ 1) such that the paths of Weinstein structures W′
t
and W(Jt,φt), t∈ [ 1
2, 1], are homotopic rel Op∂−W with ﬁxed function φt≡ φ1
and ﬁxed at t = 1
2, 1. By construction, ( Jt,φt) agrees with the Stein structure
underlying Wt onOp∂−W for all t ∈ [0, 1], and the paths W(Jt,φt) and Wt,
t∈ [0, 1], are homotopic rel Op∂−W with ﬁxed functions φ and ﬁxed endpoints.
Hence (Jt,φt), t∈ [0, 1], is the desired Stein homotopy. □
The same proofs also give the following versions of Theorems 15.1 and 15.2 for
Weinstein/Stein manifolds, which correspond to Theorem 1.1(b) and (c) from the
Introduction.
Theorem 15.3. Let Wt = (V,ωt,Xt,φt) be a homotopy of Weinstein manifolds
such that W0 = W(J,φ 0) for a Stein structure (J,φ 0) on V . Then, after target
reparametrizing theφt, there exists a diﬀeotopy ht :V →V with h0 = Id such that
the functions ht∗φt are J-convex and the paths of Weinstein structures Wt and
W(h∗
tJ,φt) are homotopic with ﬁxed functions φt and ﬁxed at t = 0.
Theorem 15.4. Let (J0,φ 0) and (J1,φ 1) be two Stein structures on the same
manifold V . Let Wt = (ωt,Xt,φt) be a Weinstein homotopy connecting W0 =
W(J0,φ 0) and W1 = W(J1,φ 1). Then, after target reparametrizing the φt, there
exists a Stein homotopy (Jt,φt) connecting (J0,φ 0) and (J1,φ 1) such that the paths
of Weinstein structures Wt and W(Jt,φt) are homotopic with ﬁxed functions φt
and ﬁxed at t = 0, 1.
Remark 15.5. Theorem 15.3 has the following consequence. If ( V,Jt,φt) is
a homotopy of Stein manifolds, then there exist diﬀeomorphisms h : V → V and
g : R→ R isotopic to the identity such that g◦φ1◦h−1 is J0-convex. In view of
Proposition 11.22, this shows that every exhaustingJ1-convex function is equivalent

15.1. FROM WEINSTEIN TO STEIN: HOMOTOPIES 297
to a J0-convex function. So Morse theoretic properties of the space of exhausting
J-convex functions, such as the minimal number of critical points of an exhausting
J-convex function, are invariant under Stein homotopies. It would be interesting
to further investigate such properties.
To put these theorems into a more topological context, we recall the setup
from the Introduction; see Appendix A.1 for the topological notions. Let us ﬁx a
cobordismW . Denote by Stein the space of Stein structures onW , by Weinstein the
space of Weinstein structures which are Stein near ∂−W , and by Morse the space
of generalized Morse functions on W (as usual with regular level sets ∂±W and
considered modulo target reparametrization). We have the commutative diagram
Stein
πS
$$JJJJJJJJJ
W // Weinstein
πW
xxqqqqqqqqqq
Morse
whereπW(ω,X,φ ) :=φ andπS(J,φ ) :=φ. Consider the ﬁbers Stein(φ) :=π−1
S (φ)
and Weinstein(φ) := π−1
W (φ) of the projections πS and πW overφ∈ Morse. For a
function φ∈ Morse we introduce the spaces
P(φ) :={(J,γ )| (J,φ )∈ Stein, γ: [0, 1]→ Weinstein(φ) ﬁxed near ∂−W,
γ(0) = W(J,φ )},
P :=
⋃
φ∈Morse
P(φ).
Theorem 15.2 asserts that the projection πP :P→ Weinstein, (h,γ )↦→ γ(1) has
the lift extension property for the pair ([0 , 1],∂ [0, 1]).
To rephrase Theorem 15.1, let us denote by D the identity component of the
group of diﬀeomorphisms of W ﬁxed near the boundary. For a Stein structure
(J,φ 0) on W and a function φ∈ Morse we introduce the spaces
DJ(φ) :={h∈D| φ ish∗J-convex},
PJ(φ) :={(h,γ )|h∈D J(φ), γ: [0, 1]→ Weinstein(φ) ﬁxed near ∂−W,
γ(0) = W(h∗J,φ )},
PJ :=
⋃
φ∈Morse
PJ(φ).
We denote by WeinsteinJ ⊂ Weinstein the connected component of W(J,φ 0) in
the space of Weinstein structures that agree with W(J,φ 0) near ∂−W . Now Theo-
rem 15.1 asserts the path lifting property for the projectionπPJ :PJ→ WeinsteinJ,
(h,γ )↦→γ(1). Note that we have a commutative diagram
PJ
πPJ
%%JJJJJJJJJJ //P
πP
zzuuuuuuuuuu
Weinstein
where the horizontal map sends (h,γ ) to (h∗J,γ ).
Now we see that the above proof of Theorem 15.2 just repeats the proof of
Corollary A.5 from Appendix A.1 in the special case k = 1: We are given a path

298 15. DEFORMATIONS OF STEIN STRUCTURES
Wt in Weinstein connecting W(J0,φ 0) =πP(P0) and W(J1,φ 1) =πP(P1) which be-
longs to WeinsteinJ0 fort∈ [0, 1
2] and to Weinstein(φ1) fort∈ [ 1
2, 1]. Theorem 15.1
and the last diagram provides a lift Pt ∈P , t∈ [0, 1
2]. Now the projections of
P 1
2
,P 1∈P (φ1) are connected by the path Wt, t∈ [ 1
2, 1], in Weinstein(φ1). Hence
Theorem 13.6, which asserts that the projection P(φ1)→ Weinstein(φ1) is a weak
homotopy equivalence, provides a path Pt, t∈ [ 1
2, 1], inP(φ1) connecting P 1
2
and
P1.
We believe that Theorem 15.1 can be improved to the following
Conjecture 15.6. The projection πPJ :PJ→ WeinsteinJ, (h,γ )↦→γ(1) is a
Serre ﬁbration.
According to Corollary A.6 in Appendix A.1, Conjecture 1.3 combined with
Theorem 1.2 would imply
Conjecture 15.7. The map W : Stein → Weinstein is a weak homotopy
equivalence.
15.2. Proof of the ﬁrst Stein deformation theorem
The proof of Theorem 15.1 follows the same scheme as that of Theorem 14.9,
based on the following 3 lemmas.
Lemma 15.8. Let (W,J,φ ) be a Stein cobordism and W = (W,ω,X,φ ) an
elementary Weinstein cobordism such that W = W(J,φ ) onOp∂W . Suppose that
W and W(J,φ ) are connected by a Weinstein homotopy with ﬁxed function φ and
ﬁxed on Op∂W . Then, after target reparametrizing φ, there exists a Weinstein
homotopy Wt = (W,ωt,Xt,φ ), t∈ [0, 1], such that
• W0 = W(J,φ ) and W1 = W;
• the homotopy Wt is ﬁxed onOp∂−W and ﬁxed up to scaling onOp∂+W ;
• for t∈ [0, 1
2] the function φ is h∗
tJ-convex and Wt = W(h∗
tJ,φ ), for a
diﬀeotopyht :W→W , t∈ [0, 1
2], with h0 = Id and ht|Op∂W = Id;
• fort∈ [ 1
2, 1] the Weinstein cobordisms Wt are elementary and the attach-
ing spheres in ∂−W of all critical points of φ remain ﬁxed for t∈ [ 1
2, 1].
Proof. Step 0. By Remark 9.2 there exists a diﬀeotopy ht : W → W ,
t ∈ [0, 1], with h0 = Id, ht|Op∂W = Id and φ◦ht = φ, such that h∗
1W(J,φ )
and W have the same local stable and unstable manifolds near critical points.
By Proposition 12.12 there exists a homotopy rel Op∂W of Weinstein structures
Wt = (W,ωt,Xt,φ ) with W0 = W such that W1 agrees with h∗
1W(J,φ ) near the
critical points, and the stable and unstable manifolds of all Wt agree with those of
W. The last property ensures that all the Wt are elementary cobordisms. After
replacing W by W1 and J by h∗
1J, we may hence assume that W agrees with
W(J,φ ) onOp (∂W∪ Critφ).
By a 1-parametric version of Proposition 12.12, we can connect W and W(J,φ )
by a Weinstein homotopy Wt with ﬁxed function φ and ﬁxed onOp (∂W∪ Critφ).
After applying Gray’s Theorem 6.23 on each level set and pulling Wt back by a
diﬀeotopy, we can further arrange that the Wt, t∈ [0, 1], induce the same contact
structures on all level sets of φ.
After these preparations, the rest of the proof follows the same steps as that of
Lemma 14.10, using the same notation.

15.2. PROOF OF THE FIRST STEIN DEFORMATION THEOREM 299
Step 1. Deﬁne cj, Wj, Vj and S±
j ⊂ Σ±
j (with respect to the Liouville ﬁeld
X) as in the proof of Lemma 14.10, see Figure 14.1.
By Step 0, the Weinstein structures W and W(J,φ ) induce the same contact
structures ξ±
j on Σ±
j . The assumption that the Weinstein cobordism W is elemen-
tary implies that S±
j is a union of isotropic resp. coisotropic spheres in the contact
manifold (Σ±
j ,ξ±
j ).
By Step 0, there exists a Weinstein homotopy Wt := (ωt,Xt,φ ) from W0 = W
to W1 = W(J,φ ) which is ﬁxed onOp (∂W∪ Critφ) and induces the same contact
structures on all level sets. Since Wt is ﬁxed near the critical points, after shrinking
the Wj we may assume that the Xt-unstable spheres in Σ +
j of the critical points
on level cj are ﬁxed. Using Lemma 12.5 we can modify Wt on⋃
jVj to a simple
Weinstein homotopy~Wt = (~ωt, ~Xt,φ ) such that the intersections of the ~Xt-stable
manifolds of critical points on level ci >c j with Σ+
j remain unchanged, and hence
the Weinstein homotopy~Wt is elementary. After renaming ~W1 back to W we may
thus assume that W = W(J,φ ) onOp ⋃N
j=1Wj.
We will construct the required homotopy Wt = (ωt,Xt,φt) separately on each
Vj, ﬁxed near ∂−Vj and ﬁxed up to scaling near ∂+Vj. This will allow us to extend
the homotopy to ⋃N
j=1Wj as ﬁxed up to scaling.
Step 2. Consider Vj for 1≤ j≤ N− 1. To simplify the notation, we will
omit the index j and denote the restriction of objects to Vj by the same symbol as
the original objects.
By assumption we have a Weinstein homotopy Wt = (Vj,ωt,Xt,φ ), t∈ [0, 1],
from W0 = W|Vj to W1 = W(J,φ )|Vj which is ﬁxed on Op (∂W∪ Critφ) and
induces the same contact structures on all level sets. Recall that the holonomy
along Xt deﬁnes contactomorphisms
ΓXt : (Σ−
j+1,ξ−
j+1)→ (Σ+
j ,ξ +
j ).
By Proposition 10.1, after target reparametrizing φ, we ﬁnd a diﬀeotopy ht :Vj→
Vj, t∈ [0, 1], with h0 = Id and ht = Id near ∂Vj, such that the functions ht∗φ are
J-convex and the holonomy of the cobordism W′
t = (Vj,ω′
t,X′
t,φ ) := W(Vj,h∗
tJ,φ )
satisﬁes
ΓX′
t(S−
j+1) = ΓXt(S−
j+1) for all t∈ [0, 1].
Now Lemma 12.6 provides a Weinstein homotopy ~Wt = (Vj,~ωt, ~Xt,φ ) such that
(i) ~Wt = W′
2t = W(h∗
2tJ,φ ) for t∈ [0, 1
2];
(ii) ~W1 = W1 = W;
(iii) ~Wt coincides up to scaling with W onOp∂Vj and induces the same
contact structures on level sets;
(iv) Γ ~Xt
(S−
j+1) = ΓX(S−
j+1) = S+
j for t∈ [ 1
2, 1].
Condition (iv) implies that the resulting Weinstein homotopy ~Wt on W is ele-
mentary over the interval [ 1
2, 1], and moreover, the intersection of the ~Xt-stable
manifolds of all critical points with ∂−W remains unchanged for t∈ [ 1
2, 1]. □
Lemma 15.9. Let (W,J,φ ) be a Stein cobordism and W = ( W,ω,X,φ ) a
Weinstein cobordism such that the function φ has exactly two critical points con-
nected by a unique X-trajectory. Suppose that W and W(J,φ ) are connected by
a Weinstein homotopy with ﬁxed function φ and ﬁxed on Op∂W . Then, after

300 15. DEFORMATIONS OF STEIN STRUCTURES
target reparametrizing φ, there exists a Weinstein homotopy Wt = (W,ωt,Xt,φ ),
t∈ [0, 1], such that
• W0 = W(J,φ ) and W1 = W;
• the homotopy Wt is ﬁxed onOp∂−W and ﬁxed up to scaling onOp∂+W ;
• for t∈ [0, 1
2] the function φ is h∗
tJ-convex and Wt = W(h∗
tJ,φ ), for a
diﬀeotopyht :W→W , t∈ [0, 1
2], with h0 = Id and ht|Op∂W = Id;
• for t∈ [ 1
2, 1] the two critical points of the function φ are connected by a
unique Xt-trajectory.
Proof. In this case the function φ has exactly 2 critical points p1,p 2∈W of
index k− 1,k and with critical values c1 <c 2. For suﬃciently small ε> 0 we split
the cobordism W into two parts:
U :={φ≤c1 +ε}, V :={φ≥c1 +ε}.
Arguing as in Steps 0 and 1 of the proof of Lemma 15.8 we can reduce to the case
that W = W(J,φ ) onOpU.
Now the restriction of W toV is elementary of type I. Hence by Lemma 15.8, af-
ter target reparametrizingφ, there exists a Weinstein homotopyWt = (V,ωt,Xt,φ ),
t∈ [0, 1], such that
• W0 = W(V,J,φ ) and W1 = W|V ;
• the homotopy Wt is ﬁxed onOp∂−V and ﬁxed up to scaling onOp∂+V ;
• for t∈ [0, 1
2] the function φ is h∗
tJ-convex and Wt = W(V,h∗
tJ,φ ), for a
diﬀeotopyht :V →V , t∈ [0, 1
2], with h0 = Id and ht|Op∂V = Id;
• fort∈ [ 1
2, 1] the Weinstein cobordisms Wt are elementary and the attach-
ing spheres in ∂−V of all critical points of φ remain ﬁxed for t∈ [ 1
2, 1].
The homotopies Wt andht extend canonically overU as a rescaling of W resp. the
identity. The last property guarantees that for t∈ [ 1
2, 1] the two critical points are
connected by a unique Xt-trajectory. □
The following lemma will serve as induction step in proving Theorem 15.1.
Lemma 15.10. Let (W,J,φ ) be a Stein cobordism and Wt = (W,ωt,Xt,φt),
t∈ [0, 1], an elementary Weinstein homotopy such that Wt = W(J,φ ) onOp (∂W ).
Suppose that we are given a Weinstein homotopy Ws
0, s∈ [0, 1], with ﬁxed function
φ and ﬁxed on Op∂W , from W0
0 = W0 to W1
0 = W(J,φ ).
Then, after target reparametrizing the φt, there exists a diﬀeotopy ht :W→W
ﬁxed on Op∂W with h0 = Id such that the functions ht∗φt are J-convex. More-
over, the Weinstein homotopy Ws
0 extends to a homotopy of paths of Weinstein
structures Ws
t, s,t ∈ [0, 1], ﬁxed on Op∂−W and up to scaling on Op∂+W , with
ﬁxed functions φt, from W0
t = Wt to W1
t = W(h∗
tJ,φt).
Proof. Type I. Consider ﬁrst the case when the homotopy Wt is elementary
of type I. We point out that W(J,φ ) need not be elementary. To remedy this,
we apply Lemma 15.8 to construct a Weinstein homotopy ~Wt = (W,~ωt, ~Xt,φ ),
t∈ [0, 1], such that
• ~W0 = W(J,φ ) and ~W1 = W0;
• the homotopy~Wt is ﬁxed onOp∂−W and ﬁxed up to scaling onOp∂+W ;
• for t∈ [0, 1
2] the function φ is h∗
tJ-convex and ~Wt = W(h∗
tJ,φ ), for a
diﬀeotopyht :W→W , t∈ [0, 1
2], with h0 = Id and ht|Op∂W = Id;

15.2. PROOF OF THE FIRST STEIN DEFORMATION THEOREM 301
• for t∈ [ 1
2, 1] the Weinstein cobordisms ~Wt are elementary.
Thus it is suﬃcient to prove the lemma for the Stein cobordism ( h∗
1
2
J,φ ) instead
of (J,φ ), and the concatenation of the Weinstein homotopies ~Wt∈[ 1
2,1] and Wt∈[0,1]
instead of Wt. To simplify the notation we rename the new Stein cobordism and
Weinstein homotopy back to (J,φ ) and Wt. So in the new notation we have W0 =
W(J,φ ).
According to Proposition 10.10, after target reparametrization of the φt, there
exists a family of J-convex functions ~φt, t∈ [0, 1], on W with the same proﬁle as
the family φt and such that ~φ0 =φ and ~φt =φt onOp (∂W ). Then Lemma 12.23
provides a diﬀeotopy ht : W→ W ﬁxed onOp (∂W∪ Critφt) with h0 = Id such
that φt = ~φt◦ht, and the paths of Weinstein structures Wt and W(h∗
tJ,φt) are
homotopic relOp∂W with ﬁxed functions φt and ﬁxed at t = 0.
Types IId and IIb. Suppose now that the homotopy Wt is of type IId. Let
t0∈ [0, 1] be the parameter value for which the functionφt has a death-type critical
point. In this case the function φ has exactly two critical points p andq connected
by a uniqueX0-trajectory. Arguing as in the type I case, using Lemma 15.9 instead
of Lemma 15.8, we can again reduce to the case that W0 = W(J,φ ).
Then Theorem 10.12 provides an elimination family of J-convex functions ~φt :
W→ R,t∈ [0, 1], starting from~φ0 =φ and killing the critical pointsp andq at time
t0. After target reparametrization of the φt, we can also arrange that ~φt coincides
with φt onOp (∂W ) and the homotopies ~φt and φt have equal proﬁles. Now we
again apply Lemma 12.23 to construct the required diﬀeotopy ht and homotopy
between the paths Wt and W(h∗
tJ,φt).
The argument in the case of type IIb is similar, except that we use the Creation
Theorem 10.11 instead of the Cancellation Theorem 10.12, and we do not need a
preliminary homotopy. □
Proof of Theorem 15.1. By Lemma 9.37 we ﬁnd an admissible partition
for the homotopy Wt:
0 =t0 <t 1 <··· <t p = 1, m (t) =ck
0(t)<c k
1(t)<··· <c k
Nk(t) =M(t),
t ∈ [tk−1,tk], k = 1,...,p . As in the proof of Theorem 14.9, by twisting the
homotopy Wt by a diﬀeotopy of W we can arrange that the values ck
j =ck
j (t) and
the hypersurfaces Σ k
j ={φt = ck
j (t)} are independent of t∈ [tk−1,tk]. We will
extend the desired isotopy ht and the homotopy Ws
t between Wt and W(h∗
tJ,φt)
inductively over the intervals [tk−1,tk],k = 1,...,p , and for eachk we extend them
inductively over the elementary cobordisms Wk
j bounded by ∂−Wk
j = Σk
j−1 and
∂+Wk
j = Σk
j .
Supposeht and Ws
t,s∈ [0, 1], are already constructed on all of W fort≤tk−1.
Recall that the restriction of the homotopy Wt,t∈ [tk−1,tk] to each cobordismWk
j
is elementary. Using Lemma 12.7 we can modify the family Wt,t∈ [tk−1,tk], near
the Σk
j to make it agree with W(h∗
tk−1J,φtk−1) onOp Σk
j for all j andt∈ [tk−1,tk].
The resulting family, which we continue to denote by Wt, will still be elementary
over each cobordism Wk
j . Hence we can apply Lemma 15.10 to each elementary
homotopy Wt|Wk
j
, the complex structure h∗
tk−1J, and the homotopy Ws
tk−1|Wk
j
,
s∈ [0, 1]. For eachj lethj
t :Wk
j →Wk
j ,t∈ [tk−1,tk], be the diﬀeotopy provided by

302 15. DEFORMATIONS OF STEIN STRUCTURES
Lemma 15.10. The hj
t ﬁt together to form a diﬀeotopy ~ht :W→W , t∈ [tk−1,tk].
Now ht := htk−1◦~ht : W → W is the desired extension of the diﬀeotopy to
the interval [tk−1,tk]. Moreover, the 2-parametric Weinstein families on each Wk
j
provided by Lemma 15.10 ﬁt together (after rescaling) to the desired extension of
the family Ws
t over the interval [tk−1,tk]. □
15.3. Homotopies of ﬂexible Stein structures
Using the results of Section 15.1, we can upgrade the results on ﬂexible Wein-
stein homotopies in Chapter 14 to corresponding results on ﬂexible Stein homo-
topies. Recall that a Stein cobordism or manifold structure ( W,J,φ ) is called
subcritical, resp. ﬂexible, if the corresponding Weinstein structure W(W,J,φ ) is
subcritical, resp. ﬂexible.
Theorems 14.1 and 15.1 (resp. 14.4 and 15.3 in the manifold case) together
with Remark 14.6 imply
Theorem 15.11. Let (W,J,φ ) be a ﬂexible Stein cobordism or manifold of real
dimension 2n >4 and ψ : W→ R, be a Morse function without critical points of
index >n which in the manifold case is exhausting, and in the cobordism case has
∂±W as its regular level sets. Then there exist diﬀeomorphisms h : W→ W and
α : R→ R diﬀeotopic to the identity such that the function α◦ψ◦h is J-convex.
The same holds in dimension 2n = 4 if we assume the existence of a Morse
homotopy φt connectingφ and ψ without critical points of index > 1, or without
critical points of index > 2 in the case that ∂−W⁄= ∅ is overtwisted.
In particular, we have the following Stein version of the h-cobordism theorem.
Corollary 15.12 (Stein h-cobordism theorem) . Any ﬂexible Stein structure
(J,φ ) on a product cobordism M× [0, 1] of dimension 2n >4 admits a J-convex
function without critical points.
More generally, recall that a Morse function on a cobordism or manifold is
called perfect if it has the minimal number of critical points compatible with the
Morse inequalities.
Corollary 15.13. (a) Let (W,J,φ ) be a simply connected ﬂexible Stein do-
main. Then there exists a perfect J-convex Morse function ψ :W→ R having ∂W
as regular level set. In particular, the stabilization V× C of any simply connected
ﬁnite type Stein manifold V admits a perfect exhausting J-convex Morse function.
(b) Let (J,φ ) be a ﬂexible Stein structure on R2n. Then there exists an exhaust-
ing J-convex function ψ : R2n→ R with a unique critical point, the minimum. In
particular, such a function exists on the stabilization V×C of any contractible Stein
manifold V .
Proof. The ﬁrst statement in (a) for dim W = 2n≥ 6 follows from Smale’s
Theorem 9.44 and Theorem 15.11. (Here simple connectedness of ∂W follows from
that of W because W is obtained from ∂W by attaching handles of index ≥ 3.)
In the case 2n = 4 the Stein domain ( W,J,φ ) is subcritical, so φ has only critical
points of index 0 and 1. Thus we just need to cancel all unnecessary minima of φ,
which can be done in any dimension.
The second statement in (a) follows from this and the observation that the sta-
bilizationV×C of a simply connected ﬁnite type Stein manifoldV is the completion
of a simply connected Stein domain W .

15.3. HOMOTOPIES OF FLEXIBLE STEIN STRUCTURES 303
The ﬁrst statement in (b) follows for n≥ 3 directly from Theorem 15.11, and
for n = 2 from the argument for part (a).
The second statement in (b) follows from Stallings’ theorem [176] which asserts
that any productV1×V2 of two contractible manifolds with dimVi≥ 1 and dim(V1×
V2)≥ 5 is diﬀeomorphic to Euclidean space. (Actually Stallings’ result is in the
PL-category; the smooth case follows using [ 142].) □
The last statement in Corollary 15.13 is Theorem 1.9 from the Introduction.
The last statement in Corollary 15.13(b) is Theorem 1.9 from the Introduction.
Theorems 14.3 and 15.2 (resp. 14.5 and 15.4 in the manifold case) together with
Remark 14.6 imply
Theorem 15.14. Let (J0,φ 0) and (J1,φ 1) be two ﬂexible Stein structures on a
cobordism or manifold W of real dimension 2n> 4. Suppose J0 and J1 are homo-
topic as almost complex structures. Then (J0,φ 0) and (J1,φ 1) are Stein homotopic.
The same holds in dimension 2n = 4 if we assume the existence of a Morse
homotopy φt connectingφ0 and φ1 without critical points of index > 1, or without
critical points of index > 2 in the case that ∂−W⁄= ∅ is overtwisted.
In particular, we have
Corollary 15.15. Any two ﬂexible Stein structures on R2n are homotopic.
In particular, the underlying Weinstein structures are exact symplectomorphic.
Proof. For n > 2 this follows directly from Theorem 15.14. Alternatively,
we can use the following argument that works for any n: By Corollary 15.13 (b)
each ﬂexible Stein structure on R2n admits an exhausting J-convex function with
a unique critical point, the minimum. Now the Stein homotopy is provided by
Proposition 11.22 and Corollary 11.27. □
Without the ﬂexibility hypothesis, Corollary 15.15 remains true for ﬁnite type
Stein structures in dimension 2n = 4 (see Chapter 16 below), while it becomes false
in all dimensions 2n> 4 (see Chapter 17).
Remark 15.16. We do not know whether any two ﬂexible (i.e., subcritical)
Stein structures on a boundary connected sum (see Chapter 16) W ofk≥ 1 copies
ofB3×S1 are homotopic. However, we will show in Chapter 16 that they become
homotopic after applying a diﬀeomorphism of W .
Finally, let us consider the J-convex pseudo-isotopy problem, i.e., the study of
the topology of the space of J-convex functions without critical points. Namely,
let (M× [0, 1],J,φ ) be a topologically trivial Stein cobordism. Let us denote by
E(M×[0, 1],J ) the space ofJ-convex functionsM×[0, 1]→ R without critical points
which are constant onM×0 andM×1. If dimM >3 and the Stein structure (J,φ )
is ﬂexible, then according to Corollary 15.12 the spaceE(M×[0, 1],J ) is non-empty.
It is interesting to study the canonical inclusion I :E(M× [0, 1],J )↪→E (M) into
the pseudo-isotopy spaceE(M) introduced in Section 9.10 of all smooth functions
M× [0, 1]→ R without critical points which are constant on M× 0 and M× 1.
The following theorem corresponds to Theorem 1.10 in the Introduction.
Theorem 15.17. For any topologically trivial ﬂexible Stein cobordism (M×
[0, 1],J,φ ) of dimension 2n> 4, the induced homomorphism
I∗ :π0E(M× [0, 1],J )→π0E(M)

304 15. DEFORMATIONS OF STEIN STRUCTURES
is surjective. □
Proof. Let ψ∈E (M) be given. By Theorem 15.11 there exist diﬀeotopies
ht : M× [0, 1]→ M× [0, 1] and αt : R→ R with h0 = Id and α0 = Id such that
the function ψ1 :=α1◦ψ◦h1 is J-convex. Since ψ1 is connected to ψ by the path
αt◦ψ◦ht of functions without critical points, the functions ψ1 and ψ belong to
the same path connected component of E(M). □

Part 5
Stein Manifolds and Symplectic
Topology

The main tool in modern symplectic topology is the theory of J-holomorphic
curves which was introduced by Gromov in 1985 ([ 83]). It was preceded by the
method of ﬁlling by holomorphic discs introduced in the theory of functions of
several complex variables by Bishop [ 19], and developed for global applications by
Bedford and Gaveau [15]. In the ﬁnal part of this book we discuss applications of
this theory to the topology of Stein manifolds.
In Chapter 16 we outline how, in complex dimension two, foliations by J-
holomorphic curves give rise to various uniqueness results for Stein structures.
Chapter 17 starts with a review of symplectic homology, the main current tool
for distinguishing Stein structures up to symplectomorphism. Then we outline
how recent work by McLean and others leads to the existence of inﬁnitely many
pairwise non-symplectomorphic Stein structures on every smooth manifold that
admits a Stein structure.

16
Stein Manifolds of Complex Dimension Two
Foliations by J-holomorphic curves provide a powerful tool for the study of
(almost) complex manifolds of complex dimension two. For example, Gromov used
in [ 83] foliations by holomorphic spheres to prove that every symplectic ﬁlling
(W,ω ) of the standard 3-sphere with ω vanishing onπ2(W ) is symplectomorphic to
the standard 4-ball. The results in the chapter are based on foliations by holomor-
phic discs, which were introduced in [43] and whose main properties (with sketches
of proofs) we review in Section 16.1.
In Section 16.2 we derive uniqueness of Stein ﬁllings up to deformation equiv-
alence for S3 and connected sums of copies of S2×S1. Along the way we prove
that the property of having unique Stein ﬁllings up to deformation equivalence
is preserved under 0-surgery. In Section 16.3 we prove that certain 4-manifolds,
including R4 and R3×S1, have unique ﬁnite type Stein structures up to deforma-
tion equivalence, and that ﬁnite type Stein manifolds cannot be homeomorphic to
S2× R2.
16.1. Filling by holomorphic discs
Consider an embedded surface S in an almost complex 4-manifold ( V,J ) (i.e.,
V has real dimension 4 and S has real dimension 2). Generically, S has isolated
pointsp∈S where the tangent plane TpS is a complex line. If the surface S is ori-
ented, then a complex point is called positive or negative depending on whether the
orientation ofTpS coincides with its orientation as a complex line, or is opposite to
it. The complement of the complex points in S is a totally real surface. Generically,
complex points can also be subdivided into elliptic and hyperbolic points; see [43].
An example one should have in mind is a surface S⊂ R3 ={y2 = 0}⊂ C2. Then
complex points of S are critical points of the function x2|S. A complex point is
nondegenerate if and only if the corresponding critical point is nondegenerate; it is
hyperbolic if the Morse index of this critical point is 1, and elliptic otherwise.
In this book we will deal only with surfacesS which are contained in aJ-convex
hypersurface M⊂ V . Hence we will restrict our further discussion to this special
case. See [ 53] for more detail.
Let us denote by ξ the induced contact structure, i.e., the ﬁeld of complex
tangencies to M. Given a surface S⊂M⊂V , its complex points are exactly the
points whereS is tangent toξ. In other words, the complex points are singularities
of the characteristic foliation generated by the line ﬁeld ξ∩TS onS in the comple-
ment of complex points. Assuming that the surface S is oriented, the characteristic
line ﬁeldξ∩TS inherits an orientation and hence can be generated by a vector ﬁeld
v. Generically, the index of the vector ﬁeld v at complex points is equal to±1. We
say that a complex point is elliptic if the index is +1, and hyperbolic if it is−1.
307

308 16. STEIN MANIFOLDS OF COMPLEX DIMENSION TWO
Let us denote by e± and h± the numbers of positive and negative elliptic and
hyperbolic points, and set d± :=e±−h±.
If S is closed, the Euler characteristic χ of S and the value c :=e(ξ)[S] of the
Euler class of ξ on [S] can be computed from the singular points as
(16.1)
χ =d+ +d−,
c =d+−d−.
Indeed, the ﬁrst formula is just the Poincar´ e–Hopf index theorem (see [ 87]). To
see the second one, note that c is the obstruction to constructing two C-linearly
independent vector ﬁelds tangent to W along S. Consider the pair of vector ﬁelds
(v,v⊥) outside the complex points, where v is a vector ﬁeld generating the charac-
teristic foliation and (v,v⊥) is a basis of TS deﬁning the orientation. These ﬁelds
are C-linearly independent away from the complex points, while positive elliptic and
negative hyperbolic points contribute 1 to the total index c, and negative elliptic
and positive hyperbolic points contribute −1.
The equations (16.1) can be rewritten in the form
(16.2) d± :=e±−h± = 1
2(χ±c).
Remark 16.1. For a general oriented closed surface in an almost complex 4-
manifold, the corresponding formula for d± contains an extra term (see [119, 51]),
(16.3) d± = 1
2(χ +ν±c).
Here ν is the normal Euler number, or equivalently, the self-intersection index, of
the surface S. Note that ν vanishes in the special case considered above when S is
contained in a J-convex hypersurface M⊂ V , as well as when S is homologically
trivial.
Example 16.2. Consider the unit ball B4 ={|z|≤ 1}⊂ C2 with complex
coordinates z = (z1,z 2), zj = xj +iyj. The ﬁeld of complex tangencies on its
i-convex boundary S3 = ∂B4 deﬁnes the standard contact structure on S3. Let
p± := (0,±i)∈S3. Then S3\{p+,p−} is foliated by the 2-spheres
St :={|z| = 1, y2 =t}⊂ S3, t ∈ (−1, 1),
see Figure 16.1. Each St has precisely two complex points q±
t = (0,±
√
1−t2 +it),
with q+
t positive and q−
t negative elliptic. Note that St bounds the Levi-ﬂat 3-ball
{|z|≤ 1, y2 =t}⊂ B4 which is foliated by the holomorphic discs
∆s,t :={x2 =s, y2 =t,|z1|2≤ 1−s2−t2}, t ∈ (−1, 1), |s|<
√
1−t2.
The boundaries of the discs ∆ s,t foliate St\{q+
t ,q−
t} by the circles{x2 =s, y2 =
t,|z1|2 = 1−s2−t2}. For later reference, let us deﬁne the Levi-ﬂat 3-ball
(16.4) D :={|z1|2 +x2
2≤ 1}⊂ R3 ={y2 = 0}⊂ C2.
Let us call an almost complex structure J tame if it admits a symplectic form
ω tamingJ, i.e., such that ω is positive on complex directions. An almost complex
4-manifold (W,J ) is called minimal if it contains no embedded holomorphic spheres
with self-intersection number−1. Any complex manifold can be blown down to a
(not necessarily unique) minimal one, and the same holds for an almost complex
manifold with taming symplectic form [ 134].

16.1. FILLING BY HOLOMORPHIC DISCS 309
y2
p+ St
q+
t
q−
t
∆s,t
D
x2
z1
p−
Figure 16.1. The foliation of the standard 4-ball by holomorphic discs.
Bishop proved in [ 19] that, as in Example 16.2 above, each elliptic complex
point p on a surface S in a complex surface (V,J ) has a neighborhood U⊂S such
that U\{p} is foliated by concentric circles which bound J-holomorphic discs in
V . Such a family of J-holomorphic discs is called a Bishop family . Importantly,
this result has the following global version, see [ 15, 83, 43].
Theorem 16.3. Let (W,J ) be a tame compact almost complex 4-manifold
with J-convex boundary. Suppose that W contains no nonconstant J-holomorphic
spheres.
(a) Let S ⊂ ∂W be an embedded 2-sphere with exactly two complex points
p+,p− which are both elliptic. Then S\{p−,p +} is foliated by circles which bound
J-holomorphic discs inside W . All these discs are embedded, disjoint, and ﬁll a
Levi-ﬂat embedded 3-ball B⊂ W bounded by S = ∂B. Moreover, there exists a
diﬀeomorphismF :D→B which is holomorphic on the discs{x2 = const}⊂ D. If
the sphere S is real analytic, then the diﬀeomorphism F can be chosen real analytic
in the complement of the points (z1 = 0,x 2 =±1).
(b) Let f : ∂D× [a,b ] ↪→ ∂W be an embedding such that each sphere St =
f(∂D×t)⊂ ∂W , t∈ [a,b ], satisﬁes the hypotheses of (a). Then f extends to an
embeddingF : D× [a,b ] ↪→ W such that the balls Bt = F (D×t), t∈ [a,b ], are
Levi-ﬂat and foliated by J-holomorphic discs. If the embedding f is real analytic
then the extension F can be chosen holomorphic along the discs (D∩{x2 =s})×t,
s∈ (−1, 1), t∈ [a,b ], and real analytic in the complement of the arcs γ± ={z1 =
0,x 2 =±1}× [a,b ].
Note that Theorem 16.3 is applicable, in particular, in the situation when (W,J )
is a Stein domain of complex dimension two.
Sketch of proof. For details of the following arguments see [ 99]. Let us
begin with (a). As already mentioned above, there exist Bishop families ([ 19],
see [195] for the case of nonintegrable J) of J-holomorphic discs emanating from
the elliptic points p±. The problem is to extend them globally to ﬁll the sphere
S. Note that near p± Bishop’s discs are embedded and disjoint. Positivity of

310 16. STEIN MANIFOLDS OF COMPLEX DIMENSION TWO
intersections (see [ 83, 135, 138 ]) then implies that all the discs in the family
are embedded and disjoint. If one can prove compactness for the moduli space
of J-holomorphic discs with boundary on S this implies that the Bishop families
emanating fromp± are ends of the same one-dimensional moduli space of embedded
disjoint discs ﬁlling S. Note that Stokes’ theorem implies that the symplectic area
of all J-holomorphic discs with boundary on S is uniformly bounded by
∫
S|ω|.
Hence, by Gromov’s compactness theorem [ 83], compactness can only fail due to
bubbling on the boundary or in the interior.
The boundaries of all holomorphic discs which ﬁll S have to be transverse to
the characteristic foliation on S. Indeed, tangency of the boundary of a disc to the
characteristic foliation would imply the tangency of the disc itself to the J-convex
boundary ∂W , which is impossible due to the maximum principle. Since ( ∂W,ξ )
is ﬁllable and hence tight, the characteristic foliation on S is homeomorphic to the
foliation by meridians connecting elliptic points. An embedded boundary curve of
a holomorphic disc thus has winding number ±1 around the elliptic points, and
hence it cannot split. This rules out bubbling at the boundary. On the other hand,
bubbling in the interior is ruled out by the assumption that W has no nonconstant
J-holomorphic spheres.
Part (b) can be proved similarly, taking into account that holomorphic discs
ﬁlling diﬀerent 2-spheres are disjoint due to positivity of intersections. □
The method of ﬁlling by holomorphic discs can also be used to prove the fol-
lowing
Theorem 16.4 ([43]). LetS be an embedded oriented closed surface contained
in the J-convex boundary of a tame compact almost complex 4-manifold (W,J ).
(i) If S⁄∼=S2 then d±≤ 0, or equivalently (in view of (16.2))|c|≤− χ.
(ii) If S∼=S2 then c = 0 and hence (in view of (16.2)) d+ =d− = 1.
(iii) By a C0-small isotopy of the surface S in ∂W the non-negative integers
e± and h± can be arbitrarily changed as long as the diﬀerences d± are preserved.
In particular, by a C0-small isotopy of S in ∂W one can get rid of all elliptic
points in case (i), and kill all complex points except two elliptic points, one positive
and one negative, in case (ii).
For a general surfaceS in a 4-manifoldV the analogue of (iii) also holds, and in
fact it is simpler because one is allowed an isotopy unconstrained by the condition
S⊂∂W , see [84] and [51].
Using the Giroux-Fuchs elimination lemma [ 66], Theorem 16.4 was extended
in [44] to the more general case of a surface in an arbitrary tight contact 3-manifold.
16.2. Stein ﬁllings
When complex analysts talk about holomorphic ﬁllings they usually mean ﬁll-
ings of CR-manifolds. The existence of such a ﬁlling is a very delicate analytic
question, see the discussion in Section 5.10 above. In this section we are interested
in holomorphic ﬁllings of smooth, or contact, manifolds.
A Stein ﬁlling of a closed oriented 3-manifold M is a Stein domain ( W,J,φ )
such that there exists an orientation preserving diﬀeomorphism between ∂W (with
the boundary orientation) and M.

16.2. STEIN FILLINGS 311
A Stein ﬁlling of a closed contact 3-manifold (M,ξ ) is a Stein domain (W,J,φ )
such that there exists an orientation preserving contactomorphism between ∂W
with the ﬁeld of complex tangencies and ( M,ξ ).
Two Stein cobordisms ( W,J,φ ) and (W′,J′,φ′) are called deformation equi-
valent if there exists a diﬀeomorphism h :W→W′ such that the Stein structures
(J,φ ) and (h∗J′,h∗φ′) on W are homotopic. An analogous deﬁnition applies to
Weinstein cobordisms and to Stein/Weinstein manifolds. Note that for ﬁxed J any
twoJ-convex functions are homotopic (this is obvious for cobordisms and Proposi-
tion 11.22 for manifolds), so in this section we will often omit φ from the notation
of a Stein cobordism or manifold.
By deﬁnition, uniqueness up to deformation equivalence of Stein ﬁllings of
M implies uniqueness up to orientation preserving diﬀeomorphism of Stein ﬁllable
contact structures onM. By Corollary 11.21, it also implies uniqueness up to exact
symplectomorphism of Weinstein completions of the ﬁllings.
For two Stein structures on the same smooth cobordism W the diﬀerence be-
tween the notions of homotopy and deformation equivalence lies in the topology of
the group Diﬀ +(W ) of orientation preserving diﬀeomorphisms of W . For instance,
by a theorem of Cerf [ 30] the group Diﬀ +(B2n) of the closed unit ball B2n is
connected for n> 2, and hence there is no diﬀerence between homotopy and defor-
mation equivalence of Stein structures on the ballB2n ifn> 2. On the other hand,
it is unknown whether the group Diﬀ +(B4) is connected, and consequently we do
not know whether deformation equivalent Stein structures on B4 are homotopic.
In this section we will use the method of ﬁlling by holomorphic discs to establish
uniqueness up to deformation equivalence of Stein ﬁllings of certain smooth and
contact 3-manifolds.
Stein ﬁllings of S3. The following result, which is Theorem 1.7 from the
Introduction, ﬁrst appeared with a sketch of a proof in [47] (for the diﬀeomorphism
part see [83, 43, 133]).
Theorem 16.5. Let (W,J ) be a tame compact complex surface with J-convex
boundary diﬀeomorphic to S3. Suppose that W is minimal. Then W is diﬀeomor-
phic to the 4-ball. Moreover, (W,J ) admits a J-convex Morse function constant on
∂W with a unique critical point, the minimum.
Proof. Step 1. Let us ﬁrst show that the manifold W is diﬀeomorphic to
the ball. Note that it follows from [ 83], [43] and [133] that W is diﬀeomorphic to
a ball, possibly blown up in a few points. In order to see that it is actually a ball
we will use a theorem of Bogomolov and de Oliveira from [ 20]. Let us pick a collar
neighborhood C =M× [0,ε ]⊂W of the boundary M× 0 = M =∂W such that
the hypersurfaces Mr =M×r, r∈ [0,ε ], are J-convex. After deforming the collar
neighborhood near two points on Mε (using e.g. Proposition 2.12), we may assume
that Mε satisﬁes the following conditions:
(i) there exist two points q±∈Mε and holomorphic coordinates (z1,z 2) on
neighborhoods U±⊂ W of q± in which q± has coordinates (0,±i) and
Mε∩U± correspond to the following parts of the unit sphere {|z|2 =
|z1|2 +|z2|2 = 1}⊂ C2,
Mε∩U+ ={|z| = 1,y 2 > 1−ε}, M ε∩U− ={|z| = 1,y 2 <−1 +ε} ;
(ii) the hypersurface Mε\ (U+∪U−) is real analytic.

312 16. STEIN MANIFOLDS OF COMPLEX DIMENSION TWO
Hence, after replacing W by the region bounded by Mε, we may assume without
loss of generality that M =∂W itself, rather than Mε, satisﬁes properties (i) and
(ii).
The induced contact structure ξ on M∼=S3 is symplectically ﬁllable and thus
tight. By uniqueness of the tight contact structure on S3 (see [ 44]) it follows
that (M,ξ ) is diﬀeomorphic to S3 with its standard contact structure described
in Example 16.2. Hence M\{q+,q−} can be foliated by a family of 2-spheres St,
t∈ (−1, 1), each having exactly two complex points which are both elliptic. In the
above neighborhoods U±∩M these spheres can be chosen as the intersections of
M with the real hyperplanes y2 =t,t∈ (−1,−1 +ε)∪ (1−ε, 1). Moreover, we can
arrange that there exists a real analytic diﬀeomorphism f :∂D× [−1 +ε, 1−ε]→
M\ (U+∪U−) such that f(∂D×t) = St. Here D is the Levi-ﬂat 3-ball deﬁned
in (16.4).
By a theorem of Bogomolov and de Oliveira ([ 20], see Theorem 5.64 above)
there exists a C∞-small deformation of J to a complex structure ~J which is Stein.
In particular, W contains no nonconstant ~J-holomorphic spheres. So we can apply
Theorem 16.3 (b) to ~J. Hence the embedding f :∂D×[−1+ε, 1−ε]↪→M extends
to an embedding F :D× [−1 +ε, 1−ε]↪→W such that the 3-balls Bt :=F (D×t),
t∈ [−1 +ε, 1−ε), bounded by the spheres St are Levi-ﬂat and foliated by the
~J-holomorphic discs ∆t,s :=F
(
(D∩{x2 =s})×t
)
, s∈ (−1, 1).
We extend the family Bt to t∈ (−1, 1), by deﬁning Bt := W∩{y2 = t} for
t∈ (−1,−1 +ε)∪ (1−ε, 1) using the local coordinates above near the points q±.
By uniqueness of the holomorphic discs, the Bt ﬁt together smoothly at t = 1−ε
and t =−1 +ε, so F extends to a smooth embedding D× (−1, 1)↪→W . Denote
by B4⊂ C2 the unit ball and let p± := (0,±i). Composing F with the inverse of
the canonical diﬀeomorphism
D× (−1, 1)↦→B4\{p+,p−},
(
(z1,x 2),t
)
↦→
( z1√
1−t2, x2√
1−t2 +it
)
yields an embedding B4\{p+,p−} ↪→ W , which extends to an embedding B4 ↪→
W by sending p± to q±. Since this embedding induces a diﬀeomorphism on the
boundary and W is connected, it is a diﬀeomorphism.
Step 2. Now we switch back to the original complex stucture J. Since the
integral of a taming symplectic form over any nonconstantJ-holomorphic sphere is
positive, each such sphere must represent a nontrivial second homology class. AsW
is diﬀeomorphic to the ball by Step 1, this shows that W contains no nonconstant
J-holomorphic spheres. So we can repeat Step 1 with the original complex structure
J.
In particular, we assume that M =∂W satisﬁes conditions (i) and (ii) in Step
1. So we ﬁnd a collar neighborhood C =M× [0,ε ]⊂W of M =M× 0 such that
• the hypersurfaces Mr =M×r, r∈ [0,ε ] are J-convex;
• Mr∩U+ ={|z| = 1−r, y2 > 1−ε}, Mr∩U− ={|z| = 1−r, y2 <−1+ε},
see Figure 16.2. Deﬁne the smaller collars
C′ :=M× [0,ε
2]⊂C′′ :=M× [0, 3ε
4 ]⊂C.
LetF :D× (−1, 1)↪→W be the embedding constructed in Step 1. For σ,τ ∈ (0, 1)
setDσ :=D∩{|x2|≤ 1−σ} andWσ,τ :=F
(
Dσ× [−1 +τ, 1−τ]
)
, see Figure 16.3.

16.2. STEIN FILLINGS 313
M
M ε
2
y2
U+
1 − ε
C ′′
C ′
z1, x2
1 + ε
U−
Mε
M 3ε
4
Figure 16.2. The diﬀerent collars of M =∂W .
x2
1 − σ
Dσ
−1 + σ
z1
Figure 16.3. The truncated Levi-ﬂat 3-ball Dσ.

314 16. STEIN MANIFOLDS OF COMPLEX DIMENSION TWO
A1− ǫ
2
A1−ǫ
A−1+ǫ
A−1+ ǫ
2
B1− ǫ
2
A1−ǫ
W ′
A−1+ǫ
B−1+ ǫ
2
W ′′
Y
Figure 16.4. Deforming the foliation by Levi-ﬂat 3-balls Bt to a
foliation by J-convex 3-balls At.
Thus
Wσ,τ =
⋃
|t|≤1−τ
|s|≤1−σ
∆t,s.
Let us ﬁx σ,τ so small that ∂Wσ,τ ⊂ IntC′. Note that for each t ∈ (−1, 1)
the embedding Ft : D ↪→ W , Ft(z1,x 2) := F (z1,x 2,t ) is real analytic in x2 and
holomorphic in z1 on the set {z1 ⁄= 0}. Hence by Corollary 5.47, there exists
δ =δ(σ,τ )> 0 such that for any t∈ [−1 +τ, 1−τ] the embedding Ft|Dσ extends
to a holomorphic embedding
~Ft :Uσ,δ :={(z1,z 2)| (z1,x 2)∈Dσ,|y2|<δ}↪→W.
Deﬁne the i-convex hypersurface
A :={y2 =−δ(|z1|2 +x2
2), (z1,x 2)∈Dσ}⊂ Uσ,δ
and let At := ~Ft(A), see Figure 16.4. We have At⊂ IntC′ if t< −1 + ε
2, and if δ
is chosen small enough then At⊂ IntC fort> 1− ε
2. Also if σ is suﬃciently small
then ∂At⊂ IntC for all t∈ (−1, 1).
Note that for suﬃciently small δ all the hypersurfaces At are transverse to the
vector ﬁeldX :=F∗ ∂
∂t . Observe also that there exists a vector ﬁeld Y onC′′ which
is transverse to the hypersurfaces M×r for allr∈ [0, 3ε
4 ], and to At fort≥− 1 +ε.
Set W′ := ⋃
|t|≤1−ε
2
At and W′′ := ⋃
t∈[−1+ε
2,−1+ε]
At ⊂ W′. By Proposition 3.25
we ﬁnd a J-convex function ψ without critical points on W′ whose level sets are
transverse to X, and on C′′\W′′ also to Y . We can furthermore assume that its
level sets in W′′ coincide with the hypersurfaces At, t∈ [−1 + ε
2,−1 +ε]. Let φ

16.2. STEIN FILLINGS 315
be a J-convex function on C whose level sets are M×r,r ∈ [0,ε ]. By a target
reparametrization of the function φ we can arrange that on M× 3ε
4 we haveφ<ψ
and onM×ε
2 we haveφ>ψ . Hence, according to Corollary 3.20 and Remark 3.24,
the function smooth max(φ,ψ ) on W isJ-convex and has a unique non-degenerate
critical point, the minimum. □
As a consequence of Theorem 16.5, we obtain the following uniqueness result.
Theorem 16.6. Every Stein (or Weinstein) ﬁlling of S3 is deformation equi-
valent to the standard Stein structure
(
B4,i
)
on the closed unit ball B4⊂ C2. In
particular, all Stein structures on B4 are deformation equivalent.
Proof. Let (W,J ) be a Stein ﬁlling of S3. By Theorem 16.5, W is diﬀeomor-
phic to B4. Moreover, there exists a J-convex Morse function ψ constant on ∂W
with a unique critical point, the minimum. Thus ( W,J ) is deformation equivalent
to (B4,i ) by Proposition 11.26. The statement for Weinstein structures follows
from that for Stein structures and Theorem 13.5. □
Stein domains with reducible boundary. A 3-manifold M is called re-
ducible if it contains an embedded non-contractible 2-sphere S⊂M. The following
theorem allows us to decompose Stein domains with reducible boundary (see the
discussion below).
Theorem 16.7. Let (W,J ) be a tame compact complex surface with J-convex
boundary. Suppose that W contains no nonconstant J-holomorphic spheres. Let
S⊂∂W be an embedded 2-sphere. Then there exists a compact domain U⊂ IntW
with smoothJ-convex boundary such that the cobordismW\IntU admits aJ-convex
Morse function with exactly one critical point of index 1 whose unstable sphere in
∂W is smoothly isotopic to S.
Proof. By Theorem 16.4, after a C0-deformation of S we may assume that S
has exactly two complex points which are both elliptic. Moreover, we can assume
that S is real analytic. Hence we can apply Theorem 16.3 (a) to construct a Levi-
ﬂat ball B ⊂ W bounded by S and an embedding F : D ↪→ W which is real
analytic in the complement of the points (0 ,±1)∈ D, and holomorphic along the
discs ∆s ={x2 =s}∩ D, s∈ (−1, 1). Let us choose a collar C =M× [0,ε ]⊂W
of M = M× 0 such that each hypersurface M×t, t∈ [0,ε ], is J-convex, see
Figure 16.5. Set C′ := M× [0, ε
2]⊂ C. Fix σ >0 so small that F (∆s)⊂ IntC′
for|s|≥ 1−σ. By Corollary 5.47 there exists a δ >0 such that the real analytic
embedding F|D∩{|x2≤1−σ} extends to a holomorphic embedding ~F : Uσ,δ ↪→ W ,
where
Uσ,δ :={|z1|2 +x2
2≤ 1,|x2|≤ 1−σ,|y2|≤ δ}⊂ C2.
We can assume that ~F ({Uσ,δ∩{x2 = 1−σ})⊂C′. Consider the following vector
ﬁeld on C2:
X :=x1
∂
∂x1
+x2
∂
∂x2
+y1
∂
∂y1
−y2
∂
∂y2
.
By Lemma 8.47 (withC = 4/δ2 anda = 1) we ﬁnd ani-convex functionψ :Uσ,δ→
R with the following properties:
(i) ψ has a unique critical point at the origin, of index 1, with stable manifold
{x1 =x2 =y1 = 0} and unstable manifold{y2 = 0};

316 16. STEIN MANIFOLDS OF COMPLEX DIMENSION TWO
M
M × ε
2
M × ε
U
U
~Σ
C ′
C
B
~U
Figure 16.5. Decomposing a Stein domain with reducible boundary.
(ii) ψ has the hypersurface Σ := {y2
2 = δ2
4
(
1 +|z1|2 +x2
2
)
}⊂ Uσ,δ as one of
its level sets;
(iii) dψ(X)> 0 outside the origin;
(iv) ψ(z1,z 2) =ψ(z1, ¯z2).
Introduce
~U :=F (Uσ,δ), ~X := ~F∗X, ~Σ := ~F (Σ), ~ψ :=ψ◦ ~F−1 : ~U→ R.
Letφ :C→ R be a J-convex function with regular level sets M×t,t∈ [0,ε ]. Note
that if σ and δ are suﬃciently small then dφ(~X)> 0 in ~U∩C.
By a target reparametrization of the function φ we can arrange that φ|M×ε <
min ~ψ and φ|M×ε
2 > max ~ψ. Deﬁne a J-convex function ϑ : ~U∪C′→ R by
ϑ :=



~ψ on ~U\C,
smooth max(~ψ,φ ) on ~U∩C,
φ on C′,
see Figure 16.5. Since ~X·φ> 0 and ~X·~ψ >0 on ~U∩C, the functionϑ has a unique
index 1 critical point at ~F (0) and is constant on M. Set a := ϑ|~Σ∩(W\C) = ~ψ|~Σ.
Then the domain U :=W\{ϑ > a} and the function ϑ|W\IntU have the required
properties. □
Let us discuss the topological implications of Theorem 16.7. Recall that if W
is an elementary cobordism of dimension m with a unique index k critical point
p, then ∂+W is obtained from ∂−W by surgery on the stable sphere S−
p ⊂ ∂−W
(see e.g. [ 115]). More abstractly, surgery on an embedded ( k− 1)-sphere S in an
(m−1)-manifoldM with trivialized normal bundle consists of cutting out a tubular

16.2. STEIN FILLINGS 317
neighborhood Sk−1×Dn−k of S and gluing in Dk×Sn−k−1 via the identity. The
sphere corresponding to 0 ×Sn−k−1 in the resulting manifold is called the belt
sphere.
Thus, in the notation of Theorem 16.7, the boundary N := ∂U is obtained
fromM :=∂W by surgery on the sphere S, and conversely,M is obtained from N
by surgery on the stable sphere in N of the unique critical point in W\ IntU. To
understand this better, we distinguish two cases.
Case 1: M\S is connected. Then N is the connected manifold obtained by
cutting M open along S and gluing 3-balls to the two boundary spheres.
Case 2: M\S has two connected components with closures M1,M 2. Then
N =N1∐N2 is the disjoint union of the two manifolds obtained by gluing 3-balls
to the boundary spheres of M1,M 2 and M is the connected sum N1#N2. Now
there are again two cases.
Case 2a: None of theMi is diﬀeomorphic to the 3-ball. ThenM is the nontrivial
connected sum N1#N2 with none of the Ni diﬀeomorphic to the 3-sphere.
Case 2b: One of the Mi is diﬀeomorphic to the 3-ball. Then N =M∐S3 and
M is the trivial connected sum M#S3. In this case the domain U in Theorem 16.7
is diﬀeomorphic to W∐B4 and what we see is just the eﬀect of creating a pair of
critical points of index 0 and 1 for a J-convex function near the boundary of W .
Note that in Case 2b the sphere S ⊂ M is contractible, i.e., it bounds an
embedded 3-ball in M, while in Cases 1 and 2a it does not (so M is reducible).
Combining Theorem 16.7 with the Deformation Theorem 15.14, we obtain
Theorem 16.8. Suppose that a closed oriented 3-manifold N has a unique
Stein ﬁlling up to deformation equivalence, and M is obtained from N by surgery
on a 0-sphere. Then M has a unique Stein ﬁlling up to deformation equivalence as
well.
Proof. Let (W,J ) and (W′,J′) be two Stein ﬁllings of M. Applying Theo-
rem 16.7 to the belt sphere S⊂ M corresponding to the surgery on N, we ﬁnd a
compact domain U⊂ IntW with smooth J-convex boundary diﬀeomorphic to N
such that the cobordismW\IntU admits aJ-convex Morse functionφ with exactly
one critical point of index 1. Since (W,J ) is Stein, by Lemma 5.8 and interpolation,
the function φ extends (after target reparametrization) to a J-convex function on
W . Similarly we ﬁnd U′⊂ IntW′ and φ′ :W′→ R for (W′,J′).
By assumption the Stein domains (U,J,φ ) and (U′,J′,φ′) are deformation equi-
valent. So there exists a diﬀeomorphism h :U→U′ and a Stein homotopy (Jt,φt)
on U from (J,φ ) to (h∗J′,h∗φ′). After target reparametrization and adjustments
near ∂U we may assume that φt = φ near ∂U for all t∈ [0, 1]. We can extend
h over the elementary cobordism V := W\ IntU ∼= W′\ IntU′ to a diﬀeomor-
phism h : W → W′. Moreover, we can arrange that φ = φ′◦h on V . So we
obtain two subcritical Stein cobordism structures (V,J,φ ) and (V,h∗J′,h∗φ′ = φ)
with the same function which are connected by a Stein homotopy (Jt,φt =φ) near
∂−V = ∂+U. Hence by Theorem 15.14, after target reparametrization of φ, the
Stein homotopy extends from Op∂−V to a Stein homotopy ( V,Jt,φ ) connecting
(V,J,φ ) and (V,h∗J′,h∗φ′ = φ). This homotopy ﬁts together with the homotopy
onW to form a Stein homotopy (W,Jt,φ ) connecting (W,J,φ ) and (W,h∗J′,h∗φ′),
thus (W,J ) and (W′,J′) are deformation equivalent. □
Combining Theorems 16.8 and 16.6, we obtain

318 16. STEIN MANIFOLDS OF COMPLEX DIMENSION TWO
Theorem 16.9. (a) If two closed oriented 3-manifolds M1,M 2 have unique
Stein ﬁllings up deformation equivalence, then so does M1#M2.
(b) Any Stein ﬁlling of S2× S1 is deformation equivalent to the canonical
(subcritical) Stein structure onB3×S1 ={(z1,z 2)∈ C2| |z1|2+x2
2≤ 1}/y2∼y2+1
with J =i and φ(z1,z 2) =|z1|2 +x2
2.
(c) Any Stein ﬁlling of a k-fold connected sum S2×S1#··· #S2×S1, k≥ 1,
is deformation equivalent to the canonical (subcritical) Stein structure on the 4-ball
with k 1-handles attached.
Proof. Part (a) is just a special case of Theorem 16.8. As S2×S1 is ob-
tained from S3 by surgery on a 0-sphere, part (b) follows from Theorem 16.8 and
Theorem 16.6. Part (c) follows from (a) and (b). □
All the above results concerning uniqueness of Stein ﬁllings up to deformation
equivalence have Weinstein counterparts as in Theorem 16.6.
Stein ﬁllings of other 3-manifolds. We will use in this section the follow-
ing terminology. We say that a contact manifold ( M,ξ ) has a unique Stein ﬁlling
up to symplectomorphism if the following condition is satisﬁed. Suppose we are
given two Stein domains (W0,J 0,φ 0) and (W1,J 1,φ 1) such that the induced con-
tact structures on∂W0 and∂W1 are isomorphic to (M,ξ ). Let (ˆW0,ˆω0, ˆX0,ˆφ0) and
(ˆW1,ˆω1, ˆX1,ˆφ1) be Weinstein completions of the Weinstein domains W(W0,J 0,φ 0)
and W(W1,J 1,φ 1). Then there exists a symplectomorphismh : (ˆW0,ˆω0)→ (ˆW0,ˆω0)
which at inﬁnity sends the Liouville ﬁeld ˆX0 to the Liouville ﬁeld ˆX1. In particular,
h induces a contactomorphism at inﬁnity. Note that if ( M,ξ ) has a unique ﬁlling
up to Stein deformation equivalence, then by Corollary 11.21 it also has a unique
ﬁlling up to symplectomorphism.
The lens space L(p, 1) admits exactly ( p− 1) pairwise non-isotopic Stein-
ﬁllable contact structures, see [ 43, 67, 101, 95 ]. These give rise to [ p/2] pair-
wise non-contactomorphic structures. One of these [ p/2] structures is obtained as
the quotient of the standard contact structure on S3⊂ C2 by the diagonal action
(z1,z 2)↦→ (e
2πi
p z1,e
2πi
p z2). We will refer to this structure as standard. Thus the
standard structure is universally tight, i.e., its lift to the universal cover S3 is tight.
One can check that the lifts to S3 of all other contact structures on L(p, 1) are in
homotopy classes of plane ﬁelds diﬀerent from the class of the unique tight struc-
ture. Hence, according to [ 43] these lifts are overtwisted. So all non-standard tight
contact structures on L(p, 1) are virtually overtwisted, i.e., they lift to overtwisted
structures on the universal cover.
The following theorem is a combination of the results of several authors:
Theorem 16.10 (McDuﬀ [133], Plamenevskaya–Van Horn-Morris [159], Hind
[95]). All tight contact structures on L(p, 1), p≥ 2, have unique Stein ﬁllings up
to symplectomorphism, except for the standard structure on L(4, 1) which admits
exactly two (non-diﬀeomorphic) Stein ﬁllings. Moreover, the ﬁllings of the standard
structures are unique up to Stein deformation equivalence in each diﬀeomorphism
class.
The classiﬁcation up to symplectomorphism of Stein ﬁllings of the standard
structures is due to McDuﬀ [ 133], and up to Stein deformation equivalence it is
due to Hind [ 95]. The uniqueness result for ﬁllings of the virtually overtwisted

16.2. STEIN FILLINGS 319
structures is proven by Plamenevskaya and Van Horn-Morris [ 159], based on a
theorem of Wendl in [188].
Lisca [124] completely classiﬁed Stein ﬁllings up to diﬀeomorphism of all lens
spaces L(p,q ) endowed with a universally tight contact structure.
Remark 16.11. All the above results ﬁt into a general program relating the
classiﬁcation of Stein ﬁllings of certain contact manifolds to singularity theory.
Namely, if a contact 3-manifold appears as the link of an isolated normal complex
surface singularity, then one expects that all Stein ﬁllings are given by the Milnor
ﬁbers corresponding to diﬀerent irreducible components of the so-called miniversal
space of deformations of the singularity. For instance, the quotient singularity of
C2 by the diagonal action of Zp has irreducible deformation space, except in the
casep = 2 when there are exactly two irreducible components. This is the source of
McDuﬀ’s classiﬁcation result. N´ emethi and Popescu-Pampu [146] have shown that
Lisca’s Stein ﬁllings of lens spaces correspond exactly to the diﬀerent smoothings
of the associated cyclic quotient singularities of C2.
The 3-torus T 3 carries inﬁnitely many tight contact structures in the same
homotopy class of plane ﬁelds [ 68, 110]. By contrast, it was proved in [ 46] that
any Stein ﬁllable contact structure on T 3 is contactomorphic to the standard one
given by the ﬁeld of complex tangencies on the boundary of the Stein domain
T 2×D2 ={(z1,z 2)∈ C2|y2
1 +y2
2≤ 1}/(x1∼x1 + 1, x2∼x2 + 1).
Wendl has further improved this result and showed
Theorem 16.12 (Wendl [ 188]). The standard contact structure on T 3 has a
unique Stein ﬁlling up to symplectomorphism.
Not every contact 3-manifold ( M,ξ ) is Stein ﬁllable. First of all, the con-
tact structure ξ has to be tight (see [ 43]). Moreover, there is a long hierarchy
of diﬀerent degrees of ﬁllability of tight contact 3-manifolds with Stein ﬁllability
at the top, see [ 45, 54 ] for relevant discussions. On the other hand, there are
contact 3-manifolds which admit inﬁnitely many non-homeomorphic Stein ﬁllings,
see [156, 174]. Moreover, there are contact manifolds which admit inﬁnitely many
homeomorphic but non-diﬀeomorphic Stein ﬁllings, see [ 6].
It also turns out that certain 3-manifolds do not admit any Stein ﬁllings at all,
regardless of the contact structure they carry. The ﬁrst such example was obtained
by Lisca [ 123] who proved that the Poincar´ e homology sphere P with one of its
orientations admits no positive Stein ﬁllable contact structure. It then follows from
Theorem 16.7 that P #(−P ) has no Stein ﬁlling with either orientation. Etnyre
and Honda [56] improved Lisca’s result by showing thatP admits no positive tight
contact structure with the above orientation, and hence P #(−P ) admits no tight
contact structure at all. As far as we know there are no known examples of irre-
ducible orientable 3-manifolds which are not Stein ﬁllable with either orientation.
There are no known examples of diﬀerent Stein domain structures on the same
4-manifold with boundary which are homotopic as almost complex structures but
not deformation equivalent (or, more strongly, whose boundaries are not contac-
tomorphic). This is in sharp contrast to the situation in higher dimensions, as we
will see in Chapter 17.

320 16. STEIN MANIFOLDS OF COMPLEX DIMENSION TWO
16.3. Stein structures on 4-manifolds
In the previous section we proved uniqueness up to deformation equivalence of
Stein ﬁllings of certain 3-manifolds. In this section we derive from these results
uniqueness up to deformation equivalence of Stein manifolds with certain given
ends.
We need some topological preparation. We say that a topological space X
is of ﬁnite type if there exists a compact subset A⊂ X such that X\ IntA is
homeomorphic to ∂A× [0,∞). In this case we call ∂A an end of X.
Lemma 16.13. Any two ends of a ﬁnite type topological space are weakly ho-
motopy equivalent.
Proof. Let B =∂A and B′ =∂A′ be two ends of X. Then we ﬁnd compact
intervals I ⊂ J ⊂ [0,∞) and I′ ⊂ J′ ⊂ [0,∞) such that B×I ⊂ B′×I′ ⊂
M×J ⊂ M′×J′ under the homeomorphisms X\ IntA≈ B× [0,∞) and X\
IntA′≈ B′× [0,∞). Since the induced maps on homotopy groups πk(B×I)→
πk(B×J) and πk(B′×I′)→ πk(B′×J′) are isomorphisms, it follows that the
map πk(B′×I′)→πk(B×J) is an isomorphism as well. Thus for a∈I′ the map
B′≈ B′×a ↪→ B′×I′ ↪→ B×J → B induced by the obvious inclusions and
projections is a weak homotopy equivalence. □
Now we specialize to 4-manifolds. We say that a smooth oriented 4-manifold
V is of ﬁnite type if there exists a compact subset W⊂V with smooth boundary
such thatV\ IntW is diﬀeomorphic to ∂W× [0,∞). In this case we call the closed
oriented 3-manifold ∂W an end of V . It follows from Lemma 16.13 that the weak
homotopy type of an end of V is determined by the homeomorphism type of V .
Let us say that a closed oriented 3-manifold M is determined by its homotopy
type if every other closed oriented 3-manifold which is weakly homotopy equivalent
to M is actually diﬀeomorphic to M by an orientation preserving diﬀeomorphism.
Not every closed 3-manifold is determined by its homotopy type, counterexamples
being provided by certain lens spaces. On the other hand, Perelman’s proof of the
geometrization conjecture [158] implies
Theorem 16.14 (Perelman). The manifolds S3, S2×S1, RP 3, and connected
sums of these are determined up to orientation preserving diﬀeomorphism by their
homotopy type (in fact, by their fundamental group).
Proof. Let M be a closed orientable 3-manifold whose fundamental group is
a free product of copies of Z and Z2. It follows from Perelman’s work (see [ 141,
Theorem 0.1]) thatM is diﬀeomorphic to a connected sum of copies of S2×S1 and
spherical space forms. If π1(M) = 0 this implies that M is diﬀeomorphic to S3.
Otherwise, each spherical space form appearing in the connected sum must have
fundamental group Z2 and hence be diﬀeomorphic to RP 3, so M is diﬀeomorphic
to a connected sum of copies ofS2×S1 and RP 3 (with some orientations). Since all
the manifolds S3, S2×S1 and RP 3 admit orientation reversing diﬀeomorphisms,
we ﬁnd an orientation preserving diﬀeomorphism between M and the connected
sum of these manifolds with their standard orientations. □
The uniqueness results for Stein domains in Section 16.2 now imply uniqueness
results for ﬁnite type Stein structures on their interiors:

16.3. STEIN STRUCTURES ON 4-MANIFOLDS 321
Theorem 16.15. (a) Let W1,W 2 be compact oriented 4-manifolds with bound-
ary such that ∂W1#∂W2 is determined by its homotopy type. If ﬁnite type Stein
structures on the interiorsW1,W 2 are unique up to deformation equivalence, then so
are ﬁnite type Stein ﬁllings of the interior of the boundary connected sumW1#bW2
(the manifold obtained from W1∐W2 by attaching a 1-handle connecting W1 and
W2).
(b) LetW be a compact 4-manifold bounded byS3,S2×S1, RP 3, or a connected
sum of these. Suppose that IntW admits a ﬁnite type Stein manifold structure.
Then IntW is diﬀeomorphic to R4, R3×S1, T∗S2, or the interior of a boundary
connected sum of these, respectively, and the ﬁnite type Stein manifold structure on
IntW is unique up to deformation equivalence.
Proof. (a) Let (J,φ ) be a ﬁnite type Stein structure on Int (W1#bW2). Then
for suﬃciently large c the manifold {φ < c} is diﬀeomorphic to Int ( W1#bW2).
Since its end M1#M2 is determined by its homotopy type, the level set {φ =
c} is diﬀeomorphic to M1#M2. Now the claim follows from the corresponding
uniqueness result for the Stein domain {φ≤c} provided by Theorem 16.9 (a).
(b) Let (J,φ ) be a ﬁnite type Stein structure on Int W . Then for suﬃciently
large c the manifold{φ < c} is diﬀeomorphic to Int W . Since according to Theo-
rem 16.14 its end ∂W is determined by its homotopy type, the level set {φ = c}
is diﬀeomorphic to ∂W . Now the claim follows from the corresponding uniqueness
result for the Stein domain {φ≤ c} provided by Theorems 16.6, 16.10, and 16.9
(b). □
Combining Theorem 16.15 (b) with Corollary 11.27, we obtain the following
uniqueness result up to homotopy rather than just deformation equivalence.
Corollary 16.16. Any ﬁnite type Stein (or Weinstein) manifold structure on
R4 is homotopic to the standard structure. □
As we will see below (Corollary 17.5), R2n admits inﬁnitely many pairwise
non-homotopic (in fact, non-symplectomorphic) ﬁnite type Stein structures for any
n≥ 3.
Non-existence of Stein structures. An analogue of the Existence The-
orem 1.5 fails for 4-manifolds. For example, Theorem 16.15 implies the following
non-existence result.
Theorem 16.17. No ﬁnite type Stein surface is homeomorphic to S2× R2.
Proof. Suppose that (V,J,φ ) is a ﬁnite type Stein surface homeomorphic to
S2× R2. Then for suﬃciently large c the manifold{φ<c } is diﬀeomorphic to V .
Since according to Theorem 16.14 its end S2×S1 is determined by its homotopy
type, the level set {φ =c} is diﬀeomorphic to S2×S1. Hence Theorem 16.15 (b)
implies that V is diﬀeomorphic to R3×S1, which contradicts the hypothesis that
V is homeomorphic to S2× R2. □
Remark 16.18. In [125] Lisca and Mati´ c prove thatS2× R2, with its stan-
dard smooth structure, does not admit any (possibly inﬁnite type) Stein mani-
fold structure. Their proof requires the adjunction inequality of Kronheimer and
Mrowka [117], proven via Seiberg–Witten theory. As Lisca and Mati´ c show in [125],
this implies that any homologically nontrivial embedded 2-sphere in a Stein surface
must have self-intersection index≤− 2. See [ 74, 147, 148] for further discussion.

322 16. STEIN MANIFOLDS OF COMPLEX DIMENSION TWO
In sharp contrast to these non-existence results, Gompf [ 70] used the tech-
nique of Casson handles to prove an analogue of the Existence Theorem 1.5 for
4-manifolds, provided that the smooth structure is allowed to be changed (see The-
orem 1.6 in the introduction):
Every oriented open topological 4-manifold which admits a (possibly inﬁnite)
handlebody decomposition without handles of index > 2 is homeomorphic to a Stein
surface.
For example, this shows thatS2×R2 is homeomorphic to a Stein surface, which
in view of Theorem 16.17 is necessarily of inﬁnite type.
Gompf also proved a topological analogue of the Ambient Existence Theo-
rem 8.16:
Theorem 16.19 (Gompf [ 71]). An open subset U of a complex surface V is
topologically isotopic to a Stein open subset if and only if it is homeomorphic to the
interior of a handlebody without handles of index > 2.

17
Exotic Stein Structures
In this chapter we discuss how to distinguish Stein and Weinstein structures up
to deformation equivalence. The main tool for this is symplectic homology, which
turns out to be an invariant of Liouville manifolds up to Liouville homotopy. By
considering their underlying Liouville structures, symplectic homology thus gives
rise to a deformation invariant of Weinstein structures. In Section 17.2, we explain
constructions of inﬁnitely many pairwise non-deformation equivalent Stein struc-
tures on the same manifold that are distinguished by their symplectic homology.
17.1. Symplectic homology
In this section we recall the deﬁnition of symplectic homology and some of its
properties. For details we refer to [ 34, 57, 137, 169, 185 ]. We ﬁx a coeﬃcient
ring R with unit.
We begin with the completion ( V,λ ) of a Liouville domain ( W,λ|W ). Recall
that λ = erα on V\W ∼= R+×∂W , where α = λ|∂W . Consider a Hamiltonian
function H :V → R which outside a compact set is of the form H(r,x ) =h(r) for
a function h : R+→ R satisfying h′′≥ 0 and h′(r)→∞ and r→∞ . Deﬁne the
action functionalAH :C∞(S1,V )→ R by
AH(x) :=
∫ 1
0
x∗λ−
∫ 1
0
H
(
x(t)
)
dt.
Its critical points are 1-periodic solutions of the Hamiltonian system ˙ x = XH(x),
whereXH is the Hamiltonian vector ﬁeld deﬁned byiXHdλ =−dH. Pick an almost
complex structureJ onV which is compatible with ω in the sense that g =ω(·,J·)
is a Riemannian metric. Moreover, we require that outside a compact set J is
invariant under translation along R+, maps ∂r to the Reeb vector ﬁeld Rα, and
preserves the contact structure ξ = kerα. Gradient ﬂow lines of AH with respect
to theL2-metric on the loop space induced by the metricg are mapsu : R×S1→V
satisfying the Floer equation
∂su +J(u)
(
∂tu−XH(u)
)
= 0.
To deﬁne Floer homology, we need to pick generic time-dependent perturbations of
(H,J ). Since the result does not depend on these perturbations, we will suppress
them from our discussion. Then let CF∗ be the free R-module generated by the
critical points on AH. It is Z2-graded, and Z-graded if c1(V ) = 0, by the Conley-
Zehnder indices of 1-periodic orbits. The boundary operator ∂ :CF∗→CF∗−1 is
deﬁned on generators by
∂x :=
∑
y
⟨x,y⟩y,
323

324 17. EXOTIC STEIN STRUCTURES
where⟨x,y⟩ is the signed count of isolated gradient ﬂow lines fromy tox. It satisﬁes
∂2 = 0 and its homology HF∗ does not depend on the choices of ( H,J ) (within
the classes described above). So HF∗ is an invariant of the Liouville domain; we
denote it by SH∗(W,λ ) and call it the symplectic homology of (W,λ ).
Next one observes [169] that two Liouville domains with the same completion
have isomorphic symplectic homology, so symplectic homology yields an invariant of
ﬁnite type Liouville manifolds which we still denote by SH∗(V,λ ). Moreover, sym-
plectic homology is invariant under Liouville isomorphisms, i.e., diﬀeomorphisms
f :V0→V1 between ﬁnite type Liouville manifolds (V0,λ 0) and (V1,λ 1) such that
f∗λ1−λ0 is exact and compactly supported. (This diﬀers slightly from the def-
inition in [ 169] where f∗λ1−λ0 is required to be the diﬀerential of a compactly
supported function). Since by Proposition 11.8 homotopies of Liouville domains
gives rise to Liouville isomorphisms of their completions, symplectic homology de-
ﬁnes a homotopy invariant of Liouville domains.
For a Liouville subdomain W in a ﬁnite type Liouville manifold ( V,λ ) the
inclusion ι : W ↪→ V induces a homomorphism ι# : SH∗(V,λ )→ SH∗(W,λ|W ).
The transfer mapι# was introduced by Viterbo [185] and it is functorial for nested
inclusions. It allows us to extend the deﬁnition of symplectic homology to Liouville
manifolds (V,λ ) that are not of ﬁnite type as follows. Pick an exhaustion V =⋃
k∈NVk by Liouville subdomains and use the transfer maps to deﬁne the inverse
limit
SH∗(V,λ ) := lim
←−
SH∗(Vk,λ|Vk).
Functoriality of the transfer map shows that this does not depend on the cho-
sen exhaustion. A similar argument shows that symplectic homology of Liou-
ville manifolds is invariant under exact symplectomorphisms, i.e., diﬀeomorphisms
f :V0→V1 between Liouville manifolds (V0,λ 0) and (V1,λ 1) such thatf∗λ1−λ0 is
exact. Since by Proposition 11.8 homotopies of Liouville manifolds give rise to exact
symplectomorpisms, symplectic homology deﬁnes a homotopy invariant of Liouville
manifolds. Note that for a ﬁnite type Liouville manifold the new deﬁnition in terms
of the inverse limit is canonically isomorphic to the earlier one. This concludes the
deﬁnition of symplectic homology, which we summarize in the following
Proposition 17.1. Symplectic homology associates to every Liouville manifold
(V,λ ) a Z2-graded (Z-graded if c1(V ) = 0) R-moduleSH∗(V,λ ) which is invariant
under exact symplectomorphisms as well as Liouville homotopies. The inclusion
ι : W ↪→ V of a Liouville subdomain W in a Liouville manifold (V,λ ) induces a
transfer map ι# :SH∗(V,λ )→SH∗(W,λ|W ).
Let us now discuss some further properties of symplectic homology that will
be relevant in the sequel. To simplify notation, we will usually drop λ from the
notation.
(1) Symplectic homology comes with a canonical map (where dim V = 2n)
Hn−∗(V ;R)→SH∗(V )
which behaves naturally with respect to the maps in Proposition 17.1.
(2) The pair-of-pants product on Floer homology induces a product on sym-
plectic homology which makes SHn−∗(V ) a graded commutative R-algebra with
unit. The unit is the image of 1 ∈H0(V ;R) under the canonical map H0(V ;R)→
SHn(V ). The maps in Proposition 17.1 and in (1) are algebra homomorphisms.

17.2. EXOTIC STEIN STRUCTURES 325
Note that the unit in SH∗(V ) is zero if and only if SH∗(V ) = {0}. Since the
transfer map sends the unit to the unit, this has the following useful consequence
ﬁrst pointed out by McLean [ 137]: For a Liouville subdomain W in a Liouville
manifold V , vanishing of SH∗(V ) implies vanishing of SH∗(W ).
(3) A somewhat diﬀerent vanishing result is proved in [35, 162]: For a Liouville
subdomain W in a Liouville manifold V , Hamiltonian displaceability of W in V
implies vanishing of SH∗(W ). For example, in the stabilization ( V× C,λ +λst)
(where λst = 1
2(xdy −ydx ) on C) of a Liouville manifold ( V,λ ) each compact
set is displaceable, so any Liouville subdomain of V× C has vanishing symplectic
homology.
(4) Attaching a Weinsteink-handle along a Legendrian (k− 1)-sphere Λ⊂∂W
to a Liouville domain W yields a new Liouville domain W∪ΛHk which contains
W as a Liouville subdomain. It has been proved in [ 32] that the transfer map
ι# : SH∗(W∪ΛHk)→ SH (W ) is an isomorphism in the subcritical case k < n.
For example, this implies that every subcritical Weinstein manifold has vanishing
symplectic homology. (Note that this also follows from the vanishing result in (3)
and the Splitting Theorem 14.16 above.)
A special case of subcritical handle attaching is the boundary connected sum
W1#bW2 of two Liouville domains of dimension 2 n ≥ 4. This is the result of
attaching a 1-handle to W1∐W2 connecting two points pi∈∂Wi. It follows that
SH∗(W1#bW2)∼=SH∗(W1)⊕SH∗(W2) as an R-algebra.
(5) The behaviour of symplectic homology under attaching of a critical handle
is more complicated. An answer is given in [ 24] in the form of a surgery exact
sequence
(17.1) ··· SH∗(W∪ΛHn)
ι#
−→SH∗(W )−→LHHo
∗ (Λ)−→SH∗−1(W∪ΛHn)···
(At the time of writing this book, the proof of this result is not yet completed;
in particular, the compatibility of the maps with the product structures is not yet
established). Here LHHo
∗ (Λ) is a version of Legendrian contact homology which is
in general diﬃcult to compute. We will see in the next section examples where this
computation is possible.
(6) The ﬁrst nontrivial computation of symplectic homology was carried out
for cotangent bundles [185, 165, 1, 2]: Let M be a closed manifold and denote by
LM =C0(S1,M ) its loop space. Then there is an isomorphism
SH∗(T∗M,pdq )∼=H∗(LM;R)
which relates the pair-of-pants product on SH∗(T∗M) to the Chas-Sullivan loop
product on H∗(LM;R). In particular, we have SH∗(T∗M)⁄= 0. As an application,
consider a closed exact (i.e., λ|L is exact) Lagrangian submanifold L in a Liouville
manifold (V,λ ). Then Weinstein’s Lagrangian neighborhood theorem yields an
exact symplectic embedding of the unit codisc bundleD∗L intoV . So the vanishing
results in (2) and (3) imply that, in this situation, SH∗(V ) ⁄= 0 and L is not
Hamiltonian displaceable in V . (In particular, we recover Gromov’s theorem on
the non-existence of closed exact Lagrangian submanifolds in Cn).
17.2. Exotic Stein structures
By an “exotic” Stein structure one means a Stein structure on a manifold such
as Cn which is not deformation equivalent to the standard one. The ﬁrst examples
of exotic Stein structures on C2m, m≥ 2, were constructed in 2005 by Seidel and

326 17. EXOTIC STEIN STRUCTURES
Smith [167]; they were distinguished from the standard structure by the presence of
a non-displaceable Lagrangian torus. In 2009 McLean [ 137] constructed inﬁnitely
many pairwise non deformation equivalent Stein structures on Cn and T∗M for
n = dimM≥ 4, distinguished by their symplectic homologies. Other constructions
of exotic Stein structures are given in [ 131, 132, 3 ]. In particular, Abouzaid and
Seidel [3] have extended McLean’s result to the case n = 3.
In this section we will discuss McLean’s theorem and explain how, combined
with the surgery exact sequence from [ 24], it leads to the following
Theorem 17.2. Let (V,J ) be an almost complex manifold of real dimension
2n ≥ 6 which admits an exhausting Morse function with ﬁnitely many critical
points all of which have index ≤n. Then V carries inﬁnitely many ﬁnite type Stein
structures (Jk,φk), k∈ N, such that the Jk are homotopic to J as almost complex
structures and (Jk,φk), (J𝓁,φ𝓁) are not deformation equivalent for k⁄=𝓁.
We begin by recalling McLean’s theorem [ 137]. In this section we denote by
SH∗(V ) symplectic homology (of a Liouville manifold V ) with coeﬃcient ring Z2.
Recall from the previous section thatSHn−∗(V ) is a graded commutative ring with
unit. Following [137], we associate to every Liouville manifold V the quantity
i(V ) := number of idempotent elements in SHn−∗(V ).
The properties of symplectic homology imply the following properties of i(V ):
(a)i(V ) (which may be inﬁnite) is invariant under exact symplectomorphisms;
in particular, it deﬁnes a deformation invariant of Stein manifolds.
(b) If SH∗(V ) = {0} then 0 is the only idempotent and thus i(V ) = 1; if
SH∗(V ) ⁄= {0} then the unit and 0 deﬁne two diﬀerent idempotents and thus
i(V )≥ 2.
(c) For the end connected sum (i.e., the completion of the boundary connected
sum of the underlying Liouville domains) of two ﬁnite type Liouville manifolds
V1,V 2 of dimension 2n≥ 4 we have
i(V1#eV2) =i(V1)i(V2).
Now we can state McLean’s theorem.
Theorem 17.3 (McLean [ 137], Abouzaid–Seidel [ 3]). For every n≥ 3 there
exists a ﬁnite type Stein manifoldKn of complex dimensionn which is diﬀeomorphic
to Cn and satisﬁes 1<i (Kn)<∞.
By the preceding discussion, this immediately implies
Corollary 17.4 ([137, 3]). Let (V,J 0,φ 0) be any ﬁnite type Stein manifold
of complex dimension n≥ 3 with i(V )<∞. Then the end connected sums
Vk :=V #eKn#e··· #eKn
with k≥ 0 copies of Kn deﬁne ﬁnite type Stein structures (Jk,φk) on V with the
following properties:
• Jk is homotopic to J0 as almost complex structures;
• i(Vk) = i(V )i(Kn)k and hence the Stein structures (Jk,φk), (J𝓁,φ𝓁) are
not deformation equivalent for k⁄=𝓁.
In particular, by properties (4) and (6) in Section 17.1 the standard Stein
structures on Cn and T∗M satisfy i(Cn) = 1 and i(T∗M) = 2 c, where c is the
number of connected components of M, so Corollary 17.4 yields

17.2. EXOTIC STEIN STRUCTURES 327
Corollary 17.5 ([ 137, 3 ]). On Cn and T∗M, n = dim M ≥ 3, there ex-
ist inﬁnitely many ﬁnite type Stein structures that are pairwise not deformation
equivalent.
For the proof of Theorem 17.2 we need one more ingredient.
Theorem 17.6 ([24]). Let (V,J,φ ) be any ﬁnite type Stein manifold of complex
dimension n≥ 3. Then there exists a ﬁnite type Stein structure (J′,φ′) on V such
that J′ is homotopic to J as almost complex structures and SH∗(V,J′,φ′) ={0}.
Proof. (V,J ) is obtained from a subcritical Weinstein domainW by attaching
k≥ 0n-handles along disjoint Legendrian (n−1)-spheres Λ1,... Λk⊂∂W . Since W
is subcritical its symplectic homology vanishes. Now it is explained in [ 24, Section
6.2] that each Λ i can be modiﬁed to a new Legendrian ( n− 1)-sphere Λ′
i⊂ ∂W
with the following properties:
• attachingn-cells toW along Λ′
1,..., Λ′
k yields a Stein manifold (V′,J′,φ′)
diﬀeomorphic to V ;
• the pullback of J′ under the diﬀeomorphism V →V′ is homotopic to J
as almost complex structure;
• the Legendrian contact homologies LHHo
∗ (Λ′
i) vanish.
Hence the surgery exact sequence (17.1) implies vanishing of SH∗(V′,J′,φ′). □
Proof of Theorem 17.2. By the Existence Theorem 1.5 there exists a ﬁnite
type Stein structure (J0,φ 0) onV such thatJ0 is homotopic toJ as almost complex
structure. After applying Theorem 17.6, we may assume that SH∗(V,J 0,φ 0) ={0}
and thus i(V,J 0,φ 0) = 1. Now Corollary 17.4 yields inﬁnitely many ﬁnite type
Stein structures ( Jk,φk), k∈ N, on V such that the Jk are homotopic to J as
almost complex structures and (Jk,φk), (J𝓁,φ𝓁) are not deformation equivalent for
k⁄=𝓁. □



APPENDIX A
Some Algebraic Topology
In this appendix we collect some standard facts from algebraic topology that
are used in the book.
A.1. Serre ﬁbrations
In this section we collect some facts about Serre ﬁbrations that are used in the
book, see [ 91] for further discussion. Throughout all spaces are topological spaces
and all maps are continuous.
Consider a map π :E→B. A map ~f :X→E is called a lift of f :X→B if
π◦~f =f. We say thatπ has the lift extension property for a space pair (X,A ) if any
mapX→B has a lift X→E extending any given liftA→E. Let I := [0, 1]. The
homotopy lifting property ofπ for a space pair (X,A ) is the lift extension property
for the pair ( I×X, 0×X∪I×A), i.e., any homotopy I×X → B has a lift
I×X→ E extending any given lift 0 ×X∪I×A→ E. The homotopy lifting
property for a space X is the homotopy lifting property for the pair ( X, ∅).
We denote by Dk the closed unit disc in Rk. Note that the homotopy lifting
property for Dk implies the homotopy lifting property for all D𝓁, 𝓁≤ k. Since
the pair (I×Dk, 0×Dk∪I×∂Dk) is homeomorphic to ( I×Dk, 0×Dk), the
homotopy lifting property forDk implies the homotopy lifting property for the pair
(Dk,∂Dk), and hence for all k-dimensional CW pairs.
The homotopy lifting property for a point is also called thepath lifting property.
It implies surjectivity ofπ ifB is path connected (and of course E nonempty). The
mapπ is called a Serre ﬁbration if it has the homotopy lifting property for all closed
k-discs Dk.
Let us ﬁx pointse∈E andb =π(e)∈B and deﬁne the “ﬁber”F :=π−1(b). In
the following all homotopy groups are taken with base points e resp. b. We denote
byDk
1/2 the disc of radius 1/2.
Lemma A.1. Suppose thatB is path connected andπ :E→B has the homotopy
lifting property for Dk−1, for some k≥ 1. Then the following are equivalent:
(a) the induced map π∗ on homotopy groups is injective on πk−1 and surjective
on πk;
(b) πk−1F = 0;
(c) any map f : Dk→ B with f|Dk
1/2
≡ b has a lift Dk→ E extending any
given lift ∂Dk→E.
Remark A.2. Up to the technical condition f|Dk
1/2
≡b, part (c) is just the lift
extension property for the pair (Dk,∂Dk). Now any map f :Dk→B is homotopic
rel ∂Dk to one which is constant on Dk
1/2. Hence, if π has the homotopy lifting
329

330 A. SOME ALGEBRAIC TOPOLOGY
property for the pair (Dk,∂Dk), then part (c) can be replaced by the lift extension
property for the pair (Dk,∂Dk).
Proof. The homotopy lifting property forDk−1 allows us to deﬁne a connect-
ing homomorphism ∂ :πkB→πk−1F such that we get an exact sequence
πkF→πkE
π∗
→πkB
∂
→πk−1F→πk−1E
π∗
→πk−1B.
The equivalence of (a) and (b) follows from this sequence. (b) follows from (c)
applied to the map Dk→ b∈ B and a lift ∂Dk→ F . To show that (b) implies
(c), consider a map f : Dk→ B with f|Dk
1/2
≡ b and a lift ~f : ∂Dk→ E. By the
homotopy lifting property for Sk−1, the map ~f extends to a lift ~f :Dk\Dk
1/2→E.
Since πk−1F = 0, the map ~f|∂Dk
1/2
: ∂Dk
1/2→ F extends to a map ~f : Dk
1/2→ F ,
so altogether we get the desired lift ~f :Dk→E. □
In particular, Lemma A.1 for all k≥ 1 together with Remark A.2 yields
Corollary A.3. Suppose that B is path connected and π :E→B is a Serre
ﬁbration. Then the following are equivalent:
(a) π is a weak homotopy equivalence;
(b) the ﬁber F is weakly contractible;
(c) for each k≥ 1, any map Dk→B has a lift Dk→E extending any given
lift ∂Dk→E.
Recall the following standard construction from topology (see e.g. [ 91]). Given
a map f :X→Y deﬁne the space
P :={(x,γ )|x∈X, γ : [0, 1]→Y, f(x) =γ(0)}.
Note that this is just the ﬁber product over Y of X and the path space of Y . It is
easy to see that the inclusion
X ↪→P, x ↦→
(
x,f (x)
)
,
where f(x) denotes the constant path at f(x), is a deformation retract and
π :P→Y, (x,γ )↦→γ(1)
deﬁnes a Serre ﬁbration. Its ﬁber at y∈Y
F :={(x,γ )|x∈X, γ : [0, 1]→Y, f(x) =γ(0), γ(1) =y}
is called the homotopy ﬁber of f. In particular, we get a homotopy exact sequence
···→ πkF→πkX
f∗
→πkY →πk−1F→···
and Corollary A.3 implies
Corollary A.4. Consider f :X→Y and deﬁne the Serre ﬁbration π :P→
Y as above. Suppose that Y is path connected. Then the following are equivalent:
(a) f is a weak homotopy equivalence;
(b) the homotopy ﬁber F is weakly contractible;
(c) for each k≥ 1, any map Dk→Y has a lift Dk→P extending any given
lift ∂Dk→P .

A.2. SOME HOMOTOPY GROUPS 331
More generally, consider a commuting triangle
(A.1) X
πX
  @@@@@@@@
f //Y
πY
~~~~~~~~~
B
For each b∈ B we get an induced map fb := f|Xb : Xb = π−1
X (b)→ Yb = π−1
Y (b).
Deﬁne the spaces
Pb :={(x,γ )|x∈Xb, γ: [0, 1]→Yb, f(x) =γ(0)},
P :={(x,γ )|x∈X, γ : [0, 1]→YπX(x), f(x) =γ(0)} =
⋃
b∈B
Pb.
The inclusion
X ↪→P, x ↦→
(
x,f (x)
)
is again a deformation retract. The projection
πP :P→Y, (x,γ )↦→γ(1)
will in general not be a Serre ﬁbration. Note, however, that the ﬁbers at y∈Y of
πP :P→Y and its restriction πP,b :Pb→Yb, where b =πY (y), both equal
F ={(x,γ )|x∈Xb, γ: [0, 1]→Yb, f(x) =γ(0), γ(1) =y}.
Hence Lemma A.1 and Remark A.2 imply
Corollary A.5. Consider a commuting triangle as in (A.1) and deﬁne πP :
P→Y and πP,b :Pb→Yb as above. Suppose that Y is path connected and πP has
the homotopy lifting property for Dk−1, for some k≥ 1. Then the following are
equivalent:
(a) the induced map f∗ on homotopy groups is injective on πk−1 and surjective
on πk;
(b) πk−1F = 0;
(c) any map g :Dk→Y with πY◦g|Dk
1/2
≡b has a lift Dk→P extending any
given lift ∂Dk→P ;
(d) the induced map (fb)∗ on homotopy groups is injective on πk−1 and surjec-
tive on πk;
(e) any mapg :Dk→Yb has a liftDk→Pb extending any given lift∂Dk→Pb.
Corollary A.6. Consider a commuting triangle as in (A.1) and deﬁne πP :
P → Y as above. Suppose that Y is path connected and πP is a Serre ﬁbration.
Then the following are equivalent:
(a) f :X→Y is a weak homotopy equivalence;
(b) the homotopy ﬁber F is weakly contractible;
(c) fb :Xb→Yb is a weak homotopy equivalence.
A.2. Some homotopy groups
In this section we collect some results on homotopy groups that are used in this
book. The following lemma will be useful.

332 A. SOME ALGEBRAIC TOPOLOGY
Lemma A.7. Let p :E→B be a Serre ﬁbration with ﬁber F =p−1(b). Then
the map p : (E,F )→ (B,b ) induces an isomorphism of homotopy groups
p∗ :πi(E,F )→πi(B).
Proof. The long exact sequences of the pair (E,F ) and of the Serre ﬁbration
F→E→B ﬁt into a diagram
··· πi(F ) −−−−→πi(E) −−−−→πi(E,F )
∂
−−−−→πi−1(F )···
↓id
↓id
↓p∗
↓id
··· πi(F ) −−−−→πi(E) −−−−→πi(B)
∂
−−−−→πi−1(F )···
The deﬁnition of the boundary maps ∂ shows that this diagram commutes, so by
the ﬁve-lemma p∗ is an isomorphism. □
For 1≤k≤n denote by Vn,k the Stiefel manifold of orthonormal k-frames in
Rn, and byGn,k the Grassmannian ofk-dimensional subspaces in Rn. The obvious
projection p :Gn,k→Vn,k deﬁnes a ﬁbration
O(k)→Vn,k→Gn,k
with ﬁber the orthogonal group O(k). For 𝓁 < k≤ n the map Vn,k→ V𝓁,k that
forgets the last k−𝓁 vectors deﬁnes a ﬁbration
Vn−𝓁,k−𝓁→Vn,k→Vn,𝓁.
Here an explicit inclusion Vn−𝓁,k−𝓁 ↪→ Vn,k is given by adding to a ( k−𝓁)-frame
in Rn−𝓁×{ 0}⊂ Rn the last 𝓁 standard basis vectors. Note that Vn,n∼=O(n) and
Vn,1∼=Sn−1. Thus the preceding ﬁbration includes the following special cases:
Vn−1,k−1→Vn,k→Sn−1,(A.2)
O(n−k)→O(n)→Vn,k,(A.3)
O(n− 1)→O(n)→Sn−1.(A.4)
Of course, the preceding discussion carries over to the complex case: Just replace
everywhere Vn,k by the complex Siefel manifold V C
n,k, Gn,k by the complex Grass-
mannianGC
n,k,O(n) by the unitary groupU(n), andSn−1 byS2n−1. Moreover, the
ﬁbrations for the real and complex Stiefel manifolds ﬁt into the following commuting
diagram, where the vertical maps are the natural inclusions:
V C
n−1,k−1 −−−−→V C
n,k −−−−→S2n−1
↓
↓
↓id
V2n−1,k−1 −−−−→V2n,k −−−−→S2n−1.
Lemma A.7 applied to this diagram yields
Corollary A.8. (a) For i≤ 2n− 2 we have
πi(V C
n,k,V C
n−1,k−1)∼=πi(V2n,k,V 2n−1,k−1)∼=πi(S2n−1) = 0.
(b) For i = 2n− 1 the inclusion (V C
n,k,V C
n−1,k−1) ↪→ (V2n,k,V 2n−1,k−1) induces an
isomorphism
Z∼=π2n−1(V C
n,k,V C
n−1,k−1)→π2n−1(V2n,k,V 2n−1,k−1)∼= Z.

A.2. SOME HOMOTOPY GROUPS 333
The following lemma gives more information about the homotopy groups of
Stiefel manifolds.
Lemma A.9. (a) The map πiVn−1,k−1→ πiVn,k induced by the inclusion is
an isomorphism for i < n− 2 and surjective for i = n− 2. Similarly, the map
πiV C
n−1,k−1→πiV C
n,k is an isomorphism for i< 2n−2 and surjective for i = 2n−2.
(b) Vn,k is (n−k− 1)-connected andV C
n,k is (2n− 2k)-connected.
(c) For n≥k + 2, the group πkVn,n−k equals Z if k is even or k = 1, and Z2
if k> 1 is odd.
Proof. Part (a) follows directly from the long exact sequence of the ﬁbra-
tion (A.2) because Sn−1 is (n− 2)-connected. For part (b), let i<n −k. Then it
follows by induction from part (a) that πiVn,k = πiVn−k+1,1 = πiSn−k = 0. The
complex cases are analogous.
For part (c), letn≥k + 2 andk≥ 2 (the case k = 1 is trivial). Then it follows
by induction from part (a) thatπkVn,n−k =πkVk+2,2. Now observe that an element
of Vk+2,2 is a unit vector in Rk+2 and a second unit vector orthogonal to the ﬁrst
one. Thus Vk+2,2 equals the tangent sphere bundle of Sk+1 and the ﬁbration (A.2)
Vk+1,1∼=Sk→Vk+2,2→Sk+1
describes this bundle. Now for an oriented sphere bundle Sk → E → B, the
boundary mapπk+1B→πkSk∼= Z in the long exact sequence is given by evaluation
of the Euler class e(E)∈Hk+1(B) (this follows directly from the deﬁnition of the
obstruction cocycle representing the Euler class in [177]). Thus the ﬁbration above
yields an exact sequence
πk+1Sk+1∼= Z
·χ(Sk+1)
−→ πkSk∼= Z→πkVk+2,2→ 0,
where the ﬁrst map is multiplication with the Euler characteristic of Sk+1. Since
χ(Sk+1) is 0 for k even and 2 for k odd, it follows that πkVn,n−k =πkVk+2,2 equals
Z for k even and Z2 for k odd. □
Setting k =n in Lemma A.9 (a) we ﬁnd
Corollary A.10. The map πiO(n− 1)→ πiO(n) induced by the inclusion
is an isomorphism for i < n− 2 and surjective for i = n− 2. Similarly, the map
πiU(n−1)→πiU(n) is an isomorphism for i< 2n−2 and surjective fori = 2n−2.
Deﬁne the stable homotopy groups πiO := πiO(n) for i < n− 1 and πiU :=
πiU(n) for i < 2n (this is independent of n by the preceding corollary). These
groups are determined by the celebrated
Theorem A.11 (Bott periodicity theorem [21]). (a) The stable homotopy group
πiU equals 0 if i is even and Z if i is odd.
(b) The stable homotopy group πiO equals Z2 if i≡ 0 or 1 (mod 8), Z if i≡ 3
or 7 (mod 8), and 0 otherwise.
We conclude this section with two lemmas from [ 143] that we will need in
Appendix B.
Lemma A.12. The homomorphism i : πn+1U(n)→ πn+1V2n+1,n is trivial for
n⁄= 2, and a surjection Z→ Z/2 for n = 2.

334 A. SOME ALGEBRAIC TOPOLOGY
Proof. If n is odd the homomorphism πn+1U(n)→ πn+1V2n+1,n is trivial
simply because πn+1U(n) = 0. Suppose now that n is even. The inclusion map
U(n)→V2n+1,n factors as U(n)→O(2n + 1)→V2n+1,n. Consider the homotopy
exact sequence
(A.5) πn+1O(2n + 1)
p
→πn+1V2n+1,n
δ
→πnO(n + 1)
j
→πnO(2n + 1)
of the ﬁbration O(n + 1)→O(2n + 1)→V2n+1,n. Recall the geometric description
of ker(j) from [ 177],§23: Gluing two trivial bundles over the ( n + 1)-disc by a
map Sn→ O(m) yields a 1-1 correspondence between πnO(m) and isomorphism
classes of O(m)-bundles over Sn+1. Since πnO(n + 2) = πnO(2n + 1) = πnO by
Corollary A.10, the kernel of j classiﬁes stably trivial rank (n + 1) oriented vector
bundles over Sn+1. Next observe that the bundle O(n + 1)→ O(n + 2)→ Sn+1
is the bundle of orthonormal frames in the tangent bundle of Sn+1. So in the
associated exact sequence
πn+1Sn+1→πnO(n + 1)
j
→πnO(n + 2)∼=πnO(2n + 1)
the image of the generator of πn+1Sn+1 (which generates ker j) corresponds to
the gluing map of the tangent bundle of Sn+1. This shows that ker j is trivial
if and only the tangent bundle of Sn+1 is trivial, which is the case exactly for
n = 2 or n = 6 (see [ 23, 111 ]). Since πn+1V2n+1,n = Z/2, the sequence (A.5)
then implies that for n⁄= 2, 6 the homomorphism p, and hence the homomorphism
i :πn+1U(n)→πn+1V2n+1,n, is trivial.
It remains to consider the cases n = 2 and n = 6. In both cases the homotopy
groupsπn+1U(n) andπn+1O(2n+1) are in the stable range, so the Bott Periodicity
Theorem A.11 yields πn+1U(n) = πn+1U = πn+1O(2n + 1) = πn+1O = Z. More-
over, it is shown in [21] that the quotientO/U is homotopy equivalent to the based
loop space Ω O, hence the relative homotopy group πn+1(O/U) = πn+1(ΩO) =
πn+2O vanishes for n = 2 and equals Z2 for n = 6. It follows that for n = 6 the
exact sequence
πn+1U→πn+1O→πn+1(O/U)→πnU
takes the form Z→ Z→ Z/2→ 0. Hence the homomorphism πn+1U→ πn+1O,
and thereforeπn+1U(n)→πn+1O(2n + 1), is multiplication by 2. But then the ho-
momorphismU(n)→O(2n+ 1)→V2n+1,n = Z/2 is trivial. For n = 2 we conclude
that the map πn+1U(n)→πn+1O(2n + 1) is an isomorphism. Since πnO(n + 1) =
π2O(3) = 0, it follows from (A.5) that the homomorphism p : πn+1O(2n + 1)→
πn+1V2n+1,n, and hence that map i : πn+1U(n) = Z→ πn+1V2n+1,n = Z/2, is a
surjection. □
Lemma A.13. Suppose n is odd. Let δ : πn+1V2n+1,n→ πnO(n + 1) be the
boundary homomorphism of the exact sequence (A.5) and k :πnO(n + 1)→πnSn
the projection homomorphism of the ﬁbration O(n) → O(n + 1) → Sn. Then
k◦δ :πn+1V2n+1,n = Z→πn(Sn) = Z is multiplication by 2.
Proof. The elements of the group πnO(n + 1) classify ( n + 1)-dimensional
vector bundles overSn+1, and for eachx∈πnO(n+1) the elementk(x)∈πnSn = Z
is the Euler number of the bundle corresponding to x. On the other hand, as
noted in the proof of Lemma A.12, the imageδ(πn+1V2n+1,n) classiﬁes stably trivial
bundles and is generated by the tangent bundle TSn+1. This implies the claim
because χ(Sn+1) = 2 for n odd. □

APPENDIX B
Obstructions to Formal Legendrian Isotopies
In this appendix, whose content is partially taken from Murphy’s paper [ 143],
we study obstructions to formal Legendrian isotopies between genuine Legendrian
knots. We mainly restrict ourselves to spherical knots, the case which is most
relevant to the content of this book. Namely, we consider the following question.
Let (M,ξ ) be a (2 n + 1)-dimensional contact manifold, n≥ 1. Given a smooth
isotopy ft, t∈ [0, 1], connecting two Legendrian embeddings f0,f 1 :Sn ↪→ (M,ξ ),
what are the obstructions for lifting it to a formal Legendrian isotopy ( ft,F s
t )?
Recall that a formal Legendrian isotopy is a family Fs
t :TSn→TM , s,t∈ R,
of monomorphisms (i.e., injective bundle homomorphisms) covering ft such that
F 0
t = dft, Fs
0 = df0, Fs
1 = df1, and F 1
t are Legendrian monomorphisms TSn→
ξ⊂ TM . In view of Theorems 7.1 and 7.9, the problem of lifting ft to a formal
Legendrian isotopy is equivalent to the question whether the isotopyft is homotopic
to a regular Legendrian homotopyˆft through regular homotopies connectingf0 and
f1.
To a pair of Legendrian spheres f0,f 1 : Sn ↪→ (M2n+1,ξ ) connected by a
smooth isotopyft we will ﬁrst associate their relative rotation invariantr(f0,f 1;ft)
taking values in Z if n is odd and vanishing for n even. If r(f0,f 1;ft) = 0 we
will deﬁne a secondary invariant, the self-intersection invariant I(f0,f 1;ft) taking
values in Z if n is odd, in Z2 if n > 2 is even, and vanishing for n = 2. Both
invariants turn out to depend only on f0,f1 and the homotopy class of the isotopy
ft in the space of continuous homotopies connecting f0 andf1. The main result of
this appendix states that these give complete invariants for Legendrian spheres up
to formal Legendrian isotopy.
Theorem B.1. A smooth isotopy ft : Sn ↪→ M2n+1, n≥ 1, connecting two
Legendrian spheresf0,f 1 :Sn ↪→ (M,ξ ) can be lifted to a formal Legendrian isotopy
if and only if r(f0,f 1;ft) = 0 and I(f0,f 1;ft) = 0.
Note that for n = 2 both invariants vanish, so any smooth isotopy connecting
two Legendrian 2-spheres can be lifted to a formal Legendrian isotopy.
Forn odd one can deﬁne another invariant, the relative Thurston-Bennequin
invariant tb(f0,f 1;ft)∈ Z. We will show that for Legendrian spheres it is given
bytb(f0,f 1;ft) = 2I(f0,f 1;ft), so for n odd, r andtb are also complete invariants.
For homologically trivial Legendrian knots we havetb(f0,f 1) =tb(f0)−tb(f1), i.e.,
the relative Thurston-Bennequin invariant is the diﬀerence of the classical absolute
Thurston-Bennequin invariants. We will also discuss the eﬀect of the stabilization
construction in Section 7.4 on the invariants and Bennequin’s inequality.
A slightly diﬀerent question from the one discussed so far is the following:
When can two Legendrian embeddings f0,f 1 : Sn ↪→ (M,ξ ) be connected by a
formal Legendrian isotopy? Clearly a necessary condition is the existence of a
335

336 B. OBSTRUCTIONS TO FORMAL LEGENDRIAN ISOTOPIES
continuous (or equivalently, smooth) homotopy ft connecting f0 and f1. Next we
need to deform ft to a smooth isotopy. If n >2 and M is simply connected this
is always possible by Corollary 7.7, so in this case the question reduces to the one
answered by Theorem B.1. Note, however, that the answer may depend on the
homotopy class of the chosen homotopy ft.
Homotopy obstructions to formal Legendrian isotopies.
Let us endow the contact bundle ξ with a compatible complex structure J.
Then any Legendrian monomorphism F :TSn→ξ can be complexiﬁed to a com-
plex isomorphism F⊗ C :TSn⊗ C→ξ.
Fix a point p∈ Sn. Since π1V2n+1,n = 0 for all n≥ 1 (Lemma A.9), we can
assume without loss of generality that dpft :TpSn→ξ are Legendrian monomor-
phisms for all t∈ [0, 1]. Then dft can be covered by a family of complex bundle
isomorphisms Φt :TSn⊗ C→f∗
tξ such that Φ0 =df0⊗ C and Φt|TpSn =dpft⊗ C
for all t∈ [0, 1]. We use the Reeb vector ﬁeld R of a contact form deﬁning ξ to
extend the Φt to real isomorphisms Φt = Φt⊕R : (TSn⊗ C)⊕ R→ f∗
tTM . We
will view TSn as the real subbundle of TSn⊗ C and denote by b the inclusion
TSn ↪→TSn⊗ C↪→ (TSn⊗ C)⊕ R.
Thus any homotopy of monomorphisms Ft : TSn→ TM covering ft can be
equivalently viewed as a homotopy of monomorphisms ˆFt := Φ
−1
t ◦Ft : TSn→
(TSn⊗ C)⊕ R covering the identity. Let us denote by Mon the space of monomor-
phisms TSn→ (TSn⊗ C)⊕ R and by Mon based its subspace of based monomor-
phisms F satisfying F|TpSn = b|TpSn. Note that ˆdft = Φ
−1
t ◦dft is a path in
Monbased starting at b.
Lemma B.2. The inclusion homomorphism π1(Mon,b )→ π1(Monbased,b ) is
an isomorphism.
Proof. Restriction to the ﬁbers at p deﬁnes a Serre ﬁbration p : Mon →
Mon(TpSn, (TpSn⊗ C)⊕ R)∼=V2n+1,n with ﬁber Monbased. Consider its homotopy
sequence (we drop the basepoint b)
π2Mon
p∗
→π2V2n+1,n→π1Monbased→π1Mon→π1V2n+1,n = 0.
If n > 1 then π2V2n+1,n = 0 by Lemma A.9. If n = 1 the map p : Mon ≃
Map(S1,S 2)→ V3,1≃ S2 is the evaluation map γ↦→ γ(p) of a loop at p∈ S1
and thus induces (via constant loops) a surjection on π2. So for each n≥ 1 the
homomorphism p∗ :π2Mon→π2V2n+1,n is surjective and the lemma follows. □
Note that the bundleTSn⊗C is trivial because any stably trivialn-dimensional
complex bundle over Sn is trivial by Corollary A.10. Let us pick trivializations of
the bundles TSn⊗ C andTSn|Sn\p. This allows us to identify the homotopy class
with ﬁxed endpoints of the path ˆdft, t∈ [0, 1], in Mon based with an element in
πn+1(V2n+1,n,U (n)) which we denote by [ˆdft]. Here we view U(n)⊂V2n+1,n as the
subspace of unitary n-frames in Cn⊂ Cn⊕ R = R2n+1.
Lemma B.2 ensures that the class [ ˆdft]∈ πn+1(V2n+1,n,U (n)) is independent
of the way we make dpft Legendrian. It is also independent of all other choices in
the construction. Consider the exact sequence
(B.1) πn+1U(n)
i
→πn+1V2n+1,n
j
→πn+1(V2n+1,n,U (n))
∂
→πnU(n).

B. OBSTRUCTIONS TO FORMAL LEGENDRIAN ISOTOPIES 337
We call the image r(f0,f 1;ft) :=∂([ˆdft])∈πnU(n) the relative rotation invariant.
Note that r(f0,f 1;ft) can be deﬁned for any homotopy connecting f0 and f1 and
depends only on the homotopy class of this homotopy. Indeed, a homotopy between
f0 and f1 gives an isocontact bundle isomorphism f∗
0TM ∼= f∗
1TM , so we can
write F1 = g·F0 for a unique map g : Sn → U(n) whose homotopy class is
r(f0,f 1;ft). In particular, in a contact manifold M with trivial groups π1(M) and
πn(M) the relative rotation invariant r(f0,f 1;ft) is independent of ft and can be
denoted byr(f0,f 1). In this case we can also deﬁne the absolute rotation invariant
r(f)∈ πnU(n) of a Legendrian knot f as the relative rotation invariant r(f,f st),
where fst is a standard Legendrian unknot in a Darboux chart, so that we have
r(f0,f 1) =r(f0)−r(f1).
If r(f0,f 1;ft) = 0, then one can deﬁne a secondary invariant by lifting the
invariant [ˆdft]∈πn+1(V2n+1,n,U (n)) to an element
s(f0,f 1;ft)∈πn+1V2n+1,n/i(πn+1U(n)).
The preceding discussion shows: Vanishing of the rotation invariant r(f0,f 1;ft)
and the secondary invariant s(f0,f 1;ft) is a necessary and suﬃcient condition for
existence of a lifting of the isotopy ft to a formal Legendrian isotopy.
For evenn the relative rotation invariantr(f0,f 1;ft) vanishes because it takes
values in πnU(n) = 0, and hence the secondary invariant s(f0,f 1;ft) is always
deﬁned and takes values in πn+1V2n+1/i(πn+1U(n)) = Z2/i(Z). According to
Lemma A.12 the homomorphism i is surjective for n = 2 and zero for n⁄= 2. Thus
for even n⁄= 2 the invariant s is Z2-valued. For n = 2 the invariant s vanishes, so
any two Legendrian 2-spheres that are smoothly isotopic are formally Legendrian
isotopic.
For oddn we haveπnU(n)∼= Z andπn+1U(n) = 0, so both the relative rotation
invariantr(f0,f 1;ft)∈πnU(n)∼= Z and the secondary invariant
s(f0,f 1;ft)∈πn+1V2n+1,n/i(πn+1U(n)) =πn+1V2n+1,n∼= Z
are integer valued.
This discussion establishes Theorem B.1 with the invariants(f0,f 1;ft) in place
of I(f0,f 1;ft). In the following subsection we will deﬁne the geometric invariant
I(f0,f 1;ft) and show that it agrees with s(f0,f 1;ft) .
The self-intersection invariant.
Let f0,f 1 : Sn ↪→ (M,ξ ) be two Legendrian spheres connected by a smooth
isotopyft. Suppose that r(f0,f 1;ft) = 0.
Gromov’s h-principle for Legendrian immersions (Theorem 7.9) then implies
that the isotopy ft can be C0-approximated by a Legendrian regular homotopy
~ft which coincides with ft at the point p together with its diﬀerential (this stan-
dardization at p is not really necessary but will be convenient for the following
discussion). Let I{ ~ft} be its self-intersection index as deﬁned in Section 7.1. Recall
that it takes values in Z if n is odd, and in Z2 if n is even.
If ˆft is another such Legendrian regular homotopy connecting f0 and f1, then
together ~ft and ˆft give rise to an element ∆∈πn+1U(n) and the diﬀerence I{ ~ft}−
I{ ˆft} is determined by the image of ∆ under the map i :πn+1U(n)→πn+1V2n+1,n.
Recall that by Lemma A.12 the map i is surjective for n = 2 and vanishes for
n⁄= 2. Since one can always add a new self-intersection point in the interior of
a given regular homotopy (see [ 191]), this implies that for n = 2 the Legendrian

338 B. OBSTRUCTIONS TO FORMAL LEGENDRIAN ISOTOPIES
regular homotopy ~ft can be always chosen to have I{ ~ft} = 0. If n⁄= 2 it follows
that I{ ~ft} does not depend on the choice of the regular homotopy ~ft but only on
the homotopy class of the isotopy ft in the space of homotopies connecting the
two knots. Hence in this case we will write I(f0,f 1;ft) instead of I{ ~ft} and call
it the self-intersection invariant. The following proposition concludes the proof of
Theorem B.1.
Proposition B.3. Suppose that r(f0,f 1;ft) = 0. Then
s(f0,f 1;ft) =I(f0,f 1;ft)
under a suitable isomorphism from πn+1V2n+1,n to Z (forn odd) resp. Z2 (forn⁄= 2
even).
We ﬁrst prove this proposition for n odd in the following lemma. Let δ :
πn+1V2n+1,n→ πnO(n + 1) and k : πnO(n + 1)→ πnSn be the homomorphisms
introduced in Lemma A.13.
Lemma B.4. Suppose n is odd. Let ft : Sn → M2n+1 be a smooth isotopy
between two Legendrian spheresf0,f 1 :Sn→ (M,ξ ). Suppose that r(f0,f 1;ft) = 0.
Then for suitable isomorphisms πn+1V2n+1,n∼=πnSn∼= Z we have
k◦δ
(
s(f0,f 1;ft)
)
= 2s(f0,f 1;ft) = 2I(f0,f 1,ft).
Proof. Lemma A.13 implies the equality k◦δ
(
s(f0,f 1;ft)
)
= 2s(f0,f 1;ft).
For the second equality, note that the element k◦δ
(
s(f0,f 1;ft))∈ πnSn has the
following geometric interpretation. Pick a trivialization of the normal bundle to
L0 = f0(Sn) (which exists since L0 is a Legendrian sphere and hence its normal
bundle is isomorphic to the stabilized tangent bundle) and continuously extend
this trivialization to the normal bundles of the submanifolds Lt = ft(Sn). The
normalized Reeb vector ﬁelds along the Legendrian submanifolds L0 and L1 then
give us maps tj : Sn → Sn, j = 0, 1. The diﬀerence of the homotopy classes
[t0]− [t1]∈πn(Sn) is equal to k◦δ
(
s(f0,f 1;ft)).
Equivalently, this diﬀerence can be interpreted as follows. Let Rt be the Reeb
ﬂow for a contact form deﬁning ξ. Consider the singular chain C :Sn×I→M×I
deﬁned by the map C(x,t ) = (ft(x),t ), x∈ Sn, t∈ I = [0, 1]. For a suﬃciently
small ε >0 we denote by C
ε
the shifted chain C
ε
(x,t ) = (Rε◦ft(x),t ). We have
∂C =L0× 0−L1× 1 and ∂C
ε
=Lε
0× 0−Lε
1× 1. Then the intersection number
C·C
ε
is equal to [t0]− [t1].
Note that the intersection number C·C
ε
is a homological invariant: for any
two chainsA,A′ in M×I with ∂A =L0× 0−L1× 1 and ∂A′ =Lε
0× 0−Lε
1× 1
which belong to the same relative homology classes in Hn+1(M×I,L 0×0∪L1×1)
resp. Hn+1(M×I,Lε
0× 0∪Lε
1× 1) as C and C
ε
we haveA·A′ =C·C
ε
.
Now given a regular Legendrian homotopy ˆft connecting f0 and f1 we denote
by ˆC and ˆCε the corresponding singular chains ˆC : Sn×I → M×I and ˆCε :
Sn×I→M×I given by the formulas
ˆC(x,t ) = (ˆft(x),t ), ˆCε(x,t ) = (Rε◦ ˆft(x),t ), (x,t )∈Sn×I.
By the preceding discussion,
ˆC· ˆCε =C·C
ε
= [t0]− [t1].

B. OBSTRUCTIONS TO FORMAL LEGENDRIAN ISOTOPIES 339
On the other hand, since the Reeb vector ﬁeld is nowhere tangent to ˆft(Sn), the
only contributions to ˆC·ˆCε arise from self-intersections of ˆC, each self-intersection
point contributing two intersections with the same sign since n is odd. Thus
ˆC· ˆCε = 2I{ ˆft} = 2I(f0,f 1;ft),
and hence
2s(f0,f 1;ft) = [t0]− [t1] = 2I(f0,f 1,ft).
□
Proof of Proposition B.3. Forn odd this follows from Lemma B.4. For
evenn⁄= 2 one can argue as follows. Denote by H the space of regular homotopies
gt,t∈ [0, 1], connecting f0 andf1 and homotopic with ﬁxed endpoints to the path
ft, such that each gt coincides together with its diﬀerential with ft at the point
p. In view of the discussion above and the Smale–Hirsch Immersion Theorem 7.1,
concatenating gt with the inverse of the isotopy ft yields a bijection S : π0H→
πn+1V2n+1,n ∼= Z2. Associating to each gt its self-intersection index I{gt} also
deﬁnes a map I :π0H→ Z2, which is surjective because one can always add a new
self-intersection point in the interior of a given regular homotopy (see [191]). Since
S(gt) = 0 implies that the path gt is connected to the isotopy ft through regular
homotopies and thus I{gt} = 0, we see that I = S : π0H→ Z2. But by deﬁnition
s(f0,f 1;ft) = S(~ft) and I(f0,f 1;ft) = I{ ~ft} for any Legendrian regular homotopy
~ft inH, so we conclude s(f0,f 1;ft) =I(f0,f 1;ft). □
The relative Thurston-Bennequin invariant.
Suppose n is odd. As above, we denote by Rt the Reeb ﬂow. Let L0,L 1,
i = 0, 1, be two disjoint (not necessarily spherical and even not necessarily diﬀeo-
morphic) oriented Legendrian submanifolds which belong to the same homology
class in HnM. Pick a singular chain C with∂C =L0−L1. For a suﬃciently small
ε > 0 we denote by Cε and Lε
i the shifted chain Rε(C) and shifted Lagrangian
submanifolds Rε(Li), i = 0, 1.
The relative Thurston-Bennequin invariant is deﬁned as the intersection num-
ber
tb(L0,L 1;C) :=C· (Lε
0 +Lε
1).
If ~C is another chain with ∂~C =L0−L1, then we have
tb(L0,L 1;C)− tb(L0,L 1;~C) = (C− ~C)· (Lε
0 +Lε
1),
where C− ~C is an (n + 1)-cycle in M. Hence, if either Hn+1M = 0 or the ma-
nifolds L0 and L1 are homologically trivial the relative invariant tb( L0,L 1;C) is
independent of the choice of the class C, so in this case we can drop C from the
notation.
In particular, for a homologically trivial oriented Legendrian submanifold L =
∂C one can deﬁne an absolute Thurston-Bennequin invariant tb(L) :=C·L and this
deﬁnition is independent of the choice of the spanning chain C. For two homologi-
cally trivial oriented submanifoldsL0 andL1 we have tb(L0,L 1) = tb(L0)−tb(L1).
Indeed, if Li =∂Ci for i = 0, 1 then ∂(C0−C1) =L0−L1 and hence
tb(L0,L 1) = (C0−C1)· (Lε
0 +Lε
1) =C0·Lε
0−C1·Lε
1 +C0·Lε
1−C1·Lε
0
= tb(L0)− tb(L1) + lk(L0,Lε
1)− lk(L1,Lε
0) = tb(L0)− tb(L1).

340 B. OBSTRUCTIONS TO FORMAL LEGENDRIAN ISOTOPIES
Here we have used that the linking pairing is symmetric for n odd and thus
lk(L0,Lε
1)− lk(L1,Lε
0) = lk(L0,L 1)− lk(L1,L 0) = 0. Let us also point out that
tb(L) remains unchanged when one reverses the orientation of L.
If f0,f 1 : Λn ↪→M2n+1 are two disjoint parametrized Legendrian embeddings
connected by a homotopy ft we deﬁne
tb(f0,f 1;ft) := tb(L0,L 1;C),
whereLi :=fi(Λ), i = 0, 1, and C : Λ×I→M is the singular chain in M realized
by the homotopy ft, i.e., C(x,t ) =ft(x) for (x,t )∈ Λ×I.
Proposition B.5. Let ft : Sn ↪→ M2n+1 be a smooth isotopy between two
disjoint Legendrian embeddings f0,f 1 : Sn ↪→ M. Suppose that n is odd and
r(f0,f 1;ft) = 0. Then
tb(f0,f 1;ft) = 2I(f0,f 1;ft).
Proof. We continue using the notation introduced in the proof of Lemma B.4.
We showed there that
2I(f0,f 1;ft) =C·C
ε
,
where the singular chain C : Sn×I → M×I is deﬁned by the map C(x,t ) =
(ft(x),t ) and C
ε
is the shifted chain C
ε
(x,t ) = ( Rε◦ft(x),t ). We have ∂C =
L0× 0−L1× 1 and ∂C
ε
=Lε
0× 0−Lε
1× 1.
Let us deform the isotopies ft andRε◦ft to the isotopies ~ft and ~f′
t deﬁned by
the formulas
~ft :=
{
f2t, t ∈ [0, 1
2],
f1, t ∈ ( 1
2, 1],
~f′
t :=
{
Rε◦f0, t ∈ [0, 1
2],
Rεf2t−1, t ∈ ( 1
2, 1].
Let ~C and ~C′ denote the corresponding singular chains in M×I:
~C(x,t ) = (~ft(x),t ), ~C′(x,t )(~ft(x),t ).
Since the intersection number depends only on the relative homology classes, we
have
(B.2) C·C
ε
= ~C· ~C′.
The latter intersection number can also be computed in a diﬀerent way. Namely,
consider the singular chains ~C1 := ~C|Sn×[0, 1
2 ] and ~C′
1 := ~C′|Sn×[0, 1
2 ] in M× [0, 1
2],
and the chains ~C2 := ~C|Sn×[ 1
2,1] and ~C′
2 := ~C′|Sn×[ 1
2,1] in M× [ 1
2, 1]. Then
(B.3) ~C· ~C′ = ~C1· ~C′
1 + ~C2· ~C′
2,
where the intersections are computed, respectively, in the manifolds M× [0, 1],
M× [0, 1
2] and M× [ 1
2, 1]. Consider the projections C := pr(~C1) and C′ = pr(~C′
2)
of the chains ~C1 and ~C′
2, respectively, to the factor M. Then ∂C = L0−L1 and
∂C′ =Lε
0−Lε
1, hence
(B.4) ~C1· ~C′
1 =C·Lε
0 and ~C2· ~C′
2 =L1·C′ =R−ε(L1)·C.
But for n odd the vector ﬁelds R|L1 and−R|L1 are homotopic as sections of the
normal bundle to L1 in M, and therefore
(B.5) R−ε(L1)·C =Rε(L1)·C =Lε
1·C.

B. OBSTRUCTIONS TO FORMAL LEGENDRIAN ISOTOPIES 341
Combining equations (B.2), (B.3), (B.4) and (B.5) we obtain
2I(f0,f 1;ft) =C·C
ε
=C·Lε
0 +Lε
1·C =C· (Lε
0 +Lε
1) = tb(L0,L 1;C).
□
The invariant tb for homologically trivial knots in 3-manifolds was indepen-
dently deﬁned by Thurston (unpublished) and Bennequin [ 16]. It was generalized
to higher dimensions by Tabachnikov [182].
The Thurston-Bennequin invariant is most interesting for 3-dimensional con-
tact manifolds. For instance, Legendrian knots in the standard contact R3 satisfy
Bennequin’s inequality ([16])
tb(L) +|r(L)|≤ χ(Σ),
where Σ is a Seifert surface for L and r(L)∈ Z is the rotation invariant. In [ 44]
this inequality was extended from the standard contact R3 to all tight contact 3-
manifolds. Kronheimer–Mrowka [117] and Rudolph [164] proved a stronger version
of Bennequin’s inequality, replacing the 3-dimensional genus of the knot by its 4-
dimensional genus. Many other bounds on tb(Λ) have been found, see [ 55, 150]
for surveys of this subject.
Finally, let us discuss the eﬀect of the stabilization construction in Section 7.4
on the relative invariants. Recall that this construction (see Proposition 7.12 and
Lemma 7.14) associates to a Legendrian knot f0 : Λ ↪→ (M2n+1,ξ ) a Legendrian
regular homotopy ft : Λ→M such that f1 is a Legendrian embedding and I{ft} =
(−1)n(n−1)/2χ(N). Here N⊂ Rn is a compact domain with smooth boundary over
which the stabilization is performed. Note that, since the construction is supported
in a Darboux chart, it is irrelevant whether Λ is a sphere or not. Since the two knots
are connected by a Legendrian regular homotopy, the relative rotation invariant
r(f0,f 1;ft) is always zero.
Forn = 1 the Euler characteristicχ(N) and thus the self-intersection invariant
I(f0,f 1;ft) can only be positive, so tb(f0,f 1;ft) = 2I(f0,f 1;ft) can be any positive
even integer, in accordance with Bennequin’s inequality (recall that tb( L0,L 1) =
tb(L0)− tb(L1) for homologically trivial knots).
Forn = 2 the self-intersection invariant vanishes, so the two knots f0 and f1
are formally Legendrian isotopic. For even n > 2 they are formally Legendrian
isotopic if and only if χ(N) is even.
For odd n > 1 the two knots are formally Legendrian isotopic if and only if
χ(N) = 0 (note that the “if” was also shown in Proposition 7.23). By varying
χ(N) we can arrange the relative Thurston-Bennequin invariant to take any even
integer value, which shows that there is no analogue of Bennequin’s inequality for
Legendrian knots of odd dimensions n> 1.



APPENDIX C
Biographical Notes on the Main Characters
In this appendix we sketch biographies of the mathematicians whose work is
most relevant to the content of this book. We have grouped them according to
their ﬁelds, complex analysis resp. diﬀerental and symplectic topology, and put
them in chronological order within each ﬁeld. The following sources were used
in preparation: the internet site Wikipedia; several articles by J. O’Connor and
E. Robertson under http://www-history.mcs.st-andrews.ac.uk/Biographies; the ar-
ticle by L. Dell’Aglio on E. Levi under http://www.treccani.it/enciclopedia/eugenio-
elia-levi (Dizionario-Biograﬁco)/ (translated from Italian by A. Gnoatto); the arti-
cles [106] and [105] by A. Huckleberry on K. Stein and H. Grauert; the article [22]
by R. Bott on M. Morse; the article by J. Zund under http://www.anb.org/articles/
13/13-02523.html and the interview [193] with H. Whitney; the book [14] by S. Bat-
terson on S. Smale; and the preface to the book [ 127] by J. Marsden and T. Ratiu
on A. Weinstein.
C.1. Complex analysis
Friedrich Hartogs (May 20, 1874 – August 18, 1943). Friedrich Hartogs
was born in Brussels, Belgium, into the family of a German businessman. Hartogs’
family were German Jews and he was brought up in Frankfurt am Main, Germany.
He attended the Realgymnasium W¨ ohlerschule in Frankfurt, graduating from high
school in the spring of 1892.
At that time the standard university career for German students involved mov-
ing between diﬀerent institutions and Hartogs followed this route. First he spent
a semester at the Technical College at Hannover, followed by a semester at the
Technical College in Berlin. He then matriculated at the University of Berlin where
he was taught mathematics by, among others, Georg Frobenius, Lazarus Fuchs,
and Hermann Schwarz, and he attended physics lectures by Max Planck. Fol-
lowing his studies at the University of Berlin, he went to the University of Munich
where he attended courses by Ferdinand von Lindemann and Alfred Pringsheim. In
1901 Pringsheim became a full professor at Munich and he became Hartogs’ thesis
advisor. In 1903 Hartogs was awarded his doctorate from Ludwig-Maximilians-
Universit¨ at in Munich, and two years later he received his habilitation.
After that Hartogs became a privatdozent at the University of Munich. In 1909-
10 he taught Abraham Fraenkel who, years later, wrote in his memoirs that Hartogs
was by nature a consistently shy and rather anxious person. Perhaps for this reason
he was promoted only slowly when the outstanding quality of his research would
suggest that he might have risen more rapidly through his profession. He became an
extraordinary professor in 1912, then ten years later was oﬀered a full professorship
at the University of Frankfurt. Hartogs was indeed a very cautious person and
he turned down the oﬀer of this chair because, in the diﬃcult ﬁnancial climate
343

344 C. BIOGRAPHICAL NOTES ON THE MAIN CHARACTERS
of the time with hyperinﬂation gripping Germany, he did not feel conﬁdent that
a privately owned institution, which the University of Frankfurt was, oﬀered the
security that he required to support his wife and four children.
In Munich, Hartogs had several outstanding colleagues such as Oskar Perron,
Constantin Carath´ eodory, and Heinrich Tietze. These three professors all made
representations to the university arguing that Hartogs should be appointed to a
full professorship, and in 1927, ﬁve years after turning down the full professorship
at Frankfurt, he had at last reached the top of his profession in Munich. Like all
Jewish academics, after the Nazi Party came to power in 1933 Hartogs’ life became
increasingly diﬃcult. In October 1935 he was forced to retire from his professorship,
and on 10 November 1938, during the infamous “Kristallnacht”, Hartogs was one
of those arrested and taken to the Dachau concentration camp. After being held
for several weeks during which he was appallingly treated he was, nevertheless,
released.
Hartogs’ wife was not Jewish and in 1941 Hartogs and his wife were given
advice by a lawyer that in order to protect Hartogs’ wife she should divorce him.
This was a painful process for Hartogs and the process was deliberately drawn out
to be as lengthy as possible. In early 1943 the divorce was ﬁnalized but Hartogs
continued to live in his wife’s house and the authorities turned a blind eye. The
indignity and humiliation that Hartogs had suﬀered for ten years ﬁnally became
too much for him and in August 1943 he took his own life.
Hartogs is best known for his discovery of the Hartogs phenomenon, contained
in his habilitation thesis, that compact singularities of holomorphic functions in
n >1 complex variables are always removable (see Section 5.4). This result is in
striking contrast to the case of one variable, and marks the beginning of the theory
of functions of several complex variables.
Eugenio Elia Levi (October 18, 1883 – October 28, 1917). Eugenio
Elia Levi was born in Torino, Italy. His older brother Beppo Levi was also a well
known mathematician. Eugenio Levi graduated in mathematics from the Scuola
Normale di Pisa in 1905. From 1906 to 1909 he was assistant of Ulisse Dini in Pisa,
then he moved to the University of Genova where he became full professor in 1912.
Eugenio Levi was killed in World War I on October 28, 1917, in Cormons, Italy, on
the border with today’s Slovenia.
In his short life Eugenio Levi wrote 33 papers making fundamental contribu-
tions to group theory, the theory of partial diﬀerential operators, and the theory
of functions of several complex variables. In his work in group theory he discov-
ered what is now called the Levi decomposition, which was conjectured by Wilhelm
Killing and proved by ´Elie Cartan in a special case. In the theory of partial dif-
ferential operators he discovered the method of the parametrix, which is a way
to construct fundamental solutions for elliptic partial diﬀerential operators with
variable coeﬃcients. The parametrix method is widely used in the theory of pseu-
dodiﬀerential operators.
In the theory of functions of several complex variables Eugenio Levi introduced
the Levi form and the concept of (Levi) pseudoconvexity (calledJ-convexity in this
book), which turned out to be one of the key concepts in the theory of functions
of several complex variables. The question whether a bounded domain in Cn with
smooth pseudoconvex boundary is a domain of holomorphy became known as the
Levi problem and was one of the main driving forces for the development of complex

C.1. COMPLEX ANALYSIS 345
analysis in the ﬁrst half of the twentieth century. It was only solved in the 1950s
by Oka, Bremermann and Norguet.
Kiyoshi Oka (April 19, 1901 – March 1, 1978). Kiyoshi Oka entered
the Imperial University of Kyoto in 1922 to study physics. However, in 1923 he
changed subjects to study mathematics, graduating with a degree in mathematics
in 1925. In the same year he was appointed as a lecturer in the Faculty of Science
at the Imperial University of Kyoto, and in 1929 he was promoted to assistant
professor. 1929 was a very signiﬁcant year for Oka for in that year he took a
sabbatical leave and went to the University of Paris, where he met Gaston Julia
and became interested in unsolved problems in the theory of functions of several
complex variables.
Oka remained on the staﬀ at the Imperial University of Kyoto while he was on
leave in Paris, but on his return to Japan in 1932 he accepted a position as assistant
professor in the Faculty of Science of Hiroshima University. In 1938 Oka went to
Kimitoge in Wakayama to study by himself, and in 1940 he presented his doctoral
thesis to the University of Kyoto. After obtaining his doctorate and a short period
1941-42 as research assistant at Hokkaido University, Oka spent the next seven years
again at Kimitoge, supported by a scholarship of the Huju-kai Foundation. In 1949,
Oka was appointed professor at the Nara University for Women, a post he held until
1964. From 1969 until his death in 1978 he was a professor of mathematics at the
Industrial University of Kyoto.
Oka’s most famous work was published over the 25 year period 1936-1961 during
which he solved a number of important problems in the theory of functions of several
complex variables such as the Cousin problems and the Levi problem. He proved
important foundational results such as Oka’s coherence theorem (Section 5.6) and
the Oka–Weil theorem (Theorem 5.4). Oka’s principle on holomorphic approxima-
tion of continuous sections, introduced by Oka in his work on the Cousin problems
and later generalized by Grauert, provided an early example of an h-principle and
marked one of the points of departure for Gromov’s later work on this subject. In
the introduction to Oka’s collected works [ 155], Henri Cartan describes the way
that Oka came into the subject:
“The publication in 1934 of a monograph by Behnke-Thullen marked a crucial
stage in the development of the theory of analytic functions of several complex
variables. By giving a list of the open problems in the area, this work played an
important role in deciding the direction of Oka’s research. He set himself the almost
super-human task of solving these diﬃcult problems. One could say that he was
successful, overcoming one after the other the obstacles he encountered on the way.”
Henri Cartan (July 8, 1904 – August 13, 2008). Henri Cartan was born
in Nancy, France, and grew up in Paris. His father, ´Elie Cartan, was a mathemati-
cian well known for his work on Lie groups. Henri had a sister and two younger
brothers, Jean and Louis, who both died tragically. Jean, a composer, died of tu-
berculosis at the age of 25 while Louis, a physicist, was a member of the Resistance
arrested by the Germans in 1942, deported to Germany in February 1943, and
executed after 15 months in captivity.
Cartan studied at the ´Ecole Normale Sup´ erieure in Paris, where he met and
became friend with Andr´ e Weil who was one year ahead. It was on Andr´ e Weil’s
suggestion that Cartan later began working on analytic functions of several complex

346 C. BIOGRAPHICAL NOTES ON THE MAIN CHARACTERS
variables. Among Cartan’s teachers at the ´Ecole Normale were Gaston Julia and
his father ´Elie Cartan. He received his doctorate in 1928 under the supervision
of Paul Montel. After positions at the Lyc´ ee Caen and the University of Lille,
he took up a post at the University of Strasbourg in 1931. When World War II
broke out in September 1939, the inhabitants of Strasbourg had to be evacuated
and the university was displaced to Clermont-Ferrand. In November 1940 Cartan
was appointed professor at the Sorbonne in Paris. He taught in Paris from that
time until 1969 (with the exception of two years 1945-46 when he returned to the
University of Strasbourg), and then at the Universit´ e de Paris-Sud in Orsay from
1970 to until his retirement in 1975.
At the ´Ecole Normale Sup´ erieure, Cartan started the S´ eminaire Cartan. Jean-
Pierre Serre, who was one of Cartan’s doctoral students, suggested that the seminars
should be written up for publication and ﬁfteen ENS-Seminars written by Cartan
were published between 1948 and 1964. These publications played a major role in
shaping the modern theory of functions of several complex variables.
Cartan’s most important contribution to mathematics is without doubt the
introduction of sheaf-theoretical methods into complex analysis and his Theorems
A and B for coherent analytic sheaves on Stein manifolds (see Section 5.6). These
new techniques allowed him to treat many of the classical problems on several
complex variables in a uniﬁed manner, thus moving the whole ﬁeld into a new
era. After Cartan had presented his Theorems A and B at the Colloque sur les
fonctions de plusieurs variables in Brussels in 1953, the German participant Karl
Stein commented: “Wir haben Pfeil und Bogen, die Franzosen haben Panzer.” 1
Cartan also made signiﬁcant contributions to other areas of mathematics such
as algebra and topology. His 1956 book Homological Algebra with Eilenberg is a
classic text which has had a profound inﬂuence on the subject over half a century.
An important part of Cartan’s mathematical life was taken up with Bourbaki.
He was one of the founding members of this group in 1935 together with Andr´ e
Weil, Jean Dieudonn´ e, Szolem Mandelbrojt, Claude Chevalley, Ren´ e de Possel, and
Jean Delsarte.
Cartan was also involved with politics and in particular supporting human
rights. In 1974 the Russian authorities placed the mathematician Leonid Plyushch
in a special psychiatric hospital. Andrei Sakharov pointed out that this was a politi-
cal act and Cartan began a strenuous campaign for Plyushch’s release. The Interna-
tional Congress of Mathematicians was held in Vancouver in 1974 and this presented
an opportunity to gain wide international support for Plyushch with a thousand sig-
natures to a petition for his release. After the Congress Cartan played a major role
in setting up the Comit´ e des Math´ ematiciens to support Plyushch and other dis-
sident mathematicians. In January 1976 the Soviet authorities released Plyushch,
which was a major success for Cartan and the Comit´ e des Math´ ematiciens. But
the Comit´ e did not stop after this success. It has supported other mathematicians
who have suﬀered for their political views, such as the Uruguayan mathematician
Jos´ e Luis Massera. For his outstanding work in assisting dissidents Cartan received
the Pagels Award from the New York Academy of Sciences.
Karl Stein (January 1, 1913 – October 19, 2000). Karl Stein was born
in Hamm in Westfalen, Germany. He studied in M¨ unster, where he received his
1We have bows and arrows, the French have tanks.

C.1. COMPLEX ANALYSIS 347
doctorate under the supervision of H. Behnke in 1937. By that time, he had al-
ready been exposed to the fascinating developments in the area of complex analysis.
The brilliant young Peter Thullen was proving fundamental theorems, Henri Car-
tan had visited M¨ unster, and Behnke and Thullen had just written their classical
book on the subject. The amazing phenomenon of analytic continuation in higher
dimensions had already been exempliﬁed more than 20 years before in the works of
Hartogs and Levi, while the recent work of Thullen, Cartan and Behnke had gone
much further. It must have been clear to Stein that this was the way to go.
Even though the Third Reich was already invading academia, Behnke kept
things going for as long as possible, but this phase of the M¨ unster school of complex
analysis could not go on forever. Although Stein was taken into the army, during a
brief stay at home he was able to prepare and submit the paper which contained the
results from his Habilitationsarbeit which was accepted in 1940. At a certain point
he was sent to the eastern front. Luckily, however, the authorities were informed of
his mathematical abilities, and he was called back to Berlin to work until the end
of the war in some form of cryptology.
Almost immediately after the war, in a setting of total destruction, Behnke
began to rebuild his group, and very soon Stein became the mathematics guru in
M¨ unster. At the time there were only two professor positions in pure mathematics,
those of Behnke and F. K. Schmidt. Although it must have been very diﬃcult,
Behnke somehow found a position for Stein which he held from 1946 to 1955.
In 1955 Stein took a chair of mathematics at the Ludwigs-Maximilians-Univer-
sit¨ at in Munich, a position he held until his retirement in 1981. There he continued
his mathematics and built his own group in complex analysis, one of his best known
students being Otto Forster.
Stein made important contributions to many areas of several complex variables.
Until the early 1950s his main eﬀorts were directed towards the Cousin problems.
In his 1951 paper [ 178] on this subject he pointed out that most of the results he
considered were true under assumptions which now form the deﬁnition of a Stein
manifold, see Section 5.3 above. The term “variet´ e de Stein” for these new spaces
was introduced by H. Cartan at the Colloque sur les fonctions de plusieurs vari-
ables in Brussels in 1953. Stein manifolds and their generalizations, Stein spaces,
continue to play a central role in complex analysis to this day.
Hans Grauert (February 8, 1930 – September 4, 2011). Hans Grauert
was born in Haren-Ems in Niedersachsen (Lower Saxony) in the north of Germany
close to the border with the Netherlands. He attended primary and middle school
there from 1936 until the end of the war in 1945. He later recalled how he struggled
with mathematics as a school boy until a teacher told him it was acceptable to think
abstractly, he didn’t necessarily need to deal with numbers.
In 1949 he graduated from the Gymnasium in Meppen, Germany, just 12 km
from his home-town. He then studied at the University of M¨ unster, where he was
awarded his doctorate in 1954 after spending a year in 1953 at the ETH Z¨ urich,
where he was inﬂuenced by Beno Eckmann. His ﬁrst paper “M´ etrique Kaehl´ erienne
et domaines d’holomorphie” was published in French in 1954.
In September 1955 Grauert was appointed as an assistant at the University of
M¨ unster, submitting his habititation thesis there in February 1957. His output of
published papers was quite remarkable, with 10 major papers published in 1956 and
1957. He spent the year 1957–58 at the Institute for Advanced Study in Princeton,

348 C. BIOGRAPHICAL NOTES ON THE MAIN CHARACTERS
then the spring semester of 1959 at the Institut des Hautes ´Etudes Scientiﬁque in
Bures-sur-Yvette.
In 1959 Grauert was appointed as an ordinary professor at the University of
G¨ ottingen to ﬁll the chair which Carl Ludwig Siegel had occupied. He supervised
there doctoral studies of 44 students, several of whom collaborated with him on
major projects.
Grauert has been the leading mathematician in the theory of several complex
variables in his generation. He not only solved several major problems but his
work, along with the work of Henri Cartan, very much shaped the development of
this ﬁeld in the second half of 20th century. For example, the following results of
Grauert play an important role in this book: Grauert’s solution of the Levi problem
for complex manifolds and his characterization of Stein manifolds in terms of J-
convex functions (Sections 5.2 and 5.3), Grauert’s Oka principle (Section 5.5), and
his proof that complexiﬁcations of real analytic manifolds ( Grauert tubes) are Stein
(Section 5.7).
Grauert also wrote a large number of excellent textbooks, for example the
classical books Theory of Stein Spaces (1979) and Coherent Analytic Sheaves (1984)
with R. Remmert.
C.2. Diﬀerential and symplectic topology
Marston Morse (March 24, 1892 – June 22, 1977). Marston Morse
was born in Waterville, Maine, USA. His mother was Ella Phoebe Marston and
his father was Howard Calvin Morse, a farmer and real estate agent. The name
“Marston” by which he wanted to be known was therefore his mother’s maiden
name and not a forename.
Morse received his B.A. from Colby College in Waterville in 1914, and his
Ph.D from Harvard in 1917 for his thesis entitled “Certain Types of Geodesic Mo-
tion on a Surface of Negative Curvature” under the direction of G. D. Birkhoﬀ.
Morse taught brieﬂy at Harvard before entering military service. For the duration
of World War I he served as a private in the U.S. Army in France and for his out-
standing work in the Ambulance Corps he was awarded the Croix de Guerre with
Silver Star. After the war he resumed his academic career. After positions at Har-
vard (1919-20), Cornell (1920-25), Brown University (1925-26), and again Harvard
(1926-35), he moved to the Institute for Advanced Study in Princeton where he
remained until his retirement in 1962.
Morse was married twice and had 4 daughters and 3 sons.
In 1925 Morse published a paper entitled “Relations between the critical points
of a real function of n independent variables” that would shape his mathematical
life, and that of generations of mathematicians to this day. In this paper he proves
the famous Morse inequalities for Morse functions on a ﬁnite dimensional manifold,
thus initiating what is now called Morse theory (see Chapter 9).
Realizing the power of this theory, Morse devoted a large part of his mathe-
matical life to its extensions and applications. Almost from the beginning he also
considered Morse theory on inﬁnite dimensional spaces such as the loop space of a
manifold. His groundbreaking work in this direction culminated in his famous book
“The calculus of variations in the large” from 1932, where he proved for example
the existence of inﬁnitely many geodesics joining any two distinct points for an
arbitrary Riemannian metric on a sphere.

C.2. DIFFERENTIAL AND SYMPLECTIC TOPOLOGY 349
Morse also developed topological versions of his theory for very general func-
tions, and found applications to other problems such as the existence of minimal
surfaces. Morse theory was not Morse’s only contribution to mathematics – in all
he wrote about 180 papers and eight books on a whole range of topics – but clearly
the most inﬂuential one. It was the basis for many spectacular subsequent develop-
ments, from Smale’s h-cobordism theorem and Bott’s periodicity theorem to Floer
homology in gauge theory and symplectic topology. Today, Morse theory is an
indispensible tool in geometry and topology. Morse functions, and their J-convex
analogues, are also the basic objects studied in this book.
Hassler Whitney (March 23, 1907 – May 10, 1989). Hassler Whitney
was born in New York City, the son of Edward B. Whitney, a judge, and Josepha
Newcomb. His grandfathers were the philologist William D. Whitney and the as-
tronomer Simon Newcomb. Whitney received his ﬁrst degree from Yale Univer-
sity in 1928, and his Ph.D. in mathematics from Harvard University in 1932 with
the dissertation “The Coloring of Graphs” written under supervision of George
D. Birkhoﬀ. After spending the years 1931–1933 as a National Research Council
Fellow at Harvard and Princeton he returned to Harvard where he was successively
promoted until he became full professor in 1946. From 1943 to 1945 he was a
member of the Mathematics Panel of the National Defense Research Committee.
In 1952 he joined the Institute for Advanced Study at Princeton, where he was
professor of mathematics until his retirement in 1977.
Whitney was a keen mountaineer all his life. As an undergraduate in 1929,
Whitney and his cousin Bradley Gilman made the ﬁrst ascent of a 700 feet ridge in
New Hampshire which is now known as the Whitney-Gilman ridge. Later climbing
partners included the topologists James W. Alexander and Georges de Rham.
Whitney got married three times, the last time in 1986 at the age of 78, and
had ﬁve children.
Whitney’s work covers a wide range of subjects including graph theory, singu-
larity theory, diﬀerential and algebraic topology, and geometric integration theory.
In his work on graph theory in the early 1930s he made important contributions
to the four colour problem. In 1936 Whitney introduced the modern deﬁnition of
a manifold of class Cr. In 1944 studied the self-intersection index of immersions
of half dimension and proved the famous Whitney embedding theorem that any
smooth manifold of dimension n > 2 can be embedded in R2n (see Section 7.1).
The Whitney trick used in this proof was the basis for much later work in diﬀeren-
tial topology such as Smale’s proof of the h-cobordism theorem. It also underlies
all the ﬂexibility results for Stein structures proved in this book.
In the late 1930s Whitney was one of the major developers of algebraic topology,
in particular the theory of bundles and characteristic classes. The signiﬁcance of
his work is reﬂected in a large number of fundamental concepts that now carry
his name such as Whitney sum, Whitney product theorem, and Stiefel-Whitney
classes.
In the 1950s Whitney studied the topology of singular spaces and singularities of
maps. He introduced the notion of a Whitney stratiﬁcation which became the basis
for the modern theory of stratiﬁed spaces. His classiﬁcation results for singularities
of smooth maps (e.g. the Whitney umbrella) led to the new ﬁelds of singularity
theory and catastrophe theory. Whitney also did foundational work on analytic

350 C. BIOGRAPHICAL NOTES ON THE MAIN CHARACTERS
spaces, as a byproduct of which he proved together with Bruhat that every real
analytic manifold has a complexiﬁcation (Theorem 5.41).
In the last two decades of his life Whitney became involved in mathematical
education at elementary schools, vigorously opposing calls for more mathematics
to be taught earlier in school.
Stephen Smale (born in 1930). Stephen Smale was born in Flint, Michigan,
the site of General Motors. From the age of ﬁve he lived on a farm while his father
worked in the city for General Motors. Stephen attended an elementary school
with only a single classroom about a mile from his farmhouse. At high school his
favourite subject was chemistry. His interests had moved to physics by the time he
entered the University of Michigan, Ann Arbor, in 1948, but after failing a physics
course he turned to mathematics. He was awarded a BS in 1952 and an MS the
following year. In 1957 Smale received his Ph.D. from the University of Michigan
under the supervision of Raoul Bott. In his thesis he generalized a result proved
by Whitney and Graustein in 1937 for curves in the plane to curves in arbitrary
manifolds.
After postdoctoral years spent at the University of Chicago (1956-58), the Insti-
tute for Advanced Study in Princeton (1958-59), and the Instituto de Mathem´ atica
Pura e Aplicada (IMPA) in Rio de Janeiro, Smale was appointed an associate pro-
fessor of mathematics at the University of California at Berkeley in 1960. After 3
years at Columbia University, New York, Smale returned in 1964 to a professorship
at Berkeley where he remained until his retirement in 1995. After his retirement he
took up a professor position at the City University of Hong Kong, a post he held
until 2001 and again since 2009. Since 2002 he is also a professor at the Toyota
Technological Institute in Chicago.
Smale’s mathematical work is impressive both for its depth and its breadth.
He made profound contributions to a whole range of subjects including diﬀerential
topology, dynamical systems, mathematical economics, and theoretical computer
science.
In the years after his Ph.D. Smale astounded the mathematical world with a
number of breathtaking results in diﬀerential topology. In 1957 he found a general
classiﬁcation of immersions of spheres in Euclidean spaces (see Section 7.1), which
implied as a special case that the standard 2-sphere in R3 can be turned inside out
by immersions. His thesis advisor R. Bott ﬁrst didn’t believe this result because he
could not picture such a sphere eversion, but Smale’s proof withstood all scrutiny
and was ﬁnally published in 1959. Only years later did mathematicians succeed in
explicitly describing and visualizing a sphere eversion.
In 1961 Smale proved the generalized Poincar´ e conjecturein dimension > 4,
followed in 1962 by the h-cobordism theorem. His proof, sketched in Section 9.8
above, is a beautiful application of Morse theory: Beginning with an arbitrary
Morse function, Smale successively removes critical points as far as the topology
allows, crucially applying Whitney’s trick in the process. The most startling aspect
of these results was that diﬀerential topology suddenly looked simpler in higher
dimensions than in dimensions 3 and 4. Indeed, in the decade following Smale’s
work many questions were settled for manifolds of higher dimensions (in a new ﬁeld
called surgery theory), while the corresponding questions in low dimensions either
had negative answers (such as the existence of exotic smooth structures on R4),
were only solved much later (such as the 3-dimensional Poincar´ e conjecture), or

C.2. DIFFERENTIAL AND SYMPLECTIC TOPOLOGY 351
still remain open (such as the 4-dimensional Poincar´ e conjecture). For his work
on the generalized Poincar´ e conjecture Smale was awarded a Fields Medal at the
International Congress of Mathematicians in Moscow in 1966.
In the 1960s Smale’s main focus was the theory of dynamical systems where
he introduced a number of new concepts such as his famous horseshoe and Morse-
Smale systems, and proved foundational results such as his Ω-stability theorem. In
the 1970s Smale applied his ideas on dynamical systems to questions in economics,
and since the 1980s he has been mainly interested in theoretical computer science.
In the summer of 1965 Smale played an important role in the early protests
against the Vietnam War in Berkeley. He was one of the main organizers of anti-
war activities such as the Vietnam Day 1965, attempts to block trains transporting
Vietman troops, and a march to the Oakland Army Terminal. In early August
1966, the House Committee on Un-American Activities in Washington opened an
investigation of radical anti-war protests by Smale and others. At that time Smale
was in Europe on his way to Moscow for the Fields Medal Ceremony, which led to
the following headline in the San Francisco Examiner on August 5, 1966: “UC Prof
Dodges Subpoena, Skips U.S. for Moscow.”
Mikhail Gromov (born in 1943). Mikhail Leonidovich (Misha) Gromov
was born in Boksitogorsk, a town about 200 km east of St Petersburg (or Leningrad
as it was then called). Misha did not speak until the war was over, but then began
speaking with whole sentences. At the age of 6 he annoyed his ﬁrst grade teacher
by solving a problem given him by mistake and intended for the third graders. The
teacher simply refused to believe that Misha solved it by himself. But when Misha
was 10 years old the teacher told his mother that Misha will be a math professor,
though at that time the future math professor found much more delight in playing
with noxious chemicals.
From 1960 to 1969 Gromov studied at Leningrad University, receiving his mas-
ter degree in 1965 and the ﬁrst doctoral (“candidate”) degree in 1969 under the
direction of V. A. Rokhlin, followed by his second doctoral degree in 1972. During
his undergraduate years he solved several open problems such as a problem of Ba-
nach on the characterization of Banach spaces all of whosek-dimensional subspaces
are isometric. But his ﬁrst major achievement was the far-going generalization in
his PhD dissertation of the Smale–Hirsch immersion theory, which laid the foun-
dation for the area of mathematics that is now known under the name h-principle
(see Chapter 7). Over the next 4 years he made several major advances in this
theory, culminating in his theory of convex integration inspired by Nash–Kuiper’s
C1-isometric embedding theorem.
The h-principle was the subject of Gromov’s invited talk at the International
Congress of Mathematicians 1970 in Nice (which he was not allowed to attend by
the Soviet authorities). This was the ﬁrst of a series of four invited ICM talks of
Gromov, including two plenary addresses.
In 1974 Gromov left Russia and became a professor at the State University of
New York in Stony Brook, USA. In 1981 Gromov moved to France and since that
time has been a permanent member of the Institute des Hautes ´Etudes Scientiﬁque
in Bures-sur-Yvette. From 1991 until 1996 he also held a professor position at the
University of Maryland, College Park, and since 1997 he is a professor at New York
University.

352 C. BIOGRAPHICAL NOTES ON THE MAIN CHARACTERS
Gromov made revolutionary contributions to many branches of mathematics.
His work transformed several classical areas and led to the creation of entirely new
ﬁelds. In particular, his work shaped modern Riemannian geometry, and his intro-
duction of new geometric methods into group theory led to the solution of many
classical problems and the creation of the theory of hyperbolic groups. His fun-
damental paper on pseudo-holomorphic curves in symplectic manifolds essentially
created the ﬁeld of symplectic topology.
Alan Weinstein (born in 1943). Alan Weinstein was born in New York
City. He received his undergraduate degree from the Massachusetts Institute of
Technology, and his Ph.D. from University of California at Berkeley in 1967 under
the direction of S.-S. Chern. After postdoctoral years at the Institute des Hautes
´Etudes Scientiﬁque in Bures-sur-Yvette, MIT, and the University of Bonn, he joined
the faculty at Berkeley in 1969, becoming full professor in 1976. On the occasion
of Weinstein’s 60th birthday his advisor S.-S. Chern wrote ([ 127]):
“Alan came to me in the early sixties as a graduate student at the University of
California at Berkeley. At that time, a prevailing problem in our geometry group,
and the geometry community at large, was whether on a Riemannian manifold the
cut locus and the conjugate locus of a point can be disjoint. Alan immediately
showed that this was possible. The result became a part of his PhD thesis, which
was published in the Annals of Mathematics . He received his PhD degree in a
short period of two years. I introduced him to IHES and the French mathematical
community. He stays close with them and with the mathematical ideas of Charles
Ehresmann. He is original and often came up with ingenious ideas. An example
is his contribution to the solution of the Blaschke conjecture. I am very proud to
count him as one of my students.”
Weinstein became interested in symplectic geometry and its applications to me-
chanics already in the early years of his mathematical career. Marsden-Weinstein
reduction continues to play a fundamental role in classical and quantum mechanics
and in the study of the geometry of moduli spaces. Weinstein did important work
in the theory of periodic orbits of Hamitonian systems. The Weinstein conjecture
about periodic orbits of Reeb vector ﬁelds, along with Arnold’s ﬁxed point conjec-
tures, continues to be one of the driving forces in symplectic topology. Weinstein
made fundamental contributions to Poisson geometry, such as the introduction of
symplectic groupoids. Intertwined with his work on symplectic geometry and me-
chanics, Weinstein did extensive work on geometric partial diﬀerential equations,
eigenvalues, the Schr¨ odinger operator, and geometric quantization.
In [187] Weinstein introduced an object which was in [ 49] called a Weinstein
manifold, and which is one of the main objects studied in this book.
Alan Weinstein is also an inspiring lecturer and a great teacher. Many of the
32 students who obtained a PhD under his direction became themselves well known
mathematicians.

Bibliography
[1] A. Abbondandolo and M. Schwarz, On the Floer homology of cotangent bundles, Comm.
Pure Appl. Math. 59, no. 2, 254–316 (2006).
[2] A. Abbondandolo and M. Schwarz, Floer homology of cotangent bundles and the loop
product, Geom. Topol. 14, no. 3, 1569–1722 (2010).
[3] M. Abouzaid and P. Seidel, Altering symplectic manifolds by homologous recombination,
arXiv:1007.3281.
[4] R. Abraham and J. Robbin, Transversal mappings and ﬂows , with an appendix by
A. Kelley, Benjamin, New York-Amsterdam (1967).
[5] T. Akahori, A new approach to the local embedding theorem of CR-structures for
n≥ 4 (the local solvability for the operator ∂b in the abstract sense) , Mem. Amer.
Math. Soc. 67, no. 366 (1987).
[6] A. Akhmedov, J. Etnyre, T. Mark and I. Smith, A note on Stein ﬁllings of contact
manifolds, Math. Res. Lett. 15, 1127–1132 (2008).
[7] A. Andreotti and T. Frankel, The Lefschetz theorem on hyperplane sections , Ann. of
Math. 69, 717–717 (1959).
[8] A. Andreotti and R. Narasimhan, A topological property of Runge pairs , Ann. of
Math. 76, 499–509 (1962).
[9] V. I. Arnold, Ordinary Diﬀerential Equations , MIT Press, Cambridge, Massachusetts
(1973).
[10] V.I. Arnold, Mathematical Methods of Classical Mechanics , Springer (1978).
[11] V.I. Arnold, Geometrical Methods in the Theory of Ordinary Diﬀerential Equations ,
Springer (1983).
[12] W. Ballmann, Lectures on K¨ ahler manifolds, ESI Lectures in Mathematics and Physics,
European Mathematical Society, Z¨ urich (2006).
[13] A. Banyaga, Sur la structure du groupe des diﬀ´ eomorphismes qui pr´ eservent une forme
symplectique, Comment. Math. Helv. 53, no. 2, 174–227 (1978).
[14] S. Batterson, Stephen Smale: The Mathematician Who Broke the Dimension Barrier ,
Amer. Math. Soc. (2000).
[15] E. Bedford and B. Gaveau, Envelopes of holomorphy of certain 2-spheres in C2, Amer.
J. Math. 105, no. 4, 975–1009 (1983).
[16] D. Bennequin, Entrelacements et ´ equations de Pfaﬀ, Third Schnepfenried geometry con-
ference, Vol. 1 (Schnepfenried 1982), 87-161, Ast´ erisque107-108, Soc. Math. France,
Paris (1983).
[17] P. Biran, Lagrangian barriers and symplectic embeddings, Geom. Funct. Anal.11, no. 3,
407–464 (2001).
[18] E. Bishop, Mappings of partially analytic spaces , Amer. J. Math. 83, 209–242 (1961).
[19] E. Bishop, Diﬀerentiable manifolds in complex Euclidean space , Duke Math. J. 32,
1–21 (1965).
[20] F. Bogomolov and B. de Oliveira, Stein small deformations of strictly pseudoconvex
surfaces, Birational algebraic geometry (Baltimore, 1996), 25–41, Contemp. Math. 207,
Amer. Math. Soc. (1997).
[21] R. Bott, The stable homotopy of the classical groups , Ann. of Math. (2) 70, 313–337
(1959).
[22] R. Bott, Marston Morse and his mathematical works , Bull. Amer. Math. Soc. 3, no. 3,
907–950 (1980).
[23] R. Bott and J. Milnor, On the parallelizability of the spheres, Bull. Amer. Math. Soc. 64,
87–91 (1958).
353

354 BIBLIOGRAPHY
[24] F. Bourgeois, T. Ekholm and Y. Eliashberg, Eﬀect of Legendrian Surgery , arXiv:
0911.0026.
[25] F. Bruhat and H. Whitney, Quelques propri´ et´ es fondamentales des ensembles analy-
tiques-r´ eels, Comment. Math. Helv. 33, 132-160 (1959).
[26] A. Cannas da Silva, Lectures on Symplectic Geometry, Springer (2001).
[27] H. Cartan, Vari´ et´ es analytiques complexes et cohomologie, Colloque sur les fonctions
de plusieurs variables (tenu ` a Bruxelles 1953), 41-55, Georges Thone, Li` ege; Masson &
Cie, Paris (1953).
[28] H. Cartan, Vari´ et´ es analytiques r´ eelles et vari´ et´ es analytiques complexes, Bull. Soc.
Math. France 85, 77–99 (1957).
[29] D. Catlin, A Newlander-Nirenberg theorem for manifolds with boundary , Michigan
Math. J. 35, no. 2, 233–240 (1988).
[30] J. Cerf, La stratiﬁcation naturelle des espaces de fonctions diﬀ´ erentiables r´ eelles et le
th´ eor` eme de la pseudo-isotopie, Inst. Hautes ´Etudes Sci. Publ. Math. 39, 5–173 (1970).
[31] Y. Chekanov, Diﬀerential algebra of Legendrian links , Invent. Math. 150, no. 3, 441–
483 (2002).
[32] K. Cieliebak, Handle attaching in symplectic homology and the chord conjecture, J. Eur.
Math. Soc. (JEMS) 4, no. 2, 115–142 (2002).
[33] K. Cieliebak, Subcritical Stein manifolds are split , preprint 2002.
[34] K. Cieliebak, A. Floer and H. Hofer, Symplectic homology II: A general construction ,
Math. Z. 218, no. 1, 103–122 (1995).
[35] K. Cieliebak, U. Frauenfelder and A. Oancea, Rabinowitz Floer homology and symplec-
tic homology, Ann. Sci. ´Ec. Norm. Sup´ er. (4)43, no. 6, 957–1015 (2010).
[36] J.-P. Demailly, Complex analytic and diﬀerential geometry , preliminary version avail-
able on the author’s homepage.
[37] P. De Paepe, Eva Kallin’s lemma on polynomial convexity, Bull. London Math. Soc. 33,
no. 1, 1–10 (2001).
[38] F. Docquier, H. Grauert, Levisches Problem und Rungescher Satz f¨ ur Teilgebiete Stein-
scher Mannigfaltigkeiten, Math. Ann. 140, 94–123 (1960).
[39] K. Dymara, Legendrian knots in overtwisted contact structures on S3, Ann. Global
Anal. Geom. 19, no. 3, 293–305 (2001).
[40] T. Ekholm, J. Etnyre and M. Sullivan, Non-isotopic Legendrian submanifolds in R2n+1,
J. Diﬀ. Geom. 71, no. 1, 85–128 (2005).
[41] Y. Eliashberg, Classiﬁcation of overtwisted contact structures on 3-manifolds, Invent.
Math. 98, no. 3, 623–637 (1989).
[42] Y. Eliashberg, Topological characterization of Stein manifolds of dimension > 2, Inter-
nat. J. Math. 1, no. 1, 29-46 (1990).
[43] Y. Eliashberg, Filling by holomorphic discs and its applications , London Math. Soc.
Lect. Notes 151, 45–68 (1991).
[44] Y. Eliashberg, Contact 3-manifolds 20 years since J. Martinet’s work , Ann. Inst.
Fourier 42, 165–192 (1992).
[45] Y. Eliashberg, A few remarks about symplectic ﬁlling , Geom. Topol. 8, 277–293 (2004).
[46] Y. Eliashberg, Unique holomorphically ﬁllable contact structure on the 3-torus, Inter-
nat. Math. Res. Notices 1996, no. 2, 77–82.
[47] Y. Eliashberg, Symplectic geometry of plurisubharmonic functions, Notes by M. Abreu,
NATO Adv. Sci. Inst. Ser. C Math. Phys. Sci. 488, Gauge theory and symplectic ge-
ometry (Montreal, 1995), 49–67, Kluwer Acad. Publ. (1997).
[48] Y. Eliashberg and M. Fraser, Topologically trivial Legendrian knots, J. Symp. Geom. 7,
no. 2, 77–127 (2009).
[49] Y. Eliashberg and M. Gromov, Convex Symplectic Manifolds, Proceedings of Symposia
in Pure Mathematics, vol. 52, Part 2, 135–162 (1991).
[50] Y. Eliashberg and M. Gromov, Embeddings of Stein manifolds of dimension n into the
aﬃne space of dimension 3n/2 + 1, Ann. of Math. 136, 123-135 (1992).
[51] Y. Eliashberg and V. Kharlamov, On the number of complex points of a real surface
in a complex surface , Proc. Leningrad International Topology Conference, Leningrad,
1982, 143–148 (1984).
[52] Y. Eliashberg and N. Mishachev, Introduction to the h-Principle, Amer. Math. Soc.
(2002).

BIBLIOGRAPHY 355
[53] J. Etnyre, Introductory lectures on contact geometry , Topology and geometry of ma-
nifolds (Athens, GA, 2001), 81–107, Proc. Sympos. Pure Math. 71, Amer. Math. Soc.
(2003).
[54] J. Etnyre, On Symplectic Fillings , Algebr. Geom. Topol. 4, 73–80 (2004).
[55] J. Etnyre, Legendrian and Transversal Knots , Handbook of Knot Theory, 105–185,
Elsevier (2005).
[56] J. Etnyre and K. Honda, On the nonexistence of tight contact structures , Ann. of
Math. (2) 153, no. 3, 749–766 (2001).
[57] A. Floer and H. Hofer, Symplectic homology I: Open sets in Cn, Math. Z. 215, no. 1,
37–88 (1994).
[58] G. Folland, Introduction to Partial Diﬀerential Equations , Princeton Univ. Press
(1976).
[59] J. E. Fornaess and B. Stensønes, Lectures on Counterexamples in Several Complex
Variables, Princeton Univ. Press (1987), reprinted by AMS Chelsea (2007).
[60] F. Forstneriˇ c,Stein Manifolds and Holomorphic Mappings , Springer (2011).
[61] F. Forstneriˇ c and F. L´ arusson,Survey of Oka theory , New York J. Math. 17a, 1–28
(2011).
[62] F. Forstneriˇ c, E. Løw and N. Øvrelid,Solving the d- and ∂-equations in thin tubes and
applications to mappings , Michigan Math. J. 49, 369–416 (2001).
[63] F. Forstneriˇ c and M. Slapar,Stein structures and holomorphic mappings, Math. Z. 256,
no. 3, 615–646 (2007).
[64] H. Geiges, Symplectic manifolds with disconnected boundary of contact type, Int. Math.
Res. Not. 1994, no. 1, 23–30.
[65] H. Geiges, An introduction to contact topology , Cambridge Univ. Press (2008).
[66] E. Giroux, Convexit´ e en topologie de contact, Comment. Math. Helv. 66, no. 4, 637–677
(1991).
[67] E. Giroux, Une inﬁnit´ e de structures de contact tendues sur une inﬁnit´ e de vari´ et´ es,
Invent. Math. 135, 789–802 (1999).
[68] E. Giroux, Structures de contact en dimension trois et bifurcations des feuilletages de
surfaces, Invent. Math. 141, no. 3, 615–689 (2000).
[69] R. Gompf, A new construction of symplectic manifolds , Ann. of Math. 142, 527–595
(1995).
[70] R. Gompf, Handlebody construction of Stein surfaces , Ann. of Math. 148, no. 2, 619–
693 (1998).
[71] R. Gompf, Stein surfaces as open subsets of C2, Conference on Symplectic Topology,
J. Symp. Geom. 3, no. 4, 565–587 (2005).
[72] R. Gompf, Constructing Stein manifolds after Eliashberg , New perspectives and chal-
lenges in symplectic ﬁeld theory, 229–249, CRM Proc. Lecture Notes 49, Amer. Math.
Soc. (2009).
[73] R. Gompf, Smooth embeddings with Stein surface images , arXiv:1110.1865.
[74] R. Gompf and A. Stipsicz, 4 -Manifolds and Kirby Calculus , Amer. Math. Soc. (1999).
[75] J. Gray, Some global properties of contact structures , Ann. of Math. (2) 69, 421–450
(1959).
[76] H. Grauert, Holomorphe Funktionen mit Werten in komplexen Lieschen Gruppen ,
Math. Ann. 133, 450–472 (1957).
[77] H. Grauert, On Levi’s problem and the imbedding of real-analytic manifolds , Ann. of
Math. (2) 68, 460-472 (1958).
[78] H. Grauert and R. Remmert, Theory of Stein Spaces , Springer (1979).
[79] H. Grauert and R. Remmert, Coherent Analytic Sheaves, Springer (1984).
[80] P. Griﬃths and J. Harris, Principles of Algebraic Geometry , John Wiley & Sons, New
York (1978).
[81] M. Gromov, A topological technique for the construction of solutions of diﬀerential
equations and inequalities, ICM 1970, Nice, vol. 2, 221-225 (1971).
[82] M. Gromov, Convex integration of diﬀerential relations I , Izv. Akad. Nauk SSSR Ser.
Mat. 37, 329–343 (1973).
[83] M. Gromov, Pseudoholomorphic curves in symplectic manifolds , Invent. Math. 82,
no. 2, 307–347 (1985).

356 BIBLIOGRAPHY
[84] M. Gromov, Partial Diﬀerential Relations, Ergebnisse der Mathematik und ihrer Gren-
zgebiete (3) 9, Springer (1986).
[85] M. Gromov, Oka’s principle for holomorphic sections of elliptic bundles , J. Amer.
Math. Soc. 2, 851–897 (1989).
[86] M. Gromov and Y. Eliashberg, Removal of singularities of smooth maps , Izv. Akad.
Nauk SSSR Ser. Mat. 35, 600–626 (1971).
[87] V. Guillemin and A. Pollack, Diﬀerential Topology, Prentice-Hall, Englewood Cliﬀs,
New Jersey (1974).
[88] R. Gunning, Introduction to Holomorphic Functions of Several Variables , Vol. III:
Homological Theory, Wadsworth & Broofs/Cole, Belmont (1990).
[89] R. Gunning and H. Rossi, Analytic Functions of Several Complex Variables , Prentice-
Hall (1965), reprinted by AMS Chelsea (2009).
[90] A. Haeﬂiger, Plongements diﬀ´ erentiables de vari´ et´ es dans vari´ et´ es, Comment. Math.
Helv. 36, 47–82 (1961).
[91] A. Hatcher, Algebraic Topology, Cambridge Univ. Press (2002).
[92] A. Hatcher and J. Wagoner, Pseudo-isotopies of compact manifolds, Ast´ erisque6, Soc.
Math. de France (1973).
[93] G. Henkin and J. Leiterer, Theory of functions on complex manifolds , Monographs in
Mathematics 79, Birkh¨ auser (1984).
[94] C. D. Hill and M. Nacinovich, Stein ﬁllability and the realization of contact manifolds ,
Proc. Amer. Math. Soc. 133, no. 6, 1843–1850 (2005).
[95] R. Hind, Stein ﬁllings of lens spaces , Commun. Contemp. Math. 5, no. 6, 967–982
(2003).
[96] H. Hironaka, Resolution of singularities of an algebraic variety over a ﬁeld of charac-
teristic zero I, II , Ann. of Math. 79, 109–326 (1964).
[97] M. Hirsch, Immersions of manifolds , Trans. Amer. Math. Soc. 93, 242–276 (1959).
[98] M. Hirsch, Diﬀerential Topology, Springer (1976).
[99] H. Hofer, Pseudoholomorphic curves in symplectizations with applications to the Wein-
stein conjecture in dimension three , Invent. Math. 114, no. 3, 515–563 (1993).
[100] H. Hofer and E. Zehnder, Symplectic Invariants and Hamiltonian Dynamics , Birk-
h¨ auser (1994).
[101] K. Honda, On the classiﬁcation of tight contact structures I , Geom. Topol. 4, 309–368
(2000).
[102] L. H¨ ormander,L2 estimates and existence theorems for the ∂ operator, Acta Math. 113,
89–152 (1965).
[103] L. H¨ ormander, An Introduction to Complex Analysis in Several Variables , D. Van
Nostrand Comp., Princeton (1966), 3rd edition North-Holland (1990).
[104] L. H¨ ormander and J. Wermer,Uniform approximation on compact sets in Cn, Math.
Scand. 23, 5–23 (1968).
[105] A. Huckleberry, Hans Grauert: mathematician pur , Mitt. Deutsche Math.-Verein. 16,
no. 2, 75–77 (2008).
[106] A. Huckleberry, Karl Stein (1913–2000), Jahresber. Deutsch. Math.-Verein. 110, no. 4,
195–206 (2008).
[107] K. Igusa, The stability theorem for smooth pseudoisotopies, K-Theory 2, no. 1-2 (1988).
[108] H. Jacobowitz, An Introduction to CR Structures , AMS Mathematical Surveys and
Monographs 32 (1990).
[109] E. Kallin, Fat polynomially convex sets, Function Algebras (Proc. Internat. Sympos. on
Function Algebras, Tulane Univ., 1965), Scott-Foresman, 149–152 (1966).
[110] Y. Kanda, The classiﬁcation of tight contact structures on the 3-torus, Comm. Anal.
Geom. 5, no. 3, 413–438 (1997).
[111] M. Kervaire, Non-parallelizability of the n-sphere for n > 7, Proc. Nat. Acad. of
Sci. USA 44, 280–283 (1958).
[112] M. Kervaire, Le th´ eor` eme de Barden-Mazur-Stallings, Comment. Math. Helv. 40, 31–42
(1965).
[113] S. Kobayashi and K. Nomizu, Foundations of Diﬀerential Geometry , Vol. II, Inter-
science Tracts in Pure and Applied Mathematics No. 15 Vol. II, John Wiley & Sons,
New York (1969).

BIBLIOGRAPHY 357
[114] J. Kohn and H. Rossi, On the extension of holomorphic functions from the boundary
of a complex manifold , Ann. of Math. 81, 451–472 (1965).
[115] A. Kosinski, Diﬀerential Manifolds , Pure and Applied Mathematics 138, Academic
Press, Boston (1993).
[116] S. Krantz, Function Theory of Several Complex Variables , John Wiley & Sons, New
York (1982), 2nd edition reprinted by AMS Chelsea (2001).
[117] P. Kronheimer and T. Mrowka, The genus of embedded surfaces in the projective plane,
Math. Res. Lett. 1, no. 6, 797–808 (1994).
[118] M. Kuranishi, Strongly pseudo-convex CR structures over small balls, Part III , Ann. of
Math. 116, 249–330 (1982).
[119] H.-F. Lai, Characteristic classes of real manifolds immersed in complex manifolds ,
Trans. Amer. Math. Soc. 172, 1–33 (1972).
[120] P. Landweber, Complex structures on open manifolds , Topology 13, 69–75 (1974).
[121] S. Lefschetz, L’Analysis situs et la g´ eom´ etrie alg´ ebrique, Collection de Monographies
publi´ ee sous la direction de M. Emile Borel, Gauthier-Villars, Paris (1924).
[122] L. Lempert, Algebraic approximations in analytic geometry , Invent. Math. 121, no. 2,
335–353 (1995).
[123] P. Lisca, Symplectic ﬁllings and positive scalar curvature , Geom. Topol. 2, 103–116
(1998).
[124] P. Lisca, On symplectic ﬁllings of lens spaces , Trans. Amer. Math. Soc. 360, 765–799
(2008).
[125] P. Lisca and G. Matiˇ c, Tight contact structures and Seiberg-Witten invariants , In-
vent. Math. 129, 509–525 (1997).
[126] R. Lutz, Structures de contact sur les ﬁbr´ es principaux en cercles de dimension trois ,
Ann. Inst. Fourier (Grenoble) 27, 1–15 (1977).
[127] J. Marsden and T. Ratiu (eds.), The breadth of symplectic and Poisson geometry ,
Birkh¨ auser (2005).
[128] J. Martinet, Formes de contact sur les vari´ et´ es de dimension 3, Proceedings of Liv-
erpool Singularities Symposium II (1969/1970), 142-163, Lecture Notes in Math. 209,
Springer (1971).
[129] J. Martinet, Singularities of Smooth Functions and Maps , Cambridge Univ. Press
(1982).
[130] P. Massot, K. Niederkr¨ uger and C. Wendl,Weak and strong ﬁllability of higher dimen-
sional contact manifolds , arXiv:1111.6008.
[131] M. Maydanskiy, Exotic symplectic manifolds from Lefschetz ﬁbrations, arXiv:0906.2224.
[132] M. Maydanskiy and P. Seidel, Lefschetz ﬁbrations and exotic symplectic structures on
cotangent bundles of spheres , J. Topol. 3, no. 1, 157–180 (2010).
[133] D. McDuﬀ, Symplectic manifolds with contact type boundaries , Invent. Math. 103,
no. 3, 651–671 (1991).
[134] D. McDuﬀ, Blow ups and symplectic embeddings in dimension 4, Topology 30, 409–421
(1991).
[135] D. McDuﬀ, The local behavior of holomorphic curves in almost complex manifolds ,
J. Diﬀ. Geom. 34, 143–164 (1991).
[136] D. McDuﬀ and D. Salamon, Introduction to Symplectic Topology, 2nd edition, Oxford
Univ. Press (1998).
[137] M. McLean, Lefschetz ﬁbrations and symplectic homology , Geom. Topol. 13, no. 4,
1877–1944 (2009).
[138] M. Micallef and B. White, The structure of branch points in minimal surfaces and in
pseudoholomorphic curves, Ann. of Math. 141, 35–85 (1995).
[139] J. Milnor, Morse Theory, Based on lecture notes by M. Spivak and R. Wells, Annals of
Mathematics Studies 51, Princeton University Press, Princeton (1963).
[140] J. Milnor, Lectures on the h-Cobordism Theorem, Notes by L. Siebenmann and J. Son-
dow, Princeton Univ. Press, Princeton (1965).
[141] J. Morgan and G. Tian, Ricci ﬂow and the Poincar´ e conjecture, Clay Mathematics
Monographs 3, Amer. Math. Soc. (2007).
[142] J. Munkres, Obstructions to the smoothing of piecewise-diﬀerentiable homeomorphisms,
Ann. of Math. 72, 521–554 (1960).

358 BIBLIOGRAPHY
[143] E. Murphy, Loose Legendrian embeddings in high dimensional contact manifolds ,
arXiv:1201.2245.
[144] R. Narasimhan, Imbedding of holomorphically complete complex spaces , Amer. J.
Math. 82, 917–934 (1960).
[145] R. Narasimhan, A note on Stein spaces and their normalisations , Ann. Scuola Norm.
Sup. Pisa (3) 16, no. 4, 327–333 (1962).
[146] A. N´ emethi and P. Popescu-Pampu, Milnor ﬁbers of cyclic quatient singularities ,
arXiv:0805.3449v2.
[147] S. Nemirovski, Complex analysis and diﬀerential topology on complex surfaces, Russian
Math. Surveys 54, no. 4, 729–752 (1999).
[148] S. Nemirovski, Adjunction inequality and coverings of Stein surfaces , Turkish J.
Math. 27, no. 1, 161–172 (2003).
[149] A. Newlander and L. Nirenberg, Complex analytic coordinates in almost complex ma-
nifolds, Ann. of Math. (2) 65, 391–404 (1957).
[150] L. Ng, A Legendrian Thurston–Bennequin bound from Khovanov homology , Algebr.
Geom. Topol. 5, 1637–1653 (2005).
[151] K. Niederkr¨ uger and O. van Koert, Every contact manifold can be given a nonﬁllable
contact structure, Int. Math. Res. Not. IMRN 2007, no. 23.
[152] A. Nijenhuis and W. Wolf, Some integration problems in almost complex manifolds ,
Ann. of Math. (2) 77, 424–489, (1963).
[153] L. Nirenberg, Lectures on linear partial diﬀerential equations, Amer. Math. Soc. (1973).
[154] K. Oka, Sur les fonctions analytiques de plusieurs variables VII: Sur quelques notions
arithm´ etiques, Bull. Soc. Math. France 78, 1–27 (1950).
[155] Kiyoshi Oka: Collected papers , translated from the French by R. Narasimhan, with
commentaries by H. Cartan, edited by R. Remmert, Springer (1984).
[156] B. Ozbagci and A. Stipsicz, Contact 3-manifolds with inﬁnitely many Stein ﬁllings ,
Proc. Amer. Math. Soc. 132, 1549–1558 (2004).
[157] J. Palis and W. de Melo, Geometric theory of dynamical systems: An introduction ,
Springer (1982).
[158] G. Perelman, Finite extinction time for the solutions to the Ricci ﬂow on certain three-
manifolds, arXiv:math/0307245.
[159] O. Plamenevskaya and J. Van Horn-Morris, Planar open books, monodromy factoriza-
tions and symplectic ﬁllings , Geom. Topol. 14, no. 4, 2077–2101 (2010).
[160] R.M. Range, Holomorphic Functions and Integral Representations in Several Complex
Variables, Springer (1986).
[161] R. Richberg, Stetige streng pseudokonvexe Funktionen , Math. Annalen 175, 251–286
(1968).
[162] A. Ritter, Topological quantum ﬁeld theory structure on symplectic cohomology ,
arXiv:1003.1781.
[163] H. Rossi, Attaching analytic spaces to an analytic space along a pseudoconcave bound-
ary, Proc. Conf. Complex Analysis (Minneapolis, 1964), 242–256, Springer (1965).
[164] L. Rudolph, Quasipositivity as an obstruction to sliceness , Bull. Amer. Math. Soc. 29,
51–59 (1993).
[165] D. Salamon and J. Weber, Floer homology and the heat ﬂow , Geom. Funct. Anal. 16,
no. 5, 1050–1138 (2006).
[166] J. Sch¨ urmann,Embeddings of Stein spaces into aﬃne spaces of minimal dimension ,
Math. Ann. 307, no. 3, 381-399 (1997).
[167] P. Seidel and I. Smith, The symplectic topology of Ramanujam’s surface , Comment.
Math. Helv. 80, no. 4, 859–881 (2005).
[168] P. Seidel, Fukaya categories and Picard-Lefschetz theory, Zurich Lectures in Advanced
Mathematics, European Math. Soc. (2008).
[169] P. Seidel, A biased view of symplectic cohomology, Current developments in mathemat-
ics, 2006, 211–253, Int. Press (2008).
[170] J-P. Serre, Quelques probl` emes globaux relatifs aux vari´ et´ es de Stein, Colloque sur les
fonctions de plusieurs variables (Bruxelles, 1953), 57–68, Georges Thone, Li` ege; Masson
& Cie, Paris (1953).
[171] S. Smale, A classiﬁcation of immersions of the two-sphere, Trans. Amer. Math. Soc.90,
281–290 (1958).

BIBLIOGRAPHY 359
[172] S. Smale, The classiﬁcation of immersions of spheres in Euclidean spaces , Ann. of
Math. 69, 327–344 (1959).
[173] S. Smale, On the structure of manifolds , Amer. J. Math. 84, 387–399 (1962).
[174] I. Smith, Torus ﬁbrations on symplectic four-manifolds , Turkish J. Math. 25, 69–95
(2001).
[175] J. Sotomayor, Generic bifurcations of dynamical systems , Dynamical systems (Proc.
Sympos. Univ. Bahia, Salvador, 1971), Academic Press, 561–582 (1973).
[176] J. Stallings, The piecewise-linear structure of Euclidean space , Proc. Cambridge Phi-
los. Soc. 58, 481–488 (1962).
[177] N. Steenrod, The topology of ﬁbre bundles , Princeton Univ. Press, Princeton (1951).
[178] K. Stein, Analytische Funktionen mehrerer komplexer Ver¨ anderlichen zu vorgegebenen
Periodizit¨ atsmoduln und das zweite Cousinsche Problem , Math. Ann. 123, 201–222
(1951).
[179] E. Stout, Polynomial convexity, Birkh¨ auser (2007).
[180] D. Struppa, The ﬁrst eighty years of Hartogs’ theorem , Geometry Seminars 1987–1988,
Univ. Stud. Bologna, 127–209 (1988).
[181] D. Sullivan, Cycles for the dynamical study of foliated manifolds and complex manifolds,
Invent. Math. 36, 225–255 (1976).
[182] S. Tabachnikov, An invariant of a submanifold that is transversal to a distribution
(Russian), Uspekhi Mat. Nauk 43 (1988), no. 3 (261), 193–194; translation in Russian
Math. Surveys 43, no. 3, 225–226 (1988).
[183] R. Thompson, Singular values and diagonal elements of complex symmetric matrices ,
Linear Algebra Appl. 26, 65–106 (1979).
[184] W. Thurston, Some simple examples of symplectic manifolds , Proc. Amer. Math.
Soc. 55, no. 2, 467–468 (1976).
[185] C. Viterbo, Functors and computations in Floer homology with applications I ,
Geom. Funct. Anal. 9, no. 5, 985–1033 (1999).
[186] A. Weinstein, Symplectic manifolds and their Lagrangian submanifolds , Advances in
Math. 6, 329–346 (1971).
[187] A. Weinstein, Contact surgery and symplectic handlebodies , Hokkaido Math. J. 20,
241–251 (1991).
[188] C. Wendl, Strongly ﬁllable contact manifolds and J-holomorphic foliations, Duke Math.
J. 151, no. 3, 337–384 (2010).
[189] H. Whitney, Analytic extensions of diﬀerentiable functions deﬁned in closed sets, Trans.
Amer. Math. Soc. 36, no. 1, 63–89 (1934).
[190] H. Whitney, Diﬀerentiable manifolds, Ann. of Math. (2) 37, no. 3, 645–680 (1936).
[191] H. Whitney, The self-intersections of a smooth n-manifold in 2n-space, Ann. of
Math. (2) 45, 220–246 (1944).
[192] H. Whitney, On singularities of mappings of Euclidean spaces I. Mappings of the plane
into the plane , Ann. of Math. (2) 62, no. 3, 374–410 (1955).
[193] H. Whitney, Interview with A. Tucker and W. Aspray, 10 April 1984, The Princeton
Mathematics Community in the 1930s, Transcript Number 43 (PMC43), The Trustees
of Princeton University (1985).
[194] W.-T. Wu, On the isotopy of Cr-manifolds of dimension n in euclidean (2n+1)-space,
Sci. Record (N.S.) 2 271–275 (1958).
[195] R. Ye, Filling by holomorphic curves in symplectic 4-manifolds, Trans. Amer. Math.
Soc. 350, no. 1, 213–250 (1998).



Index
admissible partition, 203, 207
almost complex
manifold, 15
structure, 6, 15
almost CR manifold, 147
ample set, 146
analytic
polyhedron, 91
subvariety, 102
backward invariant set, 199
Bennequin’s inequality, 341
birth-death type
critical point, 188
zero, 191
Bishop family, 309
Bott periodicity theorem, 333
boundary connected sum, 321, 325
cancellation family, 207
Cartan’s Theorems A and B, 102
carving, 225
center manifold, 190
Chern class, 117
cobordism, 156
coherent analytic sheaf, 101
coisotropic
neighborhood theorem, 122
submanifold, 119
subspace, 115
compatible pair, 116–118
complete
-ly exhausting function, 21
vector ﬁeld, 20
completion
of Liouville domain, 239
of Weinstein domain, 243
complex
-iﬁcation, 103
curve, 34
manifold, 15
structure, 15
subspace, 117
surface, 7
vector space, 13
concatenation of paths, 140
conformal symplectic normal bundle, 126
contact
form, 28
isotopy extension theorem, 127
structure, 28, 122
contactomorphism, 122
CR
manifold, 110
structure, 110
totally real immersion, 147
creation family, 207
Darboux’s theorem, 118, 125
deformation equivalence, 311
diﬀeotopy, 120
directed immersion, 147
domain of holomorphy, 97
elementary
Lyapunov cobordism, 202
Morse cobordism, 156
Smale cobordism, 202
Smale homotopy, 207
embryonic
critical point, 188
zero, 190
end
connected sum, 326
of a 4-manifold, 320
exact
Lagrangian immersion, 118
symplectic manifold, 118, 237
symplectic map, 237
exhausting function, 3
ﬁeld of complex tangencies, 17
ﬁnite type, 6, 238
ﬂexible
Stein structure, 251
Weinstein structure, 251
ﬂow box, 198
formal
361

362 INDEX
directed embedding, 148
isotropic embedding, 136
isotropic isotopy, 137
Legendrian embedding, 136
Forstneriˇ c–Slapar’s theorem, 179
front projection, 123
generalized Morse function, 3
Gompf’s theorem, 6, 163, 322
gradient
-like vector ﬁeld, 155, 192
vector ﬁeld, 17, 20
Grassmannian, 332
Grauert
Oka principle, 98
theorem, 96
tube, 105
Gray’s stability theorem, 127
Gromov, 131, 306
–Landweber theorem, 161
h-cobordism theorem, 210
h-principle
for CR totally real embeddings, 149
for directed embeddings, 148
for directed immersions, 147
for immersions, 131
for isotropic embeddings, 137
for isotropic immersions, 135
for loose Legendrian embeddings, 146
for totally real embeddings, 148
for totally real immersions, 147
for totally real submersions, 149
H¨ ormander–Wermer’s theorem, 174
handle slide, 211
Hartogs phenomenon, 96
Hermitian
form, 13
metric, 13
structure, 116, 117
vector space, 116
Hessian, 16, 17
Hironaka’s theorem, 111
holomorphic
convexity, 91
ﬁlling, 110, 129
hull, 91
line bundle, 26
holonomy, 209, 239, 256
homotopy
ﬁber, 330
lifting property, 329
hyperbolic zero, 27, 190
i-convex
function, 3
shape, 69
index
of critical point, 16, 187
of zero of vector ﬁeld, 190
integrable almost complex structure, 15
isocontact immersion, 126
isotopy, 133
isotropic
immersion, 123
isotopy, 137
monomorphism, 135
neighborhood theorem, 122, 126
setup, 126
submanifold, 28, 119
subspace, 115
J-convex
CR structure, 110
function, 3, 15, 35
hypersurface, 18
pseudo-isotopy, 8, 303
quadratic form, 14
retract, 171
surrounding, 156
surrounding function, 167
J-lc function, 50
J-orthogonal, 28, 169
J-transverse, 154
K¨ ahler
ﬁlling, 110
form, 119
manifold, 16
metric, 119
Kallin’s lemma, 183
knot, 131
Lagrangian
neighborhood theorem, 122
projection, 123
submanifold, 119
subspace, 115
Legendrian
immersion, 123
isotopy, 141
knot, 141
monomorphism, 135
Levi
-ﬂat hypersurface, 18
form, 18
problem, 93
Liouville
cobordism, 239
domain, 239
ﬁeld, 27, 237
form, 27, 237
homotopy, 239
manifold, 237
loose Legendrian submanifold, 143
lower half-disc, 204
Lyapunov
cobordism, 202

INDEX 363
function, 192
pair, 192
McLean’s theorem, 326
mean normal curvature, 23
minimal complex surface, 7, 308
modulus
of J-convexity, 35
of subharmonicity, 33
molliﬁed function, 37
monomorphism, 131
Morse
-Smale theory, 210
cobordism, 156
function, 3, 187
homotopy, 206, 246
index of critical point, 16, 187
index of zero of vector ﬁeld, 190
inequalities, 210
lemma, 187
Moser
stability theorem, 120
trick, 119
Murphy’s h-principle, 146
Narasimhan’s theorem, 22
negative line bundle, 26
Newlander-Nirenberg theorem, 15
Nijenhuis tensor, 15
nondegenerate
2-form, 27
critical point, 187
zero, 190
normalized
Levi form, 23
modulus of J-convexity, 52
nullity, 187
Oka
–Weil theorem, 92
coherence theorem, 101
principle, 98
Op A, 9
overtwisted
contact structure, 141
disc, 141
path lifting property, 329
Perelman’s theorem, 320
perfect Morse function, 210
plurisubharmonic
function, 3, 35
hull, 93
Poincar´ e-Hopf index theorem, 139
polynomial
convexity, 91
hull, 91
positive line bundle, 26
proﬁle, 188, 207
pseudo-isotopy, 8, 213
real analytic
function, 103
manifold, 103
reducible 3-manifold, 315
Reeb vector ﬁeld, 122
Richberg’s theorem, 36
Rossi’s theorem, 111
rotation invariant, 337
absolute, 337
second fundamental form, 23
self-indexing Morse function, 211
self-intersection
index of immersion, 132
index of regular homotopy, 133
invariant, 338
Serre ﬁbration, 209, 329
shape of hypersurface, 61
skeleton, 155, 198, 238
Smale
–Hirsch immersion theorem, 131
cobordism, 202
h-cobordism theorem, 210
homotopy, 206, 246
trick, 212
stabilization
of Legendrian submanifold, 137
of Weinstein manifold, 243
stable
disc, 156, 202
homotopy group, 333
manifold, 27, 190
standard
complex structure, 3
contact structure, 123
symplectic form, 13
Stein
cobordism, 164, 244
domain, 4, 244
ﬁlling, 110, 310
homotopy, 246
manifold, 3, 95, 244
structure, 7, 244
submanifold, 96
surface, 6
Stiefel manifold, 332
Struwe’s diﬀerential equation, 71
subcritical
Stein structure, 250
Weinstein structure, 250
subharmonic function, 33
surgery, 316
exact sequence, 325
symplectic
basis, 116
ﬁlling, 129
form, 27

364 INDEX
group, 117
homology, 324
manifold, 118
neighborhood theorem, 121
normal bundle, 126
pseudo-isotopy, 292
structure, 117
submanifold, 119
subspace, 115
vector space, 115
symplectization, 128
symplectomorphism, 118
tame almost complex structure, 308
target
equivalent function, 4
reparametrization, 4
Thurston-Bennequin invariant
absolute, 339
relative, 339
tight contact structure, 141
totally real
epimorphism, 149
submanifold, 24
submersion, 149
subspace, 116
transfer map, 324
two-index theorem, 212
unstable
disc, 202
manifold, 190
weak
-ly J-convex, 15, 18, 100
-ly gradient-like vector ﬁeld, 192
Lyapunov function, 192
Lyapunov pair, 192
Weinstein
cobordism, 243
domain, 5, 243
ﬁlling, 244
homotopy, 246
Lagrangian neighborhood theorem, 122
manifold, 4, 243
structure, 4, 243
Whitney
disc, 133
embedding theorem, 132
trick, 133
ω
-convex, 128
-limit set, 198
-orthogonal complement, 115

