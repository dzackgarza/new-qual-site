Introduction to Differential Geometry
Lecture Notes for MAT367

Contents
1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1 Some history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 The concept of manifolds: Informal discussion . . . . . . . . . . . . . . . . . . 3
1.3 Manifolds in Euclidean space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Intrinsic descriptions of manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.5 Surfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.1 Atlases and charts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2 Deﬁnition of manifold . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.3 Examples of Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.3.1 Spheres . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.3.2 Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.3.3 Real projective spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.3.4 Complex projective spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.3.5 Grassmannians . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.3.6 Complex Grassmannians . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.4 Oriented manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.5 Open subsets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.6 Compact subsets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
2.7 Appendix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
2.7.1 Countability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
2.7.2 Equivalence relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3 Smooth maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.1 Smooth functions on manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.2 Smooth maps between manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.2.1 Diffeomorphisms of manifolds . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.3 Examples of smooth maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.3.1 Products, diagonal maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.3.2 The diffeomorphism RP1∼= S1 . . . . . . . . . . . . . . . . . . . . . . . . . 45
-3

-2 Contents
3.3.3 The diffeomorphism CP1∼= S2 . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.3.4 Maps to and from projective space . . . . . . . . . . . . . . . . . . . . . . 47
3.3.5 The quotient map S2n+1→ CPn . . . . . . . . . . . . . . . . . . . . . . . . 48
3.4 Submanifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
3.5 Smooth maps of maximal rank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.5.1 The rank of a smooth map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.5.2 Local diffeomorphisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
3.5.3 Level sets, submersions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.5.4 Example: The Steiner surface . . . . . . . . . . . . . . . . . . . . . . . . . . 62
3.5.5 Immersions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
3.6 Appendix: Algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
4 The tangent bundle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
4.1 Tangent spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
4.2 Tangent map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
4.2.1 Deﬁnition of the tangent map, basic properties . . . . . . . . . . . . 76
4.2.2 Coordinate description of the tangent map . . . . . . . . . . . . . . . 78
4.2.3 Tangent spaces of submanifolds . . . . . . . . . . . . . . . . . . . . . . . . 80
4.2.4 Example: Steiner’s surface revisited . . . . . . . . . . . . . . . . . . . . . 84
4.3 The tangent bundle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
5 Vector ﬁelds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
5.1 Vector ﬁelds as derivations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
5.2 Vector ﬁelds as sections of the tangent bundle . . . . . . . . . . . . . . . . . . . 89
5.3 Lie brackets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
5.4 Related vector ﬁelds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
5.5 Flows of vector ﬁelds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
5.6 Geometric interpretation of the Lie bracket . . . . . . . . . . . . . . . . . . . . . 104
5.7 Frobenius theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
5.8 Appendix: Derivations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
6 Differential forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
6.1 Review: Differential forms on Rm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
6.2 Dual spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
6.3 Cotangent spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
6.4 1-forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
6.5 Pull-backs of function and 1-forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
6.6 Integration of 1-forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
6.7 2-forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
6.8 k-forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
6.8.1 Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
6.8.2 Wedge product . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
6.8.3 Exterior differential . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
6.9 Lie derivatives and contractions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
6.9.1 Pull-backs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130

Contents -1
6.10 Integration of differential forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
6.11 Integration over oriented submanifolds . . . . . . . . . . . . . . . . . . . . . . . . . 133
6.12 Stokes’ theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
6.13 V olume forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
A Topology of manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
A.1 Topological notions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
A.2 Manifolds are second countable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
A.3 Manifolds are paracompact . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
A.4 Partitions of unity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
B Vector bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
B.1 Tangent bundle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
B.1.1 Vector bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
B.1.2 Tangent bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
B.1.3 Some constructions with vector bundles . . . . . . . . . . . . . . . . . 151
B.2 Dual bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154



Chapter 1
Introduction
1.1 Some history
In the words of S.S. Chern, ”the fundamental objects of study in differential geome-
try are manifolds.” 1 Roughly, an n-dimensional manifold is a mathematical object
that “locally” looks like Rn. The theory of manifolds has a long and complicated
history. For centuries, manifolds have been studied as subsets of Euclidean space,
given for example as level sets of equations. The term ‘manifold’ goes back to the
1851 thesis of Bernhard Riemann, “Grundlagen f ¨ur eine allgemeine Theorie der
Functionen einer ver ¨anderlichen complexen Gr ¨osse” (“foundations for a general
theory of functions of a complex variable”) and his 1854 habilitation address“ ¨Uber
die Hypothesen, welche der Geometrie zugrunde liegen” (“on the hypotheses un-
derlying geometry”).
2 However, in neither reference Riemann makes an attempt to give a precise deﬁ-
nition of the concept. This was done subsequently by many authors, including Rie-
1 Page 332 of Chern, Chen, Lam: Lectures on Differential Geometry, World Scientiﬁc
2 http://en.wikipedia.org/wiki/Bernhard_Riemann
1

2 1 Introduction
mann himself. 3 Henri Poincar´e in his 1895 work analysis situs, introduces the idea
of a manifold atlas. 4
The ﬁrst rigorous axiomatic deﬁnition of manifolds was given by Veblen and White-
head only in 1931.
We will see below that the concept of a manifold is really not all that compli-
cated; and in hindsight it may come as a bit of a surprise that it took so long to
evolve. Quite possibly, one reason is that for quite a while, the concept as such
was mainly regarded as just a change of perspective (away from level sets in Eu-
clidean spaces, towards the ‘intrinsic’ notion of manifolds). Albert Einstein’s theory
of General Relativity from 1916 gave a major boost to this new point of view; In his
theory, space-time was regarded as a 4-dimensional ‘curved’ manifold with no dis-
tinguished coordinates (not even a distinguished separation into ‘space’ and ‘time’);
a local observer may want to introduce local xyzt coordinates to perform measure-
ments, but all physically meaningful quantities must admit formulations that are
coordinate-free. At the same time, it would seem unnatural to try to embed the 4-
dimensional curved space-time continuum into some higher-dimensional ﬂat space,
in the absence of any physical signiﬁcance for the additional dimensions. Some
years later, gauge theory once again emphasized coordinate-free formulations, and
provided physics motivations for more elaborate constructions such as ﬁber bundles
and connections.
Since the late 1940s and early 1950s, differential geometry and the theory of
manifolds has developed with breathtaking speed. It has become part of the ba-
sic education of any mathematician or theoretical physicist, and with applications
in other areas of science such as engineering or economics. There are many sub-
branches, for example complex geometry, Riemannian geometry, or symplectic ge-
ometry, which further subdivide into sub-sub-branches.
3 See e.g. the article by Scholz http://www.maths.ed.ac.uk/ aar/papers/scholz.pdf for the long list
of names involved.
4 http://en.wikipedia.org/wiki/Henri_Poincare

1.2 The concept of manifolds: Informal discussion 3
1.2 The concept of manifolds: Informal discussion
To repeat, ann-dimensional manifold is something that “locally” looks likeRn. The
prototype of a manifold is the surface of planet earth:
It is (roughly) a 2-dimensional sphere, but we use local charts to depict it as subsets
of 2-dimensional Euclidean spaces. 5
To describe the entire planet, one uses an atlas with a collection of such charts, such
that every point on the planet is depicted in at least one such chart.
This idea will be used to give an ‘intrinsic’ deﬁnition of manifolds, as essentially
a collection of charts glued together in a consistent way. One can then try to de-
velop analysis on such manifolds – for example, develop a theory of integration and
differentiation, consider ordinary and partial differential equations on manifolds, by
working in charts; the task is then to understand the ‘change of coordinates’ as one
leaves the domain of one chart and enters the domain of another.
5 Note that such a chart will always give a somewhat ‘distorted’ picture of the planet; the distances
on the sphere are never quite correct, and either the areas or the angles (or both) are wrong. For
example, in the standard maps of the world, Canada always appears somewhat bigger than it really
is. (Even more so Greenland, of course.)

4 1 Introduction
1.3 Manifolds in Euclidean space
In multivariable calculus, you will have encountered manifolds as solution sets of
equations. For example, the solution set of an equation of the form f (x,y,z) = a
in R3 deﬁnes a ‘smooth’ hypersurface S⊆ R3 provided the gradient of f is non-
vanishing at all points of S. We call such a value of f a regular value, and hence
S = f−1(a) a regular level set. Similarly, the joint solution set C of two equations
f (x,y,z) = a, g(x,y,z) = b
deﬁnes a smooth curve in R3, provided (a,b) is a regular value of ( f ,g) in the sense
that the gradients of f and g are linearly independent at all points of C. A familiar
example of a manifold is the 2-dimensional sphere S2, conveniently described as a
level surface inside R3:
S2 ={(x,y,z)∈ R3| x2 + y2 + z2 = 1}.
There are many ways of introducing local coordinates on the 2-sphere: For exam-
ple, one can use spherical polar coordinates, cylindrical coordinates, stereographic
projection, or orthogonal projections onto the coordinate planes. We will discuss
some of these coordinates below. More generally, one has then-dimensional sphere
Sn inside Rn+1,
Sn ={(x0, . . . ,xn)∈ Rn+1| (x0)2 + . . .+ (xn)2 = 1}.
The 0-sphere S0 consists of two points, the 1-sphere S1 is the unit circle. Another
example is the 2-torus, T 2. It is often depicted as a surface of revolution: Given real
numbers r,R with 0 < r < R, take a circle of radius r in the x− z plane, with center
at (R,0), and rotate about the z-axis.
The resulting surface6 is given by an equation,
T 2 ={(x,y,z)|
(√
x2 + y2− R
)2 + z2 = r2}. (1.1)
Not all surfaces can be realized as ‘embedded’ in R3; for non-orientable surfaces
one needs to allow for self-intersections. This type of realization is referred to as an
6 http://calculus.seas.upenn.edu/?n=Main.CentroidsAndCentersOfMass.

1.4 Intrinsic descriptions of manifolds 5
immersion: We don’t allow edges or corners, but we do allow that different parts of
the surface pass through each other. An example is the Klein bottle7
The Klein bottle is an example of a non-orientable surface: It has only one side. (In
fact, the Klein bottle contains a M ¨obius band – see exercises.) It is not possible to
represent it as a regular level set f−1(0) of a function f : For any such surface one
has one side where f is positive, and another side where f is negative.
1.4 Intrinsic descriptions of manifolds
In this course, we will mostly avoid concrete embeddings of manifolds into anyRN.
Here, the term ‘embedding’ is used in an intuitive sense, for example as the real-
ization as the level set of some equations. (Later, we will give a precise deﬁnition.)
There are a number of reasons for why we prefer developing an ‘intrinsic’ theory of
manifolds.
1. Embeddings of simple manifolds in Euclidean space can look quite complicated.
The following one-dimensional manifold8
is intrinsically, ‘as a manifold’, just a closed curve, that is, a circle. The problem
of distinguishing embeddings of a circle intoR3 is one of the goals ofknot theory,
a deep and difﬁcult area of mathematics.
2. Such complications disappear if one goes to higher dimensions. For example, the
above knot (and indeed any knot in R3) can be disentangled inside R4 (with R3
viewed as a subspace). Thus, in R4 they become unknots.
3. The intrinsic description is sometimes much simpler to deal with than the extrin-
sic one. For instance, the equation describing the torus T 2⊆ R3 is not especially
7 http://www.map.mpim- bonn.mpg.de/2- manifolds
8 http://math201s09.wdfiles.com/local- - files/medina- knot/alternating.jpg

6 1 Introduction
simple or beautiful. But once we introduce the following parametrization of the
torus
x = (R + r cos ϕ)cos θ , y = (R + r cos ϕ)sin θ , z = r sin ϕ,
where θ , ϕ are determined up to multiples of 2π, we recognize that T 2 is simply
a product:
T 2 = S1× S1. (1.2)
That is, T 2 consists of ordered pairs of points on the circle, with the two factors
corresponding to θ , ϕ. In contrast to (1.1), there is no distinction between ‘small’
circle (of radius r) and ‘large circle’ (of radiusR). The new description suggests
an embedding of T 2 into R4 which is ‘nicer’ then the one in R3. (But does it
help?)
4. Often, there is no natural choice of an embedding of a given manifold inside RN,
at least not in terms of concrete equations. For instance, while the triple torus 9
is easily pictured in 3-space R3, it is hard to describe it concretely as the level set
of an equation.
5. While many examples of manifolds arise naturally as level sets of equations in
some Euclidean space, there are also many examples for which the initial con-
struction is different. For example, the set M whose elements are all afﬁne lines
in R2 (that is, straight lines that need not go through the origin) is naturally a
2-dimensional manifold. But some thought is required to realize it as a surface in
R3.
1.5 Surfaces
Let us brieﬂy give a very informal discussion of surfaces. A surface is the same
thing as a 2-dimensional manifold. We have already encountered some examples:
The sphere, the torus, the double torus, triple torus, and so on:
9 http://commons.wikimedia.org/wiki/File:Triple_torus_illustration.png

1.5 Surfaces 7
All of these are ‘orientable’ surfaces, which essentially means that they have two
sides which you might paint in two different colors. It turns out that these are all
orientable surfaces, if we consider the surfaces ‘intrinsically’ and only consider sur-
faces that are compact in the sense that they don’t go off to inﬁnity and do not
have a boundary (thus excluding a cylinder, for example). For instance, each of the
following drawings depicts a double torus:
We also have one example of a non-orientable surface: The Klein bottle. More ex-
amples are obtained by attaching handles (just like we can think of the torus, double
torus and so on as a sphere with handles attached).
Are these all the non-orientable surfaces? In fact, the answer is no. We have missed
what is in some sense the simplest non-orientable surface. Ironically, it is the surface
which is hardest to visualize in 3-space. This surface is called the projective plane
or projective space, and is denoted RP2. One can deﬁne RP2 as the set of all lines
(i.e., 1-dimensional subspaces) in R3. It should be clear that this is a 2-dimensional
manifold, since it takes 2 parameters to specify such a line. We can label such lines
by their points of intersection with S2, hence we can also think of RP2 as the set
of antipodal (i.e., opposite) points on S2. In other words, it is obtained from S2
by identifying antipodal points. To get a better idea of how RP2 looks like, let us
subdivide the sphere S2 into two parts:
(i) points having distance≤ ε from the equator,
(ii) points having distance≥ ε from the equator.


8 1 Introduction
If we perform the antipodal identiﬁcation for (i), we obtain a M ¨obius strip. If we
perform antipodal identiﬁcation for (ii), we obtain a 2-dimensional disk (think of it
as the points of (ii) lying in the upper hemisphere). Hence,RP2 can also be regarded
as gluing the boundary of a M¨obius strip to the boundary of a disk:
Now, the question arises: Is it possible to realize RP2 smoothly as a surface inside
R3, possibly with self-intersections (similar to the Klein bottle)? Simple attempts of
joining the boundary circle of the M ¨obius strip with the boundary of the disk will
always create sharp edges or corners – try it. Around 1900, David Hilbert posed
this problem to his student Werner Boy, who discovered that the answer is yes. The
following picture of Boy’s surfacewas created by Paul Nylander. 10
There are some nice videos illustrating the construction of the surface: See in par-
ticular
https://www.youtube.com/watch?v=9gRx66xKXek
and
www.indiana.edu/˜minimal/archive/NonOrientable/NonOrientable/
Bryant-anim/web/
While these pictures are very beautiful, it certainly makes the projective space ap-
pear more complicated than it actually is. If one is only interested in RP2 itself,
10 http://mathforum.org/mathimages/index.php/Boy’ s_Surface

1.5 Surfaces 9
rather than its realization as a surface in R3, it is much simpler to work with the
deﬁnition (as a sphere with antipodal identiﬁcation).
Going back to the classiﬁcation of surfaces: It turns out that all closed, connected
surfaces are obtained from either the 2-sphere S2, the Klein bottle, or RP2, by at-
taching handles.
Remark 1.1. Another operation for surfaces, generalizing the procedure of ‘attach-
ing handles’, is the connected sum. Given two surfaces Σ1 and Σ2, remove small
disks around given points p1∈ Σ1 and p2∈ Σ2, to create two surfaces with bound-
ary circles. Then glue-in a cylinder connecting the two boundary circles, without
creating edges. The resulting surface is denoted
Σ1♯Σ2.
For example, the connected sum Σ ♯T 2 is Σ with a handle attached. You may want
to think about the following questions: What is the connected sum of two RP2’s?
And what is the connected sum of RP2 with a Klein bottle? Both must be in the list
of 2-dimensional surfaces given above.



Chapter 2
Manifolds
It is one of the goals of these lectures to develop the theory of manifolds in intrinsic
terms, although we may occasionally use immersions or embeddings into Euclidean
space in order to illustrate concepts. In physics terminology, we will formulate the
theory of manifolds in terms that are ‘manifestly coordinate-free’.
2.1 Atlases and charts
As we mentioned above, the basic feature of manifolds is the existence of ‘local
coordinates’. The transition from one set of coordinates to another should besmooth.
We recall the following notions from multivariable calculus.
Deﬁnition 2.1. Let U⊆ Rm and V⊆ Rn be open subsets. A map F : U→ V is
called smooth if it is inﬁnitely differentiable. The set of smooth functions fromU to
V is denoted C∞(U,V ). The map F is called a diffeomorphism from U to V if it is
invertible, and the inverse map F−1 : V→ U is again smooth.
Example 2.1. The exponential map exp : R→ R, x↦→ exp(x) = ex is smooth. It may
be regarded as a map onto R>0 ={y|y > 0}, and is a diffeomorphism
exp : R→ R>0
with inverse exp−1 = log (the natural logarithm). Similarly,
tan :{x∈ R|− π/2 < x < π/2}→ R
is a diffeomorphism, with inverse arctan.
Deﬁnition 2.2. For a smooth map F∈ C∞(U,V ) between open subsets U⊆ Rm and
V⊆ Rn, and any x∈ U, one deﬁnes the Jacobian matrix DF (x) to be the n× m-
matrix of partial derivatives
(DF(x))i
j = ∂Fi
∂x j
11

12 2 Manifolds
Its determinant is called the Jacobian matrix of F at x.
The inverse function theorem states that F is a diffeomorphism if and only if it is
invertible, and for all x∈ U, the Jacobian matrix DF(x) is invertible. (That is, one
does not actually have to check smoothness of the inverse map!)
The following deﬁnition formalizes the concept of introducing local coordinates.
Deﬁnition 2.3 (Charts). Let M be a set.
1. An m-dimensional (coordinate) chart (U, ϕ) on M is a subset U⊆ M together
with a map ϕ : U→ Rm, such that ϕ(U)⊆ Rm is open and ϕ is a bijection from
U to ϕ(U).
2. Two charts (U, ϕ) and (V, ψ) are called compatible if the subsets ϕ(U∩V ) and
ψ(U∩V ) are open, and the transition map
ψ◦ ϕ−1 : ϕ(U∩V )→ ψ(U∩V )
is a diffeomorphism.
As a special case, charts with U∩V = / 0 are always compatible.
Question: Is compatibility of charts an equivalence relation? (See the appendix to
this section for a reminder of equivalence relations.)
Let (U, ϕ) be a coordinate chart. Given a point p∈ U, and writing ϕ(p) =
(u1, . . . ,um), we say that the ui are the coordinates of p in the given chart. (Letting p
vary, these become real-valued functions p↦→ ui(p).) The transition maps ψ◦ ϕ−1
amount to a change of coordinates. Here is a picture1 of a ‘coordinate change’:
Deﬁnition 2.4 (Atlas). Let M be a set. An m-dimensional atlas on M is a collection
of coordinate charts A ={(Uα , ϕα )} such that
1. The Uα cover all of M, i.e.,⋃
α Uα = M.
1 http://en.wikipedia.org/wiki/Differentiable_manifold

2.1 Atlases and charts 13
2. For all indices α, β, the charts (Uα , ϕα ) and (Uβ , ϕβ ) are compatible.
Example 2.2 (An atlas on the 2-sphere). Let S2⊆ R3 be the unit sphere, consisting
of all (x,y,z)∈ R3 satisfying the equation x2 + y2 + z2 = 1. We shall deﬁne an atlas
with two charts (U+, ϕ+) and (U−, ϕ−). Let n = (0,0,1) be the north pole, let s =
(0,0,−1) be the south pole, and put
U+ = S2−{ s}, U− = S2−{ n}.
Regard R2 as the coordinate subspace of R3 on which z = 0. Let
ϕ+ : U+→ R2, p↦→ ϕ+(p)
be stereographic projection from the south pole. That is, ϕ+(p) is the unique point
of intersection of R2 with the afﬁne line passing through p and s. Similarly,
ϕ− : U−→ R2, p↦→ ϕ−(p)
is stereographic projection from the north pole, where ϕ−(p) is the unique point of
intersection of R2 with the afﬁne line passing through p and n. A picture of ϕ−, with
p′ = ϕ−(p) (the picture uses capital letters): 2
A calculation shows that for p = (x,y,z),
ϕ+(x,y,z) =
( x
1 + z , y
1 + z
)
, ϕ−(x,y,z) =
( x
1− z , y
1− z
)
.
Exercise Verify these formulas.
Both ϕ± : U±→ R2 are bijections onto R2. Let us verify this in detail for the map
ϕ+. Given (u,v) we may solve the equation (u,v) = ϕ+(x,y,z), using the condition
that x2 + y2 + z2 = 1 and z >−1. One has
u2 + v2 = x2 + y2
(1 + z)2 = 1− z2
(1 + z)2 = (1− z)(1 + z)
(1 + z)2 = 1− z
1 + z ,
from which one obtains
z = 1− (u2 + v2)
1 + (u2 + v2) ,
2 http://en.wikipedia.org/wiki/User:Mgnbar/Hemispherical_projection

14 2 Manifolds
and since x = u(1 + z), y = v(1 + z) one obtains
ϕ−1
+ (u,v) =
( 2u
1 + (u2 + v2) , 2v
1 + (u2 + v2) , 1− (u2 + v2)
1 + (u2 + v2)
)
.
For the map ϕ−, we obtain by a similar calculation
ϕ−1
− (u,v) =
( 2u
1 + (u2 + v2) , 2v
1 + (u2 + v2) , (u2 + v2)− 1
1 + (u2 + v2)
)
.
(Actually, it is also clear from the geometry that ϕ−1
+ , ϕ−1
− only differ by the sign of
the z-coordinate.) Note that ϕ+(U+∩U−) = R2\{(0,0)}. The transition map on the
overlap of the two charts is
(ϕ−◦ ϕ−1
+ )(u,v) =
( u
u2 + v2 , v
u2 + v2
)
which is smooth on R2\{(0,0)} as required. ⊓ ⊔
Here is another simple, but less familiar example where one has an atlas with two
charts.
Example 2.3 (Afﬁne lines in R2). A line in a vector space E is the same as a 1-
dimensional subspace. By an afﬁne line, we mean a subset l⊆ E, such that the set
of differences{v− w| v,w∈ l} is a 1-dimensional subspace. Put differently, l is
obtained by adding a ﬁxed vector v0 to all elements of a 1-dimensional subspace.
In plain terms, an afﬁne line is simply a straight line that does not necessarily pass
through the origin.
Let M be a set of afﬁne lines in R2. Let U⊆ M be the subset of lines that are
not vertical, and V⊆ M the lines that are not horizontal. Any l∈ U is given by an
equation of the form
y = mx + b,
where m is the slope and b is the y-intercept. The map ϕ : U→ R2 taking l to (m,b)
is a bijection. On the other hand, lines in V are given by equations of the form
x = ny + c,
and we also have the mapψ : V→ R2 taking such l to (n,c). The intersectionU∩V
are lines l that are neither vertical nor horizontal. Hence, ϕ(U∩V ) is the set of all
(m,b) such that m⁄= 0, and similarly ψ(U∩V ) is the set of all (n,c) such that n⁄= 0.
To describe the transition mapψ◦ ϕ−1 : ϕ(U∩V )→ ψ(U∩V ), we need to express
(n,c) in terms of (m,b). Solving y = mx + b for x we obtain
x = 1
my− b
m .
Thus, n = 1
m and c =− b
m, which shows that the transition map is

2.1 Atlases and charts 15
(ψ◦ ϕ−1)(m,b) = ( 1
m ,− b
m ).
Note that this is smooth; similarly, ϕ◦ ψ−1 is smooth; hence U,V deﬁne an 2-
dimensional atlas on M.
Question: What is the resulting surface?
As a ﬁrst approximation, we may take an m-dimensional manifold to be a set
with an m-dimensional atlas. This is almost the right deﬁnition, but we will make
a few adjustments. A ﬁrst criticism is that we may not want any particular atlas
as part of the deﬁnition: For example, the 2-sphere with the atlas given by stereo-
graphic projections onto the x− y-plane, and the 2-sphere with the atlas given by
stereographic projections onto the y−z-plane, should be one and the same manifold
S2. To resolve this problem, we will use the following notion.
Deﬁnition 2.5. Suppose A ={(Uα , ϕα )} is an m-dimensional atlas on M, and let
(U, ϕ) be another chart. Then (U, ϕ) is said to be compatible with A if it is com-
patible with all charts (Uα , ϕα ) of A .
Example 2.4. On the 2-sphere S2, we had constructed the atlas
A ={(U+, ϕ+), (U−, ϕ−)}
given by stereographic projection. Consider on the chart (V, ψ), with domain V the
set of all (x,y,z)∈ S2 such that y < 0, with ψ(x,y,z) = ( x,z). To check that it is
compatible (U+, ϕ+), note that U+∩V = V , and
ϕ+(U+∩V ) ={(u,v)| v < 0}, ψ(U+∩V ) ={(x,z)| x2 + z2 < 1}
Expressing the coordinates (u,v) = ψ(x,y,z) in terms of x,z and vice versa, we ﬁnd
(x,z) = (ψ◦ ϕ−1
+ )(u,v) =
( 2u
1 + (u2 + v2) , 1− (u2 + v2)
1 + (u2 + v2)
)
(u,v) = (ϕ+◦ ψ−1)(x,z) =
( x
1 + z ,−
√
1− (x2 + z2)
1 + z
)
Both maps are smooth, proving that (V, ψ) is compatible with (U+, ϕ+).
Note that (U, ϕ) is compatible with the atlas A ={(Uα , ϕα )} if and only if the
union A∪{ (U, ϕ)} is again an atlas on M. This suggests deﬁning a bigger atlas, by
using all charts that are compatible with the given atlas. In order for this to work,
we need that the new charts are also compatible not only with the charts of A , but
also with each other.
Lemma 2.1. Let A ={(Uα , ϕα )} be a given atlas on the set M. If two charts
(U, ϕ), (V, ψ) are compatible with A , then they are also compatible with each
other.

16 2 Manifolds
Proof. For every chart Uα, the sets ϕα (U∩Uα ) and ϕα (V∩Uα ) are open, hence
their intersection is open. Since the map ϕα is injective, this intersection is
ϕα (U∩Uα )∩ ϕα (V∩Uα ) = ϕα (U∩V∩Uα ),
see the exercise below. Since ϕ◦ ϕ−1
α : ϕα (U∩Uα )→ ϕ(U∩Uα ) is a diffeomor-
phism, it follows that
ϕ(U∩V∩Uα ) = (ϕ◦ ϕ−1
α )
(
ϕα (U∩V∩Uα )
)
is open. Taking the union over all α, we see that
ϕ(U∩V ) =
⋃
α
ϕ(U∩V∩Uα )
is open. A similar argument applies to ψ(U∩ V ). The transition map ψ◦ ϕ−1 :
ϕ(U∩V )→ ψ(U∩V ) is smooth since for allα, its restriction to ϕ(U∩V∩Uα ) is a
composition of two smooth mapsϕα◦ϕ−1 : ϕ(U∩V∩Uα )−→ϕα (U∩V∩Uα ) and
ψ◦ ϕ−1
α : ϕα (U∩V∩Uα )−→ψ(U∩V∩Uα ). Likewise, the compositionϕ◦ ψ−1 :
ψ(U∩V )→ ϕ(U∩V ) is smooth. ⊓ ⊔
Exercise: Show that if f : X→ Y is an injective map between sets, and A,B⊆ X
are two subsets, then
f (A∩ B) = f (A)∩ f (B). (2.1)
Show that (2.1) is not true, in general, if f is not injective.
Theorem 2.1. Given an atlas A ={(Uα , ϕα )} on M, let ~A be the collection of all
charts (U, ϕ) that are compatible withA . Then ~A is itself an atlas on M, containing
A . In fact, ~A is the largest atlas containing A .
Proof. Note ﬁrst that ~A contains A , since the set of charts compatible with A
contains the charts from the atlas A itself. In particular, the charts in ~A cover M.
By the Lemma, any two charts in ~A are compatible. Hence ~A is an atlas. If (U, ϕ)
is a chart compatible with all charts in ~A , then in particular it is compatible with all
charts in A ; hence (U, ϕ)∈ ~A by the deﬁnition of ~A . This shows that ~A cannot
be extended to a larger atlas.
Deﬁnition 2.6. An atlas A is called maximal if it is not properly contained in any
larger atlas. Given an arbitrary atlasA , one calls ~A (as in Theorem 2.1) themaximal
atlas determined by A .
Remark 2.1. Although we will not need it, let us brieﬂy discuss the notion of equiv-
alence of atlases. (For background on equivalence relations, see the appendix to
this chapter, Section 2.7.2.) Two atlasesA ={(Uα , ϕα )} and A′ ={(U′
α , ϕ′
α )} are
called equivalent if every chart of A is compatible with every chart in A′. For ex-
ample, the atlas on the 2-sphere given by the two stereographic projections to the

2.2 Deﬁnition of manifold 17
x− y-plane is equivalent to the atlas A′ given by the two stereographic projections
to the y− z-plane. Using Lemma 2.1, one sees that equivalence of atlases is indeed
an equivalence relation. (In fact, two atlases are equivalent if and only if their union
is an atlas.) Furthermore, two atlases are equivalent if and only if they are contained
in the same maximal atlas. That is, any maximal atlas determines an equivalence
class of atlases, and vice versa.
2.2 Deﬁnition of manifold
As a next approximation towards deﬁnition of manifolds, we can take an m-
dimensional manifold to be a set M together with an m-dimensional maximal atlas.
This is already quite close to what we want, but for technical reasons we would like
to impose two further conditions.
First of all, we insist thatM can be covered bycountably many coordinate charts.
In most of our examples, M is in fact covered by ﬁnitely many coordinate charts.
This countability condition is used for various arguments involving a proof by in-
duction.
Example 2.5. A simple example that is not countable: Let M = R, with A =
{(Uα , ϕα )} the 0-dimensional maximal (!) atlas, where eachUα consists of a single
point, and ϕα : Uα→{ 0} is the unique map to R0 ={0}. Compatibility of charts
is obvious. But M cannot be covered by countably many of these charts. Thus, we
will not allow to consider R as a zero-dimensional manifold.
Secondly, we would like to avoid the following type of example.
Example 2.6. Let X be a disjoint union of two copies of the real line R. We denote
the two copies by R×{1} and R×{−1}, just so that we can tell them apart. Deﬁne
an equivalence relation on X generated by
(x,1)∼ (x′,−1)⇔ x′ = x < 0,
and let M = X/∼ the set of equivalence classes. That is, we ‘glue’ the two real
lines along their negative real axes (taking care that no glue gets on the origins of
the axes). Here is a (not very successful) attempt to sketch the resulting space:

18 2 Manifolds
As a set, M is a disjoint union of R<0 with two copies of R≥0. Let π : X→ M be
the quotient map, and let
U = π(R×{ 1}), V = π(R×{− 1})
the images of the two real lines. The projection mapX→ R, (x,±1)↦→ x is constant
on equivalence classes, hence it descends to a map f : M→ R; let ϕ : U→ R be
the restriction of f to U and ψ : V→ R the restriction to V . Then
ϕ(U) = ψ(V ) = R, ϕ(U∩V ) = ψ(U∩V ) = R<0,
and the transition map is the identity map. Hence, A ={(U, ϕ), (V, ψ)} is an atlas
for M. A strange feature of M with this atlas is that the points
p = ϕ−1({0}), q = ψ−1({0})
are ‘arbitrarily close’, in the sense that if I,J⊆ R are any open subsets containing
0, the intersection of their pre-images is non-empty:
ϕ−1(I)∩ ψ−1(J)⁄= / 0.
Yet, p⁄= q! There is no really satisfactory way of drawing M (our picture above is
inadequate), since it cannot be realized as a submanifold of any Rn.
Since such a behaviour is inconsistent with the idea of a manifold that ‘locally looks
like Rn’, we shall insist that for two distinct pointsp,q∈ M, there are always disjoint
coordinate charts containing the two points. This is called the Hausdorff condition,
after Felix Hausdorff (1868-1942). 3
3 http://en.wikipedia.org/wiki/Felix_Hausdorff

2.2 Deﬁnition of manifold 19
Deﬁnition 2.7. An m-dimensional manifold is a set M, together with a maximal
atlas A ={(Uα , ϕα )} with the following properties:
1. (Countability condition) M is covered by countably many coordinate charts in
A . That is, there are indices α1, α2, . . .with
M =
⋃
i
Uαi.
2. (Hausdorff condition) For any two distinct points p,q∈ M there are coordinate
charts (Uα , ϕα ) and (Uβ , ϕβ ) in A such that p∈ Uα, q∈ Uβ , with
Uα∩Uβ = / 0.
The charts (U, ϕ)∈ A are called (coordinate) charts on the manifold M.
Before giving examples, let us note the following useful fact concerning the Haus-
dorff condition:
Lemma 2.2. Let M be a set with a maximal atlas A ={(Uα , ϕα )}, and suppose
p,q∈ M are distinct points contained in a single coordinate chart (U, ϕ)∈ A .
Then we can ﬁnd indices α, β such that p∈ Uα, q∈ Uβ , with Uα∩Uβ = / 0.
Proof. We begin with the following remark, which we leave as an exercise. Suppose
(U, ϕ) is a chart, with image ~U = ϕ(U)⊆ Rm. Let V⊆ U be a subset such that
~V = ϕ(V )⊆~U is open, and let ψ = ϕ|V be the restriction of ϕ. Then (V, ψ) is again
a chart, and is compatible with (U, ϕ). If (U, ϕ) is a chart from an atlast A , then
(V, ψ) is compatible with that atlas.
Now let (U, ϕ) be as in the Lemma. Since
~p = ϕ(p), ~q = ϕ(q)
are distinct points in ~U⊆ Rm, we can choose disjoint open subsets ~Uα and ~Uβ⊆~U
containing~p = ϕ(p) and~q = ϕ(q), respectively.4 Let Uα , Uβ⊆ U be their preim-
ages, and take ϕα = ϕ|Uα , ϕβ = ϕ|Uβ . Then (Uα , ϕα ) and (Uβ , ϕβ ) are charts in A ,
4 For instance, take these subsets to be the elements in ~U of distance less than||~p−~q||/2 from ~p
and~q, respectively.

20 2 Manifolds
with disjoint chart domains, and by construction we have that p∈ Uα and q∈ Uβ .
⊓ ⊔
Example 2.7. Consider the 2-sphere S2 with the atlas given by the two coordinate
charts (U+, ϕ+) and (U−, ϕ−). This atlas extends uniquely to a maximal atlas. The
countability condition is satisﬁed, since S2 is already covered by two charts. The
Hausdorff condition is satisﬁed as well: Given distinct points p,q∈ S2, if both are
contained in U+ or both in U−, we can apply the Lemma. The only case to be
considered is thus if one point (say p) is the north pole and the other (say q) the
south pole. But here we can constructUα ,Uβ by replacing U+ and U− with the open
upper hemisphere and open lower hemisphere, respectively. Alternatively, we can
use the chart given by stereographic projection to the x− z plane, noting that this is
also in the maximal atlas.
Remark 2.2. As we explained above, the Hausdorff condition rules out some strange
examples that don’t quite ﬁt our idea of a space that is locally likeRn. Nevertheless,
the so-called non-Hausdorff manifolds (with non-Hausdorff more properly called
not necessarily Hausdorff ) do arise in some important applications. Much of the
theory can be developed without the Hausdorff property, but there are some com-
plications: For instance, the initial value problems for vector ﬁelds need not have
unique solutions, in general.
Remark 2.3 (Charts taking values in ‘abstract’ vector spaces). In the deﬁnition of
an m-dimensional manifold M , rather than letting the charts(Uα , ϕα ) take values in
Rm we could just as well let them take values in m-dimensional real vector spaces
Eα:
ϕα : Uα→ Eα .
Transition functions are deﬁned as before, except they now take an open subset of
Eβ to an open subset of Eα. The choice of basis identiﬁes Eα = Rm, and takes us
back to the original deﬁnition.
As far as the deﬁnition of manifolds is concerned, nothing has been gained by
adding this level of abstraction. However, it often happens that theEα’s are given to
us ‘naturally’. For example, ifM is a surface insideR3, one would typically usex−y
coordinates, or x− z coordinates, or y− z coordinates on appropriate chart domains.
It can then be useful to regard the x− y plane, x− z plane, and y− z plane as the
target space of the coordinate maps, and for notational reasons it may be convenient
to not associate them with a single R2.
2.3 Examples of Manifolds
We will now discuss some basic examples of manifolds. In each case, the manifold
structure is given by a ﬁnite atlas; hence the countability property is immediate. We
will not spend too much time on verifying the Hausdorff property; while it may be
done ‘by hand’, we will later have some better ways of doing this.

2.3 Examples of Manifolds 21
2.3.1 Spheres
The construction of an atlas for the 2-sphere S2, by stereographic projection, also
works for the n-sphere
Sn ={(x0, . . . ,xn)| (x0)2 + . . .+ (xn)2 = 1}.
Let U± be the subsets obtained by removing(∓1,0, . . . ,0). Stereographic projection
deﬁnes bijections ϕ± : U±→ Rn, where ϕ±(x0, x1, . . . ,xn) = (u1, . . . ,un) with
ui = xi
1± x0 .
For the transition function one ﬁnds (writing u = (u1, . . . ,un))
(ϕ−◦ ϕ−1
+ )(u) = u
||u||2 .
We leave it as an exercise to check the details. An equivalent atlas, with 2 n + 2
charts, is given by the subsets U +
0 , . . . ,U +
n ,U−
0 , . . . ,U−
n where
U +
j ={x∈ Sn| x j > 0}, U−
j ={x∈ Sn| x j < 0}
for j = 0, . . . ,n, with ϕ±
j : U±
j → Rn the projection to the j-th coordinate plane (in
other words, omitting the j-th component x j):
ϕ±
j (x0, . . . ,xn) = (x0, . . . ,xi−1,xi+1, . . . ,xn).
2.3.2 Products
Given manifoldsM,M′ of dimensions m,m′, with atlases{(Uα , ϕα )} and{(U′
β , ϕ′
β )},
the cartesian product M× M′ is a manifold of dimension m + m′. An atlas is
given by the product charts Uα× U′
β with the product maps ϕα× ϕ′
β : (x,x′)↦→
(ϕα (x), ϕ′
β (x′)). For example, the 2-torus T 2 = S1× S1 becomes a manifold in this
way, and likewise for the n-torus
T n = S1×···× S1.

22 2 Manifolds
2.3.3 Real projective spaces
The n-dimensional projective space RPn, also denoted RPn, is the set of all lines
l⊆ Rn+1. It may also be regarded as a quotient space5
RPn = (Rn+1\{0})/∼
for the equivalence relation
x∼ x′⇔∃ λ∈ R\{0} : x′ = λx.
Indeed, any x∈ Rn+1\{0} determines a line, and two pointsx,x′ determine the same
line if and only if they agree up to a non-zero scalar multiple. The equivalence class
of x = (x0, . . . ,xn) under this relation is commonly denoted
[x] = (x0 : . . .: xn).
RPn has a standard atlas
A ={(U0, ϕ0), . . . ,(Un, ϕn)}
deﬁned as follows. For j = 0, . . . ,n, let
Uj ={(x0 : . . .: xn)∈ RPn| x j⁄= 0}
be the set for which the j-th coordinate is non-zero, and put
ϕ j : Uj→ Rn, (x0 : . . .: xn)↦→ (x0
x j , . . . ,x j−1
x j , x j+1
x j , . . . ,xn
x j ).
This is well-deﬁned, since the quotients do not change when all xi are multiplied
by a ﬁxed scalar. Put differently, given an element [x]∈ RPn for which the j-th
component x j is non-zero, we ﬁrst rescale the representative x to make the j-th
component equal to 1, and then use the remaining components as our coordinates.
As a random example (with n = 2),
ϕ1(7 : 3 : 2) = ϕ1
(7
3 : 1 : 2
3
)
=
(7
3 , 2
3
)
.
From this description, it is immediate that ϕ j is a bijection from Uj onto Rn, with
inverse map
ϕ−1
j (u1, . . . ,un) = (u1 : . . .: u j : 1 : u j+1 : . . .: un).
Geometrically, viewing RPn as the set of lines in Rn+1, the subset Uj⊆ RPn
consists of those lines l which intersect the afﬁne hyperplane
5 See the appendix to this chapter for some background on quotient spaces.

2.3 Examples of Manifolds 23
Hj ={x∈ Rn+1| x j = 1},
and the map ϕ j takes such a line l to its unique point of intersection l∩ Hj, followed
by the identiﬁcation Hj∼= Rn (dropping the coordinate x j = 1).
Let us verify that A is indeed an atlas. Clearly, the domainsUj cover RPn, since
any element [x]∈ RPn has at least one of its components non-zero. For i⁄= j, the
intersection Ui∩Uj consists of elements x with the property that both components
xi, x j are non-zero. There are two cases:
Case 1: 0≤ i < j≤ n. We have
ϕi◦ ϕ−1
j (u1, . . . ,un) = ( u1
ui+1 , . . . , ui
ui+1 , ui+2
ui+1 , . . . , u j
ui+1 , 1
ui+1 , u j+1
ui+1 , . . . , un
ui+1 ),
deﬁned on ϕ j(Ui∩Uj) ={u∈ Rn| ui+1⁄= 0}.
Case 2: If 0≤ j < i≤ n. We have 6
ϕi◦ ϕ−1
j (u1, . . . ,un) = ( u1
ui , . . . ,u j
ui , 1
ui , u j+1
ui , . . . ,ui−1
ui , ui+1
ui , . . . ,un
ui ),
deﬁned on ϕ j(Ui∩Uj) ={u∈ Rn| ui⁄= 0}.
In both cases, we see thatϕi◦ ϕ−1
j is smooth. To complete the proof that this atlas
(or the unique maximal atlas containing it) deﬁnes a manifold structure, it remains
to check the Hausdorff property.
This can be done with the help of Lemma 2.2, but we postpone the proof since
we will soon have a simple argument in terms of smooth functions. See Proposition
3.1 below.
Remark 2.4. In low dimensions, we have that RP0 is just a point, while RP1 is a
circle.
Remark 2.5. Geometrically,Ui consists of all lines inRn+1 meeting the afﬁne hyper-
plane Hi, hence its complement consists of all lines that are parallel to Hi, i.e., the
lines in the coordinate subspace deﬁned by xi = 0. The set of such lines is RPn−1.
In other words, the complement of Ui in RPn is identiﬁed with RPn−1.
Thus, as sets, RPn is a disjoint union
RPn = Rn⊔ RPn−1,
where Rn is identiﬁed (by the coordinate map ϕi) with the open subset Un, and
RPn−1 with its complement. Inductively, we obtain a decomposition
RPn = Rn⊔ Rn−1⊔···⊔ R⊔ R0,
where R0 ={0}. At this stage, it is simply a decomposition into subsets; later it will
be recognized as a decomposition into submanifolds.
6 If i = n, the last entry in the following expression is un−1/un.

24 2 Manifolds
Exercise: Find an identiﬁcation of the space of rotations inR3 with the 3-dimensional
projective space RP3. Hint: Associate to any v∈ R3 a rotation, as follows: If v = 0,
take the trivial rotation, if v⁄= 0, take the rotation by an angle ||v|| around the ori-
ented axis determined by v. Note that for||v|| = π, the vectors v and−v determine
the same rotation.
2.3.4 Complex projective spaces
Similar to the real projective space, one can deﬁne a complex projective space CPn
as the set of complex 1-dimensional subspaces ofCn+1. We identifyC with R2, thus
Cn+1 with R2n+2. Thus
CPn = (Cn+1\{0})/∼
where the equivalence relation is z∼ z′ if and only if there exists a complex λ with
z′ = λz. (Note that the scalarλ is then unique, and is non-zero.) Alternatively, letting
S2n+1⊆ Cn+1 = R2n+2 be the ‘unit sphere’ consisting of complex vectors of length
||z|| = 1, we have
CPn = S2n+1/∼,
where z′∼ z if and only if there exists a complex number λ with z′ = λz. (Note that
the scalar λ is then unique, and has absolute value 1.) One deﬁnes charts (Uj, ϕ j)
similar to those for the real projective space:
Uj ={(z0 : . . .: zn)| z j⁄= 0}, ϕ j : Uj→ Cn = R2n,
ϕ j(z0 : . . .: zn) =
(z0
z j , . . . ,z j−1
z j , z j+1
z j , . . . ,zn
z j
)
.
The transition maps between charts are given by similar formulas as forRPn (just re-
place x with z); they are smooth maps between open subsets ofCn = R2n. Thus CPn
is a smooth manifold of dimension 2n. 7 Similar to RPn there is a decomposition
CPn = Cn⊔ Cn−1⊔···⊔ C⊔ C0.
2.3.5 Grassmannians
The set Gr(k,n) of all k-dimensional subspaces of Rn is called the Grassmannian of
k-planes in Rn. (Named after Hermann Grassmann (1809-1877).) 8
7 The transition maps are not only smooth but even holomorphic, making CPn into an example of
a complex manifold (of complex dimension n).
8 http://en.wikipedia.org/wiki/Hermann_Grassmann

2.3 Examples of Manifolds 25
As a special case, Gr(1,n) = RPn−1.
We will show that for general k, the Grassmannian is a manifold of dimension
dim(Gr(k,n)) = k(n− k).
An atlas for Gr (k,n) may be constructed as follows. The idea is to present linear
subspaces of dimension k as graphs of linear maps from Rk to Rn−k. Here Rk is
viewed as the coordinate subspace corresponding to a choice of k components from
x = (x1, . . . ,xn)∈ Rn, and Rn−k the coordinate subspace for the remaining coordi-
nates. To make it precise, we introduce some notation. For any subsetI⊆{ 1, . . . ,n}
of the set of indices, let
I′ ={1, . . . ,n}\I
be its complement. Let RI⊆ Rn be the coordinate subspace
RI ={x∈ Rn| xi = 0 for all i∈ I′}.
If I has cardinality|I| = k, then RI∈ Gr(k,n). Note that RI′
= (RI)⊥. Let
UI ={E∈ Gr(k,n)|E∩ RI′
={0}} .
Each E∈ UI is described as the graph of a unique linear map AI : RI→ RI′
,
that is,
E ={y + AI(y)|y∈ RI}.
This gives a bijection

26 2 Manifolds
ϕI : UI→ L(RI, RI′
), E↦→ ϕI(E) = AI,
where L(F,F′) denotes the space of linear maps from a vector space F to a vector
space F′. Note L(RI, RI′
)∼= Rk(n−k), because the bases of RI and RI′
identify the
space of linear maps with(n−k)×k-matrices, which in turn is justRk(n−k) by listing
the matrix entries. In terms of AI, the subspace E∈ UI is the range of the injective
linear map (
1
AI
)
: RI→ RI⊕ RI′∼= Rn (2.2)
where we write elements of Rn as column vectors.
To check that the charts are compatible, suppose E∈ UI∩UJ, and let AI and AJ
be the linear maps describing E in the two charts. We have to show that the map
ϕJ◦ ϕ−1
I : L(RI, RI′
)→ L(RJ, RJ′
), AI = ϕI(E)↦→ AJ = ϕJ(E)
is smooth. By assumption, E is described as the range of (2.2) and also as the range
of a similar map for J. Here we are using the identiﬁcations RI⊕ RI′∼= Rn and
RJ⊕ RJ′∼= Rn. It is convenient to describe everything in terms of RJ⊕ RJ′
. Let
(
a b
c d
)
: RI⊕ RI′
→ RJ⊕ RJ′
be the matrix corresponding to the identiﬁcation RI⊕ RI′
→ Rn followed by the
inverse of RJ⊕ RJ′
→ Rn. For example, c is the inclusion RI→ Rn as the corre-
sponding coordinate subspace, followed by projection to the coordinate subspace
RJ′
. 9 We then get the condition that the injective linear maps
(
a b
c d
)(
1
AI
)
: RI→ RJ⊕ RJ′
,
(
1
AJ
)
: RJ→ RJ⊕ RJ′
have the same range. In other words, there is an isomorphismS : RI→ RJ such that
(
a b
c d
)(
1
AI
)
=
(
1
AJ
)
S
as maps RI→ RJ⊕ RJ′
. We obtain
(
a + bAI
c + dAI
)
=
(
S
AJS
)
Using the ﬁrst row of this equation to eliminate the second row of this equation, we
obtain the formula
AJ = (c + dAI) (a + bAI)−1.
9 Put differently, the matrix is the permutation matrix ‘renumbering’ the coordinates ofRn.

2.3 Examples of Manifolds 27
The dependence of the right hand side on the matrix entries of AI is smooth, by
Cramer’s formula for the inverse matrix. It follows that the collection of all ϕI :
UI→ Rk(n−k) deﬁnes on Gr(k,n) the structure of a manifold of dimension k(n− k).
The number of charts of this atlas equals the number of subsetsI⊆{ 1, . . . ,n} of car-
dinality k, that is, it is equal to
(n
k
)
. (The Hausdorff property may be checked similar
to that for RPn. Alternatively, given distinct E1,E2∈ Gr(k,n), choose a subspace
F∈ Gr(k,n) such that F⊥ has zero intersection with both E1,E2. (Such a subspace
always exists.) One can then deﬁne a chart(U, ϕ), where U is the set of subspacesE
transverse to F⊥, and ϕ realizes any such map as the graph of a linear mapF→ F⊥.
Thus ϕ : U→ L(F,F⊥). As above, we can check that this is compatible with all the
charts (UI, ϕI). Since both E1,E2 are in this chart U, we are done by Lemma 2.2.)
Remark 2.6. As already mentioned, Gr(1,n) = RPn−1. One can check that our sys-
tem of charts in this case is the standard atlas for RPn−1.
Exercise: This is a preparation for the following remark. Recall that a linear map
Π : Rn→ Rn is an orthogonal projection onto some subspace E⊆ Rn if Π (x) = x
for x∈ E and Π (x) = 0 for x∈ E⊥. Show that a square matrix P∈ MatR(n) is the
matrix of an orthogonal projection if and only if it has the properties
P⊤ = P, PP = P,
where the superscript⊤ indicates ‘transpose’. What is the matrix of the orthogonal
projection onto E⊥?
Remark 2.7. For any k-dimensional subspace E⊆ Rn, let Π E : Rn→ Rn be the lin-
ear map given by orthogonal projection onto E, and let PE∈ MatR(n) be its matrix.
By the exercise,
P⊤
E = PE , PEPE = PE ,
Conversely, any square matrixP with the propertiesP⊤ = P, PP = P with rank(P) =
k is the orthogonal projection onto a subspace{Px| x∈ Rn}⊆ Rn. This identiﬁes the
Grassmannian Gr(k,n) with the set of orthogonal projections of rankk. In summary,
we have an inclusion
Gr(k,n) ↪→ MatR(n)∼= Rn2
, E↦→ PE .
By construction, this inclusion take values in the subspace SymR(n)∼= Rn(n+1)/2 of
symmetric n× n-matrices.
Remark 2.8. For all k, there is an identiﬁcation Gr (k,n)∼= Gr(n− k,n) (taking a
k-dimensional subspace to the orthogonal subspace).
Remark 2.9. Similar to RP2 = S2/∼, the quotient modulo antipodal identiﬁcation,
one can also consider
M = (S2× S2)/∼

28 2 Manifolds
the quotient space by the equivalence relation
(x,x′)∼ (−x,−x′).
It turns out that this manifold M is the same as Gr(2,4), where ‘the same’ is meant
in the sense that there is a bijection of sets identifying the atlases.
2.3.6 Complex Grassmannians
Similar to the case of projective spaces, one can also consider the complex Grass-
mannian GrC(k,n) of complex k-dimensional subspaces of Cn. It is a manifold of
dimension 2k(n−k), which can also be regarded as a complex manifold of complex
dimension k(n− k).
2.4 Oriented manifolds
The compatibility condition between charts (U, ϕ) and (V, ψ) on a set M is that the
map ψ◦ ϕ−1 : ϕ(U∩V )→ ψ(U∩V ) is a diffeomorphism. In particular, the Jaco-
bian matrix D(ψ◦ ϕ−1) of the transition map is invertible, and hence has non-zero
determinant. If the determinant is > 0 everywhere, then we say (U, ϕ), (V, ψ) are
oriented-compatible. An oriented atlas on M is an atlas such that any two of its
charts are oriented-compatible; a maximal oriented atlas is one that contains every
chart that is oriented-compatible with all charts in this atlas. An oriented manifold
is a set with a maximal oriented atlas, satisfying the Hausdorff and countability con-
ditions as in deﬁnition 2.7. A manifold is called orientable if it admits an oriented
atlas.
The notion of an orientation on a manifold will become crucial later, since inte-
gration of differential forms over manifolds is only deﬁned if the manifold is ori-
ented.
Example 2.8. The spheres Sn are orientable. To see this, consider the atlas with
the two charts (U+, ϕ+) and (U−, ϕ−), given by stereographic projections. (Sec-
tion 2.3.1.) Here ϕ−(U+∩ U−) = ϕ+(U+∩ U−) = Rn\{0}, with transition map
ϕ−◦ ϕ−1
+ (u) = u/||u||2. The Jacobian matrix D(ϕ−◦ ϕ−1
+ )(u) has entries
(
D(ϕ−◦ ϕ−1
+ )(u)
)
i j
= ∂
∂u j
( ui
||u||2
)
= 1
||u||2 δi j− 2uiu j
||u||4 . (2.3)

2.5 Open subsets 29
Its determinant is−||u||−2n (see exercise below).10 Hence, the given atlas is not an
oriented atlas. But this is easily remedied: Simply compose one of the charts, say
U−, with the map (u1,u2, . . . ,un)↦→ (−u1,u2, . . . ,un); then with the resulting new
coordinate map~ϕ− the atlas (U+, ϕ+), (U−,~ϕ−) will be an oriented atlas.
Exercise: Calculate the determinant of the matrix with entries (2.3). Hint: Check
that u is an eigenvector of the matrix, as is any vector orthogonal tou. Alternatively,
use that the Jacobian determinant must be invariant under rotations in u-space.
Example 2.9. One can show that RPn is orientable if and only if n is odd or n = 0.
More generally, Gr(k,n) is orientable if and only if n is even or n = 1. The complex
projective spaces CPn and complex Grassmannians GrC(k,n) are all orientable. This
follows because the transition maps for their standard charts, as maps between open
subsets of Cm, are actually complex-holomorphic, and this implies that as real maps,
their Jacobian has positive determinant. See the following exercise.
Exercise: Let A∈ MatC(n) be a complexn×n-matrix, and AR∈ MatR(2n) the same
matrix regarded as a real-linear transformation of R2n∼= Cn. Show that
detR(AR) =|detC(A)|2.
You may want to start with the casen = 1, and next consider the case thatA is upper
triangular.
2.5 Open subsets
Let M be a set equipped with an m-dimensional maximal atlas A ={(Uα , ϕα )}.
Deﬁnition 2.8. A subset U⊆ M is open if and only if for all charts (Uα , ϕα )∈ A
the set ϕα (U∩Uα ) is open.
To check that a subsetU is open, it is not actually necessary to verify this condition
for all charts. As the following proposition shows, it is enough to check for any col-
lection of charts whose union containsU. In particular, we may takeA in deﬁnition
2.8 to be any atlas, not necessarily a maximal atlas.
Proposition 2.1. Given U⊆ M, let B⊆ A be any collection of charts whose union
contains U. Then U is open if and only if for all charts (Uβ , ϕβ ) from B, the sets
ϕβ (U∩Uβ ) are open.
10 Actually, to decide the sign of the determinant, one does not have to compute the determinant
everywhere. If n > 1, since Rn\{0}, it sufﬁces to compute the determinant at just one point, e.g.
u = (1,0, . . . ,0).

30 2 Manifolds
Proof. In what follows, we reserve the index β to indicate charts (Uβ , ϕβ ) from B.
Suppose ϕβ (U∩Uβ ) is open for all such β. Let (Uα , ϕα ) be a given chart in the
maximal atlas A . We have that
ϕα (U∩Uα ) =
⋃
β
ϕα (U∩Uα∩Uβ )
=
⋃
β
(ϕα◦ ϕ−1
β )
(
ϕβ (U∩Uα∩Uβ )
)
=
⋃
β
(ϕα◦ ϕ−1
β )
(
ϕβ (Uα∩Uβ )∩ ϕβ (U∩Uβ )
)
.
Since B⊆ A , all ϕβ (Uα∩Uβ ) are open. Hence the intersection with ϕβ (U∩Uβ )
is open, and so is the pre-image under the diffeomorphismϕα◦ ϕ−1
β . Finally, we use
that a union of open sets is again open. This proves the ‘if’ part; the ‘only if’ part is
obvious. ⊓ ⊔
If A is an atlas on M, and U⊆ M is open, then U inherits an atlas by restriction:
AU ={(U∩Uα , ϕα|U∩Uα )}.
Exercise: Verify that if A is a maximal atlas, then so is AU, and if this maximal
atlas A satisﬁes the countability and Hausdorff properties, then so does AU.
This then proves:
Proposition 2.2. An open subset of a manifold is again a manifold.
The collection of open sets of M with respect to an atlas has properties similar to
those for Rn:
Proposition 2.3. Let M be a set with an m-dimensional maximal atlas. The collec-
tion of all open subsets of M has the following properties:
• / 0,M are open.
• The intersection U∩U′ of any two open sets U,U′ is again open.
• The union⋃
iUi of an arbitrary collection Ui, i∈ I of open sets is again open.
Proof. All of these properties follow from similar properties of open subsets inRm.
For instance, if U,U′ are open, then
ϕα ((U∩U′)∩Uα ) = ϕα (U∩Uα )∩ ϕα (U′∩Uα )
is an intersection of open subsets of Rm, hence it is open and therefore U∩U′ is
open. ⊓ ⊔
These properties mean, by deﬁnition, that the collection of open subsets ofM deﬁne
a topology on M. This allows us to adopt various notions from topology:

2.6 Compact subsets 31
1. A subset A⊆ M is called closed if its complement M\A is open.
2. M is called connected if the only subsets A⊆ M that are both closed and open
are A = / 0 andA = M.
3. If U is an open subset and p∈ U, then U is called an open neighborhood of p .
More generally, if A⊆ U is a subset contained in M, then U is called an open
neighborhood of A.
The Hausdorff condition in the deﬁnition of manifolds can now be restated as the
condition that any two distinct points p ,q in M have disjoint open neighborhoods .
(It is not necessary to take them to be domains of coordinate charts.)
It is immediate from the deﬁnition that domains of coordinate charts are open.
Indeed, this gives an alternative way of deﬁning the open sets:
Exercise: Let M be a set with a maximal atlas. Show that a subsetU⊆ M is open if
and only if it is either empty, or is a union U =⋃
i∈I Ui where the Ui are domains of
coordinate charts.
2.6 Compact subsets
Another important concept from topology that we will need is the notion of com-
pactness. Recall (e.g. Munkres, Chapter 1 § 4) that a subset A⊆ Rm is compact if it
has the following property: For every collection{Uα} of open subsets of Rm whose
union contains A, the set A is already covered by ﬁnitely many subsets from that
collection. One then proves the important result (see Munkres, Theorems 4.2 and
4.9)
Theorem 2.2 (Heine-Borel). A subset A⊆ Rm is compact if and only if it is closed
and bounded.
While ‘closed and bounded’ is a simpler characterization of compactness to work
with, it does not directly generalize to manifolds (or other topological spaces), while
the original deﬁnition does:
Deﬁnition 2.9. Let M be a manifold. 11 A subset A⊆ M is compact if it has the
following property: For every collection {Uα} of open subsets of M whose union
contains A, the setA is already covered by ﬁnitely many subsets from that collection.
In short, A⊆ M is compact if every open cover admits a ﬁnite subcover.
Proposition 2.4. If A⊆ M is contained in the domain of a coordinate chart (U, ϕ),
then A is compact in M if and only if ϕ(A) is compact in Rn.
Proof. Suppose ϕ(A) is compact. Let{Uα} be an open cover of A. Taking intersec-
tions with U, it is still an open cover (since A⊆ U). Hence
11 More generally, the same deﬁnition is used for arbitrary topological spaces – e.g., sets with an
atlas.

32 2 Manifolds
A⊆
⋃
α
(U∩Uα ),
and therefore
ϕ(A)⊆
⋃
α
ϕ(U∩Uα ).
Since ϕ(A) is compact, there are indices α1, . . . ,αN such that
ϕ(A)⊆ ϕ(U∩Uα1)∪ . . .∪ ϕ(U∩UαN ).
But then
A⊆ (U∩Uα1)∪ . . .∪ (U∩UαN )⊆ Uα1∪ . . .∪UαN .
The converse is proved similarly. ⊓ ⊔
Exercise: Complete the proof, by working out the details for the other direction.
The proposition is useful, since we can check compactness of ϕ(A) by using the
Heine-Borel criterion. For more general subsets ofM, we can often decide compact-
ness by combining this result with the following:
Proposition 2.5. If A 1, . . . ,Ak⊆ M is a ﬁnite collection of compact subsets, then
their union A = A1∪ . . .∪ Ak is again compact.
Proof. If{Uα} is an open cover of A, then in particular it is an open cover of each
of the sets A1, . . . ,Ak. For each Ai, we can choose a ﬁnite subcover. The collection
of all Uα’s such that appear in at least one of these subcovers, fori = 1, . . .k are then
a ﬁnite subcover for A.
Example 2.10. Let M = Sn. The closed upper hemisphere{x∈ Sn| x0≥ 0} is com-
pact, because is contained in the coordinate chart(U+, ϕ+) for stereographic projec-
tion, and its image under ϕ+ is the closed and bounded subset{u∈ Rn||| u||≤ 1}.
Likewise the closed lower hemisphere is compact, and hence Sn itself (as the union
of upper and lower hemispheres) is compact.
Example 2.11. Let{(Ui, ϕi)| i = 0, . . . ,n} be the standard atlas for RPn. Let
Ai ={(x0 : . . .: xn)∈ RPn||| x||2≤ (n + 1)x2
i}.
Then Ai⊆ Ui (since necessarily xi⁄= 0 for elements of Ai). Furthermore,⋃n
i=0 Ai =
RPn: Indeed, given any (x0 :··· : xn)∈ RPn, let i be an index for which|xi| is maxi-
mal. Then||x||2≤ (n +1)x2
i (since the right hand side is obtained from the left hand
side by replacing each (x j)2 with (xi)2≥ (x j)2)), hence (x0 :··· : xn)∈ Ai. Finally,
one checks that ϕi(Ai)⊆ Rn is a closed ball of radius √n + 1, and in particular is
compact.
In a similar way, one can prove compactness of CPn, Gr(k,n), GrC(k,n). How-
ever, soon we will have a simpler way of verifying compactness, by showing that
they are closed and bounded subsets of RN for a suitable N.

2.7 Appendix 33
Proposition 2.6. Let M be a set with a maximal atlas. If A ⊆ M is compact, and
C⊆ M is closed, then A∩C is compact.
Proof. Let{Uα} be an open cover of A∩C. Together with the open subset M\C,
these cover A. Since A is compact, there are ﬁnitely many indices α1, . . . ,αN with
A⊆ (M\C)∪Uα1∪ . . .∪UαN .
Hence A∩C⊆ Uα1∪ . . .∪UαN . ⊓ ⊔
The following fact uses the Hausdorff property (and holds in fact for any Haus-
dorff topological space).
Proposition 2.7. If M is a manifold, then every compact subset A⊆ M is closed.
Proof. Suppose A⊆ M is compact. Let p∈ M\A be given. For any q∈ A, there
are disjoint open neighborhoods Vq of q and Uq of p. The collection of all Vq for
q∈ A are an open cover of A, hence there exists a ﬁnite subcover Vq1, . . . ,Vqk. The
intersection U = Uq1∩ . . .∩Uqk is an open subset of M with p∈ M and not meeting
Vq1∪ . . .∪Vqk, hence not meeting A. We have thus shown that every p∈ M\A has
an open neighborhood U⊆ M\A. The union over all such open neighborhoods for
all p∈ M\A is all of M\A, which hence is open. It follows that A is closed. ⊓ ⊔
Exercise: Let M be the non-Hausdorff manifold from Example 2.6. Find a compact
subset A⊆ M that is not closed.
2.7 Appendix
2.7.1 Countability
A set X is countable if it is either ﬁnite (possibly empty), or there exists a bijective
map f : N→ X. We list some basic facts about countable sets:
• N, Z, Q are countable, R is not countable.
• If X1,X2 are countable, then the cartesian product X1× X2 is countable.
• If X is countable, then any subset of X is countable.
• If X is countable, and f : X→ Y is surjective, then Y is countable.
• If (Xi)i∈I are countable sets, indexed by a countable setI, then the (disjoint) union
⊔i∈IXi is countable.
2.7.2 Equivalence relations
We will make extensive use ofequivalence relations; hence it may be good to review
this brieﬂy. A relation from a set X to a set Y is simply a subset

34 2 Manifolds
R⊆ Y× X.
We write x∼R y if and only if (y,x)∈ R. When R is understood, we write x∼ y. If
Y = X we speak of a relation on X.
Example 2.12. Any map f : X→ Y deﬁnes a relation, given by its graph Gr f =
{( f (x),x)|x∈ X}. In this sense relations are generalizations of maps; for example,
they are often used to describe ‘multi-valued’ maps.
Remark 2.10. Given another relation S⊆ Z×Y , one deﬁnes a composition S◦ R⊆
Z× X, where
S◦ R ={(z,x)|∃ y∈ Y : (z,y)∈ S, (y,x)∈ R}.
Our conventions are set up in such a way that if f : X→ Y and g : Y→ Z are two
maps, then Grg◦ f = Grg◦ Gr f .
Example 2.13. On the set X = R we have relations≥, >, <,≤, =. But there is also
the relation deﬁned by the condition x∼ x′⇔ x′− x∈ Z, and many others.
A relation∼ on a set X is called an equivalence relation if it has the following
properties,
1. Reﬂexivity: x∼ x for all x∈ X,
2. Symmetry: x∼ y⇒ y∼ x,
3. Transitivity: x∼ y, y∼ z⇒ x∼ z.
Given an equivalence relation, we deﬁne the equivalence class of x∈ X to be the
subset
[x] ={y∈ X| x∼ y}.
Note that X is a disjoint union of its equivalence classes. We denote by X/∼ the
set of equivalence classes. That is, all the elements of a given equivalence class are
lumped together and represent a single element of X/∼. One deﬁnes the quotient
map
q : X→ X/∼, x↦→ [x].
By deﬁnition, the quotient map is surjective.
Remark 2.11. There are two other useful ways to think of equivalence relations:
• An equivalence relation R on X amounts to a decomposition X =⊔i∈IXi as a
disjoint union of subsets. Given R, one takes Xi to be the equivalence classes;
given the decomposition, one deﬁnes R ={(y,x)∈ X× X|∃i∈ I : x,y∈ Xi}.
• An equivalence relation amounts to a surjective map q : X→ Y . Indeed, given
R one takes Y := X/∼ with q the quotient map; conversely, given q one deﬁnes
R ={(y,x)∈ X× X| q(x) = q(y)}.
Remark 2.12. Often, we will not write out the entire equivalence relation. For exam-
ple, if we say “the equivalence relation on S2 given by x∼− x”, then it is understood
that we also have x∼ x, since reﬂexivity holds for any equivalence relation. Sim-
ilarly, when we say “ the equivalence relation on R generated by x∼ x + 1”, it is

2.7 Appendix 35
understood that we also have x∼ x + 2 (by transitivity: x∼ x + 1∼ x + 2) as well as
x∼ x−1 (by symmetry), hence x∼ x +k for all k∈ Z. (Any relation R0⊆ X×X ex-
tends to a unique smallest equivalence relation R; one says that R is the equivalence
relation generated by R0.)
Example 2.14. Consider the equivalence relation on S2 given by
(x,y,z)∼ (−x,−y,−z).
The equivalence classes are pairs of antipodal points; they are in 1-1 correspondence
with lines in R3. That is, the quotient space S2/∼ is naturally identiﬁed with RP2.
Example 2.15. The quotient space R/∼ for the equivalence relation x∼ x + 1 on R
is naturally identiﬁed with S1. If we think of S1 as a subset of R, the quotient map
is given by t↦→ (cos(2πt),sin(2πt)).
Example 2.16. Similarly, the quotient space for the equivalence relation onR2 given
by (x,y)∼ (x + k,y + l) for k,l∈ Z is the 2-torus T 2.
Example 2.17. Let E be a k-dimensional real vector space. Given two ordered bases
(e1, . . . ,ek) and (e′
1, . . . ,e′
k), there is a unique invertible linear transformation A :
E→ E with A(ei) = e′
i. The two ordered bases are called equivalent if det(A) > 0.
One checks that equivalence of bases is an equivalence relation. There are exactly
two equivalence classes; the choice of an equivalence class is called an orientation
on E. For example, Rn has a standard orientation deﬁned by the standard basis
(e1, . . . ,en). The opposite orientation is deﬁned, for example, by (−e1,e2, . . . ,en).
A permutation of the standard basis vectors deﬁnes the standard orientation if and
only if the permutation is even.



Chapter 3
Smooth maps
3.1 Smooth functions on manifolds
A real-valued function on an open subset U⊆ Rn is called smooth if it is inﬁnitely
differentiable. The notion of smooth functions on open subsets of Euclidean spaces
carries over to manifolds: A function is smooth if its expression in local coordinates
is smooth.
Deﬁnition 3.1. A function f : M→ R on a manifold M is called smooth if for all
charts (U, ϕ) the function
f◦ ϕ−1 : ϕ(U)→ R
is smooth. The set of smooth functions on M is denoted C∞(M).
Remarks 3.1. 1. Since transition maps are diffeomorphisms, it sufﬁces to check the
condition for the charts from any given atlas A ={(Uα , ϕα )}, which need not
be the maximal atlas. Indeed, if the condition on f holds for all charts from the
atlas A , and if (U, ϕ) is another chart compatible with A , then the functions
f◦ ϕ−1⏐⏐
ϕ(U∩Uα ) = ( f◦ ϕ−1
α )◦ (ϕα◦ ϕ−1) : ϕ(U∩Uα )→ R
are smooth, and since the open sets ϕ(U∩Uα ) cover ϕ(U) this implies smooth-
ness of f◦ ϕ−1.
2. Given an open subset U⊆ M, we say that a function f is smooth on U if its
restriction f|U is smooth. (Here we are using that U itself is a manifold.) Given
p∈ M, we say that f is smooth at p if it is smooth on some open neighborhood
of p.
Example 3.1. The ‘height function’
f : S2→ R, (x,y,z)↦→ z
is smooth. In fact, we see that for any smooth functionh∈ C∞(R3) (for example the
coordinate functions), the restriction f = h|S2 is again smooth. This may be checked
37

38 3 Smooth maps
using the atlas with 6 charts given by projection to coordinate planes: E.g., in the
chart U ={(x,y,z)| z > 0} with ϕ(x,y,z) = (x,y), we have
( f◦ ϕ−1)(x,y) = h
(
x,y,
√
1− (x2 + y2)
)
which is smooth on ϕ(U) ={(x,y)| x2 +y2 < 1}. (The argument for the other charts
in this atlas is similar.)
Of course, if h is not smooth, it might still happen that its restriction to S2 is
smooth. On the other hand, the map f : S2→ R, (x,y,z)↦→
√
1− z2 is smooth only
on S2\{(0,0,1), (0,0,−1)}. To analyse the situation near the north pole, use the
coordinate chart (U, ϕ) as above. In these coordinates, z =
√
1− (x2 + y2), hence√
1− z2 =
√
x2 + y2 which is not smooth near (x,y) = (0,0).
Example 3.2. Let
π : Rn+1\{0}→ RPn
be the quotient map. Given f : RPn→ R, the function
ˆf = f◦ π : Rn+1\{0}→ R
satisﬁes ˆf (λx) = ˆf (x) for λ⁄= 0; conversely any ˆf with this property descends to
a function f on the projective space. We claim that f is smooth if and only if ˆf is
smooth. To see this, note that in the standard coordinate chart (Ui, ϕi) for RPn, the
function f◦ ϕ−1
i may be written as the smooth map
Ui→ Rn+1\{0}, (u1, . . . ,un)↦→ (u1, . . . ,ui,1,ui+1, . . . ,un)
followed by ˆf . Hence, if ˆf is smooth then so is f . (The converse is similar.) As a
special case, we see that for all 0≤ j≤ k≤ n the functions
f : RPn→ R, (x0 : . . .: xn)↦→ x jxk
||x||2 (3.1)
are well-deﬁned and smooth. By a similar argument, the functions
f : CPn→ C, (z0 : . . .: zn)↦→ z jzk
||z||2 (3.2)
(where the bar denotes complex conjugation) are well-deﬁned and smooth, in the
sense that both the real and imaginary part are smooth.
Lemma 3.1. Smooth functions f ∈ C∞(M) are continuous: For every open subset
J⊆ R, the pre-image f−1(J)⊆ M is open.
Proof. We have to show that for every(U, ϕ), the set ϕ(U∩ f−1(J))⊆ Rm is open.
But this subset coincides with the pre-image of J under the map f◦ ϕ−1 : ϕ(U)→
R, which is a smooth function on an open subset ofRm, and these are (by deﬁnition)
continuous.

3.1 Smooth functions on manifolds 39
Exercise Show that f : M→ R continuous (i.e., the pre-image of any open subset
J⊆ R under f is open) if and only if for all charts (U, ϕ) the function f◦ ϕ−1 is
continuous.
From the properties of smooth functions on Rm, one immediately gets the fol-
lowing properties of smooth functions on manifolds M:
• If f ,g∈ C∞(M) and λ , µ∈ R, then λ f + µg∈ C∞(M).
• If f ,g∈ C∞(M), then f g∈ C∞(M).
• 1∈ C∞(M) (where 1 denotes the constant function p↦→ 1).
These properties say that C∞(M) is an algebra with unit 1. (See the appendix to
this chapter for some background information on algebras.) Below, we will develop
many of the concepts of manifolds in terms of this algebra of smooth functions.
Suppose M is any set with a maximal atlas{(Uα , ϕα )}. The deﬁnition of C∞(M)
does not use the Hausdorff or countability conditions; hence it makes sense in this
more general context. We may use functions to check the Hausdorff property:
Proposition 3.1. Suppose M is any set with a maximal atlas, and p ⁄= q are two
points in M. Then the following are equivalent:
(i) There are open subsets U,V⊆ M with p∈ U, q∈ V, U∩V = / 0,
(ii) There exists f ∈ C∞(M) with f (p)⁄= f (q).
Proof. “(i)⇒ (ii)”. Suppose (i) holds. As explained in Section 2.5, we may take
U,V to be the domains of coordinate charts (U, ϕ) and (V, ψ) around p,q. Choose
ε > 0 such that the closed ε-ball
Bε (ϕ(p)) =
{
x∈ Rm⏐⏐||x− ϕ(p)||≤ ε
}
is contained in ϕ(U); let A⊆ U be its pre-image under ϕ. Let χ∈ C∞(Rm) be a
‘bump function’ centered atϕ(p), with χ(ϕ(p)) = 1 and χ(x) = 0 for||x− ϕ(p)||≥
ε. (For the existence of such a function see Munkres, Lemma 16.1, or Lemma A.2
in the appendix.)
The function f : M→ R such that f = χ◦ ϕ on U and f = 0 on M\A is smooth,
and satisﬁes f (p) = 1, f (q) = 0.
“(ii)⇐ (i)”. Suppose (ii) holds. Let δ =| f (q)− f (p)|/2, and put

40 3 Smooth maps
U ={x∈ M|| f (x)− f (p)| < δ}, (3.3)
V ={x∈ M|| f (x)− f (q)| < δ} (3.4)
By the Lemma 3.1, U,V are open, and clearly p∈ U, q∈ V , U∩V = / 0.
A direct consequence of this result is:
Corollary 3.1 (Criterion for Haudorff condition). A set M with an atlas satisﬁes
the Hausdorff condition if and only if for any two distinct points p ,q∈ M, there
exists a smooth function f ∈ C∞(M) with f (p)⁄= f (q). In particular, if there exists
a smooth injective map F : M→ RN, then M is Hausdorff.
Remark 3.2. One may replace ‘smooth’ with continuous in Proposition 3.1 and
Corollary 3.1.
Example 3.3 (Projective spaces). Write vectors x∈ Rn+1 as column vectors, hence
x⊤ is the corresponding row vector. The matrix product xx⊤ is a square matrix with
entries x jxk. The map
RPn→ MatR(n + 1), (x0 : . . .: xn)↦→ x x⊤
||x||2 (3.5)
is a smooth; indeed, its matrix components are the functions (3.1). For any given
(x0 : . . . : xn)∈ RPn, at least one of these components is non-zero. Identifying
MatR(n + 1)∼= RN, where N = (n + 1)2, this gives the desired smooth injective
map from projective space into RN; hence the criterion applies, and the Hausdorff
condition follows. For the complex projective space, one similarly has a smooth and
injective map
CPn→ MatC(n + 1), (z0 : . . .: zn)↦→ z z†
||x||2 (3.6)
(where z† = z⊤ is the conjugate transpose of the complex column vector z) into
MatC(n + 1) = RN with N = 2(n + 1)2.
Exercise: Verify that the map
Gr(k,n)→ MatR(n), E↦→ PE , (3.7)
taking a subspace E to the matrix of the orthogonal projection onto E, is smooth
and injective, hence Gr (k,n) is Hausdorff. Discuss a similar map for the complex
Grassmannian GrC(k,n).
In the opposite direction, the criterion tells us that for a setM with an atlas, if the
Hausdorff condition does not hold then no smooth injective map into RN exists.
Example 3.4. Consider the non-Hausdorff manifold M from Example 2.6. Here,
there are two points p,q that do not admit disjoint open neighborhoods. We see
directly that any smooth function on M must take on the same values at p and q:
With the coordinate charts (U, ϕ), (V, ψ) in that example,

3.2 Smooth maps between manifolds 41
f (p) = f (ϕ−1(0)) = lim
t→0−
f (ϕ−1(t)) = lim
t→0−
f (ψ−1(t)) = f (ψ−1(0)) = f (q),
since ϕ−1(t) = ψ−1(t) for t < 0.
3.2 Smooth maps between manifolds
The notion of smooth maps from M to R generalizes to smooth maps between man-
ifolds.
Deﬁnition 3.2. A map F : M→ N between manifolds is smooth at p∈ M if there
are coordinate charts (U, ϕ) around p and (V, ψ) around F(p) such that F(U)⊆ V
and such that the composition
ψ◦ F◦ ϕ−1 : ϕ(U)→ ψ(V )
is smooth. The function F is called a smooth map from M to N if it is smooth at all
p∈ M.
Remarks 3.3. 1. 1. The condition for smoothness atp does not depend on the choice
of charts: Given a different choice of charts (U′, ϕ′) and (V′, ψ′) with F(U′)⊆
V′, we have
ψ′◦ F◦ (ϕ′)−1 = (ψ′◦ ψ−1)◦ (ψ◦ F◦ (ϕ)−1)◦ (ϕ◦ (ϕ′)−1)
on ϕ′(U∩U′).
2. To check smoothness of F, it sufﬁces to take any atlas{(Uα , ϕα )} of M with
the property that F(Uα )⊆ Vα for some chart (Vα , ψα ) of N, and then check
smoothness of the maps

42 3 Smooth maps
ψα◦ F◦ ϕ−1
α : ϕα (Uα )→ ψα (Vα ).
3. Smooth maps M→ R are the same thing as smooth functions on M:
C∞(M, R) = C∞(M).
Smooth functions γ : J→ M from an open interval J⊆ R to M are called
(smooth) curves in M . Note that the image of a smooth curve need not look
smooth. For instance, the image of γ : R→ R2, t↦→ (t2,t3) has a ‘cusp singular-
ity’ at(0,0).
Example 3.5. a) Consider the map F : RP1→ RP1 given by
(t : 1)↦→ (et2
: 1) for t∈ R, (1 : 0)↦→ (1 : 0).
In the chart U1, we have F(U1)⊆ U1, and ϕ1◦ F◦ ϕ−1
1 (t) = et2
, which is smooth.
It remains to check smoothness at the point p = (1 : 0). Since F(p) = p, we will
verify this using the chart U0 around p. We have, for u⁄= 0
F(ϕ−1
0 (u)) = F(1 : u) = F(1
u : 1) = (e
1
u2 : 1) = (1 : e− 1
u2 ),
Hence ϕ0◦ F◦ ϕ−1
0 is the map
u↦→ e− 1
u2 for u⁄= 0, 0↦→ 0.
As is well-known, this map is smooth even at u = 0.
b) The same calculation applies for the map F : CP1→ CP1, given by the same
formulas. However, the conclusion is different: The map
z↦→ e− 1
z2 for u⁄= 0, 0↦→ 0.
is not smooth (or even continuous) at z = 0. (For a non-zero complex number a,
consider the limit of this function for z = sa as s→ 0. If a = 1, the limit is 0. If

3.2 Smooth maps between manifolds 43
z = 1 + i, the absolute value is always one, and the limit doesn’t exist. If a = i, the
limit is ∞.)
Proposition 3.2. Suppose F1 : M1→ M2 and F2 : M2→ M3 are smooth maps. Then
the composition
F2◦ F1 : M1→ M3
is smooth.
Proof. Given p∈ M1, choose charts (U1, ϕ1) around p, (U2, ϕ2) around F1(p), and
(U3, ϕ3) around F2(F1(p)), with F2(U2)⊆ U3 and F1(U1)⊆ U2. (This is always
possible – see exercise below.) Then F2(F1(U2))⊆ U3, and we have:
ϕ3◦ (F2◦ F1)◦ ϕ−1
1 = (ϕ3◦ F2◦ ϕ−1
2 )◦ (ϕ2◦ F1◦ ϕ−1
1 ),
a composition of smooth maps between open subsets of Euclidean spaces. ⊓ ⊔
Exercise: Suppose F∈ C∞(M,N).
1. Let (U, ϕ) be a coordinate chart for M and (V, ψ) a coordinate chart for N, with
F(U)⊆ V . Show that for all open subsets W⊆ N the set U∩ F−1(W ) is open.
Hint: Show that ϕ(U∩ F−1(W )) is the pre-image of the open set ψ(V∩ W )
under the smooth map ψ◦ F◦ ϕ−1 : ϕ(U)→ ψ(V ).
2. Show that F is continuous: For every open W⊆ N the pre-image F−1(W ) is
open.
3. Given p∈ M and any chart (V, ψ) around F(p), show that there exists a chart
(U, ϕ) around p such that F(U)⊆ V .
Hint: Start with any open chart (U1, ϕ1) around p, and replace U1 with U =
U1∩ F−1(V ).
Exercise: Using the previous exercise, show that smooth maps F∈ C∞(M,N) are
continuous: The pre-images of every open subsets of N is open in M.
3.2.1 Diffeomorphisms of manifolds
Deﬁnition 3.3. A smooth map F : M→ N is called a diffeomorphism if it is invert-
ible, with a smooth inverse F−1 : N→ M. Manifolds M,N are called diffeomorphic
if there exists a diffeomorphism from M to N.
In other words, a diffeomorphism of manifolds is a bijection of the underlying sets
that identiﬁes the maximal atlases of the manifolds. Manifolds that are diffeomor-
phic are therefore considered ‘the same manifolds’.
Similarly, a continuous mapF : M→ N is called a homeomorphism if it is invert-
ible, with a continuous inverse. Manifolds that are homeomorphic are considered
‘the same topologically’. Since every smooth map is continuous, every diffeomor-
phism is a homeomorphism.

44 3 Smooth maps
Example 3.6. By deﬁnition, every coordinate chart (U, ϕ) on a manifold M gives a
diffeomorphism ϕ : U→ ϕ(U) onto an open subset of Rm.
Example 3.7. The standard example of a homeomorphism of smooth manifolds that
is not a diffeomorphism is the map
R→ R, x↦→ x3.
Indeed, this map is smooth and invertible, but the inverse mapy↦→ y
1
3 is not smooth.
Example 3.8. Give a manifold M, with maximal atlas A , then any homeomorphism
F : M→ M can be used to deﬁne a new atlas A′ on M, with charts (U′, ϕ′)∈ A′
obtained from charts (U, ϕ)∈ A as U′ = F(U), ϕ′ = ϕ◦ F−1. One can verify
(please do) that A′ = A if and only if F is a diffeomorphism. Thus, if F is a
homeomorphism of M which is not a diffeomorphism, then F deﬁnes a new atlas
A′⁄= A .
However, the new manifold structure on M is not genuinely different from the
old one. Indeed, while F : M→ M is not a diffeomorphism relative to the atlas A
on the domain M and target M, it does deﬁne a diffeomorphism if we use the atlas
A on the domain and the atlas A′ on the target. Hence, even though A and A′ are
different atlases, the resulting manifold structures are still diffeomorphic.
Remark 3.4. In the introduction, we explained (without proof) the classiﬁcation of
1-dimensional and 2-dimensional connected compact manifolds up to diffeomor-
phism. This classiﬁcation coincides with their classiﬁcation up to homeomorphism.
This means, for example, that for any maximal atlas A′ on S2 which induces the
same system of open subsets as the standard maximal atlas A , there exists a home-
omorphism F : S2→ S2 taking A to A′, in the sense that (U, ϕ)∈ A if and only if
(U′, ϕ′)∈ A′, where U′ = F(U) and ϕ′◦ F = ϕ. In higher dimensions, it becomes
much more complicated: .
It is quite possible for two manifolds to be homeomorphic but not diffeomor-
phic (unlike example 3.8). The ﬁrst example of ‘exotic’ manifold structures was
discovered by John Milnor in 1956, who found that the 7-sphereS7 admits manifold
structures that are not diffeomorphic to the standard manifold structure, but induce
the standard topology. Kervaire and Milnor in 1963, proved that there are exactly
28 distinct manifold structures on S7, and in fact classiﬁed all manifold structures
on all spheres Sn with the exception of the case n = 4. For example, they showed
that S3,S5,S6 do not admit exotic (i.e., non-standard) manifold structures, while S15
has 16256 different manifold structures. For S4 the existence of exotic manifold
structures is an open problem; this is known as the smooth Poincare conjecture.
Around 1982, Michael Freedman (using results of Simon Donaldson) discovered
the existence of exotic manifold structures on R4; later Clifford Taubes showed that
there are uncountably many such. For Rn with n⁄= 4, it is known that there are no
exotic manifold structures on Rn.

3.3 Examples of smooth maps 45
3.3 Examples of smooth maps
3.3.1 Products, diagonal maps
a) If M,N are manifolds, then the projection maps
prM : M× N→ M, prN : M× N→ N
are smooth. (This follows immediately by taking product charts Uα×Vβ .)
b) The diagonal inclusion
∆M : M→ M× M
is smooth. (In a coordinate chart (U, ϕ) around p and the chart (U× U, ϕ× ϕ)
around (p, p), the map is the restriction to ϕ(U)⊆ Rn of the diagonal inclusion
Rn→ Rn× Rn.)
c) Suppose F : M→ N and F′ : M′→ N′ are smooth maps. Then the direct
product
F× F′ : M× M′→ N× N′
is smooth. This follows from the analogous statement for smooth maps on open
subsets of Euclidean spaces.
3.3.2 The diffeomorphism RP1∼= S1
We have stated before that RP1∼= S1. To obtain an explicit diffeomorphism, we
construct a bijection identifying the standard atlas for RP1 with (essentially) the
standard atlas for S1. Recall that the atlas for RP1 is given by
U1 ={(u : 1)| u∈ R}, ϕ1(u : 1) = u,
U0 ={(1 : u)| u∈ R}, ϕ0(1 : u) = u
with ϕi(Ui) = R and ϕ0(U0∩U1) = ϕ1(U0∩U1) = R\{0}, with the transition map
ϕ1◦ ϕ−1
0 : u↦→ u−1. Similarly, the atlas for S1 is
U+ ={(x,y)∈ S1| y⁄=−1} ϕ+(x,y) = x
1 + y ,
U− ={(x,y)∈ S1| y⁄= +1} ϕ−(x,y) = x
1− y .
again with ϕ±(U±) = R, ϕ±(U+∩U−) = R\{0}, and transition map u↦→ u−1.
Hence, there is a well-deﬁned diffeomorphism F : RP1→ S1 which identiﬁes
the chart (U−, ϕ−) with (U1, ϕ1) and (U+, ϕ+) with (U0, ϕ0), in the sense that both

46 3 Smooth maps
ϕ−◦ F◦ ϕ−1
1 : R→ R, ϕ+◦ F◦ ϕ−1
0 : R→ R
are the identity idR. Namely, the restriction ofF to U1 is FU1 = ϕ−1
− ◦ ϕ1 : U1→ U−,
the restriction to U0 is F|U0 = ϕ−1
+ ◦ ϕ0 : U0→ U+. The inverse map G = F−1 :
S1→ RP(1) is similarly given by ϕ−1
0 ◦ ϕ+ over U+ and by ϕ−1
1 ◦ ϕ− over U−. A
calculation gives
F : RP1→ S1, (w0 : w1)↦→ 1
||w||2 (2w1w0, (w0)2− (w1)2);
with inverse.
G(x,y) = ( 1 + y : x), y⁄=−1,
G(x,y) = ( x : 1− y), y⁄= 1
(note that the two expressions agree if−1 < y < 1). For example, to get the formula
for G(x,y) for y⁄=−1, i.e. (x,y)∈ U+, we calculate as follows:
ϕ−1
0 ◦ ϕ+(x,y) = ϕ−1
0
( x
1 + y
)
=
(
1 : x
1 + y
)
= (1 + y : x).
Exercise: Work out the details of the calculation of F(w0 : w1).
3.3.3 The diffeomorphism CP1∼= S2
By a similar reasoning, we ﬁnd CP1∼= S2. For S2 we use the atlas given by stereo-
graphic projection.
U+ ={(x,y,z)∈ S2| z⁄=−1} ϕ+(x,y,z) = 1
1 + z (x,y),
U− ={(x,y,z)∈ S2| z⁄= +1} ϕ−(x,y,z) = 1
1− z (x,y).
The transition map is u↦→ u
||u||2 , for u = (u1,u2). Regarding u as a complex number
u = u1 + iu2, the norm||u|| is just the absolute value of u, and the transition map
becomes
u↦→ u
|u|2 = 1
u .
Note that it is not quite the same as the transition map for the standard atlas of CP1,
which is given by u↦→ u−1. We obtain a unique diffeomorphism F : CP1→ S2
such that ϕ+◦ F◦ ϕ−1
0 is the identity, while ϕ−◦ F◦ ϕ−1
1 is complex conjugation. A
calculation shows that this map is

3.3 Examples of smooth maps 47
F(w0 : w1) = 1
|w0|2 +|w1|2
(
2Re(w1w0), 2Im(w1w0),|w0|2−| w1|2
)
;
the inverse map G = F−1 : S2→ CP(1) is
G(x,y,z) = ( 1 + z : x + iy), z⁄=−1,
G(x,y,z) = ( x− iy : 1− z), z⁄= 1
(note that the two expressions agree if−1 < z < 1).
Exercise: Work out the details of the calculation.
3.3.4 Maps to and from projective space
The quotient map
π : Rn+1\{0}→ RPn, x = (x0, . . . ,xn)↦→ (x0 : . . .: xn)
is smooth, as one veriﬁes by checking in the standard atlas for RPn. Indeed, on the
open subset where xi⁄= 0, we have π(x)∈ Ui, and
(ϕi◦ π)(x0, . . . ,xn) = ( x0
xi , . . . ,xi−1
xi , xi+1
xi , . . . ,xn
xi ).
which is a smooth function on the open set of x’s for whichxi⁄= 0.
Given a map F : RPn→ N to a manifold N, let ~F = F◦ π : Rn+1\{0}→ N be
its composition with the projection map π : Rn+1\{0}→ RPn. That is,
~F(x0, . . . ,xn) = F(x0 : . . .: xn).
Note that ~F(λx0 : . . .: λxn) = ~F(x0, . . . ,xn) for all non-zero λ; conversely, every
map ~F with this property descends to a map F on projective space. We claim that
the map F is smooth if and only the corresponding map ~F is smooth. One direction
is clear: If F is smooth, then ~F = F◦ π is a composition of smooth maps. For the
other direction, assuming that~F is smooth, note that for the standard chart (Uj, ϕ j),
the maps
(F◦ ϕ−1
j )(u1, . . . ,un) =~F(u1, . . . ,ui,1,ui+1, . . . ,un),
are smooth.
An analogous argument applies to the complex projective space CPn, taking the
xi to be complex numbers zi. That is, the quotient map π : Cn+1\{0}→ CPn is
smooth, and a map F : CPn→ N is smooth if and only if the corresponding map
~F : Cn+1\{0}→ N is smooth.
As an application, we can see that the map
CP1→ CP2, (z0 : z1)↦→ ((z0)2 : (z1)2 : z0z1)

48 3 Smooth maps
is smooth, starting with the (obvious) fact that the lifted map
C2\{0}→ C3\{0}, (z0,z1)↦→ ((z0)2, (z1)2,z0z1)
is smooth.
3.3.5 The quotient map S2n+1→ CPn
As we explained above, the quotient mapq : Cn+1\{0}→ CPn is smooth. Since any
class [z] = (z0 : . . .: zn) has a representative with|z0|2 + . . .+|zn|2 = 1, and|zi|2 =
(xi)2 + (yi)2 for zi = xi +√−1yi, we may also regard CPn as a set of equivalence
classes in the unit sphere S2n+1⊆ R2n+2 = Cn+1. The resulting quotient map
π : S2n+1→ CPn
is again smooth, because it can be written as a composition of two smooth maps
π = q◦ ι
where ι : S2n+1→ R2n+2\{0} = Cn+1\{0} is the inclusion map.
For any p∈ CPn, the corresponding ﬁber π−1(p)⊆ S2n+1 is diffeomorphic to a
circle S1 (which we may regard as complex numbers of absolute value 1). Indeed,
given any point (z0, . . . ,zn)∈ π−1(p) in the ﬁber, the other points are obtained as
(λz0, . . . ,λzn) where|λ| = 1.
In other words, we can think of
S2n+1 =
⋃
p∈CPn
π−1(p)
as a union of circles, parametrized by the points of CPn. This is an example of
what differential geometers call a ﬁber bundle or ﬁbration. We won’t give a formal
deﬁnition here, but let us try to ‘visualize’ the ﬁbration for the important casen = 1.
Identifying CP1∼= S2 as above, the map π becomes a smooth map
π : S3→ S2
with ﬁbers diffeomorphic to S1. This map appears in many contexts; it is called the
Hopf ﬁbration (after Heinz Hopf (1894-1971)).

3.3 Examples of smooth maps 49
Let S∈ S3 be the ‘south pole’, andN∈ S3 the ‘north pole’. We have thatS3−{S}∼=
R3 by stereographic projection. The set π−1(π(S))−{ S} projects to a straight line
(think of it as a circle with ‘inﬁnite radius’). The ﬁber π−1(N) is a circle that goes
around the straight line. If Z⊆ S2 is a circle at a given ‘latitude’, then π−1(Z) is
is a 2-torus. For Z close to N this 2-torus is very thin, while for Z approaching the
south pole S the radius goes to inﬁnity. Each such 2-torus is itself a union of circles
π−1(p), p∈ Z. Those circles are neither the usual ‘vertical’ or ‘horizontal’ circles
of a 2-torus in R3, but instead are ‘tilted’. In fact, each such circle is a ‘perfect ge-
ometric circle’ obtained as the intersection of its 2-torus with a carefully positioned
afﬁne 2-plane.
Moreover, any two of the circles π−1(p) are linked:
The full picture looks as follows:1
1 http://perso- math.univ- mlv.fr/users/kloeckner.benoit/images.html

50 3 Smooth maps
A calculation shows that over the chartsU+,U− (from stereographic projection), the
Hopf ﬁbration is just a product. That is, one has
π−1(U+)∼= U+× S1, π−1(U−)∼= U−× S1.
In particular, the pre-image of the closed upper hemisphere is asolid 2-torus D2×S1
(with D2 ={z∈ C|| z|≤ 1} the unit disk), geometrically depicted as a 2-torus inR3
together with its interior.2 We hence see that the S3 may be obtained by gluing two
solid 2-tori along their boundaries S1× S1.
3.4 Submanifolds
Let M be a manifold of dimension m. We will deﬁne a k-dimensional submanifold
S⊆ M to be a subset that looks locally like Rk⊆ Rm (which we take to be the
coordinate subspace deﬁned by xk+1 =··· = xm = 0.
Deﬁnition 3.4. A subset S⊆ M is called a submanifold of dimension k≤ m, if for
all p∈ S there exists a coordinate chart (U, ϕ) around p such that
ϕ(U∩ S) = ϕ(U)∩ Rk.
Charts (U, ϕ) of M with this property are called submanifold charts for S.
Remark 3.5. 1. A chart (U, ϕ) such that U∩S = / 0 andϕ(U)∩ Rk = / 0 is considered
a submanifold chart.
2. We stress that the existence of submanifold charts is only required for points p
that lie in S. For example, the half-open line S = (0, ∞) is a submanifold of R.
There does not exist a submanifold chart containing 0, but this is not a problem
since 0⁄∈ S.
Strictly speaking, a submanifold chart for S is not a chart for S, but is a chart for M
which is adapted to S. On the other hand, submanifold charts restrict to charts for S,
and this may be used to construct an atlas for S:
Proposition 3.3. Suppose S is a submanifold of M. Then S is a k-dimensional man-
ifold in its own right, with atlas consisting of all charts (U∩ S, ϕ|U∩S) such that
(U, ϕ) is a submanifold chart.
Proof. Let (U, ϕ) and (V, ψ) be two submanifold charts for S. We have to show that
the charts (U∩ S, ϕ|U∩S) and (V∩ S, ψ|V∩S) are compatible. The map
ψ|V∩S◦ ϕ|−1
U∩S : ϕ(U∩V )∩ Rk→ ψ(U∩V )∩ Rk
2 A solid torus is an example of a ”manifold with boundary”, a concept we haven’t properly dis-
cussed yet.

3.4 Submanifolds 51
is smooth, because it is the restriction ofψ◦ ϕ−1 : ϕ(U∩V )→ ψ(U∩V ) to the co-
ordinate subspace Rk. Likewise its inverse map is smooth. The Hausdorff condition
follows because any two distinct points p,q∈ S, one can take disjoint submanifold
charts around p,q. (Just take any submanifold charts, and intersect with the domains
of disjoint charts around p,q.)
The proof that S admits a countable atlas is unfortunately a bit technical 3. We
use the following
Fact: Every open subset of Rm is a union of rational ε-balls Bε (x), ε > 0. Here, ‘rational’
means that both the center of the ball and its radius are rational: x∈ Qn, ε∈ Q.
(We leave this as an exercise.) Our goal is to construct a countable collection of
submanifold charts coveringS. (The atlas forS itself is then obtained by restriction.)
Start with any countable atlas (Uα , ϕα ) for M. Given p∈ S∩Uα, we can choose
a submanifold chart (V, ψ) containing p. Using the above fact, we can choose a
rational ε-ball with
ϕ(p)∈ Bε (x)⊆ ϕα (Uα∩V ).
This shows that the subsets of the form ϕ−1
α (Bε (x)), with Bε (x)⊆ ϕα (Uα ) a ra-
tional ε-ball such that ϕ−1
α (Bε (x)) is contained in some submanifold chart, cover
all of S. Take these to be the domains of a charts (Vβ , ψβ ), where Vβ is one of the
ϕ−1
α (Bε (x)), and ψβ is the restriction of the coordinate maps of a submanifold chart
containing ϕ−1
α (Bε (x)). Then{(Vβ , ψβ )} is a countable collection of submanifold
charts covering S. (Recall that a countable union of countable sets is again count-
able.) ⊓ ⊔
Example 3.9 (Open subsets). The m-dimensional submanifolds of anm-dimensional
manifold are exactly the open subsets.
Example 3.10 (Spheres). Let Sn ={x∈ Rn+1||| x||2 = 1}. Write x = (x0, . . . ,xn), and
regard
Sk⊆ Sn
for k < n as the subset where the last n− k coordinates are zero. These are subman-
ifolds: The charts (U±, ϕ±) for Sn given by stereographic projection
ϕ±(x0, . . . ,xn) = 1
1± x0 (x1, . . . ,xn)
are submanifold charts. In fact, the charts U±
i , given by the condition that±xi > 0,
with ϕ±
i the projection to the remaining coordinates, are submanifold charts as well.
Example 3.11 (Projective spaces). For k < n, regard
RPk⊆ RPn
as the subset of all (x0 : . . .: xn) for which xk+1 = . . .= xn = 0. These are submani-
folds, with the standard charts (Ui, ϕi) for RPn as submanifold charts. (Note that the
3 You are welcome to ignore the following proof.

52 3 Smooth maps
charts Uk+1, . . . ,Un don’t meet RPk, but this does not cause a problem.) In fact, the
resulting charts for RPk obtained by restricting these submanifold charts, are just
the standard charts of RPk. Similarly,
CPk⊆ CPn
are submanifolds, and for n < n′ we have Gr(k,n)⊆ Gr(k,n′) as a submanifold.
Proposition 3.4. Let F : M→ N be a smooth map between manifolds of dimensions
m and n. Then
graph(F) ={(F(p), p)| p∈ M}⊆ N× M
is a submanifold of N× M, of dimension equal to the dimension of M.
Proof. Given p∈ M, choose charts (U, ϕ) around p and (V, ψ) around F(p), with
F(U)⊆ V , and let W = V×U. We claim that (W, κ) with
κ(q, p) = (ϕ(p), ψ(q)− ψ(F(p))) (3.8)
is a submanifold chart for graph (F)⊆ N× M. Note that this is indeed a chart of
N×M, because it is obtained from the product chart(V×U, ψ× ϕ) by composition
with the diffeomorphism ψ(V )× ϕ(U)→ ϕ(U)× ψ(V ), (v,u)↦→ (u,v), followed
by the diffeomorphism
ϕ(U)× ψ(V )→ κ(W ), (u,v)↦→ (u,v−~F(u)). (3.9)
where~F = ψ◦F◦ ϕ−1. (The map (3.9) is smooth and injective, and its Jacobian has
determinant one, hence is invertible everywhere.) Furthermore, the second compo-
nent in (3.8) vanishes if and only if F(p) = q. That is,
κ(W∩ graph(F)) = κ(W )∩ Rm
as required. ⊓ ⊔
This result has the following consequence: If a subset of a manifold, S⊆ M, can be
locally described as the graph of a smooth map, then S is a submanifold. In more
detail, suppose that S can be covered by open sets U, such that for each U there is a
diffeomorphism U→ P×Q taking S∩U to the graph of a smooth mapQ→ P, then
S is a submanifold.
Example 3.12. The 2-torus S = f−1(0)⊆ R3, where
f (x,y,z) = (
√
x2 + y2− R)2 + z2− r2
is a submanifold of R3, since it can locally be expressed as the graph of a function
of x,y, or of y,z, or of x,z. For example, on the subset where z > 0, it is the graph of
the smooth function on the annulus{(x,y)| (R− r)2 < x2 + y2 < (R + r)2}, given as
H(x,y) =
√
r2− (
√
x2 + y2− R)2.

3.4 Submanifolds 53
This function is obtained by solving the equation f (x,y,z) for z. Similarly, on each
of the four components of the subset where x2 + y2⁄= R2 and x⁄= 0 (respectively,
y⁄= 0), one can solve the equation f (x,y,z) = 0 uniquely for x (respectively, for y),
expressing S as the graph of a smooth function of y and z (respectively, of x and z).
Exercise: Work out the formula for theF(y,z) on the subset where x2 +y2 < R2 and
x > 0.
Example 3.13. More generally, suppose S⊆ R3 is given as a level set S = f−1(0)
for a smooth map f∈ C∞(R3). (Actually, we only need f to be deﬁned and smooth
on an open neighborhood of S.) Let p∈ S, and suppose
∂ f
∂x
⏐⏐⏐
p
⁄= 0.
By the implicit function theoremfrom multivariable calculus, there is an open neigh-
borhood U⊆ R3 of p on which the equation f (x,y,z) = 0 can be uniquely solved
for x. That is,
S∩U ={(x,y,z)∈ U| x = F(y,z)}
for a smooth function F, deﬁned on a suitable open subset of R2. This shows that S
is a submanifold near p, and in fact we may use y,z as coordinates near p. Similar
arguments apply for ∂ f
∂y|p⁄= 0 or ∂ f
∂z|p⁄= 0. Hence, if the gradient
∇ f = ( ∂ f
∂x , ∂ f
∂y , ∂ f
∂z )
is non-vanishing at all pointsp∈ S = f−1(0), then S is a 2-dimensional submanifold.
Of course, there is nothing special about 2-dimensional submanifolds of R3, and
below, we will put this discussion in a more general framework.
As we saw, submanifoldsS of manifolds M are themselves manifolds. They come
with an inclusion map
i : S→ M, p↦→ p,
taking any point of S to the same point but viewed as a point of M. Unsurprisingly,
we have:
Proposition 3.5. The inclusion map i : S→ M is smooth.
Proof. Given p∈ S⊆ M, let (U, ϕ) be a submanifold chart around p∈ M, and
(U∩ S, ϕ|U∩S) the corresponding chart around p∈ S. The composition
ϕ◦ i◦ (ϕ|U∩S)−1 : ϕ(U∩ S)→ ϕ(U)
is simply the inclusion map from ϕ(U)∩ Rk to ϕ(U), which is obviously smooth.
⊓ ⊔

54 3 Smooth maps
This shows in particular that if F∈ C∞(M,N) is a smooth map, then its restriction
F|S : S→ N is again smooth. Indeed, F|S = F◦ i is a composition of smooth maps.
This is useful in practice, because in such cases there is no need to verify smoothness
in local coordinates ofS! For example, the mapS2→ R, (x,y,z)↦→ z is smooth since
it is the restriction of a smooth map R3→ R to the submanifold S2. A related result,
which we leave as an exercise, is the following:
Exercise. Let S⊆ M be a submanifold, with inclusion map i, and let F : Q→ S be
a map from another manifold Q. Then F is smooth if and only if i◦ F is smooth. (In
other words, if and only if F is smooth as a map into M.)
For the following proposition, recall that a subset U of a manifold is open if
and only if for all p∈ U, and any coordinate chart (V, ψ) around p, the subset
ψ(U∩V )⊆ Rm is open. (This does not depend on the choice of chart.)
Proposition 3.6. Suppose S is a submanifold of M. Then the open subsets of S for
its manifold structure are exactly those of the form U∩S, where U is an open subset
of M.
In other words, the topology of S as a manifold coincides with the ‘subspace topol-
ogy’ as a subset of the manifoldM.
Proof. We have to show:
U′⊆ S is open ⇔ U′ = U∩ S where U⊆ M is open.
“⇒”. SupposeU⊆ M is open, and letU′ = U∩S. For any submanifold chart(V, ψ),
with corresponding chart (V∩ S, ψ|V∩S) for S, we have that
ψ((V∩ S)∩U′) = ψ(V∩ S∩U) = ψ(U)∩ ψ(V )∩ Rk
is the intersection of the open set ψ(U)∩ ψ(V )⊆ Rn with the subspace Rk, hence
is open in Rk. Since submanifold charts cover all of S, this shows that U′ is open.
“⇐” Suppose U′⊆ S is open in S. Deﬁne
U =
⋃
V
ψ−1(ψ(U′∩V )× Rm−k)⊆ M,
where the union is over any collection of submanifold charts(V, ψ) that cover all of
S. SinceU′ is open inS, so isU′∩V≡ U′∩(V∩S). Hence ψ(U′∩V ) = ψ(U′∩(V∩
S)) is open in Rk, and its cartesian product with Rm−k is open in Rm. The pre-image
ψ−1(ψ(U′∩V )× Rm−k) is thus open in V , hence also in M, and the union over all
such sets is open in M. Since U∩ S = U′ (see exercise below) we are done. ⊓ ⊔
Exercise: Fill in the last detail of this proof: Check that U∩ S = U′.
Remark 3.6. As a consequence, if a manifold M can be realized realized as a sub-
manifold M⊆ Rn, then M is compact with respect to its manifold topology if and
only if it is compact as a subset ofRn, if and only if it is a closed and bounded subset

3.5 Smooth maps of maximal rank 55
of Rn. This can be used to give quick proofs of the facts that the real or complex
projective spaces, as well as the real or complex Grassmannians, are all compact.
Remark 3.7. Sometimes, the result can be used to show that certain subsets are not
submanifolds. Consider for example the subset
S ={(x,y)∈ R2| xy = 0}⊆ R2
given as the union of the coordinate axes. If S were a 1-dimensional submanifold,
then there would exist an open neighborhood U′ of p = (0,0) in S which is dif-
feomorphic to an open interval. But for any open subset U⊆ R2 containing p, the
intersection U′ = U∩ S cannot possibly be an open interval, since (U∩ S)\{p} has
at least four components, while removing a point from an open interval gives only
two components.
3.5 Smooth maps of maximal rank
Let F∈ C∞(M,N) be a smooth map. Then the ﬁbers (level sets)
F−1(q) ={x∈ M| F(x) = q}
for q∈ N need not be submanifolds, in general. Similarly, the image F(M)⊆ N
need not be a submanifold – even if we allow self-intersections. (More precisely,
there may be points p such that the image F(U)⊆ N of any open neighborhood U
of p is never a submanifold.) Here are some counter-examples:
1. The ﬁbers f−1(c) of the map f (x,y) = xy are hyperbolas for c⁄= 0, but f−1(0) is
the union of coordinate axes. What makes this possible is that the gradient of f
is zero at the origin.
2. As we mentioned earlier, the image of the smooth map
γ : R→ R2, γ(t) = (t2,t3)
does not look smooth near (0,0) (and replacing R by an open interval around 0
does not help). 4 What makes this is possible is that the velocity ˙γ(t) vanishes for
t = 0: the curve described by γ ‘comes to a halt’ att = 0, and then turns around.
In both cases, the problems arise at points where the map does not have maximal
rank. After reviewing the notion of rank of a map from multivariable calculus, we
will generalize to manifolds.
4 It is not a submanifold, although we haven’t proved it (yet).

56 3 Smooth maps
3.5.1 The rank of a smooth map
The following discussion will involve some notions from multivariable calculus. Let
U⊆ Rm and V⊆ Rn be open subsets, and F∈ C∞(U,V ) a smooth map.
Deﬁnition 3.5. The derivative of F at p∈ U is the linear map
DpF : Rm→ Rn, v↦→ d
dt
⏐⏐⏐
t=0
F(p +tv).
The rank of F at p is the rank of this linear map:
rankp(F) = rank(DpF).
(Recall that the rank of a linear map is the dimension of its range.) Equivalently,
DpF is the n× m matrix of partial derivatives (DpF)i
j = ∂Fi
∂x j
⏐⏐⏐
p
:
DpF =


∂F1
∂x1
⏐⏐
p
∂F1
∂x2
⏐⏐
p··· ∂F1
∂xm
⏐⏐
p
∂F2
∂x1
⏐⏐
p
∂F2
∂x2
⏐⏐
p··· ∂F2
∂xm
⏐⏐
p
··· ··· ··· ···
∂Fn
∂x1
⏐⏐
p
∂Fn
∂x2
⏐⏐
p··· ∂Fn
∂xm
⏐⏐
p


and the rank of F at p is the rank of this matrix (i.e., the number of linearly inde-
pendent rows, or equivalently the number of linearly independent columns). Note
rankp(F)≤ min(m,n). By the chain rule for differentiation, the derivative of a com-
position of two smooth maps satisﬁes
Dp(F′◦ F) = DF(p)(F′)◦ Dp(F). (3.10)
In particular, if F′ is a diffeomorphism then rankp(F′◦ F) = rankp(F), and if F is a
diffeomorphism then rankp(F′◦ F) = rankF(p)(F′).
Deﬁnition 3.6. Let F∈ C∞(M,N) be a smooth map between manifolds, and p∈ M.
The rank of F at p∈ M is deﬁned as
rankp(F) = rankϕ(p)(ψ◦ F◦ ϕ−1)
for any two coordinate charts (U, ϕ) around p and (V, ψ) around F(p) such that
F(U)⊆ V .
By (3.10), this is well-deﬁned: if we use different charts (U′, ϕ′) and (V′, ψ′), then
the rank of
ψ′◦ F◦ (ϕ′)−1 = (ψ′◦ ψ−1)◦ (ψ◦ F◦ ϕ−1)◦ (ϕ◦ (ϕ′)−1)
at ϕ′(p) equals that of ψ◦ F◦ ϕ−1 at ϕ(p), since the two maps are related by dif-
feomorphisms.

3.5 Smooth maps of maximal rank 57
The following discussion will focus on maps of maximal rank. We have that
rankp(F)≤ min(dimM, dimN)
for all p∈ M; the map F is said to have maximal rank at p if rank p(F) =
min(dimM, dimN). A point p∈ M is called a critical point for F if rank p(F) <
min(dimM, dimN).
3.5.2 Local diffeomorphisms
In this section we will consider the case dim M = dimN. Our ‘workhorse theorem’
from multivariable calculus is going to be the following fact.
Theorem 3.1 (Inverse Function Theorem for Rm). Let F∈ C∞(U,V ) be a smooth
map between open subsets of Rm, and suppose that the derivative D pF at p∈ U is
invertible. Then there exists an open neighborhood U1⊆ U of p such that F restricts
to a diffeomorphism U1→ F(U1).
Remark 3.8. The theorem tells us that for a smooth bijection, a sufﬁcient condition
for smoothness of the inverse map is that the differential (i.e., the ﬁrst derivative) is
invertible everywhere. It is good to see, in just one dimensions, how this is possible.
Given an invertible smooth function y = f (x), with inverse x = g(y), and using
d
dy = dx
dy
d
dx, we have
g′(y) = 1
f′(x) ,
g′′(y) = = − f′′(x)
f′(x)3 ,
g′′′(y) = = − f′′′(x)
f′(x)4 + 3 f′′(x)2
f′(x)5 ,
and so on; only powers of f′(x) appear in the denominator.
Theorem 3.2 (Inverse function theorem for manifolds). Let F∈ C∞(M,N) be a
smooth map between manifolds of the same dimension m = n. If p∈ M is such that
rankp(F) = m, then there exists an open neighborhood U ⊆ M of p such that F
restricts to a diffeomorphism U→ F(U).
Proof. Choose charts (U, ϕ) around p and (V, ψ) around F(p) such that F(U)⊆ V .
The map
~F = ψ◦ F◦ ϕ−1 : ~U := ϕ(U)→~V := ψ(V )
has rank m at ϕ(p). Hence, by the inverse function theorem for Rm, after replac-
ing ~U with a smaller open neighborhood of ϕ(p) (equivalently, replacing U with

58 3 Smooth maps
a smaller open neighborhood of p) the map ~F becomes a diffeomorphism from ~U
onto~F(~U) = ψ(F(U)). It then follows that
F = ψ−1◦~F◦ ϕ : U→ V
is a diffeomorphism U→ F(U). ⊓ ⊔
A smooth map F∈ C∞(M,N) is called a local diffeomorphism if dim M = dimN,
and F has maximal rank everywhere. By the theorem, this is equivalent to the con-
dition that every point p has an open neighborhood U such that F restricts to a
diffeomorphism U→ F(U). It depends on the map in question which of these two
conditions is easier to verify.
Example 3.14. The quotient map π : Sn→ RPn is a local diffeomorphism. Indeed,
one can see (using suitable coordinates) that π restricts to diffeomorphisms from
each U±
j ={x∈ Sn|± x j > 0} to the standard chart Uj.
Example 3.15. The map R→ S1, t↦→ (cos(2πt), sin(2πt)) is a local diffeomor-
phism. (Exercise.)
Example 3.16. Let M be a manifold with a countable open cover{Uα}, and let
Q =
⨆
α
Uα
be the disjoint union. Then the map π : Q→ M, given on Uα⊆ Q by the inclusion
into M, is a local diffeomorphism. Sinceπ is surjective, it determines an equivalence
relation on Q, with π as the quotient map and M = Q/∼.
We leave it as an exercise to show that if the Uα’s are the domains of coordinate
charts, then Q is diffeomorphic to an open subset of Rm. This then shows that any
manifold is realized as a quotient of an open subset of Rm, in such a way that the
quotient map is a local diffeomorphism.
3.5.3 Level sets, submersions
The inverse function theorem is closely related to theimplicit function theorem, and
one may be obtained as a consequence of the other. (We have chosen to take the
inverse function theorem as our starting point.)
Proposition 3.7. Suppose F∈ C∞(U,V ) is a smooth map between open subsets U⊆
Rm and V⊆ Rn, and suppose p∈ U is such that the derivative D pF is surjective.
Then there exists an open neighborhood U 1⊆ U of p and a diffeomorphism κ :
U1→ κ(U1)⊆ Rm such that
(F◦ κ−1)(u1, . . . ,um) = (um−n+1, . . . ,um)
for all u = (u1, . . . ,um)∈ κ(U1).

3.5 Smooth maps of maximal rank 59
Thus, in suitable coordinates F is given by a projection onto the last n coordinates.
Although it belongs to multivariable calculus, let us recall how to get this result from
the inverse function theorem.
Proof. The idea is to extendF to a map between open subsets ofRm, and then apply
the inverse function theorem.
By assumption, the derivative DpF has rank equal to n. Hence it has n linearly
independent columns. By re-indexing the coordinates of Rm (this permutation is
itself a change of coordinates) we may assume that these are the last n columns.
That is, writing
DpF =
(
C,D
)
where C is the n× (m− n)-matrix formed by the ﬁrst m− n columns and D the
n× n-matrix formed by the last n columns, the square matrix D is invertible. Write
elements x∈ Rm in the form x = (x′,x′′) where x′ are the ﬁrst m− n coordinates and
x′′ the last n coordinates. Let
G : U→ Rm, x = (x′,x′′)↦→ (x′,F(x)).
Then the derivative DpG has block form
DpG =
(
Im−n 0
C D
)
,
(where Im−n is the square (m− n)× (m− n) matrix), and is hence is invertible.
Hence, by the inverse function theorem there exists a smaller open neighborhood
U1 of p such that G restricts to a diffeomorphism κ : U1→ κ(U1)⊆ Rm. We have,
G◦ κ−1(u′,u′′) = (u′,u′′)
for all (u′,u′′)∈ κ(U1). Since F is just G followed by projection to the x′′ compo-
nent, we conclude
F◦ κ−1(u′,u′′) = u′′.
⊓ ⊔

60 3 Smooth maps
Again, this result has a version for manifolds:
Theorem 3.3. Let F∈ C∞(M,N) be a smooth map between manifolds of dimensions
m≥ n, and suppose p∈ M is such that rankp(F) = n. Then there exist coordinate
charts (U, ϕ) around p and (V, ψ) around F(p), with F(U)⊆ V , such that
(ψ◦ F◦ ϕ−1)(u′,u′′) = u′′
for all u = (u′,u′′)∈ ϕ(U). In particular, for all q∈ V the intersection
F−1(q)∩U
is a submanifold of dimension m− n.
Proof. Start with coordinate charts (U, ϕ) around p and (V, ψ) around F(p) such
that F(U)⊆ V . Apply Proposition 3.7 to the map~F = ψ◦F◦ ϕ−1 : ϕ(U)→ ψ(V ),
to deﬁne a smaller neighborhoodϕ(U1)⊆ ϕ(U) and change of coordinatesκ so that
~F◦ κ−1(u′,u′′) = u′′. After renaming (U1, κ◦ ϕ|U1) as (U, ϕ) we have the desired
charts for F. The last part of the Theorem follows since (U, ϕ) becomes a subman-
ifold chart for F−1(q)∩U (after shifting ϕ by ψ(q)∈ Rn). ⊓ ⊔
Deﬁnition 3.7. Let F∈ C∞(M,N). A point q∈ N is called a regular value of F∈
C∞(M,N) if for all x∈ F−1(q), one has rank x(F) = dimN. It is called a singular
value if it is not a regular value.
Note that regular values are only possible if dimN≤ dimM. Note also that all points
of N that are not in the image of the map F are considered regular values. We may
restate Theorem 3.3 as follows:
Theorem 3.4 (Regular Value Theorem). For any regular value q∈ N of a smooth
map F∈ C∞(M,N), the level set S = F−1(q) is a submanifold of dimension
dimS = dimM− dimN.
Example 3.17. The n-sphere Sn may be deﬁned as the level set F−1(1) of the func-
tion F∈ C∞(Rn+1, R) given by
F(x0, . . . ,xn) = (x0)2 + . . .+ (xn)2.
The derivative of F is the 1× (n + 1)-matrix of partial derivatives, that is, the gradi-
ent ∇F:
DpF = (2x0, . . . ,2xn).
For x⁄= 0 this has maximal rank. Note that any nonzero real number q is a regular
value since 0⁄∈ F−1(q). Hence all the level sets F−1(q) for q⁄= 0 are submanifolds.
Example 3.18. Let 0 < r < R. Then
F(x,y,z) = (
√
x2 + y2− R)2 + z2
has r2 as a regular value, with corresponding level set the 2-torus.

3.5 Smooth maps of maximal rank 61
Example 3.19. The orthogonal group O(n) is the group of matrices A∈ MatR(n)
satisfying A⊤ = A−1. We claim that O(n) is a submanifold of MatR(n). To see this,
consider the map
F : Mat R(n)→ SymR(n), A↦→ A⊤A,
where SymR(n)⊆ MatR(n) denotes the subspace of symmetric matrices. We want
to show that the identity matrixI is a regular value ofF. We compute the differential
DAF : Mat R(n)→ SymR(n) using the deﬁnition5
(DAF)(X) = d
dt
⏐⏐⏐
t=0
F(A +tX )
= d
dt
⏐⏐⏐
t=0
((A⊤ +tX⊤)(A +tX ))
= A⊤X + X⊤A.
To see that this is surjective, for A∈ F−1(I), we need to show that for any Y∈
SymR(n) there exists a solution of
A⊤X + X⊤A = Y.
Using A⊤A = F(A) = I we see that X = 1
2AY is a solution. We conclude that I is a
regular value, and hence that O(n) = F−1(I) is a submanifold. Its dimension is
dimO (n) = dimMat R(n)− dimSym R(n) = n2− 1
2n(n + 1) = 1
2n(n− 1).
Note that it was important here to regard F as a map to SymR(n); for F viewed as a
map to MatR(n) the identity would not be a regular value.
Deﬁnition 3.8. A smooth map F∈ C∞(M,N) is a submersion if rankp(F) = dimN
for all p∈ M.
Thus, for a submersion all level sets F−1(q) are submanifolds.
Example 3.20. Local diffeomorphisms are submersions; here the level sets F−1(q)
are discrete points, i.e. 0-dimensional manifolds.
Example 3.21. Recall that CPn can be regarded as a quotient ofS2n+1. Using charts,
one can check that the quotient map π : S2n+1→ CPn is a submersion. Hence its
ﬁbers π−1(q) are 1-dimensional submanifolds. Indeed, as discussed before these
ﬁbers are circles. As a special case, the Hopf ﬁbration S3→ S2 is a submersion. As
a special case, the Hopf ﬁbration S3→ S2 is a submersion.
Remark 3.9. (For those who are familiar with quaternions.) Let H = C2 = R4 be
the quaternionic numbers. The unit quaternions are a 3-sphere S3. Generalizing the
5 Note that it would have been confusing to work with the description ofDAF as a matrix of partial
derivatives.

62 3 Smooth maps
deﬁnition of RPn and CPn, there are also quaternionic projective spaces,HPn. These
are quotients of the unit sphere inside Hn+1, hence one obtains submersions
S4n+3→ HPn;
the ﬁbers of this submersion are diffeomorphic to S3. For n = 1, one can show that
HP1 = S4, hence one obtains a submersion
π : S7→ S4
with ﬁbers diffeomorphic to S3.
3.5.4 Example: The Steiner surface
In this section, we will give more lengthy examples, investigating the smoothness
of level sets. 6
Example 3.22 (Steiner’s surface).Let S⊆ R3 be the solution set of
y2z2 + x2z2 + x2y2 = xyz.
in R3. Is this a smooth surface in R3? (We use surface as another term for 2-
dimensional manifold; by a surface in M we mean a 2-dimensional submanifold.)
Actually, we can easily see that it’snot. If we take one of x,y,z equal to 0, then the
equation holds if and only if one of the other two coordinates is 0. Hence, the inter-
section of S with the set where xyz = 0 (the union of the coordinate hyperplanes) is
the union of the three coordinate axes.
Hence, let us rephrase the question: LettingU⊆ R3 be the subset where xyz⁄= 0,
is S∩U is surface? To investigate the problem, consider the function
f (x,y,z) = y2z2 + x2z2 + x2y2− xyz.
The differential (which in this case is the same as the gradient) is the 1× 3-matrix
D(x,y,z) f =
(
2x(y2 + z2)− yz 2y(z2 + x2)− zx 2z(x2 + y2)− xy
)
This vanishes if and only if all three entries are zero. Vanishing of the ﬁrst entry
gives, after dividing by 2xy2z2, the condition
1
z2 + 1
y2 = 1
2xyz;
we get similar conditions after cyclic permutation of x,y,z. Thus we have
6 We won’t cover this example in class, for lack of time, but you’re encouraged to read it.

3.5 Smooth maps of maximal rank 63
1
z2 + 1
y2 = 1
x2 + 1
z2 = 1
y2 + 1
x2 = 1
2xyz ,
with a unique solution x = y = z = 1
4. Thus, D(x,y,z) f has maximal rank (i.e., it is
nonzero) except at this point. But this point doesn’t lie onS. We conclude thatS∩U
is a submanifold. How does it look like? It turns out that there is a nice answer. First,
let’s divide the equation forS∩U by xyz. The equation takes on the form
xyz( 1
x2 + 1
y2 + 1
z2 ) = 1. (3.11)
The solution set of (3.11) is contaned in the set of all (x,y,z) such that xyz > 0. On
this subset, we introduce new variables
α =
√xyz
x , β =
√xyz
y , γ =
√xyz
z ;
the old variables x,y,z are recovered as
x = β γ, y = αγ , z = αβ .
In terms of α, β , γ, Equation (3.11) becomes the equation α2 + β 2 + γ2 = 1. Actu-
ally, it is even better to consider the corresponding points
(α : β : γ) = ( 1
x : 1
y : 1
z )∈ RP2,
because we could take either square root of xyz (changing the sign of all α, β , γ
doesn’t affect x,y,z). We conclude that the map U→ RP2, (x,y,z)↦→ ( 1
x : 1
y : 1
z )
restricts to a diffeomorphism from S∩U onto
RP2\{(α : β : γ)| αβ γ = 0}.
The image of the map
RP2→ R3, (α : β : γ)↦→ 1
|α|2 +|β|2 +|γ|2 (β γ, αβ , αγ ).
is called Steiner’s surface, even though it is not a submanifold (not even animmersed
submanifold). Here is a picture: 7
7 Source: http://upload.wikimedia.org/wikipedia/commons/7/7a/
RomanSurfaceFrontalView.PNG

64 3 Smooth maps
Note that the subset of RP2 deﬁned by αβ γ = 0 is a union of three RP1∼= S1,
each of which maps into a coordinate axis (but not the entire coordinate axis).
For example, the circle deﬁned by α = 0 maps to the set of all (0,0,z) with
− 1
2≤ z≤ 1
2. In any case, S is the Steiner surface together with the three coordinate
axes. See http://www.math.rutgers.edu/courses/535/535-f02/
pictures/romancon.jpg for a very nice picture.
Example 3.23. Let S⊆ R4 be the solution set of
y2x2 + x2z2 + x2y2 = xyz, y2x2 + 2x2z2 + 3x2y2 = xyzw.
Again, this cannot quite be a surface because it contains the coordinate axes for
x,y,z. Closer investigation shows that S is the union of the three coordinate axes,
together with the image of an injective map
RP2→ R4, (α : β : γ)↦→ 1
α2 + β 2 + γ2 (β γ, αβ , αγ , α2 + 2β 2 + 3γ2).
It turns out (see Section 4.2.4 below) that the latter is a submanifold, which realizes
RP2 as a surface in R4.
3.5.5 Immersions
We next consider maps F : M→ N of maximal rank between manifolds of dimen-
sions m≤ n. Once again, such a map can be put into a ‘normal form’: By choosing
suitable coordinates it becomes linear.
Proposition 3.8. Suppose F∈ C∞(U,V ) is a smooth map between open subsets U⊆
Rm and V⊆ Rn, and suppose p∈U is such that the derivative DpF is injective. Then
there exist smaller neighborhoods U1⊆U of p and V1⊆V of F(p), with F(U1)⊆V1,
and a diffeomorphism χ : V1→ χ(V1), such that
(χ◦ F)(u) = (u,0)∈ Rm× Rn−m

3.5 Smooth maps of maximal rank 65
Proof. Since DpF is injective, it has m linearly independent rows. By re-indexing
the rows (which amounts to a change of coordinates on V ), we may assume that
these are the ﬁrst m rows.
That is, writing
DpF =
(
A
C
)
where A is the m× m-matrix formed by the ﬁrst m rows and C is the (n− m)× m-
matrix formed by the last n−m rows, the square matrix A is invertible. Consider the
map
H : U× Rn−m→ Rn, (x,y)↦→ F(x) + (0,y)
Then
D(p,0)H =
(
A 0
C I n−m
)
is invertible. Hence, by the inverse function theorem for Rn, H is a diffeomorphism
from some neighborhood of (p,0) in U× Rn−m onto some neighborhood V1 of
H(p,0) = F(p), which we may take to be contained in V . Let
χ : V1→ χ(V1)⊆ U× Rn−m
be the inverse; thus
(χ◦ H)(x,y) = (x,y)
for all (x,y)∈ χ(V1). Replace U with the smaller open neighborhood
U1 = F−1(V1)∩U
of p. Then F(U1)⊆ V1, and
(χ◦ F)(u) = (χ◦ H)(u,0) = (u,0)

66 3 Smooth maps
for all u∈ U1. ⊓ ⊔
The manifolds version reads as follows:
Theorem 3.5. Let F∈ C∞(M,N) be a smooth map between manifolds of dimensions
m≤ n, and p ∈ M a point with rankp(F) = m. Then there are coordinate charts
(U, ϕ) around p and (V, ψ) around F(p) such that F(U)⊆ V and
(ψ◦ F◦ ϕ−1)(u) = (u,0).
In particular, F(U)⊆ N is a submanifold of dimension m.
Proof. Once again, this is proved by introducing charts around p, F(p) to reduce
to a map between open subsets of Rm, Rn, and then use the multivariable version of
the result to obtain a change of coordinates, putting the map into normal form. ⊓ ⊔
Deﬁnition 3.9. A smooth map F : M→ N is an immersion if rankp(F) = dimM for
all p∈ M.
Example 3.24. Let J⊆ R be an open interval. A smooth map γ : J→ M is also
called a smooth curve. We see that the image of γ is an immersed submanifold,
provided that rank p(γ) = 1 for all p∈ M. In local coordinates (U, ϕ), this means
that d
dt (ϕ◦ γ)(t)⁄= 0 for all t with γ(t)∈ U. For example, the curve γ(t) = (t2,t3)
fails to have this property at t = 0.
Example 3.25 (Figure eight). The map
γ : R→ R2, t↦→
(
sin(t),sin(2t)
)
is an immersion; the image is a ﬁgure eight.
(Indeed, for all t∈ R we have Dt γ≡ ˙γ(t)⁄= 0.)
Example 3.26 (Immersion of the Klein bottle). The Klein bottle admits a ‘ﬁgure
eight’ immersion into R3, obtained by taking the ﬁgure eight in the x− z-plane,
moving in the x-direction by R > 1, and then rotating about the z-axis while at the
same time rotating the ﬁgure eight, so that after a full turn ϕ↦→ ϕ + 2π the ﬁgure
eight has performed a half turn. 8
8 Picture source: http://en.wikipedia.org/wiki/Klein_bottle

3.5 Smooth maps of maximal rank 67
We can regard this procedure as a composition of the following maps:
F1 : (t, ϕ)↦→ (sin(t),sin(2t), ϕ) = (u,v, ϕ),
F2 : (u,v, ϕ)↦→
(
ucos( ϕ
2 ) +vsin( ϕ
2 ), vcos( ϕ
2 )− usin( ϕ
2 ), ϕ
)
= (a,b, ϕ)
F3 :
(
a,b, ϕ)↦→ ((a + R)cos ϕ, (a + R)sin ϕ, b
)
= (x,y,z).
Here F1 is the ﬁgure eight in the u− v-plane (with ϕ just a bystander). F2 rotates
the u− v-plane as it moves in the direction of ϕ, by an angle of ϕ/2; thus ϕ = 2π
corresponds to a half-turn. The map F3 takes this family of rotating u,v-planes, and
wraps it around the circle in thex−y-plane of radius R, with ϕ now playing the role
of the angular coordinate.
The resulting map F = F3◦ F2◦ F1 : R2→ R3 is given by F(t, ϕ) = ( x,y,z),
where with
x =
(
R + cos( ϕ
2 )sin(t) +sin( ϕ
2 )sin(2t)
)
cos ϕ,
y =
(
R + cos( ϕ
2 )sin(t) +sin( ϕ
2 )sin(2t)
)
sin ϕ,
z = cos( ϕ
2 )sin(2t)− sin( ϕ
2 )sin(t)
is an immersion. To verify that this is an immersion, it would be cumbersome to
work out the Jacobian matrix directly. It is much easier to use that F is obtained as
a composition F = F3◦ F2◦ F1 of the three maps considered above, where F1 is an
immersion, F2 is a diffeomorphism, and F3 is a local diffeomorphism from the open
subset where|a| < R onto its image.
Since the right hand side of the equation for F does not change under the trans-
formations
(t, ϕ)↦→ (t + 2π, ϕ), (t, ϕ)↦→ (−t, ϕ + 2π),
this descends to an immersion of the Klein bottle. It is straightforward to check
that this immersion of the Klein bottle is injective, except over the ‘central circle’
corresponding to t = 0, where it is 2-to-1.
Note that under the above construction, any point of the ﬁgure eight creates a
circle after two‘full turns’,ϕ↦→ ϕ +4π. The complement of the circle generated by
the point t = π/2 consists of two subsets of the Klein bottle, generated by the parts

68 3 Smooth maps
of the ﬁgure eight deﬁned by −π/2 < t < π/2, and by π/2 < t < 3π/2. Each of
these is a ‘curled-up’ immersion of an open M¨obius strip. (Remember, it is possible
to remove a circle from the Klein bottle to create two M¨obius strips!) The pointt = 0
also creates a circle; its complement is the subset of the Klein bottle generated by
0 < t < 2π. (Remember, it is possible to remove a circle from a Klein bottle to create
one M¨obius strip.) We can also remove one copy of the ﬁgure eight itself; then the
‘rotation’ no longer matters and the complement is an open cylinder. (Remember, it
is possible to remove a circle from a Klein bottle to create a cylinder.)
Example 3.27. Let M be a manifold, and S⊆ M a k-dimensional submanifold. Then
the inclusion map ι : S→ M, x↦→ x is an immersion. Indeed, if (V, ψ) is a subman-
ifold chart for S, with p∈ U = V∩ S, ϕ = ψ|V∩S then
(ψ◦ F◦ ϕ−1)(u) = (u,0),
which shows that
rankp(F) = rankϕ(p)(ψ◦ F◦ ϕ−1) = k.
By an embedding, we will mean an immersion given as the inclusion map for a
submanifold. Not every injective immersion is an embedding; the following picture
gives a counter-example:
In practice, showing that an injective smooth map is an immersion tends to be easier
than proving that its image is a submanifold. Fortunately, for compact manifolds we
have the following fact:
Theorem 3.6. If M is a compact manifold, then every injective immersion F : M→
N is an embedding as a submanifold S = F(M).
Proof. Let p∈ M be given. By Theorem 3.5, we can ﬁnd charts (U, ϕ) around p
and (V, ψ) around F(p), with F(U)⊆ V , such that ~F = ψ◦ F◦ ϕ−1 is in normal
form: i.e., ~F(u) = ( u,0). We would like to take (V, ψ) as a submanifold chart for
S = F(M), but this may not work yet since F(M)∩V = S∩V may be strictly larger
than F(U)∩V . Note however that A := M\U is compact, hence its image F(A) is
compact, and therefore closed (here we are using that N is Haudorff). Since F is
injective, we have that p⁄∈ F(A). Replace V with the smaller open neighborhood
V1 = V\(V∩ F(A)). Then (V1, ψ|V1) is the desired submanifold chart.
Remark 3.10. Some authors refer to injective immersions ι : S→ M as ‘subman-
ifolds’ (thus, a submanifold is taken to be a map rather than a subset). To clarify,

3.6 Appendix: Algebras 69
‘our’ submanifolds are sometimes called ‘embedded submanifolds’ or ‘regular sub-
manifolds’.
Example 3.28. Let A,B,C be distinct real numbers. We will leave it as a homework
problem to verify that the map
F : RP2→ R4, (α : β : γ)↦→ (β γ, αγ , αβ , Aα2 + Bβ 2 +Cγ2),
where we use representatives (α, β , γ) such that α2 + β 2 + γ2 = 1, is an injective
immersion. Hence, by Theorem 3.6, it is an embedding of RP2 as a submanifold of
R4.
To summarize the outcome from the last few sections: IfF∈ C∞(M,N) has max-
imal rank near p∈ M, then one can always choose local coordinates around p and
around F(p) such that the coordinate expression ofF becomes a linear map of maxi-
mal rank. (This simple statement contains the inverse and implicit function theorems
from multivariable calculus are special cases.)
Remark 3.11. This generalizes further to maps of constant rank. In fact, if rankp(F)
is independent of p on some open subset U, then for all p∈ U one can choose
coordinates in which F becomes linear.
3.6 Appendix: Algebras
An algebra (over the ﬁeld R of real numbers) is a vector space A , together with a
multiplication (product) A× A→ A , (a,b)↦→ ab such that
1. The multiplication is associative: That is, for all a,b,c∈ A
(ab)c = a(bc).
2. The multiplication map is linear in both arguments: That is,
(λ1a1 + λ2a2)b = λ1(a1b) +λ2(a2b),
a(µ1b1 + µ2b2) = µ1(ab1) + µ2(ab2),

70 3 Smooth maps
for all a,a1,a2,b,b1,b2∈ A and all scalars λ1, λ2, µ1, µ2∈ R.
The algebra is called commutative if ab = ba for all a,b∈ A . A unital algebra is
an algebra A with a distinguished element 1A∈ A (called the unit), with
1A a = a = a1A
for all a∈ A .
Remark 3.12. One can also consider non-associative product operations on vector
spaces, most importantly one has the class of Lie algebras. If there is risk of confu-
sion with these or other concepts, we may refer to associative algebras.
For example, the space C of complex numbers (regarded as a real vector space
R2) is a unital, commutative algebra. A more sophisticated example is the alge-
bra H∼= R4 of quaternions, which is a unital non-commutative algebra. (Recall
that elements of H are expressions x + iu + jv + kw, where i, j,k have products
i2 = j2 = k2 =−1, i j = k =− ji, jk = i =−k j, ki = j =−ik.) For any n, the
space MatR(n) of n× n matrices, with product the matrix multiplication, is a non-
commutative unital algebra. One can also consider matrices with coefﬁcients in C,
or in fact with coefﬁcients in any given algebra. For any set X, the space of func-
tions f : X→ R is a unital commutative algebra, where the product is given by
pointwise multiplication. Given a topological space X, one has the algebra C(X) of
continuous R-valued functions. A homomorphism of algebras Φ : A → A′ is a
linear map preserving products: Φ(ab) = Φ(a)Φ(b). (For a homomorphism of uni-
tal algebras, one asks in addition that Φ(1A ) = 1A′.) It is called an isomorphism
of algebras if Φ is invertible. For the special case A′ = A , these are also called
algebra automorphisms of A . Note that the algebra automorphisms form a group
under composition.
Example 3.29. Consider R2 as an algebra, with product coming from the identiﬁca-
tion R2 = C. The complex conjugationz↦→ z deﬁnes an automorphism Φ : R2→ R2
of this algebra.
Example 3.30. The algebra H of quaternions has an automorphism given by cyclic
permutation of the three imaginary units. That is, Φ(x + iu + jv + kw) = x + ju +
kv + iw
Example 3.31. Let A = MatR(n) the algebra of n× n-matrices. If U∈ A is invert-
ible, then X↦→ Φ(X) = UXU−1 is an algebra automorphism.
Example 3.32. Suppose A is a unital algebra. Let A× be the set of invertible ele-
ments, that is, elements u∈ A for which there exists v∈ A with uv = vu = 1A .
Given u, such v is necessarily unique (write v = u−1), and the map A→ A , a↦→
uau−1 is an algebra automorphism. Such automorphisms are called ‘inner’.

Chapter 4
The tangent bundle
4.1 Tangent spaces
For embedded submanifoldsM⊆ Rn, the tangent spaceTpM at p∈ M can be deﬁned
as the set of all velocity vectors v = ˙γ(0), where γ : J→ M is a smooth curve with
γ(0) = p; here J⊆ R is an open interval around 0.
It turns out (not entirely obvious!) that TpM becomes a vector subspace of Rn.
(Warning: In pictures we tend to draw the tangent space as anafﬁne subspace, where
the origin has been moved to p.)
Example 4.1. Consider the sphere Sn⊆ Rn+1, given as the set of x such that||x||2 =
1. A curve γ(t) lies in Sn if and only if ||γ(t)|| = 1. Taking the derivative of the
equation γ(t)· γ(t) = 1 at t = 0, we obtain (after dividing by 2, and using γ(0) = p)
p· ˙γ(0) = 0.
That is, TpM consists of vectors v∈ Rn+1 that are orthogonal to p∈ R3\{0}. It is
not hard to see that every such vector v is of the form ˙γ(0),1 hence that
TpSn = (Rp)⊥,
the hyperplane orthogonal to the line through p.
1 Given v, take γ(t) = (p +tv)/||p +tv||.
71

72 4 The tangent bundle
To extend this idea to general manifolds, note that the vector v = ˙γ(0) deﬁnes a
“directional derivative”C∞(M)→ R:
v : f↦→ d
dt|t=0 f (γ(t)).
For a general manifold, we will deﬁne TpM as a set of directional derivatives.
Deﬁnition 4.1 (Tangent spaces – ﬁrst deﬁnition). Let M be a manifold, p∈ M.
The tangent space TpM is the set of all linear maps v : C∞(M)→ R of the form
v( f ) = d
dt|t=0 f (γ(t))
for some smooth curve γ∈ C∞(J,M) with γ(0) = p.
The elements v∈ TpM are called the tangent vectors to M at p.
The following local coordinate description makes it clear that TpM is a linear
subspace of the vector spaceL(C∞(M), R) of linear mapsC∞(M)→ R, of dimension
equal to the dimension of M.
Theorem 4.1. Let (U, ϕ) be a coordinate chart around p. A linear map v: C∞(M)→
R is in TpM if and only if it has the form,
v( f ) =
m
∑
i=1
ai ∂ ( f◦ ϕ−1)
∂ui
⏐⏐⏐
u=ϕ(p)
for some a = (a1, . . . ,am)∈ Rm.
Proof. Given a linear map v of this form, let ˜γ : R→ ϕ(U) be a curve with ˜γ(t) =
ϕ(p) +ta for|t| sufﬁciently small. Let γ = ϕ−1◦ ˜γ. Then
d
dt
⏐⏐⏐
t=0
f (γ(t)) = d
dt
⏐⏐⏐
t=0
( f◦ ϕ−1)(ϕ(p) +ta)
=
m
∑
i=1
ai ∂ ( f◦ ϕ−1)
∂ui
⏐⏐⏐
u=ϕ(p)
,
by the chain rule. Conversely, given any curve γ with γ(0) = p, let ˜γ = ϕ◦ γ be the
corresponding curve in ϕ(U) (deﬁned for small|t|). Then~γ(0) = ϕ(p), and
d
dt
⏐⏐⏐
t=0
f (γ(t)) = d
dt
⏐⏐⏐
t=0
( f◦ ϕ−1)( ˜γ(t))
=
m
∑
i=1
ai ∂ ( f◦ ϕ−1)
∂ui |u=γ(p),
where a = d ˜γ
dt
⏐⏐⏐
t=0
. ⊓ ⊔
We can use this result as an alternative deﬁnition of the tangent space, namely:

4.1 Tangent spaces 73
Deﬁnition 4.2 (Tangent spaces – second deﬁnition). Let (U, ϕ) be a chart around
p. The tangent space TpM is the set of all linear maps v : C∞(M)→ R of the form
v( f ) =
m
∑
i=1
ai ∂ ( f◦ ϕ−1)
∂ui
⏐⏐⏐
u=ϕ(p)
(4.1)
for some a = (a1, . . . ,am)∈ Rm.
Remark 4.1. From this version of the deﬁnition, it is immediate that TpM is an m-
dimensional vector space. It is not immediately obvious from this second deﬁnition
that TpM is independent of the choice of coordinate chart, but this follows from the
equivalence with the ﬁrst deﬁnition. Alternatively, one may check directly that the
subspace of L(C∞(M), R) characterized by (4.1) does not depend on the chart, by
studying the effect of a change of coordinates.
According to (4.1), any choice of coordinate chart (U, ϕ) around p deﬁnes a vector
space isomorphism TpM∼= Rm, taking v to a = (a1, . . . ,am). In particular, we see
that if U⊆ Rm is an open subset, and p∈ U, then TpU is the subspace of the space
of linear maps C∞(M)→ R spanned by the partial derivatives at p. That is, TpU has
a basis
∂
∂x1|p, . . . , ∂
∂xm|p
identifying TpU≡ Rm. Given
v = ∑ai ∂
∂xi|p
the coefﬁcients ai are obtained by applying v to the coordinate functions x1, . . . ,xm :
U→ R, that is, ai = v(xi).
We now describe yet another approach to tangent spaces which again charac-
terizes “directional derivatives” in a coordinate-free way, but without reference to
curves γ. Note ﬁrst that every tangent vector satisﬁes the product rule, also called
the Leibniz rule:
Lemma 4.1. Let v∈ TpM be a tangent vector at p∈ M. Then
v( f g) = f (p)v(g) +v( f )g(p) (4.2)
for all f ,g∈ C∞(M).
Proof. Letting v be represented by a curve γ, this follows from
d
dt
⏐⏐⏐
t=0
(
f
(
γ(t)
)
g
(
γ(t)
))
= f (p)
( d
dt
⏐⏐⏐
t=0
g
(
γ(t)
))
+
( d
dt
⏐⏐⏐
t=0
f
(
γ(t)
))
g(p).
⊓ ⊔
Alternatively, in local coordinates it is just the product rule for partial derivatives. It
turns out that the product rule completely characterizes tangent vectors:

74 4 The tangent bundle
Theorem 4.2. A linear map v : C∞(M)→ R deﬁnes an element of TpM if and only
if it satisﬁes the product rule (4.2).
The proof of this result will require the following fact from multivariable calculus:
Lemma 4.2 (Hadamard Lemma). Let U = BR(0)⊆ Rm be an open ball of radius
R > 0 and h∈ C∞(U) a smooth function. Then there exist smooth functions h i∈
C∞(U) with
h(u) = h(0) +
m
∑
i=1
uihi(u)
for all u∈ U. Here hi(0) = ∂h
∂ui (0).
Proof. Let hi be the functions deﬁned for u = (u1, . . . ,um)∈ U by
hi(u) =



1
ui
(
h(u1, . . . ,ui,0, . . . ,0)− h(u1, . . . ,ui−1,0,0, . . . ,0)
)
if ui⁄= 0
∂h
∂ui (u1, . . . ,ui−1,0,0, . . . ,0) if ui = 0
Using Taylor’s formula with remainder, one sees that these functions are smooth.
2 If all ui⁄= 0, then the sum ∑m
i=1 uihi(u) is a telescoping sum, equal to h(u)− h(0).
By continuity, this result extends to all u. Finally, evaluating the derivative
∂h
∂ui = hi(u) +∑
k
uk ∂hk
∂ui
at u = 0, we see that ∂h
∂ui
⏐⏐
u=0 = hi(0). ⊓ ⊔
Proof (Theorem 4.2). Let v : C∞(M)→ R be a linear map satisfying the product
rule (4.2).
Step 1: v vanishes on constants.
By the product rule, applied to the constant function 1 = 1· 1, we have v(1) = 0.
Thus v vanishes on constants.
Step 2: If f 1 = f2 on some open neighborhood U of p, then v ( f1) = v( f2).
Equivalently, letting f = f1− f2, we show that v( f ) = 0 if f = 0 on U. Choose
a ‘bump function’χ∈ C∞(M) with χ(p) = 1, with χ|M\U = 0. Then f χ = 0. The
product rule tells us that
0 = v( f χ) = v( f )χ(p) +v(χ) f (p) = v( f ).
Step 3: If f (p) = g(p) = 0, then v( f g) = 0.
2 It is a well-known fact from calculus (proved e.g. by using Taylor’s theorem with remainder) that
if f is a smooth function of a real variablex, then the functiong, deﬁned as g(x) = x−1( f (x)− f (0))
for x⁄= 0 and g(0) = f′(0), is smooth.

4.1 Tangent spaces 75
This is immediate from the product rule.
Step 4: Let (U, ϕ) be a chart around p, with image ~U = ϕ(U). Then there is
unique linear map ~v : C∞(~U)→ R such that~v(~f ) = v( f ) whenever ~f agrees with
f◦ ϕ−1 on some neighborhood of~p.
Given ~f , we can always ﬁnd a function f such that ~f agrees with f◦ ϕ−1 on
some neighborhood of ~p. Given another such function f′, it follows from Step 2
that v( f ) = v( f′).
Step 5: In a chart (U, ϕ) around p, the map v : C∞(M)→ R is of the form (4.1).
Since the condition (4.1) does not depend on the choice of chart around p, we
may assume that ~p = ϕ(p) = 0, and that ~U is an open ball of some radius R > 0
around 0. Deﬁne ~v as in Step 4. Since v satisﬁes the product rule on C∞(M), the
map~v satisﬁes the product rule on C∞(~U). Given f∈ C∞(M), consider the Taylor
expansion of the coordinate expression ˜f = f◦ ϕ−1 near u = 0:
˜f (u) = ~f (0) +∑
i
ui ∂ ˜f
∂ui
⏐⏐⏐
u=0
+ ˜r(u)
The remainder term ˜r is a smooth function that vanishes at u = 0 together with its
ﬁrst derivatives. By Lemma 4.2, it can be written in the form ˜r(u) = ∑i ui ˜ri(u) where
˜ri are smooth functions that vanish at 0. Let us now apply ~v to the formula for ~f .
Since~v vanishes on products of functions vanishing at 0 (by Step 3), we have that
~v(~r) = 0. Since it also vanishes on constants (by Step 1), we obtain
v( f ) =~v(~f ) = ∑
i
ai ∂ ˜f
∂ui
⏐⏐⏐
u=0
,
where we put ai =~v(ui).
To summarize, we have the following alternative deﬁnition of tangent spaces:
Deﬁnition 4.3 (Tangent spaces – third deﬁnition). The tangent space TpM is the
space of linear maps C∞(M)→ R satisfying the product rule,
v( f g) = f (p)v(g) +v( f )g(p)
for all f ,g∈ C∞(M).
At ﬁrst sight, this characterization may seem a bit less intuitive then the deﬁni-
tion as directional derivatives along curves. But it has the advantage of being less
redundant – a tangent vector may be represented by many curves. Also, as in the co-
ordinate deﬁnition it is immediate that TpM is a linear subspace of the vector space
L(C∞(M), R). One may still want to use local charts, however, to prove that this
vector subspace has dimension equal to the dimension of M.
The following remark gives yet another characterization of the tangent space.
Please read it only if you like it abstract – otherwise skip this!

76 4 The tangent bundle
Remark 4.2 (A fourth deﬁnition). There is a fourth deﬁnition of TpM, as follows.
For any p∈ M, let C∞
p (M) denotes the subspace of functions vanishing at p, and let
C∞
p (M)2 consist of ﬁnite sums ∑i fi gi where fi,gi∈ C∞
p (M). We have a direct sum
decomposition
C∞(M) = R⊕C∞
p (M),
where R is regarded as the constant functions. Since any tangent vectorv : C∞(M)→
R vanishes on constants, v is effectively a mapv : C∞
p (M)→ R. By the product rule,
v vanishes on the subspace C∞
p (M)2⊆ C∞
p (M). Thus v descends to a linear map
C∞
p (M)/C∞
p (M)2→ R, i.e. an element of the dual space (C∞
p (M)/C∞
p (M)2)∗. The
map
TpM→ (C∞
p (M)/C∞
p (M)2)∗
just deﬁned is an isomorphism, and can therefore be used as a deﬁnition of TpM.
This may appear very fancy on ﬁrst sight, but really just says that a tangent vector
is a linear functional on C∞(M) that vanishes on constants and depends only on
the ﬁrst order Taylor expansion of the function at p. Furthermore, this viewpoint
lends itself to generalizations which are relevant to algebraic geometry and non-
commutative geometry: The ‘vanishing ideals’ C∞
p (M) are the maximal ideals in
the algebra of smooth functions, with C∞
p (M)2 their second power (in the sense of
products of ideals). Thus, for any maximal ideal I in a commutative algebra A
one may regard (I /I 2)∗ as a ‘tangent space’.
After this lengthy discussion of tangent spaces, observe that the velocity vectors
of curves are naturally elements of the tangent space. Indeed, let J⊆ R be an open
interval, and γ∈ C∞(J,M) a smooth curve. Then for any t0∈ J, the tangent (or
velocity) vector
˙γ(t0)∈ Tγ(t0)M.
at time t0 is given in terms of its action on functions by
( ˙γ(t0))( f ) = d
dt
⏐⏐⏐
t=t0
f (γ(t))
We will also use the notation dγ
dt (t0) or dγ
dt|t0 to denote the velocity vector.
4.2 Tangent map
4.2.1 Deﬁnition of the tangent map, basic properties
For smooth maps F∈ C∞(U,V ) between open subsets U⊆ Rm and V⊆ Rn of
Euclidean spaces, and any given p∈ U, we considered the derivative to be the linear
map
DpF : Rm→ Rn, a↦→ d
dt
⏐⏐⏐
t=0
F(p +ta).

4.2 Tangent map 77
The following deﬁnition generalizes the derivative to smooth maps between mani-
folds.
Deﬁnition 4.4. Let M,N be manifolds and F∈ C∞(M,N). For any p∈ M, we deﬁne
the tangent map to be the linear map
TpF : TpM→ TF(p)N
given by (
TpF(v)
)
(g) = v(g◦ F)
for v∈ TpM and g∈ C∞(N).
We leave it as an exercise to check that the right hand side does indeed deﬁne a
tangent vector:
Exercise: Show that for all v∈ TpM, the map g↦→ v(g◦F) satisﬁes the product rule
at q = F(p), hence deﬁnes an element of TqN.
Proposition 4.1. If v∈ TpM is represented by a curve γ : J→ M, then (TpF)(v) is
represented by the curve F◦ γ.
Proof. For g∈ C∞(N),
TpF(v)(g) = v(g◦ F) = d
dt
⏐⏐⏐
t=0
(g◦ F)(γ(t)) = d
dt
⏐⏐⏐
t=0
g
(
(F◦ γ)(t)
)
.
This shows that TpF(v) is represented by F◦ γ : R→ N.
Remark 4.3 (Pull-backs, push-forwards). For smooth maps F∈ C∞(M,N), one can
consider various ‘pull-backs’ of objects onN to objects on M, and ‘push-forwards’
of objects on M to objects on N. Pull-backs are generally denoted by F∗, push-
forwards by F∗. For example, functions on N pull back
g∈ C∞(N) ↝ F∗g = g◦ F∈ C∞(M).
Curves push on M forward:
γ : J→ M ↝ F∗γ = F◦ γ : J→ N.
Tangent vectors to M also push forward,
v∈ TpM ↝ F∗(v) = (TpF)(v).
The deﬁnition of the tangent map can be phrased in these terms as (F∗v)(g) =
v(F∗g). Note also that if v is represented by the curve γ, then F∗v is represented
by the curve F∗γ.
Proposition 4.2 (Chain rule). Let M ,N,Q be manifolds. Under composition of
maps F∈ C∞(M,N) and F′∈ C∞(N,Q),

78 4 The tangent bundle
Tp(F′◦ F) = TF(p)F′◦ TpF.
Proof. Let v∈ TpM be represented by a curve γ. Then both Tp(F′◦ F)(v) and
TF(p)F′(TpF(v)) are represented by the curve F′◦ (F◦ γ) = (F′◦ F)◦ γ. ⊓ ⊔
Exercise: a) Show that the tangent map of the identity map idM : M→ M at p∈ M
is the identity map on the tangent space:
Tp idM = idTpM.
b) Show that if F∈ C∞(M,N) is a diffeomorphism, then TpF is a linear isomor-
phism, with inverse
(TpF)−1 = (TF(p)F−1).
4.2.2 Coordinate description of the tangent map
To get a better understanding of the tangent map, let us ﬁrst consider the spacial
case that F∈ C∞(U,V ) is a smooth map between open subsetsU⊆ Rm and V⊆ Rn.
For p∈ U, the tangent space TpU is canonically identiﬁed with Rm, using the basis
∂
∂x1
⏐⏐⏐
p
, . . . , ∂
∂xm
⏐⏐⏐
p
∈ TpU
of the tangent space. Similarly,TF(p)V∼= Rn, using the basis given by partial deriva-
tives ∂
∂y j|F(p). Using this identiﬁcations, the tangent map becomes a linear map
TpF : Rm→ Rn, i.e. it is given by an n× m-matrix. This matrix is exactly the
Jacobian:
Proposition 4.3. Let F∈ C∞(U,V ) is a smooth map between open subsets U⊆ Rm
and V⊆ Rn. For all p∈ M, the tangent map TpF is just the derivative (i.e., Jacobian
matrix) DpF of F at p.
Proof. For g∈ C∞(V ), we calculate
(
(TpF)
( ∂
∂xi
⏐⏐⏐
p
))
(g) = ∂
∂xi
⏐⏐⏐
p
(g◦ F)
=
n
∑
j=1
∂g
∂y j
⏐⏐⏐
F(p)
∂F j
∂xi
⏐⏐⏐
p
=
( n
∑
j=1
∂F j
∂xi
⏐⏐⏐
p
∂
∂y j
⏐⏐⏐
F(p)
)
(g).
This shows
(TpF)
( ∂
∂xi
⏐⏐⏐
p
)
=
n
∑
j=1
∂F j
∂xi
⏐⏐⏐
p
∂
∂y j
⏐⏐⏐
F(p)
.

4.2 Tangent map 79
Hence, in terms of the given bases of TpU and TF(p)V , the matrix of the linear map
TpF has entries ∂F j
∂xi
⏐⏐⏐
p
.
Remark 4.4. For F∈ C∞(U,V ), it is common to write y = F(x), and accordingly
write ( ∂y j
∂xi )i, j for the Jacobian. In these terms, the derivative reads as
TpF
( ∂
∂xi
⏐⏐⏐
p
)
= ∑
j
∂y j
∂xi
⏐⏐⏐
p
∂
∂y j
⏐⏐⏐
F(p)
.
This formula is often used for explicit calculations.
For a general smooth map F∈ C∞(M,N), we obtain a similar description once
we pick coordinate charts. Given p∈ M, choose charts (U, ϕ) around p and (V, ψ)
around F(p), with F(U)⊆ V . Let ~U = ϕ(U), ~V = ψ(V ), and put
~F = ψ◦ F◦ ϕ−1 : ~U→~V .
Since the coordinate map ϕ : U→ Rm is a diffeomorphism onto ~U, It gives an
isomorphism
Tpϕ : TpU→ Tϕ(p)~U = Rm.
Similarly, TF(p)ψ gives an isomorphism of TF(p)V with Rn. Note also that since
U⊆ M is open, we have that TpU = TpM. We obtain,
Tϕ(p)~F = TF(p)ψ◦ TpF◦ (Tpϕ)−1.
which may be depicted in a commutative diagram
Rm Dϕ(p)~F
// Rn
TpM = TpU
∼=Tpϕ
OO
TpF
// TF(p)V = TF(p)N
∼= TF(p)ψ
OO
Now that we have recognized TpF as the derivative expressed in a coordinate-
free way, we may liberate some of our earlier deﬁnitions from coordinates:
Deﬁnition 4.5. Let F∈ C∞(M,N).
• The rank of F at p∈ M, denoted rankp(F), is the rank of the linear map TpF.
• F has maximal rank at p if rankp(F) = min(dimM,dimN).
• F is a submersion if TpF is surjective for all p∈ M,
• F is an immersion if TpF is injective for all p∈ M,
• F is a local diffeomorphism if TpF is an isomorphism for all p∈ M.
• p∈ M is a critical point of F is TpF does not have maximal rank at p.
• q∈ N is a regular valueof F if TpF is surjective for all p∈ F−1(q) (in particular,
if q⁄∈ F(M)).

80 4 The tangent bundle
• q∈ N is a singular value if it is not a regular value.
Exercise: Using this new deﬁnitions, show that the compositions of two submer-
sions is again a submersion, and that the composition of two immersions is an im-
mersion.
4.2.3 Tangent spaces of submanifolds
Suppose S⊆ M is a submanifold, and p∈ S. Then the tangent space TpS is canon-
ically identiﬁed as a subspace of TpM. Indeed, since the inclusion i : S ↪→ M is an
immersion, the tangent map is an injective linear map,
Tpi : TpS→ TpM,
and we identify TpS with the subspace given as the image of this map. (Hopefully,
the identiﬁcations are not getting too confusing: S gets identiﬁed with i(S)⊆ M,
hence also p∈ S with its image i(p) in M, and TpS gets identiﬁed with (Tpi)(TpS)⊆
TpM.) As a special case, we see that wheneverM is realized as a submanifold ofRn,
then its tangent spaces TpM may be viewed as subspaces of TpRn = Rn.
Proposition 4.4. Let F∈ C∞(M,N) be a smooth map, having q ∈ N as a regular
value, and let S = F−1(q). For all p∈ S,
TpS = ker(TpF),
as subspaces of TpM.
Proof. Let m = dimM, n = dimN. Since TpF is surjective, its kernel has dimension
m− n. By the normal form for submersions, this is also the dimension of S, hence
of TpS. It is therefore enough to show that TpS⊆ ker(TpF). Letting i : S→ M be he
inclusion, we have to show that
TpF◦ Tpi = Tp(F◦ i)
is the zero map. But F◦ i is a constant map, taking all points of S to the constant
value q∈ N. The tangent map to a constant map is just zero. (See below.) Hence
Tp(F◦ i) = 0. ⊓ ⊔
Exercise: Suppose that F∈ C∞(M,N) is a constant map, that is, F(M) ={q} for
some element q∈ N. Show that TpF = 0 for all p∈ M. (Hint: Use the deﬁnition
of TpF, and observe that for g∈ C∞(N) the pull-back F∗g = g◦ F is a constant
function.)
As a special case, we can describe the tangent spaces to level sets:

4.2 Tangent map 81
Corollary 4.1. Suppose V ⊆ Rn is open, and q ∈ Rk is a regular value of F ∈
C∞(M, Rk), deﬁning an embedded submanifold M = F−1(q). For all p ∈ M, the
tangent space TpM⊆ TpRn = Rn is given as
TpM = ker(TpF)≡ ker(DpF).
Example 4.2. Let F : Rn+1→ R be the map F(x) = x·x = (x0)2 + . . .+ (xn)2. Then,
for all p∈ F−1(1) = Sn,
(DpF)(a) = d
dt
⏐⏐⏐
t=0
F(p +ta) = d
dt
⏐⏐⏐
t=0
(p +ta)· (p +ta) = 2p· a,
hence
TpSn ={a∈ Rn+1| a· p = 0} = span(p)⊥.
As another typical application, suppose that S⊆ M is a submanifold, and f∈
C∞(S) is a smooth function given as the restriction f = h|S of a smooth function
h∈ C∞(M). Consider the problem of ﬁnding the critical points p∈ S of f , that is,
Crit( f ) ={p∈ S| Tp f = 0}.
Letting i : S→ M be the inclusion, we have f = h|S = h◦ i, hence Tp f = Tph◦ Tpi.
It follows that Tp f = 0 if and only ifTph vanishes on the range ofTpi, that is on TpS:
Crit( f ) ={p∈ S| TpS⊆ ker(Tph)}.
If M = Rm, then Tph is just the JacobianDph, whose kernel is sometimes rather easy
to compute – in any case this approach tends to be much faster than a calculation in
charts. Here is a concrete example:
Example 4.3. Problem. Find the critical points of
f : S2→ R, f (x,y,z) = xy.
Solution. Following the strategy outlined above, we write f = h◦ i with h(x,y,z) =
xy. For p = (x,y,z) we have
Tph = Dph = (y x 0),
as a linear map R3→ R. There are two cases: Case 1. Dph = 0, i.e. x = y = 0. This
means p = (0,0,±1). In this case ker (Tph) = R3, which of course contains TpS.
Thus both
(0,0,±1) (4.3)
are critical points of f .
Case 2. Dph⁄= 0. Then

82 4 The tangent bundle
ker(Tph) = span





0
0
1

 ,


x
−y
0




 .
This contains TpS if and only if it is equal to TpS. To check whether the two basis
vectors are in TpS, we just have to check their dot products with p = (x,y,z). This
gives the conditions z = 0 and x2− y2 = 0, which together with x2 + y2 + z2 = 1
leads to the four critical points
(± 1√
2
,± 1√
2
, 0). (4.4)
In summary, the functionF has six critical points, corresponding to two sign choices
in (4.3) and four sign choices in (4.4). ⊓ ⊔
As another application of the same idea, you should try to prove:
Exercise: Let S⊆ R3 be a surface. Show that p∈ S is a critical point of the function
f∈ C∞(S) given by f (x,y,z) = z, if and only if TpS is the x-y-plane.
Example 4.4. Problem. Show that the equations
x2 + y = 0, x2 + y2 + z3 + w4 + y = 1
deﬁne a two dimensional submanifold S of R4, and ﬁnd the equation of the tangent
space at the point (x0,y0,z0,w0) = (−1,−1,−1,−1).
Solution. Let F∈ C∞(R4, R2) be the function
F(x,y,z,w) = (x2 + y, x2 + y2 + z3 + w4 + y).
The Jacobian matrix is ( 2x 1 0 0
2x 2y + 1 3z2 4w3
)
.
Since the ﬁrst row is non-zero, this has rank 2 unless the second row is a scalar
multiple of the ﬁrst row. This is the case if either x⁄= 0 and y = z = w, or x = 0 and
z = w = 0. In particular, x = 0 or y = 0. But if such a point (x,y,z,w) also satisﬁes
the ﬁrst equation for S, that is x2 + y = 0, we see that x,y must both be zero. This
only leaves the point (0,0,0,0), which however does not solve the second equation
x2 +y2 +z3 +w4 +y = 1. This shows thatS is a submanifold of dimension 4−2 = 2.
At (−1,−1,−1,−1) the Jacobian matrix becomes
(
−2 1 0 0
−2−1 3−4
)
;
so the equation of the tangent space TpS = ker(DpF) reads as

4.2 Tangent map 83
(
−2 1 0 0
−2−1 3−4
)


x
y
z
w

 =
(
0
0
)
;
that is,
−2x + y = 0, −2x− y + 3z− 4w = 0.
Example 4.5. We had discussed various matrix Lie groups G as examples of mani-
folds. By deﬁnition, these are submanifolds G⊆ MatR(n), consisting of invertible
matrices with the properties
A,B∈ G⇒ AB∈ G, A∈ G⇒ A−1∈ G.
The tangent space to the identity (group unit) for such matrix Lie groupsG turns out
to be important; it is commonly denoted by lower case fracture letters:
g = TIG.
Some concrete examples:
1. The matrix Lie group
GL(n, R) ={A∈ MatR(n)| det(A)⁄= 0}
of all invertible matrices is an open subset of MatR(n), hence
gl(n, R) = MatR(n)
is the entire space of matrices.
2. For the group O(n), consisting of matrices with F(A) := A⊤A = I, we has com-
puted TAF(X) = X⊤A + AX⊤. For A = I, the kernel of this map is
o(n) ={X∈ MatR(n)| X⊤ =−X}.
3. For the group SL (n, R) ={A∈ MatR(n)| det(A) = 1}, given as the level set
F−1(1) of the function det : Mat R(n)→ R, we calculate
DAF(X) = d
dt
⏐⏐⏐
t=0
F(A+tX ) = d
dt
⏐⏐⏐
t=0
det(A+tX ) = d
dt
⏐⏐⏐
t=0
det(I +tA−1X) = tr(A−1X),
where tr : Mat R(n)→ R is the trace (sum of diagonal entries). (See exercise
below.) Hence
sl(n, R) ={X∈ MatR(n)| tr(X) = 0}.
Exercise: Show that for every X∈ MatR(n),
d
dt
⏐⏐
t=0 det(I +tX ) = tr(X).

84 4 The tangent bundle
(Hint: Use that every matrix is conjugate (i.e., similar) to an upper triangular matrix,
and that both determinant and trace are unchanged under conjugation (i.e., similarity
transformation).)
4.2.4 Example: Steiner’s surface revisited
As we discussed in Section 3.5.4, Steiner’s ‘Roman surface’ is the image of the map
RP2→ R3, (x : y : z)↦→ 1
x2 + y2 + z2 (yz, xz, xy).
(We changed notation from α, β , γ to x,y,z.) At what points p∈ RP2 does this map
have maximal rank (so that the map is an immersion on an open neighborhood
of p?). To investigate this question, one can express the map in local charts, and
compute the resulting Jacobian matrix. However, while this approach is perfectly
ﬁne, the resulting expressions will become rather complicated. A simpler approach
is to consider the composition with the local diffeomorphism π : S2→ RP2, given
as
S2→ R3, (x,y,z)↦→ (yz, xz, xy).
In turn, this map is the restriction F|S2 of the map
F : R3→ R3, (x,y,z)↦→ (yz, xz, xy).
We have Tp(F|S2) = TpF|TpS2, hence ker(Tp(F|S2)) = ker(TpF)∩ TpS2. But TpF =
DpF for p = (x,y,z) is given by the Jacobian matrix
DpF =


0 z y
z 0 x
y x 0

 .
This has determinant det(DpF) = 2xyz, hence its kernel is zero unlessx = 0 or y = 0
or z = 0. If x = 0, thus p = (0,y,z), the matrix simpliﬁes to
DpF =


0 z y
z 0 0
y 0 0

 ,
which (unless both y and z are zero as well) has a 1-dimensional kernel spanned by
column vectors of the form (0,−y,z)⊤. Such a vector is tangent to S2 if and only
if its dot product with p = (0,y,z) is zero, that is, y2 = z2. Since p∈ S2 this means
p = (0,± 1√
2 ,± 1√
2 ). Similarly if y = 0, or if z = 0. We have thus shown: The map
F|S2 has maximal rank at all points of S2, except at the following twelve points:

4.3 The tangent bundle 85
(0,± 1√
2
,± 1√
2
), (± 1√
2
,0,± 1√
2
), (± 1√
2
,± 1√
2
,0).
The kernel of Tp(F|S2) at (0,± 1√
2 ,± 1√
2 ) is the 1-dimensional space spanned by
(0,± 1√
2 ,∓ 1√
2 ) (sign change in the last entry), and similarly for the points where
y = 0 or z = 0. We conclude that the map RP2→ R3 deﬁning Steiner’s surface has
exactly six points where it fails to be an immersion, and we have computed the
kernel of the tangent map at those points.
4.3 The tangent bundle
Proposition 4.5. For any manifold M of dimension m, the tangent bundle
T M =
⨆
p∈M
TpM
(disjoint union of vector spaces) is a manifold of dimension 2m. The map
π : T M→ M
taking v∈ TpM to the base point p, is a smooth submersion, with ﬁbers the tangent
spaces.
Proof. The idea is simple: Take charts for M, and use the tangent map to get charts
for T M. For any open subset U of M, we have
TU =
⨆
p∈U
TpM = π−1(U).
(Note TpU = TpM.) Every chart (U, ϕ) for M, with ϕ : U→ Rm, gives vector space
isomorphisms
Tpϕ : TpM→ Tϕ(p)Rm = Rm
for all p∈ U. The collection of all maps Tpϕ for p∈ U gives a bijection,
T ϕ : TU→ ϕ(U)× Rm, v↦→ (ϕ(p), (Tpϕ)(v))
for v∈ TpU⊆ TU . The image of these bijections are the open subsets subsets
(T ϕ)(TU ) = ϕ(U)× Rm⊆ R2m,
hence they deﬁne charts. We take the collection of all such charts as an atlas forT M:

86 4 The tangent bundle
TU T ϕ
//
π

ϕ(U)× Rm
(u,v)↦→u

U ϕ
// ϕ(U)
We need to check that the transition maps are smooth. If(V, ψ) is another coordinate
chart with U∩V⁄= / 0, the transition map forTU∩ TV = T (U∩V ) = π−1(U∩V ) is
given by,
T ψ◦ (T ϕ)−1 : ϕ(U∩V )× Rm→ ψ(U∩V )× Rm. (4.5)
But Tpψ◦ (Tpϕ)−1 = Tϕ(p)(ψ◦ ϕ−1) is just the derivative (Jacobian matrix) for the
change of coordinates ψ◦ ϕ−1; hence (4.5) is given by
(x,a)↦→
(
(ψ◦ ϕ−1)(x), Dx(ψ◦ ϕ−1)(a)
)
Since the Jacobian matrix depends smoothly on x, this is a smooth map. This shows
that any atlas A ={(Uα , ϕα )} for M deﬁnes an atlas{(TUα ,T ϕα )} for T M. Taking
A to be countable the atlas for T M is countable. The Hausdorff property is easily
checked as well. ⊓ ⊔
Proposition 4.6. For any smooth map F∈ C∞(M,N), the map
T F : T M→ T N
given on TpM as the tangent maps TpF : TpM→ TF(p)N, is a smooth map.
Proof. Given p∈ M, choose charts (U, ϕ) around p and (V, ψ) around F(p), with
F(U)⊆ V . Then (TU ,T ϕ) and (TV,T ψ) are charts for T M and T N, respectively,
with T F(TU )⊆ TV . Let~F = ψ◦ F◦ ϕ−1 : ϕ(U)→ ψ(V ). The map
T~F = T ψ◦ T F◦ (T ϕ)−1 : ϕ(U)× Rm→ ψ(V )× Rn
is given by
(x,a)↦→
(
(~F)(x), Dx(~F)(a)
)
.
It is smooth, by smooth dependence of the differential Dx~F on the base point. Con-
sequently, T F is smooth, ⊓ ⊔

Chapter 5
Vector ﬁelds
5.1 Vector ﬁelds as derivations
A vector ﬁeld on a manifold may be regarded as a family of tangent vectors Xp∈
TpM for p∈ M, depending smoothly on the base points p∈ M. One way of making
precise what is meant by ‘depending smoothly’ is the following.
Deﬁnition 5.1 (Vector ﬁelds – ﬁrst deﬁnition). A collection of tangent vectors
Xp, p∈ M deﬁnes a vector ﬁeld X∈ X∈ M if and only if for all functionsf∈C∞(M)
the function p↦→ Xp( f ) is smooth. The space of all vector ﬁelds on M is denoted
X(M).
We hence obtain a linear map X : C∞(M)→ C∞(M) such that
X( f )|p = Xp( f ). (5.1)
Since each Xp satisfy the product rule (atp), it follows thatX itself satisﬁes a product
rule. We can use this as an alternative deﬁnition:
Deﬁnition 5.2 (Vector ﬁelds – second deﬁnition). A vector ﬁeld on M is a linear
map
X : C∞(M)→ C∞(M)
satisfying the product rule,
X( f g) = X( f )g + f X(g) (5.2)
for f ,g∈ C∞(M).
Remark 5.1. The condition (5.2) says that X is a derivation of the algebra C∞(M)
of smooth functions. More generally, a derivation of an algebra A is a linear map
D : A→ A such that
D(a1a2) = D(a1) a2 + a1 D(a2).
(Appendix 5.8 reviews some facts about derivations.)
87

88 5 Vector ﬁelds
We can also express the smoothness of the tangent vectorsXp in terms of coordi-
nate charts (U, ϕ). Recall that for any p∈ U, and all f∈ C∞(M), the tangent vector
Xp is expressed as
Xp( f ) =
m
∑
i=1
ai ∂
∂ui
⏐⏐⏐
u=ϕ(p)
( f◦ ϕ−1).
The vector a = (a1, . . . ,am)∈ Rm represents Xp in the chart; i.e., (Tpϕ)(Xp) = a
under the identiﬁcation Tϕ(p)ϕ(U) = Rm. As p varies in U, the vector a becomes a
function of p∈ U, or equivalently of u = ϕ(p).
Proposition 5.1. The collection of tangent vectors Xp, p∈ M deﬁne a vector ﬁeld if
and only if for all charts (U, ϕ), the functions ai : ϕ(U)→ R deﬁned by
Xϕ−1(u)( f ) =
m
∑
i=1
ai(u) ∂
∂ui ( f◦ ϕ−1),
are smooth.
Proof. If the ai are smooth functions, then for every f∈ C∞(M) the function X( f )◦
ϕ−1 : ϕ(U)→ R is smooth, and hence X( f )|U is smooth. Since this is true for all
charts, it follows that X( f ) is smooth. Conversely, if X is a vector ﬁeld, and p∈ M
some point in a coordinate chart (U, ϕ), and i∈{ 1, . . . ,m} a given index, choose
f∈ C∞(M) such that f (ϕ−1(u)) = ui. Then X( f )◦ ϕ−1 = ai(u), which shows that
the ai are smooth.
Exercise: In the proof, we used that for any coordinate chart (U, ϕ) around p, one
can choose f∈ C∞(M) such that f◦ ϕ−1 : ϕ(U)→ R coincides with u j near ϕ(p).
Write out the details in the construction of such a function f , using a choice of
‘bump function’.
In particular, we see that vector ﬁelds on open subsets U⊆ Rm are of the form
X = ∑
i
ai ∂
∂xi
where ai∈ C∞(U). Under a diffeomorphism F : U→ V, x↦→ y = F(x), the coordi-
nate vector ﬁelds transform with the Jacobian
T F( ∂
∂xi ) = ∑
j
∂F j
∂xi
⏐⏐⏐
x=F−1(y)
∂
∂y j
Informally, this ‘change of coordinates’ is often written
∂
∂xi = ∑
j
∂y j
∂xi
∂
∂y j .

5.2 Vector ﬁelds as sections of the tangent bundle 89
Here one thinks of the xi and y j as coordinates on the same set, and doesn’t worry
about writing coordinate maps, and one uses the (somewhat sloppy, but convenient)
notation y = y(x) instead of y = F(x).)
Example 5.1. Problem. Express the coordinate vector ﬁelds ∂
∂x , ∂
∂y in polar coordi-
nates, given by
x = r cos θ , y = r sin θ
(valid for r > 0 and−π < θ < π).
Solution. We have
∂
∂r = ∂x
∂r
∂
∂x + ∂y
∂r
∂
∂y = cos θ ∂
∂x + sin θ ∂
∂y
and similarly
∂
∂ θ = ∂x
∂ θ
∂
∂x + ∂y
∂ θ
∂
∂y =−r sin θ ∂
∂x + r cos θ ∂
∂y .
The matrix of coefﬁcients is of course the Jacobian. Inverting this matrix
(
cos θ sin θ
−r sin θ r cos θ
)−1
= 1
r
(
r cos θ−sin θ
r sin θ cos θ
)
(in other words, solving the equations for ∂
∂x and ∂
∂y) we obtain
∂
∂x = cos θ ∂
∂r− 1
r sin θ ∂
∂ θ ,
∂
∂y = sin θ ∂
∂r + 1
r cos θ ∂
∂ θ .
5.2 Vector ﬁelds as sections of the tangent bundle
The ‘best’ way of describing the smoothness ofp↦→ Xp is that it is literally a smooth
map into the tangent bundle.
Deﬁnition 5.3 (Vector ﬁelds – third deﬁnition). A vector ﬁeld on M is a smooth
map X∈ C∞(M,T M) such that π◦ X is the identity.
It is common practice to use the same symbol X both as a linear map from smooth
functions to smooth functions, or as a map into the tangent bundle. Thus
X : M→ T M, X : C∞(M)→ C∞(M)
coexist. But if it gets too confusing, one uses a symbol

90 5 Vector ﬁelds
LX : C∞(M)→ C∞(M)
for the interpretation as a derivation; here the L stands for ‘Lie derivative’ (named
after Sophus Lie). Both viewpoints are useful and important, and both have their
advantages and disadvantages. For instance, from (A) it is immediate that vector
ﬁelds on M restrict to open subsets U⊆ M; this map
X(M)→ X(U), X↦→ X|U
may seem a little awkward from viewpoint (B) since C∞(U) is not a subspace of
C∞(M). (There is a restriction map C∞(M)→ C∞(U), but no natural map in the
other direction.) On the other hand, (B) gives the Lie bracket operation discussed
below, which seems unexpected from viewpoint (A).
5.3 Lie brackets
Let M be a manifold. Given vector ﬁelds X,Y : C∞(M)→ C∞(M), the composition
X◦Y is not a vector ﬁeld: For example, if X = Y = ∂
∂x as vector ﬁelds on R, then
X◦ Y = ∂ 2
∂x2 is a second order derivative, which is not a vector ﬁeld (it does not
satisfy the Leibnitz rule). However, the commutator turns out to be a vector ﬁeld:
Theorem 5.1. For any two vector ﬁelds X,Y∈ X(M) (regarded as derivations), the
commutator
[X,Y ] := X◦Y−Y◦ X : C∞(M)→ C∞(M)
is again a vector ﬁeld.
Proof. To check that [X,Y ] is a vector ﬁeld, we verify the derivation property, by
direct calculation. We have that
(X◦Y )( f1 f2) = X
(
Y ( f1) f2 + f1Y ( f2)
)
= X(Y ( f1)) f2 + f1 X(Y ( f2)) +X( f1)Y ( f2) +Y ( f1)X( f2);
subtracting a similar expression with 1 and 2 interchanged, some terms cancel, and
we obtain
[X,Y ]( f1 f2) = X(Y ( f1)) f2 + f1 X(Y ( f2))− X(Y ( f2)) f1 + f2 X(Y ( f1))
= [X,Y ]( f1) f2 + f1 [X,Y ]( f2)
as required.
Remark 5.2. A similar calculation applies to derivations of algebras in general: The
commutator of two derivations is again a vector ﬁeld.
Deﬁnition 5.4. The vector ﬁeld

5.3 Lie brackets 91
[X,Y ] := X◦Y−Y◦ X
is called the Lie bracket of X,Y∈ X(M).
It is instructive to see how this works in local coordinates. For open subsetsU⊆ Rm,
if
X =
m
∑
i=1
ai ∂
∂xi , Y =
m
∑
i=1
bi ∂
∂xi ,
with coefﬁcient functions ai,bi∈ C∞(U), the composition X◦Y is a second order
differential operators on functions f∈ C∞(U):
X◦Y =
m
∑
i=1
m
∑
j=1
a j ∂bi
∂x j
∂
∂xi +
m
∑
i=1
m
∑
j=1
aib j ∂ 2
∂xi∂x j
Subtracting a similar expression for Y◦ X, the terms involving second derivatives
cancel, and we obtain
[X,Y ] =
m
∑
i=1
m
∑
j=1
(
a j ∂bi
∂x j− b j ∂ai
∂x j
) ∂
∂xi .
(This calculation applies to general manifolds, by taking local coordinates.) The
signiﬁcance of the Lie bracket will become clear later. At this stage, let us give
some examples.
Example 5.2. Consider the following two vector ﬁelds on R2,
X = ∂
∂x , Y = (1 + x2) ∂
∂y .
We have
X◦Y = (1 + x2) ∂ 2
∂x∂y + 2x ∂
∂y , Y◦ X = (1 + x2) ∂ 2
∂y∂x .
Both a second order differential operators. Taking the difference, the second order
derivatives cancel, due to the equality of mixed partials. We obtain
[X,Y ] = 2x ∂
∂y .
Note that the vector ﬁelds X,Y are linearly independent everywhere. Is it possible to
introduce coordinates (u,v) = ϕ(x,y), such that in the new coordinates, these vector
ﬁelds are the coordinate vector ﬁelds ∂
∂u , ∂
∂v? The answer is no: the coordinate
vector ﬁelds have zero Lie bracket
[ ∂
∂u , ∂
∂v ] = 0,

92 5 Vector ﬁelds
(they ‘commute’), but[X,Y ]⁄= 0.
Example 5.3. Consider the following two vector ﬁelds on R2, on the open subset
where xy > 0,
X = x
y
∂
∂x + ∂
∂y , Y = 2√xy ∂
∂x
Indicating second order derivatives by dots we have
X◦Y =
(x
y
√y
x +
√x
y
) ∂
∂x + . . .= 2
√x
y
∂
∂x + . . .
Y◦ X = 2
√x
y
∂
∂x + . . . .
Thus, [X,Y ] = X◦Y−Y◦ X = 0. Can one introduce coordinates u,v in which these
vector ﬁelds become the coordinate vector ﬁelds? This time, the answer is yes: De-
ﬁne a change of coordinates u,v by putting x = uv2, y = u. Then
∂
∂u = ∂x
∂u
∂
∂x + ∂y
∂u
∂
∂y = v2 ∂
∂x + ∂
∂y = x
y
∂
∂x + ∂
∂y = X,
∂
∂v = ∂x
∂v
∂
∂x + ∂y
∂v
∂
∂y = 2uv ∂
∂x = 2√xy ∂
∂x = Y,
Note: When calculating Lie brackets X◦Y−Y◦ X of vector ﬁelds X,Y in local
coordinates, it is not necessary to work out the second order derivatives – we know
in advance that these are going to cancel out! This is why we indicated second order
derivatives by “. . .” in the calculation above.
Example 5.4. Consider the same problem for the vector ﬁelds
X = x ∂
∂y− y ∂
∂x , Y = x ∂
∂x + y ∂
∂y .
This time, we may verify that [X,Y ] = 0. Introduce polar coordinates,
x = r cos θ , y = r sin θ .
(this is a well-deﬁned coordinate chart for r > 0 and−π < θ < π). We have 1
∂
∂r = ∂x
∂r
∂
∂x + ∂y
∂r
∂
∂y = 1
r Y
and
1 In the following, we are using somewhat sloppy notation. Given(θ ,r) = ϕ(x,y), we should more
properly write ϕ∗X, ϕ∗Y for the vector ﬁelds in the new coordinates.

5.3 Lie brackets 93
∂
∂ θ = ∂x
∂ θ
∂
∂x + ∂y
∂ θ
∂
∂y = X
Hence X = ∂
∂ θ , Y = r ∂
∂r . To get this into the desired form, we make another change
of coordinates ρ = f (r) in such a way that Y becomes ∂
∂ ρ . Since
∂
∂r = ∂ ρ
∂r
∂
∂ ρ = f′(r) ∂
∂ ρ
we want f′(r) = 1
r , thus f (r) = ln(r). So, r = eρ. Hence, the desired change of
coordinates is
x = eρ cos θ , y = eρ sin θ .
Let S⊆ M be a submanifold. A vector ﬁeld X∈ X(M) is called tangent to S if for
all p∈ S, the tangent vector Xp lies in TpS⊆ TpM. (Thus X restricts to a vector ﬁeld
X|S∈ X(S).)
Example 5.5. The three vector ﬁelds
X = y ∂
∂z− z ∂
∂y , Y = z ∂
∂x− x ∂
∂z , Z = x ∂
∂y− y ∂
∂x
on R3 are tangent to the 2-sphere S2: For example, under the identiﬁcation TpR3 =
R3, for p = (x,y,z), each of
Xp = (0,−z,y), Yp = (z,0,−x), Zp = (−y,x,0)
have zero dot product with p. The bracket of any two of X,Y,Z is again tangent; in
fact we have
[X,Y ] = Z, [Y,Z] = X, [Z,X] = Y.
More generally, we have:
Proposition 5.2. If two vector ﬁelds X,Y∈ X(M) are tangent to a submanifold S⊆
M, then their Lie bracket is again tangent to S.
Proposition 5.2 can be proved by using the coordinate expressions of X,Y in sub-
manifold charts. But we will postpone the proof for now since there is a much
shorter, coordinate-independent proof, see the next section.
Example 5.6. Consider the vector ﬁelds on R3,
X = ∂
∂x , Y = ∂
∂y + x ∂
∂z .
We have
[X,Y ] = ∂
∂z;

94 5 Vector ﬁelds
hence Xp, Yp, Zp are a basis of R3 for all p∈ R3. In particular, there cannot exist a
surface S⊆ R3 such that both X and Y are tangent to S.
5.4 Related vector ﬁelds
Deﬁnition 5.5. Let F∈ C∞(M,N) be a smooth map. Vector ﬁelds X∈ X(M) and
Y∈ X(N) are called F-related, written as
X∼F Y,
if
TpF(Xp) = YF(p)
for all p∈ M.
Example 5.7. If F is a diffeomorphism, then X∼F Y if and only if Y = F∗X. In
particular, if N = M, then an equation X∼F X means that X is invariant under F.
Example 5.8. Let S⊆ M be an embedded submanifold and i : S→ M the inclusion.
Let X∈ X(S) and Y∈ X(M). Then
X∼i Y
if and only if Y is tangent to S, with X as its restriction. In particular,
0∼i Y
if and only if Y vanishes along the submanifold S.
Example 5.9. If F : M→ N is a submersion, and X∈ X(M), then X∼F 0 if and
only if X is tangent to the ﬁbers of F.
Example 5.10. Let π : Sn→ RPn be the quotient map. Then X∼π Y if and only if
the vector ﬁeld X is invariant under the transformation F : Sn→ Sn, x↦→− x (that
is, T F◦ X = X◦ F, and with Y the induced vector ﬁeld on the quotient.
The F-relation of vector ﬁelds also has a simple interpretation in terms of the
‘differential operator’ picture.
Proposition 5.3. One has X∼F Y if and only if for all g∈ C∞(N),
X(g◦ F) = Y (g)◦ F.
In terms of the pull-back notation, with F∗g = g◦ F for g∈ C∞(N), this means
X◦ F∗ = F∗◦Y :

5.4 Related vector ﬁelds 95
C∞(M) X
// C∞(M)
C∞(N)
F∗
OO
Y
// C∞(N)
F∗
OO
Proof. The condition X(g◦ F) = Y (g)◦ F says that
(TpF(Xp))(g) = YF(p)(g)
for all p∈ M. ⊓ ⊔
The key fact concerning related vector ﬁelds is the following.
Theorem 5.2. Let F∈C∞(M,N) For vector ﬁelds X1,X2∈ X(M) and Y1,Y2∈ X(M),
we have
X1∼F Y1, X2∼F Y2⇒ [X1,X2]∼F [Y1,Y2].
Proof. Using the differential operator picture, we have that
[X1,X2](g◦ F) = X1(X2(g◦ F))− X2(X1(g◦ F))
= X1(Y2(g)◦ F)− X2(Y1(g)◦ F)
= Y1(Y2(g))◦ F−Y2(Y1(g))◦ F
= [Y1,Y2](g)◦ F.
⊓ ⊔
Example 5.11. If two vector ﬁelds Y1,Y2 are tangent to a submanifold S⊆ M then
their Lie bracket [Y1,Y2] is again tangent to S, and the Lie bracket of their restriction
is the restriction of the Lie brackets. Indeed, letting Xi be the restrictions, we have
X1∼i Y1, X2∼i Y2 ⇒ [X1,X2]∼i [Y1,Y2].
Similarly, ifY1 is tangent to S and Y2 vanishes along S, then the Lie bracket vanishes
along S. This follows from the above by putting X2 = 0, since [X1,0] = 0.
Exercise. Explore the consequences of Proposition 5.3 for the other examples of
related vector ﬁelds given above.
Exercise. Show that in the description of vector ﬁelds as sections of the tangent
bundle, two vector ﬁelds X∈ X(M), Y∈ X(M) are F-related if and only if the
following diagram commutes:
T M T F // T N
M F
//
X
OO
N
Y
OO

96 5 Vector ﬁelds
5.5 Flows of vector ﬁelds
For any curve γ : J→ M, with J⊆ R an open interval, and any t∈ J, the velocity
vector
˙γ(t)≡ dγ
dt ∈ Tγ(t)M
is deﬁned as the tangent vector, given in terms of its action on functions as
( ˙γ(t))( f ) = d
dt f (γ(t)).
(The dot signiﬁes a t-derivative.) The curve representing this tangent vector for a
given t, in the sense of our earlier deﬁnition, is the shifted curve τ↦→ γ(t + τ).
Equivalently, one may think of the velocity vector as the image of ∂
∂t|t∈ TtJ∼= R
under the tangent map Tt γ:
˙γ(t) = (Tt γ)( ∂
∂t|t ).
Deﬁnition 5.6. Suppose X∈ X(M) is a vector ﬁeld on a manifold M. A smooth
curve γ∈ C∞(J,M), where J⊆ R is an open interval, is called a solution curve to X
if
˙γ(t) = Xγ(t) (5.3)
for all t∈ J.
Geometrically, Equation (5.3) means that at any given time t, the value of X at γ(t)
agrees with the velocity vector to γ at t.
Equivalently, in terms of related vector ﬁelds,
∂
∂t∼γ X.
Consider ﬁrst the case that M = U⊆ Rm. Here curves γ(t) are of the form

5.5 Flows of vector ﬁelds 97
γ(t) = x(t) = (x1(t), . . . ,xm(t)),
hence
˙γ(t)( f ) = d
dt f (x(t)) =
m
∑
i=1
dxi
dt
∂ f
∂xi (x(t)).
That is
˙γ(t) =
m
∑
i=1
dxi
dt
∂
∂xi
⏐⏐⏐
x(t)
.
On the other hand, the vector ﬁeld has the form X = ∑m
i=1 ai(x) ∂
∂xi . Hence (5.3)
becomes the system of ﬁrst order ordinary differential equations,
dxi
dt = ai(x(t)), i = 1, . . . ,m. (5.4)
Example 5.12. The solution curves of the coordinate vector ﬁeld ∂
∂x j are of the form
xi(t) = xi
0, i⁄= j, x j(t) = x j
0 +t.
More generally, if a = (a1, . . . ,am) is a constant function of x (so that X = ∑ai ∂
∂xi is
the constant vector ﬁeld, the solution curves are afﬁne lines,
x(t) = x0 +ta.
Example 5.13. Consider the vector ﬁeld on R2,
X =−y ∂
∂x + x ∂
∂y .
The corresponding differential equation is ˙x =−y, ˙y = x. Its solutions are γ(t) =
(x(t),y(t)), where
x(t) = x0 cos(t)− y0 sin(t), y(t) = y0 cos(t) +x0 sin(t),
for any given (x0,y0)∈ R2.
Example 5.14. Consider the following vector ﬁeld on Rm,
X =
m
∑
i=1
xi ∂
∂xi .

98 5 Vector ﬁelds
The corresponding differential equation is
˙xi = xi(t),
with solution xi(t) = et xi
0, for i = 1, . . . ,m. That is,
x(t) = et x0.
One of the main results from the theory of ODE’s says that for any given initial
condition x(0) = x0, a solution to the system (5.4) exists and is (essentially) unique:
Theorem 5.3 (Existence and uniqueness theorem for ODE’s).Let U⊆ Rm be an
open subset, and a∈ C∞(U, Rm). For any given x 0∈ U, there is an open interval
Jx0⊆ R around 0, and a solution x : Jx0→ U of the ODE
dxi
dt = ai(x(t)), i = 1, . . . ,m
with initial condition x (0) = x0, and which is maximal in the sense that any other
solution to this initial value problem is obtained by restriction to some subinterval
of Jx0.
Thus, Jx0 is the maximal open interval on which the solution is deﬁned. The solution
depends smoothly on initial conditions, in the following sense. For any givenx0, let
Φ(t,x0) be the solution x(t) of the initial value problem with initial condition x0,
that is,
Φ(0,x0) = x0, d
dt Φ(t,x0) = a(Φ(t,x0)).
Theorem 5.4 (Dependence on initial conditions for ODE’s). For a∈ C∞(U, Rm)
as above, the set
J ={(t,x)∈ R×U| t∈ Jx}.
is an open neighborhood of{0}× U in R×U, and the map
Φ : J→ U, (t,x)↦→ Φ(t,x)
is smooth.
In general, the interval Jx0 may be strictly smaller than R, because a solution might
escape to inﬁnity in ﬁnite time.
Examples 5.15. 1. Consider the ODE
˙x = 1
on U = (0,1)⊆ R. Thus a(x) = 1. The solution curves with initial condition
x0∈ U are x(t) = x0 +t, deﬁned for−x0 < t < 1− x0. Thus Jx0 = (−x0,1− x0),
and

5.5 Flows of vector ﬁelds 99
J ={(t,x)|x∈ (0,1), t + x∈ (0,1)}, Φ(t,x) = t + x.
2. Conside the ODE
˙x = x2
on U = R. Here the solution curves escape to inﬁnity in ﬁnite time. The initial
value problem has solutions
x(t) = x0
1−tx0
,
with domain of deﬁnition
Jx0 ={t∈ R| tx0 < 1}.
The set J ={(t,x)|tx < 1} is the region between the two branches of the hy-
perbola tx = 1, and Φ(t,x) = x
1−tx .
3. A similar example, which we leave as an exercise, is
˙x = 1 + x2.
For a general vector ﬁeld X∈ X(M) on manifolds, Equation (5.3) becomes (5.4)
after introduction of local coordinates. In detail: Let(U, ϕ) be a coordinate chart. In
the chart, X becomes the vector ﬁeld
ϕ∗(X) =
m
∑
j=1
a j(u) ∂
∂u j
and ϕ(γ(t)) = u(t) with
˙ui = ai(u(t)).
If a = (a1, . . . ,am) : ϕ(U)→ Rm corresponds to X in a local chart (U, ϕ), then
any solution curve x : J→ ϕ(U) for a deﬁnes a solution curve γ(t) = ϕ−1(x(t))
for X. The existence and uniqueness theorem for ODE’s extends to manifolds, as
follows:
Theorem 5.5 (Solutions of vector ﬁelds on manifolds). Let X∈ X(M) be a vector
ﬁeld on a manifold M. For any given p ∈ M, there is an open interval Jp⊆ R
around 0, and a solution γ : Jp→ M of the initial value problem
˙γ(t) = Xγ(t), γ(0) = p, (5.5)
which is maximal in the sense that any other solution of the initial value problem is
obtained by restriction to a subinterval. The set
J ={(t, p)∈ R× M| t∈ Jp}
is an open neighborhood of{0}× M, and the map
Φ : J→ M, (t, p)↦→ Φ(t, p)

100 5 Vector ﬁelds
such that γ(t) = Φ(t, p) solves the initial value problem (5.5), is smooth.
Proof. Existence and uniqueness of solutions for small times t follows from the
existence and uniqueness theorem for ODE’s, by considering the vector ﬁeld in
local charts. To prove uniqueness even for large timest, let γ : J→ M be a maximal
solution of (5.5) (i.e., a solution that cannot be extended to a larger open interval),
and let γ1 : J1→ M be another solution of the same initial value problem, but with
γ1(t)⁄= γ(t) for some t∈ J, t > 0. (There is a similar discussion if the solution is
different for some t < 0). Then we can deﬁne
b = inf{t∈ J| t > 0, γ1(t)⁄= γ(t)}.
By the uniqueness for small t, we have b > 0. We will get a contradiction in both of
the following cases:
Case 1: γ1(b) = γ(b) =: q. Then both λ1(s) = γ1(b + s) and λ (s) = γ(b + s) are
solutions to the initial value problem
λ (0) = q, ˙λ (s) = Xλ (s);
hence they have to agree for small|s|, and consequently γ1(t), γ(t) have to agree for
t close to b. This contradicts the deﬁnition of b.
Case 2: γ1(b)⁄= γ(b). Using the Hausdorff property ofM, we can choose disjoint
open neighborhoods U of γ(b) and U1 of γ(b1). For t = b− ε with ε > 0 sufﬁciently
small, γ(t)∈ U while γ1(t)∈ U1. But this is impossible since γ(t) = γ1(t) for 0≤
t < b.
The result for ODE’s about the smooth dependence on initial conditions shows,
by taking local coordinate charts, that J contains an open neighborhood of{0}×
M, on which Φ is given by a smooth map. The fact that J itself is open, and the
map Φ is smooth everywhere, follows by the ‘ﬂow property’ to be discussed below.
(We will omit the details of this part of the proof.) ⊓ ⊔
Note that the uniqueness part uses the Hausdorff property in the deﬁnition of
manifolds. Indeed, the uniqueness part may fail for non-Hausdorff manifolds.
Example 5.16. A counter-example is the non-Hausdorff manifold
Y = (R×{ 1})∪ (R×{− 1})/∼,
where∼ glues two copies of the real line along the strictly negative real axis. Let
U± denote the charts obtained as images of R×{± 1}. Let X be the vector ﬁeld on
Y , given by ∂
∂x in both charts. It is well-deﬁned, since the transition map is just the
identity map. Then γ+(t) = π(t,1) and γ−(t) = π(t,−1) are both solution curves,
and they agree for negative t but not for positive t.
Given a vector ﬁeld X, the map Φ : J→ M is called the ﬂow of X. For any
given p, the curve γ(t) = Φ(t, p) is a solution curve. But one can also ﬁx t and
consider the time-t ﬂow,

5.5 Flows of vector ﬁelds 101
Φt (p)≡ Φ(t, p).
It is a smooth map Φt : Ut→ M, deﬁned on the open subset
Ut ={p∈ M| (t, p)∈ J}.
Note that Φ0 = idM.
Intuitively, Φt (p) is obtained from the initial point p∈ M by ﬂowing for time t
along the vector ﬁeld X. One expects that ﬁrst ﬂowing for time t, and then ﬂowing
for time s, should be the same as ﬂowing for timet +s. Indeed one has the following
ﬂow property.
Theorem 5.6 (Flow property). Let X∈ X(M), with ﬂow Φ : J→ M. Let (t2, p)∈
J , and t1∈ R. Then
(t1, Φt2 (p))∈ J⇔ (t1 +t2, p)∈ J ,
and one has
Φt1(Φt2(p)) = Φt1+t2(p).
Proof. Given t2∈ Jp, we consider both sides as functions oft1 = t. Write q = Φt2(p).
We claim that both
t↦→ Φt (Φt2(p)), t↦→ Φt+t2(p)
are maximal solution curves of X, for the same initial condition q. This is clear for
the ﬁrst curve, and follows for the second curve by the calculation, for f∈ C∞(M),
d
dt f (Φt+t2(p)) = d
ds
⏐⏐⏐
s=t+t2
Φs(p) = XΦs(p)( f )
⏐⏐⏐
s=t+t2
= XΦt+t2 (p)( f ).
Hence, the two curves must coincide. The domain of deﬁnition of t↦→ Φt+t2(p) is
the interval Jp, shifted by t2. Hence, t1∈ JΦ(t2,p) if and only if t1 +t2∈ Jp. ⊓ ⊔
We see in particular that for any t, the map Φt : Ut→ M is a diffeomorphism
onto its image Φt (Ut ) = U−t, with inverse Φ−t.
Example 5.17. Let us illustrate the ﬂow property for various vector ﬁelds on R. The
ﬂow property is evident for ∂
∂x with ﬂow Φt (x) = x + t, as well as for x ∂
∂x, with
ﬂow Φt (x) = et x. The vector ﬁeld x2 ∂
∂x has ﬂow Φt (x) = x/(1− tx), deﬁned for
1−tx < 1. We can explicitly verify the ﬂow property:
Φt1(Φt2(x)) = Φt2(x)
1−t1Φt2(x) =
x
1−t2x
1−t1 x
1−t2x
= x
1− (t1 +t2)x = Φt1+t2(x).
Let X be a vector ﬁeld, and J = J X be the domain of deﬁnition for the ﬂow
Φ = ΦX.
Deﬁnition 5.7. A vector ﬁeld X∈ X(M) is called complete if J X = R× M.
Thus X is complete if and only if all solution curves exist for all time.

102 5 Vector ﬁelds
Example 5.18. The vector ﬁeld x ∂
∂x on M = R is complete, but x2 ∂
∂x is incomplete.
A vector ﬁeld may fail to be complete if a solution curve escapes to inﬁnity in
ﬁnite time. This suggests that a vector ﬁelds X that vanishes outside a compact set
must be complete, because the solution curves are ‘trapped’ and cannot escape to
inﬁnity.
Proposition 5.4. If X∈ X(M) is a vector ﬁeld that has compact support, in the sense
that X|M−A = 0 for some compact subset A, then X is complete. In particular, every
vector ﬁeld on a compact manifold is complete.
Proof. By the uniqueness theorem for solution curves γ, and since X vanishes out-
side A, if γ(t0)∈ M− A for some t0, then γ(t) = γ(t0) for all t. Hence, if a solution
curve γ : J→ M has γ(0)∈ A, then γ(t)∈ A for all t. Let Uε⊆ M be the set of
all p such that the solution curve γ with initial condition γ(0) = p exists for|t| < ε
(that is, (−ε, ε)⊆ Jp). By smooth dependence on initial conditions,Uε is open. The
collection of all Uε with ε > 0 covers A, since every solution curve exists for suf-
ﬁciently small time. Since A is compact, there exists a ﬁnite subcover Uε1, . . . ,Uεk.
Let ε be the smallest ofε1, . . . ,εk. ThenUεi⊆ Uε, for all i, and hence A⊆ Uε. Hence,
for any p∈ A we have (−ε, ε)⊆ Jp, that is any solution curve γ(t) starting in A ex-
ists for times|t| < ε. But γ(−ε/2), γ(ε/2)∈ A, hence the solution curve starting at
those points again exist for times < ε. This shows (−3ε/2,3ε/2)⊆ Jp. Continuing
in this way, we ﬁnd that (−ε− Nε/2, ε + Nε/2)⊆ Jp for all N, thus Jp = R for all
p∈ A. For points p∈ M−A, it is clear anyhow thatJp = R, since the solution curves
are constant. ⊓ ⊔
Theorem 5.7. If X is a complete vector ﬁeld, the ﬂow Φt deﬁnes a 1-parameter
group of diffeomorphisms. That is, each Φt is a diffeomorphism and
Φ0 = idM, Φt1◦ Φt2 = Φt1+t2.
Conversely, if Φt is a 1-parameter group of diffeomorphisms such that the map
(t, p)↦→ Φt (p) is smooth, the equation
Xp( f ) = d
dt
⏐⏐⏐
t=0
f (Φt (p))
deﬁnes a complete vector ﬁeld X on M, with ﬂow Φt.
Proof. It remains to show the second statement. Given Φt, the linear map
C∞(M)→ C∞(M), f↦→ d
dt
⏐⏐⏐
t=0
f (Φt (p))
satisﬁes the product rule, hence it is a vector ﬁeld X. Given p∈ M the curve γ(t) =
Φt (p) is an integral curve of X since
d
dt Φt (p) = d
ds
⏐⏐⏐
s=0
Φt+s(p) = d
ds
⏐⏐⏐
s=0
Φs(Φt (p)) = XΦt (p).

5.5 Flows of vector ﬁelds 103
⊓ ⊔
Remark 5.3. In terms of pull-backs, the relation between the vector ﬁeld and its ﬂow
reads as d
dt Φ∗
t ( f ) = Φ∗
t
d
ds
⏐⏐⏐
s=0
Φ∗
s ( f ) = Φ∗
t X( f ).
This identity
d
dt Φ∗
t = Φ∗
t◦ X
as linear maps C∞(M)→ C∞(M) may be viewed as the deﬁnition of the ﬂow.
Example 5.19. Given A∈ MatR(m) let
Φt : Rm→ Rm, x↦→ etAx =
( ∞
∑
j=0
t j
j!A j
)
x
(using the exponential map of matrices). Sincee(t1+t2)A = et1Aet2A, and since (t,x)↦→
etAx is a smooth map, Φt deﬁnes a ﬂow. What is the corresponding vector ﬁeld X?
For any function f∈ C∞(Rm) we calculate,
X( f )(x) = d
dt
⏐⏐⏐
t=0
f (etAx)
= ∑
j
∂ f
∂x j (Ax) j
= ∑
i j
Ai jxi ∂ f
∂x j
showing that
X = ∑
i j
Ai jxi ∂
∂x j .
2
As a special case, taking A to be the identity matrix, we recover the Euler vector
ﬁeld X = ∑i xi ∂
∂xi , and its ﬂow Φt (x) = etx.
Example 5.20. Let X be a complete vector ﬁeld, with ﬂow Φt. For each t∈ R, the
tangent map T Φt : T M→ T M has the ﬂow property,
T Φt1◦ T Φt2 = T (Φt1◦ Φt2) = T (Φt1+t2),
2 Here we wrote the matrix entries for the i-th row and j-th column as Ai j rather than Ai j. That is,
one standard basis vectors ei∈ Rm (written as column vectors), we have A(ei) = ∑ j Ai je j, hence
for x = ∑xiei we get
Ax = ∑
i j
Ai jxie j
from which we read off (Ax) j = ∑i Ai jxi.

104 5 Vector ﬁelds
and the map R× T M→ T M, (t,v)↦→ Φt (v) is smooth (since it is just the restriction
of the map T Φ : T (R× M)→ T M to the submanifold R× T M). Hence, T Φt is a
ﬂow on T M, and therefore corresponds to a complete vector ﬁeldˆX∈ X(T M). This
is called the tangent lift of X.
Proposition 5.5. Let F ∈ C∞(M,N), and X ∈ X(M), Y∈ X(N) complete vector
ﬁelds, with ﬂows ΦX
t , ΦY
t .
X∼F Y ⇔ F◦ ΦX
t = ΦY
t ◦ F for all t .
3
In short, vector ﬁelds are F-related if and only if their ﬂows are F-related.
Proof. Suppose F◦ ΦX
t = ΦY
t ◦ F for all t. For g∈ C∞(N), and p∈ M, taking a
t-derivative of
g(F(ΦX
t (p))) = g(ΦY
t (F(p)))
at t = 0 on both sides, we get
(
TpF(Xp)
)
(g) = YF(p)(g)
i.e. TpF(Xp) = YF(p). Hence X∼F Y . Conversely, supposeX∼F Y . As we had seen,
if γ : J→ M is a solution curve for X, with initial condition γ(0) = p then F◦ γ :
J→ M is a solution curve for Y , with initial condition F(p). That is, F(ΦX
t (p)) =
ΦY
t (F(p)), or F◦ ΦX
t = ΦY
t ◦ F. ⊓ ⊔
5.6 Geometric interpretation of the Lie bracket
For any smooth map F∈ C∞(M,N) we deﬁned the pull-back
F∗ : C∞(N)→ C∞(M), g↦→ g◦ F.
If F is a diffeomorphism, then we can also pull back vector ﬁelds:
F∗ : X(N)→ X(M), Y↦→ F∗Y,
by the condition (F∗Y )(F∗g) = F∗(Y (g)) for all functions g. That is, F∗Y∼F Y , or
in more detail
(F∗Y )p = (TpF)−1YF(p).
By Theorem 5.2, we have F∗[X,Y ] = [F∗X,F∗Y ].
Any complete vector ﬁeld X∈ X(M) with ﬂow Φt gives rise to a families of
pull-back maps
3 This generalizes to possibly incomplete vector ﬁelds: The vector ﬁelds are related if and only if
F◦ Φ = Φ◦ (idR× F). But for simplicity, we only consider the complete case.

5.6 Geometric interpretation of the Lie bracket 105
Φ∗
t : C∞(M)→ C∞(M), Φ∗
t : X(M)→ X(M).
The Lie derivative of a function f with respect to X is the function
LX ( f ) = d
dt
⏐⏐⏐
t=0
Φ∗
t f ;
thus LX ( f ) = X( f ). The Lie derivative measures how f changes in the direction of
X. Similarly, for a vector ﬁeld Y one deﬁnes the Lie derivative LX (Y ) by
LX (Y ) = d
dt
⏐⏐⏐
t=0
Φ∗
t Y∈ X(M).
The deﬁnition of Lie derivative also works for incomplete vector ﬁelds, since the
deﬁnition only involves derivatives at t = 0. The Lie derivative measures how Y
changes in the direction of X. Note that
(Φ∗
t Y )p = (TpΦ−1
t ) YΦt (p);
that is, we use the inverse to the tangent map of the ﬂow ofX to move YΦt (p) to p. If
Y were invariant under the ﬂow of X, this would agree with Yp; hence (Φ∗
t Y )p−Yp
measures how Y fails to be Φt-invariant. LXY is the inﬁnitesimal version of this. As
we will see below, the inﬁnitesimal version actually implies the global version.
Theorem 5.8. For any X,Y∈ X(M), the Lie derivative LXY is just the Lie bracket:
LX (Y ) = [X,Y ].
Proof. Let Φt = ΦX
t be the ﬂow of X. For all f∈ C∞(M) we obtain, by taking the
t-derivative at t = 0 of both sides of
Φ∗
t (Y ( f )) = (Φ∗
t Y )(Φ∗
t f ),
that
X(Y ( f )) =
( d
dt
⏐⏐⏐
t=0
Φ∗
t Y
)
( f ) +Y
( d
dt
⏐⏐⏐
t=0
Φ∗
t f
)
= (LXY )( f ) +Y (X( f )).
That is, LXY = X◦Y−Y◦ X = [X,Y ]. ⊓ ⊔
Thus, the Lie bracket [X,Y ] measures ‘inﬁnitesimally’ how the vector ﬁeld Y
changes along the ﬂow of X. Note that in particular, LXY is skew-symmetric in
X and Y – this is not obvious from the deﬁnition.
One can also interpret the Lie bracket as measuring how the ﬂows ofX and Y fail
to commute.
Theorem 5.9. Let X,Y be complete vector ﬁelds, with ﬂows Φt ,Ψs. Then
[X,Y ] = 0⇔ Φ∗
t Y = Y for all t
⇔ Ψ∗
s X = X for all s

106 5 Vector ﬁelds
⇔ Φt◦Ψs = Ψs◦ Φt for all s,t.
Proof. The calculation
d
dt (Φt )∗Y = (Φt )∗LXY = (Φt )∗[X,Y ]
shows that Φ∗
t Y is independent of t if and only if [X,Y ] = 0. Since [Y,X] =−[X,Y ],
interchanging the roles of X,Y this is also equivalent to Ψ∗
s X being independent of
s. The property Φ∗
t Y = Y means that Y is Φt-related to itself, hence it takes the ﬂow
of Ψs to itself, that is
Φt◦Ψs = Ψs◦ Φt .
Conversely, if this equation holds then Φ∗
t (Ψ∗
s f ) = Ψ∗
s (Φ∗
t f ) for all f∈ C∞(M).
Differentiating with respect to s at s = 0, we obtain
Φ∗
t (Y ( f )) = Y (Φ∗
t f ).
Hence Φ∗
t (Y ) = Y . Differentiating with respect to t at t = 0, we get that [X,Y ] = 0.
⊓ ⊔
Example 5.21. If X = ∂
∂y as a vector ﬁeld on R2, then [X,Y ] = 0 if and only if Y is
invariant under translation in the y-direction.
Example 5.22. The vector ﬁelds X = x ∂
∂y− y ∂
∂x and Y = x ∂
∂x + y ∂
∂y commute. This
is veriﬁed by direct calculation but can also be ‘seen’ in the following picture
The ﬂow of X is rotations around the origin, but Y is invariant under rotations.
Likewise, the ﬂow of Y is by dilations away from the origin,, but X is invariant
under dilations.
Aside from being skew-symmetric [X,Y ] =−[Y,X], the Lie bracket of vector
ﬁelds satisﬁes the important Jacobi identity.
Proposition 5.6. The Lie bracket of vector ﬁelds satisﬁes the Jacobi identity
[X, [Y,Z]] + [Y, [Z,X]] + [Z, [X,Y ]] = 0.
Proof. This may be proved ‘by hand’, expanding the deﬁnition of the Lie bracket
[X,Y ] = X◦Y−Y◦ X. Each summand gives rise to 4 terms, hence there are alto-
gether 12 terms. Each of the 3!= 6 orderings of X,Y,Z appears twice, with opposite

5.7 Frobenius theorem 107
signs. For example, the termY◦Z◦X appears with coefﬁcient−1 in [X, [Y,Z]], with
coefﬁcient +1 in [Y, [Z,X]], with coefﬁcient 0 in [Z, [X,Y ]]. ⊓ ⊔
The identity may be equivalently stated as
[LX ,LY ]Z = L[X,Y ]Z,
or also as a ‘derivation property’
LX [Y,Z] = [LXY,Z] + [Y,LXZ].
This last form gives an ‘explanation’ of the Jacobi identity, as the derivative att = 0
of the identity
Φ∗
t [Y,Z] = [Φ∗
t Y, Φ∗
t Z],
where Φt is the ﬂow of X.
5.7 Frobenius theorem
We saw that for any vector ﬁeld X∈ X(M), there are solution curves through any
given point p∈ M. The image of this curve is an (immersed) submanifold to which
X is everywhere tangent. One might similarly ‘integral surfaces’ for pairs of vector
ﬁelds, and ‘integral submanifolds’ for collections of vector ﬁelds.
Suppose X1, . . . ,Xr are vector ﬁelds on the manifold M, such that the tangent
vectors X1|p, . . . ,Xr|p∈ TpM are linearly independent for allp∈ M. A r-dimensional
submanifold S⊆ M is called an integral submanifold if the vector ﬁelds X1, . . . ,Xr
are all tangent to S.
Suppose that there exists an integral submanifold S through any given point p∈
M. Then each Lie bracket [Xi,Xj]|p∈ TpS, and hence is a linear combination of
X1|p, . . . ,Xr|p. It follows that
[Xi,Xj] =
r
∑
k=1
ck
i jXk (5.6)
for certain (smooth) functions ck
i j.
A bit more generally, consider a sub-bundleE⊆ T M of rank r. Such a subbundle
is called involutive if the Lie bracket of any two sections of E is again a section of
E. For vector ﬁelds Xi as above, the pointwise spans
Ep = span{X1|p, . . . ,Xr|p}
deﬁne a subbundle with this property. Indeed, givenX = ∑m
i=1 aiXi and Y = ∑m
i=1 biXi
with functions ai,bi, the condition (5.6) guarantees that E is involutive. Given any
rank r subbundle E⊆ T M (not necessarily involutive), a submanifold S⊆ M is

108 5 Vector ﬁelds
called an integral submanifold if Ep = TpS for all p∈ S. The following result is due
to F. G. Frobenius. 4
Theorem 5.10 (Frobenius theorem). Let E⊆ T M be a subbundle of rank r. The
following are equivalent:
1. There exists an integral submanifold through every p∈ M.
2. E is involutive.
In fact, if E is involutive, then it is possible to ﬁnd a coordinate chart (U, ϕ) near
any given p, in such a way that the subbundle (T ϕ)(E|U )⊆ T ϕ(U) is spanned by
the ﬁrst r≤ m coordinate vector ﬁelds
∂
∂u1 , . . . , ∂
∂ur .
Proof. The statement is local; hence, by choosing coordinates we may assume M
is an open subset U⊆ Rm, with p = (0,0). In particular, the tangent spaces are all
identiﬁed with Rm. By re-indexing the coordinates, we may assume that Ep∩ (0⊕
Rm−r) = 0. It is convenient to denote the ﬁrst r coordinates by x1, . . . ,xr and the
remaining coordinates by y1, . . . ,ym−r. Thus Ep projects isomorphically onto the
coordinate subspace spanned by x1, . . . ,xr. Taking U smaller if necessary, we may
assume that this remains true for all points in U. Then E is spanned by vector ﬁelds
of the form
Xi = ∂
∂xi +
m−r
∑
j=1
a j
i (x,y) ∂
∂y j .
We claim that the Xi commute. Indeed, since [Xi,Xj] takes values in E, it is of the
form ∑k ck
i jXk for some functions ck
i j. By comparing the coefﬁcients in front of ∂
∂xk ,
we see that ck
i j = 0. (Indeed, [Xi,Xj] is a linear combination of vector ﬁelds in the
y-direction.) Thus
[Xi,Xj] = 0.
Since the Xi commute, also their ﬂows Φi,ti commute:
Φi,ti◦ Φ j,t j = Φ j,t j◦ Φi,ti.
4 http://upload.wikimedia.org/wikipedia/en/c/c9/Ferdinand_Georg_Frobenius.jpg

5.7 Frobenius theorem 109
Note also that Φi,ti(x1, . . . ,xr,∗) = ( x1, . . . ,xi + ti, . . . ,xr,∗). (This follows because
Xi is related to ∂
∂xi under projection (x,y)↦→ x.) We deﬁne a change of coordinates
by the equation
(x,y) = κ(u,v) := Φ1,u1◦···◦ Φr,ur (0,v).
(The Jacobian for this change of variables is invertible at (0,0). Indeed, note that
κ(0,v) = (0,v), while κ(u,0) = (u,∗) where∗ indicates some function. This implies
that the Jacobian matrix at (0,0) is upper triangular with 1’s along the diagonal,
hence that its determinant is 1.) In these new coordinated the ﬂow of theXi is simply
addition of ti in the i-th entry. This means that Xi = ∂
∂ui . Each subspace consisting
of elements (u,v) with v = const is an integral submanifold. [MORE DETAILS
NEEDED] ⊓ ⊔
Thus, for any involutive subbundleE⊆ T M, then any p∈ M has an open neigh-
borhood U with a nice decomposition into r-dimensional submanifolds.
One calls such a decomposition (or sometimes the involutive subbundleE itself)
a (local) foliation.
Example 5.23. Let Φ : M→ N be a submersion. Then the subbundle E⊆ T M with
ﬁbers
Ep = ker(TpΦ)⊆ TpM
is an involutive subbundle of rank dimM− dimN. Every ﬁber Φ−1(q) is an integral
submanifold.
Example 5.24. Consider the vector ﬁelds on R3,
X = (y− z) ∂
∂x , Y = ∂
∂y + ∂
∂z .
Away from y = z these are linearly independent. Since [X,Y ] = 0, the Frobenius
theorem tells us there are integral submanifolds. Indeed, for any given C⁄= 0 one
has the integral submanifold given by the equation y− z = C.
Remark 5.4. A foliation gives a decomposition into submanifolds on a neighbor-
hood of any given point. Globally, the integral submanifolds are often only im-
mersed submanifolds, given by immersions i : S→ M with (Tpi)(TpS) = Ep for
all p∈ S. The problem is already present for the foliation deﬁned by a single non-
vanishing vector ﬁeld X = X1: It may happen that a solution curve γ through p gets
arbitrarily close to p for larget; hence one cannot get a submanifold chart atp unless
one restricts the domain of γ.

110 5 Vector ﬁelds
5.8 Appendix: Derivations
A vector ﬁeld on a manifold can be regarded as a derivation of the algebra of smooth
functions.
Let us quickly recall the notion of a derivation.
Deﬁnition 5.8. A derivation of an algebra A is a linear mapD : A→ A satisfying
the product rule
D(a1a2) = D(a1)a2 + a1D(a2).
Remarks 5.5. 1. If dim A < ∞, a derivation is an inﬁnitesimal automorphism of an
algebra. Indeed, let U : R→ End(A), t↦→ Ut be a smooth curve with U0 = I,
such that each Ut is an algebra automorphism. Consider the Taylor expansion,
Ut = I +tD + . . .
here
D = d
dt
⏐⏐⏐
t=0
Ut
is the velocity vector at t = 0. By taking the derivative of the condition
Ut (a1a2) = Ut (a1)Ut (a2)
at t = 0, we get the derivation property for D. Conversely, if D is a derivation,
then
Ut = exp(tD) =
∞
∑
n=0
tn
n!Dn
(using the exponential of a matrix) is a well-deﬁned curve of algebra automor-
phisms. We leave it as an exercise to check the automorphism property; it in-
volves proving the property
Dn(a1a2) = ∑
k
(
n
k
)
Dk(a1) Dn−k(a2)
for all a1,a2∈ A.
If A has inﬁnite dimensions, one may still want to think of derivations D as in-
ﬁnitesimal automorphisms, even though the discussion will run into technical
problems. (For instance, the exponential map of inﬁnite rank endomorphisms is
not well-deﬁned in general.)
2. Any given x∈ A deﬁnes a derivation
D(a) = [x,a] := xa− ax.
(Exercise: Verify that this is a derivation.) These are called inner derivations. If
A is commutative (for example A = C∞(M)) the inner derivations are all trivial.
At the other extreme, for the matrix algebra A = MatR(n), one may show that
every derivation is inner.

5.8 Appendix: Derivations 111
3. If A is a unital algebra, with unit 1 A, then D(1A) = 0 for all derivations D. (This
follows by applying the deﬁning property of derivations to 1A = 1A1A.)
4. Given two derivations D1,D2 of an algebra A, their commutator
[D1,D2] = D1D2− D2D1
is again a derivation. Indeed, if a,b∈ A then
D1D2(ab) = D1
(
D2(a)b + aD2(b)
)
= (D1D2)(a)b + a(D1D2)(b) +D1(a)D2(b) +D2(a)D1(b).
Subtracting a similar expression with 1 ,2 interchanged, one obtains the deriva-
tion property of [D1,D2].
5. If the algebra A is commutative, then the space of derivations is a ‘left-module
over A’. That is, if D is a derivation and x∈ A then a↦→ (xD)(a) := xD (a) is
again a derivation:
(xD)(ab) = x(D(ab)) = x(D(a)b + a(D(b)) = (xD)(a)b + a (xD)(b),
where we used xa = ax.



Chapter 6
Differential forms
6.1 Review: Differential forms on Rm
A differential k-form on an open subset U⊆ Rm is an expression of the form
ω = ∑
i1···ik
ωi1...ikdxi1∧···∧ dxik
where ωi1...ik∈ C∞(U) are functions, and the indices are numbers
1≤ i1 <··· < ik≤ m.
Let Ω k(U) be the vector space consisting of such expressions, with the pointwise
addition. It is convenient to introduce a short hand notation I ={i1, . . . ,ik} for the
index set, and write ω = ∑I ωIdxI with
ωI = ωi1...ik , dxI = dxi1∧···∧ dxik .
Since a k-form is determined by these functionsωI, and since there are m!
k!(m−k)! ways
of picking k-element subsets from {1, . . . ,m}, the space Ω k(U) can be identiﬁed
with vector-valued smooth functions,
Ω k(U) = C∞(U, R
m!
k!(m−k)! ).
The d xI are just formal expressions; at this stage they don’t have any particular
meaning. They are used, however, to deﬁne an associative product operation
Ω k(U)× Ω l(U)→ Ω k+l(U)
by the ‘rule of computation’
dxi∧ dx j =−dx j∧ dxi
113

114 6 Differential forms
for all i, j; in particular d xi∧ dxi = 0. In turn, using the product structure we may
deﬁne the exterior differential
d : Ω k(U)→ Ω k+1(U), d
(
∑
I
ωIdxI
)
=
m
∑
i=1
∑
I
∂ ωI
∂xi dxi∧ dxI. (6.1)
The key property of the exterior differential is the following fact:
Proposition 6.1. The exterior differential satisﬁes
d◦ d = 0,
i.e. ddω = 0 for all ω.
Proof. By deﬁnition,
ddω =
m
∑
j=1
m
∑
i=1
∑
I
∂ 2ωI
∂x j∂xi dx j∧ dxi∧ dxI,
which vanishes by equality of mixed partials ∂ ωI
∂xi∂x j = ∂ ωI
∂x j∂xi . (We have dxi∧ dx j =
−dx j∧ dxi, but the coefﬁcients in front of dxi∧ dx j and dx j∧ dxi are the same.) ⊓ ⊔
Example 6.1. Consider forms on R3.
• The differential of a function f∈ Ω 0(R3) is a 1-form
d f = ∂ f
∂x dx + ∂ f
∂y dy + ∂ f
∂z dz,
with components the gradient
grad f = ∇ f .
• A 1-form ω∈ Ω 1(R3) is an expression
ω = f dx + gdy + hdz
with functions f ,g,h. The differential is
dω =
( ∂g
∂x− ∂ f
∂y
)
dx∧ dy +
( ∂h
∂y− ∂g
∂z
)
dy∧ dz +
( ∂ f
∂z− ∂h
∂x
)
dz∧ dx.
Thinking of the coefﬁcients of ω as the components of a function F = ( f ,g,h) :
U→ R3, we see that the coefﬁcients of dω give the curl of F,
curl(F) = ∇× F.
• Finally, any 2-form ω∈ Ω 2(R3) may be written
ω = a dy∧ dz + b dz∧ dx + c dx∧ dy,

6.2 Dual spaces 115
with A = (a,b,c) : U→ R3. We obtain
dω = ( ∂a
∂x + ∂b
∂y + ∂c
∂z ) dx∧ dy∧ dz;
the coefﬁcient is the divergence
div(A) = ∇· A
The usual properties
curl(grad( f )) = 0, div(curl(F)) = 0
are both special cases of d◦ d = 0.
The support supp(ω)⊆ U of a differential form is the smallest closed subset such
that ω vanishes onU\supp(ω). Suppose ω∈ Ω m(U) is a compactly supported form
of the top degree k = m. Such a differential form is an expression
ω = f dx1∧···∧ dxm
where f∈ C∞(U) is a compactly supported function. One deﬁnes the integral of ω
to be the usual Riemann integral:
∫
U
ω =
∫
Rm
f (x1, . . . ,xm)dx1··· dxm. (6.2)
Note that we can regard ω as a form on all of Rm, due to the compact support
condition.
Our aim is now to deﬁne differential forms on manifolds, beginning with 1-
forms. Even though 1-forms on U⊆ Rm are identiﬁed with functions U→ Rm,
they should not be regarded as vector ﬁelds, since their transformation properties
under coordinate changes are different. In fact, while vector ﬁelds are sections of
the tangent bundle, the 1-forms are sections of its dual, the cotangent bundle. We
will thus begin with a review of dual spaces in general.
6.2 Dual spaces
For any real vector space E, we denote by E∗ = L(E, R) its dual space, consisting
of all linear maps α : E→ R. We will assume thatE is ﬁnite-dimensional. Then the
dual space is also ﬁnite-dimensional, and dim E∗ = dimE. 1 It is common to write
the value of α∈ E∗ on v∈ E as a pairing, using the bracket notation:2
1 For possibly inﬁnite-dimensional vector spaces, the dual space E∗ is not isomorphic to E, in
general.
2 In physics, one also uses the Dirac bra-ket notation⟨α| v⟩ := α(v); here α =⟨α| is the ‘bra’ and
v =|v⟩ is the ‘ket’.

116 6 Differential forms
⟨α,v⟩ := α(v).
Let e1, . . . ,er be a basis of E. Any element of E∗ is determined by its values on
these basis vectors. For i = 1, . . . ,r, let ei∈ E∗ (with upper indices) be the linear
functional such that
⟨ei, e j⟩ = δ i j =
{
0 if i⁄= j,
1 if i = j.
The elements e1, . . . ,er are a basis of E∗; this is called the dual basis. The element
α∈ E∗ is described in terms of the dual bases as
α =
r
∑
j=1
α j e j, α j =⟨α,e j⟩.
Similarly, for vectors v∈ E we have
v =
r
∑
i=1
viei, vi =⟨ei,v⟩.
Notice the placement of indices: In a given summation over i, j, . . ., upper indices
are always paired with lower indices.
Remark 6.1. As a special case, for Rr with its standard basis, we have a canonical
identiﬁcation (Rr)∗ = Rr. For more generalE with dimE < ∞, there is nocanonical
isomorphism between E and E∗ unless more structure is given.
Given a linear map R : E→ F between vector spaces, one deﬁnes the dual map
R∗ : F∗→ E∗
(note the direction), by setting
⟨R∗β , v⟩ =⟨β ,R(v)⟩
for β∈ F∗ and v∈ E. This satisﬁes (R∗)∗ = R, and under the composition of linear
maps,
(R1◦ R2)∗ = R∗
2◦ R∗
1.
In terms of basise1, . . . ,er of E and f1, . . . ,fs of F, and the corresponding dual bases
(with upper indices), a linear map R : E→ F is given by the matrix with entries
Ri j =⟨ f j, R(ei)⟩,
while R∗ is described by the transpose of this matrix (the roles of i and j are re-
versed). Namely,3
3 In bra-ket notation, we have Ri j =⟨ f j|R|ei⟩, and
|Rei⟩ = R|ei⟩ = ∑
j
| f j⟩⟨ f j|R|ei⟩, ⟨R∗( f j)| =⟨( f j)|R =⟨ f j|R|ei⟩⟨ei|

6.3 Cotangent spaces 117
R(ei) =
s
∑
j=1
Ri j f j, R∗( f j) =
r
∑
i=1
Ri j f i.
Thus,
(R∗) j
i = Ri j.
6.3 Cotangent spaces
Deﬁnition 6.1. The dual of the tangent space TpM of a manifold M is called the
cotangent space at p, denoted
T∗
p M = (TpM)∗.
Elements of T∗
p M are called cotangent vectors, or simplycovectors. Given a smooth
map F∈ C∞(M,N), and any p∈ M we have the cotangent map
T∗
p F = (TpF)∗ : T∗
F(p)N→ T∗
p M
deﬁned as the dual to the tangent map.
Thus, a co(tangent) vector at p is a linear functional on the tangent space, as-
signing to each tangent vector at p a number. The very deﬁnition of the tangent
space suggests one such functional: Every function f∈ C∞(M) deﬁnes a linear map,
TpM→ R, v↦→ v( f ). This linear functional is denoted (d f )p∈ T∗
p M.4
Deﬁnition 6.2. Let f∈ C∞(M) and p∈ M. The covector
(d f )p∈ T∗
p M, ⟨(d f )p,v⟩ = v( f ).
is called the differential of f at p .
Lemma 6.1. For F∈ C∞(M,N) and g∈ C∞(N),
d(F∗g)p = T∗
p F((dg)F(p)).
Proof. Check on tangent vectors v∈ TpM,
⟨T∗
p F((dg)F(p)), v⟩ =⟨(dg)F(p)), (TpF)(v)⟩
= ((TpF)(v))(g)
= v(F∗g)
=⟨d(F∗g)p, v⟩.
⊓ ⊔
4 Note that this is actually the same as the tangent map Tp f : TpM→ Tf (p)R = R.

118 6 Differential forms
Consider an open subset U⊆ Rm, with coordinates x1, . . . ,xm. Here TpU∼= Rm,
with basis
∂
∂x1
⏐⏐⏐
p
, . . . , ∂
∂xm
⏐⏐⏐
p
∈ TpU (6.3)
The basis of the dual space T∗
p U, dual to the basis (6.3), is given by the differentials
of the coordinate functions:
(dx1)p, . . . , (dxm)p∈ T∗
p U.
Indeed, ⟨
(dxi)p, ∂
∂x j
⏐⏐⏐
p
⟩
= ∂
∂x j
⏐⏐⏐
p
(xi) = δ i j
as required. For f∈ C∞(M), the coefﬁcients of (d f )p = ∑i⟨(d f )p, ei⟩ei are deter-
mined as ⟨
(d f )p, ∂
∂x j
⏐⏐⏐
p
⟩
= ∂
∂x j
⏐⏐⏐
p
( f ) = ∂ f
∂x j
⏐⏐⏐
p
.
Thus,
(d f )p =
m
∑
i=1
∂ f
∂xi
⏐⏐⏐
p
(dxi)p.
Let U⊆ Rm and V⊆ Rn be open, with coordinates x1, . . . ,xm and y1, . . . ,yn. For
F∈ C∞(U,V ), the tangent map is described by the Jacobian matrix, with entries
(DpF)i
j = ∂F j
∂xi (p)
for i = 1, . . . ,m, j = 1, . . . ,n. We have:
(TpF)( ∂
∂xi
⏐⏐⏐
p
) =
n
∑
j=1
(DpF)i
j ∂
∂y j
⏐⏐⏐
F(p)
,
hence dually
(TpF)∗(dy j)F(p) =
m
∑
i=1
(DpF)i
j (dxi)p. (6.4)
Thought of as matrices, the coefﬁcients of the cotangent map are the transpose of
the coefﬁcients of the tangent map.
6.4 1-forms
Similar to the deﬁnition of vector ﬁelds, one can deﬁne co-vector ﬁelds, more com-
monly known as 1-forms: Collections of covectors αp∈ T∗
p M depending smoothly
on the base point. One approach of making precise the smooth dependence on the
base point is to endow the cotangent bundle

6.4 1-forms 119
T∗M =
⋃
p
T∗
p M.
(disjoint union of all cotangent spaces), and require that the map p↦→ αp is
smooth. The construction of charts on T∗M is similar to that for the tangent bun-
dle: Charts (U, ϕ) of M give cotangent charts (T∗U,T∗ϕ−1) of T∗M, using the
fact that T∗(ϕ(U)) = ϕ(U)× Rm canonically (since ϕ(U) is an open subset of
Rm). Here T∗ϕ−1 : T∗U→ T∗ϕ(U) is the union of inverses of all cotangent maps
T∗
p ϕ : T∗
ϕ(p)ϕ(U)→ T∗
p U. A second approach is observe that in local coordinates,
1-forms are given by expressions ∑i fidxi, and smoothness should mean that the
coefﬁcient functions are smooth.
We will use the following (equivalent) approach.
Deﬁnition 6.3. A 1-form on M is a linear map
α : X(M)→ C∞(M), X↦→ α(X) =⟨α, X⟩,
which is C∞(M)-linear in the sense that
α( f X) = f α(X)
for all f∈ C∞(M), X∈ X(M). The space of 1-forms is denoted Ω 1(M).
Let us verify that a 1-form can be regarded as a collection of covectors:
Lemma 6.2. Let α∈ Ω 1(M) be a 1-form, and p∈ M. Then there is a unique cov-
ector αp∈ T∗
p M such that
α(X)p = αp(Xp)
for all X∈ X(M).
(We indicate the value of the function α(X) at p by a subscript, just like we did for
vector ﬁelds.)
Proof. We have to show thatα(X)p depends only on the value ofX at p. By consid-
ering the difference of vector ﬁelds having the same value at p, it is enough to show
that if Xp = 0, then α(X)p = 0. But any vector ﬁeld vanishing at p can be written
as a ﬁnite sum X = ∑i fiYi where fi∈ C∞(M) vanish at p. 5 By C∞-linearity, this
implies that
α(X) = α(∑
i
fiYi) = ∑
i
fiα(Yi)
vanishes at p. ⊓ ⊔
The ﬁrst example of a 1-form is described in the following deﬁnition.
Deﬁnition 6.4. The exterior differential of a function f∈ C∞(M) is the 1-form
d f∈ Ω 1(M),
5 For example, using local coordinates, we can take the Yi to correspond to ∂
∂xi near p, and the fi
to the coefﬁcient functions.

120 6 Differential forms
deﬁned in terms of its pairings with vector ﬁelds X∈ X(M) as⟨d f , X⟩ = X( f ).
Clearly, df is the 1-form deﬁned by the family of covectors(d f )p. Note that critical
points of f may be described in terms of this 1-form: p∈ M is a critical point of f
if and only if (d f )p = 0.
Similar to vector ﬁelds, 1-forms can be multiplied by functions; hence one has
more general examples of 1-forms as ﬁnite sums,
α = ∑
i
fi dgi
where fi,gi∈ C∞(M).
Let us examine what the 1-forms are for open subsetsU⊆ Rm. Givenα∈ Ω 1(U),
we have
α =
m
∑
i=1
αi dxi
with coefﬁcient functions αi =
⟨
α, ∂
∂xi
⟩
∈ C∞(U). (Indeed, the right hand side takes
on the correct values at any p∈ U, and is uniquely determined by those values.)
General vector ﬁelds on U may be written
X =
m
∑
j=1
X j ∂
∂x j
(to match the notation for 1-forms, we write the coefﬁcients as X i rather than ai, as
we did in the past), where the coefﬁcient functions are recovered as X j =⟨dx j, X⟩.
The pairing of the 1-form α with the vector ﬁeld X is then
⟨α, X⟩ =
m
∑
i=1
αiX i.
Lemma 6.3. Let α : p↦→ αp∈ T∗
p M be a collection of covectors. Then α deﬁnes a
1-form, with
α(X)p = αp(Xp)
for p∈ M, if and only if for all charts (U, ϕ), the coefﬁcient functions for α in the
chart are smooth.
Proof. This is similar to the discussion for vector ﬁelds, and is left as an exercise.
6.5 Pull-backs of function and 1-forms
Recall again that for any manifoldM, the vector spaceC∞(M) of smooth functions is
an algebra, with product the pointwise multiplication. Any smooth mapF : M→ M′
between manifolds deﬁned an algebra homomorphism, called the pull-back

6.5 Pull-backs of function and 1-forms 121
F∗ : C∞(M′)→ C∞(M), f↦→ F∗( f ) := f◦ F.
The fact that this preserves products is the following simple calculation:
(F∗( f )F∗(g))(p) = f (F(p))g(F(p)) = ( f g)(F(p)) = F∗( f g)(p).
Given another smooth map F′ : M′→ M′′ we have
(F′◦ F)∗ = F∗◦ (F′)∗
(note the ordering).
Let F∈ C∞(M,N) be a smooth map. Recall that for vector ﬁelds, there is no
general ‘push-forward’ or ‘pull-back’ operation, unlessF is a diffeomorphism. For
1-forms the situation is better. Indeed, for any p∈ M one has the dual to the tangent
map
T∗
p F = (TpF)∗ : T∗
F(p)N→ T∗
p M.
For a 1-form β∈ Ω 1(N), we can therefore deﬁne
(F∗β )p := (T∗
p F)(βF(p)).
Lemma 6.4. The collection of co-vectors (F∗β )p∈ T∗
p M depends smoothly on p,
deﬁning a 1-form F∗β∈ Ω 1(M).
Proof. By working on local coordinates, we may assume that M is an open subset
U⊆ Rm, and N is an open subset V⊆ Rn. Write
β =
n
∑
j=1
β j(y)dy j.
By (6.4), the pull-back of β is given by
F∗β =
m
∑
i=1
( n
∑
j=1
β j(F(x)) ∂F j
∂xi
)
dxi.
In particular, the coefﬁcients are smooth. ⊓ ⊔
The Lemma shows that we have a well-deﬁned pull-back map
F∗ : Ω 1(N)→ Ω 1(M), β↦→ F∗β .
Under composition of two maps, (F1◦ F2)∗ = F∗
2◦ F∗
1 . The pull-back of forms is
related to the pull-back of functions, g↦→ F∗g = g◦ F:
Proposition 6.2. For g∈ C∞(N),
F∗(dg) = d(F∗g).

122 6 Differential forms
Proof. We have to show (F∗(dg))p = (d(F∗g))p for all p∈ M. But this is just
Lemma 6.1. ⊓ ⊔
Remark 6.2. Recall once again that while F∈ C∞(M,N) induces a tangent map
T F∈ C∞(T M,T N), there is no natural push-forward operation for vector ﬁelds.
By contrast, for cotangent bundles there is no naturally induced map from T∗N to
T∗M (or the other way), yet there is a natural pull-back operation for 1-forms!
In the case of vector ﬁelds, rather than working with ‘F∗(X)’ one has the notion of
related vector ﬁelds, X∼F Y . For any related vector ﬁelds X∼F Y , and β∈ Ω 1(N),
we then have that
(F∗β )(X) = F∗(β (Y )).
Indeed, at any given p∈ M this just becomes the deﬁnition of the pullback map.
6.6 Integration of 1-forms
Given a curveγ : J→ M in a manifold, and any 1-formα∈ Ω 1(M), we can consider
the pull-back γ∗α∈ Ω 1(J). By the description of 1-forms on R, this is of the form
γ∗α = f (t)dt
for a smooth function f∈ C∞(J).
To discuss integration, it is convenient to work with closed intervals rather than
open intervals. Let [a,b]⊆ R be a closed interval. A map γ : [a,b]→ M into a
manifold will be called smooth if it extends to a smooth map from an open interval
containing [a,b]. We will call such a map a smooth path.
Deﬁnition 6.5. Given a smooth path γ : [a,b]→ M, we deﬁne the integral of a 1-
form α∈ Ω 1(M) along γ as ∫
γ
α =
∫ b
a
γ∗α.
The fundamental theorem of calculus has the following consequence for manifolds.
It is a special case of Stokes’ theorem.
Proposition 6.3. Let γ : [a,b]→ M be a smooth path, with γ(a) = p, γ(b) = q. For
any f ∈ C∞(M), we have ∫
γ
d f = f (q)− f (p).
In particular, the integral of d f depends only on the end points of the path, rather
than the path itself.
Proof. We have
γ∗d f = dγ∗ f = d( f◦ γ) = ∂ ( f◦ γ)
∂t dt.

6.7 2-forms 123
Integrating froma to b, we obtain, by the fundamental theorem of calculus,f (γ(b))−
f (γ(a)). ⊓ ⊔
A 1-form α∈ Ω 1(M) such that α = d f for some function f∈ C∞(M) is called
exact.
Example 6.2. Consider the 1-form
α = y2exdx + 2yexdy∈ Ω (R2).
Problem: Find the integral of α along the path
γ : [0,1]→ M, t↦→ (sin(πt/2),t3).
Solution: Observe that the 1-form α is exact:
α = d
(
y2ex)
= d f
with f (x,y) = y2ex. The path has end points γ(0) = (0,0) and γ(1) = (1,1). Hence,
∫
γ
α = f (γ(1))− f (γ(0)) = e.
Note that the integral over, say,α = y2exdx would be much harder.
Remark 6.3. The proposition gives a necessary condition for exactness: The integral
of α along paths should depend only on the end points. This condition is also suf-
ﬁcient, since we can deﬁne f on the connected components of M, by ﬁxing a base
point p0 on each such component, and putting f (p) =
∫
γ α for any path from p0 to
p.
If M is an open subset U⊆ Rm, so that α = ∑i αidxi, then α = d f means that
αi = ∂ f
∂xi . A necessary condition is the equality of partial derivatives,
∂ αi
∂x j = ∂ αj
∂xi ,
In multivariable calculus one learns that this condition is also sufﬁcient, provided
U is simply connected (e.g., convex). Using the exterior differential of forms in
Ω 1(U), this condition becomes d α = 0. To obtain a coordinate-free version of the
condition, we need higher order forms.
6.7 2-forms
To get a feeling for higher degree forms, and constructions with higher forms, we
ﬁrst discuss 2-forms.

124 6 Differential forms
Deﬁnition 6.6. A 2-form on M is a C∞(M)-bilinear skew-symmetric map
α : X(M)× X(M)→ C∞(M), (X,Y )↦→ α(X,Y ).
Here skew-symmetry means that α(X,Y ) =−α(Y,X) for all vector ﬁelds X,Y ,
while C∞(M)-bilinearity means
α( f X,Y ) = f α(X,Y ) = α(X, fY )
for f∈ C∞(M), as well as α(X′ + X′′,Y ) = α(X′,Y ) + α(X′′,Y ), and similarly in
the second argument. (Actually, by skew-symmetry it sufﬁces to require C∞(M)-
linearity in the ﬁrst argument.) By the same argument as for 1-forms, the value
α(X,Y )p depends only on the values Xp,Yp. Also, if α is a 2-form then so is f α for
any smooth function f .
First examples of 2-forms are obtained from 1-forms: Let α, β∈ Ω 1(M). Then
we deﬁne a wedge product α∧ β∈ Ω 2(M), as follows:
(α∧ β )(X,Y ) = α(X)β (Y )− α(Y )β (X).
This is well-deﬁned, since the right hand side is skew-symmetric and bi-linear in X
and Y .
For an open subset U⊆ Rm, a 2-form ω∈ Ω 2(U) is uniquely determined by its
values on coordinate vector ﬁelds. By skew-symmetry the functions
ωi j = ω
( ∂
∂xi , ∂
∂x j
)
satisfy ωi j =−ω ji; hence it sufﬁces to know these functions for i < j. As a conse-
quence, we see that the most general 2-form on U is
ω = 1
2
m
∑
i, j=1
ωi jdxi∧ dx j = ∑
i< j
ωi jdxi∧ dx j.
6.8 k-forms
We now generalize to forms of arbitrary degree.
6.8.1 Deﬁnition
Deﬁnition 6.7. Let k be a non-negative integer. Ak-form on M is aC∞(M)-multilinear,
skew-symmetric map

6.8 k-forms 125
α : X(M)×···× X(M)| {z }
k times
→ C∞(M).
The space of k-forms is denoted Ω k(M); in particular Ω 0(M) = C∞(M).
Here, skew-symmetry means that α(X1, . . . ,Xk) changes sign under exchange of any
two of its elements. For example,α(X1,X2,X3, . . .) =−α(X2,X1,X3, . . .). More gen-
erally, if Sk is the group of permutations of{1, . . . ,k}, and sign(s) is the sign of a
permutation s∈ Sk (+1 for an even permutation,−1 for an odd permutation) then
α(Xs(1), . . . ,Xs(k)) = sign(s)α(X1, . . . ,Xk).
The C∞(M)-multilinearity means C∞(M)-linearity in each argument, similar to the
condition for 2-forms. It implies, in particular,α is local in the sense that the value of
α(X1, . . . ,Xk) at any given p∈ M depends only on the values X1|p, . . . ,Xk|p∈ TpM.
One thus obtains a skew-symmetric multilinear form
αp : TpM×···× TpM→ R,
for all p∈ M.
If α1, . . . ,αk are 1-forms, then one obtains a k-formα =: α1∧ . . .∧ αk by ‘wedge
product’.
(α1∧ . . .∧ αk)(X1, . . . ,Xk) = ∑
s∈Sk
sign(s)α1(Xs(1))··· αk(Xs(k)).
(More general wedge products will be discussed below.) Here, the signed summa-
tion over the permutation group guarantees that the result is skew-symmetric.
Using C∞-multilinearity, a k-form on U⊆ Rm is uniquely determined by its val-
ues on coordinate vector ﬁelds ∂
∂x1 , . . . , ∂
∂xm , i.e. by the functions
αi1...ik = α
( ∂
∂xi1
, . . . , ∂
∂xik
)
.
Moreover, by skew-symmetry we only need to consider ordered index sets I =
{i1, . . . ,ik}⊆{ 1, . . . ,m}, that is, i1 < . . . < ik. Using the wedge product notation,
we obtain
α = ∑
i1<···<ik
αi1...ikdxi1∧··· dxik .
6.8.2 Wedge product
We next turn to the deﬁnition of a wedge product of forms α∈ Ω k(M) and β∈
Ω l(M). A permutation s∈ Sk+l is called a k,l shufﬂe if it satisﬁes
s(1) < . . . <s(k), s(k + 1) < . . . <s(k + l).

126 6 Differential forms
Deﬁnition 6.8. The wedge product of α∈ Ω k(M), β∈ Ω l(M) is the element
α∧ β∈ Ω k+l(M)
given as
(α∧ β )(X1, . . . ,Xk+l) = ∑sign(s)α(Xs(1), . . . ,Xs(k)) β (Xs(k+1), . . . ,Xs(k+l))
where the sum is over all k,l-shufﬂes.
Example 6.3. For α, β∈ Ω 2(M),
(α∧ β )(X,Y,Z,W ) = α(X,Y )β (Z,W )− α(X,Z)β (Y,W )
+α(X,W )β (Y,Z) +α(Y,Z)β (X,W )
−α(Y,W )α(X,Z) +α(Z,W )β (X,Y ).
⊓ ⊔
The wedge product is graded commutative: If α∈ Ω k(M) and β∈ Ω l(M) then
α∧ β = (−1)kl β∧ α.
Furthermore, it is associative:
Lemma 6.5. Given αi∈ Ωki(M) we have
(α1∧ α2)∧ α3 = α1∧ (α2∧ α3)
Proof. For both sides, the evaluation onX1, . . . ,Xk with k = k1 + k2 + k3, is a signed
sum over all k1,k2,k3-shufﬂes (it should be clear how this is deﬁned).
So, we may in fact drop the parentheses when writing wedge products.
6.8.3 Exterior differential
Recall that we deﬁned the exterior differential on functions by the formula
(d f)(X) = X( f ). (6.5)
we will now extend this deﬁnition to all forms.
Theorem 6.1. There is a unique collection of linear maps d : Ω k(M)→ Ω k+1(M),
extending the map (6.5) for k = 0, such that d(d f ) = 0 and satisfying the graded
product rule,
d(α∧ β ) = dα∧ β + (−1)kα∧ dβ (6.6)
for α∈ Ω k(M) and β∈ Ω l(M). This exterior differential satisﬁes d◦ d = 0.

6.8 k-forms 127
Proof. Suppose ﬁrst that such an exterior differential is given. Then d is local, in the
sense that for any open subset U⊆ M the restriction (dα)|U depends only on α|U,
or equivalently (dα)|U = 0 when α|U = 0. Indeed, if this is the case and p∈ U, we
may choose f∈ C∞(M) = Ω 0(M) such that f vanishes on M\U and f|p = 1. Then
f α = 0, hence the product rule (6.6) gives
0 = d( f α) = d f∧ α + f dα.
Evaluating at p we obtain (dα)p = 0 as claimed. Using locality, we may thus work
in local coordinates. If α∈ Ω 1(M) is locally given by
α = ∑
i1<···<ik
αi1···ikdxi1∧···∧ dxik ,
then the product rule together with ddxi = 0 forces us to deﬁne
dα = ∑
i1<···<ik
dαi1···ik∧ dxi1∧···∧ dxik =
m
∑
l=1
∑
i1<···<ik
∂ αi1···ik
∂xl dxl∧ dxi1∧···∧ dxik .
Conversely, we may use this explicit formula (cf. (6.1)) to deﬁne dα|U for a coor-
dinate chart domain U; by uniqueness the local deﬁnitions on overlas of coordinate
chart domains agree. Proposition 6.1 shows that (ddα)|U = 0, hence it also holds
globally. ⊓ ⊔
Deﬁnition 6.9. A k-form ω∈ Ω k(M) is called exact if ω = dα for some α∈
Ω k−1(M). It is called closed if dω = 0.
Since d◦d = 0, the exact k-forms are a subspace of the space of closedk-forms. For
the case of 1-forms, we had seen that the integral
∫
γ α of an exact 1-form α = d f
along a smooth path γ : [a,b]→ M is given by the difference of the values at the
end points; a necessary condition for α to be exact is that it is closed. An example
of a 1-form that is closed but not exact is
α = ydx− xdy
x2 + y2 ∈ Ω 1(R2\{0}).
Remark 6.4. The quotient space (closed k-forms modulo exact k-forms) is a vector
space called the k-th (de Rham) cohomology
Hk(M) ={α∈ Ω k(M)| α is closed}
{α∈ Ω k(M)| α is exact} .
It turns out that wheneverM is compact (and often also ifM is non-compact), Hk(M)
is a ﬁnite-dimensional vector space. The dimension of this vector space
bk(M) = dimHk(M)

128 6 Differential forms
is called the k-th Betti number of M; these numbers are important invariants of
M which one can use to distinguish non-diffeomorphic manifolds. For example, if
M = CPn one can show that
bk(CPn) = 1 for k = 0,2, . . . ,2n
and bk(CPn) = 0 otherwise. For M = SN the Betti numbers are
bk(Sn) = 1 for k = 0,n
while bk(Sn) = 0 for all other k. Hence CPn cannot be diffeomorphic to S2n unless
n = 1.
6.9 Lie derivatives and contractions
Given a vector ﬁeld X, and a k-form α∈ Ω k(M), we can deﬁne a k− 1-form
ιX α∈ Ω k−1(M)
by contraction: Thinking of α as a multi-linear form, one simply puts X into the
ﬁrst slot:
(ιX α)(X1, . . . ,Xk−1) = α(X,X1, . . . ,Xk−1).
Contractions have the following compatibility with the wedge product, similar to
that for the exterior differential:
ιX (α∧ β ) = ιX α∧ β + (−1)kα∧ ιX β , (6.7)
for α∈ Ω k(M), β∈ Ω l(M), which one veriﬁes by evaluating both sides on vector
ﬁelds. Another important operator on forms is the Lie derivative:
Theorem 6.2. Given a vector ﬁeld X, there is a unique collection of linear maps
LX : Ω k(M)→ Ω k(M), such that
LX ( f ) = X( f ), LX (d f ) = dX( f ),
and satisfying the product rule,
LX (α∧ β ) = LX α∧ β + α∧ LX β (6.8)
for α∈ Ω k(M) and β∈ Ω l(M).
Proof. As in the case of the exterior differential, we can use the product rule to show
that LX is local: (LX α)|U depends only on α|U and X|U. Since any differential form
is a sum of wedge products of 1-forms, LX is uniquely determined by its action on
functions and differential of functions. This proves uniqueness. For existence, we
give the following formula:

6.9 Lie derivatives and contractions 129
LX = d◦ ιX + ιX◦ d.
On functions, this gives the correct result since
LX f = ιXd f = X( f ),
and also on differentials of functions since
LXd f = dιXd f = dLX f = 0.
⊓ ⊔
To summarize, we have introduced three operators
d : Ω k(M)→ Ω k+1(M), LX : Ω k(M)→ Ω k(M), ιX : Ω k(M)→ Ω k−1(M).
These have the following compatibilities with the wedge product: For α∈ Ω k(M)
and β∈ Ω l(M) one has
d(α∧ β ) = ( dα)∧ β + (−1)kα∧ dβ ,
LX (α∧ β ) = ( LX α)∧ β + α∧ LX β ,
ιX (α∧ β ) = ( ιX α)∧ β + (−1)kα∧ ιX β .
One says that LX is an even derivation relative to the wedge product, whereas d, ιX
are odd derivations. They also satisfy important relations among each other:
d◦ d = 0
LX◦ LY− LY◦ LX = L[X,Y ]
ιX◦ ιY + ιY◦ ιX = 0
d◦ LX− LX◦ d = 0
LX◦ ιY− ιY◦ LX = ι[X,Y ]
ιX◦ d + d◦ ιX = LX .
Again, the signs are determined by the even/odd parity of these operators; one
should think of the left hand side as ‘graded’ commutators, where a plus sign ap-
pears whenever two entries are odd. Writing [·,·] for the graded commutators (with
the agreement that the commutator of two odd operators has a sign built in) the iden-
tities becomes [d,d] = 0, [LX ,LY ] = L[X,Y ], [ιX , ιY ] = 0, [d,LX ] = 0, [LX , ιY ] = ι[X,Y ]
and [d, ιX ] = LX.
This collection of identities is referred to as theCartan calculus, after ´Elie Cartan
(1861-1951), and in particular the last identity (which certainly is the most intrigu-
ing) is called the Cartan formula. Basic contributions to the theory of differential
forms were made by his son Henri Cartan (1906-1980), who also wrote a textbook
on the subject.

130 6 Differential forms
Exercise: Prove these identities. (Note that some have already been established.)
Hint: First check that the left hand side satisﬁes a (graded) product rule with respect
to wedge product. It therefore sufﬁces to check that both sides agree on functions f
and differentials of functions df .
As an illustration of the Cartan identities, let us prove the following formula for
the exterior differential of a 1-form α∈ Ω 1(M):
(dα)(X,Y ) = LX (α(Y ))− LY (α(X))− α([X,Y ]).
(In the Cartan Calculus, we prefer to wrote LX f instead of X( f ) since expressions
such as X(α(Y )) would look too confusing.) The calculation goes as follows:
(dα)(X,Y ) = ιY ιXdα
= ιY LX α− ιY dιX α
= LX ιY α− ι[X,Y ]α− LY ιX α + dιY ιX α
= LX (α(Y ))− LY (α(X))− α([X,Y ]).
In the last step we used that ιY ιX α = 0, because α is a 1-form.
Exercise: Prove a similar formula for the exterior differential of a 2-form, and try
to generalize to arbitrary k-forms.
6.9.1 Pull-backs
Similar to the pull-back of functions (0-forms) and 1-forms, we have a pull-back
operation for k-forms,
F∗ : Ω k(N)→ Ω k(M)
for any smooth map between manifolds, F∈ C∞(M,N). Its evaluation at any p∈ M
is given by
(F∗β )p(v1, . . . ,vk) = βF(p)(TpF(v1), . . . ,TpF(vk)).
The pull-back map satisﬁes d(F∗β ) = F∗dβ, and for a wedge product of forms,
F∗(β1∧ β2) = F∗β1∧ F∗β2.
In local coordinates, if F : U→ V is a smooth map between open subsets of Rm
and Rn, with coordinates x,y, the pull-back just amounts to ‘puttingy = F(x)’.
Example 6.4. If F : R3→ R2 is given by (u,v) = F(x,y,z) = (y2z, x) then
F∗(du∧ dv) = d(y2z)∧ dx = y2dz∧ dx + 2yzdy∧ dx.
The next example is very important, hence we state it as a proposition. It is the
‘key fact’ toward the deﬁnition of an integral.

6.9 Lie derivatives and contractions 131
Proposition 6.4. Let U⊆ Rm with coordinates xi, and V⊆ Rn with coordinates yj.
Suppose m = j, and F∈ C∞(U,V ). Then
F∗(dy1∧···∧ dyn) = J dx1∧···∧ dxn
where J(x) is the determinant of the Jacobian matrix,
J(x) = det
( ∂Fi
∂x j
)n
i, j=1
.
Proof.
F∗β = dF1∧···∧ dFn
= ∑
i1...in
∂F1
∂xi1
··· ∂Fn
∂xin
dxi1∧···∧ dxin
= ∑
s∈Sn
∂F1
∂xs(1)··· ∂Fn
∂xs(n) dxs(1)∧···∧ dxs(n)
= ∑
s∈Sn
sign(s) ∂F1
∂xs(1)··· ∂Fn
∂xs(n) dx1∧···∧ dxn
= J dx1∧···∧ dxn,
Here we noted that the wedge product d xi1∧···∧ dxin is zero unless i1, . . . ,in are a
permutation of 1, . . . ,n. ⊓ ⊔
One may regard this result as giving a new, ‘better’ deﬁnition of the Jacobian deter-
minant.
Remark 6.5. The Lie derivative LX α of a differential form with respect to a vector
ﬁeld X has an important interpretation in terms of the ﬂow Φt of X. Assuming for
simplicity that X is complete (so that Φt is a globally deﬁned diffeomorphism), one
has the formula
LX α = d
dt
⏐⏐⏐
t=0
Φ∗
t α.
(If X is incomplete, the ﬂow Φt is deﬁned only locally, but the deﬁnition still works.)
To prove this identity, it sufﬁces to check that the right hand side satisﬁes a product
rule with respect to the wedge product of forms, and that it takes on the correct
values on functions and on differentials of functions. The formula shows that LX
measures to what extent α is invariant under the ﬂow of X.

132 6 Differential forms
6.10 Integration of differential forms
Differential forms of top degree can be integrated overoriented manifolds. Let M be
an oriented manifold of dimension m, and ω∈ Ω m(M). Let supp(ω) be the support
of ω. 6
If supp(ω) is contained in an oriented coordinate chart (U, ϕ), then one deﬁnes
∫
M
ω =
∫
Rm
f (x)dx1··· dxm
where f∈ C∞(Rm) is the function, with supp( f )⊆ ϕ(U), determined from
(ϕ−1)∗ω = f dx1∧···∧ dxm.
This deﬁnition does not depend on the choice of oriented chart. Indeed, suppose
(V, ψ) is another oriented chart with supp(ω)⊆ V , and write
(ψ−1)∗ω = g dy1∧···∧ dym.
where we write y1, . . . ,ym for the coordinates on V . Letting F = ψ◦ ϕ−1 be the
change of coordinates y = F(x), Proposition 6.4 says that
F∗(dy1∧···∧ dym) = J(x)dx1∧···∧ dxm,
where J(x) = det(DF(x)) is the determinant of the Jacobian matrix ofF at x. Hence,
f (x) = g(F(x))J(x), and we obtain
∫
ψ(U)
g(y)dy1··· ym =
∫
ϕ(U)
g(F(x))J(x)dx1··· dxm =
∫
ϕ(U)
f (x)dx1··· dxm,
as required.
Remark 6.6. Here we used the change-of-variables formula from multivariable cal-
culus. It was very important that the charts are oriented, so that J > 0 everywhere.
Indeed, for general changes of variables, the change-of-variables formula involves
|J| rather than J itself.
If ω is not necessarily supported in a single oriented chart, we proceed as follows.
Let (Ui, ϕi), i = 1, . . . ,r be a ﬁnite collection of oriented charts covering supp (ω).
Together withU0 = M\supp(ω) this is an open cover of M.
Lemma 6.6. Given a ﬁnite open cover of a manifold there exists apartition of unity
subordinate to the cover, i.e. functions χi∈ C∞(M) with supp(χi)⊆ Ui and ∑r
i=0 χi =
1.
6 The support of a form is deﬁned similar to the support of a function, or support of a vector ﬁeld.
For any differential form α∈ Ω k(M), we deﬁne the support supp(α) to be the smallest closed
subset of M outside of which α is zero. (Equivalently, it is the closure of the subset over which α
is non-zero.)

6.12 Stokes’ theorem 133
Indeed, partitions of unity exists for any open cover, not only ﬁnite ones. A proof is
given in the appendix on ‘topology of manifolds’.
Let χ0, . . . ,χr be a partition of unity subordinate to this cover. We deﬁne
∫
M
ω =
r
∑
i=1
∫
M
χiω
where the summands are deﬁned as above, sinceχiω is supported inUi for i≥ 1. (We
didn’t include the term fori = 0, since χ0ω = 0.) We have to check that this is well-
deﬁned, independent of the choices. Thus, let (Vj, ψ j) for j = 1, . . . ,s be another
collection of oriented coordinate charts covering supp (ω), put V0 = M− supp(ω),
and let σ0, . . . ,σs a corresponding partition of unity subordinate to the cover by the
Vi’s.
Then the Ui∩Vj form an open cover, with the collection of χiσ j as a partition of
unity. We obtain
s
∑
j=1
∫
M
σ jω =
s
∑
j=1
∫
M
(
r
∑
i=1
χi) σ jω =
s
∑
j=1
r
∑
i=1
∫
M
σ jχiω.
This is the same as the corresponding expression for ∑r
i=1
∫
M χiω.
6.11 Integration over oriented submanifolds
Let M be a manifold, not necessarily oriented, and S is a k-dimensional oriented
submanifold, with inclusion i : S→ M. We deﬁne the integral overS, of any k-form
ω∈ Ω k(M) such that S∩ supp(ω) is compact, as follows:
∫
S
ω =
∫
S
i∗ω.
Of course, this deﬁnition works equally well for any smooth map from S into M.
For example, the integral of compactly supported 1-forms along arbitrary paths γ :
R→ M is deﬁned. Note also that M itself does not have to be oriented, it sufﬁces
that S is oriented.
6.12 Stokes’ theorem
Let M be an m-dimensional oriented manifold.
Deﬁnition 6.10. A region with (smooth) boundary in M is a closed subset D⊆ M
with the following property: There exists a smooth function f∈ C∞(M, R) such that
0 is a regular value of f , and

134 6 Differential forms
D ={p∈ M| f (p)≤ 0}.
We do not consider f itself as part of the deﬁnition of D, only the existence of f
is required. The interior of a region with boundary, given as the largest open subset
contained in D, is int(D) ={p∈ M| f (p) < 0, and the boundary itself is
∂D ={p∈ M| f (p) = 0},
a codimension 1 submanifold (i.e., hypersurface) in M.
Example 6.5. The region with bounday deﬁned by the function f∈ C∞(R2), given
by f (x,y) = x2 + y2− 1, is the unit disk D⊆ R2; its boundary is the unit circle.
Example 6.6. Recall that for 0 < r < R, zero is a regular value of the function onR3,
f (x,y,z) = z2 + (
√
x2 + y2− R)2− r2.
The corresponding region with boundary D⊆ R3 is the solid torus, its boundary is
the torus.
Recall that we are considering D inside an oriented manifold M. The boundary
∂D may be covered by oriented submanifold charts (U, ϕ), in such a way that ∂D
is given in the chart by the condition x1 = 0, and D by the condition x1≤ 0: 7
ϕ(U∩ D) = ϕ(U)∩{ x∈ Rm| x1≤ 0}.
(Indeed, given an oriented submanifold chart for which D lies on the side where
x1≥ 0, one obtains a region chart by composing with the orientation-preserving co-
ordinate change (x1, . . . ,xm)↦→ (−x1,−x2,x3 . . . ,xm).) We call oriented submanifold
charts of this kind ‘region charts’.8
Lemma 6.7. The restriction of the region charts to ∂D form an oriented atlas for
∂D.
Proof. Let (U, ϕ) and (V, ψ) be two region charts, deﬁning coordinates x1, . . . ,xm
and y1, . . . ,ym, and let F = ψ◦ ϕ−1 : ϕ(U∩ V )→ ψ(U∩ V ), x↦→ y = F(x). It
restricts to a map
F1 :{x∈ ϕ(U∩V )| x1 = 0}→{ y∈ ψ(U∩V )|y1 = 0}.
Since y1 > 0 if and only if x1 > 0, the change of coordinates satisﬁes
∂y1
∂x1
⏐⏐⏐
x1=0
> 0, ∂y1
∂x j
⏐⏐⏐
x1=0
= 0, for j > 0.
7 Note that while we originally deﬁned submanifold charts in such a way that the last m− k coor-
dinates are zero on S, here we require that the ﬁrst coordinate be zero. It doesn’t matter, since one
can simply reorder coordinates, but works better for our description of the ‘induced orientation’.
8 This is not a standard name.

6.12 Stokes’ theorem 135
Hence, the Jacobian matrix DF(x)|x1=0 has a positive (1,1) entry, and all other
entries in the ﬁrst row equal to zero. Using expansion of the determinant across the
ﬁrst row, it follows that
det(DF(0,x2, . . . ,xm)) = ∂y1
∂x1
⏐⏐⏐
x1=0
det(DF′(x2, . . . ,xm)).
which shows that det(DF′) > 0.
In particular, ∂D is again an oriented manifold. To repeat: If x1, . . . ,xm are local
coordinates near p∈ ∂D, compatible with the orientation and such thatD lies on the
side x1≤ 0, then x2, . . . ,xm are local coordinates on∂D. This convention of ‘induced
orientation’ is arranged in such a way that the Stokes’ theorem holds without extra
signs.
For an m-form ω such that supp(ω)∩ D is compact, the integral
∫
D
ω
is deﬁned similar to the case of D = M: One covers D∩ supp(ω) by ﬁnitely many
submanifold charts (Ui, ϕi) with respect to ∂D (this includes charts that are entirely
in the interior of D), and puts
∫
D
ω = ∑
∫
D∩Ui
χiω
where the χi are supported in Ui and satisfy ∑i χi over D∩ supp(ω). By the same
argument as for D = M, this deﬁnition of the integral is independent of the choice
made.
Theorem 6.3 (Stokes’ theorem). Let M be an oriented manifold of dimension m,
and D⊆ M a region with smooth boundary ∂D. Let α∈ Ω m−1(M) be a form of
degree m− 1, such that supp(α)∩ D is compact. Then
∫
D
dα =
∫
∂D
α.
As explained above, the right hand side means
∫
∂D i∗α, where i : ∂D ↪→ M is the
inclusion map.
Proof. We will see that Stokes’ theorem is just a coordinate-free version of the
fundamental theorem of calculus. Let (Ui, ϕi) for i = 1, . . . ,r be a ﬁnite collection
of region charts covering supp (α)∩ D. Let χ1, . . . ,χr∈ C∞(M) be functions with
χi≥ 0, supp (χi)⊆ Ui, and such that χ1 + . . .+ χr is equal to 1 on supp (α)∩ D.
(E.g., we may take U1, . . . ,Ur together with U0 = M\supp(ω) as an open covering,
and take the χ0, . . . ,χr∈ C∞(M) to be a partition of unity subordinate to this cover.)
Since ∫
D
dα =
r
∑
i=1
∫
D
d(χiα),
∫
∂D
α =
r
∑
i=1
∫
∂D
χiα,

136 6 Differential forms
it sufﬁces to consider the case that α is supported in a region chart.
Using the corresponding coordinates, it hence sufﬁces to prove Stokes’ theorem
for the case that α∈ Ω m−1(Rm) is a compactly supported form inRm, and D ={x∈
Rm|x1≤ 0}. That is, α has the form
α =
m
∑
i=1
fi dx1∧··· ˆdxi∧···∧ dxm,
with compactly supported fi where the hat means that the corresponding factor is to
be omitted. Only the i = 1 term contributes to the integral over ∂D = Rm−1, and
∫
Rm−1
α =
∫
f1(0,x2, . . . ,xm) dx2··· dxm.
On the other hand,
dα =
( m
∑
i=1
(−1)i+1 ∂ fi
∂xi
)
dx1∧···∧ dxm
Let us integrate each summand over the region D given by x1≤ 0. For i > 1, we
have ∫ ∞
∞
···
∫ ∞
−∞
∫ 0
−∞
∂ fi
∂xi
(x1, . . . ,xm)dx1··· dxm = 0
where we used Fubini’s theorem to carry out thexi-integration ﬁrst, and applied the
fundamental theorem of calculus to the xi-integration (keeping the other variables
ﬁxed, the integrand is the derivative of a compactly supported function). It remains
to consider the casei = 1. Here we have, again by applying the fundamental theorem
of calculus,
∫
D
dα =
∫ ∞
∞
···
∫ ∞
−∞
∫ 0
−∞
∂ f1
∂x1
(x1, . . . ,xm)dx1··· dxm
=
∫ ∞
∞
···
∫ ∞
−∞
fm(0,x2, . . . ,xm)dx2··· dxm =
∫
∂D
α
⊓ ⊔
As a special case, we have
Corollary 6.1. Let α∈ Ω m−1(M) be a compactly supported form on the oriented
manifold M. Then ∫
M
dα = 0.
Note that it does not sufﬁce that d α has compact support. For example, if f (t) is a
function with f (t) = 0 for t < 0 and f (t) = 1 for t > 0, then df has compact support,
but
∫
R d f = 1.
A typical application of Stokes’ theorem shows that for a closed form ω∈
Ω k(M), the integral of ω over an oriented compact submanifold does not change
with smooth deformations of the submanifold.

6.12 Stokes’ theorem 137
Theorem 6.4. Let ω∈ Ω k(M) be a closed form on a manifold M, and S a compact,
oriented manifold of dimension k. Let F∈ C∞(R× S,M) be a smooth map, thought
of as a smooth family of maps
Ft = F(t,·) : S→ M.
Then the integrals ∫
S
F∗
t ω
do not depend on t.
If Ft is an embedding, then this is the integral ofω over the submanifold Ft (S)⊆ M.
Proof. Let a < b, and consider the domainD = [a,b]×S⊆ R×S. The boundary ∂D
has two components, both diffeomorphic to S. At t = b the orientation is the given
orientation on S, while at t = a we get the opposite orientation. Hence,
0 =
∫
D
F∗dω =
∫
D
dF∗ω =
∫
∂D
F∗ω =
∫
S
F∗
b ω−
∫
S
F∗
a ω.
Hence
∫
S F∗
b ω =
∫
S F∗
a ω. ⊓ ⊔
Remark 6.7. Note that if one member of this family of maps, say the map F1, takes
values in a k− 1-dimensional submanifold (for instance, if F1 is a constant map),
then F∗
1 ω = 0. (Indeed, the assumption means that F1 = j◦ F′
1, where j is the inclu-
sion of a k− 1-submanifold and F′
1 takes values in that submanifold. But j∗ω = 0
for degree reasons.) It then follows that
∫
S F∗
t ω = 0 for all t.
Given a smooth map ϕ : S→ M, one refers to a smooth map F : R× S→ M
with F0 = ϕ as an ‘smooth deformation’ (or ‘isotopy’) of ϕ. We say that ϕ can
be smoothly deformed into ϕ′ if there exists a smooth isotopy F with ϕ = F0 and
ϕ′ = F1. The theorem shows that if S is oriented, and if there is a closed form
ω∈ Ω k(M) with ∫
S
ϕ∗ω⁄=
∫
S
(ϕ′)∗ω
then ϕ cannot be smoothly deformed into ϕ′. This observation has many applica-
tions; here are some of them. 9
Example 6.7. Suppose ϕ : S→ M is a smooth map, whereS is oriented of dimension
k, and ω∈ Ω k(M) is closed. If
∫
S ϕ∗ω⁄= 0, then ϕ cannot smoothly be ‘deformed’
into a map taking values in a lower-dimensional submanifold. (In particular it cannot
be deformed into a constant map.) Indeed, if ϕ′ takes values in a lower-dimensional
submanifold, then ϕ′ = j◦ ϕ′
1 where j is the inclusion of that submanifold. But then
9 You may wonder if it is still possible to ﬁnd a continuous deformation, rather than smooth. It
turns out that it doesn’t help: Results from differential topology show that two smooth maps can
be smoothly deformed into each other if and only if they can be continuously deformed into each
other.

138 6 Differential forms
j∗ω = 0, hence (ϕ′)∗ω = 0. For instance, the inclusion ϕ : S2→ M = R3\{0}
cannot be smoothly deformed inside M so that ϕ′ would take values in R2\{0}⊆
R3\{0}.
Example 6.8 (Winding number). Let ω∈ Ω 2(R2\{0}) be the 1-form
ω = 1
x2 + y2 (xdy− ydx)
In polar coordinates x = r cos θ , y = r sin θ, one has that ω = dθ. Using this fact
one sees that ω is closed (but not exact, since θ is not a globally deﬁned function
on R2\{0}.) Hence, if
γ : S1→ R2\{0}
is any smooth map (a ‘loop’), then the integral
∫
S1
γ∗ω
does not change under deformations (isotopies) of the loop. In particular, γ cannot
be deformed into a constant map, unless the integral is zero. The number
w(γ) = 1
2π
∫
S1
γ∗ω
is the winding number of γ. (One can show that this is always an integer, and that
two loops can be deformed into each other if and only if they have the same winding
number.)
Example 6.9 (Linking number). Let f ,g : S1→ R3 be two smooth maps whose
images don’t intersect, that is, with f (z)⁄= g(w) for all z,w∈ S1 (we regard S1 as
the unit circle in C). Deﬁne a new map
F : S1× S1→ S2, (z,w)↦→ f (z)− g(w)
|| f (z)− g(w)|| .
On S2, we have a 2-form ω of total integral 4π. It is the pullback of
xdy∧ dz− ydx∧ dz + zdx∧ dy∈ Ω 2(R3)
to the 2-sphere. The integral
L( f ,g) = 1
4π
∫
S1×S1
F∗ω
is called thelinking number of f and g. (One can show that this is always an integer.)
Note that if it is possible to deform one of the loops, say f , into a constant loop
through loops that are always disjoint fromg, then the linking number is zero. In his
case, we consider f ,g as ‘unlinked’.

6.13 V olume forms 139
6.13 Volume forms
A top degree differential form Γ∈ Ω m(M) is called a volume form if it is non-
vanishing everywhere: Γp⁄= 0 for all p∈ M. In a local coordinate chart (U, ϕ), this
means that
(ϕ−1)∗Γ = f dx1∧···∧ dxm
where f (x)⁄= 0 for all x∈ ϕ(U).
Example 6.10. The Euclidean space Rn has a standard volume form Γ0 = dx1∧···∧
dxn. Suppose S⊆ Rn is a submanifold of dimension n− 1, and X a vector ﬁeld that
is nowhere tangent to S. Let i : S→ Rn be the inclusion. Then
Γ := i∗(
ιXΓ0
)
∈ Ω n−1(S)
is a volume form. For instance, ifS is given as a level setf−1(0), where 0 is a regular
value of f , then the gradient vector ﬁeld
n
∑
i=1
∂ f
∂xi
∂
∂xi
has this property.
Exercise: Verify the claim that Γ := i∗(
ιXΓ0
)
is a volume form.
Example 6.11. Let i : Sn→ Rn+1 be the inclusion of the standard n-sphere. Let
X = ∑n
i=0 xi ∂
∂xi . Then
ιX (dx0∧···∧ dxn) =
n
∑
i=0
(−1)ixidx1∧··· dxi−1∧ dxi+1∧···∧ dxn
pulls back to a volume form on Sn.
Lemma 6.8. A volume form Γ∈ Ω m(M) determines an orientation on M, by taking
as the oriented charts those charts (U, ϕ) such that (ϕ−1)∗Γ = f dx1∧···∧ dxm
with f > 0 everywhere on Φ(U).
Proof. We have to check that the condition is consistent. Suppose(U, ϕ) and (V, ψ)
are two charts, where (ϕ−1)∗Γ = f dx1∧···∧ dxm and (ψ−1)∗Γ = g dy1∧···∧ dym
with f > 0 and g > 0. If U∩V is non-empty, let F = ψ◦ ϕ−1 : ϕ(U)→ ψ(V ) be
the transition function. Then
F∗(ψ−1)∗Γ|U∩V = (ϕ−1)∗Γ|U∩V ,
hence
g(F(x)) J(x) dx1∧···∧ dxm = f (x) dx1∧···∧ dxm.

140 6 Differential forms
where J is that Jacobian determinant of the transition map F = ψ◦ ϕ−1. Hence
f = J (g◦ F) on ϕ(U∩V ). Since f > 0 and g > 0, it follows that J > 0. Hence the
two charts are oriented compatible. ⊓ ⊔
Theorem 6.5. A manifold M is orientable if and only if it admits a volume form.
In this case, any two volume forms compatible with the orientation differ by an
everywhere positive smooth function:
Γ′ = f Γ , f > 0.
Proof. As we saw above, any volume form determines an orientation. Conversely,
if M is an oriented manifold, there exists a volume form compatible with the orien-
tation: Let{(Uα , ϕα )} be an oriented atlas on M. Then each
Γα = ϕ∗
α (dx1∧···∧ dxm)∈ Ω m(Uα )
is a volume form on Uα; on overlaps Uα∩ Uβ these are related by the Jacobian
determinants of the transition functions, which are strictly positive functions. Let
{χα} be a locally ﬁnite partition of unity subordinate to the cover {Uα}, see Ap-
pendix A.4. The forms χαΓα have compact support in Uα, hence they extend by
zero to global forms on M (somewhat imprecisely, we use the same notation for this
extension). The sum
Γ = ∑
α
χαΓα∈ Ω m(M)
is a well-deﬁned volume form. Indeed, near any pointp at least one of the summands
is non-zero; and if other summands in this sum are non-zero, they differ by a positive
function.
For a compact manifold M with a given volume form Γ∈ Ω m(M), one can deﬁne
the volume of M,
vol(M) =
∫
M
Γ .
Here the orientation used in the deﬁnition of the integral is taken to be the orientation
given by Γ . Thus vol(M) > 0.
Note that volume forms are always closed, for degree reasons (sinceΩ m+1(M) =
0). But on a compact manifold, they cannot be exact:
Theorem 6.6. Let M be a compact manifold with a volume form Γ∈ Ω m(M). Then
Γ cannot be exact.
Proof. We have vol (M) =
∫
M Γ > 0. But if Γ were exact, then Stokes’ theorem
would give
∫
M Γ = 0.
Of course, the compactness of M is essential here: For instance, dx is an exact vol-
ume form on R.

Appendix A
Topology of manifolds
A.1 Topological notions
A topological space is a set X together with a collection of subsets U⊆ X called
open subsets, with the following properties:
• / 0,X are open.
• If U,U′ are open then U∩U′ is open.
• For any collection Ui of open subsets, the union⋃
iUi is open.
The collection of open subsets is called thetopology of X. In the third condition, the
index set need not be ﬁnite, or even countable.
The space Rm has a standard topology given by the usual open subsets. Likewise,
the open subsets of a manifold M deﬁne a topology on M. For any set X, one has
the trivial topology where the only open subsets are / 0 andX, and the discrete topol-
ogy where every subset is considered open. An open neighborhood of a point p is
an open subset containing it. A topological space is called Hausdorff of any two
distinct points have disjoint open neighborhoods.
Let X be a topological space. Then any subset A⊆ X has a subspace topology,
with open sets the collection of all intersections U∩ A such that U⊆ X is open.
Given a surjective map q : X→ Y , the space Y inherits a quotient topology, whose
open sets are allV⊆ Y such that the pre-imageq−1(V ) ={x∈ X| q(x)∈ V} is open.
A subset A is closed if its complement X\A is open. Dual to the statements for
open sets, one has
• / 0,X are closed.
• If A,A′ are closed then A∪ A′ is closed.
• For any collection Ai of open subsets, the intersection⋂
i Ai is closed.
For any subset A, denote by A its closure, given as the smallest closed subset con-
taining A.
141

142 A Topology of manifolds
A.2 Manifolds are second countable
A basis for the topology on X is a collection B ={Uα} of open subsets of X such
that every U is a union from sets from B.
Example A.1. The collection of all open subsets of a topological space X is a basis
of the topology.
Example A.2. Let X = Rn. Then the collection of all open balls Bε (x), with ε > 0
and x∈ Rn, is a basis for the topology on Rn.
A topological space is said to be second countable if its topology has a countable
basis.
Proposition A.1. Rn is second countable.
Proof. A countable basis is given by the collection of all rational balls, by which
we mean ε-balls Bε (x) such that x∈ Qm and ε∈ Q>0. To check it is a basis, let
U⊆ Rm be open, and p∈ U. Choose ε∈ Q>0 such that B2ε (p)⊆ U. There exists a
rational point x∈ Qn with||x− p|| < ε. This then satisﬁes p∈ Bε (x)⊆ U. Since p
was arbitrary, this proves the claim.
The same reasoning shows that for any open subsetU⊆ Rm, the rational ε-balls that
are contained in U form a basis of the topology of U.
Proposition A.2. Manifolds are second countable.
Proof. Given a manifold M, let A ={(Uα , ϕα )} be a countable atlas. Then the set
of all ϕ−1
α (Bε (x)), where Bε (x) is a rational ball contained inϕα (Uα ), is a countable
basis for the topology of M. Indeed, any open subset U is a countable union over
all U∩Uα, and each of these intersections is a countable union over all ϕ−1
α (Bε (x))
such that Bε (x) is a rational ε-ball contained in U∩Uα. ⊓ ⊔
A.3 Manifolds are paracompact
A collection {Uα} of open subsets of X is called an open covering of A⊆ X if
A⊆⋃
α Uα. Consider the case A = X. A reﬁnement of an open cover{Uα} of X is
an open cover{Vβ} of X such that each Vβ is contained in someUα. It is a subcover
if each Vβ ’s is equal to someUα.
A topological space X is called compact if every open cover of X has a ﬁnite
subcover. A topological space is called paracompact if every open cover{Uα} has
a locally ﬁnite reﬁnement{Vβ}: that is, every point has an open neighborhood meet-
ing only ﬁnitely many Vβ ’s.
Proposition A.3. Manifolds are paracompact.
We will need the following auxiliary result.

A.4 Partitions of unity 143
Lemma A.1. For any manifold M, there exists a sequence of open subsets W1,W2, . . .
of M such that ⋃
Wi = M,
and such that each Wi has compact closure with Wi⊆ Wi+1.
Proof. Start with a a countable open cover O1,O2, . . .of M such that each Oi has
compact closure Oi. (We saw in the proof of Proposition A.2 how to construct such
a cover, by taking pre-images of ε-balls in coordinate charts.) Replacing Oi with
O1∪···∪ Oi we may assume O1⊆ O2⊆··· . For each i, the covering of the compact
set Oi by the collection of all O j’s admits a ﬁnite subcover. Since the sequence of
O j’s is nested, this just means Oi is contained in O j for j sufﬁciently large. We
can thus deﬁne W1,W2, . . .as a subsequence Wi = O j(i), starting with W1 = O1, and
inductively letting j(i) for i > 1 be the smallest index j(i) such that W i−1⊆ O j(i).
Proof (Proof or Proposition A.3). Let{Uα} be an open cover of M. Let Wi be a
sequence of open sets as in the lemma. For every i, the compact subset W i+1\Wi is
contained in the open set Wi+2\W i−1, hence it is covered by the collection of open
sets
(Wi+2\W i−1)∩Uα . (A.1)
By compactness, it is already covered by ﬁnitely many of the subsets (A.1). Let
V (i) be this ﬁnite collection, and V =⋃∞
i=1 V (i) ={Vβ} the resulting countable
open cover of M.
Note that by construction, if Vβ∈ V (i), then Vβ∩Wi−1 = / 0. That is, a givenWi
meets only Vβ ’s fromV (k) with k≤ i. Since these are ﬁnitely many Vβ ’s, it follows
that the cover V ={Vβ} is locally ﬁnite. ⊓ ⊔
Remark A.1. (Cf. Lang, page 35.) One can strengthen the result a bit, as follows:
Given a cover{Uα}, we can ﬁnd a reﬁnement to a cover {Vβ} such that each Vβ is
the domain of a coordinate chart (Vβ , ψβ ), with the following extra properties, for
some 0 < r < R:
(i) ψβ (Vβ ) = BR(0), and
(ii) M is already covered by the smaller subsets V′
β = ψ−1
β (Br(0)).
To prove this, we change the second half of the proof as follows: For each p∈
W i+1\Wi choose a coordinate chart (Vp, ψp) such that ψp(p) = 0, ψp(Vp) = BR(0),
and Vp⊆ (Wi+2\W i−1)∩Uα. Let V′
p⊆ Vp be the pre-image of Br(0). The V′
p cover
W i+1\Wi; let V (i) be a ﬁnite subcover and proceed as before. This remark is useful
for the construction of partitions of unity.
A.4 Partitions of unity
We will need the following result from multivariable calculus.

144 A Topology of manifolds
Lemma A.2 (Bump functions). For all 0 < r < R, there exists a function f ∈
C∞(Rm), with f (x) = 0 for||x||≥ R and f (x) = 1 for||x||≤ r.
Proof. It sufﬁces to prove the existence of a function g∈ C∞(R) such that g(t) = 0
for t≥ R and g(t) = 1 for t≤ r: Given such g we may take f (x) = g(||x||). To
construct g, recall that the function
h(t) = 0 if t≤ 0, h(t) = exp(−1/t) if x > 0
is smooth even at t = 0. The function h(t− r) +h(R− t) is strictly positive every-
where, since for t≥ r the ﬁrst summand is positive and for t≥ R the second sum-
mand is positive. Furthermore, it agrees with h(t− r) for t≥ R. Hence the function
g∈ C∞(R) given as
g(t) = 1− h(t− r)
h(t− r) +h(R−t)
is 1 for t≤ r, and 0 for t≤ R. ⊓ ⊔
The support supp( f ) of a function f on M is the smallest closed subset such that f
vanishes on M\supp( f ). Equivalently, p∈ M\supp( f ) if and only if f vanishes on
some open neighborhood of p. In the Lemma above, we can take f to have support
in BR(0) – simply apply the Lemma to 0 < r < R′ := 1
2 (R + r).
Deﬁnition A.1. A partition of unity subordinate to an open cover{Uα} of a mani-
fold M is a collection of smooth functions χα∈ C∞(M), with 0≤ χα≤ 1, such that
supp(χα )⊆ Uα, and
∑
α
χα = 1.
Proposition A.4. For any open cover{Uα} of a manifold, there exists a partition
of unity{χα} subordinate to that cover. One can take this partition of unity to be
locally ﬁnite: That is, for any p∈ M there is an open neighborhood U meeting the
support of only ﬁnitely many χα’s.
Proof. Let Vβ be a locally ﬁnite reﬁnement of the cover Uα, given by coordinate
charts of the kind described in Remark A.1, and let V′
β⊆ Vβ be as described there.
Since the images of V′
β⊆ Vβ are Br(0)⊆ BR(0), we can use Lemma A.2 to deﬁne
a function fβ∈ C∞(M) with fβ (p) = 1 for p∈ V′p and supp( fβ )⊆ Vβ . Since the V′
β
are already a cover, the sum ∑β fβ is strictly positive everywhere.
For each index β, pick an index α such that Vβ⊆ Uα. This deﬁnes a map d :
β↦→ d(β ) between the indexing sets. The functions
χα = ∑β∈d−1(α) fβ
∑γ fγ
.
give the desired partition of unity. ⊓ ⊔
An important application of partitions of unity is the following result, a weak
version of the Whitney embedding theorem.

A.4 Partitions of unity 145
Theorem A.1. Let M be a manifold admitting a ﬁnite atlas with r charts. Then there
is an embedding of M as a submanifold of Rr(m+1).
Proof. Let (Ui, ϕi), i = 1, . . . ,r be a ﬁnite atlas for M, and χ1, . . . ,χr a partition of
unity subordinate to the cover by coordinate charts. Then the products χiϕi : Ui→
Rm extend by zero to smooth functions ψi : M→ Rm. The map
F : M→ Rr(m+1), p↦→ (ψ1(p), . . . ,ψr(p), χ1(p) . . . ,χr(p))
is the desired embedding. Indeed, F is injective: if F(p) = F(q), choose i with
χi(p) > 0. Then χi(q) = χi(p) > 0, hence both p,q∈ Ui, and the condition ψi(p) =
ψi(q) gives ϕi(p) = ϕi(q), hence p = q. Similarly TpF is injective: For v∈ TpM in
the kernel of TpF, choose i such that χi(p) > 0, thus v∈ TpUi. Then v being in the
kernel of Tpψi and of Tpχi implies that it is in the kernel of Tpϕi, hence v = 0 since
ϕi is a diffeomorphism. This shows that we get an injective immersion, we leave
it as an exercise to verify that the image is a submanifold (e.g., by constructing
submanifold charts).
The theorem applies in particular to all compact manifolds. Actually, one can show
that all manifolds admit a ﬁnite atlas; for a proof see e.g. Greub-Halperin-Vanstone,
connections, curvature and cohomology , volume I. Hence, every manifold can be
realized as a submanifold.



Appendix B
Vector bundles
B.1 Tangent bundle
Let M be a manifold of dimension m. The disjoint union over all the tangent spaces
T M =
⋃
p∈M
TpM
is called the tangent bundle of M. It comes with a projection map
π : T M→ M
taking a tangent vector v∈ TpM to its base point p, and with an inclusion map
i : M→ T M
taking p∈ M to the zero vector in TpM⊆ T M. We will show that T M is itself a
manifold of dimension 2m, in such a way that π and i are smooth maps.
Example B.1. Suppose M is given as a submanifold M⊆ Rn. Then each tangent
space TpM is realized as a subspace of Rn, and
T M ={(p,v)∈ Rn× Rn| p∈ M, v∈ TpM}.
We will show that this subset is a submanifold of dimension 2m. (The dimension is
to be expected: p varies in an m-dimensional manifold, and once p is ﬁxed then v
varies in an m-dimensional vector space.) For instance, if M = S1, and using coor-
dinates x,y on the ﬁrst copy of R2 and a,b on the second copy, then
T S1 ={(x,y,r,s)∈ R4| x2 + y2 = 1, xr + ys = 0};
one can check directly that (1,0) is a regular value of the function Φ(x,y,r,s) =
(x2 + y2, xr + ys).
147

148 B Vector bundles
The tangent bundle of a general manifoldM is a special case of the more general
concept of a vector bundle, which we will ﬁrst deﬁne.
B.1.1 Vector bundles
Let Ep be k-dimensional vector spaces indexed by the points p∈ M of an m-
dimensional manifold M, and
E =
⋃
p∈M
Ep
their disjoint union. We denote by π : E→ M the projection and i : M→ E the
inclusion of zeroes.
Deﬁnition B.1. E is called a vector bundle of rank r over M if for each p∈ M there
are charts (U, ϕ) around p and (ˆU,ˆϕ) around i(p), with ˆU = π−1(U), such that ˆϕ
restricts to vector space isomorphisms
Ep = π−1(p)→{ ϕ(p)}× Rr∼= Rr
for all p∈ M. One calls E the total space and M the base of the vector bundle.
Charts (ˆU,ˆϕ) are called vector bundle charts.
The vector bundle charts may be pictured in terms of a diagram,
E⊇ˆU ˆϕ
//
π

ϕ(U)× Rr
(u,v)↦→u

M⊇ U ϕ
// ϕ(U)
The key condition is that ˆϕ restricts to vector space isomorphisms ﬁberwise. Thus,
just like a manifoldM looks locally like an open subset ofRm, a vector bundle looks
over M locally like a product of an open subset of Rm with the vector space Rr.
Proposition B.1. For any vector bundle E over M, the projection π : E→ M is a
smooth submersion, while the inclusion i : M→ E is an embedding as a submani-
fold.
Proof. In vector bundle charts, the maps π and i are just the obvious projection
ϕ(U)× Rr→ ϕ(U) and inclusion ϕ(U)→ ϕ(U)× Rr, which obviously are sub-
mersions and embeddings respectively. ⊓ ⊔
Note that the vector bundle charts (ˆU,ˆϕ) are submanifold charts for i(M)⊆ E. We
will identify M with its image i(M); it is called thezero section of the vector bundle.
Example B.2 (Trivial bundles).The trivial vector bundleover M is the direct product
M× Rr. Charts for M directly give vector bundle charts for M× Rr.

B.1 Tangent bundle 149
Example B.3 (The inﬁnite M ¨obius strip). View M = S1 as a quotient R/∼ for the
equivalence relation x∼ x +1. Let E = (R× R)/∼ be the quotient under the equiv-
alence relation (x,y)∼ (x + 1,−y), with the natural map
π : E→ M, [(x,y)]↦→ [x].
Then E is a rank 1 vector bundle (a line bundle) over S1. Its total space is an inﬁnite
M¨obius strip.
Example B.4 (Vector bundles over the Grassmannians). For any p∈ Gr(k,n), let
Ep⊆ Rn be the k-dimensional subspace that it represents. Then
E =∪p∈Gr(k,n)Ep
is a vector bundle over Gr (k,n), called the tautological vector bundle . Recall our
construction of charts (UI, ϕI) for the Grassmannian, where UI is the set of all p
such that the projection map ΠI : Rn→ RI restricts to an isomorphism Ep→ RI,
and
ϕI : UI→ L(RI, RI′
),
takes p∈ UI to the linear map A having Ep as its graph. Let
ˆϕI : π−1(UI)→ L(RI, RI′
)× RI
be the map given on the ﬁber Ep by
ˆϕI(v) = (ϕI(p), ΠI(v)).
The ˆϕI are vector bundle charts for E (once we identify L(RI, RI′
) = Rk(n−k) and
RI = Rk).
There is another natural vector bundle E′ over Gr(k,n), with ﬁber E′
p := E⊥
p the
orthogonal complement of Ep. In terms of the identiﬁcation Gr(k,n) = Gr(n− k,n),
E′ is the tautological vector bundle over Gr(n− k,n).
Remark B.1. Note that we did not worry about the ‘Hausdorff property’ for the total
space. We leave it as an exercise to show that for any (possibly non-Hausdorff)
vector bundle E→ M, the Hausdorff property for the total spaceE follows from the
Hausdorff property of the base M.
Example B.5. As a special case, we obtain the tautological line bundle E and the
hyperplane bundle E′ over RPn = Gr(1,n + 1). The tautological line bundle is non-
trivial: i.e., there do not exist global trivializations E→ RPn× R. In the case n = 1
the line bundle over RP1∼= S1 is the ‘inﬁnite M¨obius strip’ considered above.
Deﬁnition B.2. A vector bundle map (also called vector bundle morphism ) from
E→ M to F→ N is a smooth map ˆΦ : E→ F of the total spaces, together with a
smooth map Φ : M→ N of the base manifolds, such that ˆΦ restricts to linear maps
ˆΦ : Ep→ FΦ(p).

150 B Vector bundles
If ˆΦ is a diffeomorphisms, then it is called a vector bundle isomorphism. An iso-
morphism E→ M× Rr with a trivial vector bundle is called a trivialization of M.
Vector bundle maps are pictured by commutative diagrams:
E ˆΦ
//

F

M Φ
// N
Example B.6. Any vector bundle chart (ˆU,ˆϕ) deﬁnes a vector bundle map ˆϕ :
E|U := π−1(U)→ ϕ(U)× Rr.
Example B.7. The tautological line bundle E over RP1 is the simplest example of a
vector bundle that does not admit a global trivialization. (For example, one can note
that if one removes the zero section from E, then E− M stays connected; on the
other hand (M× R)− M falls into two components.)
B.1.2 Tangent bundles
We return to the discussion of tangent bundles of manifolds.
Proposition B.2. For any manifold M of dimension m, the tangent bundle
T M =∪p∈MTpM
(disjoint union of vector spaces) has the structure of a rank m vector bundle over
M. Here π : T M→ M takes v∈ TpM to the base point p.
Proof. Recall that any chart (U, ϕ) for M gives vector space isomorphisms
Tpϕ : TpM = TpU→ Tϕ(p)ϕ(U) = Rm
for all p∈ U. Let TU =∪p∈UTpM = π−1(U). The collection of maps Tpϕ gives a
bijection,
T ϕ : TU→ ϕ(U)× Rm.
We take the collection of (ˆU,ˆϕ) = (TU ,T ϕ) as vector bundle charts for T M:
T M⊇ TU T ϕ
//
π

ϕ(U)× Rm
(u,v)↦→u

M⊇ U ϕ
// ϕ(U)

B.1 Tangent bundle 151
We need to check that the transition maps are smooth. If(V, ψ) is another coordinate
chart with U∩V⁄= / 0, the transition map forTU∩ TV = T (U∩V ) = π−1(U∩V ) is
given by,
T ψ◦ (T ϕ)−1 : ϕ(U∩V )× Rm→ ψ(U∩V )× Rm.
But Tpψ◦ (Tpϕ)−1 = Tϕ(p)(ψ◦ ϕ−1) is just the derivative (Jacobian matrix) for the
change of coordinates ψ◦ ϕ−1; hence this map is given by
ϕ(U∩V )× Rm→ ψ(U∩V )× Rm, (x,a)↦→ ((ψ◦ ϕ−1)(x), Dx(ψ◦ ϕ−1)(a))
Since the Jacobian matrix depends smoothly on x, this is a smooth map. ⊓ ⊔
Proposition B.3. For any smooth map Φ∈ C∞(M,N), the map
T Φ : T M→ T N
given on TpΦ as the tangent maps TpΦ : TpM→ TΦ(p)N, is a vector bundle map.
Proof. Given p∈ M, choose charts (U, ϕ) around p and (V, ψ) around Φ(p), with
Φ(U)⊆ V . As explained above, these give vector bundle charts (TU ,T ϕ) and
(TV,T ψ). Let ~Φ = ψ◦ Φ◦ ϕ−1 : ϕ(U)→ ψ(V ). The map
T~Φ = T ψ◦ T Φ◦ (T ϕ)−1 : T ϕ(TU )→ T ψ(TV )
is smooth, since by smooth dependence of the differential Dx~Φ on the base point.
Consequently, T Φ is smooth, ⊓ ⊔
B.1.3 Some constructions with vector bundles
There are several natural constructions producing new vector bundles out of given
vector bundles.
1. If E1→ M1 and E2→ M2 are vector bundles of rank r1,r2, then the cartesian
product E1× E2 is a vector bundle over M1× M2, of rank r1 + r2.
2. Let π : E→ M be a given vector bundle.
Proposition B.4. Given a submanifold S⊆ M, the restriction E|S := π−1(S) is a
vector bundle over S, in such a way that the inclusion map E|S→ E is a vector
bundle map (and also an embedding as a submanifold).
Proof. Given p∈ S⊆ M, let (ˆU,ˆϕ) be a vector bundle chart for E, with under-
lying chart (U, ϕ) containing p. Let (U′, ϕ′) be a submanifold chart for S at p.
Replacing U,U′ with their intersection, we may assume U′ = U. Let ˆϕ′ be the
composition ofˆϕ : π−1(U)→ ϕ(U)× Rr with the map
(ϕ′◦ ϕ−1)× id : ϕ(U)× Rr→ ϕ′(U)× Rr.

152 B Vector bundles
Then ˆϕ′ takes π−1(S) to (Rl∩ ϕ′(U))× Rr; hence it is a vector bundle chart and
also a submanifold chart. ⊓ ⊔
More generally, supposeΦ∈ C∞(M,N) is a smooth map between manifolds, and
π : E→ N is a vector bundle. Then the pull-back bundle
Φ∗E :=∪p∈MEΦ(p)
is a vector bundle over M. One way to prove this is as follows: Consider the
embedding of M as the submanifold of N× M given as the graph of Φ:
M∼= gr(Φ) ={(Φ(x),x)| x∈ M}.
The vector bundle E→ N deﬁnes a vector bundle over N×M, by cartesian prod-
uct with the zero bundle 0M→ M. We have
Φ∗E∼= (E× 0M)|graph(Φ).
3. Let E,E′ be two vector bundles overM. Then the direct sum (also called Whitney
sum)
E⊕ E′ :=∪p∈MEp⊕ E′
p
is again a vector bundle over M. One way to see this is to regard E⊕ E′ as
the pull-back of the cartesian product E× E′ under the diagonal inclusion M→
M× M, x↦→ (x,x).
4. Suppose π : E→ M is a vector bundle of rankr, and E′⊆ E is a vector subbundle
of rank r′≤ r. That is, E′ is a submanifold of E, and is itself a vector bundle
over M, with the map π′ : E′→ M given by restriction of π. In particular, each
E′
p = π′−1(p) a vector subspace of Ep. The quotient bundle
E/E′ :=
⋃
p
Ep/E′
p
is again a vector bundle over M.
5. For any vector bundle E→ M, the dual bundle
E∗ =∪p∈ME∗
p
(where E∗
p = L(Ep, R) is the dual space to Ep) is again a vector bundle.
Example B.8. Given a manifoldM with a submanifold S, one calls T M|S the tangent
bundle of M along S. It contains T S as a subbundle; the normal bundle of S in M is
deﬁned as a quotient bundle νS = T M|S/T S with ﬁbers,
(νS)p = TpM/TpS.
Example B.9. The dual of the tangent bundleT Mis called thecotangent bundle, and
is denoted T∗M. Given a submanifold S⊆ M, one can consider the set of covectors

B.1 Tangent bundle 153
α∈ T∗
p M for p∈ S that annihilate TpS, that is,⟨α,v⟩ = 0 for all v∈ TpS. This is a
vector bundle called the conormal bundle ν∗
S of S. The notation is justiﬁed, since it
is the dual bundle to νS.
Example B.10. The direct sum of the two natural bundles E,E′ over the Grass-
mannian Gr (k,n) has ﬁbers Ep⊕ E′
p = Rn, hence E⊕ E′ is the trivial bundle
Gr(k,n)× Rn.
Deﬁnition B.3. A smooth section of a vector bundle π : E→ M is a smooth map
σ : M→ E with the property π◦ σ = idM. The space of smooth sections of E is
denoted Γ ∞(M,E), or simply Γ ∞(E).
Thus, a section is a family of vectors σp∈ Ep depending smoothly on p.
Examples B.11. 1. Every vector bundle has a distinguished section, thezero section
p↦→ σp = 0,
where 0 is the zero vector in the ﬁber Ep. One usually denotes the zero section
itself by 0.
2. For a trivial bundle M× Rr, a section is the same thing as a smooth function from
M to Rr:
Γ ∞(M,M× Rr) = C∞(M, Rr).
Indeed, any such function f : M→ Rr deﬁnes a section σ (p) = ( p, f (p)); con-
versely, any section σ : M→ E = M× Rr deﬁnes a function by composition
with the projection M× Rr→ Rr.
In particular, if κ : E|U→ U× Rr is a local trivialization of a vector bundle E
over an open subset U, then a section σ∈ Γ ∞(E) restricts to a smooth function
ψ◦ σ|U : U→ Rr.
3. Let π : E→ M be a rankr vector bundle. Aframe for E overU⊆ M is a collection
of sections σ1, . . . ,σr of EU, such that (σ j)p are linearly independent at each
point p∈ U. Any frame over U deﬁnes a local trivialization ψ : EU→ U× Rr,
given in terms of its inverse mapψ−1(p,a) = ∑ j a j(σ j)p. Conversely, each local
trivialization gives rise to a frame.
The space Γ ∞(M,E) is a vector space under pointwise addition:
(σ1 + σ2)p = (σ1)p + (σ2)p.
Moreover, it is a module over the algebra C∞(M), under multiplication 1: ( f σ )p =
fpσp.
1 Here and from now on, we will often write fp or f|p for the value f (p).

154 B Vector bundles
B.2 Dual bundles
More generally, if E→ M is a vector bundle of rank r, then we can deﬁne its dual
E∗→ M with ﬁbers E∗
p = (Ep)∗.
Proposition B.5. The dual E∗ of a vector bundle E is itself a vector bundle.
Proof. For any open subset U⊆ M, write EU =⋃
p∈U Ep for the restriction of E to
U, and similarly E∗
U =⋃
p∈U Ep. Recall that a vector bundle chart for E is given by
a chart (U, ϕ) for M together with a chart for E, of the form (EU ,ˆϕ), where
ˆϕ : EU→ ϕ(U)× Rr
is a ﬁberwise linear isomorphism. Taking the inverse of the dual of the vector space
isomorphism Ep→ Rr, we get maps E∗
p→ (Rr)∗, hence
(ˆϕ∗)−1 : E∗
U→ ϕ(U)× (Rr)∗.
Identifying (Rr)∗∼= Rr, these serve as vector bundle charts (E∗
U , (ˆϕ∗)−1) for E∗.
⊓ ⊔
Given smooth sections σ∈ Γ ∞(M,E) and τ∈ Γ ∞(M,E∗), one can take the pairing
to deﬁne a function
⟨τ, σ⟩∈ C∞(M), ⟨τ, σ⟩(p) =⟨τp, σp⟩.
This pairing is C∞(M)-linear in both entries: That is,
⟨τ, f σ⟩ = f⟨τ, σ⟩ =⟨ f τ, σ⟩
for all τ∈ Γ ∞(M,E∗), σ∈ Γ ∞(M,E), f∈C∞(M). We can use pairings with smooth
sections of E to characterize the smooth sections of E∗.
Proposition B.6. 1. A family of elementsτp∈ E∗
p for p∈ M deﬁnes a smooth section
of E∗ if and only if for all σ∈ Γ ∞(M,E), the function
M→ R, p↦→⟨ τp, σp⟩
is smooth.
2. The space of sections of the dual bundle is identiﬁed with the space of C ∞(M)-
linear maps
τ : Γ ∞(M,E)→ C∞(M), σ↦→⟨ τ, σ⟩.
Here C∞(M)-linear means that⟨τ, f σ⟩ = f⟨τ, σ⟩ for all functions f .
Proof. The proof uses local bundle charts and bump functions. Details are left as an
exercise. 2
2 It is similar to the fact, proved earlier, that a collection of tangent vectors Xp∈ TpM deﬁnes a
smooth vector ﬁeld if and only if for any f∈ C∞(M) the map↦→ Xp( f ) is smooth.

B.2 Dual bundles 155
Remark B.2. A slightly more precise version of the second part of this proposition
is as follows: Regard E = Γ ∞(M,E) as a module over the algebra A = C∞(M) of
smooth functions, and likewise for E∗ = Γ ∞(M,E∗). The space Hom A(E ,A) of
A = C∞(M)-linear maps E→ A is again an A-module. There is a natural A-module
map
E∗→ HomA(E ,A)
deﬁned by the pairing of sections. This map is an isomorphism.

