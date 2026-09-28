# An Introduction to Lie Groups and Symplectic Geometry

A series of nine lectures on Lie groups and symplectic geometry delivered at the Regional Geometry Institute in Park City, Utah, 24 June–20 July 1991.

by

Robert L. Bryant

Duke University

Durham, NC

bryant@math.duke.edu

This is an unofficial version of the notes and was last modified on 23 July 2018.

## Introduction

These are the lecture notes for a short course entitled “Introduction to Lie groups and symplectic geometry” that I gave at the 1991 Regional Geometry Institute at Park City, Utah starting on 24 June and ending on 11 July.

The course really was designed to be an introduction, aimed at an audience of students who were familiar with basic constructions in differential topology and rudimentary differential geometry, who wanted to get a feel for Lie groups and symplectic geometry. My purpose was not to provide an exhaustive treatment of either Lie groups, which would have been impossible even if I had had an entire year, or of symplectic manifolds, which has lately undergone something of a revolution. Instead, I tried to provide an introduction to what I regard as the basic concepts of the two subjects, with an emphasis on examples that drove the development of the theory.

I deliberately tried to include a few topics that are not part of the mainstream subject, such as Lie’s reduction of order for differential equations and its relation with the notion of a solvable group on the one hand and integration of ODE by quadrature on the other. I also tried, in the later lectures to introduce the reader to some of the global methods that are now becoming so important in symplectic geometry. However, a full treatment of these topics in the space of nine lectures beginning at the elementary level was beyond my abilities.

After the lectures were over, I contemplated reworking these notes into a comprehensive introduction to modern symplectic geometry and, after some soul-searching, finally decided against this. Thus, I have contented myself with making only minor modifications and corrections, with the hope that an interested person could read these notes in a few weeks and get some sense of what the subject was about.

An essential feature of the course was the exercise sets. Each set begins with elementary material and works up to more involved and delicate problems. My object was to provide a path to understanding of the material that could be entered at several different levels and so the exercises vary greatly in difficulty. Many of these exercise sets are obviously too long for any person to do them during the three weeks the course, so I provided extensive hints to aid the student in completing the exercises after the course was over.

I want to take this opportunity to thank the many people who made helpful suggestions for these notes both during and after the course. Particular thanks goes to Karen Uhlenbeck and Dan Freed, who invited me to give an introductory set of lectures at the RGI, and to my course assistant, Tom Ivey, who provided invaluable help and criticism in the early stages of the notes and tirelessly helped the students with the exercises. While the faults of the presentation are entirely my own, without the help, encouragement, and proofreading contributed by these folks and others, neither these notes nor the course would never have come to pass.

Background Material and Basic Terminology. In these lectures, I assume that the reader is familiar with the basic notions of manifolds, vector fields, and differential forms. All manifolds will be assumed to be both second countable and Hausdorff. Also, unless I say otherwise, I generally assume that all maps and manifolds are $C ^ { \infty }$

Since it came up several times in the course of the course of the lectures, it is probably worth emphasizing the following point: A submanifold of a smooth manifold X is, by definition, a pair $( S , f )$ where S is a smooth manifold and $f \colon S \ \to \ X$ is a one-to-one immersion. In particular, f need not be an embedding.

The notation I use for smooth manifolds and mappings is fairly standard, but with a few slight variations:

If $f \colon X \to Y$ is a smooth mapping, then $f ^ { \prime } { : } T X \to T Y$ denotes the induced mapping on tangent bundles, with $f ^ { \prime } ( x )$ denoting its restriction to $T _ { x } X$ . (However, I follow tradition when $X = \mathbb { R }$ and let $f ^ { \prime } ( t )$ stand for $f ^ { \prime } ( t ) ( \partial / \partial t )$ for all $t \in \mathbb { R }$ . I trust that this abuse of notation will not cause confusion.)

For any vector space V , I generally use $A ^ { p } ( V )$ (instead of, say, $\Lambda ^ { p } ( V ^ { * } ) )$ to denote the space of alternating (or exterior) p-forms on V . For a smooth manifold M, I denote the space of smooth, alternating p-forms on M by $A ^ { p } ( M )$ . The algebra of all (smooth) differential forms on M is denoted by $A ^ { * } ( M )$

I generally reserve the letter d for the exterior derivative d: $\mathcal { A } ^ { p } ( M ) \to \mathcal { A } ^ { p + 1 } ( M )$

For any vector field X on M , I will denote left-hook with X (often called interior product with X) by the symbol X . This is the graded derivation of degree −1 of $A ^ { * } ( M )$ that satisfies $X \lrcorner ( d f ) = X f$ for all smooth functions f on M. For example, the Cartan formula for the Lie derivative of differential forms is written in the form

$$
{ \mathfrak { L } } _ { X } \phi = X \lrcorner d \phi + d ( X \lrcorner \phi ) .
$$

Jets. Occasionally, it will be convenient to use the language of jets in describing certain constructions. Jets provide a coordinate free way to talk about the Taylor expansion of some mapping up to a specified order. No detailed knowledge about these objects will be needed in these lectures, so the following comments should suffice:

If f and g are two smooth maps from a manifold $X ^ { m }$ to a manifold $Y ^ { n }$ , we say that f and g agree to order k at $x \in X$ if, first, $f ( x ) = g ( x ) = y \in Y$ and, second, when u: $U \to \mathbb { R } ^ { m }$ and v: $V \to \mathbb { R } ^ { n }$ are local coordinate systems centered on x and y respectively, the functions $F = v \circ f \circ u ^ { - 1 }$ and $G = v \circ g \circ u ^ { - 1 }$ have the same Taylor series at $0 \in \mathbb { R } ^ { m }$ up to and including order k. Using the Chain Rule, it is not hard to show that this condition is independent of the choice of local coordinates u and v centered at x and y respectively.

The notation $\scriptstyle f \equiv _ { x , k } g$ will mean that f and g agree to order k at x. This is easily seen to define an equivalence relation. Denote the ≡x,k-equivalence class of f by $j ^ { k } ( f ) ( x )$ , and call it the k-jet of f at x.

For example, knowing the 1-jet at x of a map $f \colon X \to Y$ is equivalent to knowing both $f ( x )$ and the linear map $f ^ { \prime } ( x ) { \mathrel { : } } T _ { x } \to T _ { f ( x ) } Y$

The set of k-jets of maps from X to $Y$ is usually denoted by $J ^ { k } ( X , Y )$ . It is not hard to show that $J ^ { k } ( X , Y )$ can be given a unique smooth manifold structure in such a way that, for any smooth $f \colon X \to Y$ , the obvious map $j ^ { k } ( f ) \colon X \to J ^ { k } ( X , Y )$ is also smooth.

These jet spaces have various functorial properties that we shall not need at all. The main reason for introducing this notion is to give meaning to concise statements like “The critical points of $f$ are determined by its $\mathrm { 1 - j e t } ^ { \dag }$ “The curvature at x of a Riemannian metric $g$ is determined by its 2-jet at $x '$ , or, from Lecture 8, “The integrability of an almost complex structure $J { \mathrm { : } } T X \to T X$ is determined by its $\mathrm { 1 - j e t } ^ { \dag }$ Should the reader wish to learn more about jets, I recommend the first two chapters of [GG].

Basic and Semi-Basic. Finally, I use the following terminology: If π: $V  X$ is a smooth submersion, a p-form $\phi \in { \mathcal { A } } ^ { p } ( V )$ is said to be $\pi { - } b a s i c$ if it can be written in the form $\phi = \pi ^ { * } ( \varphi )$ for some $\varphi \in { \mathcal { A } } ^ { p } ( X )$ and π-semi-basic if, for any π-vertical\*vector field X, we have $X \ J \phi = 0$ . When the map π is clear from context, the terms “basic” or “semi-basic” are used.

It is an elementary result that if the fibers of $\pi$ are connected and $\phi$ is a p-form on V with the property that both $\phi$ and $d \phi$ are π-semi-basic, then $\phi$ is actually π-basic.

At least in the early lectures, we will need very little in the way of major theorems, but we will make extensive use of the following results:

• The Implicit Function Theorem: If $f \colon X \to Y$ is a smooth map of manifolds and $y \in Y$ is a regular value of $f ,$ then $f ^ { - 1 } ( y ) \subset X$ is a smooth embedded submanifold of $X$ , with

$$
T _ { x } f ^ { - 1 } ( y ) = \ker ( f ^ { \prime } ( x ) { \colon } T _ { x } X \to T _ { y } Y )
$$

• Existence and Uniqueness of Solutions of ODE: If X is a vector field on a smooth manifold M, then there exists an open neighborhood U of $\{ 0 \} \times M$ in $\mathbb { R } \times M$ and a smooth mapping $F \colon U \to M$ with the following properties:

i. $F ( 0 , m ) = m$ for all $m \in M$

ii. For each $m \in M$ , the slice $U _ { m } ~ = ~ \{ t \in \mathbb { R } | ( t , m ) \in U \}$ is an open interval in R (containing 0) and the smooth mapping $\phi _ { m } \colon U _ { m } \to M$ defined by $\phi _ { m } ( t ) = F ( t , m )$ is an integral curve of X.

iii. ( Maximality ) If $\phi \colon I  M$ is any integral curve of X where $I \subset \mathbb { R }$ is an interval containing 0, then $I \subset U _ { \phi ( 0 ) }$ and ${ \phi } ( t ) = { \phi } _ { \phi ( 0 ) } ( t )$ for all $t \in I$

The mapping F is called the (local) flow of X and the open set U is called the domain of the flow of X. If $U = \mathbb { R } \times M$ , then we say that X is complete.

Two useful properties of this flow are easy consequences of this existence and uniqueness theorem. First, the interval $U _ { F ( t , m ) } \subset \mathbb { R }$ is simply the interval $U _ { m }$ translated by t. Second, $F ( s + t , m ) = F \left( s , F ( t , m ) \right)$ whenever t and $s + t$ lie in $U _ { m }$

The Simultaneous Flow-Box Theorem: If $X _ { 1 } , X _ { 2 } , . . . , X _ { r }$ are smooth vector fields on M that satisfy the Lie bracket identities

$$
[ X _ { i } , X _ { j } ] = 0
$$

for all $i$ and $j ,$ and if $p \in M$ is a point where the r vectors $X _ { 1 } ( p ) , X _ { 2 } ( p ) , \ldots , X _ { r } ( p )$ are linearly independent in $T _ { p } M$ , then there exists a local coordinate system $x ^ { 1 } , x ^ { 2 } , \ldots , x ^ { n }$ on an open neighborhood U of $p$ so that, on U,

$$
X _ { 1 } = { \frac { \partial } { \partial x ^ { 1 } } } , \qquad X _ { 2 } = { \frac { \partial } { \partial x ^ { 2 } } } , \qquad \ldots , \qquad X _ { r } = { \frac { \partial } { \partial x ^ { r } } } .
$$

The Simultaneous Flow-Box Theorem has two particularly useful consequences. Before describing them, we introduce an important concept.

Let M be a smooth manifold and let $E \subset T M$ be a smooth subbundle of rank $p .$ . We say that E is integrable if, for any two vector fields X and Y on M that are sections of $E$ , their Lie bracket $[ X , Y ]$ is also a section of E.

The Local Frobenius Theorem: If $M ^ { n }$ is a smooth manifold and $E \subset T M$ is a smooth, integrable sub-bundle of rank $r ,$ then every p in M has a neighborhood U on which there exist local coordinates $x ^ { 1 } , \ldots , x ^ { r } , y ^ { 1 } , \ldots , y ^ { n - r }$ so that the sections of E over U are spanned by the vector fields

$$
{ \frac { \partial } { \partial x ^ { 1 } } } , \qquad { \frac { \partial } { \partial x ^ { 2 } } } , \qquad \ldots , \qquad { \frac { \partial } { \partial x ^ { r } } } .
$$

Associated to this local theorem is the following global version:

The Global Frobenius Theorem: Let M be a smooth manifold and let $E \subset T M$ be a smooth, integrable subbundle of rank r. Then for any $p \in M$ , there exists a connected r-dimensional submanifold $L \subset M$ that contains $p ,$ that satisfies $T _ { q } L = E _ { q }$ for all $q \in S$ and that is maximal in the sense that any connected r′-dimensional submanifold $L ^ { \prime } \subset M$ that contains $p$ and satisfies $T _ { q } L ^ { \prime } \subset E _ { q }$ for all $q \in L ^ { \prime }$ is a submanifold of L.

The submanifolds L provided by this theorem are called the leaves of the sub-bundle $E$ . (Some books call a sub-bundle $E \subset T M$ a distribution on M , but I avoid this since “distribution” already has a well-established meaning in analysis.)

## Contents

## 1. Introduction: Symmetry and Differential Equations

First notions of differential equations with symmetry, classical “integration methods.” Examples: Motion in a central force field, linear equations, the Riccati equation, and equations for space curves.

## 2. Lie Groups

Lie groups. Examples: Matrix Lie groups. Left-invariant vector fields. The exponential mapping. The Lie bracket. Lie algebras. Subgroups and subalgebras. Classification of the two and three dimensional Lie groups and algebras.

## 3. Group Actions on Manifolds

38

Actions of Lie groups on manifolds. Orbit and stabilizers. Examples. Lie algebras of vector fields. Equations of Lie type. Solution by quadrature. Appendix: Lie’s Transformation Groups, I. Appendix: Connections and Curvature.

## 4. Symmetries and Conservation Laws

61

Particle Lagrangians and Euler-Lagrange equations. Symmetries and conservation laws: Noether’s Theorem. Hamiltonian formalism. Examples: Geodesics on Riemannian Manifolds, Left-invariant metrics on Lie groups, Rigid Bodies. Poincar´e Recurrence.

## 5. Symplectic Manifolds, I

80

Symplectic Algebra. The structure theorem of Darboux. Examples: Complex Manifolds, Cotangent Bundles, Coadjoint orbits. Symplectic and Hamiltonian vector fields. Involutivity and complete integrability.

## 6. Symplectic Manifolds, II

100

Obstructions to the existence of a symplectic structure. Rigidity of symplectic structures. Symplectic and Lagrangian submanifolds. Fixed Points of Symplectomorphisms. Appendix: Lie’s Transformation Groups, II

## 7. Classical Reduction

116

Symplectic manifolds with symmetries. Hamiltonian and Poisson actions. The moment map. Reduction.

## 8. Recent Applications of Reduction

128

Riemannian holonomy. K¨ahler Structures. K¨ahler Reduction. Examples: Projective Space, Moduli of Flat Connections on Riemann Surfaces. HyperK¨ahler structures and reduction. Examples: Calabi’s Examples.

## 9. The Gromov School of Symplectic Geometry

147

The Soft Theory: The h-Principle. Gromov’s Immersion and Embedding Theorems. Almost-complex structures on symplectic manifolds. The Hard Theory: Area estimates, pseudo-holomorphic curves, and Gromov’s compactness theorem. A sample of the new results.

## Lecture 1:

# Introduction: Symmetry and Differential Equations

Consider the classical equations of motion for a particle in a conservative force field

$$
{ \ddot { x } } = - \mathrm { g r a d } \ V ( x ) ,
$$

where $V : \mathbb { R } ^ { n }  \mathbb { R }$ is some function on $\mathbb { R } ^ { n }$ . If V is proper (i.e. the inverse image under V of a compact set is compact, as when $V ( x ) = | x | ^ { 2 } )$ , then, to a first approximation, V is the potential for the motion of a ball of unit mass rolling around in a cup, moving only under the influence of gravity. For a general function V we have only the grossest knowledge of how the solutions to this equation ought to behave.

Nevertheless, we can say a few things. The total energy (= kinetic plus potential) is given by the formula $\begin{array} { r } { E = \frac 1 2 | \dot { x } | ^ { 2 } + V ( x ) } \end{array}$ and is easily shown to be constant on any solution (just differentiate $E \big ( x \bar { ( } t ) \big )$ and use the equation). Since, V is proper, it follows that x must stay inside a compact set $V ^ { - 1 } \big ( [ 0 , E ( x ( 0 ) ) ] \big )$ , and so the orbits are bounded. Without knowing any more about $V ,$ one can show (see Lecture 4 for a precise statement) that the motion has a certain ‘recurrent’ behaviour: The trajectory resulting from ‘most’ initial positions and velocities tends to return, infinitely often, to a small neighborhood of the initial position and velocity. Beyond this, very little is known is known about the behaviour of the trajectories for generic V .

Suppose now that the potential function V is rotationally symmetric, i.e., that V depends only on the distance from the origin and, for the sake of simplicity, let us take $n = 3$ as well. This is classically called the case of a central force field in space. If we let $\begin{array} { r } { V ( x ) = \frac { 1 } { 2 } v ( | x | ^ { 2 } ) } \end{array}$ , then the equations of motion become

$$
\ddot { x } = - v ^ { \prime } \bigl ( | x | ^ { 2 } \bigr ) \ x .
$$

As conserved quantities, i.e., functions of the position and velocity that stay constant on any solution of the equation, we still have the energy $\begin{array} { r } { E = \frac 1 2 \big ( | \dot { x } | ^ { 2 } + v ( | x | ^ { 2 } ) \big ) } \end{array}$ , but is it also easy to see that the vector-valued function $x \times { \dot { x } }$ is conserved, since

$$
{ \frac { d } { d t } } ( x \times \dot { x } ) = \dot { x } \times \dot { x } - x \times v ^ { \prime } ( | x | ^ { 2 } ) \ x = 0 - 0 = 0 .
$$

Call this vector-valued function $\mu .$ . We can think of E and $\mu$ as functions on the phase space $\mathbb { R } ^ { 6 }$ . For generic values of $E _ { 0 }$ and $\mu _ { 0 }$ , the simultaneous level set

$$
\Sigma _ { E _ { 0 } , \mu _ { 0 } } = \{ \left( x , \dot { x } \right) | E ( x , \dot { x } ) = E _ { 0 } , \mu ( x , \dot { x } ) = \mu _ { 0 } \}
$$

of these functions is a surface $\Sigma _ { E _ { 0 } , \mu _ { 0 } } \subset \mathbb { R } ^ { 6 }$ , and any integral of the equations of motion must lie in one of these surfaces. Since we know a great deal about integrals of ODEs on surfaces, this problem is very tractable. (See Lecture 4 and its exercises for more details on this.)

The function $\mu ,$ known as the angular momentum, is called a first integral of the second-order ODE for $x ( t )$ and seems to somehow correspond to the rotational symmetry of the original ODE. This vague relationship will be considerably sharpened and made precise in the upcoming lectures.

The relationship between symmetry and solvability in differential equations is profound and far reaching. The subjects that are now known as ‘Lie groups’ and ‘symplectic geometry’ got their beginnings from the study of symmetries of systems of ordinary differential equations and of integration techniques for them.

By the middle of the nineteenth century, Galois theory had clarified the relationship between the solvability of polynomial equations by radicals and the group of ‘symmetries’ of the equations. Sophus Lie set out to do the same thing for differential equations and their symmetries.

Here is a ‘dictionary’ showing the (rough) correspondence that Lie developed between these two achievements of nineteenth century mathematics.

<table><tr><td>Galois theory</td><td>infinitesimal symmetries</td></tr><tr><td>finite groups</td><td>continuous groups</td></tr><tr><td>polynomial equations</td><td>differential equations</td></tr><tr><td>solvable by radicals</td><td>solvable by quadrature</td></tr></table>

Although the full explanation of these correspondances must await the later lectures, we can at least begin the story in the simplest examples as motivation for developing the general theory. This is what I shall do for the rest of today’s lecture.

Classical Integration Techniques. The very simplest ordinary differential equation that we ever encounter is the equation

$$
{ \dot { x } } ( t ) = \alpha ( t )\tag{1}
$$

where $\alpha$ is a known function of t. The solution of this differential equation is simply

$$
x ( t ) = x _ { 0 } + \int _ { 0 } ^ { x } \alpha ( \tau ) d \tau .
$$

The process of computing an integral was known as ‘quadrature’ in the classical literature (a reference to expressing the area under a curve as the area of a quadrilateral), so it was said that (1) was ‘solvable by quadrature’. Note that, once one finds a particular solution, all of the others are got by simply translating the particular solution by a constant, in this case, by $x _ { 0 }$ . Alternatively, one could say that the equation (1) itself was invariant under ‘translation in $x '$

The next most trivial case is the homogeneous linear equation

$$
{ \dot { x } } = \beta ( t ) x .\tag{2}
$$

This equation is invariant under scale transformations $x \mapsto r x$ Since the mapping log: $\mathbb { R } ^ { + } $ R converts scaling to translation, it should not be surprising that the differential equation (2) is also solvable by a quadrature:

$$
x ( t ) = x _ { 0 } e ^ { \int _ { 0 } ^ { t } \beta ( \tau ) d \tau } .
$$

Note that, again, the symmetries of the equation suffice to allow us to deduce the general solution from a particular one.

Next, consider an equation where the right hand side is an affine function of $x ,$

$$
{ \dot { x } } = \alpha ( t ) + \beta ( t ) x .\tag{3}
$$

This equation is still solvable in full generality, using two quadratures. For, if we set

$$
x ( t ) = u ( t ) e ^ { \int _ { 0 } ^ { t } \beta ( \tau ) d \tau } ,
$$

then u satisfies $\dot { u } = \alpha ( t ) e ^ { - \int _ { 0 } ^ { t } \beta ( \tau ) d \tau }$ , which can be solved for u by another quadrature. It is not at all clear why one can somehow ‘combine’ equations (1) and (2) and get an equation that is still solvable by quadrature, but this will become clear in Lecture 3.

Now consider an equation with a quadratic right-hand side, the so-called Riccati equation:

$$
\dot { x } = \alpha ( t ) + 2 \beta ( t ) x + \gamma ( t ) x ^ { 2 } .\tag{4}
$$

It can be shown that there is no method for solving this by quadratures and algebraic manipulations alone. However, there is a way of obtaining the general solution from a particular solution: If s(t) is a particular solution of (4), try the ansatz $x ( t ) = s ( t ) +$ $1 / u ( t )$ . The resulting differential equation for u has the form (3) and hence is solvable by quadratures.

The Riccati equation (4) has an extensive history, and we will return to it often. Its remarkable property, that given one solution we can obtain the general solution, should be contrasted with the case of

$$
\dot { x } = \alpha ( t ) + \beta ( t ) x + \gamma ( t ) x ^ { 2 } + \delta ( t ) x ^ { 3 } .\tag{5}
$$

For equation (5), knowing one solution does not help give the rest of the solutions. There is in fact a world of difference between this and the Riccati equation, although this is far from evident looking at them.

Before leaving these simple ODE, we note the following curious progression: $\operatorname { I f } x _ { 1 }$ and x2 are solutions of an equation of type (1), then clearly the difference $x _ { 1 } - x _ { 2 }$ is constant. Similarly, if $x _ { 1 }$ and $x _ { 2 } \neq 0$ are solutions of an equation of type (2), then the ratio $x _ { 1 } / x _ { 2 }$ is constant. Furthermore, if $x _ { 1 } , \ x _ { 2 }$ 2, and $x _ { 3 } \neq x _ { 1 }$ are solutions of an equation of type (3), then the expression $( x _ { 1 } - x _ { 2 } ) / ( x _ { 1 } - x _ { 3 } )$ is constant. Finally, if $x _ { 1 } , x _ { 2 } , x _ { 3 } \neq x _ { 1 }$ , and $x _ { 4 } \neq x _ { 2 }$ are solutions of an equation of type (4), then the cross-ratio

$$
\frac { ( x _ { 1 } - x _ { 2 } ) ( x _ { 4 } - x _ { 3 } ) } { ( x _ { 1 } - x _ { 3 } ) ( x _ { 4 } - x _ { 2 } ) }
$$

is constant. There is no such corresponding expression (for any number of particular solutions) for equations of type (5). The reason for this will be made clear in Lecture 3. For right now, we just want to remark on the fact that the linear fractional transformations of the real line, a group isomorphic to SL(2, R), are exactly the transformations that leave fixed the cross-ratio of any four points. As we shall see, the group $\operatorname { S L } ( 2 , \mathbb { R } )$ is closely connected with the Riccati equation and it is this connection that accounts for many of the special features of this equation.

We will conclude this lecture by discussing the group of rigid motions in Euclidean 3-space. These are transformations of the form

$$
T ( \mathbf { x } ) = \mathbf { R } \mathbf { x } + \mathbf { t } ,
$$

where R is a rotation in $\mathbb { E } ^ { 3 }$ and $\mathbf { t } \in \mathbb { E } ^ { 3 }$ is any vector. It is easy to check that the set of rigid motions form a group under composition that is, in fact, isomorphic to the group of 4-by-4 matrices

$$
\left\{ \begin{array} { r l } { \left( R \right)} & { t } \\ { 0 } & { 1 } \end{array}  ^ { t } \mathbf { R } \mathbf { R } = \mathbf { I } _ { 3 } , ~ \mathbf { t } \in \mathbb { R } ^ { 3 } ~ \right\} .
$$

(Topologically, the group of rigid motions is just the product $\mathrm { O ( 3 ) \times \mathbb { R } ^ { 3 } . ) }$

Now, suppose that we are asked to solve for a curve $\mathbf { x } { : \mathbb { R } } \to { \mathbb { R } } ^ { 3 }$ with a prescribed curvature $\kappa ( t )$ and torsion $\tau ( t )$ . If x were such a curve, then we could calculate the curvature and torsion by defining an oriented orthonormal basis $\left( \mathbf { e } _ { 1 } , \mathbf { e } _ { 2 } , \mathbf { e } _ { 3 } \right)$ along the curve, satisfying ${ \dot { x } } = \mathbf { e } _ { 1 } , { \dot { \mathbf { e } } } _ { 1 } = \kappa \mathbf { e } _ { 2 } , { \dot { \mathbf { e } } } _ { 2 } = - \kappa \mathbf { e } _ { 1 } + \tau \mathbf { e } _ { 3 }$ . (Think of the torsion as measuring how $\mathbf { e } _ { 2 }$ falls away from the $\mathbf { e } _ { 1 } \mathbf { e } _ { 2 } { \mathrm { - p l a n e . } } )$ Form the 4-by-4 matrix

$$
X = \left( \begin{array} { c c c c } { { { \bf e } _ { 1 } } } & { { { \bf e } _ { 2 } } } & { { { \bf e } _ { 3 } } } & { { { \bf x } } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) ,
$$

(where we always think of vectors in $\mathbb { R } ^ { 3 }$ as columns). Then we can express the ODE for prescribed curvature and torsion as

$$
\dot { X } = X \left( \begin{array} { c c c c } { { 0 } } & { { - \kappa } } & { { 0 } } & { { 1 } } \\ { { \kappa } } & { { 0 } } & { { - \tau } } & { { 0 } } \\ { { 0 } } & { { \tau } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) .
$$

We can think of this as a linear system of equations for a curve $X ( t )$ in the group of rigid motions.

It is going to turn out that, just as in the case of the Riccati equation, the prescribed curvature and torsion equations cannot be solved by algebraic manipulations and quadrature alone. However, once we know one solution, all other solutions for that particular  κ(t), τ (t) can be obtained by rigid motions. In fact, though, we are going to see that one does not have to know a solution to the full set of equations before finding the rest of the solutions by quadrature, but only a solution to an equation connected to SO(3), just in the same way that the Riccati equation is connected to SL(2, R), the group of transformations of the line that fix the cross-ratio of four points.

## Lecture 2:

## Lie Groups and Lie Algebras

Lie Groups. In this lecture, I define and develop some of the basic properties of the central objects of interest in these lectures: Lie groups and Lie algebras.

Definition 1: A Lie group is a pair $( G , \mu )$ where $G$ is a smooth manifold and $\mu : G { \times } G \to G$ is a smooth mapping that gives G the structure of a group.

When the multiplication $\mu$ is clear from context, one usually just says $^ { 6 6 } G$ is a Lie group.” Also, for the sake of notational sanity, I will follow the practice of writing $\mu ( a , b )$ simply as ab whenever this will not cause confusion. I will usually denote the multiplicative identity by $e \in G$ and the multiplicative inverse of $a \in G$ by $a ^ { - 1 } \in G$

Most of the algebraic constructions in the theory of abstract groups have straightforward analogues for Lie groups:

Definition 2: A Lie subgroup of a Lie group G is a subgroup $H \subset G$ that is also a submanifold of G. A Lie group homomorphism is a group homomorphism $\phi : H \to G$ that is also a smooth mapping of the underlying manifolds.

Here is the prototypical example of a Lie group:

Example : The General Linear Group. The (real) general linear group in dimension n, denoted ${ \mathrm { G L } } ( n , \mathbb { R } )$ , is the set of invertible $n { \mathrm { - } } \mathrm { b y } { \mathrm { - } } n$ real matrices regarded as an open submanifold of the $n ^ { 2 } .$ -dimensional vector space of all n-by-n real matrices with multiplication map $\mu$ given by matrix multiplication: $\mu ( a , b ) = a b$ . Since the matrix product ab is defined by a formula that is polynomial in the matrix entries of a and b, it is clear that ${ \mathrm { G L } } ( n , \mathbb { R } )$ is a Lie group.

Actually, if V is any finite dimensional real vector space, then GL(V ), the set of bijective linear maps $\phi : V \to V$ , is an open subset of the vector space End $( V ) = V \otimes V ^ { * }$ and becomes a Lie group with multiplication $\mu : \operatorname { G L } ( V ) \times \operatorname { G L } ( V ) \to \operatorname { G L } ( V )$ given by composition of maps: $\mu ( \phi _ { 1 } , \phi _ { 2 } ) = \phi _ { 1 } \circ \phi _ { 2 }$ . If dim $( V ) = n$ , then GL(V ) is isomorphic (as a Lie group) to ${ \mathrm { G L } } ( n , \mathbb { R } )$ , though not canonically.

The advantage of considering abstract vector spaces V rather than just $\mathbb { R } ^ { n }$ is mainly conceptual, but, as will be seen, this conceptual advantage is great. In fact, Lie groups of linear transformations are so fundamental that a special terminology is reserved for them:

Definition 3: A (linear) representation of a Lie group G is a Lie group homomorphism $\rho : G \to { \mathrm { G L } } ( V )$ for some vector space V (called the representation space). Such a representation is said to be faithful (resp., almost faithful) if $\rho$ is one-to-one (resp., has 0-dimensional kernel).

It is a consequence of a theorem of Ado and Iwasawa that every connected Lie group has an almost faithful, finite-dimensional representation. (One of the later exercises constructs a connected Lie group that has no faithful, finite-dimensional representation, so almost faithful is the best one can hope for.)

Example: Vector Spaces. Any vector space over R becomes a Lie group when the group “multiplication” is taken to be addition.

Example: Matrix Lie Groups. The Lie subgroups of GL(n, R) are called matrix Lie groups and play an important role in the theory. Not only are they the most frequently encountered, but, because of the theorem of Ado and Iwasawa, practically anything that is true for matrix Lie groups has an analog for a general Lie group. In fact, for the first pass through, the reader can simply imagine that all of the Lie groups mentioned are matrix Lie groups. Here are a few simple examples:

1. Let $A _ { n }$ be the set of diagonal n-by-n matrices with positive entries on the diagonal.

2. Let $N _ { n }$ be the set of upper triangular n-by-n matrices with all diagonal entries all equal to 1.

3. (n = 2 only) Let $\mathbb { C } ^ { \bullet } = \left\{ { \binom { a - b } { b } } \vert a ^ { 2 } + b ^ { 2 } > 0 \right\}$ . Then $\mathbb { C } ^ { \bullet }$ is a matrix Lie group diffeomorphic to $S ^ { 1 } \times \mathbb { R }$ . (You should check that this is actually a subgroup of ${ \mathrm { G L } } ( 2 , \mathbb { R } ) ! )$

4. Let ${ \mathrm { G L } } _ { + } ( n , \mathbb { R } ) = \{ a \in { \mathrm { G L } } ( n , \mathbb { R } ) | { \mathrm { ~ d e t } } ( a ) > 0 \}$

There are more interesting examples, of course. A few of these are

$$
\begin{array} { r l } & { \mathrm { S L } ( n , \mathbb { R } ) = \{ a \in \mathrm { G L } ( n , \mathbb { R } ) | \operatorname* { d e t } ( a ) = 1 \} } \\ & { \qquad \mathrm { O } ( n ) = \{ a \in \mathrm { G L } ( n , \mathbb { R } ) | ^ { t _ { a } } a = I _ { n } \} } \\ & { \mathrm { S O } ( n , \mathbb { R } ) = \{ a \in \mathrm { O } ( n ) | \operatorname* { d e t } ( a ) = 1 \} , } \end{array}
$$

which are known respectively as the special linear group , the orthogonal group , and the special orthogonal group in dimension n. In each case, one must check that the given subset is actually a subgroup and submanifold of GL(n, R). These are exercises for the reader. (See the problems at the end of this lecture for hints.)

A Lie group can have ‘wild’ subgroups that cannot be given the structure of a Lie group. For example, (R, +) is a Lie group that contains totally disconnected, uncountable subgroups. Since all manifolds in these notes are second countable, such subgroups (by definition) cannot be given the structure of a (0-dimensional) Lie group.

However, it can be shown [see Warner, pg. 110] that any closed subgroup of a Lie group G is an embedded submanifold of G and hence is a Lie subgroup. However, for reasons that will soon become apparent, it is disadvantageous to consider only closed subgroups.

Example: A non-closed subgroup. For example, even ${ \mathrm { G L } } ( n , \mathbb { R } )$ can have Lie subgroups that are not closed. Here is a simple example: Let λ be any irrational real number and define a homomorphism $\phi _ { \lambda } : \mathbb { R } \to { \mathrm { G L } } ( 4 , \mathbb { R } )$ by the formula

$$
\phi _ { \lambda } ( t ) = \left( \begin{array} { c c c c } { { \cos t } } & { { - \sin t } } & { { 0 } } & { { 0 } } \\ { { \sin t } } & { { \cos t } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \cos \lambda t } } & { { - \sin \lambda t } } \\ { { 0 } } & { { 0 } } & { { \sin \lambda t } } & { { \cos \lambda t } } \end{array} \right)
$$

Then $\phi _ { \lambda }$ is easily seen to be a one-to-one immersion so its image is a submanifold $G _ { \lambda } \subset$ GL(4, R), which is therefore a Lie subgroup. It is not hard to see that

$$
{ \overline { { G _ { \lambda } } } } = \left\{ \left. \left( { \begin{array} { c c c c } { \cos t } & { - \sin t } & { 0 } & { 0 } \\ { \sin t } & { \cos t } & { 0 } & { 0 } \\ { 0 } & { 0 } & { \cos s } & { - \sin s } \\ { 0 } & { 0 } & { \sin s } & { \cos s } \end{array} } \right) \right| s , t \in \mathbb { R } \right\} .
$$

Note that $G _ { \lambda }$ is diffeomorphic to R while its closure in GL(4, R) is diffeomorphic to $S ^ { 1 } { \times } S ^ { 1 } !$

It is also useful to consider matrix Lie groups with complex coefficients. However, complex matrix Lie groups are really no more general than real matrix Lie groups (though they may be more convenient to work with). To see why, note that one can write a complex $n { \mathrm { - } } \mathrm { b y } { \mathrm { - } } n$ matrix $A + B i$ (where A and B are real n-by-n matrices) as the 2n-by-2n matrix $\textstyle { \binom { \zeta } { B } } ^ { - B }$ . In this way, one can embed $\mathrm { G L } ( n , \mathbb { C } )$ , the space of n-by-n invertible complex matrices, as a closed submanifold of GL(2n, R). The reader should check that this mapping is actually a group homomorphism.

Among the more commonly encountered complex matrix Lie groups are the complex special linear group, denoted by $\mathrm { S L } ( n , \mathbb { C } )$ , and the unitary and special unitary groups, denoted, respectively, as

$$
\begin{array} { c } { { \mathrm { U } ( n ) = \{ a \in \mathrm { G L } ( n , \mathbb { C } ) | \mathrm { ~ } ^ { * } a a = I _ { n } \} } } \\ { { \mathrm { S U } ( n ) = \{ a \in \mathrm { U } ( n ) | \operatorname* { d e t } _ { \mathbb { C } } ( a ) = 1 \} } } \end{array}
$$

where ${ } ^ { * } a = { } ^ { t } \bar { a }$ is the Hermitian adjoint of a. These groups will play an important role in what follows. One may want to familiarize oneself with these groups by doing some of the exercises for this section.

Basic General Properties. If G is a Lie group with $a \in G$ , let $L _ { a } , R _ { a } : G \to G$ denote the smooth mappings defined by

$$
L _ { a } ( b ) = a b \qquad { \mathrm { a n d } } \qquad R _ { a } ( b ) = b a .
$$

Proposition 1: For any Lie group G, the maps $L _ { a }$ and $R _ { a }$ are diffeomorphisms, the map $\mu : G \times G \to G$ is a submersion, and the inverse mapping $\iota : G \to G$ defined by $\iota ( a ) = a ^ { - 1 }$ is smooth.

Proof: By the axioms of group multiplication, $L _ { a ^ { - 1 } }$ is both a left and right inverse to $L _ { a }$ . Since $( \dot { L } _ { a } ) ^ { - 1 }$ exists and is smooth, $L _ { a }$ is a diffeomorphism. The argument for $R _ { a }$ is similar.

In particular, $L _ { a } ^ { \prime } : T G \to T G$ induces an isomorphism of tangent spaces $T _ { b } G { \tilde {  } } T _ { a b } G$ for all $b \in G$ and ${ \cal R } _ { a } ^ { \prime } : T { \cal G }  T { \cal G }$ induces an isomorphism of tangent spaces $T _ { b } G { \tilde {  } } T _ { b a } G$ for all $b \in G$ . Using the natural identification $T _ { ( a , b ) } G \times G \simeq T _ { a } G \oplus T _ { b } G$ , the formula for $\mu ^ { \prime } ( a , b ) : T _ { ( a , b ) } G \times G \to T _ { a b } G$ is readily seen to be

$$
\mu ^ { \prime } ( a , b ) ( v , w ) = L _ { a } ^ { \prime } ( w ) + R _ { b } ^ { \prime } ( v )
$$

for all $v \in T _ { a } G$ and $w \in T _ { b } G$ . In particular $\mu ^ { \prime } ( a , b )$ is surjective for all $( a , b ) \in G \times G$ G, so $\mu : G \times G \to G$ is a submersion.

Now, by the Implicit Function Theorem, $\mu ^ { - 1 } ( e )$ is a closed, embedded submanifold of $G \times G$ whose tangent space at $( a , b )$ , by the above formula, is

$$
T _ { ( a , b ) } \mu ^ { - 1 } ( e ) = \{ ( v , w ) \in T _ { a } G \times T _ { b } G \big | L _ { a } ^ { \prime } ( w ) + R _ { b } ^ { \prime } ( v ) = 0 \} .
$$

Meanwhile, the group axioms imply that

$$
\mu ^ { - 1 } ( e ) = \left\{ ( a , a ^ { - 1 } ) \left| a \in G \right. \right\} ,
$$

which is precisely the graph of $\iota : G \to G$ . Since $L _ { a } ^ { \prime }$ and $R _ { b } ^ { \prime }$ are isomorphisms, the tangent space $T _ { ( a , b ) } \mu ^ { - 1 } ( e )$ intersects each of the subspaces $T _ { ( a , b ) } \check { ( } \{ a \} { \times } G $ and $T _ { ( a , b ) } \mathopen { } \mathclose \bgroup \left( \mathclose \bgroup { G } \times \{ b \} \aftergroup \egroup \right)$ in the trivial subspace. It then follows that the projection on the first factor $\pi _ { 1 } : G \times G \to G$ restricts to $\mu ^ { - 1 } ( e )$ to be a smooth, one-to-one map of $\mu ^ { - 1 } ( e )$ onto G that is a local diffeomorphism. The inverse of this diffeomorphism is therefore also smooth and is simply the graph of ι. It follows that ι is smooth, as desired. 

The Identity Component. For any Lie group G, let $G ^ { \circ } \subset G$ denote the connected component of G that contains e. This is usually called the identity component of G.

Proposition 2: For any Lie group G, the set $G ^ { \circ }$ is an open, normal subgroup of G. Moreover, if U is any open neighborhood of e in $G ^ { \circ }$ , then $G ^ { \circ }$ is the union of the “powers” $U ^ { n }$ defined inductively by $U ^ { 1 } = U$ and $U ^ { k + 1 } = \mu ( U ^ { k } , U )$ for $k > 0$

Proof: Since G is a manifold, its connected components are open and path-connected, so $G ^ { \circ }$ is open and path-connected. If $\alpha , \beta : [ 0 , 1 ] \to G$ are two continuous maps with $\alpha ( 0 ) = \beta ( 0 ) = e ,$ then $\gamma : [ 0 , 1 ] \to G$ defined by $\dot { \gamma } ( t ) = \alpha ( t ) \beta ( t ) ^ { - 1 }$ is a continuous path from e to $\stackrel { \cdot } { \alpha } ( 1 ) \beta ( 1 ) ^ { - 1 }$ , so $G ^ { \circ }$ is closed under multiplication and inverse, and hence is a subgroup. It is a normal subgroup since, for any $a \in G$ , the map

$$
C _ { a } = L _ { a } \circ ( R _ { a } ) ^ { - 1 } : G \to G
$$

(conjugation by $a )$ is a diffeomorphism that clearly fixes e and hence fixes its connected component $G ^ { \circ }$ also.

Finally, let $U \subset G ^ { \circ }$ be any open neighborhood of e and, setting $U ^ { 1 } = U$ , inductively define the powers $U ^ { k } = \mu ( U ^ { k - 1 } , U ) \subset G ^ { \circ }$ . Since $e \in U$ , note that $U ^ { k - 1 } \subset U ^ { k }$ and, since $\mu$ is a submersion, each of the sets $U ^ { k }$ is open, as is their union $U ^ { \infty } \subset G ^ { \circ }$

It remains to show that $U ^ { \infty } = G ^ { \circ }$ For any $a \ \in \ G ^ { \circ }$ , let $\gamma : [ 0 , 1 ] \ \to \ G ^ { \circ }$ be a continuous path with $\gamma ( 0 ) = e$ and $\gamma ( 1 ) = a$ . If a $\notin { U ^ { \infty } }$ , then by the openness of $U ^ { \infty }$ and the continuity of γ there will be a $t _ { 0 } \in ( 0 , 1 ]$ such that $\gamma ( t _ { 0 } ) \notin U ^ { \infty }$ , while $\gamma ( t ) \in U ^ { \infty }$ for all $0 ~ \leq ~ t ~ < ~ t _ { 0 }$ . By continuity, there will exist a $t \in [ 0 , t _ { 0 } )$ such that $\gamma ( t )$ lies in the open set $L _ { \gamma ( t _ { 0 } ) } \left( \iota ( U ) \right)$ (since $\iota ( U )$ is an open neighborhood of $e )$ . However, since $\gamma ( t ) = a _ { 0 } a _ { 1 } \cdot \cdot \cdot a _ { k }$ for some $a _ { i } \in U$ and since $\gamma ( t ) = \gamma ( t _ { 0 } ) b ^ { - 1 }$ for some $b \in U$ , it now follows that $\gamma ( t _ { 0 } ) = a _ { 0 } a _ { 1 } \cdot \cdot \cdot a _ { k } b ,$ i.e., that $\gamma ( t _ { 0 } )$ lies in $U ^ { k + 1 } \subset U ^ { \infty }$ . This contradiction establishes that $a \in U ^ { \infty }$ . Thus, $U ^ { \infty } = G ^ { \circ }$ 

An immediate consequence of Proposition 2 is that, for a connected Lie group H, any Lie group homomorphism $\phi : H \to G$ is determined by its behavior on any open neighborhood of $e \in H$ . We are soon going to show an even more striking fact, namely that, for connected H, any homomorphism $\phi : H \to G$ is determined by $\phi ^ { \prime } ( e ) : T _ { e } H  T _ { e } G$

The Adjoint Representation. It is conventional to denote the tangent space at the identity of a Lie group by an appropriate lower case gothic letter. Thus, the vector space $T _ { e } G$ is denoted g, the vector space $T _ { e } \mathrm { G L } ( n , \mathbb { R } )$ is denoted ${ \mathfrak { g l } } ( n , \mathbb { R } )$ , etc.

For example, one can easily compute the tangent spaces at e of the Lie groups defined so far. Here is a sample:

$$
\begin{array} { r l } & { \mathfrak { s l } ( n , \mathbb { R } ) = \{ a \in \mathfrak { g l } ( n , \mathbb { R } ) \vert \mathrm { t r } ( a ) = 0 \} } \\ & { \mathfrak { s o } ( n , \mathbb { R } ) = \{ a \in \mathfrak { g l } ( n , \mathbb { R } ) \vert a + \iota _ { a } = 0 \} } \\ & { \mathfrak { u } ( n , \mathbb { R } ) = \{ a \in \mathfrak { g l } ( n , \mathbb { C } ) \vert a + \iota _ { \bar { a } = 0 } \} } \end{array}
$$

Definition 4: For any Lie group G, the adjoint mapping is the mapping $\operatorname { A d } : G \to \operatorname { E n d } ( { \mathfrak { g } } )$ defined by

$$
\operatorname { A d } ( a ) = \left( L _ { a } \circ \left( R _ { a } \right) ^ { - 1 } \right) ^ { \prime } ( e ) : T _ { e } G \to T _ { e } G .
$$

As an example, for $G = \operatorname { G L } ( n , \mathbb { R } )$ it is easy to see that

$$
\mathrm { A d } ( a ) ( x ) = a x a ^ { - 1 }
$$

for all $a \in \operatorname { G L } ( n , \mathbb { R } )$ and $x \in { \mathfrak { g l } } ( n , \mathbb { R } )$ . Of course, this formula is valid for any matrix Lie group.

The following proposition explains why the adjoint mapping is also called the adjoint representation.

Proposition 3: The adjoint mapping is a linear representation Ad : $G \to { \mathrm { G L } } ( { \mathfrak { g } } )$

Proof: For any $a \in G .$ , let $C _ { a } = L _ { a } \circ R _ { a ^ { - 1 } }$ . Then $C _ { a } : G \to G$ is a diffeomorphism that satisfies $C _ { a } ( e ) = e$ . In particular, $\operatorname { A d } ( a ) = C _ { a } ^ { \prime } ( e ) : { \mathfrak { g } } \to { \mathfrak { g } }$ is an isomorphism and hence belongs to $\operatorname { G L } ( { \mathfrak { g } } )$

The associative property of group multiplication implies $C _ { a } \circ C _ { b } = C _ { a b }$ , so the Chain Rule implies that $C _ { a } ^ { \prime } ( e ) \circ C _ { b } ^ { \prime } ( e ) = C _ { a b } ^ { \prime } ( e )$ Hence, $\mathrm { A d } ( a ) \mathrm { A d } ( b ) = \mathrm { A d } ( a b )$ , so Ad is a homomorphism.

It remains to show that Ad is smooth. However, if $C : G \times G \to G$ is defined by $C ( a , b ) = a b a ^ { - 1 }$ , then, by Proposition 1, C is a composition of smooth maps and hence is smooth. It follows easily that the map $c : G \times { \mathfrak { g } } \to { \mathfrak { g } }$ given by $c ( a , v ) = C _ { a } ^ { \prime } ( e ) ( v ) =$ $\operatorname { A d } ( a ) ( v )$ is a composition of smooth maps. The smoothness of the map c clearly implies the smoothness of $\operatorname { A d } : G \to { \mathfrak { g } } \otimes { \mathfrak { g } } ^ { * }$ 

Left-invariant vector fields. Because $L _ { a } ^ { \prime }$ induces an isomorphism from g to $T _ { a } G$ for all $a \in G .$ , it is easy to show that the map $\Psi : G \times { \mathfrak { g } } \to T G$ given by

$$
\Psi ( a , v ) = L _ { a } ^ { \prime } ( v )
$$

is actually an isomorphism of vector bundles that makes the following diagram commute.

$$
\begin{array} { c c c } { G \times { \mathfrak { g } } } & { { \stackrel { \Psi } { \longrightarrow } } } & { T G } \\ { \pi _ { 1 } { \Big \downarrow } } & { } & { { \Big \downarrow } \pi } \\ { G } & { { \stackrel { { i d } } { \longrightarrow } } } & { G } \end{array}
$$

Note that, in particular, G is a parallelizable manifold. This implies, for example, that the only compact surface that can be given the structure of a Lie group is the torus $S ^ { 1 } \times S ^ { 1 }$

For each $v \in { \mathfrak { g } }$ , one uses Ψ to define a vector field $X _ { v }$ on G by the rule $X _ { v } ( a ) = L _ { a } ^ { \prime } ( v )$ Note that, by the Chain Rule and the definition of $X _ { v } ,$ one has

$$
L _ { a } ^ { \prime } ( X _ { v } ( b ) ) = L _ { a } ^ { \prime } ( L _ { b } ^ { \prime } ( v ) ) = L _ { a b } ^ { \prime } ( v ) = X _ { v } ( a b ) .
$$

Thus, the vector field $X _ { v }$ is invariant under left translation by any element of G. Such vector fields turn out to be extremely useful in understanding the geometry of Lie groups, and are accorded a special name:

Definition 5: If G is a Lie group, a left-invariant vector field on G is a vector field X on G that satisfies $L _ { a } ^ { \prime } ( X ( b ) ) = X ( a b )$

For example, consider $\operatorname { G L } ( n , \mathbb { R } )$ as an open subset of the vector space of n-by-n matrices with real entries. Here, ${ \mathfrak { g l } } ( n , \mathbb { R } )$ is just the vector space of n-by-n matrices with real entries itself and one easily sees that

$$
X _ { v } ( a ) = ( a , a v ) .
$$

(Since ${ \mathrm { G L } } ( n , \mathbb { R } )$ is an open subset of a vector space, namely, ${ \mathfrak { g l } } ( n , \mathbb { R } )$ , one can use the standard identification of the tangent bundle of ${ \mathrm { G L } } ( n , \mathbb { R } )$ with ${ \mathrm { G L } } ( n , \mathbb { R } ) \times { \mathfrak { g l } } ( n , \mathbb { R } ) . )$

The following proposition determines all of the left-invariant vector fields on a Lie group.

Proposition 4: Every left-invariant vector field X on G is of the form $X = X _ { v }$ where $v = X ( e )$ and hence is smooth. Moreover, such an X is complete, i.e., the flow Φ associated to X has domain $\mathbb { R } \times G$ . Finally, for all $s , t \in \mathbb { R }$ , one has

$$
\Phi ( s + t , e ) = \Phi ( s , e ) \Phi ( t , e ) .
$$

Proof: That every left-invariant vector field on G has the stated form is an easy exercise for the reader.

Let $\Phi : D  G$ be the flow of X, where $D \subset \mathbb { R } \times G$ is an open neighborhood of $\{ 0 \} \times G$ with the property that, for all $a \in G$ , there is an open interval $I _ { a } \subset \mathbb { R }$ such that $D \cap ( \mathbb { R } \times \{ a \} ) = I _ { a } \times \{ a \}$ and the curve $\gamma _ { a } : I _ { a } \to G$ defined by $\gamma _ { a } ( t ) = \Phi ( t , a )$ is the maximally extended integral curve of $X { \mathrm { ~ ( i . e . , ~ } } \gamma _ { a } ^ { \prime } ( t ) = X { \left( \gamma _ { a } ( t ) \right) }$ for all $t \in I _ { a } )$ that satisfies the initial condition $\gamma _ { a } ( 0 ) = a$ .

Note that, for any $a \in G$ , the curve

$$
\delta _ { a } ( t ) = a \gamma _ { e } ( t )
$$

satisfies $\delta _ { a } ( 0 ) = a$ and

$$
\delta _ { a } ^ { \prime } ( t ) = L _ { a } ^ { \prime } \left( \gamma _ { e } ^ { \prime } ( t ) \right) = L _ { a } ^ { \prime } \left( X \left( \gamma _ { e } ( t ) \right) \right) = X \left( a \gamma _ { e } ( t ) \right) = X \left( \delta _ { a } ( t ) \right) .
$$

Thus, it follows that $I _ { e } \subset I _ { a }$ and that

$$
\gamma _ { a } ( t ) = a \gamma _ { e } ( t )
$$

for all $t \in { \cal I } _ { e }$

Since the domain D of the flow Φ of X contains the product open set $I _ { e } \times G \subset \mathbb { R } \times G .$ it follows by standard arguments that $D = \mathbb { R } \times G , { \mathrm { i . e . } }$ , that X is complete.

Finally, because $\Phi ( s + t , e ) = \Phi \big ( t , \Phi ( s , e ) \big )$ by the properties of flows, one has, by the above formula for $\gamma _ { a }$ in terms of $\gamma _ { e }$ that

$$
\Phi ( s + t , e ) = \Phi \bigl ( t , \Phi ( s , e ) \bigr ) = \gamma _ { \Phi ( s , e ) } ( t ) = \Phi ( s , e ) \gamma _ { e } ( t ) = \Phi ( s , e ) \Phi ( t , e ) .
$$

As an example, consider the flow of the left-invariant vector fields on ${ \mathrm { G L } } ( n , \mathbb { R } )$ (or any matrix Lie group, for that matter): For any $v \in { \mathfrak { g l } } ( n , \mathbb { R } )$ , the differential equation that $\gamma _ { e }$ satisfies is simply

$$
\gamma _ { e } ^ { \prime } ( t ) = \gamma _ { e } ( t ) v .
$$

This is a matrix differential equation and, in elementary ode courses, one learns that the ‘fundamental solution’ is

$$
\gamma _ { e } ( t ) = e ^ { t v } = I _ { n } + \sum _ { k = 1 } ^ { \infty } \frac { v ^ { k } } { k ! } t ^ { k }
$$

and that this series converges uniformly on compact sets in $\mathbb { R }$ to a smooth matrix-valued function of t.

Matrix Lie groups are by far the most commonly encountered and, for this reason, one often uses the notation $\exp ( t \boldsymbol { v } )$ or even $e ^ { t v }$ for the integral curve $\gamma _ { e } ( t )$ associated to $X _ { v }$ in a general Lie group G. (Actually, in order for this notation to be unambiguous, it has to be checked that if $t v = u w$ for $t , u \in \mathbb { R }$ and $v , w \in { \mathfrak { g } }$ , then $\gamma _ { e } ( t ) = \delta _ { e } ( u )$ where $\gamma _ { e }$ is the integral curve of $X _ { v }$ with initial condition e and $\delta _ { e }$ is the integral curve of $X _ { w }$ initial condition e. However, this is an easy exercise in the use of the Chain Rule.)

It is worth remarking explicitly that for any $v \in { \mathfrak { g } }$ the formula for the flow of the left invariant vector field $X _ { v }$ on $G$ is simply

$$
\Phi ( t , a ) = a \exp ( t v ) = a e ^ { t v } .
$$

(Warning: many beginners make the mistake of thinking that the formula for the flow of the left invariant vector field $X _ { v }$ should be $\Phi ( t , a ) = \exp ( t v )$ a instead. It is worth pausing for a moment to think why this is not so.)

It is now possible to describe all of the homomorphisms from the Lie group $( \mathbb { R } , + )$ into any given Lie group:

Proposition 5: Every Lie group homomorphism $\phi : \mathbb { R }  G$ is of the form $\phi ( t ) = e ^ { t v }$ where $v = \phi ^ { \prime } ( 0 ) \in \mathfrak { g }$

Proof: Let $v = \phi ^ { \prime } ( 0 ) \in \mathfrak { g }$ , and let $X _ { v }$ be the associated left-invariant vector field on G. Since $\phi ( 0 ) = e$ , by ode uniqueness, it suffices to show that $\phi$ is an integral curve of $X _ { v }$ . However, $\phi ( s + t ) = \phi ( s ) \phi ( t )$ implies $\phi ^ { \prime } ( s ) = L _ { \phi ( s ) } ^ { \prime } \bigl ( \phi ^ { \prime } ( 0 ) \bigr ) = X _ { v } \bigl ( \phi ( s ) \bigr )$ , as desired. 

The Exponential Map. We are now ready to introduce one of the principal tools in the study of Lie groups.

Definition 6: For any Lie group, the exponential mapping of G is the mapping exp : ${ \mathfrak { g } } \to G$ defined by $\exp ( v ) = \gamma _ { e } ( 1 )$ where $\gamma _ { e }$ is the integral curve of the vector field $X _ { v }$ with initial condition e .

It is an exercise for the reader to show that exp : ${ \mathfrak { g } } \to G$ is smooth and that

$$
\exp ^ { \prime } ( 0 ) : { \mathfrak { g } }  T _ { e } G = { \mathfrak { g } }
$$

is just the identity mapping.

Example: As has been seen, for ${ \mathrm { G L } } ( n , \mathbb { R } )$ (or GL(V ) in general for that matter), the formula for the exponential mapping is just the usual power series:

$$
\begin{array} { r } { e ^ { x } = I + x + \frac { 1 } { 2 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 3 } + \cdot \cdot \cdot . } \end{array}
$$

This formula works for all matrix Lie groups as well, and can simplify considerably in certain special cases. For example, for the group $N _ { 3 }$ defined earlier (usually called the Heisenberg group), one has

$$
{ \mathfrak { n } } _ { 3 } = \{ { ( \begin{array} { l l l } { 0 } & { x } & { z } \\ { 0 } & { 0 } & { y } \\ { 0 } & { 0 } & { 0 } \end{array} ) } \ { | \begin{array} { l } { x , y , z \in \mathbb { R } } \\ { } \end{array} \} } ,
$$

and $v ^ { 3 } = 0$ for all $v \in { \mathfrak { n } } _ { 3 }$ . Thus

$$
\exp \left( { \left( { \begin{array} { c c c } { 0 } & { x } & { z } \\ { 0 } & { 0 } & { y } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) } \right) = { \left( { \begin{array} { c c c } { 1 } & { x } & { z + { \frac { 1 } { 2 } } x y } \\ { 0 } & { 1 } & { y } \\ { 0 } & { 0 } & { 1 } \end{array} } \right) } .
$$

The Lie Bracket. Now, the mapping exp is not generally a homomorphism from g (with its additive group structure) to $G ,$ although, in a certain sense, it comes as close as possible, since, by construction, it is a homomorphism when restricted to any onedimensional linear subspace $\mathbb { R } v \subset { \mathfrak { g } }$ We now want to spend a few moments considering what the multiplication map on G “looks like” when pulled back to g via exp.

Since $\exp ^ { \prime } ( 0 ) : { \mathfrak { g } }  T _ { e } G = { \mathfrak { g } }$ is the identity mapping, it follows from the Implicit Function Theorem that there is a neighborhood U of $0 ~ \in ~ { \mathfrak { g } } ~ \operatorname { s o }$ that exp $\colon U  G$ is a diffeomorphism onto its image. Moreover, there must be a smaller open neighborhood $V \subset U$ of 0 so that $\mu ( \exp ( V ) \times \exp ( V ) ) \subset \exp ( U )$ . It follows that there is a unique smooth mapping $\nu : V \times V \to U$ such that

$$
\mu \left( \exp ( x ) , \exp ( y ) \right) = \exp \left( \nu ( x , y ) \right) .
$$

Since exp is a homomorphism restricted to each line through 0 in g, it follows that ν satisfies

$$
\nu ( \alpha x , \beta x ) = ( \alpha + \beta ) x
$$

for all $x \in V$ and $\alpha , \beta \in \mathbb { R }$ such that αx, $\beta x \in V$

Since $\nu ( 0 , 0 ) = 0$ , the Taylor expansion to second order of ν about (0, 0) is of the form,

$$
\begin{array} { r } { \nu ( x , y ) = \nu _ { 1 } ( x , y ) + \frac { 1 } { 2 } \nu _ { 2 } ( x , y ) + R _ { 3 } ( x , y ) } \end{array}
$$

where $\nu _ { i }$ is a g-valued polynomial of degree i on the vector space ${ \mathfrak { g } } \oplus { \mathfrak { g } }$ and $R _ { 3 }$ is a g-valued function on V that vanishes to at least third order at (0, 0).Since $\nu ( x , 0 ) = \nu ( 0 , x ) = x .$ , it easily follows that $\nu _ { 1 } ( x , y ) = x + y$ and that $\nu _ { 2 } ( x , 0 ) =$ $\nu _ { 2 } ( 0 , y ) = 0$ . Thus, the quadratic polynomial $\nu _ { 2 }$ is linear in each g-variable separately.

Moreover, since $\nu ( x , x ) = 2 x$ for all $x \in V$ , substituting this into the above expansion and comparing terms of order 2 yields that $\nu _ { 2 } ( x , x ) \equiv 0$ . Of course, this implies that $\nu _ { 2 }$ is actually skew-symmetric since

$$
0 = \nu _ { 2 } ( x + y , x + y ) - \nu _ { 2 } ( x , x ) - \nu _ { 2 } ( y , y ) = \nu _ { 2 } ( x , y ) + \nu _ { 2 } ( y , x ) .
$$

Definition 7: The skew-symmetric, bilinear multiplication $[ , ] : { \mathfrak { g } } \times { \mathfrak { g } } \to { \mathfrak { g } }$ defined by

$$
[ x , y ] = \nu _ { 2 } ( x , y )
$$

is called the Lie bracket in g. The pair $( { \mathfrak { g } } , [ , ] )$ is called the Lie algebra of G.

With this notation, one obtains a formula

$$
\begin{array} { r } { \exp ( x ) \exp ( y ) = \exp \bigl ( x + y + \frac 1 2 [ x , y ] + R _ { 3 } ( x , y ) \bigr ) } \end{array}
$$

valid for all x and y in some fixed open neighborhood of 0 in g.

One might think of the term involving [, ] as the first deviation of the Lie group multiplication from being just vector addition. In fact, it is clear from the above formula that, if the group G is abelian, then $[ x , y ] = 0$ for all $x , y \in { \mathfrak { g } }$ . For this reason, a Lie algebra in which all brackets vanish is called an abelian Lie algebra. (In fact, (see the Exercises) g being abelian implies that $G ^ { \circ }$ , the identity component of $G ,$ is abelian.)

Example : If $G = \operatorname { G L } ( n , \mathbb { R } )$ , then it is easy to see that the induced bracket operation on ${ \mathfrak { g l } } ( n , \mathbb { R } )$ , the vector space of n-by-n matrices, is just the matrix “commutator”

$$
[ x , y ] = x y - y x .
$$

In fact, the reader can verify this by examining the following second order expansion:

$$
\begin{array} { l } { e ^ { x } e ^ { y } = ( I _ { n } + x + \frac { 1 } { 2 } x ^ { 2 } + \cdot \cdot \cdot ) ( I _ { n } + y + \frac { 1 } { 2 } y ^ { 2 } + \cdot \cdot \cdot ) } \\ { = ( I _ { n } + x + y + \frac { 1 } { 2 } ( x ^ { 2 } + 2 x y + y ^ { 2 } ) + \cdot \cdot \cdot ) } \\ { = ( I _ { n } + ( x + y + \frac { 1 } { 2 } [ x , y ] ) + \frac { 1 } { 2 } ( x + y + \frac { 1 } { 2 } [ x , y ] ) ^ { 2 } + \cdot \cdot \cdot ) } \end{array}
$$

Moreover, this same formula is easily seen to hold for any x and y in ${ \mathfrak { g l } } ( V )$ where V is any finite dimensional vector space.

Theorem 1: $I f \phi : H \to G$ is a Lie group homomorphism, then $\varphi = \phi ^ { \prime } ( e ) : { \mathfrak { h } } \to { \mathfrak { g } }$ satisfies

$$
\exp _ { G } ( \varphi ( x ) ) = \phi ( \exp _ { H } ( x ) )
$$

for all $x \in { \mathfrak { h } }$ . In other words, the diagram

$$
{ \mathfrak { h } } \quad { \xrightarrow { \varphi } } \quad { \mathfrak { g } }
$$

$$
\left. \begin{array} { c c c } { { \exp _ { H } } } \\ { { \downarrow } } & { { } } & { { \downarrow ^ { \exp _ { G } } } } \\ { { H } } & { { \stackrel { \phi } { \longrightarrow } } } & { { G } } \end{array} \right.
$$

commutes. Moreover, for all x and y in h,

$$
\varphi ( [ x , y ] _ { H } ) = [ \varphi ( x ) , \varphi ( y ) ] _ { G } .
$$

Proof: The first statement is an immediate consequence of Proposition 5 and the Chain Rule since, for every $x \in { \mathfrak { h } }$ , the map $\gamma : \mathbb { R } \to G$ given by $\gamma ( t ) = \phi ( e ^ { t x } )$ is clearly a Lie group homomorphism with initial velocity $\gamma ^ { \prime } ( 0 ) = \varphi ( x )$ and hence must also satisfy $\gamma ( t ) = e ^ { t \varphi ( x ) }$

To get the second statement, let x and y be elements of h that are sufficiently close to zero. Then, using self-explanatory notation:

$$
\phi ( \exp _ { H } ( x ) \exp _ { H } ( y ) ) = \phi ( \exp _ { H } ( x ) ) \phi ( \exp _ { H } ( y ) ) ,
$$

so

$$
\begin{array} { r } { \phi ( \exp _ { H } ( x + y + \frac { 1 } { 2 } [ x , y ] _ { H } + R _ { 3 } ^ { H } ( x , y ) ) ) = \exp _ { G } ( \varphi ( x ) ) \exp _ { G } ( \varphi ( y ) ) , } \end{array}
$$

and thus

$$
\begin{array} { r } { \exp _ { G } ( \varphi ( x + y + \frac { 1 } { 2 } [ x , y ] _ { H } + R _ { 3 } ^ { H } ( x , y ) ) ) = \exp _ { G } ( \varphi ( x ) + \varphi ( y ) + \frac { 1 } { 2 } [ \varphi ( x ) , \varphi ( y ) ] _ { G } + R _ { 3 } ^ { G } ( \varphi ( x ) , \varphi ( y ) ) ) , } \end{array}
$$

finally giving

$$
\begin{array} { r } { \varphi ( x + y + \frac { 1 } { 2 } [ x , y ] _ { H } + R _ { 3 } ^ { H } ( x , y ) ) = \varphi ( x ) + \varphi ( y ) + \frac { 1 } { 2 } [ \varphi ( x ) , \varphi ( y ) ] _ { G } + R _ { 3 } ^ { G } ( \varphi ( x ) , \varphi ( y ) ) . } \end{array}
$$

Now using the fact that $\varphi$ is linear and comparing second order terms gives the desired result. 

On account of this theorem, it is usually not necessary to distinguish the map exp or the bracket [, ] according to the group in which it is being applied, so I will follow this practice also. Henceforth, these symbols will be used without group decorations whenever confusion seems unlikely.

Theorem 1 has many useful corollaries. Among them is

Proposition 6: If H is a connected Lie group and $\phi _ { 1 } , \phi _ { 2 } : H \to G$ are two Lie group homomorphisms that satisfy $\phi _ { 1 } ^ { \prime } ( e ) = \phi _ { 2 } ^ { \prime } ( e )$ , then $\phi _ { 1 } = \phi _ { 2 }$

Proof: There is an open neighborhood U of e in H so that $\mathrm { e x p } _ { H }$ is invertible on this neighborhood with inverse satisfying $\exp _ { H } ^ { - 1 } ( e ) = 0$ . Then for $a \in U$ one has, by Theorem 1,

$$
\phi _ { i } ( a ) = \mathrm { e x p } _ { G } ( \varphi _ { i } ( \mathrm { e x p } _ { H } ^ { - 1 } ( a ) ) ) .
$$

Since $\varphi _ { 1 } = \varphi _ { 2 }$ , one has $\phi _ { 1 } = \phi _ { 2 }$ on U. By Proposition 2, every element of H can be written as a finite product of elements of U, so one must have $\phi _ { 1 } = \phi _ { 2 }$ everywhere. 

We also have the following fundamental result:

Proposition 7: If $\operatorname { A d } : G \to \operatorname { G L } ( { \mathfrak { g } } )$ is the adjoint representation, then ad $= \operatorname { A d } ^ { \prime } ( e ) : { \mathfrak { g } } \to$ ${ \mathfrak { g l } } ( { \mathfrak { g } } )$ is given by the formula $\operatorname { a d } ( x ) ( y ) = [ x , y ]$ . In particular, one has the Jacobi identity

$$
\operatorname { a d } ( [ x , y ] ) = [ \operatorname { a d } ( x ) , \operatorname { a d } ( y ) ] .
$$

Proof: This is simply a matter of unwinding the definitions. By definition, $\operatorname { A d } ( a ) = C _ { a } ^ { \prime } ( e )$ where $C _ { a } : G \to G$ is defined by $C _ { a } ( b ) = a b a ^ { - 1 }$ . In order to compute $C _ { a } ^ { \prime } ( e ) ( y )$ for $y \in { \mathfrak { g } }$

one may just compute $\gamma ^ { \prime } ( 0 )$ where $\gamma$ is the curve $\gamma ( t ) = a \exp ( t y ) a ^ { - 1 }$ . Moreover, since $\exp ^ { \prime } ( 0 ) : { \mathfrak { g } } \to { \mathfrak { g } }$ is the identity, one may as well compute $\beta ^ { \prime } ( 0 )$ where $\beta = \exp ^ { - 1 } \circ \gamma$ . Now, assuming $a = \exp ( x )$ , one computes

$$
{ \begin{array} { r l } & { \beta ( t ) = \exp ^ { - 1 } ( \exp ( x ) \exp ( t y ) \exp ( - x ) ) } \\ & { \qquad = \exp ^ { - 1 } ( \exp ( x + t y + { \frac { 1 } { 2 } } [ x , t y ] + \cdot \cdot \cdot ) \exp ( - x ) ) } \\ & { \qquad = \exp ^ { - 1 } ( \exp ( ( x + t y + { \frac { 1 } { 2 } } [ x , t y ] ) + ( - x ) + { \frac { 1 } { 2 } } [ x + t y , - x ] + \cdot \cdot \cdot ) } \\ & { \qquad = t y + t [ x , y ] + E _ { 3 } ( x , t y ) } \end{array} }
$$

where the omitted terms and the function $E _ { 3 }$ vanish to order at least 3 at $( x , y ) = ( 0 , 0 )$ (Note that I used the identity $[ y , x ] = - [ x , y ] . )$ It follows that

$$
\mathrm { A d } ( \exp ( x ) ) ( y ) = \beta ^ { \prime } ( 0 ) = y + [ x , y ] + E _ { 3 } ^ { \prime } ( x , 0 ) y
$$

where $E _ { 3 } ^ { \prime } ( x , 0 )$ denotes the derivative of $E _ { 3 }$ with respect to y evaluated at $( x , 0 )$ and is hence a function of x that vanishes to order at least 2 at $x = 0$ . On the other hand, by the first part of Theorem 1,

$$
\mathrm { A d } ( \exp ( x ) ) = \exp ( \operatorname { a d } ( x ) ) = I + \operatorname { a d } ( x ) + { \textstyle { \frac { 1 } { 2 } } } ( \operatorname { a d } ( x ) ) ^ { 2 } + \cdots .
$$

Comparing the x-linear terms in the last two equations clearly gives the desired result. The validity of the Jacobi identity now follows by applying the second part of Theorem 1 to Proposition 3. 

The Jacobi identity is often presented differently. The reader can verify that the equation ad $\bigl ( [ x , y ] \bigr ) = \bigl [ \mathrm { a d } ( x ) , \mathrm { a d } ( y ) \bigr ]$ where ad $1 ( x ) ( y ) = [ x , y ]$ is equivalent to the condition that

$$
[ [ x , y ] , z ] + [ [ y , z ] , x ] + [ [ z , x ] , y ] = 0 \qquad { \mathrm { f o r ~ a l l } } \quad z \in { \mathfrak { g } } .
$$

This is a form in which the Jacobi identity is often stated. Unfortunately, although this is a very symmetric form of the identity, it somewhat obscures its importance and meaning.

The Jacobi identity is so important that the class of algebras in which it holds is given a name:

Definition 8: A Lie algebra is a pair $\left( { \mathfrak { g } } , \left[ , \right] \right)$ where g is a vector space and $[ , ] : { \mathfrak { g } } \times { \mathfrak { g } } \to { \mathfrak { g } }$ i s a skew-symmetric bilinear multiplication that satisfies the Jacobi identity, i.e., ad $( [ x , y ] ) =$ $[ \operatorname { a d } ( x ) , \operatorname { a d } ( y ) ]$ , where ad : ${ \mathfrak { g } } \to { \mathfrak { g l } } ( { \mathfrak { g } } )$ is defined by ad $( x ) ( y ) = [ x , y ] \mathrm { ~ A ~ }$ Lie subalgebra of g is a linear subspace ${ \mathfrak { h } } \subset { \mathfrak { g } }$ that is closed under bracket. A homomorphism of Lie algebras is a linear mapping of vector spaces $\varphi : { \mathfrak { h } }  { \mathfrak { g } }$ that satisfies

$$
\varphi \big ( [ x , y ] \big ) = \big [ \varphi ( x ) , \varphi ( y ) \big ] .
$$

The only examples of Lie algebras encountered so far are the ones provided by Proposition 6, namely, the Lie algebras of Lie groups. This is not accidental, for, as will be seen, every finite dimensional Lie algebra is the Lie algebra of some Lie group.

Lie Brackets of Vector Fields. There is another notion of Lie bracket, namely the Lie bracket of smooth vector fields on a smooth manifold. This bracket is also skewsymmetric and satisfies the Jacobi identity, so it is reasonable to ask how it might be related to the notion of Lie bracket that has already been defined. Since Lie bracket of vector fields commutes with diffeomorphisms, it easily follows that the Lie bracket of two left-invariant vector fields on a Lie group G is also a left-invariant vector field on G. The following result is, perhaps then, to be expected.

Proposition 8: For any $x , y \in { \mathfrak { g } }$ , one has $[ X _ { x } , X _ { y } ] = X _ { [ x , y ] }$

Proof: This is a direct calculation. For simplicity, I will use the following characterization of the Lie bracket for vector fields: If $\Phi _ { x }$ and $\Phi _ { y }$ are the flows associated to the vector fields $X _ { x }$ and $X _ { y }$ , then for any function $f$ on G one has the formula:

$$
( [ X _ { x } , X _ { y } ] f ) ( a ) = \operatorname* { l i m } _ { t \to 0 ^ { + } } { \frac { f \bigl ( \Phi _ { y } ( - { \sqrt { t } } , \Phi _ { x } ( - { \sqrt { t } } , \Phi _ { y } ( { \sqrt { t } } , \Phi _ { x } ( { \sqrt { t } } , a ) ) ) ) \bigr ) - f ( a ) } { t } } .
$$

Now, as has been seen, the formulas for the flows of $X _ { x }$ and $X _ { y }$ are given by $\Phi _ { x } ( t , a ) =$ a exp(tx) and $\Phi _ { y } ( t , a ) = a \exp ( t y )$ . This implies that the general formula above simplifies to

$$
( [ X _ { x } , X _ { y } ] f ) ( a ) = \operatorname* { l i m } _ { t \to 0 ^ { + } } { \frac { f { \big ( } a \exp ( { \sqrt { t } } x ) \exp ( { \sqrt { t } } y ) \exp ( - { \sqrt { t } } x ) \exp ( - { \sqrt { t } } y ) { \big ) } - f ( a ) } { t } } .
$$

Now

$$
\begin{array} { r } { \exp ( \pm \sqrt { t } x ) \exp ( \pm \sqrt { t } y ) = \exp ( \pm \sqrt { t } ( x + y ) + \frac { t } { 2 } [ x , y ] + \cdot \cdot \cdot ) } \end{array}
$$

so $\exp ( \sqrt { t } x ) \exp ( \sqrt { t } y ) \exp ( - \sqrt { t } x ) \exp ( - \sqrt { t } y )$ simplifies to $\exp ( t [ x , y ] + \cdot \cdot \cdot )$ where the omitted terms vanish to higher t-order than t itself. Thus,

$$
( [ X _ { x } , X _ { y } ] f ) ( a ) = \operatorname* { l i m } _ { t \to 0 ^ { + } } { \frac { f { \big ( } a \exp ( t [ x , y ] + \cdot \cdot \cdot ) { \big ) } - f ( a ) } { t } } .
$$

Since $[ X _ { x } , X _ { y } ]$ must be a left-invariant vector field and since

$$
( X _ { [ x , y ] } f ) ( a ) = \operatorname* { l i m } _ { t \to 0 ^ { + } } { \frac { f { \big ( } a \exp ( t [ x , y ] ) { \big ) } - f ( a ) } { t } } ,
$$

the desired result follows.

We can now prove the following fundamental result.

Theorem 2: For each Lie subgroup H of a Lie group G, the subspace $\mathfrak { h } = T _ { e } H$ is a Lie subalgebra of g. Moreover, every Lie subalgebra ${ \mathfrak { h } } \subset { \mathfrak { g } }$ is $T _ { e } H$ for a unique connected Lie subgroup H of G.

Proof: Suppose that $H \subset G$ is a Lie subgroup. Then the inclusion map is a Lie group homomorphism and Theorem 1 thus implies that the inclusion map ${ \mathfrak { h } } \hookrightarrow { \mathfrak { g } }$ is a Lie algebra homomorphism. In particular, h, when considered as a subspace of g, is closed under the Lie bracket in G and hence is a subalgebra.

Suppose now that ${ \mathfrak { h } } \subset { \mathfrak { g } }$ is a subalgebra.

First, let us show that there is at most one connected Lie subgroup of G with Lie algebra h. Suppose that there were two, say $H _ { 1 }$ and $H _ { 2 }$ . Then by Theorem $1 , \exp _ { G } ( { \mathfrak { h } } )$ is a subset of both $H _ { 1 }$ and $H _ { 2 }$ and contains an open neighborhood of the identity element in each of them. However, since, by Proposition 2, each of $H _ { 1 }$ and $H _ { 2 }$ are generated by finite products of the elements in any open neighborhood of the identity, it follows that $H _ { 1 } \subset H _ { 2 }$ and $H _ { 2 } \subset H _ { 1 }$ , so $H _ { 1 } = H _ { 2 }$ , as desired.

Second, the existence of a subgroup H with $T _ { e } H = \mathfrak { h }$ , will be proved by calling on the Global Frobenius Theorem. Let $r = \dim ( { \mathfrak { h } } )$ and let $E \subset T G$ be the rank r subbundle spanned by the vector fields $X _ { x }$ where $x \in { \mathfrak { h } }$ . Note that $E _ { a } = L _ { a } ^ { \prime } ( E _ { e } ) = L _ { a } ^ { \prime } ( \mathfrak { h } )$ for all $a \in G$ , so $E$ is left-invariant. Since h is a subalgebra of g, Proposition 8 implies that E is an integrable distribution on G. By the Global Frobenius Theorem, there is an r-dimensional leaf of E passing through e. Call this E-leaf H.

It remains to show that H is closed under multiplication and inverse. To do this, first note that, because E is left-invariant, it follows that, for any $a \in G$ , the leaf of E that passes through a is $L _ { a } ( H ) = a H$ . Now, if a lies in H, then $a H \cap H$ contains a (since H contains e) and hence the two E-leaves aH and H must be equal. Since $a H = H$ it follows that ab lies in H if both a and b do, so that H is closed under multiplication. Since $a H = H$ and H passes through e, it follows that there is a $b \in H$ such that $a b = e$ . Thus, $b = a ^ { - 1 }$ belongs to H as well. Thus, H is closed under inverse. 

Theorem 3: If H is a connected and simply connected Lie group, then, for any Lie group G, each Lie algebra homorphism $\varphi : { \mathfrak { h } }  { \mathfrak { g } }$ is of the form $\varphi = \phi ^ { \prime } ( e )$ for some unique Lie group homorphism $\phi : H \to G$

Proof: In light of Theorem 1 and Proposition 6, all that remains to be proved is that for each Lie algebra homorphism $\varphi : { \mathfrak { h } }  { \mathfrak { g } }$ there exists a Lie group homomorphism $\phi$ satisfying $\phi ^ { \prime } ( e ) = \varphi$

We do this as follows: Suppose that $\varphi : { \mathfrak { h } } \to { \mathfrak { g } }$ is a Lie algebra homomorphism. Consider the product Lie group $H \times G$ . Its Lie algebra is h ⊕ g with Lie bracket given by $[ ( h _ { 1 } , g _ { 1 } ) , ( h _ { 2 } , g _ { 2 } ) ] = ( [ h _ { 1 } , h _ { 2 } ] , [ g _ { 1 } , g _ { 2 } ] )$ , as is easily verified. Now consider the subspace ${ \widehat { \mathfrak { h } } } \subset { \mathfrak { h } } \oplus { \mathfrak { g } }$ spanned by elements of the form $( x , \varphi ( x ) )$ where $x \in { \mathfrak { h } }$ . Since $\varphi$ is a Lie algebra homomorphism, $\widehat { \mathfrak { h } }$ is a Lie subalgebra of ${ \mathfrak { h } } \oplus { \mathfrak { g } }$ (and happens to be isomorphic to h). In particular, by Theorem 2, it follows that there is a connected Lie subgroup ${ \widehat { H } } \subset H \times G .$ whose Lie algebra is $\widehat { \mathfrak { h } }$ . We are now going to show that $\widehat { H }$ is the graph of the desired Lie group homomorphism $\phi : H \to G$

Note that since $\widehat { H }$ is a Lie subgroup of $H \times G$ , the projections $\pi _ { 1 } : { \widehat { H } }  H$ and $\pi _ { 2 } : { \widehat { H } }  G$ ^ arnd homomorphisms. Tare clearly given by e algand s. $\varpi _ { 1 } : { \mathfrak { h } } \to { \mathfrak { h } }$ $\varpi _ { 2 } : { \mathfrak { h } } \to { \mathfrak { g } }$ $\varpi _ { 1 } ( x , \varphi ( x ) ) = x$ $\varpi _ { 2 } ( x , \varphi ( x ) ) = \varphi ( x )$

Now, I claim that $\pi _ { 1 }$ is actually a surjective covering map: It is surjective since $\varpi _ { 1 } : \widehat { \mathfrak { h } }  \mathfrak { h }$ is an isomorphism so $\pi _ { 1 } ( \widehat { H } )$ contains a neighborhood of the identity in H and hence, by Proposition 2 and the connectedness of H, must contain all of H. It remains to show that, under $\pi _ { 1 }$ , points of H have evenly covered neighborhoods.

Let ${ \widehat Z } = \ker ( \pi _ { 1 } )$ Then $\widehat { Z }$ is a closed discrete subgroup of $\widehat { H }$ . Let ${ \widehat { U } } \subset { \widehat { H } }$ be a neighborhood of the identity to which $\pi _ { 1 }$ restricts to be a smooth diffeomorphism onto a neighborhood U of e in H. Then the reader can easily verify that for each $a \in { \widehat { H } }$ the map $\overset { \smile } { \sigma } _ { a } : \widehat { Z } \times \widehat { U } \to \widehat { H }$ given by $\sigma _ { a } ( z , u ) = a z u$ is a diffeomorphism onto $( \pi _ { 1 } ) ^ { - 1 } ( L _ { \pi _ { 1 } ( a ) } ( U ) )$ that commutes with the appropriate projections and hence establishes the even covering property.

Finally, since $\widehat { H }$ is connected and, by hypothesis, H is simply connected, it follows that $\pi _ { 1 }$ must actually be a one-to-one and onto diffeomorphism. The map $\phi = \pi _ { 2 } \circ \pi _ { 1 } ^ { - 1 }$ is then the desired homomorphism. 

As one final general Theorem, I state, without proof, the following existence result.

Theorem 4: For each finite dimensional Lie algebra g, there exists a Lie group G whose Lie algebra is isomorphic to g.

Unfortunately, this theorem is surprisingly difficult to prove. It would suffice, by Theorem 2, to show that every Lie algebra g is isomorphic to a subalgebra of the Lie algebra of a Lie group. In fact, an even stronger statement is true. A theorem of Ado asserts that every finite dimensional Lie algebra is isomorphic to a subalgebra of ${ \mathfrak { g l } } ( n , \mathbb { R } )$ for some n. Thus, to prove Theorem 4, it would be enough to prove Ado’s theorem. Unfortunately, this theorem also turns out to be rather delicate (see [Po] for a proof). However, there are many interesting examples of g for which a proof can be given by elementary means (see the Exercises).

On the other hand, this abstract existence theorem is not used very often anyway. It is rare that a (finite dimensional) Lie algebra arises in practice that is not readily representable as the Lie algebra of some Lie group.

The reader may be wondering about uniqueness: How many Lie groups are there whose Lie algebras are isomorphic to a given ${ \mathfrak { g } } ?$ Since the Lie algebra of a Lie group G only depends on the identity component $G ,$ it is reasonable to restrict to the case of connected Lie groups. Now, as you are asked to show in the Exercises, the universal cover $\tilde { G }$ of a connected Lie group $G$ can be given a unique Lie group structure for which the covering map $\tilde { G }  G$ is a homomorphism. Thus, there always exists a connected and simply connected Lie group, say $G ( { \mathfrak { g } } )$ , whose Lie algebra is isomorphic to g. A simple application of Theorem 3 shows that if $G ^ { \prime }$ is any other Lie group with Lie algebra g, then there is a homomorphism $\phi : G ( { \mathfrak { g } } ) \to G$ that induces an isomorphism on the Lie algebras. It follows easily that, up to isomorphism, there is only one simply-connected and connected Lie group with Lie algebra g. Moreover, every other connected Lie group with Lie algebra G is isomorphic to a quotient of $G ( { \mathfrak { g } } )$ by a discrete subgroup of G that lies in the center of $G ( { \mathfrak { g } } )$ (see the Exercises).

The Structure Constants. Our work so far has shown that the problem of classifying the connected Lie groups up to isomorphism is very nearly the same thing as classifying the (finite dimensional) Lie algebras. (See the Exercises for a clarification of this point.) This is a remarkable state of affairs, since, a priori, Lie groups involve the topology of smooth manifolds and it is rather surprising that their classification can be reduced to what is essentially an algebra problem. It is worth taking a closer look at this algebra problem itself.

Let g be a Lie algebra of dimension n, and let $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ be a basis for ${ \mathfrak { g } } .$ . Then there exist constants $\overset { \vartriangle } { c _ { i j } ^ { k } }$ so that (using the summation convention)

$$
[ x _ { i } , x _ { j } ] = c _ { i j } ^ { k } x _ { k } .
$$

(These quantities c are called the structure constants of g relative to the given basis.) The skew-symmetry of the Lie bracket is is equivalent to the skew-symmetry of c in its lower indices:

$$
c _ { i j } ^ { k } + c _ { j i } ^ { k } = 0 .
$$

The Jacobi identity is equivalent to the quadratic equations:

$$
\begin{array} { r } { c _ { i j } ^ { \ell } c _ { k \ell } ^ { m } + c _ { j k } ^ { \ell } c _ { i \ell } ^ { m } + c _ { k i } ^ { \ell } c _ { j \ell } ^ { m } = 0 . } \end{array}
$$

Conversely, any set of $n ^ { 3 }$ constants satisfying these relations defines an n-dimensional Lie algebra by the above bracket formula.

Of course, because of the skew-symmetry of the bracket, only $n { \binom { n } { 2 } }$ of these constants are independent. In fact, using the dual basis $x ^ { 1 } , \ldots , x ^ { n }$ of ${ \mathfrak { g } } ^ { * }$ , one can write the expression for the Lie bracket as an element $\beta \in { \mathfrak { g } } \otimes \Lambda ^ { 2 } ( { \mathfrak { g } } ^ { * } )$ , in the form

$$
\begin{array} { r } { \beta = \frac 1 2 c _ { j k } ^ { i } x _ { i } \otimes x ^ { j } \wedge x ^ { k } . } \end{array}
$$

The Jacobi identity is then equivalent to the condition $J ( \beta ) = 0$ , where

$$
J : { \mathfrak { g } } \otimes \Lambda ^ { 2 } ( { \mathfrak { g } } ^ { * } ) \to { \mathfrak { g } } \otimes \Lambda ^ { 3 } ( { \mathfrak { g } } ^ { * } )
$$

is the quadratic polynomial map given in coordinates by

$$
\begin{array} { r } { J ( \beta ) = \frac { 1 } { 6 } \left( c _ { i j } ^ { \ell } c _ { k \ell } ^ { m } + c _ { j k } ^ { \ell } c _ { i \ell } ^ { m } + c _ { k i } ^ { \ell } c _ { j \ell } ^ { m } \right) x _ { m } \otimes x ^ { i } \wedge x ^ { j } \wedge x ^ { k } . } \end{array}
$$

Left-Invariant Forms and the Structure Equations. Dual to the left-invariant vector fields on a Lie group $G ,$ there are the left-invariant 1-forms, which are indispensable as calculational tools.

Definition 9: For any Lie group $G ,$ the g-valued 1-form on G defined by

$$
\omega _ { G } ( v ) = L _ { a ^ { - 1 } } ^ { \prime } ( v ) \qquad { \mathrm { f o r ~ } } v \in T _ { a } G
$$

is called the canonical left-invariant 1-form on $G .$

It is easy to see that $\omega _ { G }$ is smooth. Moreover, $\omega _ { G }$ is the unique left-invariant g-valued 1-form on G that satisfies $\omega _ { G } ( v ) = v$ for all $v \in { \mathfrak { g } } = T _ { e } G$ .

By a calculation that is left as an exercise for the reader,

$$
\phi ^ { * } ( \omega _ { G } ) = \varphi ( \omega _ { H } )
$$

for any Lie group homomorphism $\phi : H \to G$ with $\varphi = \phi ^ { \prime } ( e )$ . In particular, when H is a subgroup of $G ,$ the pull back of $\omega _ { G }$ to H via the inclusion mapping is just $\omega _ { H }$ . For this reason, it is common to simply write $\omega$ for $\omega _ { G }$ when there is no danger of confusion.

Example: If $G \subset \operatorname { G L } ( n , \mathbb { R } )$ is a matrix Lie group, then one may regard the inclusion $g : G \to { \mathrm { G L } } ( n , \mathbb { R } )$ as a matrix-valued function on G and compute that $\omega$ is given by the simple formula

$$
\omega = g ^ { - 1 } d g .
$$

From this formula, the left-invariance of $\omega$ is obvious.

In the matrix Lie group case, it is also easy to compute the exterior derivative of ω: Since $g g ^ { - 1 } = I _ { n }$ , one obtains

$$
d g g ^ { - 1 } + g d \bigl ( g ^ { - 1 } \bigr ) = 0 ,
$$

so

$$
d \left( g ^ { - 1 } \right) = - g ^ { - 1 } d g g ^ { - 1 } .
$$

This implies the formula

$$
d \omega = - \omega \wedge \omega .
$$

(Warning: Matrix multiplication is implicit in this formula!)

For a general Lie group, the formula for $d \omega$ is only slightly more complicated. To state the result, let me first define some notation. I will use $[ \omega , \omega ]$ to denote the g-valued 2-form on $G$ whose value on a pair of vectors $v , w \in T _ { a } G$ is

$$
[ \omega , \omega ] ( v , w ) = [ \omega ( v ) , \omega ( w ) ] - [ \omega ( w ) , \omega ( v ) ] = 2 [ \omega ( v ) , \omega ( w ) ] .
$$

Proposition 9: For any Lie group G, $\begin{array} { r } { d \omega = - \frac { 1 } { 2 } [ \omega , \omega ] } \end{array}$

Proof: First, let $X _ { v }$ and $X _ { w }$ be the left-invariant vector fields on G whose values at e are v and w respectively. Then, by the usual formula for the exterior derivative

$$
d \omega ( X _ { v } , X _ { w } ) = X _ { v } { \big ( } \omega ( X _ { w } ) { \big ) } - X _ { w } { \big ( } \omega ( X _ { v } ) { \big ) } - \omega { \big ( } [ X _ { v } , X _ { w } ] { \big ) } .
$$

However, the g-valued functions $\omega ( X _ { v } )$ and $\omega ( X _ { w } )$ are clearly left-invariant and hence are constants and equal to v and w respectively. Moreover, by Proposition 8, $[ X _ { v } , X _ { w } ] =$ $X _ { [ v , w ] }$ , so the formula simplifies to

$$
d \omega ( X _ { v } , X _ { w } ) = - \omega ( X _ { [ v , w ] } ) .
$$

The right hand side is, again, a left-invariant function, so it must equal its value at the identity, which is clearly $- [ v , w ]$ , that equals $- [ \omega ( X _ { v } ) , \omega ( X _ { w } ) ]$ Thus,

$$
\begin{array} { r } { d \omega ( X _ { v } , X _ { w } ) = - \frac { 1 } { 2 } [ \omega ( X _ { v } ) , \omega ( X _ { w } ) ] } \end{array}
$$

for any pair of left-invariant vector fields on G. Since any pair of vectors in $T _ { a } G$ can be written as $X _ { v } ( a )$ and $X _ { w } ( a )$ for some $v , w \in { \mathfrak { g } }$ , the result follows. 

The formula proved in Proposition 9 is often called the structure equation of Maurer and Cartan. It is also usually expressed slightly differently. If $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ is a basis for g with structure constants $c _ { j k } ^ { i }$ , then ω can be written in the form

$$
\omega = x _ { 1 } \omega ^ { 1 } + \cdot \cdot \cdot + x _ { n } \omega ^ { n }
$$

where the $\omega ^ { i }$ are R-valued left-invariant 1-forms and Proposition 9 can then be expanded to give

$$
\begin{array} { r } { d \omega ^ { i } = - \frac { 1 } { 2 } c _ { j k } ^ { i } \omega ^ { j } \wedge \omega ^ { k } , } \end{array}
$$

which is the most common form in which the structure equations are given. Note that the identity $d ( d ( \omega ^ { i } ) ) = 0$ is equivalent to the Jacobi identity.

An Extended Example: 2- and 3-dimensional Lie Algebras. It is clear that up to isomorphism, there is only one (real) Lie algebra of dimension 1, namely ${ \mathfrak { g } } = \mathbb { R }$ with the zero bracket. This is the Lie algebra of the connected Lie groups R and $S ^ { 1 }$ . (You are asked to prove in an exercise that these are, in fact, the only connected one-dimensional Lie groups.)

The first interesting case, therefore, is dimension 2. If g is a 2-dimensional Lie algebra with basis $x _ { 1 } , x _ { 2 }$ , then the entire Lie algebra structure is determined by the bracket $[ x _ { 1 } , x _ { 2 } ] = a ^ { 1 } x _ { 1 } + a ^ { 2 } x _ { 2 }$ . If $a ^ { 1 } = a ^ { 2 } = 0$ , then all brackets are zero, and the algebra is abelian. If one of $a ^ { 1 }$ or $a ^ { 2 }$ is non-zero, then, by switching $x _ { 1 }$ and $x _ { 2 }$ if necessary, one may assume that $a ^ { 1 } \neq 0$ . Then, considering the new basis $y _ { 1 } = a ^ { 1 } x _ { 1 } + a ^ { 2 } x _ { 2 }$ and $y _ { 2 } = ( 1 / a ^ { 1 } ) x _ { 2 }$ , one obtains $[ y _ { 1 } , y _ { 2 } ] = y _ { 1 }$ . Since the Jacobi identity is easily verified for this Lie bracket, this does define a Lie algebra. Thus, up to isomorphism, there are only two distinct 2-dimensional Lie algebras.

The abelian example is, of course, the Lie algebra of the vector space $\mathbb { R } ^ { 2 }$ (as well as the Lie algebra of $S ^ { 1 } \times \mathbb { R }$ , and the Lie algebra of $S ^ { 1 } \times S ^ { 1 } )$

An example of a Lie group of dimension 2 with a non-abelian Lie algebra is the matrix Lie group

$$
G = \{ { ( \begin{array} { l l } { a } & { b } \\ { 0 } & { 1 } \end{array} ) } \ { | \ a \in \mathbb { R } ^ { + } , \ b \in \mathbb { R } } \} .
$$

In fact, it is not hard to show that, up to isomorphism, this is the only connected nonabelian Lie group of dimension 2 (see the Exercises).

Now, let us pass on to the classification of the three dimensional Lie algebras. Here, the story becomes much more interesting. Let g be a 3-dimensional Lie algebra, and let $x _ { 1 } , x _ { 2 } , x _ { 3 }$ be a basis of g. Then, one may write the bracket relations in matrix form as

$$
{ \left( \begin{array} { l } { \left[ x _ { 2 } , x _ { 3 } \right] } \end{array} \left[ x _ { 3 } , x _ { 1 } \right] \begin{array} { l } { \left[ x _ { 1 } , x _ { 2 } \right] } \end{array} \right) } = { \left( \begin{array} { l l l } { x _ { 1 } } & { x _ { 2 } } & { x _ { 3 } } \end{array} \right) } C
$$

where $C$ is the 3-by-3 matrix of structure constants. How is this matrix affected by a change of basis? Well, let

$$
( \ y _ { 1 } y _ { 2 } y _ { 3 } ) = \left( \begin{array} { l l l } { x _ { 1 } x _ { 2 } x _ { 3 } } \end{array} \right) A
$$

where $A \in \operatorname { G L } ( 3 , \mathbb { R } )$ . Then it is easy to compute that

$$
{ \left( \begin{array} { l } { \left[ y _ { 2 } , y _ { 3 } \right] } \end{array} [ y _ { 3 } , y _ { 1 } ] \begin{array} { l } { \left[ y _ { 1 } , y _ { 2 } \right] } \end{array} \right) } = { \left( \begin{array} { l } { \left[ x _ { 2 } , x _ { 3 } \right] } \end{array} [ x _ { 3 } , x _ { 1 } ] \begin{array} { l } { \left[ x _ { 1 } , x _ { 2 } \right] } \end{array} \right) } { \mathrm { A d j } } ( A )
$$

where $\operatorname { A d j } ( A )$ is the classical adjoint matrix of A, i.e., the matrix of 2-by-2 minors. Thus,

$$
A ^ { - 1 } = ( \operatorname* { d e t } ( A ) ) ^ { - 1 } \operatorname { } ^ { t } \mathrm { A d j } ( A ) .
$$

(Do not confuse this with the adjoint mapping defined earlier!) It then follows that

$$
\begin{array}{c} { ( \begin{array} { l l } { [ y _ { 2 } , y _ { 3 } ] } & { [ y _ { 3 } , y _ { 1 } ] } \end{array} ) } { [ y _ { 1 } , y _ { 2 } ] }  \end{array} )  = { ( \begin{array} { l l l } { y _ { 1 } } & { y _ { 2 } } & { y _ { 3 } } \end{array} ) } { \cal C } ^ { \prime } ,
$$

where

$$
C ^ { \prime } = A ^ { - 1 } C \operatorname { A d j } ( A ) = \operatorname* { d e t } ( A ) A ^ { - 1 } C ^ { t } A ^ { - 1 } .
$$

It follows without too much difficulty that, if one writes $C = S + \hat { a }$ , where S is a symmetric 3-by-3 matrix and

$$
{ \hat { a } } = \left( { \begin{array} { c c c } { 0 } & { - a ^ { 3 } } & { a ^ { 2 } } \\ { a ^ { 3 } } & { 0 } & { - a ^ { 1 } } \\ { - a ^ { 2 } } & { a ^ { 1 } } & { 0 } \end{array} } \right) \qquad { \mathrm { w h e r e } } \qquad a = \left( { \begin{array} { c } { a ^ { 1 } } \\ { a ^ { 2 } } \\ { a ^ { 3 } } \end{array} } \right) ,
$$

then $C ^ { \prime } = S ^ { \prime } + \widehat { a ^ { \prime } }$ , where

$$
S ^ { \prime } = \operatorname * { d e t } ( A ) A ^ { - 1 } S ^ { t } A ^ { - 1 } \qquad \mathrm { a n d } \qquad a ^ { \prime } = { } ^ { t } A a .
$$

Now, I claim that the condition that the Jacobi identity hold for the bracket defined by the matrix C is equivalent to the condition $S a = 0$ . To see this, note first that

$$
\begin{array} { r l } & { [ [ x _ { 2 } , x _ { 3 } ] , x _ { 1 } ] + [ [ x _ { 3 } , x _ { 1 } ] , x _ { 2 } ] + [ [ x _ { 1 } , x _ { 2 } ] , x _ { 3 } ] } \\ & { \phantom { [ [ [object Object] ] { ] } } = [ C _ { 1 } ^ { 1 } x _ { 1 } + C _ { 1 } ^ { 2 } x _ { 2 } + C _ { 1 } ^ { 3 } x _ { 3 } , x _ { 1 } ] + [ C _ { 2 } ^ { 1 } x _ { 1 } + C _ { 2 } ^ { 2 } x _ { 2 } + C _ { 2 } ^ { 3 } x _ { 3 } , x _ { 2 } ] + [ C _ { 3 } ^ { 1 } x _ { 1 } + C _ { 3 } ^ { 2 } x _ { 2 } + C _ { 3 } ^ { 3 } x _ { 3 } , x _ { 3 } ] } \\ & { \phantom { [ [ [object Object] ] { ] } } = ( C _ { 3 } ^ { 2 } - C _ { 2 } ^ { 3 } ) [ x _ { 2 } , x _ { 3 } ] + ( C _ { 1 } ^ { 3 } - C _ { 3 } ^ { 1 } ) [ x _ { 3 } , x _ { 1 } ] + ( C _ { 2 } ^ { 1 } - C _ { 1 } ^ { 2 } ) [ x _ { 1 } , x _ { 2 } ] } \\ & { \phantom { [ [ [object Object] ] { ] } } = 2 a ^ { 1 } [ x _ { 2 } , x _ { 3 } ] + 2 a ^ { 2 } [ x _ { 3 } , x _ { 1 } ] + 2 a ^ { 3 } [ x _ { 1 } , x _ { 2 } ] } \\ & { \phantom { [ [ [object Object] ] { ] } } = 2 ( \begin{array} { l } { [ x _ { 2 } , x _ { 3 } ] } & { [ x _ { 3 } , x _ { 1 } ] } \end{array} ) \ [ x _ { 1 } , x _ { 2 } ] \ ) \ a } \\ & { \phantom { [ [ [object Object] ] { ] } } = 2 ( \begin{array} { l } { x _ { 1 } } \end{array}  } \end{array}
$$

and $C a = ( S + \hat { a } ) a = S a$ since $\hat { a } a = 0$ . Thus, the Jacobi identity applied to the basis $x _ { 1 } , x _ { 2 } , x _ { 3 }$ implies that $S a = 0$ . However, if $y _ { 1 } , y _ { 2 } , y _ { 3 }$ is any other triple of elements of g, then for some 3-by-3 matrix B, one has

$$
\left( \begin{array} { l l l } { y _ { 1 } } & { y _ { 2 } } & { y _ { 3 } } \end{array} \right) = \left( \begin{array} { l l l } { x _ { 1 } } & { x _ { 2 } } & { x _ { 3 } } \end{array} \right) B ,
$$

and I leave it to the reader to check that

$$
[ [ y _ { 2 } , y _ { 3 } ] , y _ { 1 } ] + [ [ y _ { 3 } , y _ { 1 } ] , y _ { 2 } ] + [ [ y _ { 1 } , y _ { 2 } ] , y _ { 3 } ] = \operatorname* { d e t } ( B ) \left( [ [ x _ { 2 } , x _ { 3 } ] , x _ { 1 } ] + [ [ x _ { 3 } , x _ { 1 } ] , x _ { 2 } ] + [ [ x _ { 1 } , x _ { 2 } ] , x _ { 3 } ] \right)
$$

in this case. Thus, $S a = 0$ implies the full Jacobi identity.

There are now two essentially different cases to treat.

In the first case, if $a = 0$ , then the Jacobi identity is automatically satisfied, and S can be any symmetric matrix. However, two such choices S and $S ^ { \prime }$ will clearly give rise to isomorphic Lie algebras if and only if there is an $A \in \operatorname { G L } ( 3 , \mathbb { R } )$ for which $S ^ { \prime } =$ $\operatorname* { d e t } ( A ) A ^ { - 1 } S ^ { t } A ^ { - 1 }$ . I leave as an exercise for the reader to show that every choice of $S$ yields an algebra (with $a = 0 )$ that is equivalent to exactly one of the algebras made by one of the following six choices for S:

$$
\begin{array} { r l } { \left( { \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) } & { { } \left( { \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) \quad \left( { \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} } \right) } \end{array}
$$

$$
\begin{array} { r l } { \left( { \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) } & { { } \left( { \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) \quad \left( { \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} } \right) } \end{array}
$$

In the second case, if $a \neq 0$ , then by a suitable change of basis A, one can assume that $a ^ { 1 } = a ^ { 2 } = 0$ and that $a ^ { 3 } = 1$ . Any change of basis A that preserves this normalization is seen to be of the form

$$
A = \left( \begin{array} { c c c } { { A _ { 1 } ^ { 1 } } } & { { A _ { 2 } ^ { 1 } } } & { { A _ { 3 } ^ { 1 } } } \\ { { A _ { 1 } ^ { 2 } } } & { { A _ { 2 } ^ { 2 } } } & { { A _ { 3 } ^ { 2 } } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) .
$$

Since $S a = 0$ and since S is symmetric, it follows that S must be of the form

$$
S = \left( \begin{array} { c c c } { { s _ { 1 1 } } } & { { s _ { 1 2 } } } & { { 0 } } \\ { { s _ { 1 2 } } } & { { s _ { 2 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) .
$$

Moreover, a simple calculation shows that the result of applying a change of basis of the above form is to change the matrix S into the matrix

$$
S ^ { \prime } = \left( \begin{array} { c c c } { { s _ { 1 1 } ^ { \prime } } } & { { s _ { 1 2 } ^ { \prime } } } & { { 0 } } \\ { { s _ { 1 2 } ^ { \prime } } } & { { s _ { 2 2 } ^ { \prime } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right)
$$

where

$$
\left( \begin{array} { l l } { s _ { 1 1 } ^ { \prime } } & { s _ { 1 2 } ^ { \prime } } \\ { s _ { 1 2 } ^ { \prime } } & { s _ { 2 2 } ^ { \prime } } \end{array} \right) = \frac { 1 } { A _ { 1 } ^ { 1 } A _ { 2 } ^ { 2 } - A _ { 2 } ^ { 1 } A _ { 1 } ^ { 2 } } \left( \begin{array} { l l } { A _ { 2 } ^ { 2 } } & { - A _ { 2 } ^ { 1 } } \\ { - A _ { 1 } ^ { 2 } } & { A _ { 1 } ^ { 1 } } \end{array} \right) \left( \begin{array} { l l } { s _ { 1 1 } } & { s _ { 1 2 } } \\ { s _ { 1 2 } } & { s _ { 2 2 } } \end{array} \right) \left( \begin{array} { l l } { A _ { 2 } ^ { 2 } } & { - A _ { 1 } ^ { 2 } } \\ { - A _ { 2 } ^ { 1 } } & { A _ { 1 } ^ { 1 } } \end{array} \right) .
$$

It follows that $s _ { 1 1 } ^ { \prime } s _ { 2 2 } ^ { \prime } - ( s _ { 1 2 } ^ { \prime } ) ^ { 2 } = s _ { 1 1 } s _ { 2 2 } - ( s _ { 1 2 } ) ^ { 2 }$ , so there is an ‘invariant’ to be considered. I leave it to the reader to show that the upper left-hand 2-by-2 block of S can be brought by a change of basis of the above form into exactly one of the four forms

$$
\left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) \quad \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) \quad \left( \begin{array} { c c } { { \sigma } } & { { 0 } } \\ { { 0 } } & { { \sigma } } \end{array} \right) \quad \left( \begin{array} { c c } { { \sigma } } & { { 0 } } \\ { { 0 } } & { { - \sigma } } \end{array} \right)
$$

where $\sigma > 0$ is a real positive number.

To summarize, every 3-dimensional Lie algebra is isomorphic to exactly one of the following Lie algebras: Either

$$
\begin{array} { r l r } { { \scriptstyle \left[ x _ { 2 } , x _ { 3 } \right] = x _ { 1 } } } & { } & { { \scriptstyle \left[ x _ { 2 } , x _ { 3 } \right] = x _ { 2 } } } \\ { { \scriptstyle \mathfrak { s o } ( 3 ) : \ \left[ x _ { 3 } , x _ { 1 } \right] = x _ { 2 } } } & { } & { { \mathrm { o r } \quad \quad \mathfrak { s } \mathfrak { t } ( 2 , \mathbb { R } ) : \ \left[ x _ { 3 } , x _ { 1 } \right] = x _ { 1 } } } \\ { { \scriptstyle \left[ x _ { 1 } , x _ { 2 } \right] = x _ { 3 } } } & { } & { { \scriptstyle \left[ x _ { 1 } , x _ { 2 } \right] = x _ { 3 } } } \end{array}
$$

or an algebra of the form

$$
\begin{array} { l } { { [ x _ { 2 } , x _ { 3 } ] = b _ { 1 1 } x _ { 1 } + b _ { 1 2 } x _ { 2 } } } \\ { { { } [ x _ { 3 } , x _ { 1 } ] = b _ { 2 1 } x _ { 1 } + b _ { 2 2 } x _ { 2 } } } \\ { { { } [ x _ { 1 } , x _ { 2 } ] = 0 } } \end{array}
$$

where the 2-by-2 matrix B is one of the following

$$
\left( \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right)
$$

$$
\left( \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right)
$$

$$
\left( \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right)
$$

$$
\left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right)
$$

$$
\left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - 1 } } & { { 0 } } \end{array} \right) \quad \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { - 1 } } & { { 0 } } \end{array} \right) \quad \left( \begin{array} { c c } { { \sigma } } & { { 1 } } \\ { { - 1 } } & { { \sigma } } \end{array} \right) \quad \left( \begin{array} { c c } { { \sigma } } & { { 1 } } \\ { { - 1 } } & { { - \sigma } } \end{array} \right) \quad \left( \begin{array} { c c } { { \sigma } } & { { 0 } } \\ { { - 1 } } & { { - \sigma } } \end{array} \right) \quad \left( \begin{array} { c c } { { \sigma } } & { { 0 } } \\ { { - 1 } } & { { \sigma } } \end{array} \right) \quad \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right) \quad \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) .
$$

and, in the latter two cases, $\sigma$ is a positive real number. Each of these eight latter types can be represented as a subalgebra of gl(3, R) in the form

$$
{ \mathfrak { g } } = \left\{ \left. { \left( \begin{array} { c c c } { ( 1 + b _ { 2 1 } ) z } & { - b _ { 1 1 } z } & { x } \\ { b _ { 2 2 } z } & { ( 1 - b _ { 1 2 } ) z } & { y } \\ { 0 } & { 0 } & { z } \end{array} \right) } ~ \right| ~ x , y , z \in \mathbb { R } \right\}
$$

I leave as an exercise for the reader to show that the corresponding subgroup of ${ \mathrm { G L } } ( 3 , \mathbb { R } )$ is a closed, embedded, simply connected matrix Lie group whose underlying manifold is diffeomorphic to $\mathbb { R } ^ { 3 }$

# Exercise Set 2: Lie Groups

1. Show that for any real vector space of dimension n, the Lie group $\operatorname { G L } ( V )$ is isomorphic to $\operatorname { G L } ( n , \mathbb { R } )$ . (Hint: Choose a basis b of $V ,$ use b to construct a mapping $\phi _ { \mathbf { b } } \colon \mathrm { G L } ( V ) \to$ $\operatorname { G L } ( n , \mathbb { R } )$ , and then show that $\phi _ { \mathbf { b } }$ is a smooth isomorphism.)

2. Let G be a Lie group and let H be an abstract subgroup. Show that if there is an open neighborhood $U$ of e in $G$ so that $H \cap U$ is a smooth embedded submanifold of $G ,$ then H is a Lie subgroup of $G$ .

3. Show that $\operatorname { S L } ( n , \mathbb { R } )$ is an embedded Lie subgroup of ${ \mathrm { G L } } ( n , \mathbb { R } )$ . (Hint: $\mathrm { S L } ( n , \mathbb { R } ) =$ $\mathrm { d e t } ^ { - 1 } ( 1 ) . )$ )

4. Show that ${ \mathrm { O } } ( n )$ is an compact Lie subgroup of $\operatorname { G L } ( n , \mathbb { R } )$ (Hint: $\mathrm { O } ( n ) = F ^ { - 1 } ( I _ { n } )$ , where F is the map from ${ \mathrm { G L } } ( n , \mathbb { R } )$ to the vector space of $n { \mathrm { - } } \mathrm { b y } { \mathrm { - } } n$ symmetric matrices given by $F ( A ) = { } ^ { t } A A$ Taking note of Exercise 2, show that the Implicit Function Theorem applies. To show compactness, apply the Heine-Borel theorem.) Show also that $\operatorname { S O } ( n )$ is an open-and-closed, index 2 subgroup of ${ \mathrm { O } } ( n )$ .

5. Carry out the analysis in Exercise 3 for the complex matrix Lie group $\mathrm { S L } ( n , \mathbb { C } )$ and the analysis in Exercise 4 for the complex matrix Lie groups $\mathrm { U } ( n )$ and $\operatorname { S U } ( n )$ . What are the (real) dimensions of all of these groups?

6. Show that the map $\mu { : } \operatorname { O } ( n ) \times A _ { n } \times N _ { n } \to \operatorname { G L } ( n , \mathbb { R } )$ defined by matrix multiplication is a diffeomorphism although it is not a group homomorphism. (Hint: The map is clearly smooth, you must only compute an inverse. To get the first factor $\nu _ { 1 } \colon \operatorname { G L } ( n , \mathbb { R } ) \to \operatorname { O } ( n )$ of the inverse map, think of an element b $\in \operatorname { G L } ( n , \mathbb { R } )$ as a row of column vectors in $\mathbb { R } ^ { n }$ and let $\nu _ { 1 } ( { \mathbf { b } } )$ be the row of column vectors that results from b by apply the Gram-Schmidt orthogonalization process. Why does this work and why is the resulting map $\nu _ { 1 }$ smooth?) Show, similarly that the map

$$
\mu \colon \operatorname { S O } ( n ) \times \left( A _ { n } \cap \operatorname { S L } ( n , \mathbb { R } ) \right) \times N _ { n } \to \operatorname { S L } ( n , \mathbb { R } )
$$

is a diffeomorphism. Are there similar factorizations for the groups $\mathrm { G L } ( n , \mathbb { C } )$ and $\mathrm { S L } ( n , \mathbb { C } ) \overset { \gamma } { . }$ (Hint: Consider unitary bases rather than orthogonal ones.)

7. Show that

$$
\mathrm { S U ( 2 ) } = \left\{ \left( { \begin{array} { c c } { a } & { - { \overline { { b } } } } \\ { b } & { { \overline { { a } } } } \end{array} } \right) \bigg | a { \overline { { a } } } + b { \overline { { b } } } = 1 \right\} .
$$

Conclude that ${ \mathrm { S U } } ( 2 )$ is diffeomorphic to the 3-sphere and, using the previous exercise, that, in particular, $\mathrm { S L } ( 2 , \mathbb { C } )$ is simply connected, while $\pi _ { 1 } ( { \mathrm { S L } } ( 2 , \mathbb { R } ) ) \simeq \mathbb { Z }$

8. Show that, for any Lie group $G ,$ , the mappings $L _ { a }$ satisfy

$$
L _ { a } ^ { \prime } ( b ) = L _ { a b } ^ { \prime } ( e ) \circ \left( L _ { b } ^ { \prime } ( e ) \right) ^ { - 1 } .
$$

where ${ \cal L } _ { a } ^ { \prime } ( b ) { : } T _ { b } G \to T _ { a b } G$ . (This shows that the effect of left translation is completely determined by what it does at $e . )$ State and prove a similar formula for the mappings $R _ { a }$

9. Let $( G , \mu )$ be a Lie group. Using the canonical identification $T _ { ( a , b ) } ( G \times G ) = T _ { a } G \oplus T _ { b } G .$ prove the formula

$$
\mu ^ { \prime } ( a , b ) ( v , w ) = R _ { b } ^ { \prime } ( a ) ( v ) + L _ { a } ^ { \prime } ( b ) ( w )
$$

for all $v \in T _ { a } G$ and $w \in T _ { b } G$

10. Complete the proof of Proposition 3 by explicitly exhibiting the map c as a composition of known smooth maps. (Hint: if $f \colon X \to Y$ is smooth, then $f ^ { \prime } { : } T X \to T Y$ is also smooth.)

11. Show that, for any $v \in { \mathfrak { g } }$ , the left-invariant vector field $X _ { v }$ is indeed smooth. Also prove the first statement in Proposition 4. (Hint: Use Ψ to write the mapping $X _ { v } \colon G \to T G$ as a composition of smooth maps. Show that the assignment $v \mapsto X _ { v }$ is linear. Finally, show that if a left-invariant vector field on G vanishes anywhere, then it vanishes identically.)

12. Show that exp: ${ \mathfrak { g } } \to G$ is indeed smooth and that $\exp ^ { \prime } { \colon } { \mathfrak { g } }  { \mathfrak { g } }$ is the identity mapping. (Hint: Write down a smooth vector field Y on ${ \mathfrak { g } } \times G$ such that the integral curves of Y are of the form $\gamma ( t ) = ( v _ { 0 } , a _ { 0 } e ^ { t v _ { 0 } } )$ . Now use the flow of Y ,

$$
\Psi \colon \mathbb { R } \times { \mathfrak { g } } \times G \to { \mathfrak { g } } \times G ,
$$

to write exp as the composition of smooth maps.)

13. Show that, for the homomorphism det: ${ \mathrm { G L } } ( n , \mathbb { R } ) \to \mathbb { R } ^ { \bullet }$ , we have $\operatorname* { d e t } ^ { \prime } ( I _ { n } ) ( x ) = \operatorname { t r } ( x )$ where tr denotes the trace function. Conclude, using Theorem 1 that, for any matrix a,

$$
\operatorname* { d e t } ( e ^ { a } ) = e ^ { \operatorname { t r } ( a ) } .
$$

14. Prove that, for any $g \in G$ and any $x \in { \mathfrak { g } }$ , we have the identity

$$
g \exp ( x ) g ^ { - 1 } = \exp \bigl ( \mathrm { A d } ( g ) ( x ) \bigr ) .
$$

(Hint: Replace x by tx in the above formula and consider Proposition 5.) Use this to show that $\operatorname { t r } ( \exp ( x ) ) \geq - 2$ for all $x \in { \mathfrak { s l } } ( 2 , \mathbb { R } )$ . Conclude that $\exp \colon { \mathfrak { s l } } ( 2 , \mathbb { R } ) \to \mathrm { S L } ( 2 , \mathbb { R } )$ is not surjective. (Hint: show that every $x \in { \mathfrak { s l } } ( 2 , \mathbb { R } )$ is of the form $g y g ^ { - 1 }$ for some $g \in \mathrm { S L } ( 2 , \mathbb { R } )$ and some y that is one of the matrices

$$
\left( { \begin{array} { c c } { 0 } & { \pm 1 } \\ { 0 } & { 0 } \end{array} } \right) , \qquad \left( { \begin{array} { c c } { \lambda } & { 0 } \\ { 0 } & { - \lambda } \end{array} } \right) , { \mathrm { o r } } \qquad \left( { \begin{array} { c c } { 0 } & { - \lambda } \\ { \lambda } & { 0 } \end{array} } \right) , \qquad ( \lambda > 0 ) .
$$

Also, remember that tr $( a b a ^ { - 1 } ) = \operatorname { t r } ( b ) . )$

15. Using Theorem 1, show that if $H _ { 1 }$ and $H _ { 2 }$ are Lie subgroups of $G ,$ , then $H _ { 1 } \cap H _ { 2 }$ is also a Lie subgroup of $G .$ . (Hint: What should the Lie algebra of this intersection be? Be careful: $H _ { 1 } \cap H _ { 2 }$ might have countably many distinct components even if $H _ { 1 }$ and $H _ { 2 }$ are connected!)

16. For any skew-commutative algebra $( { \mathfrak { g } } , [ , ] )$ , we define the map ad: ${ \mathfrak { g } } \to { \mathrm { E n d } } ( { \mathfrak { g } } )$ by ad $( x ) ( y ) = [ x , y ]$ . Verify that the validity of the Jacobi identity $[ \operatorname { a d } ( x ) , \operatorname { a d } ( y ) ] = \operatorname { a d } ( [ x , y ] )$ (where, as usual, the bracket on End(g) is the commutator) is equivalent to the validity of the identity

$$
[ [ x , y ] , z ] + [ [ y , z ] , x ] + [ [ z , x ] , y ] = 0
$$

for all $x , y , z \in { \mathfrak { g } }$

17. Show that, as $\lambda \in \mathbb { R }$ varies, all of the groups

$$
G _ { \lambda } = \left\{ { \left( \begin{array} { l l } { a } & { b } \\ { 0 } & { a ^ { \lambda } } \end{array} \right) } \normalsize \ \middle | \ a \in \mathbb { R } ^ { + } , \ b \in \mathbb { R } \right\}
$$

with $\lambda \neq 1$ are isomorphic, but are not conjugate in ${ \mathrm { G L } } ( 2 , \mathbb { R } )$ . What happens when $\lambda = 1 2$

18. Show that a connected Lie group G is abelian if and only if its Lie algebra satisfies $[ x , y ] = 0$ for all $x , y \in { \mathfrak { g } }$ . Conclude that a connected abelian Lie group of dimension n is isomorphic to $\mathbb { R } ^ { n } / \mathbb { Z } ^ { d }$ where $\mathbb { Z } ^ { d }$ is some discrete subgroup of rank $d \leq n$ . (Hint: To show $\cdot _ { G }$ abelian’ implies ‘g abelian’, look at how [, ] was defined. To prove the converse, use Theorem 3 to construct a surjective homomorphism $\phi \colon \mathbb { R } ^ { n } \to G$ with discrete kernel.)

19. (Covering Spaces of Lie groups) Let G be a connected Lie group and let $\pi { \colon } \tilde { G } \to G$ be the universal covering space of G. (Recall that the points of $\tilde { G }$ can be regarded as the space of fixed-endpoint homotopy classes of continuous maps $\gamma \colon [ 0 , 1 ] \to G$ with $\gamma ( 0 ) = e . )$ Show that there is a unique Lie group structure ${ \tilde { \mu } } \colon { \tilde { G } } \times { \tilde { G } } \to { \tilde { G } }$ for which the homotopy class of the constant map $\tilde { e } \in \tilde { G }$ is the identity and so that $\pi$ is a homomorphism. (Hints: Give $\tilde { G }$ the (unique) smooth structure for which $\pi$ is a local diffeomorphism. The multiplication $\tilde { \mu }$ can then be defined as follows: The map $\bar { \mu } = \mu \circ ( \pi \times \pi )             { : } \tilde { G } \times \tilde { G }  G$ is a smooth map and satisfies $\bar { \mu } ( \tilde { e } , \tilde { e } ) = e$ . Since $\tilde { G } \times \tilde { G }$ is simply connected, the universal lifting property of the covering map π implies that there is a unique map ${ \tilde { \mu } } \colon { \tilde { G } } \times { \tilde { G } } \to { \tilde { G } }$ that satisfies $\pi \circ \tilde { \mu } = \bar { \mu }$ and $\tilde { \mu } ( \tilde { e } , \tilde { e } ) = \tilde { e }$ . Show that $\tilde { \mu }$ is smooth, that it satisfies the axioms for a group multiplication (associativity, existence of an identity, and existence of inverses), and that π is a homomorphism. You will want to use the universal lifting property of covering spaces a few times.)

The kernel of $\pi$ is a discrete normal subgroup of $\tilde { G }$ . Show that this kernel lies in the center of $\tilde { G }$ . In fact, show that, for any connected Lie group G, any discrete normal subgroup $H \subset G$ lies in the center of $G .$ . (Hint: For any $z \in H$ , the connected set $\{ a z a ^ { - 1 } \mid a \in G \}$ must also lie in H.)

Show that the center of the simply connected Lie group

$$
G = \left\{ { \left( \begin{array} { l l } { a } & { b } \\ { 0 } & { 1 } \end{array} \right) } \normalsize \ \middle | \ a \in \mathbb { R } ^ { + } , \ b \in \mathbb { R } \right\}
$$

is trivial, so any connected Lie group with the same Lie algebra is actually isomorphic to G.

(In the next Lecture, we will show that whenever K is a closed normal subgroup of a Lie group $G ,$ the quotient group $G / K$ can be given the structure of a Lie group. Thus, in many cases, one can effectively list all of the connected Lie groups with a given Lie algebra.)

20. Show that ${ \widehat { \mathrm { S L } } } { \widetilde { ( 2 , \mathbb { R } ) } }$ is not a matrix group! In fact, show that any homomorphism $\phi \colon { \mathrm { S L } } ( 2 , \mathbb { R } ) \to { \mathrm { G L } } ( n , \mathbb { R } )$ factors through the projections $\operatorname { S L } ( 2 , \mathbb { R } ) \to \operatorname { S L } ( 2 , \mathbb { R } )$ . (Hint: Recall, from earlier exercises, that the inclusion map SL $_ { \ i } ( 2 , \mathbb { R } ) \to \mathrm { S L } ( 2 , \mathbb { C } )$ induces the zero map on $\pi _ { 1 }$ since $\mathrm { S L } ( 2 , \mathbb { C } )$ is simply connected. Now, any homomorphism $\phi \colon \mathrm { S L } ( 2 , \mathbb { R } ) \ \to$ $\operatorname { G L } ( n , \mathbb { R } )$ induces a Lie algebra homomorphism $\phi ^ { \prime } ( e ) \colon \mathfrak { s l } ( 2 , \mathbb { R } ) \ \to \ \mathfrak { g l } ( n , \mathbb { R } )$ and this may clearly be complexified to yield a Lie algebra homomorphism $\phi ^ { \prime } ( e ) ^ { \mathbb { C } } { : \mathfrak { s l } } ( 2 , \mathbb { C } ) \to \mathfrak { g l } ( n , \mathbb { C } )$ Since $\mathrm { S L } ( 2 , \mathbb { C } )$ is simply connected, there must be a corresponding Lie group homorphism $\phi ^ { \mathbb { C } } \colon { \mathrm { S L } } ( 2 , \mathbb { C } ) \ \to \ { \mathrm { G L } } ( n , \mathbb { C } )$ . Now suppose that $\phi$ does not factor through SL(2, R), i.e., that $\phi$ is non-trivial on the kernel of $\mathrm { S L } ( 2 , \mathbb { R } ) \to \mathrm { S L } ( 2 , \mathbb { R } )$ , and show that this leads to a contradiction.)

21. An ideal in a Lie algebra g is a linear subspace h that satisfies $[ { \mathfrak { h } } , { \mathfrak { g } } ] \subset { \mathfrak { h } }$ Show that the kernel k of a Lie algebra homomorphism $\varphi \colon { \mathfrak { h } }  { \mathfrak { g } }$ is an ideal in h and that the image $\varphi ( { \mathfrak { h } } )$ is a subalgebra of g. Conversely, show that if ${ \mathfrak { k } } \subset { \mathfrak { h } }$ is an ideal, then the quotient vector space ${ \mathfrak { h } } / { \mathfrak { k } }$ carries a unique Lie algebra structure for which the quotient mapping ${ \mathfrak { h } } \to { \mathfrak { h } } / { \mathfrak { k } }$ is a homomorphism.

Show that the subspace [g, g] of g that is generated by all brackets of the form $[ x , y ]$ is an ideal in g. What can you say about the quotient ${ \mathfrak { g } } / [ { \mathfrak { g } } , { \mathfrak { g } } ] ?$

22. Show that, for a connected Lie group $G ,$ a connected Lie subgroup H is normal if and only if h is an ideal of g. (Hint: Use Proposition 7 and the fact that $H \subset G$ is normal if and only if $e ^ { x } H e ^ { - x } = H$ for all $x \in { \mathfrak { g } } .$ )

23. For any Lie algebra g, let ${ \mathfrak { z } } ( { \mathfrak { g } } ) \subset { \mathfrak { g } }$ denote the kernel of the homomorphism ad: ${ \mathfrak { g } } \to$ ${ \mathfrak { g l } } ( { \mathfrak { g } } )$ . Use Theorem 2 and Exercise 16 to prove Theorem 4 for any Lie algebra g for which ${ \mathfrak { z } } ( { \mathfrak { g } } ) = 0$ . (Hint: Look at the discussion after the statement of Theorem 4.)

Show also that if g is the Lie algebra of the connected Lie group $G ,$ then the connected Lie subgroup $Z ( { \mathfrak { g } } ) \subset G$ that corresponds to ${ \mathfrak { z } } ( { \mathfrak { g } } )$ lies in the center of G. (In the next lecture, we will be able to prove that the center of G is a closed Lie subgroup of $G$ and that $Z ( { \mathfrak { g } } )$ is actually the identity component of the center of G.)

24. For any Lie algebra g, there is a canonical bilinear pairing $\kappa \colon { \mathfrak { g } } \times { \mathfrak { g } }  \mathbb { R }$ , called the Killing form, defined by the rule:

$$
\kappa ( x , y ) = \operatorname { t r } \bigl ( \operatorname { a d } ( x ) \operatorname { a d } ( y ) \bigr ) .
$$

(i) Show that κ is symmetric and, if g is the Lie algebra of a Lie group $G ,$ , then κ is Ad-invariant:

$$
\kappa ( \mathrm { A d } ( g ) x , \mathrm { A d } ( g ) y ) = \kappa ( x , y ) = \kappa ( y , x ) .
$$

Show also that

$$
\kappa ( [ z , x ] , y ) = - \kappa ( x , [ z , y ] ) .
$$

A Lie algebra g is said to be semi-simple if κ is a non-degenerate bilinear form on g.

(ii) Show that, of all the 2- and 3-dimensional Lie algebras, only so(3) and ${ \mathfrak { s l } } ( 2 , \mathbb { R } )$ are semi-simple.

(iii) Show that if ${ \mathfrak { h } } \subset { \mathfrak { g } }$ is an ideal in a semi-simple Lie algebra g, then the Killing form of h as an algebra is equal to the restriction of the Killing form of g to h. Show also that the subspace $\mathfrak { h } ^ { \perp } = \{ x \in \mathfrak { g } | \kappa ( x , y ) = 0$ for all $y \in { \mathfrak { h } } \}$ is also an ideal in g and that $\mathfrak { g } = \mathfrak { h } \oplus \mathfrak { h } ^ { \perp }$ as Lie algebras. (Hint: For the first part, examine the effect of ad(x) on a basis of g chosen so that the first dim h basis elements are a basis of h.)

(iv) Finally, show that a semi-simple Lie algebra can be written as a direct sum of ideals ${ \mathfrak { h } } _ { i } ,$ each of which has no proper ideals. (Hint: Apply (iii) as many times as you can find proper ideals of the summands found so far.) A Lie algebra h of dimension greater than 1 that has no proper ideals is said to be simple.

A more general class of Lie algebras are the reductive ones. We say that a Lie algebra is reductive if there is a non-degenerate symmetric bilinear form $( \mathbf { \partial } , \mathbf { \partial } ) \colon \mathfrak { g } \times \mathfrak { g } \to \mathbb { R }$ that satisfies the identity $\left( [ z , x ] , y \right) + \left( x , [ z , y ] \right) = 0$ . Using the above arguments, it is easy to see that a reductive algebra can be written as the direct sum of an abelian algebra and some number of simple algebras in a unique way.

25. Show that, if ω is the canonical left-invariant 1-form on $G$ and $Y _ { v }$ is the right-invariant vector field on $G$ satisfying $Y _ { v } ( e ) = v$ , then

$$
\omega { \big ( } Y _ { v } ( a ) { \big ) } = \operatorname { A d } { \big ( } a ^ { - 1 } { \big ) } ( v ) .
$$

(Remark: For any skew-commutative algebra $\left( \mathfrak { a } , [ , ] \right)$ , the function $[ [ , ] ] \colon { \mathfrak { a } } \times { \mathfrak { a } } \times { \mathfrak { a } } \to { \mathfrak { a } }$ defined by

$$
[ x , y , z ] = [ [ x , y ] , z ] + [ [ y , z ] , x ] + [ [ z , x ] , y ]
$$

is tri-linear and skew-symmetric, and hence represents an element of ${ \mathfrak { a } } \otimes \Lambda ^ { 3 } ( { \mathfrak { a } } ^ { * } ) . )$

## Lecture 3:

## Group Actions on Manifolds

In this lecture, I turn from the abstract study of Lie groups to their realizations as ‘transformation groups.’

Lie group actions.

Definition 1: If $( G , \mu )$ is a Lie group and M is a smooth manifold, then a $l e f t$ action of $G$ on M is a smooth mapping $\lambda \colon G \times M \to M$ that satisfies $\lambda ( e , m ) = m$ for all $m \in M$ and

$$
\lambda ( a , \lambda ( b , m ) ) = \lambda ( \mu ( a , b ) , m ) .
$$

Similarly, a right action of G on M is a smooth mapping $\rho \colon M \times G \to M$ , that satisfies $\rho ( m , e ) = m$ for all $m \in M$ and

$$
\rho \big ( \rho ( m , a ) , b \big ) = \rho \big ( m , \mu ( a , b ) \big ) .
$$

For notational sanity, whenever the action (left or right) can be easily inferred from context, we will usually write $a \cdot m$ instead of $\lambda ( a , m )$ or $m \cdot a$ instead of $\rho ( m , a )$ ). Thus, for example, the axioms for a left action in this abbreviated notation are simply $e \cdot m = m$ and $a \cdot ( b \cdot m ) = a b \cdot m$

For a given a left action $\lambda \colon G \times M \to M$ , it is easy to see that for each fixed $a \in G$ the map $\lambda _ { a } \colon M \to M$ defined by $\lambda _ { a } ( m ) = \lambda ( a , m )$ is a smooth diffeomorphism of M onto itself. Thus, G gets represented as a group of diffeomorphisms, or ‘transformations’ of a manifold M. This notion of ‘transformation group’ was what motivated Lie to develop his theory in the first place. See the Appendix to this Lecture for a more complete discussion of this point.

Equivalence of Left and Right Actions. Note that every right action $\rho \colon M \times G $ M can be rewritten as a left action and vice versa. One merely defines

$$
\tilde { \rho } ( a , m ) = \rho ( m , a ^ { - 1 } ) .
$$

(The reader should check that this $\tilde { \rho }$ is, in fact, a left action.) Thus, all theorems about left actions have analogues for right actions. The distinction between the two is mainly for notational and conceptual convenience. I will concentrate on left actions and only occasionally point out the places where right actions behave slightly differently (mainly changes of sign, etc.).

Stabilizers and Orbits. A left action is said to be effective if $g \cdot m = m$ for all $m \in M$ implies that $g = e$ . (Sometimes, the word faithful is used instead.) A left action is said to be free if $g \neq e$ implies that $g \cdot m \neq m$ for all $m \in M$

A left action is said to be transitive if, for any $x , y \in M$ , there exists a $g \in G$ so that $g \cdot x = y$ . In this case, M is usually said to be homogeneous under the given action.

For any $m \in M$ , the G-orbit of m is defined to be the set

$$
G \cdot m = \left\{ g \cdot m \left| g \in G \right. \right\}
$$

and the stabilizer (or isotropy group) of m is defined to be the subset

$$
G _ { m } = \{ g \in G | g \cdot m = m \} .
$$

Note that

$$
G _ { g \cdot m } = g G _ { m } g ^ { - 1 } .
$$

Thus, whenever $H \subset G$ is the stabilizer of a point of M, then all of the conjugate subgroups of H are also stabilizers. These results imply that

$$
G _ { M } = \bigcap _ { m \in M } G _ { m }
$$

is a closed normal subgroup of G and consists of those $g \in G$ for which $g \cdot m = m$ for all $m \in M$ . Often in practice, $G _ { M }$ is a discrete (in fact, usually finite) subgroup of G. When this is so, we say that the action is almost effective.

The following theorem says that orbits and stabilizers are particularly nice objects. Though the proof is relatively straightforward, it is a little long, so we will consider a few examples before attempting it.

Theorem 1: Let $\lambda \colon G \times M \to M$ be a left action of G on M. Then, for all $m \in M$ , the stabilizer $G _ { m }$ is a closed Lie subgroup of G. Moreover, the orbit G · m can be given the structure of a smooth submanifold of M in such a way that the map φ: $G  G \cdot m$ defined by $\phi ( g ) = \lambda ( g , m )$ is a smooth submersion.

Example 1. Any Lie group left-acts on itself by left multiplication. I.e., we set $M = G$ and define $\lambda \colon G \times M \to M$ to simply be $\mu .$ This action is both free and transitive.

Example 2. Given a homomorphism of Lie groups φ: $H  G .$ define a smooth left action λ: $H \times G \to G$ by the rule $\lambda ( h , g ) = \phi ( h ) g$ . Then $H _ { e } = \ker ( \phi )$ and $H \cdot e = \phi ( H ) \subset G$

In particular, Theorem 1 implies that the kernel of a Lie group homomorphism is a (closed, normal) Lie subgroup of the domain group and the image of a Lie group homomorphism is a Lie subgroup of the range group.

Example 3. Any Lie group acts on itself by conjugation: $g \cdot g _ { 0 } = g g _ { 0 } g ^ { - 1 }$ This action is neither free nor transitive (unless $\boldsymbol { G } = \{ e \} )$ . Note that $G _ { e } = G$ and, in general, $G _ { g }$ is the centralizer of $g \in G$ . This action is effective (respectively, almost effective) if and only if the center of G is trivial (respectively, discrete). The orbits are the conjugacy classes of G.

Example 4. ${ \mathrm { G L } } ( n , \mathbb { R } )$ acts on $\mathbb { R } ^ { n }$ as usual by $A \cdot v = A v$ . This action is effective but is neither free nor transitive since ${ \mathrm { G L } } ( n , \mathbb { R } )$ fixes $0 \in \mathbb { R } ^ { n }$ and acts transitively on $\mathbb { R } ^ { n } \backslash \{ 0 \}$ Thus, there are exactly two orbits of this action, one closed and the other not.Example 5. $\mathrm { S O } ( n { + } 1 )$ acts on $S ^ { n } = \{ x \in \mathbb { R } ^ { n + 1 } | x \cdot x = 1 \}$ by the usual action $A \cdot x = A x$ This action is transitive and effective, but not free (unless $n = 1 )$ since, for example, the stabilizer of $e _ { n + 1 }$ is clearly isomorphic to ${ \mathrm { S O } } ( n )$ •

Example 6. Let $\mathcal { S } _ { n }$ be the $n ( n { + } 1 ) / 2$ -dimensional vector space of $n { \mathrm { - } } \mathrm { b y } { \mathrm { - } } n$ real symmetric matrices. Then ${ \mathrm { G L } } ( n , \mathbb { R } )$ acts on $\mathcal { S } _ { n }$ by $A \cdot S = A S ^ { t } A$ The orbit of the identity matrix $I _ { n }$ is $\mathcal { S } _ { + } ( n )$ , the set of all positive-definite n-by-n real symmetric matrices (Why?). In fact, it is known that, if we define $I _ { p , q } \in \mathcal { S } _ { n }$ to be the matrix

$$
I _ { p , q } = \left( \begin{array} { c c c } { { I _ { p } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - I _ { q } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) ,
$$

(where the $^ { \cdot } 0 ^ { \cdot }$ entries have the appropriate dimensions) then $\mathcal { S } _ { n }$ is the (disjoint) union of the orbits of the matrices $I _ { p , q }$ where $0 \leq p , q$ and $p + q \le n$ (see the Exercises).

The orbit of $I _ { p , q }$ is open in $\mathcal { S } _ { n }$ iff $p + q = n$ . The stabilizer of $I _ { p , q }$ in this case is defined to be $\mathrm { O } ( p , q ) \subset \mathrm { G } \bar { \mathrm { L } } ( \bar { n } , \mathbb { R } )$

Note that the action is merely almost effective since $\{ \pm I _ { n } \} \subset \mathrm { G L } ( n , \mathbb { R } )$ fixes every $S \in \mathcal S _ { n }$

Example 7. Let $\mathcal { J } = \left\{ J \in \mathrm { G L } ( 2 n , \mathbb { R } ) | J ^ { 2 } = - I _ { 2 n } \right\}$ Then $\operatorname { G L } ( 2 n , \mathbb { R } )$ acts on $\mathcal { J }$ on the left by the formula $A \cdot J { \stackrel { \cdot } { = } } A J A ^ { - 1 }$ . I leave as exercises for the reader to prove that J is a smooth manifold and that this action of ${ \mathrm { G L } } ( 2 n , \mathbb { R } )$ is transitive and almost effective. The stabilizer of $J _ { 0 } =$ multiplication by i in $\mathbb { C } ^ { n } \left( = \mathbb { R } ^ { 2 \dot { n } } \right)$ is simply $\mathrm { G L } ( n , \mathbb { C } ) \subset \mathrm { G L } ( 2 n , \mathbb { R } )$

Example 8. Let $M = \mathbb { R } \mathbb { P } ^ { 1 }$ , denote the projective line, whose elements are the lines through the origin in $\mathbb { R } ^ { 2 }$ . We will use the notation $\left[ { x \atop y } \right]$ to denote the line in $\mathbb { R } ^ { 2 }$ spanned by the non-zero vector $\textstyle { \binom { x } { y } }$

Let $G = \mathrm { { S L } } ( 2 , \mathbb { R } )$ act on $\mathbb { R } ^ { \mathbb { P } ^ { 1 } }$ on the left by the formula

$$
{ \left( \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right) } \cdot { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } = { \left[ \begin{array} { l } { a x + b y } \\ { c x + d y } \end{array} \right] } .
$$

This action is easily seen to be almost effective, with only $\pm I _ { 2 } \in \mathrm { S L } ( 2 , \mathbb { R } )$ acting trivially.

Actually, it is more common to write this action more informally by using the identification $\mathbb { R P } ^ { 1 } = \mathbb { R } \cup \{ \infty \}$ that identifies $\left[ { x \atop y } \right]$ when $y \ne 0$ with $x / y \in \mathbb { R }$ and $\left[ ^ { 1 } _ { 0 } \right]$ with . With this convention, the action takes on the more familiar ‘linear fractional’ form

$$
{ \left( { \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} } \right) } \cdot x = { \frac { a x + b } { c x + d } } .
$$

Note that this form of the action makes it clear that the so-called ‘linear fractional’ action or ‘M¨obius’ action on the real line is just the projectivization of the usual linear representation of SL(2, R) on $\mathbb { R } ^ { 2 }$

We now turn to the proof of Theorem 1.

Proof of Theorem 1: Fix $m \in M$ and define φ: $G  M$ by $\phi ( g ) = \lambda ( g , m )$ as in the theorem. Since $G _ { m } = \phi ^ { - 1 } ( m )$ , it follows that $G _ { m }$ is a closed subset of G. The axioms for a left action clearly imply that $G _ { m }$ is closed under multiplication and inverse, so it is a subgroup.

I claim that $G _ { m }$ is a submanifold of G. To see this, let ${ \mathfrak { g } } _ { m } \subset { \mathfrak { g } } = T _ { e } G$ be the kernel of the mapping $\phi ^ { \prime } ( e ) { : } T _ { e } G  T _ { m } M$ . Since φ $L _ { g } = \lambda _ { g } \ :$ ◦ φ for all $g \in G$ , the Chain Rule yields a commutative diagram:

$$
\begin{array} { l c c } { { \mathfrak { g } } } & { { \stackrel { L _ { g } ^ { \prime } ( e ) } { \longrightarrow } } } & { { T _ { g } G } } \\ { { { } } } & { { { } } } & { { { } } } \\ { { \phi ^ { \prime } ( e ) \rule { 0 ex } { 5 ex } } } & { { { } } } & { { { \Biggl \downarrow \phi ^ { \prime } ( g ) } } } \\ { { { T _ { m } M \stackrel { \lambda _ { g } ^ { \prime } ( m ) } { \longrightarrow } } } } & { { T _ { g \cdot m } M } } \end{array}
$$

Since both $L _ { g } ^ { \prime } ( e )$ and $\lambda _ { g } ^ { \prime } ( m )$ are isomorphisms, it follows that ker $( \phi ^ { \prime } ( g ) ) = L _ { g } ^ { \prime } ( e ) ( \mathfrak { g } _ { m } )$ for all $g \in G$ . In particular, the rank of $\phi ^ { \prime } ( g )$ is independent of $g \in G$ . By the Implicit Function Theorem (see Exercise 2), it follows that $\phi ^ { - 1 } ( m ) = G _ { m }$ is a smooth submanifold of G.

It remains to show that the orbit $G \cdot m$ can be given the structure of a smooth submanifold of M with the stated properties. That is, that $G \cdot m$ can be given a second countable, Hausdorff, locally Euclidean topology and a smooth structure for which the inclusion map $G \cdot m \hookrightarrow M$ is a smooth immersion and for which the map φ: $G  G \cdot m$ is a submersion.

Before embarking on this task, it is useful to remark on the nature of the fibers of the map $\phi .$ . By the axioms for left actions, $\phi ( h ) = h \cdot m = g \cdot m = \phi ( g )$ if and only if $g ^ { - 1 } h \cdot m = m$ , i.e., if and only if $g ^ { - 1 } h$ lies in $G _ { m }$ . This is equivalent to the condition that h lie in the left Gm-coset $g G _ { m }$ . Thus, the fibers of the map φ are the left $G _ { m } \mathrm { - c o s e t s }$ in G. In particular, the map $\phi$ establishes a bijection $\bar { \phi } { : } G / G _ { m } \to G \cdot m$ .

First, I specify the topology on $G \cdot m$ to be quotient topology induced by the surjective map φ: $G  G \cdot m$ Thus, a set U in $G \cdot m$ is open if and only if $\phi ^ { - 1 } ( U )$ is open in G. Since $\phi \colon G \to M$ is continuous, the quotient topology on the image $G \cdot m$ is at least as fine as the subspace topology G · m inherits via inclusion into M. Since the subspace topology is Hausdorff, the quotient topology must be also. Moreover, the quotient topology on $G \cdot m$ is also second countable since the topology of G is. For the rest of the proof, ‘the topology on $G \cdot m ^ { \ ' }$ means the quotient topology.

I will both establish the locally Euclidean nature of this topology and construct a smooth structure on $G \cdot m$ at the same time by finding the required neighborhood charts and proving that they are smooth on overlaps. First, however, I need a lemma establishing the existence of a ‘tubular neighborhood’ of the submanifold $G _ { m } \subset G$ . Let $d = \dim ( G ) -$ dim $\left( G _ { m } \right)$ . Then there exists a smooth mapping ψ: $B ^ { d } \to G$ (where $B ^ { d }$ is an open ball about 0 in $\mathbb { R } ^ { d } )$ so that $\psi ( 0 ) = e$ and so that g is the direct sum of the subspaces ${ \mathfrak { g } } _ { m }$ and $V = \psi ^ { \prime } ( 0 ) ( \mathbb { R } ^ { d } )$ . By the Chain Rule and the definition of ${ \mathfrak { g } } _ { m }$ , it follows that $( \phi \circ \psi ) ^ { \prime } ( 0 ) \colon \mathbb { R } ^ { d } \to$

$T _ { m } M$ is injective. Thus, by restricting to a smaller ball in $\mathbb { R } ^ { d }$ if necessary, I may assume henceforth that $\phi \circ \psi \colon B ^ { d } \to M$ is a smooth embedding.

Consider the mapping Ψ: $B ^ { d } \times G _ { m } \to G$ defined by $\Psi ( x , g ) = \psi ( x ) g$ . I claim that Ψ is a diffeomorphism onto its image (which is an open set), say $U = \Psi ( B ^ { d } \times G _ { m } ) \subset G$ (Thus, U forms a sort of ‘tubular neighborhood’ of the submanifold $G _ { m }$ in G.)

To see this, first I show that Ψ is one-to-one: If $\Psi ( x _ { 1 } , g _ { 1 } ) = \Psi ( x _ { 2 } , g _ { 2 } )$ , then

$$
( \phi \circ \psi ) ( x _ { 1 } ) = \psi ( x _ { 1 } ) \cdot m = ( \psi ( x _ { 1 } ) g _ { 1 } ) \cdot m = ( \psi ( x _ { 2 } ) g _ { 2 } ) \cdot m = \psi ( x _ { 2 } ) \cdot m = ( \phi \circ \psi ) ( x _ { 2 } ) ,
$$

so the injectivity of φ ◦ ψ implies $x _ { 1 } = x _ { 2 }$ . Since $\psi ( x _ { 1 } ) g _ { 1 } = \psi ( x _ { 2 } ) g _ { 2 }$ , this in turn implies that $g _ { 1 } = g _ { 2 }$

Second, I must show that the derivative

$$
\Psi ^ { \prime } ( x , g ) \colon T _ { x } \mathbb { R } ^ { d } \oplus T _ { g } G _ { m } \to T _ { \psi ( x ) g } G
$$

is an isomorphism for all $( x , g ) \in B ^ { d } \times G _ { m }$ . However, from the beginning of the proof, ker $( \phi ^ { \prime } ( \psi ( x ) g ) ) = L _ { \psi ( x ) q } ^ { \prime } ( e ) ( \mathfrak { g } _ { m } )$ and this latter space is clearly $\Psi ^ { \prime } ( x , g ) ( 0 \oplus T _ { g } G _ { m } )$ . On the other hand, since $\dot { \phi ( \Psi ( x , g ) ) } = \phi \circ \psi ( x )$ , it follows that

$$
\phi ^ { \prime } ( \Psi ( x , g ) ) \bigl ( \Psi ^ { \prime } ( x , g ) ( T _ { x } \mathbb { R } ^ { d } \oplus 0 ) \bigr ) = ( \phi \circ \psi ) ^ { \prime } ( x ) ( T _ { x } \mathbb { R } ^ { d } )
$$

and this latter space has dimension d by construction. Hence, $\Psi ^ { \prime } ( x , g ) ( T _ { x } \mathbb { R } ^ { d } \oplus 0 )$ is a d-dimensional subspace of $T _ { \psi ( x ) g } G$ that is transverse to $\Psi ^ { \prime } ( x , g ) ( 0 \oplus T _ { g } G _ { m } )$ Thus, $\Psi ^ { \prime } ( x , g ) \colon T _ { x } \mathbb { R } ^ { d } \oplus T _ { g } G _ { m } \to T _ { \psi ( x ) g } G$ is surjective and hence an isomorphism, as desired.

This completes the proof that Ψ is a diffeomorphism onto U. It follows that the inverse of Ψ is smooth and can be written in the form $\Psi ^ { - 1 } = \pi _ { 1 } \times \pi _ { 2 }$ where $\pi _ { 1 } \colon U \to B ^ { d }$ and $\pi _ { 2 } { \colon } U \to G _ { m }$ are smooth submersions.

Now, for each $g \in G$ , define $\rho _ { g } \colon B ^ { d } \to M$ by the formula $\rho _ { g } ( x ) = \phi { \bigl ( } g \psi ( x ) { \bigr ) }$ . Then $\rho _ { g } = \lambda _ { g } \circ \phi \circ \psi .$ , so $\rho _ { g }$ is a smooth embedding of $B ^ { d }$ into M . By construction, $U =$ $\dot { \phi ^ { - 1 } } ( \phi \circ \dot { \psi } ( B ^ { d } ) ) = \phi ^ { - 1 } \bar { ( } \rho _ { e } ( B ^ { d } ) )$ is an open set in G, so it follows that $\rho _ { e } ( B ^ { d } )$ is an open neighborhood of $e \cdot m = m$ in $G \cdot m$ . By the axioms for left actions, it follows that $\phi ^ { - 1 } \big ( \rho _ { g } ( B ^ { d } ) \big ) \ : = \ : L _ { g } ( U )$ (which is open in G) for all $g \in G$ Thus, $\rho _ { g } ( B ^ { d } )$ is an open neighborhood of $g \cdot m$ in $G \cdot m$ (in the quotient topology). Moreover, contemplating the commutative square

$$
\begin{array} { r l } { U } & { { } \xrightarrow { L _ { g } } \quad L _ { g } ( U ) } \\ { \pi _ { 1 } \Big \downarrow } & { { } \qquad \Big \downarrow \phi } \\ { B ^ { d } } & { { } \xrightarrow { \rho _ { g } } \quad \rho _ { g } ( B ^ { d } ) } \end{array}
$$

whose upper horizontal arrow is a diffeomorphism that identifies the fibers of the vertical arrows (each of which is a topological identification map) implies that $\rho _ { g }$ is, in fact, a homeomorphism onto its image. Thus, the quotient topology is locally Euclidean.

Finally, I show that the ‘patches’ $\rho _ { g }$ overlap smoothly. Suppose that

$$
\rho _ { g } ( B ^ { d } ) \cap \rho _ { h } ( B ^ { d } ) \neq \emptyset .
$$

Then, because the maps $\rho _ { g }$ and $\rho _ { h }$ are homeomorphisms,

$$
\rho _ { g } ( B ^ { d } ) \cap \rho _ { h } ( B ^ { d } ) = \rho _ { g } ( W _ { 1 } ) = \rho _ { h } ( W _ { 2 } )
$$

where $W _ { i } \neq \emptyset$ are open subsets of $B ^ { d }$ . It follows that

$$
L _ { g } \bigl ( \Psi ( W _ { 1 } \times G _ { m } ) \bigr ) = L _ { h } \bigl ( \Psi ( W _ { 2 } \times G _ { m } ) \bigr ) .
$$

Thus, if $\tau \colon W _ { 1 } \to W _ { 2 }$ is defined by the rule $\tau = \pi _ { 1 } \circ L _ { h ^ { - 1 } } \circ L _ { g } \circ \psi$ , then $\tau$ is a smooth map with smooth inverse $\tau ^ { - 1 } = \pi _ { 1 } \circ L _ { q ^ { - 1 } } \circ L _ { h } \circ \psi$ and hence is a diffeomorphism. Moreover, we have $\rho _ { g } = \rho _ { h } \circ \tau$ , thus establishing that the patches $\rho _ { g }$ overlap smoothly and hence that the patches define the structure of a smooth manifold on $G \cdot m$

That the map $\phi \colon G \to G \cdot m$ is a smooth submersion and that the inclusion $G \cdot m \hookrightarrow M$ is a smooth one-to-one immersion are now clear. 

It is worth remarking that the proof of Theorem 1 shows that the Lie algebra of $G _ { m }$ is the subspace ${ \mathfrak { g } } _ { m }$ . In particular, if $G _ { m } = \{ e \}$ , then the map $\phi \colon G \to M$ is a one-to-one immersion.

The proof also brings out the fact that the orbit $G \cdot m$ can be identified with the left coset space $G / G _ { m }$ , which thereby inherits the structure of a smooth manifold. It is natural to wonder which subgroups H of G have the property that the coset space $G / H$ can be given the structure of a smooth manifold for which the coset projection $\pi { \colon } G \to G / H$ is a smooth map. This question is answered by the following result. The proof is quite similar to that of Theorem 1, so I will only provide an outline, leaving the details as exercises for the reader.

Theorem 2: If H is a closed subgroup of a Lie group $G ,$ then the left coset space $G / H$ can be given the structure of a smooth manifold in a unique way so that the coset mapping $\pi { \colon } G \to G / H$ is a smooth submersion. Moreover, with this smooth structure, the left action $\lambda { \colon } G \times G / H \to G / H$ defined by $\lambda ( g , h H ) = g h H$ is a transitive smooth left action.

Proof: (Outline.) If the coset mapping $\pi \colon G \to G / H$ is to be a smooth submersion, elementary linear algebra tells us that the dimension of $G / H$ will have to be $d = \dim ( G ) -$ dim(H). Moreover, for every $g \in G$ , there will have to exist a smooth mapping $\psi _ { g } \colon B ^ { d } \to G$ with $\psi _ { g } ( 0 ) = g$ that is transverse to the submanifold $g H$ at $g$ and so that the composition $\pi \circ \psi \colon B ^ { d } \to G / H$ is a diffeomorphism onto a neighborhood of $g H \in G / H$ . It is not difficult to see that this is only possible if $G / H$ is endowed with the quotient topology. The hypothesis that H be closed implies that the quotient topology is Hausdorff. It is automatic that the quotient topology is second countable. The proof that the quotient topology is locally Euclidean depends on being able to construct the ‘tubular neighborhood’ U of H as constructed for the case of a stabilizer subgroup in the proof of Theorem 1. Once this is done, the rest of the construction of charts with smooth overlaps follows the end of the proof of Theorem 1 almost verbatim. 

Group Actions and Vector Fields. A left action $\lambda \colon \mathbb { R } \times M \to M$ (where R has its usual additive Lie group structure) is, of course, the same thing as a flow. Associated to each flow on M is a vector field that generates this flow. The generalization of this association to more general Lie group actions is the subject of this section.

Let λ: $G \times M \to M$ be a left action. Then, for each $v \in { \mathfrak { g } }$ , there is a flow $\Psi _ { v } ^ { \lambda }$ on M defined by the formula

$$
\Psi _ { v } ^ { \lambda } ( t , m ) = e ^ { t v } \cdot m .
$$

This flow is associated to a vector field on M that we shall denote by $Y _ { v } ^ { \lambda }$ , or simply $Y _ { v }$ if the action λ is clear from context. This defines a mapping $\lambda _ { * } \colon { \mathfrak { g } } \to { \mathfrak { X } } ( M )$ , where $\lambda _ { * } ( v ) = Y _ { v } ^ { \lambda }$

Proposition 1: For each left action $\lambda \colon G \times M \to M$ , the mapping $\lambda _ { * }$ is a linear antihomomorphism from g to ${ \mathfrak { X } } ( M )$ . In other words, λ∗ is linear and

$$
\lambda _ { * } ( [ x , y ] ) = - [ \lambda _ { * } ( x ) , \lambda _ { * } ( y ) ] .
$$

Proof: For each $v \in { \mathfrak { g } }$ , let $Y _ { v }$ denote the right invariant vector field on $G$ whose value at e is v. Then, according to Lecture 2, the flow of $Y _ { v }$ on G is given by the formula $\Psi _ { v } ( t , g ) = \exp ( t v ) g$ . As usual, let $\Phi _ { v }$ denote the flow of the left invariant vector field $X _ { v }$ Then the formula

$$
\Psi _ { v } ( t , g ) = \left( \Phi _ { - v } ( t , g ^ { - 1 } ) \right) ^ { - 1 }
$$

is immediate. If $\iota _ { * } \colon \mathfrak { X } ( G ) \to \mathfrak { X } ( G )$ is the map induced by the diffeomorphism $\iota ( g ) = g ^ { - 1 }$ then the above formula implies

$$
\iota _ { * } ( X _ { - v } ) = Y _ { v } .
$$

In particular, since $\iota _ { * }$ commutes with Lie bracket, it follows that

$$
[ Y _ { x } , Y _ { y } ] = - Y _ { [ x , y ] }
$$

for all $x , y \in { \mathfrak { g } } .$

Now, regard $Y _ { v }$ and $\Psi _ { v }$ as being defined on $G \times M$ in the obvious way, i.e., $\Psi _ { v } ( g , m ) =$ $( e ^ { t v } g , m )$ . Then λ intertwines this flow with that of $\Psi _ { v } ^ { \lambda }$ :

$$
\lambda \circ \Psi _ { v } = \Psi _ { v } ^ { \lambda } \circ \lambda .
$$

It follows that the vector fields $Y _ { v }$ and $Y _ { v } ^ { \lambda }$ are λ-related. Thus, $[ Y _ { x } ^ { \lambda } , Y _ { y } ^ { \lambda } ]$ is λ-related to $[ Y _ { x } , Y _ { y } ] = - Y _ { [ x , y ] }$ and hence must be equal to $- Y _ { [ x , y ] } ^ { \lambda }$ . Finally, since the map $v \mapsto Y _ { v }$ is clearly linear, it follows that $\lambda _ { * }$ is also linear. 

The appearance of the minus sign in the above formula is something of an annoyance and has led some authors (cf. [A]) to introduce a non-classical minus sign into either the definition of the Lie bracket of vector fields or the definition of the Lie bracket on g in order to get rid of the minus sign in this theorem. As logical as this revisionism is, it has not been particularly popular. However, it turns up just often enough that the reader of other sources should be wary of it.

Even with a minus sign, however, Proposition 1 implies that the subspace $\lambda _ { * } ( { \mathfrak { g } } ) \subset$ ${ \mathfrak { X } } ( M )$ is a (finite dimensional) Lie subalgebra of the Lie algebra of all vector fields on M.

Example: Linear Fractional Transformations. Consider the M¨obius action introduced earlier of $\operatorname { S L } ( 2 , \mathbb { R } )$ on $\mathbb { R } ^ { \mathbb { P } ^ { 1 } }$ :

$$
{ \binom { a } { c } } ^ { \ b } . s = { \frac { a s + b } { c s + d } } .
$$

A basis for the Lie algebra ${ \mathfrak { s l } } ( 2 , \mathbb { R } )$ is

$$
x = \left( { \begin{array} { c c } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} } \right) , \qquad h = \left( { \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { - 1 } \end{array} } \right) , \qquad y = \left( { \begin{array} { c c } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} } \right)
$$

Thus, for example, the flow $\Psi _ { y } ^ { \lambda }$ is given by

$$
\Psi _ { y } ^ { \lambda } ( t , s ) = \exp { \left( \begin{array} { l l } { 0 } & { 0 } \\ { t } & { 0 } \end{array} \right) } \cdot s = { \left( \begin{array} { l l } { 1 } & { 0 } \\ { t } & { 1 } \end{array} \right) } \cdot s = { \frac { s } { t s + 1 } } = s - s ^ { 2 } t + \cdot \cdot \cdot ,
$$

so $Y _ { y } ^ { \lambda } = - s ^ { 2 } \partial / \partial s$ . In fact, it is easy to see that, in general,

$$
\lambda _ { * } ( a _ { 0 } x + a _ { 1 } h + a _ { 2 } y ) = ( a _ { 0 } + 2 a _ { 1 } s - a _ { 2 } s ^ { 2 } ) \frac { \partial } { \partial s } .
$$

The basic ODE existence theorem can be regarded as saying that every vector field $X \in { \mathfrak { X } } ( M )$ arises as the ‘flow’ of a ‘local’ R-action on M. There is a generalization of this notion that covers finite dimensional subalgebras of ${ \mathfrak { X } } ( M )$

To state it precisely, we first define a local left action of a Lie group $G$ on a manifold M to be an open neighborhood $U \subset G \times M$ of $\{ e \} \times M$ together with a smooth map $\lambda { \colon } U \to M$ satisfying $\lambda ( e , m ) = m$ for all $m \in M$ and

$$
\lambda ( a , \lambda ( b , m ) ) = \lambda ( a b , m )
$$

whenever this makes sense, i.e., whenever $( b , m ) , ( a b , m )$ , and $\left( a , \lambda ( b , m ) \right)$ all lie in $U .$

For example, the linear fractional transformations of the last example could just as easily have been regarded as a local action of $\operatorname { S L } ( 2 , \mathbb { R } )$ on R, where the open set $U \subset$ $\mathrm { { \vec { s L } } } ( 2 , \mathbb { R } ) \times \mathbb { R }$ is just the set of pairs where $c s + d \neq 0$

It is easy to see that even a mere local Lie group action induces a Lie algebra antihomomorphism $\lambda _ { * } \colon { \mathfrak { g } } \to { \mathfrak { X } } ( M )$ as above. There is a converse to this statement, due, originally to Lie:

Proposition 2: Let G be a connected Lie group and let $\varphi \colon { \mathfrak { g } } \to { \mathfrak { X } } ( M )$ be a Lie algebra anti-homomorphism. Then there exists a local left action $( U , \lambda )$ of G on M so that $\lambda _ { * } = \varphi$

Proof: On $G \times M \times M$ , define, for each $v \ \in \ { \mathfrak { g } }$ , a vector field $Z _ { v }$ such that, for each $( g , p , q ) \in G \times M \times M$

$$
Z _ { v } ( g , p , q ) = \bigl ( Y _ { v } ( g ) , \ 0 _ { p } , \ \phi ( v ) ( q ) \bigr ) \in T _ { g } G \oplus T _ { p } M \oplus T _ { q } M = T _ { ( g , p , q ) } G \times M \times M .
$$

Then, by hypotheses, $[ Z _ { v } , Z _ { w } ] = - Z _ { [ v , w ] }$ for all $v , w \in { \mathfrak { g } }$ . Moreover, $Z _ { v }$ is nowhere vanishing when $v \neq 0$ (since $Y _ { v }$ is nowhere vanishing). Thus, the $Z _ { v }$ span an integrable d-plane field (where $d = \dim ( G ) )$ , and $G \times M \times M$ is foliated by the leaves of this plane field. Let F denote the foliation by these d-dimensional leaves

Let $n = \dim M$ . The union of the F -leaves that pass through the points $( e , m , m )$ for $m \in M$ is a smooth submanifold $S \subset G { \times } M { \times } M$ of dimension $d { + } n$ . The tangent space of S at $( e , m , m )$ is the direct sum of the d-dimensional subspace spanned by the vector fields $Z _ { v }$ and the n-dimensional subspace spanned by vectors of the form $( 0 , w , w )$ for $w \in T _ { m } M$ . Thus, in a neighborhood of $\{ e \} \times \mathrm { d i a g } ( M )$ , the submanifold S can be written as the graph of a smooth map $\mu \colon U \to M$ , where U is an open neighborhood of $\{ e \} \times M$ i.e., the manifold consists of triples $\left( g , m , \mu ( g , m ) \right)$ . This mapping satisfies $\mu ( e , m ) = m$ for all $m \in M$ , and it also satisfies

$$
\mu ( \exp ( t v ) g , m ) = \Phi _ { t } ( \phi ( v ) , \mu ( g , m ) )
$$

for all $v \in { \mathfrak { g } }$ and all t and g sufficiently small that $P h i _ { t } ( \phi ( v ) , \mu ( g , m ) )$ , i.e., the time t flow of $\phi ( v )$ with initial point $\mu ( g , m )$ , exists and $( \exp ( t v ) g , m )$ lies in U. From this follows the desired property that

$$
\mu ( h , \mu ( g , m ) ) = \mu ( h g , m )
$$

holds when it makes sense.

Equations of Lie type. Early in the theory of Lie groups, a special family of ordinary differential equations was singled out for study that generalized the theory of linear equations and the Riccati equation. These have come to be known as equations of Lie type. We are now going to describe this class.

Given a Lie algebra homomorphism $\lambda _ { * } \colon { \mathfrak { g } } \to { \mathfrak { X } } ( M )$ where g is the Lie algebra of a Lie group $G ,$ and a curve $\operatorname { \cal A } \colon \mathbb { R } \to { \mathfrak { g } } .$ , the ordinary differential equation for a curve $\gamma \colon \mathbb { R } \to M$

$$
\gamma ^ { \prime } ( t ) = \lambda _ { * } \bigl ( A ( t ) \bigr ) \bigl ( \gamma ( t ) \bigr )
$$

is known as an equation of Lie type.

Example: The Riccati equation. By our previous example, the classical Riccati equation

$$
s ^ { \prime } ( t ) = a _ { 0 } ( t ) + 2 a _ { 1 } ( t ) s ( t ) + a _ { 2 } ( t ) \bigl ( s ( t ) \bigr ) ^ { 2 }
$$

is an equation of Lie type for the (local) linear fractional action of $\mathrm { S L } ( 2 , \mathbb { R } )$ on $\mathbb { R } .$ The curve $A$ is

$$
A ( t ) = \binom { a _ { 1 } ( t ) } { - a _ { 2 } ( t ) } \quad \begin{array} { r } { a _ { 0 } ( t ) } \\ { - a _ { 1 } ( t ) } \end{array} \bigg )
$$

Example: Linear Equations. Every linear equation is an equation of Lie type. Let G be the matrix Lie subgroup of $\mathrm { G L } ( n { + } 1 , \mathbb { R } )$

$$
G = \{ { ( \begin{array} { l l } { A } & { B } \\ { 0 } & { 1 } \end{array} ) } { \mathrm { ~ } } | { \mathrm { ~ } } A \in \operatorname { G L } ( n , \mathbb { R } ) \quad { \mathrm { a n d } } \quad B \in \mathbb { R } ^ { n } \} .
$$

Then $G$ acts on $\mathbb { R } ^ { n }$ by the standard affine action:

$$
{ \left( \begin{array} { l l } { A } & { B } \\ { 0 } & { 1 } \end{array} \right) } \cdot x = A x + B .
$$

It is easy to verify that the inhomogeneous linear differential equation

$$
x ^ { \prime } ( t ) = a ( t ) x ( t ) + b ( t )
$$

is then a Lie equation, with

$$
A ( t ) = \left( \begin{array} { c c } { { a ( t ) } } & { { b ( t ) } } \\ { { 0 } } & { { 0 } } \end{array} \right) .
$$

The following proposition follows from the fact that a left action λ: $G \times M \to M$ relates the right invariant vector field $Y _ { v }$ to the vector field $\lambda _ { * } ( v )$ on M . Despite its simplicity, it has important consequences.

Proposition 3: $I f A { : \mathbb { R } \to \mathfrak { g } }$ is a curve in the Lie algebra of a Lie group G and $S { \mathrm { : } } \mathbb { R } \to G$ is the solution to the equation $S ^ { \prime } ( t ) = Y _ { A ( t ) } ( S ( t ) )$ with initial condition $S ( 0 ) = e$ , then on any manifold M endowed with a left G-action λ, the equation of Lie type

$$
\gamma ^ { \prime } ( t ) = \lambda _ { * } \bigl ( A ( t ) \bigr ) \bigl ( \gamma ( t ) \bigr ) ,
$$

with initial condition $\gamma ( 0 ) = m$ has, as its solution, $\gamma ( t ) = S ( t ) \cdot m$

The solution S of Proposition 3 is often called the fundamental solution of the Lie equation associated to $A ( t )$ . The most classical example of this is the fundamental solution of a linear system of equations:

$$
x ^ { \prime } ( t ) = a ( t ) x ( t )
$$

where a is an $n { \mathrm { - } } \mathrm { b y } { \mathrm { - } } n$ matrix of functions of t and x is to be a column of height n. In ODE classes, we learn that every solution of this equation is of the form $x ( t ) = X ( t ) x _ { 0 }$ where X is the n-by-n matrix of functions of t that solves the equation $X ^ { \prime } ( t ) = a ( t ) X ( t )$ with initial condition $X ( 0 ) = I _ { n }$ . Of course, this is a special case of Proposition 3 where ${ \mathrm { G L } } ( n , \mathbb { R } )$ acts on $\mathbb { R } ^ { n }$ via the standard left action described in Example 4.

Lie’s Reduction Method. I now want to explain Lie’s method of analysing equations of Lie type. Suppose that λ: $G \times M \to M$ is a left action and that $A : \mathbb { R }  { \mathfrak { g } }$ is a smooth curve. Suppose that we have found (by some method) a particular solution $\gamma \colon \mathbb { R }  M$ of the equation of Lie type associated to A with $\gamma ( 0 ) = m$ . Select a curve $g \colon { \mathbb { R } } \to G$ so that $\gamma ( t ) = g ( t ) \cdot m$ . Of course, this g will not, in general be unique, but any other choice $\tilde { g }$ will be of the form $\tilde { g } ( t ) = g ( t ) h ( t )$ where $h \colon \mathbb { R } \to G _ { m }$

I would like to choose h so that $\tilde { g }$ is the fundamental solution of the Lie equation associated to A, i.e., so that

$$
\tilde { g } ^ { \prime } ( t ) = Y _ { A ( t ) } \bigl ( \tilde { g } ( t ) \bigr ) = R _ { \tilde { g } ( t ) } ^ { \prime } \bigl ( A ( t ) \bigr )
$$

Unwinding the definitions, it follows that h must satisfy

$$
R _ { g ( t ) h ( t ) } ^ { \prime } ( A ( t ) ) = L _ { g ( t ) } ^ { \prime } \bigl ( h ^ { \prime } ( t ) \bigr ) + R _ { h ( t ) } ^ { \prime } \bigl ( g ^ { \prime } ( t ) \bigr )
$$

so

$$
R _ { h ( t ) } ^ { \prime } \left( R _ { g ( t ) } ^ { \prime } \bigl ( A ( t ) \bigr ) \right) = L _ { g ( t ) } ^ { \prime } \bigl ( h ^ { \prime } ( t ) \bigr ) + R _ { h ( t ) } ^ { \prime } \bigl ( g ^ { \prime } ( t ) \bigr )
$$

Solving for $h ^ { \prime } ( t )$ , we find that h must satisfy the differential equation

$$
h ^ { \prime } ( t ) = R _ { h ( t ) } ^ { \prime } \left( L _ { g ( t ) ^ { - 1 } } ^ { \prime } \left( R _ { g ( t ) } ^ { \prime } \big ( A ( t ) \big ) - g ^ { \prime } ( t ) \right) \right) .
$$

If we set

$$
B ( t ) = L _ { g ( t ) ^ { - 1 } } ^ { \prime } \left( R _ { g ( t ) } ^ { \prime } ( A ( t ) ) - g ^ { \prime } ( t ) \right) ,
$$

then B is clearly computable from g and A and hence may be regarded as known. Since $B ( t ) = \left( R _ { h ( t ) } ^ { \prime } \right) ^ { - 1 } \left( h ^ { \prime } ( t ) \right)$ and since h is a curve in $G _ { m }$ , it follows that B must actually be a curve in ${ \mathfrak { g } } _ { m } .$

## It follows that the equation

$$
h ^ { \prime } ( t ) = R _ { h ( t ) } ^ { \prime } \big ( B ( t ) \big )
$$

is a Lie equation for h. In other words in order to find the fundamental solution of a Lie equation for G when the particular solution with initial condition $g ( 0 ) = m \in M$ is known, it suffices to solve a Lie equation in $G _ { m } !$

This observation is known as Lie’s method of reduction. It shows how knowledge of a particular solution to a Lie equation simplifies the search for the general solution. (Note that this is definitely not true of general differential equations.) Also, Lie’s method generalizes to cover the case of several particular solutions. If one knows k particular solutions with initial values $m _ { 1 } , \ldots , m _ { k } \in M$ , then (by letting $G$ act on the k-fold product of M with itself) one can reduce finding the fundamental solution to finding the fundamental solution of a Lie equation in

$$
G _ { m _ { 1 } , \dots , m _ { k } } = G _ { m _ { 1 } } \cap G _ { m _ { 2 } } \cap \cdot \cdot \cdot \cap G _ { m _ { k } } .
$$

If it happens that this intersection is discrete, then one can explicitly compute a fundamental solution that will then yield the general solution.

Example: The Riccati equation again. Consider the Riccati equation

$$
s ^ { \prime } ( t ) = a _ { 0 } ( t ) + 2 a _ { 1 } ( t ) s ( t ) + a _ { 2 } ( t ) \bigl ( s ( t ) \bigr ) ^ { 2 }
$$

and suppose that we know a particular solution $s _ { 0 } ( t )$ . Then let

$$
g ( t ) = { \binom { 1 } { 0 } } \quad s _ { 0 } ( t ) \bigg ) ,
$$

so that $s _ { 0 } ( t ) = g ( t ) \cdot 0$ (we are using the linear fractional action of SL(2, R) on $\mathbb { R } )$ . The stabilizer of 0 is the subgroup $G _ { 0 }$ of matrices of the form:

$$
\left( \begin{array} { c c } { { u } } & { { 0 } } \\ { { v } } & { { u ^ { - 1 } } } \end{array} \right) .
$$

Thus, if we set, as usual,

$$
A ( t ) = \left( \begin{array} { c c } { { a _ { 1 } ( t ) } } & { { a _ { 0 } ( t ) } } \\ { { - a _ { 2 } ( t ) } } & { { - a _ { 1 } ( t ) } } \end{array} \right) ,
$$

then the fundamental solution of $S ^ { \prime } ( t ) = A ( t ) S ( t )$ can be written in the form

$$
S ( t ) = g ( t ) h ( t ) = \left( \begin{array} { c c c } { { 1 } } & { { s _ { 0 } ( t ) } } \\ { { 0 } } & { { 1 } } \end{array} \right) \left( \begin{array} { c c } { { u ( t ) } } & { { 0 } } \\ { { v ( t ) } } & { { \left( u ( t ) \right) ^ { - 1 } } } \end{array} \right)
$$

Solving for the matrix $B ( t )$ (which we know will have values in the Lie algebra of $G _ { 0 } )$ , we find

$$
B ( t ) = \binom { b _ { 1 } ( t ) } { b _ { 2 } ( t ) } \quad \begin{array} { c c } { 0 } \\ { - b _ { 1 } ( t ) } \end{array} \bigg ) = \left( \begin{array} { c c } { a _ { 1 } ( t ) + a _ { 2 } ( t ) s _ { 0 } ( t ) } & { 0 } \\ { - a _ { 2 } ( t ) } & { - a _ { 1 } ( t ) - a _ { 2 } ( t ) s _ { 0 } ( t ) } \end{array} \right) ,
$$

and the remaining equation to be solved is

$$
\begin{array} { r } { h ^ { \prime } ( t ) = B ( t ) h ( t ) , } \end{array}
$$

which is solvable by quadratures in the usual way:

$$
u ( t ) = \exp \left( \int _ { 0 } ^ { t } b _ { 1 } ( \tau ) d \tau \right) ,
$$

and, once $u ( t )$ has been found,

$$
v ( t ) = \bigl ( u ( t ) \bigr ) ^ { - 1 } \int _ { 0 } ^ { t } \ d b _ { 2 } ( \tau ) \bigl ( u ( \tau ) \bigr ) ^ { 2 } d \tau .
$$

Example: Linear Equations Again. Consider the general inhomogeneous n-by-n system

$$
x ^ { \prime } ( t ) = a ( t ) x ( t ) + b ( t ) .
$$

Let G be the matrix Lie subgroup of $\mathrm { G L } ( n { + } 1 , \mathbb { R } )$

$$
G = \{ { ( \begin{array} { l l } { A } & { B } \\ { 0 } & { 1 } \end{array} ) } { \mathrm { ~ } } | { \mathrm { ~ } } A \in \operatorname { G L } ( n , \mathbb { R } ) \quad { \mathrm { a n d } } \quad B \in \mathbb { R } ^ { n } \} .
$$

acting on $\mathbb { R } ^ { n }$ by the standard affine action as before. If we embed $\mathbb { R } ^ { n }$ into $\mathbb { R } ^ { n + 1 }$ by the rule

$$
x \mapsto { \binom { x } { 1 } } ,
$$

then the standard affine action of G on $\mathbb { R } ^ { n }$ extends to the standard linear action of G on $\mathbb { R } ^ { n + 1 }$ . Note that G leaves invariant the subspace $x ^ { n + 1 } = 0$ , and solutions of the Lie equation corresponding to

$$
A ( t ) = \left( \begin{array} { c c } { { a ( t ) } } & { { b ( t ) } } \\ { { 0 } } & { { 0 } } \end{array} \right)
$$

that lie in this subspace are simply solutions to the homogeneous equation $x ^ { \prime } ( t ) = a ( t ) x ( t )$ Suppose that we knew a basis for the homogeneous solutions, i.e., the fundamental solution to $X ^ { \prime } ( t ) \ = \ a ( x ) X ( t )$ with $X ( 0 ) ~ = ~ I _ { n }$ This corresponds to knowing the n particular solutions to the Lie equation on $\mathbb { R } ^ { n + 1 }$ that have the initial conditions $e _ { 1 } , \ldots , e _ { n }$ The simultaneous stabilizer of all of these points in $\mathbb { R } ^ { n + 1 }$ is the subgroup $H \subset G$ of matrices of the form

$$
\left( \begin{array} { c c } { { I _ { n } } } & { { y } } \\ { { 0 } } & { { 1 } } \end{array} \right)
$$

Thus, we choose

$$
\begin{array}{c} g ( t ) = { \binom { X ( t ) } { 0 } } \quad \mathrm { { 0 } }  \end{array}
$$

as our initial guess and look for the fundamental solution in the form:

$$
S ( t ) = g ( t ) h ( t ) = \left( \begin{array} { c c } { { X ( t ) } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right) \left( \begin{array} { c c } { { I _ { n } } } & { { y ( t ) } } \\ { { 0 } } & { { 1 } } \end{array} \right) .
$$

Expanding the condition $S ^ { \prime } ( t ) = A ( t ) S ( t )$ and using the equation $X ^ { \prime } ( t ) = a ( t ) X ( t )$ then reduces us to solving the equation

$$
y ^ { \prime } ( t ) = { \bigl ( } X ( t ) { \bigr ) } ^ { - 1 } b ( t ) ,
$$

which is easily solved by integration. The reader will probably recognize that this is precisely the classical method of ‘variation of parameters’.

Solution by quadrature. This brings us to an interesting point: Just how hard is it to compute the fundamental solution to a Lie equation of the form

$$
\gamma ^ { \prime } ( t ) = R _ { \gamma ( t ) } ^ { \prime } ( A ( t ) ) \colon
$$

One case where it is easy is if the Lie group is abelian. We have already seen that if T is a connected abelian Lie group with Lie algebra t, then the exponential map exp: $\mathbf { t } \to T$ is a surjective homomorphism. It follows that the fundamental solution of the Lie equation associated to $A \colon \mathbb { R }  { \textrm { t } }$ is given in the form

$$
S ( t ) = \exp \left( \int _ { 0 } ^ { t } A ( \tau ) d \tau \right)
$$

(Exercise: Why is this true?) Thus, the Lie equation for an abelian group is ‘solvable by quadrature’ in the classical sense.

Another instance where one can at least reduce the problem somewhat is when one has a homomorphism $\phi \colon G \to H$ and knows the fundamental solution $S _ { H }$ to the Lie equation for $\varphi \circ A { : } \mathbb { R } \to \mathfrak { h }$ . In this case, $S _ { H }$ is the particular solution (with initial condition $S _ { H } ( 0 ) = e )$ of the Lie equation on H associated to A by regarding $\phi$ as defining a left action on H. $\mathrm { B y }$ Lie’s method of reduction, therefore, we are reduced to solving a Lie equation for the group ker $( \phi ) \subset G$

Example. Suppose that G is connected and simply connected. Let g be its Lie algebra and let $[ { \mathfrak { g } } , { \mathfrak { g } } ] \subset { \mathfrak { g } }$ be the linear subspace generated by all brackets of the form $[ x , y ]$ where x and y lie in g. Then, by the Exercises of Lecture 2, we know that $[ { \mathfrak { g } } , { \mathfrak { g } } ]$ is an ideal in g (called the commutator ideal of g). Moreover, the quotient algebra $\mathfrak { t } = \mathfrak { g } / [ \mathfrak { g } , \mathfrak { g } ]$ is abelian.

Since G is connected and simply connected, Theorem 3 from Lecture 2 implies that there is a Lie group homomorphism $\phi _ { 0 } \colon G \to T _ { 0 } = \mathfrak { t }$ whose induced Lie algebra homomorphism $\varphi _ { 0 } \colon { \mathfrak { g } }  { \mathfrak { t } } = { \mathfrak { g } } / [ { \mathfrak { g } } , { \mathfrak { g } } ]$ is just the canonical quotient mapping. From our previous remarks, it follows that any Lie equation for $G$ can be reduced, by one quadrature, to a Lie equation for $G _ { 1 } = \ker \phi _ { 0 }$ . It is not difficult to check that the group $G _ { 1 }$ constructed in this argument is also connected and simply connected.

The desire to iterate this process leads to the following construction: Define the sequence $\{ \mathfrak { g } _ { k } \}$ of commutator ideals of g by the rules ${ \mathfrak { g } } _ { 0 } = { \mathfrak { g } }$ and and ${ \mathfrak { g } } _ { k + 1 } = [ { \mathfrak { g } } _ { k } , { \mathfrak { g } } _ { k } ]$ for $k \geq 0$ . Then we have the following result:

Proposition 4: Let G be a connected and simply connected Lie group for which the sequence $\left\{ { \mathfrak { g } } _ { k } \right\}$ of commutator ideals satisfies ${ \mathfrak { g } } _ { N } = ( 0 )$ for some $N > 0$ . Then any Lie equation for G can be solved by a sequence of quadratures.

A Lie algebra with the property described in Proposition 4 is called ‘solvable’. For example, the subalgebra of upper triangular matrices in ${ \mathfrak { g l } } ( n , \mathbb { R } )$ is solvable, as the reader is invited to check.

While it may seem that solvability is a lot to ask of a Lie algebra, it turns out that this property is surprisingly common. The reader can also check that, of all of the two and three dimensional Lie algebras found in Lecture 2, only ${ \mathfrak { s l } } ( 2 , \mathbb { R } )$ and so(3) fail to be solvable.

This (partly) explains why the Riccati equation holds such an important place in the theory of ODE. In some sense, it is the first Lie equation that cannot be solved by quadratures. (See the exercises for an interpretation and ‘proof’ of this statement.)

In any case, the sequence of subalgebras $\{ { \mathfrak { g } } _ { k } \}$ eventually stabilizes at a subalgebra ${ \mathfrak { g } } _ { N }$ whose Lie algebra satisfies $[ { \mathfrak { g } } _ { N } , { \mathfrak { g } } _ { N } ] = { \mathfrak { g } } _ { N }$ A Lie algebra g for which $[ { \mathfrak { g } } , { \mathfrak { g } } ] = { \mathfrak { g } }$ is called ‘perfect’. Our analysis of Lie equations shows that, by Lie’s reduction method, we can, by quadrature alone, reduce the problem of solving Lie equations to the problem of solving Lie equations associated to Lie groups with perfect algebras. Further analysis of the relation between the structure of a Lie algebra and the solvability by quadratures of any associated Lie equation leads to the development of the so-called Jordan-H¨older decomposition theorems, see [?].

## Appendix: Lie’s Transformation Groups, I

When Lie began his study of symmetry groups in the nineteenth century, the modern concepts of manifold theory were not available. Thus, the examples that he had to guide him were defined as ‘transformations in n variables’ that were often, like the M¨obius transformations on the line or like conformal transformations in space, only defined ‘almost everywhere’. Thus, at first glance, it might appear that Lie’s concept of a ‘continuous transformation group’ should correspond to what we have defined as a local Lie group action.

However, it turns out that Lie had in mind a much more general concept. For Lie, a set Γ of local diffeomorphisms in Rn formed a ‘continuous transformation group’ if it was closed under composition and inverse and moreover, the elements of Γ were characterized as the solutions of some system of differential equations.

For example, the M¨obius group on the line could be characterized as the set Γ of (non-constant) solutions f(x) of the differential equation

$$
2 f ^ { \prime \prime \prime } ( x ) f ^ { \prime } ( x ) - 3 { \bigl ( } f ^ { \prime \prime } ( x ) { \bigr ) } ^ { 2 } = 0 .
$$

As another example, the ‘group’ of area preserving transformations of the plane could be characterized as the set of solutions $\big ( f ( x , y ) , g ( x , y ) \big )$ to the equation

$$
f _ { x } g _ { y } - g _ { x } f _ { y } \equiv 1 ,
$$

while the ‘group’ of holomorphic transformations of the plane

$$
\mathbb { R } ^ { 2 }
$$

(regarded as C) was the set of solutions $\big ( f ( x , y ) , g ( x , y ) \big )$ to the equations

$$
f _ { x } - g _ { y } = f _ { y } + g _ { x } = 0 .
$$

Notice a big difference between the first example and the other two. In the first example, there is only a 3-parameter family of local solutions and each of these solutions patches together on $\mathbb { R P } ^ { 1 } = \mathbb { R } \cup \{ \infty \}$ to become an element of the global Lie group action of SL(2, R) on $\mathbb { R } ^ { \mathbb { P } ^ { 1 } }$ . In the other two examples, there are many local solutions that cannot be extended to the entire plane, much less any ‘completion’. Moreover in the volume preserving example, it is clear that no finite dimensional Lie group could ever contain all of the globally defined volume preserving transformations of the plane.

Lie regarded these latter two examples as ‘infinite continuous groups’. Nowadays, we would call them ‘infinite dimensional pseudo-groups’. I will say more about this point of view in an appendix to Lecture 6.

Since Lie did not have a group manifold to work with, he did not regard his ‘infinite groups’ as pathological. Instead of trying to find a global description of the groups, he worked with what he called the ‘infinitesimal transformations’ of Γ. We would say that, for each of his groups Γ, he considered the space of vector fields $\gamma \subset { \mathfrak { X } } ( \mathbb { R } ^ { n } )$ whose (local) flows were 1-parameter ‘subgroups’ of Γ. For example, the infinitesimal transformations associated to the area preserving transformations are the vector fields

$$
X = f ( x , y ) { \frac { \partial } { \partial x } } + g ( x , y ) { \frac { \partial } { \partial y } }
$$

that are divergence free, i.e., satisfy $f _ { x } + g _ { y } = 0$

Lie ‘showed’ that for any ‘continuous transformation group’ Γ, the associated set of vector fields γ was actually closed under addition, scalar multiplication (by constants), and, most significantly, the Lie bracket. (The reason for the quotes around ‘showed’ is that Lie was not careful to specify the nature of the differential equations that he was using to define his groups. Without adding some sort of constant rank or non-degeneracy hypotheses, many of his proofs are incorrect.)

For Lie, every subalgebra L of the algebra $\mathfrak { X } ( \mathbb { R } ^ { n } )$ that could be characterized by some system of pde was to be regarded the Lie algebra of some Lie group. Thus, rather than classify actual groups (that might not really be groups because of domain problems), Lie classified subalgebras of the algebra of vector fields.

In the case that L was finite dimensional, Lie actually proved that there was a ‘germ’ of a Lie group (in our sense) and a local Lie group action that generated this algebra of vector fields. This is Lie’s so-called Third Fundamental Theorem.

The case where L was infinite dimensional remained rather intractable. I will have more to say about this in Lecture 6. For now, though, I want to stress that there is a sort of analogue of actions for these ‘infinite dimensional Lie groups’.

For example, if M is a manifold and Diff(M) is the group of (global) diffeomorphisms, then we can regard the natural (evaluation) map $\lambda \colon \mathsf { D i f f } ( M ) \times M \to M$ given by $\lambda ( \phi , m ) =$ $\phi ( m )$ as a faithful Lie group action. If M is compact, then every vector field is complete, so, at least formally, the induced map $\lambda _ { * } \colon T _ { i d } \operatorname { D i f f } ( M ) \to { \mathfrak { X } } ( M )$ ought to be an isomorphism of vector spaces. If our analogy with the finite dimensional case is to hold $\mathrm { u p } , \ \lambda _ { * }$ must reverse the Lie bracket.

Of course, since we have not defined a smooth structure on Diff(M), it is not immediately clear how to make sense of $T _ { i d } \mathrm { D i f f } ( M )$ . I will prefer to proceed formally and simply define the Lie algebra diff(M ) of Diff(M ) to be the vector space ${ \mathfrak { X } } ( M )$ with the Lie algebra bracket given by the negative of the vector field Lie bracket.

With this definition, it follows that a left action $\lambda \colon G \times M \to M$ where G is finite dimensional can simply be regarded as a homomorphism $\Lambda \colon G \to \mathsf { D i f f } ( M )$ inducing a homomorphism of Lie algebras.

A modern treatment of this subject can be found in [SS].

## Appendix: Connections and Curvature

In this appendix, I want briefly to describe the notions of connections and curvature on principal bundles in the language that I will be using them in the examples in this Lecture.

Let G be a Lie group with Lie algebra g and let $\omega _ { G }$ be the canonical g-valued, leftinvariant 1-form on $G$

Principal Bundles. Let M be an n-manifold and let P be a principal right G-bundle over M. Thus, P comes equipped with a submersion $\pi \colon P  M$ and a free right action $\rho \colon P \times G \to P$ so that the fibers of $\pi$ are the G-orbits of $\rho .$

The Gauge Group. The group $\operatorname { A u t } ( P )$ of automorphisms of $P$ is, by definition, the set of diffeomorphisms $\phi \colon P \to P$ that are compatible with the two structure maps, i.e.,

$$
\pi \circ \phi = \pi \qquad { \mathrm { a n d } } \qquad \rho _ { g } \circ \phi = \phi \circ \rho _ { g } \quad { \mathrm { f o r ~ a l l ~ } } g \in G .
$$

For reasons having to do with Physics, this group is nowadays referred to as the gauge group of P . Of course, $\mathsf { A u t } ( P )$ is not a finite dimensional Lie group, but it would have been considered by Lie himself as a perfectly reasonable ‘continuous transformation group’ (although not a very interesting one for his purposes).

For any $\phi \in \mathsf { A u t } ( P )$ , there is a unique smooth map $\varphi \colon P  G$ that satisfies $\phi ( p ) = $ $p \cdot \varphi ( p )$ . The identity $\rho _ { g } \circ \phi = \phi \circ \rho _ { g }$ implies that $\varphi$ satisfies $\varphi ( p \cdot g ) = g ^ { - 1 } \varphi ( p ) g$ for all $g \in G$ . Conversely, any smooth map $\varphi \colon P  G$ satisfying this identity defines an element of $\sf { A u t } ( P )$ . It follows that $\operatorname { A u t } ( P )$ is the space of sections of the bundle $C ( P ) = P \times _ { C } G$ where $C \colon G \times G \to G$ is the conjugation action $C ( a , b ) = a b a ^ { - 1 }$

Moreover, it easily follows that the set of vector fields on P whose flows generate 1-parameter subgroups of $\mathsf { A u t } ( P )$ is identifiable with the space of sections of the vector bundle $\operatorname { A d } ( P ) = P \times _ { \operatorname { A d } { \mathfrak { g } } }$

Connections. Let $\mathfrak { A } ( P )$ denote the space of connections on P . Thus, an element $A \in { \mathfrak { A } } ( P )$ is, by definition, a g-valued 1-form A on P with the following two properties:

(1) For any $p \in P$ , we have $\iota _ { p } ^ { * } ( A ) = \omega _ { G }$ where $\iota _ { p } \colon G \to P$ is given by $\iota _ { p } ( g ) = p \cdot g .$

(2) For all g in G, we have $\rho _ { g } ^ { * } ( A ) = \operatorname { A d } ( g ^ { - 1 } ) ( A )$ where $\rho _ { g } \colon P  P$ is right action by g.

It follows from Property 1 that, for any connection A on P , we have $A ( \rho _ { * } ( x ) ) = x$ for all $x \in { \mathfrak { g } }$ . It follows from Property 2 that $\mathfrak { L } _ { \rho _ { * } ( x ) } A = - [ x , A ]$ for all $x \in { \mathfrak { g } }$

If $A _ { 0 }$ and $A _ { 1 }$ are connections on P , then it follows from Property 1 that the difference $\alpha = A _ { 1 } - A _ { 0 }$ is a g-valued 1-form that is ‘semi-basic’ in the sense that $\alpha ( v ) = 0$ for all $v \in \ker \pi ^ { \prime }$ . Moreover, Property 2 implies that α satisfies $\rho _ { g } ^ { * } ( \alpha ) = \mathrm { A d } ( g ^ { - 1 } ) ( \alpha )$ . Conversely, if α is any g-valued 1-form on P satisfying these latter two properties and $A \in { \mathfrak { A } } ( P )$ is a connection, then $A + \alpha$ is also a connection. It is easy to see that a 1-form α with these two properties can be regarded as a 1-form on M with values in $\operatorname { A d } ( P )$

Thus, $\mathfrak { A } ( P )$ is an affine space modeled on the vector space $\ A ^ { 1 } \left( { \mathrm { A d } } ( P ) \right)$ . In particular, if we regard $\mathfrak { A } ( P )$ as an ‘infinite dimensional manifold’, the tangent space $T _ { A } { \mathfrak { A } } ( P )$ at any point A is naturally isomorphic to $\mathcal { A } ^ { 1 } \big ( \mathrm { A d } ( P ) \big )$ .

Curvature. The curvature of a connection A is the 2-form $F _ { A } = d A + \textstyle { \frac { 1 } { 2 } } [ A , A ]$ . From our formulas above, it follows that

$$
\rho _ { * } ( x ) \lrcorner F _ { A } = \rho _ { * } ( x ) \lrcorner d A + [ x , A ] = \mathfrak { L } _ { \rho _ { * } ( x ) } A + [ x , A ] = 0 .
$$

Since the vector fields $\rho _ { * } ( x )$ span the vertical tangent spaces of P , it follows that $F _ { A }$ is a ‘semi-basic’ 2-form (with values in g). Moreover, the Ad-equivariance of A implies that $\rho _ { g } ^ { * } ( F _ { A } ) = \mathrm { A d } ( g ^ { - 1 } ) ( F _ { A } )$ Thus, $F _ { A }$ may be regarded as a section of the bundle of 2-forms on M with values in the bundle $\operatorname { A d } ( P )$

The group $\mathsf { A u t } ( P )$ acts naturally on the right on $\mathfrak { A } ( P )$ via pullback: $A \cdot \phi = \phi ^ { * } ( A )$ In terms of the corresponding map $\varphi \colon P  G$ , we have

$$
{ \cal A } \cdot \phi = \varphi ^ { * } ( \omega _ { G } ) + \mathrm { A d } \big ( \varphi ^ { - 1 } \big ) ( { \cal A } ) .
$$

It follows by direct computation that $F _ { A \cdot \phi } = \phi ^ { * } ( F _ { A } ) = \mathrm { A d } \left( \varphi ^ { - 1 } \right) ( F _ { A } )$

We say that A is flat if $F _ { A } = 0$ It is an elementary ode result that A is flat if and only if, for every $m \in M$ , there exists an open neighborhood U of m and a smooth map $\tau { \colon } \pi ^ { - 1 } ( U ) \to G$ that satisfies $\tau ( p \cdot g ) = \tau ( p ) g$ and $\tau ^ { * } ( \omega _ { G } ) = A _ { | U }$ In other words A is flat if and only if the bundle-with-connection $( P , A )$ is locally diffeomorphic to the trivial bundle-with-connection $( M \times G , \omega _ { G } )$ .

Covariant Differentiation. The space $\mathcal { A } ^ { p } \big ( \mathrm { A d } ( P ) \big )$ of p-forms on M with values in $\operatorname { A d } ( P )$ can be identified with the space of g-valued, p-forms $\beta$ on P that are both semibasic and Ad-equivariant $( \mathrm { i . e . , ~ } \rho _ { q } ^ { * } ( \beta ) = \mathrm { A d } ( g ^ { - 1 } ) ( \beta )$ for all $g \in G )$ Given such a form $\beta ,$ the expression $d \beta + [ A , \beta ]$ is easily seen to be a g-valued $( p { + } 1 )$ -form on $P$ that is also semi-basic and Ad-equivariant. It follows that this defines a first-order differential operator

$$
d _ { A } \colon { \mathcal { A } } ^ { p } \bigl ( \mathrm { A d } ( P ) \bigr ) \to { \mathcal { A } } ^ { p + 1 } \bigl ( \mathrm { A d } ( P ) \bigr )
$$

called covariant differentiation with respect to A. It is elementary to check that

$$
d _ { A } \big ( d _ { A } \beta \big ) = [ F _ { A } , \beta ] = \mathrm { a d } ( F _ { A } ) ( \beta ) .
$$

Thus, for a flat connection, $\left( \mathcal { A } ^ { \ast } ( \operatorname { A d } ( P ) ) , d _ { A } \right)$ forms a complex over M.

We also have the Bianchi identity $d _ { A } F _ { A } = 0$

For some, ‘covariant differentiation’ means only $d _ { A } \colon { \mathcal { A } } ^ { 0 } ( \operatorname { A d } ( P ) ) \to { \mathcal { A } } ^ { 1 } ( \operatorname { A d } ( P ) )$

Horizontal Lifts and Holonomy. Let A be a connection on P . $\operatorname { I f } \gamma \colon [ 0 , 1 ] \to M$ is a C1 curve and $p \in \pi ^ { - 1 } ( \gamma ( 0 ) )$ is chosen, then there exists a unique $C ^ { 1 }$ curve $\tilde { \gamma } \colon [ 0 , 1 ] \to P$ that both $ { \mathrm { \Delta ^ { 6 } l i f t s } } ^ { \prime } \gamma$ in the sense that $\gamma = \pi \circ \tilde { \gamma }$ and also satisfies the differential equation $\tilde { \gamma } ^ { * } ( A ) = 0$

(To see this, first choose any lift ${ \bar { \gamma } } \colon [ 0 , 1 ] \to P$ that satisfies $\bar { \gamma } ( 0 ) = p$ . Then the desired lifting will then be given by $\tilde { \gamma } ( t ) = \bar { \gamma } ( t ) \cdot g ( t )$ where $g \colon [ 0 , 1 ]  G$ is the solution of the Lie equation $g ^ { \prime } ( t ) = - R _ { g ( t ) } \bigl ( A ( \bar { \gamma } ^ { \prime } ( t ) ) \bigr )$ satisfying the initial condition $g ( 0 ) = e . )$

The resulting curve $\tilde { \gamma }$ is called a horizontal $l i f t$ of $\gamma , ~ \mathrm { I f } ~ \gamma$ is merely piecewise $C ^ { 1 }$ , the horizontal lift can still be defined by piecing together horizontal lifts of the $C ^ { 1 }$ -segments in the obvious way. Also, if $p ^ { \prime } = p \cdot g _ { 0 }$ , then the horizontal lift of $\gamma$ with initial condition $p ^ { \prime }$ is easily seen to be $\rho _ { g _ { 0 } } \circ \tilde { \gamma }$

Let $p \in P$ be chosen and set $m = \pi ( p )$ For every piecewise $C ^ { 1 }$ -loop $\gamma \colon [ 0 , 1 ] \to M$ based at $m$ , the horizontal lift $\tilde { \gamma }$ has the property that $\tilde { \gamma } ( 1 ) = p \cdot h ( \gamma ) $ for some unique $h ( \gamma ) \in G$ . The holonomy of $A$ at $p ,$ denoted by $H _ { A } ( p )$ is, by definition, the set of all such elements $h ( \gamma )$ of $G$ where $\gamma$ ranges over all of the piecewise $C ^ { 1 }$ closed loops based at $m$

I leave it to the reader to show that $H _ { A } ( p \cdot g ) = g ^ { - 1 } H _ { A } ( p ) g$ and that, if $p$ and $p ^ { \prime }$ can be joined by a horizontal curve in $P$ , then $H _ { A } ( p ) = H _ { A } ( p ^ { \prime } )$ . Thus, the conjugacy class of $H _ { A } ( p )$ in $G$ is independent of $p$ if M is connected.

A basic theorem due to Borel and Lichnerowitz (see [KN]) asserts that $H _ { A } ( p )$ is always a Lie subgroup of $G$ .

# Exercise Set 3:

## Actions of Lie Groups

1. Verify the claim made in the lecture that every right (respectively, left) action of a Lie group on a manifold can be rewritten as a left (respectively, right) action. Is the assumption that a left action $\lambda \colon G \times M \to M$ satisfy $\lambda ( e , m ) = m$ for all $m \in M$ really necessary?

2. Show that if $f \colon X \to Y$ is a map of smooth manifolds for which the rank of $f ^ { \prime } ( x ) { : } T _ { x } X $ $T _ { f ( x ) } Y$ is independent of x, then $f ^ { - 1 } ( y )$ is a (possibly empty) closed, smooth submanifold of X for all $y \in Y$ . Note that this properly generalizes the usual Implicit Function Theorem, which requires $f ^ { \prime } ( x )$ to be a surjection everywhere in order to conclude that $f ^ { - 1 } ( y )$ is a smooth submanifold.

(Hint: Suppose that the rank of $f ^ { \prime } ( x )$ is identically k. You want to show that $f ^ { - 1 } ( y )$ (if non-empty) is a submanifold of X of codimension k. To do this, let $x \in f ^ { - 1 } ( y )$ be given and construct a map ψ: $V \to \mathbb { R } ^ { k }$ on a neighborhood V of y so that $\psi \circ f$ is a submersion near x. Then show that $( \psi \circ f ) ^ { - 1 } ( \psi ( y ) )$ (which, by the Implicit Function Theorem, is a closed codimension k submanifold of the open set $f ^ { - 1 } ( V ) \subset X )$ is actually equal to $f ^ { - 1 } ( y )$ on some neighborhood of x. Where do you need the constant rank hypothesis?)

3. This exercise concerns the automorphism groups of Lie algebras and Lie groups.

(i) Show that, for any Lie algebra g, the group of automorphisms $\operatorname { A u t } ( { \mathfrak { g } } )$ defined by

$$
\operatorname { A u t } ( { \mathfrak { g } } ) = \{ a \in \operatorname { E n d } ( { \mathfrak { g } } ) \mid \left[ a ( x ) , a ( y ) \right] = a ( [ x , y ] ) \quad { \mathrm { f o r ~ a l l ~ } } x , y \in { \mathfrak { g } } \}
$$

is a closed Lie subgroup of GL(g). Show that its Lie algebra is

$$
\mathfrak { d e r } ( \mathfrak { g } ) = \{ a \in \operatorname { E n d } ( \mathfrak { g } ) | a \big ( [ x , y ] \big ) = \big [ a ( x ) , y \big ] + \big [ x , a ( y ) \big ] \quad \mathrm { f o r ~ a l l ~ } x , y \in \mathfrak { g } \} .
$$

(Hint: Show that $\operatorname { A u t } ( { \mathfrak { g } } )$ is the stabilizer of some point in some representation of the Lie group GL(g).)

(ii) Show that if G is a connected and simply connected Lie group with Lie algebra g, then the group of (Lie) automorphisms of G is isomorphic to $\operatorname { A u t } ( { \mathfrak { g } } )$

(iii) Show that ad: ${ \mathfrak { g } } \to { \mathrm { E n d } } ( { \mathfrak { g } } )$ actually has its image in $\mathfrak { d e r } ( \mathfrak { g } )$ , and that this image is an ideal in $\mathfrak { d e r } ( \mathfrak { g } )$ . What is the interpretation of this fact in terms of “inner” and “outer” automorphisms of G? (Hint: Use the Jacobi identity.)

(iv) Show that if the Killing form of g is non-degenerate, then $[ { \mathfrak { g } } , { \mathfrak { g } } ] = { \mathfrak { g } }$ . (Hint: Suppose that $[ { \mathfrak { g } } , { \mathfrak { g } } ]$ lies in a proper subspace of g. Then there exists an element $y \in { \mathfrak { g } }$ so that $\kappa ( [ x , z ] , y ) = 0$ for all $x , z \in { \mathfrak { g } }$ . Show that this implies that $[ x , y ] = 0$ for all $x \in { \mathfrak { g } }$ 2 and hence that $\operatorname { a d } ( y ) = 0 . )$

(v) Show that if the Killing form of g is non-degenerate, then $\mathfrak { d e r } ( { \mathfrak { g } } ) = \operatorname { a d } ( { \mathfrak { g } } )$ . This shows that all of the automorphisms of a simple Lie algebra are $\mathrm { ^ { 6 6 } i n n e r } ^ { \prime \prime }$ . (Hint: Show that the set ${ \mathfrak { p } } = \left\{ a \in { \mathfrak { d e r } } ( { \mathfrak { g } } ) | \operatorname { t r } \left( a \operatorname { a d } ( x ) \right) = 0 \right.$ for all $x \in { \mathfrak { g } } \}$ is also an ideal in $\mathfrak { d e r } ( \mathfrak { g } )$ and hence that ${ \mathfrak { d e r } } ( { \mathfrak { g } } ) = { \mathfrak { p } } \oplus \operatorname { a d } ( { \mathfrak { g } } )$ as algebras. Show that this forces ${ \mathfrak { p } } = 0$ by considering what it means for elements of p (which, after all, are derivations of g) to commute with elements in ad(g).)

4. Consider the 1-parameter group that is generated by the flow of the vector field X in the plane

$$
X = \cos y { \frac { \partial } { \partial x } } + \sin ^ { 2 } y { \frac { \partial } { \partial y } } .
$$

Show that this vector field is complete and hence yields a free R-action on the plane. Let Z also act on the plane by the action

$$
m \cdot ( x , y ) = ( ( - 1 ) ^ { m } x , y + m \pi ) .
$$

Show that these two actions commute, and hence together define a free action of $G = \mathbb { R } \times \mathbb { Z }$ on the plane. Sketch the orbits and show that, even though the G-orbits of this action are closed, and the quotient space is Hausdorff, the quotient space is not a manifold. (The point of this problem is to warn the student not to make the common mistake of thinking that the quotient of a manifold by a free Lie group action is a manifold if it is Hausdorff.)

5. Show that if $\rho \colon M \times G \to M$ is a right action, then the induced map $\rho _ { * } \colon { \mathfrak { g } } \to { \mathfrak { X } } ( M )$ satisfies $\rho _ { * } \bigl ( [ x , y ] \bigr ) = \bigl [ \rho _ { * } ( x ) , \rho _ { * } ( y ) \bigr ]$

6. Prove Proposition 2. (Hint: you are trying to find an open neighborhood U of $\{ e \} \times M$ in $G \times M$ and a smooth map $\lambda { \colon } U \to M$ with the requisite properties. To do this, look for the graph of λ as a submanifold $\Gamma \subset G \times M \times M$ that contains all the points $( e , m , m )$ and is tangent to a certain family of vector fields on $G \times M \times M$ constructed using the left invariant vector fields on G and the corresponding vector fields on M determined by the Lie algebra homomorphism $\phi \colon { \mathfrak { g } }  { \mathfrak { X } } ( M ) . \qquad $ )

7. Show that, if $A \colon \mathbb { R }  { \mathfrak { g } }$ is a curve in the Lie algebra of a Lie group G, then there exists a unique solution to the ordinary differential equation $S ^ { \prime } ( t ) = R _ { S ( t ) } ( A ( t ) )$ with initial condition $S ( 0 ) = e$ . (It is clear that a solution exists on some interval $( - \varepsilon , \varepsilon )$ in R. The problem is to show that the solution exists on all of R.)

8. Show that, under the action of ${ \mathrm { G L } } ( n , \mathbb { R } )$ on the space of symmetric $n { \mathrm { - } } \mathrm { b y } { \mathrm { - } } n$ matrices defined in the Lecture, every symmetric n-by-n matrix is in the orbit of an $I _ { p , q }$

9. This problem examines the geometry of the classical second order equation for one unknown.

(i) Rewrite the second-order ODE

$$
\frac { d ^ { 2 } x } { d t ^ { 2 } } = F ( t ) x
$$

as a system of first-order ODEs of Lie type for an action of SL(2, R) on $\mathbb { R } ^ { 2 }$(ii) Suppose in particular that $F ( t )$ is of the form $\left( f ( t ) \right) ^ { 2 } + f ^ { \prime } ( t )$ , where $f ( 0 ) \neq 0$ . Use the solution

$$
x ( t ) = \exp \left( \int _ { 0 } ^ { t } f ( \tau ) d \tau \right)
$$

to write down the fundamental solution for this Lie equation up in $\operatorname { S L } ( 2 , \mathbb { R } )$

(iii) Explain why the (more general) second order linear ODE

$$
x ^ { \prime \prime } = a ( t ) x ^ { \prime } + b ( t ) x
$$

is solvable by quadratures once we know a single solution with either $x ( 0 ) \neq 0$ or $x ^ { \prime } ( 0 ) \neq 0$ . (Hint: all two-dimensional Lie groups are solvable.)

$\mathbf { 1 0 ^ { * } }$ Show that the general equation of the form $y ^ { \prime \prime } ( x ) = f ( x ) y ( x )$ is not integrable by quadratures. Specifically, show that there do not exist “universal” functions $F _ { 0 }$ and $F _ { 1 }$ of two and three variables respectively so that the function $y$ defined by taking the most general solution of

$$
\begin{array} { l } { { u ^ { \prime } ( x ) = F _ { 0 } \big ( x , f ( x ) \big ) } } \\ { { y ^ { \prime } ( x ) = F _ { 1 } \big ( x , f ( x ) , u ( x ) \big ) } } \end{array}
$$

is the general solution of $y ^ { \prime \prime } ( x ) = f ( x ) y ( x )$ . Note that this shows that the general solution cannot be got by two quadratures, which one might expect to need since the general solution must involve two constants of integration. However, it can be shown that no matter how many quadratures one uses, one cannot get even a particular solution of $y ^ { \prime \prime } ( x ) = f ( x ) y ( x )$ (other than the trivial solution $y \equiv 0 )$ by quadrature. (If one could get a (non-trivial) particular solution this way, then, by two more quadratures, one could get the general solution.)

11. The point of this exercise is to prove Lie’s theorem (stated below) on (local) group actions on R. This theorem “explains” the importance of the Riccati equation, and why there are so few actions of Lie groups on R. Let ${ \mathfrak { g } } \subset { \mathfrak { X } } ( \mathbb { R } )$ be a finite dimensional Lie algebra of vector fields on R with the property that, at every $x \in \mathbb { R }$ , there is at least one $X \in { \mathfrak { g } }$ so that $X ( x ) \neq 0$ . (Thus, the (local) flows of the vector fields in g do not have any common fixed point.)

(i) For each $x \in \mathbb { R }$ , let ${ \mathfrak { g } } _ { x } ^ { k } \subset { \mathfrak { g } }$ denote the subspace of vector fields that vanish to order at least $k + 1$ at x. (Thus, ${ \mathfrak { g } } _ { x } ^ { - 1 } = { \mathfrak { g } }$ for all x.) Let ${ \mathfrak { g } } _ { x } ^ { \infty } \subset { \mathfrak { g } }$ denote the intersection of all the ${ \mathfrak { g } } _ { x } ^ { k }$ . Show that $\mathfrak { g } _ { x } ^ { \infty } = 0$ for all x. (Hint: Fix $a \in \mathbb { R }$ and choose an $X \in { \mathfrak { g } }$ so that $X ( a ) \neq 0$ . Make a local change of coordinates near a so that $X = \partial / \partial x$ on a neighborhood of $a .$ . Note that $[ X , \mathfrak { g } _ { a } ^ { \infty } ] \subset \mathfrak { g } _ { a } ^ { \infty }$ . Now choose a basis $Y _ { 1 } , \dots , Y _ { N }$ of ${ \mathfrak { g } } _ { a } ^ { \infty }$ and note that, near a, we have $Y _ { i } = f _ { i } \partial / \partial x$ for some functions $f _ { i }$ . Show that the $f _ { i }$ must satisfy some differential equations and then apply ODE uniqueness. Now go on from there.)

(ii) Show that the dimension of g is at most 3. (Hint: First, show that $[ \mathfrak { g } _ { x } ^ { j } , \mathfrak { g } _ { x } ^ { k } ] = \subset \mathfrak { g } _ { x } ^ { j + k }$ Now, by part (i), you know that there is a smallest integer N (which may depend on x) so that $\mathfrak { g } _ { x } ^ { N + 1 } = 0$ . Show that if $X \in { \mathfrak { g } }$ does not vanish at x and $Y _ { N } \in { \mathfrak { g } }$ vanishes to exactly order N at x, then $Y _ { N - 1 } = [ X , Y _ { N } ]$ vanishes to order exactly $N - 1$ . Conclude that the vectors $X , Y _ { 0 } , \ldots , Y _ { N }$ (where $Y _ { i - 1 } = [ X , Y _ { i } ]$ for $i > 0 )$ form a basis of g. Now, what do you know about $[ Y _ { N - 1 } , Y _ { N } ] ? )$

(iii) (Lie’s Theorem) Show that, if $\dim ( { \mathfrak { g } } ) = 2$ , then g is isomorphic to the (unique) nonabelian Lie algebra of that dimension and that there is a local change of coordinates so that

$$
{ \mathfrak { g } } = \{ ( a + b x ) \partial / \partial x | a , b \in \mathbb { R } \} .
$$

Show also that, if $\dim ( { \mathfrak { g } } ) = 3$ , then g is isomorphic to s $[ ( 2 , \mathbb { R } )$ and that there exist local changes of coordinates so that

$$
{ \mathfrak { g } } = \{ ( a + b x + c x ^ { 2 } ) \partial / \partial x | a , b , c \in \mathbb { R } \} .
$$

(In the second case, after you have shown that the algebra is isomorphic to ${ \mathfrak { s l } } ( 2 , \mathbb { R } )$ , show that, at each point of R, there exists a element $X \in { \mathfrak { g } }$ that does not vanish at the point and that satisfies $\left( \operatorname { a d } ( X ) \right) ^ { 2 } = 0$ . Now put it in the form $X = \partial / \partial x$ for some local coordinate x and ask what happens to the other elements of g.)

(iv) (This is somewhat harder.) Show that if dim $( { \mathfrak { g } } ) = 3$ , then there is a diffeomorphism of R with an open interval $I \subset \mathbb { R }$ so that g gets mapped to the algebra

$$
{ \mathfrak { g } } = \left\{ \left. ( a + b \cos x + c \sin x ) { \frac { \partial } { \partial x } } \right| a , b , c \in \mathbb { R } \ \right\} .
$$

In particular, this shows that every local action of $\operatorname { S L } ( 2 , \mathbb { R } )$ on R is the restriction of the M¨obius action on $\mathbb { R } ^ { \mathbb { P } ^ { 1 } }$ after $\mathrm { \hbar ^ { 6 6 } l i f t i n g ^ { \prime } }$ to its universal cover. Show that two intervals $I _ { 1 } = ( 0 , a )$ and $I _ { 2 } = ( 0 , b )$ are diffeomorphic in such a way as to preserve the Lie algebra g if and only if either $a = b = 2 n \pi$ for some positive integer n or else $2 n \pi < a , b < ( 2 n + 2 ) \pi$ for some positive integer n. (Hint: Show, by a local analysis, that any vector field $X \in { \mathfrak { g } }$ that vanishes at any point of R must have $\kappa ( X , X ) \geq 0$ . Now choose an X so that $\kappa ( X , X ) = - 2$ and choose a global coodinate $x : \mathbb { R } $ R so that $X = \partial / \partial x$ . You must still examine the effect of your choices on the image interval $x ( \mathbb { R } ) \subset \mathbb { R } . )$

Lie and his coworkers attempted to classify all of the finite dimensional Lie subalgebras of the vector fields on $\mathbb { R } ^ { k }$ , for $k \leq 5$ , since (they thought) this would give a classification of all of the equations of Lie type for at most 5 unknowns. The classification became extremely complex and lengthy by dimension 5 and it was abandoned. On the other hand, the project of classifying the abstract finite dimensional Lie algebras has enjoyed a great deal of success. In fact, one of the triumphs of nineteenth century mathematics was the classification, by Killing and Cartan, of all of the finite dimensional simple Lie algebras over C and R.

## Lecture 4:

## Symmetries and Conservation Laws

Variational Problems. In this Lecture, I will introduce a particular set of variational problems, the so-called ‘first-order particle Lagrangian problems’, that will serve as a link to the ‘symplectic’ geometry to be developed in the next Lecture.

Definition 1: A Lagrangian on a manifold M is a smooth function $L \colon T M \to \mathbb { R }$ . For any smooth curve $\gamma \colon [ a , b ] \to M$ , define

$$
\mathcal { F } _ { L } ( \gamma ) = \int _ { a } ^ { b } L ( \dot { \gamma } ( t ) ) d t .
$$

$\mathcal { F } _ { L }$ is called the functional associated to $L .$

(The use of the word “functional” here is classical. The reader is supposed to think of the set of all smooth curves $\gamma \colon [ a , b ] \to M$ as a sort of infinite dimensional manifold and of $\mathcal { F } _ { L }$ as a function on it.)

I have deliberately chosen to avoid the (mild) complications caused by allowing less smoothness for $L$ and $\gamma ,$ though for some purposes, it is essential to do so. The geometric points that I want to make, however will be clearest if we do not have to worry about determining the optimum regularity assumptions.

Also, some sources only require L to be defined on some open set in T M. Others allow L to “depend on $t ^ { \gamma } , \mathrm { i . e . }$ , take L to be a function on $\mathbb { R } \times T M$ . Though I will not go into any of these (slight) extensions, the reader should be aware that they exist. For example, see [A].

Example: Suppose that L: T M  R restricts to each $T _ { x } M$ to be a positive definite quadratic form. Then L defines what is usually called a Riemannian metric on $M .$ . For a curve $\gamma$ in M , the functional $\mathcal { F } _ { L } ( \gamma )$ is then twice what is usually called the “action” of $\gamma .$ This example is, by far, the most commonly occurring Lagrangian in differential geometry. We will have more to say about this below.

For a Lagrangian $L ,$ one is usually interested in finding the curves $\gamma \colon [ a , b ] \to M$ with given “endpoint conditions” $\gamma ( a ) = p$ and $\gamma ( b ) = q$ for which the functional $\mathcal { F } _ { L } ( \gamma )$ is a minimum. For example, in the case where L defines a Riemannian metric on M, the curves with fixed endpoints of minimum “action” turn out also to be the shortest curves joining those endpoints. From calculus, we know that the way to find minima of a function on a manifold is to first find the “critical points” of the function and then look among those for the minima. As mentioned before, the set of curves in M can be thought of as a sort of “infinite dimensional” manifold, but I won’t go into details on this point. What I will do instead is describe what ought to be the set of “curves” in this space (classically called “variations”) if it were a manifold.

Given a curve $\gamma \colon [ a , b ] \to M$ , a (smooth) variation of $\gamma$ with fixed endpoints is, by definition, a smooth map

$$
\Gamma : [ a , b ] \times ( - \varepsilon , \varepsilon )  M
$$

for some $\varepsilon > 0$ with the property that $\Gamma ( t , 0 ) = \gamma ( t )$ for all $t \in [ a , b ]$ and that $\Gamma ( a , s ) = \gamma ( a )$ and $\Gamma ( b , s ) = \gamma ( b )$ for all $s \in ( - \varepsilon , \varepsilon )$

In this lecture, “variation” will always mean “smooth variation with fixed endpoints”.

If L is a Lagrangian on M and Γ is a variation of $\gamma \colon [ a , b ] \to M$ , then we can define a function $\mathcal { F } _ { L , \Gamma } \colon ( - \varepsilon , \varepsilon ) \to  { \mathbb { R } }$ by setting

$$
\mathcal { F } _ { L , \Gamma } ( s ) = \mathcal { F } _ { L } ( \gamma _ { s } )
$$

where $\gamma _ { s } ( t ) = \Gamma ( t , s )$

Definition 2: A curve $\gamma \colon [ a , b ] \to M$ is L-critical if $\mathcal { F } _ { L , \Gamma } ^ { \prime } ( 0 ) = 0$ for all variations of $\gamma$ .

It is clear from calculus that a curve that minimizes $\mathcal { F } _ { L }$ among all curves with the same endpoints will have to be L-critical, so the search for minimizers usually begins with the search for the critical curves.

Canonical Coordinates. I want to examine what the problem of finding L-critical curves “looks like” in local coordinates. If $U \subset M$ is an open set on which there exists a coordinate chart $x \colon U \to \mathbb { R } ^ { n }$ , then there is a canonical extension of these coordinates to a coordinate chart $( x , p ) \colon T U \to \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ with the property that, for any curve $\gamma \colon [ a , b ] \to U _ { : }$ with coordinates $y = x \circ \gamma$ , the p-coordinates of the curve ${ \dot { \gamma } } \colon [ a , b ] \to T U$ are given by $p \circ \dot { \gamma } = \dot { y }$ . We shall call the coordinates $( x , p )$ on $T U$ , the canonical coordinates associated to the coordinate system x on $U$

The Euler-Lagrange Equations. In a canonical coordinate system $( x , p )$ on T U where U is an open set in M, the function L can be expressed as a function $L ( x , p )$ of x and p. For a curve $\gamma \colon [ a , b ] \to M$ that happens to lie in $U _ { : }$ the functional $\mathcal { F } _ { L }$ becomes simply

$$
\mathcal { F } _ { L } ( \gamma ) = \int _ { a } ^ { b } L \big ( y ( t ) , \dot { y } ( t ) \big ) d t .
$$

I will now derive the classical conditions for such a γ to be L-critical: Let $h \colon [ a , b ] \to \mathbb { R } ^ { n }$ be any smooth map that satisfies $h ( a ) = h ( b ) = 0$ . Then, for sufficiently small ε, there is a variation $\Gamma$ of $\gamma$ that is expressed in $( x , p )$ -coordinates as

$$
( x , p ) \circ \Gamma = ( y + s h , \dot { y } + s \dot { h } ) .
$$

Then, by the classic integration-by-parts method,

$$
\begin{array} { l } { \displaystyle \mathcal { F } _ { L , \Gamma } ^ { \prime } ( 0 ) = \frac { d } { d s } \Big | _ { s = 0 } \left( \int _ { a } ^ { b } L \big ( y ( t ) + s h ( t ) , \dot { y } ( t ) + s \dot { h } ( t ) \big ) d t \right) } \\ { \displaystyle = \int _ { a } ^ { b } \left( \frac { \partial L } { \partial x ^ { k } } ( y ( t ) , \dot { y } ( t ) ) h ^ { k } ( t ) + \frac { \partial L } { \partial p ^ { k } } ( y ( t ) , \dot { y } ( t ) ) \dot { h } ^ { k } ( t ) \right) d t } \\ { \displaystyle = \int _ { a } ^ { b } \left( \frac { \partial L } { \partial x ^ { k } } ( y ( t ) , \dot { y } ( t ) ) - \frac { d } { d t } \left( \frac { \partial L } { \partial p ^ { k } } ( y ( t ) , \dot { y } ( t ) ) \right) \right) h ^ { k } ( t ) d t . } \end{array}
$$

This formula is valid for any $h \colon [ a , b ] \ \to \ \mathbb { R } ^ { n }$ that vanishes at the endpoints. It follows without difficulty that the curve $\gamma$ is L-critical if and only if $y = x \circ \gamma$ satisfies the n differential equations

$$
{ \frac { \partial L } { \partial x ^ { k } } } { \big ( } y ( t ) , { \dot { y } } ( t ) { \big ) } - { \frac { d } { d t } } \left( { \frac { \partial L } { \partial p ^ { k } } } { \big ( } y ( t ) , { \dot { y } } ( t ) { \big ) } \right) = 0 , \qquad { \mathrm { f o r ~ } } 1 \leq k \leq n .
$$

These are the famous Euler-Lagrange equations.

The main drawback of the Euler-Lagrange equations in this form is that they only give necessary and sufficient conditions for a curve to be L-critical if it lies in a coordinate neighborhood $U .$ . It is not hard to show that if $\gamma \colon [ a , b ] \to M$ is L-critical, then its restriction to any subinterval $[ a ^ { \prime } , b ^ { \prime } ] \subset [ a , b ]$ is also L-critical. In particular, a necessary condition for $\gamma$ to be L-critical is that it satisfy the Euler-Lagrange equations on any subcurve that lies in a coordinate system. However, it is not clear that these ‘local conditions’ are sufficient.

Another drawback is that, as derived, the equations depend on the choice of coordinates and it is not clear that one’s success in solving them might not depend on a clever choice of coordinates.

In what follows, we want to remedy these defects. First, though, here are a couple of examples.

Example: Riemannian Metrics. Consider a Riemannian metric $L \colon T M \to \mathbb { R }$ . Then, in local canonical coordinates,

$$
L ( x , p ) = g _ { i j } ( x ) p ^ { i } p ^ { j } .
$$

where $g ( x )$ is a positive definite symmetric matrix of functions. (Remember, the summation convention is in force.) In this case, the Euler-Lagrange equations are

$$
\frac { \partial g _ { i j } } { \partial x ^ { k } } ( y ( t ) ) \dot { y } ^ { i } ( t ) \dot { y } ^ { j } ( t ) = \frac { d } { d t } \left( 2 g _ { k j } \big ( y ( t ) \big ) \dot { y } ^ { j } ( t ) \right) = 2 \frac { \partial g _ { k j } } { \partial x ^ { i } } \big ( y ( t ) \big ) \dot { y } ^ { i } ( t ) \dot { y } ^ { j } ( t ) + 2 g _ { k j } \big ( y ( t ) \big ) \ddot { y } ^ { j } ( t ) .
$$

Since the matrix $g ( x )$ is invertible for all x, these equations can be put in more familiar form by solving for the second derivatives to get

$$
\ddot { y } ^ { i } = - \Gamma _ { j k } ^ { i } ( y ) \dot { y } ^ { j } \dot { y } ^ { k }
$$

where the functions $\Gamma _ { j k } ^ { i } = \Gamma _ { k j } ^ { i }$ are given by the formula so familiar to geometers:

$$
\Gamma _ { j k } ^ { i } = { \frac { 1 } { 2 } } g ^ { i \ell } \left( { \frac { \partial g _ { \ell j } } { \partial x ^ { k } } } + { \frac { \partial g _ { \ell k } } { \partial x ^ { j } } } - { \frac { \partial g _ { j k } } { \partial x ^ { \ell } } } \right)
$$

where the matrix $\left( g ^ { i j } \right)$ is the inverse of the matrix $\left( g _ { i j } \right)$

Example: One-Forms. Another interesting case is when $L$ is linear on each tangent space, i.e., $L = \omega$ where ω is a smooth 1-form on M. In local canonical coordinates,

$$
L = a _ { i } ( x ) p ^ { i }
$$

for some functions $a _ { i }$ and the Euler-Lagrange equations become:

$$
{ \frac { \partial a _ { i } } { \partial x ^ { k } } } { \big ( } y ( t ) { \big ) } { \dot { y } } ^ { i } ( t ) = { \frac { d } { d t } } { \big ( } a _ { k } { \big ( } y ( t ) { \big ) } { \big ) } = { \frac { \partial a _ { k } } { \partial x ^ { i } } } { \big ( } y ( t ) { \big ) } { \dot { y } } ^ { i } ( t )
$$

or, simply,

$$
\left( \frac { \partial a _ { i } } { \partial x ^ { k } } ( y ) - \frac { \partial a _ { k } } { \partial x ^ { i } } ( y ) \right) \dot { y } ^ { i } = 0 .
$$

This last equation should look familiar. Recall that the exterior derivative of $\omega$ has the coordinate expression

$$
d \omega = { \frac { 1 } { 2 } } \left( { \frac { \partial a _ { j } } { \partial x ^ { i } } } - { \frac { \partial a _ { i } } { \partial x ^ { j } } } \right) d x ^ { i } \wedge d x ^ { j } .
$$

If $\gamma \colon [ a , b ] \to U$ is $\mathcal { F } _ { \omega } \mathrm { - c r i t i c a l }$ , then for every vector field $v$ along $\gamma$ the Euler-Lagrange equations imply that

$$
d \omega \big ( \dot { \gamma } ( t ) , v ( t ) \big ) = \frac { 1 } { 2 } \left( \frac { \partial a _ { j } } { \partial x ^ { i } } \big ( y ( t ) \big ) - \frac { \partial a _ { i } } { \partial x ^ { j } } \big ( y ( t ) \big ) \right) \dot { y } ^ { i } ( t ) v ^ { j } ( t ) = 0 .
$$

In other words, $\dot { \gamma } ( t ) \lrcorner d \omega = 0$ . Conversely, if this identity holds, then $\gamma$ is clearly ω-critical. This leads to the following global result:

Proposition 1: A curve $\gamma \colon [ a , b ] \to M$ is ω-critical for a 1-form $\omega$ on M if and only if it satisfies the first order differential equation

$$
\dot { \gamma } ( t ) \lrcorner d \omega = 0 .
$$

Proof: A straightforward integration-by-parts on M yields the coordinate-free formula

$$
\mathcal { F } _ { \omega , \Gamma } ^ { \prime } ( 0 ) = \int _ { a } ^ { b } d \omega \big ( \dot { \gamma } ( t ) , \frac { \partial \Gamma } { \partial s } ( t , 0 ) \big ) d t
$$

where Γ is any variation of $\gamma$ and $\frac { \partial \Gamma } { \partial s }$ is the “variation vector field” along $\gamma .$ . Since this vector field is arbitrary except for being required to vanish at the endpoints, we see that ${ } ^ { \mathfrak { a } } d \omega ( \dot { \gamma } , v ) = 0$ for all vector fields v along $\gamma ^ { \mathfrak { s } }$ is the desired condition for ω-criticality. 

The way is now paved for what will seem like a trivial observation, but, in fact, turns out to be of fundamental importance: It is the “seed” of Noether’s Theorem.

Proposition 2: Suppose that $\omega$ is a 1-form on M and that X is a vector field on M whose (local) flow leaves ω invariant. Then the function $\omega ( X )$ is constant on all ω-critical curves.

Proof: The condition that the flow of X leave $\omega$ invariant is just that $\mathfrak { L } _ { X } ( \omega ) = 0$ However, by the Cartan formula,

$$
0 = \mathfrak { L } _ { X } ( \omega ) = d ( X \lrcorner \omega ) + X \lrcorner d \omega ,
$$

so for any curve $\gamma$ in M, we have

$$
d \omega \big ( \dot { \gamma } ( t ) , X ( \gamma ( t ) ) \big ) = - d \omega \big ( X ( \gamma ( t ) ) , \dot { \gamma } ( t ) \big ) = - ( X \mathbin { \lrcorner } d \omega ) \big ( \dot { \gamma } ( t ) \big ) = d \big ( X \mathbin { \lrcorner } \omega \big ) \big ( \dot { \gamma } ( t ) \big )
$$

and this last expression is clearly the derivative of the function $X \lrcorner \omega = \omega ( X )$ along γ. Now apply Proposition 1. 

It is worth pausing a moment to think about what Proposition 2 means. The condition that the flow of X leave ω invariant is essentially saying that the flow of X is a “symmetry” of $\omega$ and hence of the functional $\mathcal { F } _ { \omega }$ . What Proposition 2 says is that a certain kind of symmetry of the functional gives rise to a “first integral” (sometimes called “conservation law”) of the equation for ω-critical curves. If the function $\omega ( X )$ is not a constant function on M , then saying that the ω-critical curves lie in its level sets is useful information about these critical curves.

Now, this idea can be applied to the general Lagrangian with symmetries. The only trick is to find the appropriate 1-form on which to evaluate ‘symmetry’ vector fields.

Proposition 3: For any Lagrangian L: $T M \to \mathbb { R }$ , there exist a unique function $E _ { L }$ on T M and a unique 1-form $\omega _ { L }$ on T M that, relative to any local coordinate system x: $U \to \mathbb { R }$ , have the expressions

$$
E _ { L } = p ^ { i } { \frac { \partial L } { \partial p ^ { i } } } - L \qquad { \mathrm { a n d } } \qquad \omega _ { L } = { \frac { \partial L } { \partial p ^ { i } } } d x ^ { i } .
$$

Moreover, $i f \gamma \colon [ a , b ] \to M$ is any curve, then $\gamma$ satisfies the Euler-Lagrange equations for L in every local coordinate system if and only if its canonical lift ${ \dot { \gamma } } \colon [ a , b ] \to T M$ satisfies

$$
\ddot { \gamma } ( t ) \lrcorner d \omega _ { L } = - d E _ { L } ( \dot { \gamma } ( t ) ) .
$$

Proof: This will mainly be a sequence of applications of the Chain Rule.

There is an invariantly defined vector field R on T M that is simply the radial vector field on each subspace $T _ { m } M$ . It is expressed in canonical coordinates as $R = p ^ { i } \partial / \partial p ^ { i }$ Now, using this vector field, the quantity $E _ { L }$ takes the form

$$
E _ { L } = - L + d L ( R ) .
$$

Thus, it is clear that $E _ { L }$ is well-defined on $^ { T M }$

Now we check the well-definition of $\omega _ { L }$ . If $z \colon U  \mathbb { R }$ is any other local coordinate system, then $z = F ( x )$ for some $F \colon \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ . The corresponding canonical coordinates on $T U$ are $( z , q )$ where $q = F ^ { \prime } ( x ) p$ . In particular,

$$
\binom { d z } { d q } = \binom { F ^ { \prime } ( x ) } { G ( x , p ) } \quad F ^ { \prime } ( x ) \bigg ) \binom { d x } { d p } .
$$

where $G$ is some matrix function whose exact form is not relevant. Then writing $L _ { z }$ for $\textstyle \left( { \frac { \partial L } { \partial z ^ { 1 } } } , \ldots , { \frac { \partial L } { \partial z ^ { n } } } \right)$ , etc., yields

$$
\begin{array} { r l } & { d L = L _ { z } d z + L _ { q } d q } \\ & { \quad = \left( L _ { z } F ^ { \prime } ( x ) + L _ { q } G ( x , p ) \right) d x + L _ { q } F ^ { \prime } ( x ) d p } \\ & { \quad = L _ { x } d x + L _ { p } d p . } \end{array}
$$

Comparing dp-coefficients yields $L _ { p } = L _ { q } F ^ { \prime } ( x )$ , so $L _ { p } d x = L _ { q } F ^ { \prime } ( x ) d x = L _ { q } d z$ . In particular, as we wished to show, there exists a well-defined 1-form $\omega _ { L }$ on T M whose coordinate expression in local canonical coordinates $( x , p )$ is $L _ { p } d x$

The remainder of the proof is a coordinate calculation. The reader will want to note that I am using the expression $\ddot { \gamma }$ to denote the velocity of the curve $\dot { \gamma }$ in $T M$ . The curve $\dot { \gamma }$ is described in $U$ as $( x , p ) = ( y , \dot { y } )$ and its velocity vector $\ddot { \gamma }$ is simply $( { \dot { x } } , { \dot { p } } ) = ( { \dot { y } } , { \ddot { y } } )$

Now, the Euler-Lagrange equations are just

$$
\frac { \partial L } { \partial x ^ { i } } ( y , \dot { y } ) = \frac { d } { d t } \left( \frac { \partial L } { \partial p ^ { i } } ( y , \dot { y } ) \right) = \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial p ^ { j } } ( y , \dot { y } ) \ddot { y } ^ { j } + \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial x ^ { j } } ( y , \dot { y } ) \dot { y } ^ { j } .
$$

Meanwhile,

$$
d \omega _ { L } = \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial p ^ { j } } d p ^ { j } \wedge d x ^ { i } + \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial x ^ { j } } d x ^ { j } \wedge d x ^ { i } ,
$$

so

$$
\ddot { \gamma } \lrcorner d \omega _ { L } = \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial p ^ { j } } ( y , \dot { y } ) \left( \ddot { y } ^ { j } d x ^ { i } - \dot { y } ^ { i } d p ^ { j } \right) + \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial x ^ { j } } ( y , \dot { y } ) \left( \dot { y } ^ { j } d x ^ { i } - \dot { y } ^ { i } d x ^ { j } \right) .
$$

On the other hand, an easy computation yields

$$
- d E _ { L } ( \dot { \gamma } ) = \left( \frac { \partial L } { \partial x ^ { i } } ( y , \dot { y } ) - \frac { \partial ^ { 2 } L } { \partial p ^ { j } \partial x ^ { i } } ( y , \dot { y } ) \dot { y } ^ { j } \right) d x ^ { i } - \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial p ^ { j } } ( y , \dot { y } ) \dot { y } ^ { i } d p ^ { j } .
$$

Comparing these last two equations, the condition $\ddot { \gamma } \lrcorner d \omega _ { L } = - d E _ { L } ( \dot { \gamma } )$ is seen to be the Euler-Lagrange equations, as desired. 

Conservation of Energy. One important consequence of Proposition 3 is that the function $E _ { L }$ is constant along the curve $\dot { \gamma }$ for any L-critical curve $\gamma \colon [ a , b ] \to M$ . This follows since, for such a curve,

$$
d E _ { L } \big ( \ddot { \gamma } ( t ) \big ) = - d \omega _ { L } \big ( \ddot { \gamma } ( t ) , \ddot { \gamma } ( t ) \big ) = 0 .
$$

$E _ { L }$ is generally interpreted as the “energy” of the Lagrangian $L$ , and this constancy of $E _ { L }$ on L-critical curves is often called the principle of Conservation of Energy.

Some sources define $E _ { L }$ as $L - d L ( R )$ My choice was to have $E _ { L }$ agree with the classical energy in the classical problems.

Definition 3: If $L \colon T M \to \mathbb { R }$ is a Lagrangian on M, a diffeomorphism $f \colon M \to M$ is said to be a symmetry of L if L is invariant under the induced diffeomorphism $f ^ { \prime } { : } T M \to T M$ , i.e., if $L \circ f ^ { \prime } = L$ . A vector field X on M is said to be an infinitesimal symmetry of L if the (local) flow $\Phi _ { t }$ of X is a symmetry of L for all t.

It is perhaps necessary to make a remark about the last part of this definition. For a vector field X that is not necessarily complete, and for any $t \in \mathbb { R }$ , the “time $t ^ { \dag }$ local flow of X is well-defined on an open set $U _ { t } \subset M$ . The local flow of X then gives a well-defined diffeomorphism $\Phi _ { t } \colon U _ { t } \to U _ { - t }$ . The requirement for X is that, for each t for which ${ U _ { t } } \ne \emptyset$ the induced map $\Phi _ { t } ^ { \prime } \colon T U _ { t } \to T U _ { - t }$ should satisfy $L \circ \Phi _ { t } ^ { \prime } = L$ . (Of course, if X is complete, then $U _ { t } = M$ for all t, so symmetry has its usual meaning.)

Let X be any vector field on M with local flow Φ. This induces a local flow on T M that is associated to a vector field $X ^ { \prime }$ on T M. If, in a local coordinate chart, x: $U \to \mathbb { R } ^ { n }$ , the vector field X has the expression

$$
X = a ^ { i } ( x ) { \frac { \partial } { \partial x ^ { i } } } ,
$$

then the reader may check that, in the associated canonical coordinates on $T U$

$$
X ^ { \prime } = a ^ { i } { \frac { \partial } { \partial x ^ { i } } } + p ^ { j } { \frac { \partial a ^ { i } } { \partial x ^ { j } } } { \frac { \partial } { \partial p ^ { i } } } .
$$

The condition that X be an infinitesimal symmetry of L is then that L be invariant under the flow of $X ^ { \prime }$ , i.e., that

$$
d L ( X ^ { \prime } ) = a ^ { i } { \frac { \partial L } { \partial x ^ { i } } } + p ^ { j } { \frac { \partial a ^ { i } } { \partial x ^ { j } } } { \frac { \partial L } { \partial p ^ { i } } } = 0 .
$$

The following theorem is now a simple calculation. Nevertheless, it is the foundation of a vast theory. It usually goes by the name “Noether’s Theorem”, though, in fact, Noether’s Theorem is more general.

Theorem 1: If X is an infinitesimal symmetry of the Lagrangian $L ,$ then the function $\omega _ { L } ( X ^ { \prime } )$ is constant on ${ \dot { \gamma } } \colon [ a , b ] \to T M$ for every L-critical path $\gamma \colon [ a , b ] \to M$

Proof: Since the flow of $X ^ { \prime }$ fixes L it should not be too surprising that it also fixes $E _ { L }$ and $\omega _ { L }$ . These facts are easily checked by the reader in local coordinates, so they are left as exercises. In particular,

$$
\pounds _ { X ^ { \prime } } \omega _ { L } = d ( X ^ { \prime } \lrcorner \omega _ { L } ) + X ^ { \prime } \lrcorner d \omega _ { L } = 0 \qquad \mathrm { a n d } \qquad \pounds _ { X ^ { \prime } } E _ { L } = d E _ { L } ( X ^ { \prime } ) = 0 \ .
$$

Thus, for any L-critical curve $\gamma$ in $M$

$$
\begin{array} { r l } & { d \bigl ( \omega _ { L } ( X ^ { \prime } ) \bigr ) \bigl ( \ddot { \gamma } ( t ) \bigr ) = d ( X ^ { \prime } - \omega _ { L } ) \bigl ( \ddot { \gamma } ( t ) \bigr ) = - \bigl ( X ^ { \prime } - d \omega _ { L } \bigr ) \bigl ( \ddot { \gamma } ( t ) \bigr ) } \\ & { \qquad = d \omega _ { L } \bigl ( \ddot { \gamma } ( t ) , X ^ { \prime } ( \dot { \gamma } ( t ) ) \bigr ) = \bigl ( \ddot { \gamma } ( t ) - d \omega _ { L } \bigr ) \bigl ( X ^ { \prime } ( \dot { \gamma } ( t ) ) \bigr ) } \\ & { \qquad = - d E _ { L } \bigl ( X ^ { \prime } ( \dot { \gamma } ( t ) ) \bigr ) = 0 . } \end{array}
$$

Hence, the function $\omega _ { L } ( X ^ { \prime } )$ is constant on ${ \dot { \gamma } } ,$ as desired.

Of course, the formula for $\omega _ { L } ( X ^ { \prime } )$ in local canonical coordinates is simply

$$
\omega _ { L } ( X ^ { \prime } ) = a ^ { i } \frac { \partial L } { \partial p ^ { i } } ,
$$

and the constancy of this function on the solution curves of the Euler-Lagrange equations is not difficult to check directly.

The principle

$$
\begin{array} { r l r l } { { \bf S y m m e t r y } } & { { } } & { \implies } & { { } } & { { \bf C o n s e r v a t i o n ~ L a w } } \end{array}
$$

is so fundamental that whenever a new system of equations is encountered an enormous effort is expended to determine its symmetries. Moreover, the intuition is often expressed that “every conservation law ought to come from some symmetry”, so whenever conserved quantities are observed in Nature (or, more accurately, our models of Nature) people nowadays look for a symmetry to explain it. Even when no symmetry is readily apparent, in many cases a sort of “hidden symmetry” can be found.

Example: Motion in a Central Force Field. Consider the Lagrangian of “kinetic minus potential energy” for an particle (of mass $m \neq 0 )$ moving in a “central force field”. Here, we take $\mathbb { R } ^ { n }$ with its usual inner product and a function $V ( | x | ^ { 2 } )$ (called the potential energy) that depends only on distance from the origin. The Lagrangian is

$$
\begin{array} { r } { L ( x , p ) = \frac { m } { 2 } | p | ^ { 2 } - V ( | x | ^ { 2 } ) . } \end{array}
$$

The function $E _ { L }$ is given by

$$
\begin{array} { r } { E _ { L } ( x , p ) = \frac { m } { 2 } | p | ^ { 2 } + V ( | x | ^ { 2 } ) , } \end{array}
$$

and $\omega _ { L } = m p ^ { i } d x ^ { i } = m p \cdot d x$

The Lagrangian L is clearly symmetric with respect to rotations about the origin. For example, the rotation in the ij-plane is generated by the vector field

$$
X _ { i j } = x ^ { j } { \frac { \partial } { \partial x ^ { i } } } - x ^ { i } { \frac { \partial } { \partial x ^ { j } } } .
$$

According to Noether’s Theorem, then, the functions

$$
\mu _ { i j } = \omega _ { L } ( X _ { i j } ^ { \prime } ) = m \big ( x ^ { j } p ^ { i } - x ^ { i } p ^ { j } \big )
$$

are constant on all solutions. These are usually called the “angular momenta”. It follows from their constancy that the bivector $\xi = y ( t ) \land \dot { y } ( t )$ is constant on any solution $x = y ( t )$ of the Euler-Lagrange equations and hence that $y ( t )$ moves in a fixed 2-plane. Thus, we are essentially reduced to the case $n = 2$ . In this case, for constants $E _ { 0 }$ and $\mu _ { 0 }$ , the equations

$$
\begin{array} { r } { \frac { m } { 2 } | p | ^ { 2 } + V ( | x | ^ { 2 } ) = E _ { 0 } \qquad \mathrm { a n d } \qquad m ( x ^ { 1 } p ^ { 2 } - x ^ { 2 } p ^ { 1 } ) = \mu _ { 0 } } \end{array}
$$

will generically define a surface in $T \mathbb { R } ^ { 2 }$ . The solution curves to the Euler-Lagrange equations

$$
\dot { x } = p \qquad \mathrm { a n d } \qquad \dot { p } = - \frac { 2 } { m } V ^ { \prime } ( | x | ^ { 2 } ) x
$$

that lie on this surface can then be analyzed by phase portrait methods. (In fact, they can be integrated by quadrature.)

Example: Riemannian metrics with Symmetries. As another example, consider the case of a Riemannian manifold with infinitesimal symmetries. If the flow of X on M preserves a Riemannian metric L, then, in local coordinates,

$$
L = g _ { i j } ( x ) p ^ { i } p ^ { j }
$$

and

$$
X = a ^ { i } ( x ) \frac { \partial } { \partial x ^ { i } } .
$$

According to Conservation of Energy and Noether’s Theorem, the functions

$$
E _ { L } = g _ { i j } ( x ) p ^ { i } p ^ { j } \qquad \mathrm { a n d } \qquad \omega _ { L } ( X ^ { \prime } ) = 2 g _ { i j } ( x ) a ^ { i } ( x ) p ^ { j }
$$

are first integrals of the geodesic equations.

For example, if a surface $S \subset \mathbb { R } ^ { 3 }$ is a surface of revolution, then the induced metric can locally be written in the form

$$
I = E ( r ) d r ^ { 2 } + 2 F ( r ) d r d \theta + G ( r ) d \theta ^ { 2 }
$$

where the rotational symmetry is generated by the vector field $X = \partial / \partial \theta$ . The following functions are then constant on solutions of the geodesic equations:

$$
E ( r ) \dot { r } ^ { 2 } + 2 F ( r ) \dot { r } \dot { \theta } + G ( r ) \dot { \theta } ^ { 2 } \qquad \mathrm { a n d } \qquad F ( r ) \dot { r } + G ( r ) \dot { \theta } .
$$

This makes it possible to integrate by quadratures the geodesic equations on a surface of revolution, a classical accomplishment. (See the Exercises for details.)

Subexample: Left Invariant Metrics on Lie Groups. Let G be a Lie group and let $\omega ^ { 1 } , \omega ^ { 2 } , \ldots , \omega ^ { n }$ be any basis for the left-invariant 1-forms on G. Consider the Lagrangian

$$
L = \left( \omega ^ { 1 } \right) ^ { 2 } + \cdot \cdot \cdot + \left( \omega ^ { n } \right) ^ { 2 } ,
$$

which defines a left-invariant metric on G. Since left translations are symmetries of this metric and since the flows of the right-invariant vector fields $Y _ { i }$ leave the left-invariant 1-forms fixed, we see that these generate symmetries of the Lagrangian L. In particular, the functions $E _ { L } = L$ and

$$
\mu _ { i } = \omega ^ { 1 } ( Y _ { i } ) \omega ^ { 1 } + \cdot \cdot \cdot + \omega ^ { n } ( Y _ { i } ) \omega ^ { n }
$$

are functions on $T G$ that are constant on all of the geodesics of G with the metric L. I will return to this example several times in future lectures.

Subsubexample: The Motion of Rigid Bodies. A special case of the Lie group example is particularly noteworthy, namely the theory of the rigid body.

A rigid body (in Rn) is a (finite) set of points $\mathbf { x } _ { 1 } , \ldots , \mathbf { x } _ { N }$ with masses $\displaystyle m _ { 1 } , \ldots , m _ { N }$ such that the distances $d _ { i j } = | \mathbf { x } _ { i } - \mathbf { x } _ { j } |$ are fixed (hence the name “rigid”). The free motion of such a body is governed by the “kinetic energy” Lagrangian

$$
L = { \frac { m _ { 1 } } { 2 } } | \mathbf { p } _ { 1 } | ^ { 2 } + \cdot \cdot \cdot + { \frac { m _ { N } } { 2 } } | \mathbf { p } _ { N } | ^ { 2 } .
$$

where $\mathbf { p } _ { i }$ represents the velocity of the i’th point mass. Here is how this can be converted into a left-invariant Lagrangian variational problem on a Lie group:

Let G be the matrix Lie group

$$
G = \{ { ( \begin{array} { l l } { A } & { b } \\ { 0 } & { 1 } \end{array} ) } \normalsize \ | \ A \in \operatorname { O } ( n ) , b \in \mathbb { R } ^ { n } \} .
$$

Then $G$ acts as the space of isometries of $\mathbb { R } ^ { n }$ with its usual metric and thus also acts on the N-fold product

$$
Y _ { N } = \mathbb { R } ^ { n } \times \mathbb { R } ^ { n } \times \cdot \cdot \cdot \times \mathbb { R } ^ { n }
$$

by the “diagonal” action. It is not difficult to show that $G$ acts transitively on the simultaneous level sets of the functions $f _ { i j } ( \mathbf { x } ) = | \mathbf { x } _ { i } - \mathbf { x } _ { j } |$ . Thus, for each symmetric matrix $\Delta = ( d _ { i j } )$ , the set

$$
M _ { \Delta } = \left\{ \mathbf x \in Y _ { N } \mid | \mathbf x _ { i } - \mathbf x _ { j } | = d _ { i j } \right\}
$$

is an orbit of G (and hence a smooth manifold) when it is not empty. The set $M _ { \Delta }$ is said to be the “configuration space” of the rigid body. (Question: Can you determine a necessary and sufficient condition on the matrix $\Delta$ so that $M _ { \Delta }$ is not empty? In other words, which rigid bodies are possible?)

Let us suppose that $M _ { \Delta }$ is not empty and let $\bar { \mathbf { x } } \in M _ { \Delta }$ be a ‘reference configuration’, which, for convenience, we shall suppose has its center of mass at the origin:

$$
m _ { k } \bar { \bf x } _ { k } = 0 .
$$

(This can always be arranged by a simultaneous translation of all of the point masses.) Now let $\gamma \colon [ a , b ] \to M _ { \Delta }$ be a curve in the configuration space. (Such curves are often called “trajectories”.) Since $M _ { \Delta }$ is a G-orbit, there is a curve $g \colon [ a , b ]  G$ so that $\gamma ( t ) = g ( t ) \cdot \bar { \mathbf { x } } .$ Let us write

$$
\gamma ( t ) = ( { \bf x } _ { 1 } ( t ) , \ldots , { \bf x } _ { N } ( t ) )
$$

and let

$$
g ( t ) = \left( \begin{array} { c c } { { A ( t ) } } & { { b ( t ) } } \\ { { 0 } } & { { 1 } } \end{array} \right) .
$$

The value of the canonical left invariant form on $g$ is

$$
g ^ { - 1 } \dot { g } = \left( \begin{array} { c c } { { \alpha } } & { { \beta } } \\ { { 0 } } & { { 0 } } \end{array} \right) = \left( \begin{array} { c c } { { A ^ { - 1 } \dot { A } } } & { { A ^ { - 1 } \dot { b } } } \\ { { 0 } } & { { 0 } } \end{array} \right) .
$$

The kinetic energy along the trajectory $\gamma$ is then

$$
{ \frac { 1 } { 2 } } \sum _ { k } m _ { k } | { \dot { \mathbf { x } } } _ { k } | ^ { 2 } = { \frac { 1 } { 2 } } \sum _ { k } m _ { k } \left( { \dot { \mathbf { x } } } _ { k } \cdot { \dot { \mathbf { x } } } _ { k } \right) = { \frac { 1 } { 2 } } \sum _ { k } m _ { k } \left( { \dot { A } } { \bar { \mathbf { x } } } _ { k } + { \dot { b } } \right) \cdot \left( { \dot { A } } { \bar { \mathbf { x } } } _ { k } + { \dot { b } } \right) .
$$

Since A is a curve in O(n), this becomes

$$
\begin{array} { r l } & { = \frac { 1 } { 2 } \displaystyle \sum _ { k } m _ { k } ( ( A ^ { - 1 } \big ( \dot { A } \bar { \mathbf { x } } _ { k } + \dot { b } \big ) ) \cdot ( ( A ^ { - 1 } \big ( \dot { A } \bar { \mathbf { x } } _ { k } + \dot { b } ) )  } \\ & { = \frac { 1 } { 2 } \displaystyle \sum _ { k } m _ { k }  ( \alpha \bar { \mathbf { x } } _ { k } + \beta ) \cdot ( \alpha \bar { \mathbf { x } } _ { k } + \beta ) . } \end{array}
$$

Using the center-of-mass normalization, this simplifies to

$$
= \frac { 1 } { 2 } \sum _ { k } m _ { k } \ \left( - \frac { t } { \bf \bar { x } } _ { k } \alpha ^ { 2 } \bar { \bf x } _ { k } + | \beta | ^ { 2 } \right) .
$$

With a slight rearrangement, this takes the simple form

$$
\begin{array} { r } { L \bigl ( \dot { \gamma } ( t ) \bigr ) = - \mathrm { t r } \left( \bigl ( \alpha ( t ) \bigr ) ^ { 2 } \mu \right) + \frac { 1 } { 2 } m | \beta ( t ) | ^ { 2 } } \end{array}
$$

where $m = m _ { 1 } + \cdot \cdot \cdot + m _ { N }$ is the total mass of the body and $\mu$ is the positive semi-definite symmetric n-by-n matrix

$$
\begin{array} { r } { \mu = \frac { 1 } { 2 } \displaystyle \sum _ { k } m _ { k } \bar { \bf x } _ { k } ^ { } \frac { t _ { - } } { { \bf x } _ { k } } . } \end{array}
$$

It is clear that we can interpret L as a left-invariant Lagrangian on G. Actually, even the formula we have found so far can be simplified: If we write $\mu = R \delta ^ { t } R$ where $\delta$ is diagonal and R is an orthogonal matrix (which we can always do), then right acting on G by the element

$$
\left( \begin{array} { c c } { { R } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right)
$$

will reduce the Lagrangian to the form

$$
L { \big ( } { \dot { g } } ( t ) { \big ) } = - \mathrm { t r } \left( { \big ( } \alpha ( t ) { \big ) } ^ { 2 } \delta \right) + { \textstyle { \frac { 1 } { 2 } } } m | \beta ( t ) | ^ { 2 } .
$$

Thus, only the eigenvalues of the matrix µ really matter in trying to solve the equations of motion of a rigid body. This observation is usually given an interpretation like “the motion of any rigid body is equivalent to the motion of its ‘ellipsoid of inertia’ ”.

Hamiltonian Form. Let us return to the consideration of the Euler-Lagrange equations. As we have seen, in expanded form, the equations in local coordinates are

$$
{ \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial p ^ { j } } } ( y , { \dot { y } } ) { \ddot { y } } ^ { j } + { \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial x ^ { j } } } ( y , { \dot { y } } ) { \dot { y } } ^ { j } - { \frac { \partial L } { \partial x ^ { i } } } ( y , { \dot { y } } ) = 0 .
$$

In order for these equations to be solvable for the highest derivatives at every possible set of initial conditions, the symmetric matrix

$$
H _ { L } ( x , p ) = \left( \frac { \partial ^ { 2 } L } { \partial p ^ { i } \partial p ^ { j } } ( x , p ) \right) .
$$

must be invertible at every point $( x , p )$

Definition 4: A Lagrangian L is said to be non-degenerate if, relative to every local coordinate system x: $U \to \mathbb { R } ^ { n }$ , the matrix $H _ { L }$ is invertible at every point of $T U$

For example, if $L \colon T M \ \to \ \mathbb { R }$ restricts to each tangent space $T _ { m } M$ to be a nondegenerate quadratic form, then L is a non-degenerate Lagrangian. In particular, when L is a Riemannian metric, L is non-degenerate.

Although Definition 4 is fairly explicit, it is certainly not coordinate free. Here is a result that may clarify the meaning of non-degenerate.

Proposition 4: The following are equivalent for a Lagrangian L: $T M \to \mathbb { R } .$

(1) L is a non-degenerate Lagrangian.

(2) In local coordinates $( x , p )$ , the functions $x ^ { 1 } , \ldots , x ^ { n } , \partial L / \partial p ^ { 1 } , \ldots , \partial L / \partial p ^ { n }$ have everywhere independent differentials.

(3) The 2-form $d \omega _ { L }$ is non-degenerate at every point of T M, i.e., for any tangent vector $v \in T ( T M ) , v \lrcorner d \omega _ { L } = 0$ implies that $v = 0$

Proof: The equivalence of (1) and (2) follows directly from the Chain Rule and is left as an exercise. The equivalence of (2) and (3) can be seen as follows: Let $v \in T _ { a } ( T M )$ be a tangent vector based at $a \in T _ { m } M$ . Choose any local any canonical local coordinate system $( x , p )$ with $m \in U$ and write $q _ { i } = \partial L / \partial p ^ { i }$ for $1 \leq i \leq n$ . Then $\omega _ { L }$ takes the form

$$
d \omega _ { L } = d q _ { i } \wedge d x ^ { i } .
$$

Thus,

$$
v \lrcorner d \omega _ { L } = d q _ { i } ( v ) d x ^ { i } - d x ^ { i } ( v ) d q _ { i } .
$$

Now, suppose that the differentials $d x ^ { 1 } , \ldots , d x ^ { n } , d q _ { i } , \ldots , d q _ { n }$ are linearly independent at a and hence span $T _ { a } ^ { * } ( T M )$ . Then, if $v \lrcorner d \omega _ { L } = 0$ , we must have $d q _ { i } ( v ) = d x ^ { i } ( v ) = 0$ , which, because the given 2n differentials form a spanning set, implies that $v = 0$ Thus, $d \omega _ { L }$ is non-degenerate at a.

On the other hand, suppose that that the differentials $d x ^ { 1 } , \ldots , d x ^ { n } , d q _ { 1 } , \ldots , d q _ { n }$ are linearly dependent at $a .$ . Then, by linear algebra, there exists a non-zero vector $v \in T _ { a } ^ { * } ( T M )$ so that $d q _ { i } ( v ) = d x ^ { i } ( v ) = 0$ However, it is then clear that $v \lrcorner d \omega _ { L } = 0$ for such a $v _ { \mathrm { : } }$ so that $d \omega _ { L }$ will be degenerate at a. 

For physical reasons, the function $q _ { i }$ is usually called the conjugate momentum to the coordinate $x ^ { i }$

Before exploring the geometric meaning of the coordinate system $( x , q )$ , we want to give the following description of the L-critical curves of a non-degenerate Lagrangian.

Proposition 5: If L: $T M \to \mathbb { R }$ is a non-degenerate Lagrangian, then there exists a unique vector field Y on T M so that, for every L-critical curve γ: $[ a , b ] \to M$ , the associated curve ${ \dot { \gamma } } \colon [ a , b ] \to T M$ is an integral curve of Y . Conversely, for any integral curve $\varphi \colon [ a , b ] \to T M$ of $Y$ , the composition $\phi = \pi \circ \varphi \colon [ a , b ] \to M$ is an L-critical curve in $M$

Proof: It is clear that we should take $Y$ to be the unique vector field on T M that satisfies $Y \lrcorner d \omega _ { L } = - d E _ { L }$ (There is only one since, by Proposition 4, $d \omega _ { L }$ is non-degenerate.) Proposition 3 then says that for every L-critical curve, its lift $\dot { \gamma }$ satisfies $\ddot { \gamma } ( t ) = Y ( \dot { \gamma } ( t ) )$ for all t, i.e., that $\dot { \gamma }$ is indeed an integral curve of $Y$

The details of the converse will be left to the reader. First, one must check that, with $\phi$ defined as above, we have ${ \dot { \phi } } = \varphi$ . This is best done in local coordinates. Second, one must check that $\phi$ is indeed L-critical, even though it may not lie entirely within a coordinate neighborhood. This may be done by computing the variation of $\phi$ restricted to appropriate subintervals and taking account of the boundary terms introduced by integration by parts when the endpoints are not fixed. Details are in the Exercises. 

The canonical vector field Y on T M is just the coordinate free way of expressing the fact that, for non-degenerate Lagrangians, the Euler-Lagrangian equations are simply a non-singular system of second order ODE for maps $\gamma \colon [ a , b ] \to M$

Unfortunately, the expression for Y in canonical $( x , p )$ -coordinates on T M is not very nice; it involves the inverse of the matrix $H _ { L }$ . However, in the $( x , q )$ -coordinates, it is a completely different story. In these coordinates, everything takes a remarkably simple form, a fact that is the cornerstone on symplectic geometry and the calculus of variations.

Before taking up the geometric interpretation of these new coordinates, let us do a few calculations. We have already seen that , in these coordinates, the canonical 1-form $\omega _ { L }$ takes the simple form $\omega _ { L } = q _ { i } d x ^ { i }$

We can also express $E _ { L }$ as a function of $( x , q )$ . It is traditional to denote this expression by $H ( x , q )$ and call it the Hamiltonian of the variational problem (even though, in a certain sense, it is the same function as $E _ { L } )$ . The equation determining the vector field $Y$ is expressed in these coordinates as

$$
\begin{array} { l } { { \displaystyle Y \lrcorner d \omega _ { L } = Y \lrcorner ( d q _ { i } \wedge d x ^ { i } ) = d q _ { i } ( Y ) d x ^ { i } - d x ^ { i } ( Y ) d q _ { i } } } \\ { { \mathrm { ~ } } } \\ { { \mathrm { ~ } = - d H = - \frac { \partial H } { \partial x ^ { i } } d x ^ { i } - \frac { \partial H } { \partial q _ { i } } d q _ { i } \mathrm { ~ , ~ } } } \end{array}
$$

so the expression for Y in these coordinates is

$$
Y = { \frac { \partial H } { \partial q _ { i } } } { \frac { \partial } { \partial x ^ { i } } } - { \frac { \partial H } { \partial x ^ { i } } } { \frac { \partial } { \partial q _ { i } } } .
$$

In particular, the flow of Y takes the form

$$
\dot { x } ^ { i } = \frac { \partial H } { \partial q _ { i } } \qquad \mathrm { a n d } \qquad \dot { q } _ { i } = - \frac { \partial H } { \partial x ^ { i } } .
$$

These equations are known as Hamilton’s Equations or, sometimes, as the Hamiltonian form of the Euler-Lagrange equations.

Part of the reason for the importance of the $( x , q )$ coordinates is the symmetric way they treat the positions and momenta. Another reason comes from the form the infinitesimal symmetries take in these coordinates: If X is an infinitesimal symmetry of L and $X ^ { \prime }$ is the induced vector field on T M with conserved quantity $G = \omega _ { L } ( X ^ { \prime } )$ , then, since $\mathfrak { L } _ { X ^ { \prime } } \omega _ { L } = 0$ ,

$$
X ^ { \prime } \lrcorner d \omega _ { \cal L } = - d ( \omega _ { \cal L } ( X ^ { \prime } ) ) = - d G .
$$

Thus, by the same analysis as above, the ODE represented by $X ^ { \prime }$ in the $( x , q )$ coordinates becomes

$$
\dot { x } ^ { i } = \frac { \partial G } { \partial q _ { i } } \qquad \mathrm { a n d } \qquad \dot { q } _ { i } = - \frac { \partial G } { \partial x ^ { i } } .
$$

In other words, in the $( x , q )$ coordinates, the flow of a symmetry $X ^ { \prime }$ has the same Hamiltonian form as the flow of the vector field Y that gives the solutions of the Euler-Lagrange equations! This method of putting the symmetries of a Lagrangian and the solutions of the Lagrangian on a sort of equal footing will be seen to have powerful consequences.

The Cotangent Bundle. Early on in this lecture, we introduced, for each coordinate chart x: $U \to \mathbb { R } ^ { n }$ , a canonical extension $( x , p ) \colon T U \to \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ and characterized it by a geometric property. There is also a canonical extension $( x , \xi ) \colon T ^ { * } U \to \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ where $\xi = ( \xi _ { i } ) \colon T ^ { * } U \to \mathbb { R } ^ { n }$ is characterized by the condition that, if $f \colon U  \mathbb { R }$ is any smooth function on U, then, regarding its exterior derivative df as a section $d f \colon U \to T ^ { * } U$ , we have

$$
\xi _ { i } \circ d f = { \frac { \partial f } { \partial x ^ { i } } } .
$$

I will leave to the reader the task of showing that $( x , \xi )$ is indeed a coordinate system on $T ^ { * } U$

It is a remarkable fact that the cotangent bundle π: $T ^ { * } M \to M$ of any smooth manifold carries a canonical 1-form $\omega$ defined by the following property: For each $\alpha \in T _ { x } ^ { * } M$ , we define the linear function $\omega _ { \alpha } \colon T _ { \alpha } \bigl ( T ^ { * } M \bigr ) \to \mathbb { R }$ by the rule $\omega _ { \alpha } ( v ) = \alpha { \big ( } \pi ^ { \prime } ( \alpha ) ( v ) { \big ) }$ . I leave to the reader the task of showing that, in canonical coordinates $( x , \xi ) \colon T ^ { * } U \to \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ , this canonical 1-form has the expression

$$
\omega = \xi _ { i } d x ^ { i } .
$$

The Legendre transformation. Now consider a smooth Lagrangian $L \colon T M \to$ R as before. We can use L to construct a smooth mapping $\tau _ { L } \colon T M \to T ^ { * } M$ as follows: At each $v \in T M$ , the 1-form $\omega _ { L } ( v )$ is semi-basic, i.e., there exists a (necessarily unique) 1- form $\tau _ { L } ( v ) \in T _ { \pi ( v ) } ^ { * } M$ so that $\omega _ { L } ( v ) = \pi ^ { * } ( \tau _ { L } ( v ) )$ . This mapping is known as the Legendre transformation associated to the Lagrangian L.

This definition is rather abstract, but, in local coordinates, it takes a simple form. The reader can easily check that in canonical coordinates associated to a coordinate chart x: $U \to \mathbb { R } ^ { n }$ , we have

$$
( x , \xi ) \circ \tau _ { L } = ( x , q ) = \big ( x ^ { i } , \frac { \partial L } { \partial p ^ { i } } \big ) .
$$

In other words, the $( x , q )$ coordinates are just the canonical coordinates on the cotangent bundle composed with the Legendre transformation! It is now immediate that $\tau _ { L }$ is a local diffeomorphism if and only if L is a non-degenerate Lagrangian. Moreover, we clearly have $\omega _ { L } = \tau _ { L } ^ { * } ( \omega )$ , so the 1-form $\omega _ { L }$ is also expressible in terms of the canonical 1-form ω and the Legendre transform.

What about the function $E _ { L }$ on T M? Let us put the following condition on the Lagrangian L: Let us assume that $\tau _ { L } \colon T M \ \to \ T ^ { * } M$ is a (one-to-one) diffeomorphism onto its image $\tau _ { L } ( T M ) \subset T ^ { * } M$ . (Note that this implies that L is non-degenerate, but is stronger than this.) Then there clearly exists a function on $\tau _ { L } ( T M )$ that pulls back to T M to be $E _ { L }$ . In fact, as the reader can easily verify, this is none other than the Hamiltonian function H constructed above.

The fact that the Hamiltonian H naturally ‘lives’ on $T ^ { * } M$ (or at least an open subset thereof) rather than on T M justifies it being regarded as distinct from the function $E _ { L }$ There is another reason for moving over to the cotangent bundle when one can: The vector field Y on $T M$ corresponds, under the Legendre transformation, to a vector field Z on $\tau _ { L } ( T M )$ that is characterized by the simple rule $Z \lrcorner d \omega = - d H$ Thus, just knowing the Hamiltonian H on an open set in $T ^ { * } M$ determines the vector field that sweeps out the solution curves! We will see that this is a very useful observation in what follows.

Poincar´e Recurrence. To conclude this lecture, I want to give an application of the geometry of the form $\omega _ { L }$ to understanding the global behavior of the L-critical curves when L is a non-degenerate Lagrangian. First, I make the following observation:

Proposition 6: Let $L \colon T M \to \mathbb { R }$ be a non-degenerate Lagrangian. Then 2n-form $\mu _ { L } =$ $( d \omega _ { L } ) ^ { n }$ is a volume form on T M (i.e., it is nowhere vanishing). Moreover the (local) flow of the vector field Y preserves this volume form.

Proof: To see that $\mu _ { L }$ is a volume form, just look in local $( x , q )$ -coordinates:

$$
\begin{array} { r l } & { \mu _ { L } = ( d \omega _ { L } ) ^ { n } = ( d q _ { i } \wedge d x ^ { i } ) ^ { n } } \\ & { \qquad = n ! d q _ { 1 } \wedge d x ^ { 2 } \wedge d q _ { 2 } \wedge d x ^ { 2 } \wedge \cdots \wedge d q _ { n } \wedge d x ^ { n } . } \end{array}
$$

By Proposition 4, this latter form is not zero.

Finally, since

$$
\mathfrak { L } _ { Y } ( d \omega _ { L } ) = d ( Y \lrcorner d \omega _ { L } ) = - d \bigl ( d E _ { L } \bigr ) = 0 ,
$$

it follows that the (local) flow of Y preserves $d \omega _ { L }$ and hence preserves $\mu _ { L }$

Now we shall give an application of Proposition 6. This is the famous Poincar´e Recurrence Theorem.

Theorem 2: Let $L \colon T M \to \mathbb { R }$ be a non-degenerate Lagrangian and suppose that $E _ { L }$ is a proper function on T M. Then the vector field Y is complete, with flow $\Phi \colon \mathbb { R } \times T M  T M$ . Moreover, this flow is recurrent in the following sense: For any point $v \in T M$ , any open neighborhood U of v, and any positive time interval $T > 0$ , there exists an integer $N > 0$ so that $\Phi ( T N , U ) \cap U \neq \emptyset$

Proof: The completeness of the flow of Y follows immediately from the fact that the integral curve of Y that passes through $v \in T M$ must stay in the compact set $E _ { L } ^ { - 1 } \big ( E _ { L } ( v ) \big )$ (Recall that $E _ { L }$ is constant on all of the integral curves of Y .) Details are left to the reader.

I now turn to the proof of the recurrence property. Let $E _ { 0 } = E _ { L } ( v )$ . By hypothesis, the set $C = E _ { L } ^ { - 1 } \big ( [ E _ { 0 } - 1 , E _ { 0 } + 1 ] \big )$ is compact, so the $\mu _ { L } .$ -volume of the open set $W =$ $E _ { L } ^ { - 1 } \big ( ( E _ { 0 } - 1 , E _ { 0 } + 1 ) \big )$ (which lies inside C) is finite. It clearly suffices to prove the recurrence property for any open neighborhood U of v that lies inside W , so let us assume that $U \subset W$

Let $\phi \colon W \ \to \ W$ be the diffeomorphism $\phi ( w ) = \Phi ( T , w )$ This diffeomorphism is clearly invertible and preserves the $\mu _ { L } \mathrm { - v o l u m e }$ of open sets in W . Consider the open sets $U ^ { k } = \phi ^ { k } ( U )$ for $k > 0$ (integers). These open sets all have the same $\mu _ { L } \mathrm { - v o l u m e }$ and hence cannot be all disjoint since then their union (which lies in W ) would have infinite $\mu _ { L } \mathrm { - v o l u m e }$ . Let $0 < j < k$ be two integers so that $U ^ { j } \cap U ^ { k } \neq \emptyset$ . Then, since

$$
U ^ { j } \cap U ^ { k } = \phi ^ { j } ( U ) \cap \phi ^ { k } ( U ) = \phi ^ { j } \big ( U \cap \phi ^ { k - j } ( U ) \big ) ,
$$

it follows that $U \cap \phi ^ { k - j } ( U ) \neq \emptyset$ , as we wished to show.

This theorem has the amazing consequence that, whenever one has a non-degenerate Lagrangian with a proper energy function, the corresponding mechanical system “recurs” in the sense that “arbitrarily near any given initial condition, there is another initial condition so that the evolution brings this initial condition back arbitrarily close to the first initial condition”. I realize that this statement is somewhat vague and subject to misinterpretation, but the precise statement has already been given, so there seems not to be much harm in giving the paraphrase.

# Exercise Set 4: Symmetries and Conservation Laws

1. Show that two Lagrangians $L _ { 1 } , L _ { 2 } \colon T M  \mathbb { R }$ satisfy

$$
E _ { L _ { 1 } } = E _ { L _ { 2 } } \mathrm { a n d } d \omega _ { L _ { 1 } } = d \omega _ { L _ { 2 } }
$$

if and only if there is a smooth function f on M so that ${ L _ { 1 } } = { L _ { 2 } } + d f$ . Such Lagrangians are said to differ by a “divergence term.” Show that such Lagrangians share the same critical curves and that one is non-degenerate if and only if the other is.

2. What does Conservation of Energy mean for the case where L defines a Riemannian metric on M ?

3. Show that the equations for geodesics of a rotationally invariant metric of the form

$$
I = E ( r ) d r ^ { 2 } + 2 F ( r ) d r d \theta + G ( r ) d \theta ^ { 2 }
$$

can be integrated by separation of variables and quadratures. (Hint: Start with the conservation laws we already know:

$$
\begin{array} { r } { E ( r ) \dot { r } ^ { 2 } + 2 F ( r ) \dot { r } \dot { \theta } + G ( r ) \dot { \theta } ^ { 2 } = v _ { 0 } ^ { 2 } } \\ { F ( r ) \dot { r } + G ( r ) \dot { \theta } = u _ { 0 } } \end{array}
$$

where $v _ { 0 }$ and $u _ { 0 }$ are constants. Then eliminate $\dot { \theta }$ and go on from there.)

4. The definition of $\omega _ { L }$ given in the text might be regarded as somewhat unsatisfactory since it is given in coordinates and not “invariantly”. Show that the following invariant description of $\omega _ { L }$ is valid: The manifold T M inherits some extra structure by virtue of being the tangent bundle of another manifold M. Let $\pi \colon T M \to M$ be the basepoint projection. Then π is a submersion: For every $a \in T M$

$$
\pi ^ { \prime } ( a ) { : } T _ { a } T M \to T _ { \pi ( a ) } M
$$

is a surjection and the fiber at $\pi ( a )$ is equal to

$$
\pi ^ { - 1 } \bigl ( \pi ( a ) \bigr ) = T _ { \pi ( a ) } M .
$$

It follows that the kernel of $\pi ^ { \prime } ( a )$ (i.e., the “vertical space” of the bundle π: $T M  M$ at $a )$ is naturally isomorphic to $T _ { \pi ( a ) } M$ . Call this isomorphism α: $T _ { \pi ( a ) } { \cal M } \tilde {  } \ker ( \pi ^ { \prime } ( a ) )$ Then the 1-form $\omega _ { L }$ is defined by

$$
\omega _ { L } ( v ) = d L { \big ( } \alpha \circ \pi ^ { \prime } ( v ) { \big ) } \qquad { \mathrm { f o r ~ } } v \in T ( T M ) .
$$

Hint: Show that, in local canonical coordinates, the map $\alpha \circ \pi ^ { \prime }$ satisfies

$$
\alpha \circ \pi ^ { \prime } \left( a ^ { i } { \frac { \partial } { \partial x ^ { i } } } + b ^ { i } { \frac { \partial } { \partial p ^ { i } } } \right) = a ^ { i } { \frac { \partial } { \partial p ^ { i } } } .
$$

5. For any vector field $X$ on $M .$ , let the associated vector field on T M be denoted $X ^ { \prime }$ Show that if X has the form

$$
X = a ^ { i } { \frac { \partial } { \partial x ^ { i } } }
$$

in some local coordinate system, then, in the associated canonical $( x , p )$ coordinates, $X ^ { \prime }$ has the form

$$
X ^ { \prime } = a ^ { i } { \frac { \partial } { \partial x ^ { i } } } + p ^ { j } { \frac { \partial a ^ { i } } { \partial x ^ { j } } } { \frac { \partial } { \partial p ^ { i } } } .
$$

6. Show that conservation of angular momenta in the motion of a point mass in a central force field implies Kepler’s Law that “equal areas are swept out over equal time intervals.” Show also that, in the $n = 2$ case, employing the conservation of energy and angular momentum allows one to integrate the equations of motion by quadratures. (Hint: For the second part of the problem, introduce polar coordinates: $( x ^ { 1 } , x ^ { 2 } ) = ( r \cos \theta , r \sin \theta ) . \nonumber$ )

7. In the example of the motion of a rigid body, show that the Lagrangian on G is always non-negative and is non-degenerate (so that L defines a left-invariant metric on G) if and only if the matrix $\mu$ has at most one zero eigenvalue. Show that L is degenerate if and only if the rigid body lies in a subspace of dimension at most $n { - } 2$

8. Supply the details in the proof of Proposition 5. You will want to go back to the integration-by-parts derivation of the Euler-Lagrange equations and show that, even if the variation Γ induced by h does not have fixed endpoints, we still get a local coordinate formula of the form

$$
\mathcal { F } _ { L , \Gamma } ^ { \prime } ( 0 ) = \frac { \partial L } { \partial p ^ { k } } \big ( y ( b ) , \dot { y } ( b ) \big ) h ^ { k } ( b ) - \frac { \partial L } { \partial p ^ { k } } \big ( y ( a ) , \dot { y } ( a ) \big ) h ^ { k } ( a )
$$

for any variation of a solution of the Euler-Lagrange equations. Give these “boundary terms” an invariant geometric meaning and show that they cancel out when we sum over a partition of a (fixed-endpoint) variation of an L-critical curve $\gamma$ into subcurves that lie in coordinate neighborhoods.)

9. (Alternate to Exercise 8.) Here is another approach to proving Proposition 5. Instead of dividing the curve up into sub-curves, show that for any variation Γ of a curve $\gamma \colon [ a , b ] \to M$ (not necessarily with fixed endpoints), we have the formula

$$
\mathfrak { F } _ { L , \Gamma } ^ { \prime } ( 0 ) = \omega _ { L } \bigl ( V ( b ) \bigr ) - \omega _ { L } \bigl ( V ( a ) \bigr ) - \int _ { a } ^ { b } d \omega _ { L } \bigl ( \ddot { \gamma } ( t ) , V ( t ) \bigr ) + d E _ { L } \bigl ( V ( t ) \bigr ) d t
$$

where $V ( t ) = \dot { \Gamma } ^ { \prime } ( t , 0 ) ( \partial / \partial s )$ is the “variation vector $\mathrm { f i e l d } ^ { \prime \prime }$ at $s = 0$ of the lifted variation Γ in ˙ T M. Conclude that, whether L is non-degenerate or not, the condition $\ddot { \gamma } \lrcorner d \omega _ { L } +$ $d E _ { L } \big ( \dot { \gamma } ( t ) \big ) = 0$ is the necessary and sufficient condition that $\gamma$ be L-critical.10. The Two Body Problem. Consider a pair of point masses (with masses $m _ { 1 }$ and $m _ { 2 } )$ that move freely subject to a force between them that depends only on the distance between the two bodies and is directed along the line joining the two bodies. This is what is classically known as the Two Body Problem. It is represented by a Lagrangian on the manifold $M = \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ with position coordinates $x _ { 1 } , x _ { 2 } \colon M \to \mathbb { R } ^ { n }$ of the form

$$
L ( x _ { 1 } , x _ { 2 } , p _ { 1 } , p _ { 2 } ) = \frac { m _ { 1 } } { 2 } | p _ { 1 } | ^ { 2 } + \frac { m _ { 2 } } { 2 } | p _ { 2 } | ^ { 2 } - V ( | x _ { 1 } - x _ { 2 } | ^ { 2 } ) .
$$

(Here, $( p _ { 1 } , p _ { 2 } )$ are the canonical fiber (velocity) coordinates on TM associated to the coordinate system $( x _ { 1 } , x _ { 2 } ) . )$ Notice that L has the form “kinetic minus potential”. Show that rotations and translations in $\mathbb { R } ^ { n }$ generate a group of symmetries of this Lagrangian and compute the conserved quantities. What is the interpretation of the conservation law associated to the translations?

11. The Sliding Particle. Suppose that a particle of unit weight and mass (remember: “geometric units” means never having to state your constants) slides without friction on a smooth hypersurface $x ^ { n + 1 } = F ( x ^ { 1 } , . . . , x ^ { n } )$ subject only to the force of gravity (which is directed downward along the ${ x ^ { n + 1 } } \mathrm { - a x i s } )$ Show that the “kinetic-minus-potential” Lagrangian for this motion in the x-coordinates is

$$
L = { \textstyle \frac { 1 } { 2 } } \left( ( p ^ { 1 } ) ^ { 2 } + \dots + ( p ^ { n } ) ^ { 2 } + \bigl ( \frac { \partial F } { \partial x ^ { i } } p ^ { i } \bigr ) ^ { 2 } \right) - F ( x ^ { 1 } , \dots , x ^ { n } ) .
$$

Show that this is a non-degenerate Lagrangian and that its energy $E _ { L }$ is proper if and only if $F ^ { - 1 } \bigl ( ( - \infty , a ] \bigr )$ is compact for all $a \in \mathbb { R }$

Suppose that F is invariant under rotation, i.e., that

$$
F ( x ^ { 1 } , \ldots , x ^ { n } ) = f \left( ( x ^ { 1 } ) ^ { 2 } + \cdot \cdot \cdot + ( x ^ { n } ) ^ { 2 } \right)
$$

for some smooth function f. Show that the “shadow” of the particle in $\mathbb { R } ^ { n }$ stays in a fixed 2-plane. Show that the equations of motion can be integrated by quadrature.

Remark: This Lagrangian is also used to model a small ball of unit mass and weight “rolling without friction in a cup”. Of course, in this formulation, the kinetic energy stored in the ball by its spinning is ignored. If you want to take this ‘spinning’ energy into account, then you must study quite a different Lagrangian, especially if you assume that the ball rolls without slipping. This goes into the very interesting theory of ‘non-holonomic systems’, which we (unfortunately) do not have time to go into.

12. Let L be a Lagrangian that restricts to each fiber $T _ { x } M$ to be a non-degenerate (though not necessarily positive definite) quadratic form. Show that $L$ is non-degnerate as a Lagrangian and that the Legendre mapping $\tau _ { L } \colon T M \to T ^ { * } M$ is an isomorphism of vector bundles. Show that, if L is, in addition a positive definite quadratic form on each fiber, then the new Lagrangian defined by

$$
\tilde { L } = \left( L + 1 \right) ^ { \frac { 1 } { 2 } }
$$

is also a non-degenerate Lagrangian, but that the map $\tau _ { \tilde { L } } \colon T M \to T ^ { * } M$ , though one-to-one, is not onto.

## Lecture 5:

## Symplectic Manifolds, I

In Lecture 4, I associated a non-degenerate 2-form $d \omega _ { L }$ on T M to every non-degenerate Lagrangian $L \colon T M \to \mathbb { R }$ . In this section, I want to begin a more systematic study of the geometry of manifolds on which there is specified a closed, non-degenerate 2-form.

## Symplectic Algebra.

First, I will develop the algebraic precursors of the manifold concepts that are to follow. For simplicity, all of these constructions will be carried out on vector spaces over the reals, but they could equally well have been carried out over any field of characteristic not equal to 2.

Symplectic Vector Spaces. A bilinear pairing $B \colon V \times V \to \mathbb { R }$ is said to be skewsymmetric (or alternating) if $B ( x , y ) = - B ( y , x )$ for all $x , y$ in V . The space of skewsymmetric bilinear pairings on V will be denoted by $A ^ { 2 } ( V )$ . The set $A ^ { 2 } ( V )$ is a vector space under the obvious addition and scalar multiplication and is naturally identified with $\Lambda ^ { 2 } ( V ^ { \ast } )$ , the space of exterior 2-forms on V . The elements of $A ^ { 2 } ( V )$ are often called skew-symmetric bilinear forms on V. A pairing $B \in A ^ { 2 } ( V )$ is said to be non-degenerate if, for every non-zero $v \in V$ , there is a $w \in V$ for which $B ( v , w ) \neq 0$

Definition 1: A symplectic space is a pair (V, B) where V is a vector space and B is a non-degenerate, skew-symmetric, bilinear pairing on V .

Example. Let $V = \mathbb { R } ^ { 2 n }$ and let $J _ { n }$ be the 2n-by-2n matrix

$$
J _ { n } = \left( \begin{array} { c c } { { 0 _ { n } } } & { { I _ { n } } } \\ { { - I _ { n } } } & { { 0 _ { n } } } \end{array} \right) .
$$

For vectors $v , w \in \mathbb { R } ^ { 2 n }$ , define

$$
B _ { 0 } ( x , y ) = ^ { t } x J _ { n } y .
$$

Then it is clear that $B _ { 0 }$ is bilinear and skew-symmetric. Moreover, in components

$$
B _ { 0 } ( x , y ) = x ^ { 1 } y ^ { n + 1 } + \cdot \cdot \cdot + x ^ { n } y ^ { 2 n } - x ^ { n + 1 } y ^ { 1 } - \cdot \cdot \cdot - x ^ { 2 n } y ^ { n }
$$

so it is clear that if $B _ { 0 } ( x , y ) = 0$ for all $y \in \mathbb { R } ^ { 2 n }$ then $x = 0$ . Hence, $B _ { 0 }$ is non-degenerate.

Generally, in order for $B ( x , y ) = ^ { t } x A y$ to define a skew-symmetric bilinear form on $\mathbb { R } ^ { n }$ , it is only necessary that A be a skew-symmetric n-by-n matrix. Conversely, every skew-symmetric bilinear form B on $\mathbb { R } ^ { n }$ can be written in this form for some unique skewsymmetric n-by-n matrix A. In order that this B be non-degenerate, it is necessary and sufficient that A be invertible. (See the Exercises.)

The Symplectic Group. Now, a linear transformation $R \colon \mathbb { R } ^ { 2 n }  \mathbb { R } ^ { 2 n }$ preserves $B _ { 0 }$ , i.e., satisfies $B _ { 0 } ( R x , R y ) = B _ { 0 } ( x , y )$ for all $x , y \in \mathbb { R } ^ { 2 n }$ , if and only if ${ } ^ { t } R J _ { n } R = J _ { n }$ . This motivates the following definition:

Definition 2: The subgroup of $\operatorname { G L } ( 2 n , \mathbb { R } )$ defined by

$$
\operatorname { S p } ( n , \mathbb { R } ) = \left\{ R \in \operatorname { G L } ( 2 n , \mathbb { R } ) \ | \ ^ { t } R J _ { n } R = J _ { n } \right\}
$$

is called the symplectic group of rank n.

It is clear that $\operatorname { S p } ( n , \mathbb { R } )$ is a (closed) subgroup of ${ \mathrm { G L } } ( 2 n , \mathbb { R } )$ . In the Exercises, you are asked to prove that $\operatorname { S p } ( n , \mathbb { R } )$ is a Lie group of dimension $2 n ^ { 2 } + n$ and to derive other of its properties.

Symplectic Normal Form. The following proposition shows that there is a normal form for finite dimensional symplectic spaces.

Proposition 1: If (V, B) is a finite dimensional symplectic space, then there exists a basis $e _ { 1 } , \ldots , e _ { n } , f ^ { 1 } \ldots , f ^ { n }$ of V so that, for all $1 \leq i , j \leq n$ ,

$$
B ( e _ { i } , e _ { j } ) = 0 , \qquad B ( e _ { i } , f ^ { j } ) = \delta _ { i } ^ { j } , \mathrm { ~ a n d ~ } \qquad B ( f ^ { i } , f ^ { j } ) = 0
$$

Proof: The desired basis will be constructed in two steps. Let $m = \dim ( V )$

Suppose that for some $n \geq 0$ , we have found a sequence of linearly independent vectors $e _ { 1 } , \ldots , e _ { n }$ so that $B ( e _ { i } , e _ { j } ) = 0$ for all $1 \leq i , j \leq n$ . Consider the vector space $W _ { n } \subset V$ that consists of all vectors $w \in V$ so that $B ( e _ { i } , w ) = 0$ for all $1 \leq i \leq n$ Since the $e _ { i }$ are linearly independent and since B is non-degenerate, it follows that $W _ { n }$ has dimension $m - n$ . We must have $n \leq m - n$ since all of the vectors $e _ { 1 } , \ldots , e _ { n }$ clearly lie in $W _ { n }$

If $n \ < \ m { - } n$ , then there exists a vector $e _ { n + 1 } ~ \in ~ W _ { n }$ that is linearly independent from $e _ { 1 } , \ldots , e _ { n }$ . It follows that the sequence $e _ { 1 } , \ldots , e _ { n + 1 }$ satisfies $B ( e _ { i } , e _ { j } ) = 0$ for all $1 \leq i , j \leq n + 1$ (Since B is skew-symmetric, $B ( e _ { n + 1 } , e _ { n + 1 } ) = 0$ is automatic.) This extension process can be repeated until we reach a stage where $n = m - n , { \mathrm { i . e . , ~ } } m = 2 n$ . At that point, we will have a sequence $e _ { 1 } , \ldots , e _ { n }$ for which $B ( e _ { i } , e _ { j } ) = 0$ for all $1 \leq i , j \leq n$

Next, we construct the sequence $f ^ { 1 } , \ldots , f ^ { n }$ . For each j in the range $1 \leq j \leq n$ consider the set of n linear equations

$$
B ( e _ { i } , w ) = \delta _ { i } ^ { j } , \qquad 1 \leq i \leq n .
$$

We know that these n equations are linearly independent, so there exists a solution $f _ { 0 } ^ { j }$ . Of course, once one particular solution is found, any other solution is of the form $f ^ { j } = f _ { 0 } ^ { j } { + } a ^ { j i } e _ { i }$ for some $n ^ { 2 }$ numbers $a ^ { j i }$ . Thus, we have found the general solutions $f ^ { j }$ to the equations $B ( e _ { i } , f ^ { j } ) = \delta _ { i } ^ { j }$

We now show that we can choose the $a ^ { i j }$ so as to satisfy the last remaining set of conditions, $B ( f ^ { i } , f ^ { j } ) = 0$ . If we set $b ^ { i j } = B ( f _ { 0 } ^ { i } , f _ { 0 } ^ { j } ) = - b ^ { j i }$ , then we can compute

$$
\begin{array} { c } { { B ( f ^ { i } , f ^ { j } ) = B ( f _ { 0 } ^ { i } , f _ { 0 } ^ { j } ) + B ( a ^ { i k } e _ { k } , f _ { 0 } ^ { j } ) + B ( f _ { 0 } ^ { i } , a ^ { j l } e _ { l } ) + B ( a ^ { i k } e _ { k } , a ^ { j l } e _ { l } ) } } \\ { { { } } } \\ { { = b ^ { i j } + a ^ { i j } - a ^ { j i } + 0 . } } \end{array}
$$

Thus, it suffices to set $a ^ { i j } = - b ^ { i j } / 2$ . (This is where the hypothesis that the characteristic of R is not 2 is used.)

Finally, it remains to show that the vectors $e _ { 1 } , \ldots , e _ { n } , f ^ { 1 } \ldots , f ^ { n }$ form a basis of V . Since we already know that dim $( V ) = 2 n$ , it is enough to show that these vectors are linearly independent. However, any linear relation of the form

$$
a ^ { i } e _ { i } + b _ { j } f ^ { j } = 0 ,
$$

implies $b _ { k } = B ( e _ { k } , a ^ { i } e _ { i } + b _ { j } f ^ { j } ) = 0 { \mathrm { ~ a n d ~ } } a ^ { k } = - B ( f ^ { k } , a ^ { i } e _ { i } + b _ { j } f ^ { j } ) = 0 .$

◮ We often say that a basis of the form found in Proposition 1 is a symplectic or standard basis of the symplectic space $( V , B )$

Symplectic Reduction of Vector Spaces. If $B \colon V \times V  \mathbb { R }$ is a skew-symmetric bilinear form (possibly degenerate), define the null space of B to be the subspace

$$
N _ { B } = \left\{ v \in V \vert B ( v , w ) = 0 { \mathrm { f o r ~ a l l } } w \in V \right\} .
$$

On the quotient vector space $\overline { { V } } = V / N _ { B }$ , there is a well-defined skew-symmetric bilinear form $\overline { { B } } : \bar { V } \times \overline { { V } }  \mathbb { R }$ given by

$$
\overline { { B } } ( \overline { { x } } , \overline { { y } } ) = B ( x , y )
$$

where $\textstyle { \overline { { x } } }$ and $\overline { y }$ are the cosets in $\overline { V }$ of x and y in V . It is easy to see that $( \overline { { V } } , \overline { { B } } )$ is a symplectic space.

Definition 2: If B is a skew-symmetric bilinear form on a vector space V , then the symplectic space $( \overline { { V } } , \overline { { B } } )$ is called the symplectic reduction of $( V , B )$

Here is an application of the symplectic reduction idea: Using the identification of $A ^ { 2 } ( V )$ with $\Lambda ^ { 2 } ( V ^ { \ast } )$ mentioned earlier, Proposition 1 allows us to write down a normal form for any alternating 2-form on any finite dimensional vector space.

Proposition 2: For any non-zero $\beta \in \Lambda ^ { 2 } ( V ^ { * } )$ , there exist an integer $n \leq { \frac { 1 } { 2 } } \dim ( V )$ and linearly independent 1-forms $\omega ^ { 1 } , \omega ^ { 2 } , \ldots , \omega ^ { 2 \dot { n } } \in V ^ { * }$ for which

$$
\beta = \omega ^ { 1 } \wedge \omega ^ { 2 } + \omega ^ { 3 } \wedge \omega ^ { 4 } \dots + \omega ^ { 2 n - 1 } \wedge \omega ^ { 2 n } .
$$

Thus, n is the largest integer so that $\beta ^ { n } \neq 0$

Proof: Regard $\beta$ as a skew-symmetric bilinear form B on V in the usual way. Let $( \overline { { V } } , \overline { { B } } )$ be the symplectic reduction of $( V , B )$ . Since $B \neq 0$ , we known that ${ \overline { { V } } } \neq \{ 0 \}$ . Let dim $( { \overline { { V } } } ) = 2 n \geq 2$ and let $e _ { 1 } , \ldots , e _ { n } , f ^ { 1 } \ldots , f ^ { n }$ be elements of V so that $\overline { { e } } _ { 1 } , \ldots , \overline { { e } } _ { n } , \overline { { f } } ^ { 1 } \ldots , \overline { { f } } ^ { n }$ forms a symplectic basis of $\overline { V }$ with respect to $\overline { B }$ . Let $p = \dim ( V ) - 2 n$ , and let $b _ { 1 } , \dotsc , b _ { p }$ be a basis of $N _ { B }$ •

It is easy to see that

$$
\mathbf { b } = \left( e _ { 1 } ~ f ^ { 1 } ~ e _ { 2 } ~ f ^ { 2 } ~ \cdots ~ e _ { n } ~ f ^ { n } ~ b _ { 1 } ~ \cdots ~ b _ { p } \right)
$$

forms a basis of V . Let

$$
\omega ^ { 1 } \cdot \cdot \cdot \omega ^ { 2 n + p }
$$

denote the dual basis of $V ^ { * }$ . Then, as the reader can easily check, the 2-form

$$
\Omega = \omega ^ { 1 } \wedge \omega ^ { 2 } + \omega ^ { 3 } \wedge \omega ^ { 4 } \dots + \omega ^ { 2 n - 1 } \wedge \omega ^ { 2 n }
$$

has the same values as $\beta$ does on all pairs of elements of b. Of course this implies that $\beta = \Omega$ . The rest of the Proposition also follows easily since, for example, we have

$$
\beta ^ { n } = n ! \omega ^ { 1 } \wedge \cdot \cdot \cdot \wedge \omega ^ { 2 n } \neq 0 ,
$$

although $\beta ^ { n + 1 }$ clearly vanishes.

If we regard $\beta$ as an element of $A ^ { 2 } ( V )$ , then n is one-half the dimension of $\overline { V }$ . Some sources call the integer n the half-rank of $\beta$ and others call n the rank. I use ‘half-rank’.

Note that, unlike the case of symmetric bilinear forms, there is no notion of signature type or ‘positive definiteness’ for skew-symmetric forms.

◮ It follows from Proposition 2 that for $\beta$ in $A ^ { 2 } ( V )$ , where V is finite dimensional, the pair $( V , \beta )$ is a symplectic space if and only if V has dimension 2n for some n and $\beta ^ { n } \neq 0$

Subspaces of Symplectic Vector Spaces. Let Ω be a symplectic form on a vector space V . For any subspace $W \subset V$ , we define the Ω-complement to W to be the subspace

$$
W ^ { \perp } = \{ v \in V | \Omega ( v , w ) = 0 \mathrm { ~ f o r ~ a l l ~ } w \in W \} .
$$

The Ω-complement of a subspace W is sometimes called its skew-complement. It is an exercise for the reader to check that, because Ω is non-degenerate, $\left( W ^ { \perp } \right) ^ { \perp } = W$ and that, when V is finite-dimensional,

$$
\mathrm { d i m } \ W + \mathrm { d i m } \ W ^ { \perp } = \mathrm { d i m } \ V .
$$

However, unlike the case of an orthogonal with respect to a positive definite inner product, the intersection $W \cap W ^ { \perp }$ does not have to be the zero subspace. For example, in an Ω-standard basis for V , the vectors $e _ { 1 } , \ldots , e _ { n }$ obviously span a subspace L that satisfies $L ^ { \perp } = L$

If V is finite dimensional, it turns out (see the Exercises) that, up to symplectic linear transformations of V , a subspace $W \subset V$ is characterized by the numbers d = dim W and $\nu = \dim ( W \cap W ^ { \perp } ) \leq d .$ . If $\nu = 0$ we say that W is a symplectic subspace of V . This corresponds to the case that Ω restricts to W to define a symplectic structure on W . At the other extreme is when $\nu = d$ , for then we have $W \cap W ^ { \perp } = W$ . Such a subspace is called Lagrangian.

## Symplectic Manifolds.

We are now ready to return to the study of manifolds.

Definition 3: A symplectic structure on a smooth manifold M is a non-degenerate, closed 2-form $\Omega \in { \mathcal { A } } ^ { 2 } ( M )$ . The pair (M, Ω) is called a symplectic manifold. If Ω is a symplectic structure on M and Υ is a symplectic structure on N, then a smooth map φ: $M  N$ satisfying $\phi ^ { * } ( \Upsilon ) = \Omega$ is called a symplectic map. If, in addition, $\phi$ is a diffeomorphism, we say that φ is a symplectomorphism.

Before developing any of the theory, it is helpful to see a few examples.

Surfaces with Area Forms. If S is an orientable smooth surface, then there exists a volume form $\mu$ on S. By definition, $\mu$ is a non-degenerate closed 2-form on S and hence defines a symplectic structure on S.

Lagrangian Structures on T M. From Lecture 4, any non-degenerate Lagrangian $L \colon T M \to$ R defines the 2-form $d \omega _ { L }$ , which is a symplectic structure on T M .

A ‘Standard’ Structure on $\mathbb { R } ^ { 2 n }$ . Think of $\mathbb { R } ^ { 2 n }$ as a smooth manifold and let Ω be the 2-form with constant coefficients

$$
\Omega = { \textstyle { \frac { 1 } { 2 } } } { \mathit { ^ { t } d x } } J _ { n } d x = d x ^ { 1 } \wedge d x ^ { n + 1 } + \cdot \cdot \cdot + d x ^ { n } \wedge d x ^ { 2 n } .
$$

Symplectic Submanifolds. Let $( M ^ { 2 m } , \Omega )$ be a symplectic manifold. Suppose that $P ^ { 2 p } \subset \overline { { M ^ { 2 m } } }$ be any submanifold to which the form Ω pulls back to be a non-degenerate 2-form $\Omega _ { P }$ Then $( P , \Omega _ { P } )$ is a symplectic manifold. We say that P is a symplectic submanifold of M .

It is not obvious just how to find symplectic submanifolds of M. Even though being a symplectic submanifold is an ‘open’ condition on submanifolds of M, is is not ‘dense’. One cannot hope to perturb an arbitrary even dimensional submanifold of M slightly so as to make it symplectic. There are even restrictions on the topology of the submanifolds of M on which a symplectic form restricts to be non-degenerate.

For example, no symplectic submanifold of $\mathbb { R } ^ { 2 n }$ (with any symplectic structure on $\mathbb { R } ^ { 2 n } )$ could be compact for the following simple reason: Since $\mathring { \mathbb { R } } ^ { 2 n }$ is contractible, its second deRham cohomology group vanishes. In particular, for any symplectic form Ω on $\mathbb { R } ^ { 2 n }$ , there must be a 1-form ω so that $\Omega = d \omega$ , which implies that $\Omega ^ { m } = d \left( \omega \wedge \Omega ^ { m - 1 } \right)$ . Thus, for all $m > 0$ , the 2m-form $\Omega ^ { m }$ is exact on $\mathbb { R } ^ { 2 n }$ (and every submanifold of $\mathbb { R } ^ { 2 n } )$ .

By Proposition 2, if $M ^ { 2 m }$ were a submanifold of $\mathbb { R } ^ { 2 n }$ on which Ω restricted to be nondegenerate, then $\Omega ^ { m }$ would be a volume form on M. However, on a compact manifold the volume form is never exact (just apply Stokes’ Theorem).

Example. Complex Submanifolds. Nevertheless, there are many symplectic submanifolds of $\mathbb { R } ^ { 2 n }$ . One way to construct them is to regard $\mathbb { R } ^ { 2 n }$ as $\mathbb { C } ^ { n }$ in such a way that the linear map $J \colon \mathbb { R } ^ { 2 n } \ \stackrel { \cdot } { \to } \ \mathbb { R } ^ { 2 n }$ represented by $J _ { n }$ becomes complex multiplication. (For example, just define the complex coordinates by $z ^ { k } = x ^ { k } + i x ^ { k + n } . )$ Then, for any non-zero vector $v \in \mathbb { R } ^ { 2 n }$ , we have $\Omega ( v , J v ) = - | v | ^ { 2 } \neq 0$ . In particular, Ω is non-degenerate on every complex subspace $S \subset \mathbb { C } ^ { n }$ . Thus, if $M ^ { 2 m } \subset \mathbb { C } ^ { n }$ is any complex submanifold $( \mathrm { i . e . }$ , all of its tangent spaces are m-dimensional complex subspaces of $\mathbb { C } ^ { m } )$ , then Ω restricts to be non-degenerate on M.

The Cotangent Bundle. Let M be any smooth manifold and let $T ^ { * } M$ be its cotangent bundle. As we saw in Lecture 4, there is a canonical 2-form on $T ^ { * } M$ that can be defined as follows: Let $\pi \colon T ^ { * } M \to M$ be the basepoint projection. Then, for every $v \in T _ { \alpha } ( T ^ { * } M )$ , define

$$
\omega ( v ) = \alpha ( \pi ^ { \prime } ( v ) ) .
$$

I claim that ω is a smooth 1-form on $T ^ { * } M$ and that $\Omega = d \omega$ is a symplectic form on $T ^ { * } M$

To see this, let us compute ω in local coordinates. Let x: $U \to \mathbb { R } ^ { n }$ be a local coordinate chart. Since the 1-forms $d x ^ { 1 } , \ldots , d x ^ { n }$ are linearly independent at every point of $U .$ , it follows that there are unique functions $\xi _ { i }$ on $T ^ { * } U$ so that, for $\alpha \in T _ { a } ^ { * } U$ ,

$$
\alpha = \xi _ { 1 } ( \alpha ) d x ^ { 1 } | _ { a } + \cdot \cdot \cdot + \xi _ { n } ( \alpha ) d x ^ { n } | _ { a } .
$$

The functions $x ^ { 1 } , \ldots , x ^ { n } , \xi _ { 1 } , \ldots , \xi _ { n }$ then form a smooth coordinate system on $T ^ { * } U$ in which the projection mapping π is given by

$$
\pi ( x , p ) = x .
$$

It is then straightforward to compute that, in this coordinate system,

$$
\omega = \xi _ { i } d x ^ { i } .
$$

Hence, $\Omega = d \xi _ { i } \wedge d x ^ { i }$ and so is non-degenerate.

Symplectic Products. If $( M , \Omega )$ and $( N , \Upsilon )$ are symplectic manifolds, then $M \times N$ carries a natural symplectic structure, called the product symplectic structure $\Omega \oplus \Upsilon$ defined by

$$
\Omega \oplus \Upsilon = \pi _ { 1 } ^ { * } ( \Omega ) + \pi _ { 2 } ^ { * } ( \Upsilon ) .
$$

Thus, for example, n-fold products of compact surfaces endowed with area forms give examples of compact symplectic 2n-manifolds.

Coadjoint Orbits. Let $\operatorname { A d } ^ { * } { \boldsymbol { \cdot } } G \to \operatorname { G L } ( { \mathfrak { g } } ^ { * } )$ denote the coadjoint representation of $G .$ This is the so-called ‘contragredient’ representation to the adjoint representation. Thus, for any $a \in G$ and $\xi \in { \mathfrak { g } } ^ { * }$ , the element $\operatorname { A d } ^ { * } ( a ) ( \xi ) \in { \mathfrak { g } } ^ { * }$ is determined by the rule

$$
\operatorname { A d } ^ { * } ( a ) ( \xi ) ( x ) = \xi { \big ( } \operatorname { A d } ( a ^ { - 1 } ) ( x ) { \big ) } \qquad { \mathrm { f o r ~ a l l ~ } } x \in { \mathfrak { g } } .
$$

One must be careful not to confuse $A d ^ { * } ( a )$ with $\big ( \mathrm { A d } ( a ) \big ) ^ { * }$ . Instead, as our definition shows, $A d ^ { * } ( a ) = \left( \operatorname { A d } ( a ^ { - 1 } ) \right) ^ { * }$

Note that the induced homomorphism of Lie algebras, $\operatorname { a d } ^ { * } { \mathfrak { g } } \to { \mathfrak { g l } } ( { \mathfrak { g } } ^ { * } )$ is given by

$$
\operatorname { a d } ^ { * } ( x ) ( \xi ) ( y ) = - \xi { \bigl ( } [ x , y ] { \bigr ) }
$$

The orbits $G \cdot \xi$ in ${ \mathfrak { g } } ^ { * }$ are called the coadjoint orbits. Each of them carries a natural symplectic structure. To see how this is defined, let $\xi \in { \mathfrak { g } } ^ { * }$ be fixed, and let $\phi \colon G \to G \cdot \xi$ be the usual submersion induced by the $\mathrm { A d } ^ { * }$ -action, $\phi ( a ) = \mathrm { A d } ^ { * } ( a ) ( \xi ) = a \cdot \xi$ . Now let $\omega _ { \xi }$ be the left-invariant 1-form on $G$ whose value at e is $\xi$ . Thus, $\omega _ { \xi } = \xi ( \omega )$ where $\omega$ is the canonical g-valued 1-form on $G$

Proposition 3: There is a unique symplectic form $\Omega _ { \xi }$ on the orbit $G \cdot \xi = G / G _ { \xi }$ satisfying $\phi ^ { * } ( \Omega _ { \xi } ) = d \omega _ { \xi }$

Proof: If Proposition 3 is to be true, then $\Omega _ { \xi }$ must satisfy the rule

$$
\Omega _ { \xi } { \big ( } \phi ^ { \prime } ( v ) , \phi ^ { \prime } ( w ) { \big ) } = d \omega _ { \xi } ( v , w ) \quad { \mathrm { f o r ~ a l l ~ } } v , w \in T _ { a } G .
$$

What we must do is show that this rule actually does define a symplectic 2-form on $G \cdot \xi$

First, note that, for $x , y \in { \mathfrak { g } } = T _ { e } G$ , we may compute via the structure equations that

$$
d \omega _ { \xi } ( x , y ) = \xi \big ( d \omega ( x , y ) \big ) = \xi \big ( - [ x , y ] \big ) = a d ^ { * } ( x ) ( \xi ) ( y ) .
$$

In particular, $a d ^ { * } ( x ) ( \xi ) = 0$ , if and only if x lies in the null space of the 2-form $d \omega _ { \xi } ( e )$ . In other words, the null space of $d \omega _ { \xi } ( e )$ is ${ \mathfrak { g } } _ { \xi }$ , the Lie algebra of $G _ { \xi }$ . Since $d \omega _ { \xi }$ is left-invariant, it follows that the null space of $d \omega _ { \xi } ( a )$ is $L _ { a } ^ { \prime } ( { \mathfrak { g } } _ { \xi } ) \subset T _ { a } G$ Of course, this is precisely the tangent space at a to the left coset $a G _ { \xi }$ . Thus, for each $a \in G$ ,

$$
N _ { d \omega _ { \xi } ( a ) } = \ker \phi ^ { \prime } ( a ) ,
$$

It follows that, $T _ { a \cdot \xi } ( G \cdot \xi ) = \phi ^ { \prime } ( a ) ( T _ { a } G )$ is naturally isomorphic to the symplectic quotient space $( T _ { a } G ) / \left( L _ { a } ^ { \prime } ( \mathfrak { g } _ { \xi } ) \right)$ for each $a \in G$ . Thus, there is a unique, non-degenerate 2-form $\Omega _ { a }$ on $T _ { a \cdot \xi } ( G \cdot \xi )$ so that $\left( \phi ^ { \prime } ( a ) \right) ^ { * } ( \Omega _ { a } ) = d \omega _ { \xi } ( a )$ •

It remains to show that $\Omega _ { a } = \Omega _ { b } { \mathrm { ~ i f ~ } } a \cdot \xi = b \cdot \xi$ . However, this latter case occurs only if $a = b h$ where $h \in G _ { \xi }$ . Now, for any $h \in G _ { \xi }$ , we have

$$
\begin{array} { r } { R _ { h } ^ { * } ( \omega _ { \xi } ) = \xi \big ( R _ { h } ^ { * } ( \omega ) \big ) = \xi \big ( \mathrm { A d } ( h ^ { - 1 } ) ( \omega ) \big ) = \mathrm { A d } ^ { * } ( h ) ( \xi ) ( \omega ) = \xi ( \omega ) = \omega _ { \xi } . } \end{array}
$$

Thus, $R _ { h } ^ { * } ( d \omega _ { \xi } ) = d \omega _ { \xi }$ . Since the following square commutes, it follows that $\Omega _ { a } = \Omega _ { b }$

$$
\begin{array} { r c c c } { { T _ { a } G } } & { { \xrightarrow { R _ { h } ^ { \prime } } } } & { { T _ { b } G } } \\ { { } } & { { } } & { { } } \\ { { \phi ^ { \prime } ( a ) \bigg \downarrow } } & { { } } & { { \bigg \downarrow \phi ^ { \prime } ( b ) } } \\ { { } } & { { } } & { { } } \\ { { T _ { a \cdot \xi } \big ( G \cdot \xi \big ) } } & { { \xrightarrow { i d } } } & { { T _ { b \cdot \xi } \big ( G \cdot \xi \big ) } } \end{array}
$$

All this shows that there is a well-defined, non-degenerate 2-form $\Omega _ { \xi }$ on $G \cdot \xi$ that satisfies $\phi ^ { * } ( \Omega _ { \xi } ) = d \omega _ { \xi }$ . Since $\phi$ is a smooth submersion, the equation

$$
\phi ^ { * } ( d \Omega _ { \xi } ) = d ( d \omega _ { \xi } ) = 0
$$

implies that $d \Omega _ { \xi } = 0$ , as promised.

◮ Note that a consequence of Proposition 3 is that all of the coadjoint orbits are actually even dimensional. As we shall see when we take up the subject of reduction, the coadjoint orbits are particularly interesting symplectic manifolds.

Examples: Let $G = { \mathrm { O } } ( n )$ , with Lie algebra ${ \mathfrak { s o } } ( n )$ , the space of skew-symmetric $n { \mathrm { - } } \mathrm { b y } { \mathrm { - } } n$ matrices. Now there is an ${ \mathrm { O } } ( n )$ -equivariant positive definite pairing of ${ \mathfrak { s o } } ( n )$ with itself $\langle , \rangle$ given by

$$
\langle x , y \rangle = - \mathrm { t r } ( x y ) .
$$

Thus, we can identify so $( n ) ^ { * }$ with ${ \mathfrak { s o } } ( n )$ by this pairing. The reader can check that, in this case, the coadjoint action is isomorphic to the adjoint action

$$
\mathrm { A d } ( a ) ( x ) = a x a ^ { - 1 } .
$$

If $\xi$ is the rank 2 matrix

$$
\xi = \left( \begin{array} { c c c c } { { 0 } } & { { - 1 } } & { { } } & { { 0 } } \\ { { 1 } } & { { 0 } } & { { } } & { { } } \\ { { } } & { { 0 } } & { { } } & { { 0 } } \end{array} \right) ,
$$

then it is easy to check that the stabilizer $G _ { \xi }$ is just the set of matrices of the form

$$
\left( \begin{array} { c c } { { a } } & { { 0 } } \\ { { 0 } } & { { A } } \end{array} \right)
$$

where $a \in \mathrm { S O } ( 2 )$ and $A \in { \mathrm { O } } ( n - 2 )$ . The quotient ${ \mathrm { O } } ( n ) / ( { \mathrm { S O } } ( 2 ) \times { \mathrm { O } } ( n - 2 ) )$ thus has a symplectic structure. It is not difficult to see that this homogeneous space can be identified with the space of oriented 2-planes in $\mathbb { E } ^ { n }$

As another example, if $n = 2 m$ , then $J _ { m }$ lies in ${ \mathfrak { s o } } ( 2 m )$ , and its stabilizer is $\mathrm { U } ( m ) \subset$ $\mathrm { S O } ( 2 m )$ . It follows that the quotient space $\mathrm { S O } ( 2 m ) / \mathrm { U } ( m )$ , which is identifiable as the set of orthogonal complex structures on $\mathbb { E } ^ { \bar { 2 } m }$ , is a symplectic space.

Finally, if $G = \mathrm { U } ( n )$ , then, again, we can identify ${ \mathfrak { u } } ( n ) ^ { * }$ with $\mathfrak { u } ( n )$ via the $\mathrm { U } ( n )$ invariant, positive definite pairing

$$
\langle x , y \rangle = - \mathrm { R e } \big ( \mathrm { t r } ( x y ) \big ) .
$$

Again, under this identification, the coadjoint action agrees with the adjoint action. For $0 < p < n$ , the stabilizer of the element

$$
\xi _ { p } = \left( \begin{array} { c c } { { i I _ { p } } } & { { 0 } } \\ { { 0 } } & { { - i I _ { n - p } } } \end{array} \right)
$$

is easily seen to be $\mathrm { U } ( p ) \times \mathrm { U } ( n - p )$ . The orbit of $\xi _ { p }$ is identifiable with the space $\operatorname { G r } _ { p } ( \mathbb { C } ^ { n } )$ , i.e., the Grassmannian of (complex) p-planes in $\mathbb { C } ^ { n }$ , and, by Proposition 3, carries a canonical, U(n)-invariant symplectic structure.

Darboux’ Theorem. There is a manifold analogue of Proposition 1 that says that symplectic manifolds of a given dimension are all locally ‘isomorphic’. This fundamental result is known as Darboux’ Theorem. I will give the classical proof (due to Darboux) here, deferring the more modern proof (due to Weinstein) to the next section.

Theorem 1: (Darboux’ Theorem) If Ω is a closed 2-form on a manifold $M ^ { 2 n }$ that satisfies the condition that $\Omega ^ { n }$ be nowhere vanishing, then for every $p \in M$ , there is a neighborhood U of $\dot { \mathbf { \rho } } _ { p }$ and a coordinate system $x _ { 1 } , x _ { 2 } , \ldots , x _ { n } , y ^ { 1 } , y ^ { 2 } , \ldots , y ^ { n }$ on U so that

$$
\Omega _ { | _ { U } } = d x _ { 1 } \wedge d y ^ { 1 } + d x _ { 2 } \wedge d y ^ { 2 } + \cdot \cdot \cdot + d x _ { n } \wedge d y ^ { n } .
$$

Proof: We will proceed by induction on n. Assume that we know the theorem for $n { - } 1 \geq 0$ . We will prove it for n. Fix $p ,$ and let $y ^ { 1 }$ be a smooth function on M for which $d y ^ { 1 }$ does not vanish at $p .$ . Now let X be the unique (smooth) vector field that satisfies

$$
X \lrcorner \Omega = d y ^ { 1 } .
$$

This vector field does not vanish at $p ,$ so there is a function $x _ { 1 }$ on a neighborhood U of $p$ that satisfies $X ( x _ { 1 } ) = 1$ . Now let Y be the vector field on U that satisfies

$$
Y \lrcorner \Omega = - d x _ { 1 } .
$$

Since $d \Omega = 0$ , the Cartan formula, now gives

$$
\mathfrak { L } _ { X } \Omega = \mathfrak { L } _ { Y } \Omega = 0 .
$$

We now compute

$$
\begin{array} { r l } & { [ X , Y ] \lrcorner \Omega = \mathfrak { L } _ { X } Y \lrcorner \Omega = \mathfrak { L } _ { X } ( Y \lrcorner \Omega ) - Y \lrcorner ( \mathfrak { L } _ { X } \Omega ) } \\ & { \qquad = \mathfrak { L } _ { X } ( - d x _ { 1 } ) = - d \left( X ( x ^ { 1 } ) \right) = - d ( 1 ) = 0 \mathrm { . } } \end{array}
$$

Since Ω has maximal rank, this implies $[ X , Y ] = 0$ . By the simultaneous flow-box theorem, it follows that there exist local coordinates $\dot { x _ { 1 } } , y ^ { 1 } , z ^ { 1 } , z ^ { 2 } , \dots , z ^ { 2 n - 2 }$ on some neighborhood $U _ { 1 } \subset U$ of p so that

$$
X = { \frac { \partial } { \partial x _ { 1 } } } \quad \quad { \mathrm { a n d } } \quad \quad Y = { \frac { \partial } { \partial y ^ { 1 } } } .
$$

Now consider the form $\Omega ^ { \prime } = \Omega - d x _ { 1 } { \wedge } d y ^ { 1 }$ . Clearly $d \Omega ^ { \prime } = 0$ . Moreover,

$$
X \lrcorner \Omega ^ { \prime } = \mathfrak { L } _ { X } \Omega ^ { \prime } = Y \lrcorner \Omega ^ { \prime } = \mathfrak { L } _ { Y } \Omega ^ { \prime } = 0 .
$$

It follows that $\Omega ^ { \prime }$ can be expressed as a 2-form in the variables $z ^ { 1 } , z ^ { 2 } , \dots , z ^ { 2 n - 2 }$ alone. Hence, in particular, $( \Omega ^ { \prime } ) ^ { n } \equiv 0$ . On the other hand, by the binomial theorem, then

$$
0 \neq \Omega ^ { n } = n d x _ { 1 } \wedge d y ^ { 1 } \wedge ( \Omega ^ { \prime } ) ^ { n - 1 } .
$$

It follows that $\Omega ^ { \prime }$ may be regarded as a closed 2-form of maximal half-rank $n { - } 1$ on an open set in $\mathbb { R } ^ { 2 n - 2 }$ . Now apply the inductive hypothesis to $\Omega ^ { \prime }$ . 

Darboux’ Theorem has a generalization that covers the case of closed 2-forms of constant (though not necessarily maximal) rank. It is the analogue for manifolds of the symplectic reduction of a vector space.

Theorem 2: (Darboux’ Reduction Theorem) Suppose that Ω is a closed 2-form of constant half-rank n on a manifold $M ^ { 2 n + k }$ . Then the ‘null bundle’

$$
N _ { \Omega } = \left\{ v \in T M | \Omega ( v , w ) = 0 \ f o r \ a l l \ w \in T _ { \pi ( v ) } M \right\}
$$

is integrable and of constant rank k. Moreover, any point of M has a neighborhood U on which there exist local coordinates $x _ { 1 } , \dotsc , x _ { n } , y ^ { 1 } , \dotsc , y ^ { n } , z ^ { 1 } , \dotsc z ^ { k }$ in which

$$
\Omega _ { | _ { U } } = d x _ { 1 } \wedge d y ^ { 1 } + d x _ { 2 } \wedge d y ^ { 2 } + \cdot \cdot \cdot + d x _ { n } \wedge d y ^ { n } .
$$

Proof: Note that a vector field X on M is a section of $N _ { \Omega }$ if and only if $X \ J \Omega = 0$ . In particular, since Ω is closed, the Cartan formula implies that $\mathfrak { L } _ { X } \Omega = 0$ for all such X.

If X and $Y$ are two sections of $N _ { \Omega }$ , then

$$
[ X , Y ] \lrcorner \Omega = \mathfrak { L } _ { X } ( Y \lrcorner \Omega ) - Y ( \mathfrak { L } _ { X } \Omega ) = 0 - 0 = 0 ,
$$

so it follows that [X, Y ] is a section of $N _ { \Omega }$ as well. Thus, $N _ { \Omega }$ is integrable.

Now apply the Frobenius Theorem. For any point $p \in M$ , there exists a neighborhood U on which there exist local coordinates $z ^ { 1 } \ldots , { \overset { \cdot } { z ^ { 2 n + k } } }$ so that $N _ { \Omega }$ restricted to U is spanned by the vector fields $Z _ { i } = \partial / \partial z ^ { i }$ for $1 \leq i \leq k$ Since $Z _ { i } \lrcorner \Omega = \mathfrak { L } _ { Z _ { i } } \Omega = 0$ for $1 \leq i \leq k$ , it follows that Ω can be expressed on $U$ in terms of the variables $z ^ { k + 1 } , \dots , z ^ { 2 n + k }$ alone. In particular, Ω restricted to U may be regarded as a non-degenerate closed 2-form on an open set in $\mathbb { R } ^ { 2 n }$ . The stated result now follows from Darboux’ Theorem. 

## Symplectic and Hamiltonian vector fields.

We now want to examine some of the special vector fields that are defined on symplectic manifolds. Let $M ^ { 2 n }$ be manifold and let Ω be a symplectic form on M. Let $\mathsf { S p } ( \Omega ) \subset \mathsf { D i f f } ( M )$ denote the subgroup of symplectomorphisms of $( M , \Omega )$ . We would like to follow Lie in regarding $\mathsf { S p } ( \Omega )$ as an ‘infinite dimensional Lie group’. In that case, the Lie algebra of $\mathsf { S p } ( \Omega )$ should be the space of vector fields whose flows preserve Ω. Of course, Ω will be invariant under the flow of a vector field X if and only if $\mathfrak { L } _ { X } \Omega = 0$ . This motivates the following definition:

Definition 4: A vector field X on M is said to be symplectic if $\mathfrak { L } _ { X } \Omega = 0$ . The space of symplectic vector fields on M will be denoted $\mathfrak { s p } ( \Omega )$

It turns out that there is a very simple characterization of the symplectic vector fields on M: Since $d \Omega = 0$ , it follows that for any vector field X on M,

$$
{ \mathfrak { L } } _ { X } \Omega = d ( X \lrcorner \Omega ) .
$$

Thus, X is a symplectic vector field if and only if $X \lrcorner \Omega$ is closed.

Now, since Ω is non-degenerate, for any vector field X on M, the 1-form $\flat ( X ) = - X \lrcorner \Omega$ vanishes only where X does. Since T M and $T ^ { * } M$ have the same rank, it follows that the mapping $\flat \colon { \mathfrak { X } } ( M ) \to A ^ { 1 } ( M )$ is an isomorphism of $C ^ { \infty } ( M )$ -modules. In particular, ♭ has an inverse, $\sharp \colon { \mathcal { A } } ^ { 1 } ( M ) \to { \mathfrak { X } } ( M )$

With this notation, we can write sp $( \Omega ) = \sharp \big ( \mathcal Z ^ { 1 } ( M ) \big )$ where $\mathcal { Z } ^ { 1 } ( M )$ denotes the vector space of closed 1-forms on M. Now, $\mathcal { Z } ^ { 1 } ( M )$ contains, as a subspace, $B ^ { 1 } ( M ) = d \bigl ( C ^ { \infty } ( M ) \bigr )$ , the space of exact 1-forms on M . This subspace is of particular interest; we encountered it already in Lecture 4.

Definition 5: For each $f \in C ^ { \infty } ( M )$ , the vector field $X _ { f } = { \sharp ( d f ) }$ is called the Hamiltonian vector field associated to f. The set of all Hamiltonian vector fields on M is denoted h(Ω).

Thus, by definition, $\mathsf { h } ( \Omega ) = \sharp \big ( B ^ { 1 } ( M ) \big )$ . For this reason, Hamiltonian vector fields are often called exact. Note that a Hamiltonian vector field is one whose equations, written in symplectic coordinates, represent an ODE in Hamiltonian form.

The following formula shows that, not only is sp(Ω) a Lie algebra of vector fields, but that h(Ω) is an ideal in $\mathsf { s p } ( \Omega )$ , i.e., that $[ s p ( \Omega ) , s p ( \Omega ) ] \subset \mathtt { h } ( \Omega )$

Proposition 4: For $X , Y \in { \mathfrak { s p } } ( \Omega )$ , we have

$$
[ X , Y ] = X _ { \Omega ( X , Y ) } .
$$

In particular, $[ X _ { f } , X _ { g } ] = X _ { \{ f , g \} }$ where, by definition, $\{ f , g \} = \Omega ( X _ { f } , X _ { g } )$

Proof: We use the fact that, for any vector field X, the operator ${ \mathfrak { L } } _ { X }$ is a derivation with respect to any natural pairing between tensors on M:

$$
\begin{array} { r l } & { [ X , Y ] \lrcorner \Omega = \left( \mathfrak { L } _ { X } Y \right) \lrcorner \Omega = \mathfrak { L } _ { X } \left( Y \lrcorner \Omega \right) - Y \lrcorner \left( \mathfrak { L } _ { X } \Omega \right) } \\ & { \qquad = d \left( X \lrcorner \left( Y - \Omega \right) \right) + X \lrcorner d \left( Y \lrcorner \Omega \right) + 0 = d \left( \Omega ( Y , X ) \right) + 0 } \\ & { \qquad = - d \big ( \Omega ( X , Y ) \big ) = \left( X _ { \Omega ( X , Y ) } \right) \lrcorner \Omega . } \end{array}
$$

This proves our first equation. The remaining equation follows immediately.

The definition $\{ f , g \} = \Omega ( X _ { f } , X _ { g } )$ is an important one. The bracket $( f , g ) \mapsto \{ f , g \}$ is called the Poisson bracket of the functions $f$ and g. Proposition 4 implies that the Poisson bracket gives the functions on M the structure of a Lie algebra. The Poisson bracket is slightly more subtle than the pairing $( X _ { f } , X _ { g } ) \mapsto X _ { \{ f , g \} }$ since the mapping $f \mapsto X _ { f }$ has a non-trivial kernel, namely, the locally constant functions.

Thus, if M is connected, then we get an exact sequence of Lie algebras

$$
0 \longrightarrow \mathbb { R } \longrightarrow C ^ { \infty } ( M ) \longrightarrow \mathfrak { h } ( \Omega ) \longrightarrow 0
$$

that is not, in general, split (see the Exercises). Since $\{ 1 , f \} = 0$ for all functions $f$ on M, it follows that the Poisson bracket on $C ^ { \infty } ( M )$ makes it into a central extension of the algebra of Hamiltonian vector fields. The geometry of this central extension plays an important role in quantization theories on symplectic manifolds (see [GS 2] or [We]).

Also of great interest is the exact sequence

$$
0 \longrightarrow { \sf h } ( \Omega ) \longrightarrow s \mathsf { s p } ( \Omega ) \longrightarrow H _ { d R } ^ { 1 } ( M , \mathbb { R } ) \longrightarrow 0 ,
$$

where the right hand arrow is just the map described by $X \mapsto [ X \lrcorner \Omega ]$ . Since the bracket of two elements in sp(Ω) lies in h(Ω), it follows that this linear map is actually a Lie algebra homomorphism when $H _ { d R } ^ { 1 } ( M , \mathbb { R } )$ is given the abelian Lie algebra structure. This sequence also may or may not split (see the Exercises), and the properties of this extension have a great deal to do with the study of groups of symplectomorphisms of M. See the Exercises for further developments.

## Involution

I now want to make some remarks about the meaning of the Poisson bracket and its applications.

Definition 5: Let $( M , \Omega )$ be a symplectic manifold. Two functions f and g are said to be in involution (with respect to Ω) if they satisfy the condition $\{ f , g \} = 0$ .

Note that, since $\{ f , g \} = d g ( X _ { f } ) = - d f ( X _ { g } )$ , it follows that two functions f and g are in involution if and only if each is constant on the integral curves of the other’s Hamiltonian vector field.

Now, if one is trying to describe the integral curves of a Hamiltonian vector field, $X _ { f }$ the more independent functions on M that one can find that are constant on the integral curves of $X _ { f } ,$ , the more accurately one can describe those integral curves. If one were able find, in addition to $f$ itself, 2n 2 additional independent functions on M that are constant on the integral curves of $X _ { f }$ , then one could describe the integral curves of $X _ { f }$ implicitly by setting those functions equal to a constant.

It turns out, however, that this is too much to hope for in general. It can happen that a Hamiltonian vector field $X _ { f }$ has no functions in involution with it except for functions of the form $F ( f )$ .

Nevertheless, in many cases that arise in practice, we can find several functions in involution with a given function $f = f _ { 1 }$ and, moreover, in involution with each other. In case one can find $n { - } 1$ such independent functions, $f _ { 2 } , \ldots , f _ { n }$ , we have the following theorem of Liouville, which says that the remaining $n { - } 1$ required functions can be found (at least locally) by quadrature alone. In the classical language, a vector field $X _ { f }$ for which such functions are known is said to be ‘completely integrable by quadratures’, or, more simply as ‘completely integrable’.

Theorem 3: Let $f ^ { 1 } , f ^ { 2 } , \ldots , f ^ { n }$ be n functions in involution on a symplectic manifold $( M ^ { 2 n } , \Omega )$ . Suppose that the functions $f ^ { i }$ are independent in the sense that the differentials $d f ^ { 1 } , \ldots , d f ^ { n }$ are linearly independent at every point of M. Then each point of M has an open neighborhood $U$ on which there are functions $a _ { 1 } , \ldots , a _ { n }$ on $U$ so that

$$
\Omega = d f ^ { 1 } \wedge d a _ { 1 } + \cdot \cdot \cdot + d f ^ { n } \wedge d a _ { n } .
$$

Moreover, the functions $a _ { i }$ can be found by ‘finite’ operations and quadrature.

Proof: By hypothesis, the forms $d f ^ { 1 } , \ldots , d f ^ { n }$ are linearly independent at every point of $M .$ , so it follows that the Hamiltonian vector fields $X _ { f ^ { 1 } } , \dotsc , X _ { f ^ { n } }$ are also linearly independent at every point of $M$ . Also by hypothesis, the functions $f ^ { i }$ are in involution, so it follows that $d f ^ { i } ( X _ { f ^ { j } } ) = 0$ for all i and $j$ .

The vector fields $X _ { f ^ { i } }$ are linearly independent on $M$ , so by ‘finite’ operations, we can construct 1-forms $\bar { \beta } _ { 1 } , \ldots , \bar { \beta } _ { n }$ that satisfy the conditions

$$
\bar { \beta } _ { i } ( X _ { { f ^ { j } } } ) = \delta _ { i j } \qquad \mathrm { ( K r o n e c k e r ~ d e l t a ) . }
$$

Any other set of forms $\beta _ { i }$ that satisfy these conditions are given by expressions:

$$
\beta _ { i } = \bar { \beta } _ { i } + g _ { i j } d f ^ { j }
$$

for some functions $g _ { i j }$ on $M$ . Let us regard the functions $g _ { i j }$ as unknowns for a moment. Let $Y _ { 1 } , \dots , Y _ { n }$ be the vector fields that satisfy

$$
Y _ { i } \lrcorner \Omega = \beta _ { i } ,
$$

with ${ \bar { Y } } _ { i }$ denoting the corresponding quantities when the $g _ { i j }$ are set to zero. Then it is easy to see that

$$
Y _ { i } = \bar { Y } _ { i } - g _ { i j } X _ { f ^ { j } } .
$$

Now, by construction,

$$
\Omega ( X _ { f ^ { i } } , X _ { f ^ { j } } ) = 0 \qquad \mathrm { a n d } \qquad \Omega ( Y _ { i } , X _ { f ^ { j } } ) = \delta _ { i j } .
$$

Moreover, as is easy to compute,

$$
\Omega ( Y _ { i } , Y _ { j } ) = \Omega ( \bar { Y } _ { i } , \bar { Y } _ { j } ) - g _ { j i } + g _ { i j } .
$$

Thus, choosing the functions $g _ { i j }$ appropriately, say $\begin{array} { r } { g _ { i j } = - \frac { 1 } { 2 } \Omega ( \bar { Y } _ { i } , \bar { Y } _ { j } ) } \end{array}$ , we may assume that $\Omega ( Y _ { i } , Y _ { j } ) = 0$ . It follows that the sequence of 1-forms $d f ^ { 1 ^ { - } } , \dotsc , d f ^ { n } , \beta _ { 1 } , \dotsc , \beta _ { n }$ is the dual basis to the sequence of vector fields $Y _ { 1 } , \dots , Y _ { n } , X _ { f ^ { 1 } } , \dots , X _ { f ^ { n } }$ . In particular, we see that

$$
\Omega = d f ^ { 1 } \wedge \beta _ { 1 } + \cdot \cdot \cdot + d f ^ { n } \wedge \beta _ { n } ,
$$

since the 2-forms on either side of this equation have the same values on all pairs of vector fields drawn from this basis.

Now, since Ω is closed, we have

$$
d \Omega = d f ^ { 1 } \wedge d \beta _ { 1 } + \cdot \cdot \cdot + d f ^ { n } \wedge d \beta _ { n } = 0 .
$$

If, for example, we wedge both sides of this equation with $d f ^ { 2 } , \ldots , d f ^ { n }$ , we see that

$$
d f ^ { 1 } \wedge d f ^ { 2 } \wedge \dots \wedge d f ^ { n } \wedge d \beta _ { 1 } = 0 .
$$

Hence, it follows that $d \beta _ { 1 }$ lies in the ideal generated by the forms $d f ^ { 1 } , \ldots , d f ^ { n }$ . Of course, there was nothing special about the first term, so we clearly have

$$
d \beta _ { i } \equiv 0 { \mathrm { ~ m o d ~ } } d f ^ { 1 } , \ldots , d f ^ { n } \qquad { \mathrm { f o r ~ a l l ~ } } 1 \leq i \leq n .
$$

In particular, it follows that, if we pull back the 1-forms $\beta _ { i }$ to any n-dimensional level set $M _ { c } \subset M$ defined by equations $f ^ { i } = c ^ { i }$ where the $c ^ { i }$ are constants, then each $\beta _ { i }$ becomes closed.

Let $m \in M$ be fixed and choose functions $g _ { 1 } , \ldots , g _ { n }$ on a neighborhood U of m in M so that $g _ { i } ( m ) = 0$ and so that the functions $g _ { 1 } , . . . , g _ { n } , f ^ { 1 } , . . . , f ^ { n }$ form a coordinate chart on U. By shrinking U if necessary, we may assume that the image of this coordinate chart in $\mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ is an open set of the form $B _ { 1 } \times B _ { 2 }$ , where $B _ { 1 }$ and $B _ { 2 }$ are open balls in $\mathbb { R } ^ { n }$ (with $B _ { 1 }$ centered on 0). In this coordinate chart, the $\beta _ { i }$ can be expressed in the form

$$
\beta _ { i } = B _ { i } ^ { j } ( g , f ) d g _ { j } + C _ { i j } ( g , f ) d f ^ { j } .
$$

Define new functions $a _ { i }$ on $B ^ { 1 } \times B ^ { 2 }$ by the rule

$$
h _ { i } ( g , f ) = \int _ { 0 } ^ { 1 } B _ { i } ^ { j } ( t g , f ) g _ { j } d t .
$$

(This is just the Poincar´e homotopy formula with the f’s held fixed. It is also the first place where we use ‘quadrature’.) Since setting the $f \mathrm { ^ { \prime } s }$ equals to constants makes $\beta _ { i }$ a closed 1-form, it follows easily that

$$
\beta _ { i } = d h _ { i } + A _ { i j } ( g , f ) d f ^ { j }
$$

for some functions $A _ { i j }$ on $B ^ { 1 } \times B ^ { 2 }$ . Thus, on U, the form Ω has the expression

$$
\Omega = d f ^ { i } \wedge d h _ { i } + A _ { i j } d f ^ { i } \wedge d f ^ { j } .
$$

It follows that the 2-form $A = A _ { i j } d f ^ { i } { \wedge } d f ^ { j }$ is closed on (the contractible open set) $B ^ { 1 } \times B ^ { 2 }$ Thus, the functions $A _ { i j }$ do not depend on the g-coordinates at all. Hence, by employing quadrature once more (i.e., the second time) in the Poincar´e homotopy formula, we can write $A = - d ( s _ { i } d f ^ { i } )$ for some functions $s _ { i }$ of the $f \mathrm { ^ { \prime } s }$ alone. Setting $a _ { i } = h _ { i } + s _ { i }$ , we have the desired local normal form $\Omega = d f ^ { i } { \wedge } d a _ { i }$ 

In many useful situations, one does not need to restrict to a local neighborhood U to define the functions $a _ { i }$ (at least up to additive constants) and the 1-forms $d a _ { i }$ can be defined globally on M (or, at least away from some small subset in M where degeneracies occur). In this case, the construction above is often called the construction of ‘action-angle’ coordinates. We will discuss this further in Lecture 6.

# Exercise Set 5:

# Symplectic Manifolds, I

1. Show that the bilinear form on $\mathbb { R } ^ { n }$ defined in the text by the rule $B ( x , y ) = ^ { t } x A y$ (where A is a skew-symmetric n-by-n matrix) is non-degenerate if and only if A is invertible. Show directly (i.e., without using Proposition 1) that a skew-symmetric, n-by-n matrix A cannot be invertible if n is odd. (Hint: For the last part, compute det(A) two ways.)

2. Let $( V , B )$ be a symplectic space and let $\mathbf { b } = \left( b _ { 1 } , b _ { 2 } , \ldots , b _ { m } \right)$ be a basis of B. Define the $m { \mathrm { - } } \mathrm { b y } { \mathrm { - } } m$ skew-symmetric matrix $A _ { \mathbf { b } }$ whose ij-entry is $B ( b _ { i } , b _ { j } )$ . Show that if $\mathbf { b } ^ { \prime } = \mathbf { b } R$ is any other basis of V (where $R \in \mathrm { G L } ( m , \mathbb { R } ) \ )$ , then

$$
A _ { \mathbf { b } ^ { \prime } } = { } ^ { t } R A _ { \mathbf { b } } R .
$$

Use Proposition 1 and Exercise 1 to conclude that, if A is an invertible, skew-symmetric 2n-by-2n matrix, then there exists a matrix $R \in \operatorname { G L } ( 2 n , \mathbb { R } )$ so that

$$
A = ^ { t } R \left( \begin{array} { c c } { { 0 _ { n } } } & { { I _ { n } } } \\ { { - I _ { n } } } & { { 0 _ { n } } } \end{array} \right) R .
$$

In other words, the GL(2n, R)-orbit of the matrix $J _ { n }$ defined in the text (under the “standard” (right) action of $\operatorname { G L } ( 2 n , \mathbb { R } )$ on the skew-symmetric 2n-by-2n matrices) is the open set of all invertible skew-symmetric 2n-by-2n matrices.

3. Show that $\operatorname { S p } ( n , \mathbb { R } )$ , as defined in the text, is indeed a Lie subgroup of $\operatorname { G L } ( 2 n , \mathbb { R } )$ and has dimension $2 n ^ { 2 } + n$ . Compute its Lie algebra ${ \mathfrak { s p } } ( n , \mathbb { R } )$ . Show that $\mathrm { S p } ( 1 , \mathbb { R } ) = \mathrm { S L } ( 2 , \mathbb { R } )$

4. In Lecture 2, we defined the groups ${ \mathrm { G L } } ( n , \mathbb { C } ) = \{ R \in { \mathrm { G L } } ( 2 n , \mathbb { R } ) \mid J _ { n } R = R J _ { n } \}$ and $\mathrm { O } ( 2 n ) = \{ R \in \mathrm { G L } ( 2 n , \mathbb { R } ) \ | ^ { \ t } R R = I _ { 2 n } \}$ . Show that

$$
\mathrm { G L } ( n , \mathbb { C } ) \cap \mathrm { S p } ( n , \mathbb { R } ) = \mathrm { O } ( 2 n ) \cap \mathrm { S p } ( n , \mathbb { R } ) = \mathrm { G L } ( n , \mathbb { C } ) \cap \mathrm { O } ( 2 n ) = \mathrm { U } ( n ) .
$$

5. Let Ω be a symplectic form on a vector space V of dimension 2n. Let $W \subset V$ be a subspace that satisfies dim $W = d$ and dim $( W \cap W ^ { \perp } ) = \nu$ . Show that there exists an Ω-standard basis of V so that W is spanned by the vectors

$$
e _ { 1 } , \ . \ . . , \ e _ { \nu + m } , \ f _ { 1 } , \ . \ . . , \ f _ { m }
$$

where $d - \nu = 2 m$ . In this basis of V , what is a basis for $W ^ { \perp } ?$

6. The Pfaffian. Let V be a vector space of dimension 2n. Fix a basis $\mathbf { b } = ( b _ { 1 } , \dots , b _ { 2 n } )$ For any skew-symmetric 2n-by-2n matrix $F = \left( f ^ { i j } \right)$ , define the 2-vector

$$
\Phi _ { F } = { \textstyle { \frac { 1 } { 2 } } } f ^ { i j } b _ { i } \wedge b _ { j } = { \textstyle { \frac { 1 } { 2 } } } { \bf b } \wedge F \wedge { } ^ { t } { \bf b } .
$$

Then there is a unique polynomial function Pf, homogeneous of degree n, on the space of skew-symmetric 2n-by-2n matrices for which

$$
( \Phi _ { F } ) ^ { n } = n ! \operatorname { P f } ( F ) b _ { 1 } \wedge . . . \wedge b _ { 2 n } .
$$

Show that

$$
{ \begin{array} { r l r } & { \operatorname* { P f } ( F ) = f ^ { 1 2 } \qquad } & { \mathrm { w h e n ~ } n = 1 , } \\ & { \operatorname* { P f } ( F ) = f ^ { 1 2 } f ^ { 3 4 } + f ^ { 1 3 } f ^ { 4 2 } + f ^ { 1 4 } f ^ { 2 3 } \qquad } & { \mathrm { w h e n ~ } n = 2 . } \end{array} }
$$

Show also that

$$
\mathrm { P f } ( A F ^ { t } A ) = \operatorname* { d e t } ( A ) \mathrm { P f } ( F )
$$

for all $A \in \operatorname { G L } ( 2 n , \mathbb { R } )$ (Hint: Examine the effect of a change of basis b = b′A. Compare Problem 2.) Use this to conclude that $\operatorname { S p } ( n , \mathbb { R } )$ is a subgroup of SL(2n, R). Finally, show that $\left( \mathrm { P f } \left( F \right) \right) ^ { 2 } = \operatorname* { d e t } ( F )$ . (Hint: Show that the left and right hand sides are polynomial functions that agree on a certain open set in the space of skew-symmetric 2n-by-2n matrices.)

The polynomial function Pf is called the Pfaffian. It plays an important role in differential geometry.

7. Verify that, for any $B \in A ^ { 2 } ( V )$ , the symplectic reduction $( \overline { { V } } , \overline { { B } } )$ is a well-defined symplectic space.

8. Show that if there is a G-invariant non-degnerate pairing $( , \ ) \colon { \mathfrak { g } } \times { \mathfrak { g } } \to { \mathbb { R } }$ , then g and ${ \mathfrak { g } } ^ { * }$ are isomorphic as G-representations.

9. Compute the adjoint and coadjoint representations for

$$
G = \left\{ { \left( \begin{array} { l l } { a } & { b } \\ { 0 } & { 1 } \end{array} \right) } { \bigg | } a \in \mathbb { R } ^ { + } , b \in \mathbb { R } \right\}
$$

Show that g and ${ \mathfrak { g } } ^ { * }$ are not isomorphic as G-spaces! (For a general $G ,$ the Ad-orbits of G in g are not even of even dimension in general, so they can’t be symplectic manifolds.)

10. For any Lie group G and any $\xi \in { \mathfrak { g } } ^ { * }$ , show that the symplectic structures $\Omega _ { \xi }$ and $\Omega _ { a \cdot \xi }$ on $G \cdot \xi$ are the same for any $a \in G$

11. This exercise concerns the splitting properties of the two Lie algebras sequences associated to any symplectic structure Ω on a connected manifold M:

$$
0 \longrightarrow \mathbb { R } \longrightarrow C ^ { \infty } ( M ) \longrightarrow \mathfrak { h } ( \Omega ) \longrightarrow 0
$$

and

$$
0 \longrightarrow { \sf h } ( \Omega ) \longrightarrow s { \sf p } ( \Omega ) \longrightarrow H _ { d R } ^ { 1 } ( M , \mathbb { R } ) \longrightarrow 0 .
$$

Define the “divided powers” of Ω by the rule $\Omega ^ { [ k ] } = ( 1 / k ! ) \Omega ^ { k }$ , for each $0 \leq k \leq n$

(i) Show that, for any vector fields X and Y on M,

$$
\Omega ( X , Y ) \Omega ^ { [ n ] } = - ( X \lrcorner \Omega ) \wedge ( Y \lrcorner \Omega ) \wedge \Omega ^ { [ n - 1 ] } .
$$

Conclude that the first of the above two sequences splits if M is compact. (Hint: For the latter statement, show that the set of functions $f$ on M for which $\begin{array} { r } { \int _ { M } \dot { f } \ d \Omega ^ { [ n ] } = 0 } \end{array}$ forms a Poisson subalgebra of $C ^ { \infty } ( M ) . )$

(ii) On the other hand, show that for $\mathbb { R } ^ { 2 }$ with the symplectic structure $\Omega = d x { \wedge } d y$ , the first sequence does not split. (Hint: Show that every smooth function on $\mathbb { R } ^ { 2 }$ is of the form $\{ x , g \}$ for some $g \in C ^ { \infty } ( \dot { \mathbb { R } } ^ { 2 } )$ . Why does this help?)

(iii) Suppose that M is compact. Define a skew-symmetric pairing

$$
\beta _ { \Omega } \colon H _ { d R } ^ { 1 } ( M , \mathbb { R } ) \times H _ { d R } ^ { 1 } ( M , \mathbb { R } ) \to \mathbb { R }
$$

by the formula

$$
\beta _ { \Omega } ( a , b ) = \int _ { \cal M } \tilde { a } \wedge \tilde { b } \wedge \Omega ^ { [ n - 1 ] } ,
$$

where $\tilde { a }$ and $\tilde { b }$ are closed 1-forms representing the cohomology classes a and b respectively. Show that if there is a Lie algebra splitting $\sigma \colon H _ { d R } ^ { 1 } ( M , \mathbb { R } ) \to s \mathfrak { p } ( \Omega )$ then

$$
\Omega \big ( \sigma ( a ) , \sigma ( b ) \big ) = - \frac { \beta _ { \Omega } ( a , b ) } { v o l ( M , \Omega ^ { [ n ] } ) }
$$

for all $a , b \in H _ { d R } ^ { 1 } ( M , \mathbb { R } )$ . (Remember that the Lie algebra structure on $H _ { d R } ^ { 1 } ( M , \mathbb { R } )$ is the abelian one.) Use this to conclude that the second sequence does split for a symplectic structure on the standard 1-holed torus, but does not split for any symplectic structure on the 2-holed torus. (Hint: To show the non-splitting result, use the fact that any tangent vector field on the 2-holed torus must have a zero.)

12. The Flux Homomorphism. The object of this exercise is to try to identify the subgroup of $\mathsf { S p } ( \Omega )$ whose Lie algebra is $\mathbf { h } ( \Omega )$ . Thus, let $( M , \Omega )$ be a symplectic manifold.

First, I remind you how the construction of the (smooth) universal cover of the identity component of $\mathsf { S p } ( \Omega )$ goes. Let $p \colon [ 0 , 1 ] \times M \to M$ be a smooth map with the property that the map $p _ { t } \colon M \to M$ defined by $p _ { t } ( m ) = p ( t , m )$ is a symplectomorphism for all $0 \leq t \leq 1$ Such a $p$ is called a (smooth) path in $S { \mathfrak { p } } ( M )$ . We say that $p$ is based at the identity map e: $M  M { \mathrm { i f } } p _ { 0 } = e $ . The set of smooth paths in $\mathsf { S p } ( M )$ that are based at e will be denoted by ${ \sf P } _ { \boldsymbol { e } } \big ( { \sf S p } ( \Omega ) \big )$ .

Two paths p and $p ^ { \prime }$ in $\mathsf P e \left( \mathsf { S p } ( \Omega ) \right)$ satisfying $p _ { 1 } = p _ { 1 } ^ { \prime }$ are said to be homotopic if there is a smooth map $P \colon [ 0 , 1 ] \times [ 0 , \dot { 1 } ] \times \dot { M }  M$ that satisfies the following conditions: First, $P ( s , 0 , m ) = m$ for all s and m. Second, $P ( s , 1 , m ) = p _ { 1 } ( m ) = p _ { 1 } ^ { \prime } ( m )$ for all s and $m$ Third, $P ( 0 , t , m ) = p ( t , m )$ and $P ( 1 , t , m ) = p ^ { \prime } ( t , m )$ for all t and $m .$ . The set of homotopy classes of elements of $\mathsf P e \left( \mathsf { S p } ( \Omega ) \right)$ is then denoted by $\widetilde { \mathsf { S p } } ^ { 0 } ( \Omega )$ . In any reasonable topology on $\mathsf { S p } ( \Omega )$ , this should to be the universal covering space of the identity component of $\mathsf { S p } ( \Omega )$ There is a natural group structure on $\widetilde { \mathsf { S p } } ^ { 0 } ( \Omega )$ in which ${ \tilde { e } } ,$ the homotopy class of the constant path at e, is the identity element (cf., the covering spaces exercise in Exercise Set 2).

We are now going to construct a homomorphism $\Phi { : \widetilde { { \mathsf { S p } } } ^ { 0 } } ( \Omega ) \to H ^ { 1 } ( M , \mathbb { R } )$ , called the flux homomorphism. Let $p \in \mathsf { P e } \bigl ( \mathsf { S p } ( \Omega ) \bigr )$ be chosen, and let $\gamma \colon S ^ { 1 } \to M$ be a closed curve representing an element of $H _ { 1 } ( M , \mathbb { Z } )$ . Then we can define

$$
F ( p , \gamma ) = \int _ { [ 0 , 1 ] \times S ^ { 1 } } ( p \cdot \gamma ) ^ { \ast } ( \Omega )
$$

where $( p \cdot \gamma ) \colon [ 0 , 1 ] \times S ^ { 1 } \to M$ is defined by $( p \cdot \gamma ) ( t , \theta ) = p ( t , \gamma ( \theta ) )$ . The number $F ( p , \gamma )$ is called the flux of $p$ through γ.

(i) Show that $F ( p , \gamma ) = F ( p ^ { \prime } , \gamma ^ { \prime } )$ if p is homotopic to $p ^ { \prime }$ and $\gamma$ is homologous to $\gamma ^ { \prime } )$ (Hint: Use Stokes’ Theorem several times.)

Thus, $F$ is actually well defined as a map $F \colon \widetilde { S } \overline { { \mathfrak { p } } } ^ { 0 } ( \Omega ) \times H _ { 1 } ( M , \mathbb { R } ) \to \mathbb { R } .$

(ii) Show that $F \colon \widetilde { S } \overline { { \mathfrak { p } } } ^ { 0 } ( \Omega ) \times H _ { 1 } ( M , \mathbb { R } ) \to \mathbb { R }$ is linear in its second variable and that, under the obvious multiplication, we have

$$
F ( p p ^ { \prime } , \gamma ) = F ( p , \gamma ) + F ( p ^ { \prime } , \gamma ) .
$$

(Hint: Use Stokes’ Theorem again.)

Thus, F may be transposed to become a homomorphism

$$
\Phi { : \widetilde { { \mathsf { S p } } } ^ { 0 } } ( \Omega ) \to H ^ { 1 } ( M , \mathbb { R } ) .
$$

Show (by direct computation) that if $\zeta$ is a closed 1-form on M for which the symplectic vector field $Z = \sharp \zeta$ is complete on $M$ , then the path p in $\mathsf { S p } ( M )$ defined by the flow of Z from $t = 0$ to $t = 1$ satisfies $\Phi ( p ) = [ \zeta ] \in H ^ { 1 } ( M , \mathbb { R } )$ Conclude that the flux homomorphism Φ is always surjective and that its derivative $\Phi ^ { \prime } ( \tilde { e } ) \colon s \mathfrak { p } ( \Omega )  H ^ { 1 } ( M , \mathbb { R } )$ ) is just the operation of taking cohomology classes. (Recall that we identify $\mathsf { s p } ( \Omega )$ with ${ \mathcal { Z } } ^ { 1 } ( M ) .$ )(iii) Show that if M is a compact surface of genus $g > 1$ , then the flux homomorphism is actually well defined as a map from $\mathsf { S p } ( \Omega )$ to $H ^ { 1 } ( M , \mathbb { R } )$ Would the same result be true if M were of genus 1? How could you modify the map so as to make it welldefined on $\mathsf { S p } ( \Omega )$ in the case of the torus? (Hint: Show that if you have two paths $p$ and $p ^ { \prime }$ with the same endpoint, then you can express the difference of their fluxes across a circle $\gamma$ as an integral of the form

$$
\int _ { S ^ { 1 } \times S ^ { 1 } } \Psi ^ { * } ( \Omega )
$$

where $\Psi \colon S ^ { 1 } \times S ^ { 1 } \to M$ is a certain piecewise smooth map from the torus into M. Now use the fact that, for any piecewise smooth map $\Psi \colon S ^ { 1 } \times S ^ { 1 } \to M$ , the induced map $\Psi ^ { * } \colon H ^ { 2 } ( M , \mathbb { R } ) \to H ^ { 2 } ( S ^ { 1 } \times S ^ { 1 }$ , R) on cohomology is zero. (Why does this follow from the assumption that the genus of M is greater than 1?) )

In any case, the subgroup ker Φ (or its image under the natural projection from $\widetilde { \mathsf { S p } } ^ { 0 } ( \Omega )$ to $S \mathfrak { p } ( \Omega ) )$ is known as the group H(Ω) of exact or Hamiltonian symplectomorphisms. Note that, at least formally, its Lie algebra is h(Ω).

13. In the case of the geodesic flow on a surface of revolution (see Lecture 4), show that the energy $f ^ { 1 } = E _ { L }$ and the conserved quantity $f ^ { 2 } = F ( r ) \dot { r } + G ( r ) \dot { \theta }$ are in involution. Use the algorithm described in Theorem 3 to compute the functions $a _ { 1 }$ and $a _ { 2 }$ , thus verifying that the geodesic equations on a surface of revolution are integrable by quadrature.

## Lecture 6: Symplectic Manifolds, II

The Space of Symplectic Structures on M.

I want to turn now to the problem of describing the symplectic structures a manifold M can have. This is a surprisingly delicate problem and is currently a subject of research.

Of course, one fundamental question is whether a given manifold has any symplectic structures at all. I want to begin this lecture with a discussion of the two known obstructions for a manifold to have a symplectic structure.

The cohomology ring condition. If $\Omega \in \mathcal { A } ^ { 2 } ( M ^ { 2 n } )$ is a symplectic structure on a compact manifold M, then the cohomology class $[ \Omega ] \in H _ { d R } ^ { 2 } ( M , \mathbb { R } )$ is non-zero. In fact, $[ \Omega ] ^ { n } = [ \Omega ^ { n } ]$ , but the class $\left[ \Omega ^ { n } \right]$ cannot vanish in $H _ { d R } ^ { 2 n } ( M )$ because the integral of $\Omega ^ { n }$ over M is clearly non-zero. Thus, we have

Proposition 1: If $M ^ { 2 n }$ is compact and has a symplectic structure, there must exist an element $u \in H ^ { 2 } ( M , \mathbb { R } )$ so that $u ^ { n } \neq 0 \in H _ { d R } ^ { 2 n } ( M )$ .

Example. This immediately rules out the existence of a symplectic structure on $S ^ { 2 n }$ for all $n > 1$ . One consequence of this, as you are asked to show in the Exercises, is that there cannot be any simple notion of connected sum in the category of symplectic manifolds (except in dimension 2).

The bundle obstruction. If M admits a symplectic structure Ω, then, in particular, this defines a symplectic structure on each of the tangent spaces $T _ { m } M$ that varies continuously with m. In other words, T M must carry the structure of a symplectic vector bundle. There are topological obstructions to the existence of such a structure on the tangent bundle of a general manifold. As a simple example, if M has a symplectic structure, then T M must be orientable.

There are more subtle obstructions than orientation. Unfortunately, a description of these obstructions requires some acquaintance with the theory of characteristic classes. However, part of the following discussion will be useful even to those who aren’t familiar with characteristic class theory, so I will give it now, even though the concepts will only reveal their importance in later Lectures.

Definition 1: An almost symplectic structure on a manifold $M ^ { 2 n }$ is a smooth 2-form Ω defined on M that is non-degenerate but not necessarily closed. An almost complex structure on $M ^ { 2 n }$ is a smooth bundle map $J \colon T M \to T M$ that satisfies $J ^ { 2 } v = - v$ for all v in T M .

The reason that I have introduced both of these concepts at the same time is that they are intimately related. The really deep aspects of this relationship will only become apparent in the Lecture 9, but we can, at least, give the following result now.

Proposition 2: A manifold $M ^ { 2 n }$ has an almost symplectic structure if and only if it has an almost complex structure.

Proof: First, suppose that M has an almost complex structure $J .$ Let $g _ { 0 }$ be any Riemannian metric on M. (Thus, $g _ { 0 } \colon T M \to  { \mathbb { R } }$ is a smooth function that restricts to each $T _ { m } M$ to be a positive definite quadratic form.) Now define a new Riemannian metric by the formula

$$
g ( v ) = g _ { 0 } ( v ) + g _ { 0 } ( J v ) .
$$

Then g has the property that $g ( J v ) = g ( v )$ for all $v \in T M$ since

$$
g ( J v ) = g _ { 0 } ( J v ) + g _ { 0 } ( J ^ { 2 } v ) = g _ { 0 } ( J v ) + g _ { 0 } ( - v ) = g ( v ) .
$$

Now let $\langle , \rangle$ denote the (symmetric) inner product associated with $g .$ . Thus, $\langle v , v \rangle =$ $g ( v )$ , so we have $\langle J x , J y \rangle = \langle x , y \rangle$ when x and y are tangent vector with the same base point. For $x , y \in T _ { m } M$ define $\Omega ( x , y ) = \langle J x , y \rangle$ . I claim that Ω is a non-degenerate 2-form on M. To see this, first note that

$$
\Omega ( x , y ) = \langle J x , y \rangle = - \langle J x , J ^ { 2 } y \rangle = - \langle J ^ { 2 } y , J x \rangle = - \langle J y , x \rangle = - \Omega ( y , x ) ,
$$

so Ω is a 2-form. Moreover, if x is a non-zero tangent vector, then $\Omega ( x , J x ) = \langle J x , J x \rangle =$ $g ( x ) > 0$ , so it follows that $x \lrcorner \Omega \neq 0$ . Thus Ω is non-degenerate.

To go the other way is a little more delicate. Suppose that Ω is given and fix a Riemannian metric g on M with associated inner product $\langle , \rangle$ . Then, by linear algebra there exists a unique bundle mapping $A \colon T M \to T M$ so that $\Omega ( x , y ) = \langle A x , y \rangle$ . Since Ω is skew-symmetric and non-degenerate, it follows that A must be skew-symmetric relative to $\langle , \rangle$ and must be invertible. It follows that $- A ^ { 2 }$ must be symmetric and positive definite relative to $\langle , \rangle$

Now, standard results from linear algebra imply that there is a unique smooth bundle map $B \colon T M \to T M$ that is positive definite and symmetric with respect to $\langle , \rangle$ and that satisfies $B ^ { 2 } = - A ^ { 2 }$ . Moreover, this linear mapping B must commute with A. (See the Exercises if you are not familiar with this fact). Thus, the mapping $J = A B ^ { - 1 }$ satisfies $J ^ { 2 } = - I .$ , as desired. 

It is not hard to show that the mappings $( J , g _ { 0 } ) \mapsto \Omega$ and $( \Omega , g ) \mapsto J$ constructed in the proof of Proposition 1 depend continuously (in fact, smoothly) on their arguments. Since the set of Riemannian metrics on M is contractible, it follows that the set of homotopy classes of almost complex structures on M is in natural one-to-one correspondence with the set of homotopy classes of almost symplectic structures.

(The reader who is familiar with the theory of principal bundles knows that at the heart of Proposition 1 is the fact that $\operatorname { S p } ( n , \mathbb { R } )$ and $\mathrm { G L } ( n , \mathbb { C } )$ have the same maximal compact subgroup, namely $\mathrm { U } ( n )$ .)

Now I can describe some of the bundle obstructions. Suppose that M has a symplectic structure Ω and let J be any one of the almost complex structures on M we constructed above. Then the tangent bundle of M can be regarded as a complex bundle, which we will denote by $T ^ { J }$ , and hence has a total Chern class

$$
c ( T ^ { J } ) = \big ( 1 + c _ { 1 } ( J ) + c _ { 2 } ( J ) + \dots + c _ { n } ( J ) \big )
$$

where $c _ { i } ( J ) \in H ^ { 2 i } ( M , \mathbb { Z } )$ . Now, by the properties of Chern classes, $c _ { n } ( J ) = e ( T M )$ , where $e ( T M )$ is the Euler class of the tangent bundle given the orientation determined by the volume form $\Omega ^ { n }$

These classes are related to the Pontrijagin classes of T M by the Whitney sum formula (see [MS]):

$$
\begin{array} { l } { { p ( T M ) = 1 - p _ { 1 } ( T M ) + p _ { 2 } ( T M ) - \cdots + ( - 1 ) ^ { \left\lceil n / 2 \right\rceil } p _ { \left\lceil n / 2 \right\rceil } ( T M ) } } \\ { { \qquad = c ( T ^ { J } \oplus T ^ { - J } ) } } \\ { { \qquad = \left( 1 + c _ { 1 } ( J ) + c _ { 2 } ( J ) + \cdots + c _ { n } ( J ) \right) \left( 1 - c _ { 1 } ( J ) + c _ { 2 } ( J ) - \cdots + ( - 1 ) ^ { n } c _ { n } ( J ) \right) } } \end{array}
$$

Since $p ( T M )$ depends only on the diffeomorphism class of M, this gives quadratic equations for the $c _ { i } ( J )$ ,

$$
p _ { k } ( T ) = \left( c _ { k } ( J ) \right) ^ { 2 } - 2 c _ { k - 1 } ( J ) c _ { k + 1 } ( J ) + \cdots + ( - 1 ) ^ { k } 2 c _ { 0 } ( J ) c _ { 2 k } ( J ) ,
$$

to which any manifold with an almost complex structure must have solutions. Since not every 2n-manifold has cohomology classes $c _ { i } ( J )$ satisfying these equations, it follows that some 2n-manifolds have no almost complex structure and hence, by Proposition 2, no almost symplectic structure either.

Examples. Here are two examples in dimension 4 to show that the cohomology ring condition and the bundle obstruction are independent.

• $M = S ^ { 1 } \times S ^ { 3 }$ does not have a symplectic structure because $H ^ { 2 } ( M , \mathbb { R } ) = 0$ . However the bundle obstruction vanishes because M is parallelizable (why?). Thus M does have an almost symplectic structure.

• $M = \mathbb { C P } ^ { 2 } \# \mathbb { C P } ^ { 2 }$ The cohomology ring of M in this case is generated over $\mathbb { Z }$ by two generators $u _ { 1 }$ and $u _ { 2 }$ in $H ^ { 2 } ( M , \mathbb { Z } )$ that are subject to the relations $u _ { 1 } u _ { 2 } = 0$ and $u _ { 1 } ^ { 2 } = u _ { 2 } ^ { 2 } = v$ where v generates $H ^ { 4 } ( M , \mathbb { Z } )$ For any non-zero class $u = n _ { 1 } u _ { 1 } + n _ { 2 } u _ { 2 }$ , we have $u ^ { 2 } = ( n _ { 1 } ^ { 2 } + n _ { 2 } ^ { 2 } ) v \neq 0$ . Thus the cohomology ring condition is satisfied.

However, M has no almost symplectic structure: If it did, then $T = T M$ would have a complex structure J, with total Chern class $c ( J )$ and the equations above would give $p _ { 1 } ( T ) = \left( c _ { 1 } ( J ) \right) ^ { 2 } - 2 c _ { 2 } ( J )$ . Moreover, we would have $e ( T ) = c _ { 2 } ( J )$ . Thus, we would have to have

$$
\big ( c _ { 1 } ( J ) \big ) ^ { 2 } = p _ { 1 } ( T ) + 2 e ( T ) .
$$

For any compact, simply-connected, oriented 4-manifold M with orientation class $\mu \in H ^ { 4 } ( M , \mathbb { Z } )$ , the Hirzebruch Signature Theorem (see [MS]) implies $p _ { 1 } ( T ) = 3 ( b _ { 2 } ^ { + } -$ $b _ { 2 } ^ { - } ) \mu$ , where $b _ { 2 } ^ { \pm }$ are the number of positive and negative eigenvalues respectively of the intersection pairing $H ^ { 2 } ( M , \mathbb { Z } ) \times H ^ { 2 } ( M , \mathbb { Z } ) \to \mathbb { Z }$ . In addition, $e ( T ) = ( 2 + b _ { 2 } ^ { + } + b _ { 2 } ^ { - } ) \mu$ . Substituting these into the above formula, we would have ${ \left( c _ { 1 } ( J ) \right) } ^ { 2 } = ( 4 + 5 b _ { 2 } ^ { + } - b _ { 2 } ^ { - } ) \mu$ for any complex structure J on the tangent bundle of M.

In particular, if $M = \mathbb { C P } ^ { 2 } \# \mathbb { C P } ^ { 2 }$ had an almost complex structure J, then $\left( c _ { 1 } ( J ) \right) ^ { 2 }$ would be either 14v $( { \mathrm { i f ~ } } \mu = v _ { ; }$ , since then $b _ { 2 } ^ { + } = 2$ and $b _ { 2 } ^ { - } = 0 ) \mathrm { o r } - 2 v \mathrm { ( i f } \mu = - v$ , since then $b _ { 2 } ^ { + } = 0$ and $b _ { 2 } ^ { - } = 2 )$ . However, by our previous calculations, neither 14v nor −2v is the square of a cohomology class in $\breve { H ^ { 2 } } ( \mathbb { C P } ^ { 2 } \not \mp \mathbb { C P } ^ { 2 } , \mathbb { Z } )$

◮ This example shows that, in general, one cannot hope to have a connected sum operation for symplectic manifolds.

The actual conditions for a manifold to have an almost symplectic structure can be expressed in terms of characteristic classes, so, in principle, this can always be determined once the manifold is given explicitly. In Lecture 9 we will describe more fully the following remarkable result of Gromov:

◮ If $M ^ { 2 n }$ has no compact components and has an almost symplectic structure Υ, then there exists a symplectic structure Ω on M that is homotopic to Υ through almost symplectic structures.

Thus, the problem of determining which manifolds have symplectic structures is now reduced to the compact case. In this case, no obstruction beyond what I have already described is known. Thus, I can state the following:

Basic Open Problem: If a compact manifold $M ^ { 2 n }$ satisfies the cohomology ring condition and has an almost symplectic structure, does it have a symplectic structure?

Even (perhaps especially) for 4-manifolds, this problem is extremely interesting and very poorly understood.

Deformations of Symplectic Structures. We will now turn to some of the features of the space of symplectic structures on a given manifold that does admit symplectic structures. First, we will examine the ‘deformation problem’. The following theorem due to Moser (see [We]) shows that symplectic structures determining a fixed cohomology class in $H ^ { 2 }$ on a compact manifold are ‘rigid’.

Theorem 1: $I f M ^ { 2 n }$ is a compact manifold and $\Omega _ { t }$ for $t \in [ 0 , 1 ]$ is a continuous 1-parameter family of smooth symplectic structures on M that has the property that the cohomology classes $\left[ \Omega _ { t } \right]$ in $H _ { d R } ^ { 2 } ( M , \mathbb { R } )$ are independent of $t ,$ then for each $t \in [ 0 , 1 ]$ , there exists a diffeomorphism $\phi _ { t }$ so that $\phi _ { t } ^ { * } ( \Omega _ { t } ) = \Omega _ { 0 }$ .

Proof: We will start by proving a special case and then deduce the general case from it. Suppose that $\Omega _ { 0 }$ is a symplectic structure on M and that $\varphi \in { \mathcal { A } } ^ { 1 } ( M )$ is a 1-form so that, for all $s \in ( - 1 , 1 )$ , the 2-form

$$
\Omega _ { s } = \Omega _ { 0 } + s d \varphi
$$

is a symplectic form on M as well. (This is true for all sufficiently “small” 1-forms on M since M is compact.) Now consider the 2-form on $( - 1 , 1 ) \times M$ defined by the formula

$$
\Omega = \Omega _ { 0 } + s d \varphi - \varphi \wedge d s .
$$

(Here, we are using s as the coordinate on the first factor (−1, 1) and, as usual, we write $\Omega _ { 0 }$ and $\varphi$ instead of $\pi _ { 2 } ^ { * } ( \Omega _ { 0 } )$ and $\pi _ { 2 } ^ { * } ( \varphi )$ where $\pi _ { 2 } \colon ( - 1 , 1 ) \times M \to M$ is the projection on the second factor.)

The reader can check that Ω is closed on $( - 1 , 1 ) \times M$ . Moreover, since Ω pulls back to each slice $\{ s _ { 0 } \} \times M$ to be the non-degenerate form $\Omega _ { s _ { 0 } }$ it follows that Ω has half-rank n everywhere. Thus, the kernel $N _ { \Omega }$ is 1-dimensional and is transverse to each of the slices $\{ t \} \times M$ . Hence there is a unique vector field X that spans $N _ { \Omega }$ and satisfies $d s ( X ) = 1$

Now because M is compact, it is not difficult to see that each integral curve of X projects by $s = \pi _ { 1 }$ diffeomorphically onto (−1, 1). Moreover, it follows that there is a smooth map $\phi \colon ( - 1 , 1 ) \times M \to M$ so that, for each m, the curve $t \mapsto \phi ( t , m )$ is the integral curve of X that passes through $( 0 , m )$

It follows that the map $\Phi \colon ( - 1 , 1 ) \times M \to ( - 1 , 1 ) \times M$ defined by

$$
\Phi ( t , m ) = \bigl ( t , \phi ( t , m ) \bigr )
$$

carries the vector field $\partial / \partial s$ to the vector field X. Moreover, since $\Omega _ { 0 }$ and Ω have the same value when pulled back to the slice $\{ 0 \} \times M$ and since

$$
\begin{array} { r } { \mathfrak { L } _ { \partial / \partial s } \Omega _ { 0 } = 0 \qquad \mathrm { ~ a n d ~ } \qquad \mathfrak { L } _ { X } \Omega = 0 } \\ { \partial / \partial s \lrcorner \Omega _ { 0 } = 0 \qquad \mathrm { ~ a n d ~ } \qquad X \lrcorner \Omega = 0 , } \end{array}
$$

it follows easily that $\Phi ^ { * } ( \Omega ) = \Omega _ { 0 }$ . In particular, ${ \phi } _ { t } ^ { * } ( \Omega _ { t } ) = \Omega _ { 0 }$ where $\phi _ { t }$ is the diffeomorphism of M given by $\phi _ { t } ( m ) = \phi ( t , m )$ .

Now let us turn to the general case. If $\Omega _ { t }$ for $0 \leq t \leq 1$ is any continuous family of smooth closed 2-forms for which the cohomology classes $[ \Omega _ { t } ]$ are all equal to $\left[ \Omega _ { 0 } \right]$ , then for any two values $t _ { 1 }$ and $t _ { 2 }$ in the unit interval, consider the 1-parameter family of 2-forms

$$
\Upsilon _ { s } = ( 1 - s ) \Omega _ { t _ { 1 } } + s \Omega _ { t _ { 2 } } .
$$

Using the compactness of M, it is not difficult to show that for $t _ { 2 }$ sufficiently close to $t _ { 1 }$ the family $\Upsilon _ { s }$ is a 1-parameter family of symplectic forms on M for s in some open interval containing [0, 1]. Moreover, by hypothesis, $\left[ \Omega _ { t _ { 2 } } - \Omega _ { t _ { 1 } } \right] = 0$ , so there exists a 1-form $\varphi$ on M so that $d \varphi = \Omega _ { t _ { 2 } } - \Omega _ { t _ { 1 } }$ . Thus,

$$
\Upsilon _ { s } = \Omega _ { t _ { 1 } } + s d \varphi .
$$

By the special case already treated, there exists a diffeomorphism $\phi _ { t _ { 2 } , t _ { 1 } }$ of M so that $\phi _ { t _ { 2 } , t _ { 1 } } ^ { * } ( \Omega _ { t _ { 2 } } ) = \Omega _ { t _ { 1 } }$

Finally, using the compactness of the interval $[ 0 , t ]$ for any $t \in [ 0 , 1 ]$ , we can subdivide this interval into a finite number of intervals $[ t _ { 1 } , t _ { 2 } ]$ on which the above argument works. Then, by composing diffeomorphisms, we can construct a diffeomorphism $\phi _ { t }$ of M so that $\phi _ { t } ^ { * } ( \Omega _ { t } ) = \Omega _ { 0 }$ 

The reader may have wanted the family of diffeomorphisms $\phi _ { t }$ to depend continuously on t and smoothly on t if the family $\Omega _ { t }$ is smooth in t. This can, in fact, be arranged. However, it involves showing that there is a smooth family of 1-forms $\varphi _ { t }$ on M so that $\begin{array} { r } { \frac { d } { d t } \Omega _ { t } = d \varphi _ { t } } \end{array}$ , i.e., smoothly solving the d-equation. This can be done, but requires some delicacy or use of elliptic machinery (e.g., Hodge-deRham theory).

Theorem 1 does not hold without the hypothesis of compactness. For example, if Ω is the restriction of the standard structure on $\mathbb { R } ^ { 2 n }$ to the unit ball $B ^ { 2 n }$ , then for the family $\Omega _ { t } = e ^ { t } \Omega$ there cannot be any family of diffeomorphisms of the ball $\phi _ { t }$ so that ${ \phi } _ { t } ^ { * } ( \Omega _ { t } ) = \Omega$ since the integrals over B of the volume forms $( \Omega _ { t } ) ^ { n } = e ^ { n t } \Omega ^ { n }$ are all different.

Intuitively, Theorem 1 says that the “connected components” of the space of symplectic structures on a manifold are orbits of the group $\mathsf { D i f f } ^ { 0 } ( M )$ of diffeomorphisms isotopic to the identity. (The reason this is only intuitive is that we have not actually defined a topology on the space of symplectic structures on M .)

It is an interesting question as to how many “connected components” the space of symplectic structures on M has. The work of Gromov has yielded methods to attack this problem and I will have more to say about this in Lecture 9.

## Submanifolds of Symplectic Manifolds

We will now pass on to the study of the geometry of submanifolds of a symplectic manifold. The following result describes the behaviour of symplectic structures near closed submanifolds. This theorem, due to Weinstein (see [Weinstein]), can be regarded as a generalization of Darboux’ Theorem. The reader will note that the proof is quite similar to the proof of Theorem 1.

Theorem 2: Let $P \subset M$ be a closed submanifold and let $\Omega _ { 0 }$ and $\Omega _ { 1 }$ be symplectic structures on M that have the property that $\Omega _ { 0 } ( p ) = \Omega _ { 1 } ( p )$ for all $p \in P$ . Then there exist open neighborhoods $U _ { 0 }$ and $U _ { 1 }$ of P and a diffeomorphism φ: $U _ { 0 }  U _ { 1 }$ satisfying $\phi ^ { * } ( \Omega _ { 1 } ) = \Omega _ { 0 }$ and which moreover fixes P pointwise and satisfies $\phi ^ { \prime } ( p ) = i d _ { p } \colon T _ { p } M \to T _ { p } M$ for all $p \in P$

Proof: Consider the linear family of 2-forms

$$
\Omega _ { t } = ( 1 - t ) \Omega _ { 0 } + t \Omega _ { 1 }
$$

which ‘interpolates’ between the forms $\Omega _ { 0 }$ and $\Omega _ { 1 }$ . Since [0, 1] is compact and since, by hypothesis, $\Omega _ { 0 } ( p ) = \Omega _ { 1 } ( p )$ for all $p \in P$ , it easily follows that there is an open neighborhood U of P in M so that $\Omega _ { t }$ is a symplectic structure on U for all t in some open interval $I = ( - \varepsilon , 1 + \varepsilon )$ containing [0, 1].

We may even suppose that U is a ‘tubular neighborhood’ of P that has a smooth retraction $R \colon [ 0 , 1 ] \times U  U$ into P . Since $\Phi = \Omega _ { 1 } - \Omega _ { 0 }$ vanishes on P , it follows without too much difficultly (see the Exercises) that there is a 1-form $\varphi$ on U that vanishes on P and that satisfies $d \varphi = \Phi$

Now, on $I \times U$ , consider the 2-form

$$
\Omega = \Omega _ { 0 } + s d \varphi - \varphi \wedge d s .
$$

This is a closed 2-form of half-rank n on $I \times U$ . Just as in the previous theorem, it follows that there exists a unique vector field X on $I \times U$ so that $d s ( X ) = 1$ and $X \ J \Omega = 0$

Since $\varphi$ and $d \varphi$ vanish on P , the vector field X has the property that $X ( s , p ) = \partial / \partial s$ for all $p \in P$ and $s \in I$ . In particular, the set $\{ 0 \} \times P$ lies in the domain of the time 1 flow of X. Since this domain is an open set, it follows that there is an open neighborhood $U _ { 0 }$ of P in U so that $\{ 0 \} \times U _ { 0 }$ lies in the domain of the time 1 flow of X. The image of $\{ 0 \} \times U _ { 0 }$ under the time 1 flow of X is of the form $\{ 1 \} \times U _ { 1 }$ where $U _ { 1 }$ is another open neighborhood of $P$ in $U$ .

Thus, the time 1 flow of X generates a diffeomorphism $\phi \colon U _ { 0 } \to U _ { 1 }$ . By the arguments of the previous theorem, it follows that $\phi ^ { * } ( \Omega _ { 1 } ) = \Omega _ { 0 }$ . I leave it to the reader to check that $\phi$ fixes P in the desired fashion. 

Theorem 2 has a useful corollary:

Corollary : Let Ω be a symplectic structure on M and let $f _ { 0 }$ and $f _ { 1 }$ be smooth embeddings of a manifold P into M so that $f _ { 0 } ^ { * } ( \Omega ) = f _ { 1 } ^ { * } ( \Omega )$ and so that there exists a smooth bundle isomorphism $\tau { : } f _ { 0 } ^ { * } ( T M ) \to f _ { 1 } ^ { * } ( T M )$ that extends the identity map on the subbundle $T P \subset$ $f _ { i } ^ { * } ( T M )$ and that identifies the symplectic structures on $f _ { i } ^ { * } ( T M )$ . Then there exist open neighborhoods $U _ { i }$ of $f _ { i } ( P )$ in M and a diffeomorphism φ: $U _ { 0 } \to U _ { 1 }$ that satisfies $\phi ^ { * } ( \Omega ) = \Omega$ and, moreover, $\phi \circ f _ { 0 } = f _ { 1 }$

Proof: It is an elementary result in differential topology that, under the hypotheses of the Corollary, there exists an open neighborhood $W _ { 0 }$ of $f _ { 0 } ( P )$ in M and a smooth diffeomorphic embedding $\psi \colon W _ { 0 } \to M$ so that ψ $f _ { 0 } = f _ { 1 }$ and $\psi ^ { \prime } \big ( f _ { 0 } ( p ) \big ) \colon T _ { f _ { 0 } ( p ) } ( M ) \to T _ { f _ { 1 } ( p ) } ( M )$ is equal to $\tau ( p )$ . It follows that $\psi ^ { * } ( \Omega )$ is a symplectic form on $W _ { 0 }$ that agrees with Ω along $f _ { 0 } ( P )$ By Theorem 2, it follows that there is a neighborhood $U _ { 0 }$ of $f _ { 0 } ( P )$ that lies in $W _ { 0 }$ and a smooth map ν: $U _ { 0 } \to W _ { 0 }$ that is a diffeomorphism onto its image, fixes $f _ { 0 } ( P )$ pointwise, satisfies $\nu ^ { \prime } \big ( f _ { 0 } ( p ) \big ) = i d _ { f _ { 0 } ( p ) }$ for all $p \in P$ , and also satisfies $\nu ^ { * } \bigl ( \psi ^ { * } ( \Omega ) \bigr ) = \Omega$ . Now just take $\phi = \psi \circ \nu $ 

We will now give two particularly important applications of this result:

If $P \subset M$ is a symplectic submanifold, then by using Ω, we can define a normal bundle for P as follows:

$$
\nu ( P ) = \{ ( p , v ) \in P \times T M | v \in T _ { p } M , \ \Omega ( v , w ) = 0 \mathrm { ~ f o r ~ a l l ~ } w \in T _ { p } P \} .
$$

The bundle $\nu ( P )$ has a natural symplectic structure on each of its fibers (see the Exercises), and hence is a symplectic vector bundle. The following proposition shows that, up to local diffeomorphism, this normal bundle determines the symplectic structure Ω on a neighborhood of P .

Proposition 3: Let $( P , \Upsilon )$ be a symplectic manifold and let $f _ { 0 } , f _ { 1 } \colon P  M$ be two symplectic embeddings of P as submanifolds of M so that the normal bundles $\nu _ { 0 } ( P )$ and $\nu _ { 1 } ( P )$ are isomorphic as symplectic vector bundles. Then there are open neighborhoods $U _ { i }$ of $f _ { i } ( P )$ in M and a symplectic diffeomorphism $\phi \colon U _ { 0 } \to U _ { 1 }$ that satisfies $f _ { 1 } = \phi \circ f _ { 0 }$ .

Proof: It suffices to construct the map τ required by the hypotheses of Theorem 2. Now, we have a symplectic bundle decomposition $f _ { i } ^ { * } ( T M ) = T P \oplus \nu _ { i } ( P )$ for $i = 1 , 2$ . If $\alpha \colon \nu _ { 0 } ( P ) \to \nu _ { 1 } ( P )$ is a symplectic bundle isomorphism, we then define $\tau = i d \oplus \alpha$ in the obvious way and we are done. 

At the other extreme, we want to consider submanifolds of M to which the form Ω pulls back to be as degenerate as possible.

Definition 2: If Ω is a symplectic structure on $M ^ { 2 n }$ , an immersion $f \colon P \to M$ is said to be isotropic if $f ^ { * } ( \Omega ) = 0$ . If the dimension of $P$ is n, we say that $f$ is a Lagrangian immersion. If in addition, f is one-to-one, then we say that $f ( P )$ is a Lagrangian submanifold of M.

Note that the dimension of an isotropic submanifold of $M ^ { 2 n }$ is at most $n ,$ so the Lagrangian submanifolds of M have maximal dimension among all isotropic submanifolds.

Example: Graphs of Symplectic Mappings. If $f \colon M \to N$ is a symplectic mapping where Ω and Υ are the symplectic forms on M and N respectively, then the graph of $f$ in $M \times N$ is an isotropic submanifold of $M \times N$ endowed with the symplectic structure $( - \Omega ) \oplus \Upsilon = \pi _ { 1 } ^ { * } ( - \Omega ) + \pi _ { 2 } ^ { * } ( \Upsilon )$ . If M and N have the same dimension, then the graph of $f$ in $M \times N$ is a Lagrangian submanifold.

Example: Closed 1-forms. If α is a 1-form on M, then the graph of α in $T ^ { * } M$ is a Lagrangian submanifold of $T ^ { * } M$ if and only if $d \alpha = 0$ . This follows because Ω on $T ^ { * } M$ has the “reproducing property” that $\alpha ^ { * } ( \Omega ) = d \alpha$ for any 1-form on M.

Proposition 4: Let Ω be a symplectic structure on M and let P be a closed Lagrangian submanifold of M. Then there exists an open neighborhood U of the zero section in $T ^ { * } P$ and a smooth map φ: $U \to M$ satisfying $\phi ( 0 _ { p } ) = p$ that is a diffeomorphism onto an open neighborhood of P in M and that pulls back Ω to be the standard symplectic structure on U .

Proof: From the earlier proofs, the reader probably can guess what we will do. Let $\iota \colon P  M$ be the inclusion mapping and let $\zeta \colon P \to T ^ { * } P$ be the zero section of $T ^ { * } P$ . I leave as an exercise for the reader to show that $\zeta ^ { * } ( T ( T ^ { * } P ) ) = T P \oplus T ^ { * } P ;$ , and that the induced symplectic structure Υ on this sum is simply the natural one on the sum of a bundle and its dual:

$$
\Upsilon \big ( ( v _ { 1 } , \xi _ { 1 } ) , ( v _ { 2 } , \xi _ { 2 } ) \big ) = \xi _ { 1 } ( v _ { 2 } ) - \xi _ { 2 } ( v _ { 1 } )
$$

I will show that there is a bundle isomorphism $\tau { : } T P \oplus T ^ { * } P \to \iota ^ { * } ( T M )$ that restricts to the subbundle $T P$ to be $\iota ^ { \prime } { : } T P \to \iota ^ { * } ( T M )$

First, select an n-dimensional subbundle $L ~ \subset ~ \iota ^ { * } ( T M )$ that is complementary to $\iota ^ { \prime } ( T P ) \subset \iota ^ { * } ( T M )$ . It is not difficult to show (and it is left as an exercise for the reader) that it is possible to choose L so that it is a Lagrangian subbundle of $\iota ^ { * } ( T M )$ so that there is an isomorphism $\alpha \colon T ^ { * } P \to L$ so that $\tau { : } T P \oplus T ^ { * } P \to \iota ^ { \prime } ( T P ) \oplus L$ defined by $\tau = \iota ^ { \prime } \oplus$ α is a symplectic bundle isomorphism.

Now apply the Corollary to Theorem 2.

Proposition 4 shows that the symplectic structure on a manifold M in a neighborhood of a closed Lagrangian submanifold P is completely determined by the diffeomorphism type of P . This fact has several interesting applications. We will only give one of them here.

Proposition 5: Let $( M , \Omega )$ be a compact symplectic manifold with $H _ { d R } ^ { 1 } ( M , \mathbb { R } ) = 0$ Then in Diff(M) endowed with the $C ^ { 1 }$ topology, there exists an open neighborhood U of the identity map so that any symplectomorphism φ: $M  M$ that lies in U has at least two fixed points.

Proof: Consider the manifold $M \times M$ endowed with the symplectic structure $\Omega \oplus ( - \Omega )$ The diagonal $\Delta \subset M \times M$ is a Lagrangian submanifold. Proposition 4 implies that there exists an open neighborhood $U$ of the zero section in $T ^ { * } M$ and a symplectic map $\psi : U \to M \times M$ that is a diffeomorphism onto its image so that $\psi ( 0 _ { p } ) = ( p , p )$

Now, there is an open neighborhood $\mathcal { U } _ { 0 }$ of the identity map on M in Diff(M) endowed with the $C ^ { 0 }$ topology that is characterized by the condition that $\phi$ belongs to $\mathcal { U } _ { 0 }$ if and only if the graph of $\phi$ in $M \times M$ , namely $i d \times \phi$ lies in the open set $\psi ( U ) \subset M \times M$ Moreover, there is an open neighborhood $\mathcal { U } \subset \mathcal { U } _ { 0 }$ of the identity map on M in Diff(M) endowed with the $C ^ { 1 }$ topology that is characterized by the condition that $\phi$ belongs to U if and only if $\psi ^ { - 1 } \circ ( i d \times \phi ) { : } M \to T ^ { * } M$ is the graph of a 1-form $\alpha _ { \phi }$

Now suppose that $\phi \in \mathcal { U }$ is a symplectomorphism. By our previous discussion, it follows that the graph of $\phi$ in $M \times M$ is Lagrangian. This implies that the graph of $\alpha _ { \phi }$ is Lagrangian in $T ^ { * } M$ , which, by our second example, implies that $\alpha _ { \phi }$ is closed. Since $H _ { d R } ^ { 1 } ( M , \mathbb { R } ) = 0$ , this, in turn, implies that $\alpha _ { \phi } = d f _ { \phi }$ for some smooth function $f$ on M.

Since M is compact, it follows that $f _ { \phi }$ must have at least two critical points. However, these critical points are zeros of the 1-form $d f _ { \phi } = \alpha _ { \phi }$ . It is a consequence of our construction that these points must then be places where the graph of $\phi$ intersects the diagonal $\Delta$ . In other words, they are fixed points of $\phi$ 

This theorem can be generalized considerably. According to a theorem of Hamilton [Ha], if M is compact, then there is an open neighborhood U of the identity map id in $\mathsf { S p } ( \Omega )$ (with the $C ^ { 1 }$ topology) so that every $\phi \in \mathcal { U }$ is the time-one flow of a symplectic vector field $X _ { \phi } \in { \mathfrak { s p } } ( \Omega )$ . If $X _ { \phi }$ is actually Hamiltonian (which would, of course, follow if $H _ { d R } ^ { 1 } ( M , \mathbb { R } ) = \mathrm { 0 ) }$ , then $- X _ { \phi } \lrcorner \Omega = d f _ { \phi }$ , so $X _ { \phi }$ will vanish at the critical points of $f _ { \phi }$ and these will be fixed points of $\phi .$

## Appendix: Lie’s Transformation Groups, II

The reader who is learning symplectic geometry for the first time may be astonished by the richness of the subject and, at the same time, be wondering ‘Are there other geometries like symplectic geometry that remain to be explored?’ The point of this appendix is to give one possible answer to this very vague question.

When Lie began his study of transformation groups in n variables, he modeled his attack on the known study of the finite groups. Thus, his idea was that he would find all of the “simple groups” first and then assemble them (by solving the extension problem) to classify the general group. Thus, if one “group” G had a homomorphism onto another “group” H

$$
1 \longrightarrow K \longrightarrow G \longrightarrow H \longrightarrow 1
$$

then one could regard G as a semi-direct product of H with the kernel subgroup K.

Guided by this idea, Lie decided that the first task was to classify the transitive transformation groups G, i.e., the ones that acted transitively on $\mathbb { R } ^ { n }$ (at least locally). The reason for this was that, if G had an orbit S of dimension $0 < k < n ,$ then the restriction of the action of G to S would give a non-trivial homomorphism of G into a transformation group in fewer variables.

Second, Lie decided that he needed to classify first the ‘groups’ that, in his language, ‘did not preserve any subset of the variables.’ The example he had in mind was the group of diffeomorphisms of $\mathbb { R } ^ { 2 }$ of the form

$$
\phi ( x , y ) = { \big ( } f ( x ) , g ( x , y ) { \big ) } .
$$

Clearly the assignment $\phi \mapsto f$ provides a homomorphism of this group into the group of diffeomorphisms in one variable. Lie called groups that ‘did not preserve any subset of the variables’ primitive. In modern language, primitive is taken to mean that G does not preserve any foliation on $\mathbb { R } ^ { n }$ (coordinates on the leaf space would furnish a ‘proper subset of the variables’ that was preserved by G).

Thus, the fundamental problem was to classify the “primitive transitive continuous transformation groups”.

When the algebra of infinitesimal generators of G was finite dimensional, Lie and his coworkers made good progress. Their work culminated in the work of Cartan and Killing, classifying the finite dimensional simple Lie groups. (Interestingly enough, they did not then go on to solve the extension problem and so classify all Lie groups. Perhaps they regarded this as a problem of lesser order. Or, more likely, the classification turned out to be messy, uninteresting, and ultimately intractable.)

They found that the simple groups fell into two types. Besides the special linear groups, such as $\mathrm { S L } ( n , \mathbb { R } ) , \mathrm { S L } ( n , \mathbb { C } )$ and other complex analogs; orthogonal groups, such as $\mathrm { S O } ( p , q )$ and its complex analogs; and symplectic groups, such as $\operatorname { S p } ( n , \mathbb { R } )$ and its complex analogs (which became known as the classical groups), there were five ‘exceptional’ types. This story is quite long, but very interesting. The ‘finite dimensional Lie groups’ went on to become an essential part of the foundation of modern differential geometry. A complete account of this classification (along with very interesting historical notes) can be found in [He].

However, when the algebra of infinitesimal generators of G was infinite dimensional, the story was not so complete. Lie himself identified four classes of these ‘infinite dimensional primitive transitive transformation groups’. They were

• In every dimension n, the full diffeomorphism group, $\operatorname { D i f f } ( \mathbb { R } ^ { n } )$

• In every dimension n, the group of diffeomorphisms that preserve a fixed volume form $\mu ,$ denoted by $\operatorname { S D i f f } ( \mu )$ .

In every even dimension 2n, the group of diffeomorphisms that preserve the standard symplectic form

$$
\Omega _ { n } = d x _ { 1 } \wedge d y ^ { 1 } + \cdot \cdot \cdot + d x _ { n } \wedge d y ^ { n } ,
$$

denoted by ${ \mathsf { S p } } ( \Omega _ { n } )$

• In every odd dimension $2 n + 1$ , the group of diffeomorphisms that preserve, up to a scalar function multiple, the 1-form

$$
\omega _ { n } = d z + x _ { 1 } d y ^ { 1 } + \cdot \cdot \cdot + x _ { n } d y ^ { n } .
$$

This ‘group’ was known as the contact group and I will denote it by $\operatorname { C t } ( \omega _ { n } )$

However, Lie and his coworkers were never able to discover any others, though they searched diligently. (By the way, Lie was aware that there were also holomorphic analogs acting in $\mathbb { C } ^ { n }$ , but, at that time, the distinction between real and complex was not generally made explicit. Apparently, an educated reader was supposed to know or be able to guess what the generalizations to the complex category were.)

In a series of four papers spanning from 1902 to 1910, Elie Cartan reformulated Lie’s ´ problem in terms of systems of partial differential equations and, under the hypothesis of analyticity (real and complex were not carefully distinguished), he proved that Lie’s classes were essentially all of the infinite dimensional primitive transitive transformation groups. The slight extension was that $\operatorname { S D i f f } ( \mu )$ had a companion extension to $\mathbb { R } \cdot S \mathrm { D i f f } ( \mu )$ the diffeomorphisms that preserve $\mu$ up to a constant multiple and that ${ \mathsf { S p } } ( \Omega _ { n } )$ had a companion extension to $\mathbb { R } \cdot S \mathsf { p } ( \Omega _ { n } )$ , the diffeomorphisms that preserve $\Omega _ { n }$ up to a constant multiple. Of course, there were also the holomorphic analogues of these. Notice the remarkable fact that there are no “exceptional infinite dimensional primitive transitive transformation groups”.

These papers are remarkable, not only for their results, but for the wealth of concepts that Cartan introduced in order to solve his problem. In these papers, Cartan introduces the notion of G-structures (of all orders), principal bundles and their connections, jet bundles, prolongation (both of group actions and exterior differential systems), and a host of other ideas that were only appreciated much later. Perhaps because of its originality, Cartan’s work in this area was essentially ignored for many years.

In the 1950’s, when algebraic varieties were being explored and developed as complex manifolds, it began to be understood that complex manifolds were to be thought of as manifolds with an atlas of coordinate charts whose “overlaps” were holomorphic. Generalizing this example, it became clear that, for any collection Γ of local diffeomorphisms of $\mathbb { R } ^ { n }$ that satisfied the following definition, one could define a category of Γ-manifolds as manifolds endowed with an atlas A of coordinate charts whose overlaps lay in A.

Definition 3: A local diffeomorphism of $\mathbb { R } ^ { n }$ is a pair $( U , \phi )$ where $U \subset \mathbb { R } ^ { n }$ is an open set and $\phi \colon U \ \to \ \mathbb { R } ^ { n }$ is a one-to-one diffeomorphism onto its image. A set Γ of local diffeomorphisms of $\mathbb { R } ^ { n }$ is said to form a pseudo-group on $\mathbb { R } ^ { n }$ if it satisfies the following three properties:

(1) (Composition and Inverses) If $( U , \phi )$ and $( V , \psi )$ are in Γ, then $( \phi ^ { - 1 } ( V ) , \psi \circ \phi )$ and $( \phi ( U ) , \phi ^ { - 1 } )$ also belong to Γ.

(2) (Localization and Globalization) If $( U , \phi )$ is in Γ, and $W \subset U$ is open, then $( W , \phi _ { | W } )$ is also in Γ. Moreover, if $( U , \phi )$ is a local diffeomorphism of $\mathbb { R } ^ { n }$ such that U can be written as the union of open subsets $W _ { \alpha }$ for which $( W _ { \alpha } , \phi _ { | W _ { \alpha } } )$ is in Γ for all α, then $( U , \phi )$ is in Γ.

(3) (Non-triviality) $( \mathbb { R } ^ { n } , i d )$ is in Γ.

As it turned out, the pseudo-groups Γ of interest in geometry were exactly the ones that could be characterized as the (local) solutions of a system of partial differential equations, i.e., they were Lie’s transformation groups. This caused a revival of interest in Cartan’s work. Consequently, much of Cartan’s work has now been redone in modern language. In particular, Cartan’s classification was redone according to modern standards of rigor and a very readable account of this theory can be found in [SS].

In any case, symplectic geometry, seen in this light, is one of a small handful of “natural” geometries that one can impose on manifolds.

# Exercise Set 6: Symplectic Manifolds, II

1. Assume $n > 1$ . Show that if $A _ { r , R } \subset \mathbb { R } ^ { 2 n }$ (with its standard symplectic structure) is the annulus described by the relations $r < | { \bf x } | < R$ , then there cannot be a symplectic diffeomorphism φ: $A _ { r , R } \to A _ { s , S }$ that ‘exchanges the boundaries’. (Hint: Show that if $\phi$ existed one would be able to construct a symplectic structure on $S ^ { 2 n } . )$ Conclude that one cannot na¨ıvely define connected sum in the category of symplectic manifolds. (The “na¨ıve” definition would be to try to take two symplectic manifolds $M _ { 1 }$ and $M _ { 2 }$ of the same dimension, choose an open ball in each one, cut out a sub-ball of each and identify the resulting annuli by an appropriate diffeomorphism that was chosen to be a symplectomorphism.)

2. This exercise completes the proof of Proposition 1.

(i) Let $\mathcal { S } _ { n } ^ { + }$ denote the space of n-by-n positive definite symmetric matrices. Show that the map $\sigma { : } \mathcal { S } _ { n } ^ { + } \to \mathcal { S } _ { n } ^ { + }$ defined by $\sigma ( s ) = s ^ { 2 }$ is a one-to-one diffeomorphism of $\mathcal { S } _ { n } ^ { + }$ onto itself. Conclude that every element of $\mathcal { S } _ { n } ^ { + }$ has a unique positive definite square root and that the map $s \mapsto { \sqrt { s } }$ is a smooth mapping. Show also that, for any $r \in \mathrm { O } ( n )$ , we have $\sqrt { { ^ t r a r } } = { ^ t r } \sqrt { a } r$ , so that the square root function is ${ \mathrm { O } } ( n )$ -equivariant.

(ii) Let $\mathcal { A } _ { n } ^ { \bullet }$ denote the space of n-by-n invertible anti-symmetric matrices. Show that, for $a \in \mathcal { A } _ { n } ^ { \bullet }$ , the matrix $- a ^ { 2 }$ is symmetric and positive definite. Show that the matrix $b = { \sqrt { - a ^ { 2 } } }$ is the unique symmetric positive definite matrix that satisfies $b ^ { 2 } = - a ^ { 2 }$ and moreover that b commutes with a. Check also that the mapping $a \mapsto { \sqrt { - a ^ { 2 } } }$ is ${ \mathrm { O } } ( n )$ -equivariant.

(iii) Now verify the claim made in the proof of Proposition 1 that, for any smooth vector bundle E over a manifold M endowed with a smooth inner product on the fibers and any smooth, invertible skew-symmetric bundle mapping $A \colon E \to E$ , there exists a unique smooth positive definite symmetric bundle mapping $B \colon E \to E$ that satisfies $B ^ { 2 } = - A ^ { 2 }$ and that commutes with A.

3. This exercise requires that you know something about characteristic classes.

(i) Show that $S ^ { 4 n }$ has no almost complex structure for any n. (Hint: What could the total Chern and Pontrijagin class of the tangent bundle be?)

(Using the Bott Periodicity Theorem, it can be shown that the characteristic class $c _ { n }$ of any complex bundle over $S ^ { 2 n }$ must be an integer multiple of $( n - 1 ) !$ v where $v \in H ^ { 2 n } ( S ^ { 2 n } )$ is a generator. It follows that, among the spheres, only $S ^ { 2 }$ and $S ^ { 6 }$ could have almost complex structures and, in fact, they both do. It is a long standing problem whether or not $S ^ { 6 }$ has a complex structure.)

(ii) Using the formulas for 4-manifolds developed in the Lecture, determine how many possibilities there are for the first Chern class $c _ { 1 } ( J )$ of an almost complex structure J on M where M a connected sum of 3 or 4 copies of $\mathbb { C P } ^ { 2 }$

4. Show that, if $\Omega _ { 0 }$ is a symplectic structure on a compact manifold M, then there is an open neighborhood U in $H ^ { 2 } ( M , \mathbb { R } )$ of $\left[ \Omega _ { 0 } \right]$ , such that, for all $u \in U$ , there is a symplectic structure $\Omega _ { u }$ on M with $\left[ \Omega _ { u } \right] = u$ . (Hint: Since M is compact, for any closed 2-form Υ, the 2-form $\Omega + t \Upsilon$ is non-degenerate for all sufficiently small t.)

5. Mimic the proof of Theorem 1 to prove another theorem of Moser: For any compact, connected, oriented manifold M, two volume forms $\mu _ { 0 }$ and $\mu _ { 1 }$ differ by an oriented diffeomorphism (i.e., there exists an orientation preserving diffeomorphism $\phi \colon M \to M$ that satisfies $\phi ^ { * } ( \mu _ { 1 } ) = \mu _ { 0 } )$ if and only if

$$
\int _ { M } \mu _ { 0 } = \int _ { M } \mu _ { 1 } .
$$

(This theorem is also true without the hypothesis of compactness, but the proof is slightly more delicate.)

6. Let M be a connected, smooth oriented 4-manifold and let $\mu \in \mathcal { A } ^ { 4 } ( M )$ be a volume form that satisfies $\textstyle \int _ { M } \mu = 1$ . (By the previous problem, any two such forms differ by an oriented diffeomorphism of M.) For any (smooth) $\Omega \in { \mathcal { A } } ^ { 2 } ( M )$ , define $* ( \Omega ^ { 2 } ) \in C ^ { \infty } ( M )$ by the equation

$$
\Omega ^ { 2 } = \ast ( \Omega ^ { 2 } ) \mu .
$$

Now, fix a cohomology class $u \in H _ { d R } ^ { 2 } ( M )$ satisfying $u ^ { 2 } = r [ \mu ]$ where $r \neq 0$ . Define the functional $\mathcal { F } \colon u  \mathbb { R }$

$$
\mathcal { F } ( \Omega ) = \int _ { M } \ast ( \Omega ^ { 2 } ) \Omega ^ { 2 } \qquad \mathrm { f o r } \ \Omega \in u .
$$

Show that any -critical 2-form $\Omega \in u$ is a symplectic form satisfying $* ( \Omega ^ { 2 } ) = r$ and that $\mathcal { F }$ has no critical values other than $r ^ { 2 }$ . Show also that $\mathcal { F } ( \Omega ) \geq r ^ { 2 }$ for all $\Omega \in u$

This motivates defining an invariant of the class u by

$$
{ \mathcal { T } } ( u ) = \operatorname* { i n f } _ { \Omega \in u } { \mathcal { F } } ( \Omega ) .
$$

Gromov has suggested (private communication) that perhaps $\mathcal { I } ( u ) = r ^ { 2 }$ for all $u ,$ even when the infimum is not attained.

7. Let $P \subset M$ be a closed submanifold and let $U \subset M$ be an open neighborhood of $P$ in M that can be retracted onto P , i.e., there exists a smooth map $R \colon U \times [ 0 , 1 ] \to U$ so that $R ( u , 1 ) = u$ for all $u \in U , R ( p , t ) = p$ for all $p \in P$ and $t \in [ 0 , 1 ]$ , and $R ( u , 0 )$ lies in P for all $u \in U$ . (Every closed submanifold of M has such a neighborhood.)

Show that if Φ is a closed k-form on U that vanishes at every point of P , then there exists a $( k - 1 )$ -form $\phi$ on U that vanishes on P and satisfies $d \phi = \Phi$ (Hint: Mimic Poincar´e’s Homotopy Argument: Let $\Upsilon = R ^ { * } ( \Phi )$ and set $\begin{array} { r } { v = \frac { \partial } { \partial t } \lrcorner \Upsilon } \end{array}$ . Then, using the fact that $\boldsymbol { v } ( \boldsymbol { u } , t )$ can be regarded as a $( k - 1 )$ -form at u for all t, define

$$
\phi ( u ) = \int _ { 0 } ^ { 1 } v ( u , t ) d t .
$$

Now verify that $\phi$ has the desired properties.)

8. Show that Theorem 2 implies Darboux’ Theorem. (Hint: Take P to be a point in a symplectic manifold M .)

9. This exercise assumes that you have done Exercise 5.10. Let $( M , \Omega )$ be a symplectic manifold. Show that the following description of the flux homomorphism is valid. Let p be an e-based path in $\mathsf { S p } ( \Omega )$ . Thus, $p \colon [ 0 , 1 ] \times M \to M$ satisfies $p _ { t } ^ { * } ( \Omega ) = \Omega$ for all $0 \leq t \leq 1$ . Show that $p ^ { * } ( \Omega ) = \Omega + \varphi \wedge d t$ for some 1-form ϕ on $[ 0 , 1 ] \times M$ . Let $\iota _ { t } \colon M \to [ 0 , 1 ] \times M$ be the “t-slice inclusion”: $\iota _ { t } ( m ) = ( t , m )$ , and set $\varphi _ { t } = \iota _ { t } ^ { * } ( \varphi )$

Show that $\varphi _ { t }$ is closed for all $0 \leq t \leq 1$ . Show that if we set

$$
\tilde { \Phi } ( p ) = \int _ { 0 } ^ { 1 } \varphi _ { t } d t ,
$$

then the cohomology class $[ \tilde { \Phi } ( p ) ] \in H _ { d R } ^ { 1 } ( M , \mathbb { R } )$ depends only on the homotopy class of $p$ and hence defines a map $\Phi { : \mathord { \mathrm { S p } } } ^ { 0 } ( \Omega ) \to H _ { d R } ^ { 1 } ( M , \mathbb { R } )$ . Verify that this map is the same as the flux homomorphism defined in Exercise 5.10.

Use this description to show that if $p$ is in the kernel of Φ, then p is homotopic to a path $p ^ { \prime }$ for which the forms $\varphi _ { t } ^ { \prime }$ are all exact. This shows that the kernel of Φ is actually connected.

10. The point of this exercise is to show that any symplectic vector bundle over a symplectic manifold $( M , \Omega )$ can occur as the symplectic normal bundle for some symplectic embedding M into some other symplectic manifold.

Let $( M , \Omega )$ be a symplectic manifold and let $\pi \colon E \to M$ be a symplectic vector bundle over M of rank 2n. (I.e., E comes equipped with a section B of $\Lambda ^ { 2 } ( E ^ { * } )$ that restricts to each fiber $E _ { m }$ to be a symplectic structure $B _ { m } . )$ Show that there exists a symplectic structure Ψ on an open neighborhood in E of the zero section of E that satisfies the condition that $\Psi _ { 0 _ { m } } = \Omega _ { m } + B _ { m }$ under the natural identification $T _ { 0 _ { m } } E = T _ { m } M \oplus E _ { m }$

(Hint: Choose a locally finite open cover $\mathfrak { U } = \{ U _ { \alpha } | \alpha \in A \}$ of M so that, if we define $E _ { \alpha } = \pi ^ { - 1 } ( U _ { \alpha } )$ , then there exists a symplectic trivialization $\tau _ { \alpha } \colon E _ { \alpha } \to \mathbb { R } ^ { 2 n }$ (where $\mathbb { R } ^ { 2 n }$ is given its standard symplectic structure $\Omega _ { 0 } = d x _ { i } { \wedge } d y ^ { i } )$ Now let $\{ \lambda _ { \alpha } | \alpha \in A \}$ be a partition of unity subordinate to the cover U. Show that the form

$$
\Psi = \pi ^ { * } ( \Omega ) + \sum _ { \alpha } d \big ( \lambda _ { \alpha } \tau _ { \alpha } ^ { * } ( x _ { i } d y ^ { i } ) \big )
$$

has the desired properties.)

11. Show that if E is a symplectic vector bundle over M and $L \subset E$ is a Lagrangian subbundle, then E is isomorphic to $L \oplus L ^ { * }$ as a symplectic bundle. (The symplectic bundle structure Υ on $L \oplus L ^ { * }$ is the one that, on each fiber satisfies

$$
\Upsilon \big ( ( v , \alpha ) , ( w , \beta ) \big ) = \alpha ( w ) - \beta ( v ) . \ \big )
$$

(Hint: First choose a complementary subbundle $F \subset E$ so that $E = L \oplus F$ . Show that $F$ is naturally isomorphic to $L ^ { * }$ abstractly by using the fact that the symplectic structure on E is non-degenerate. Then show that there exists a bundle map A: $F  L$ so that

$$
\tilde { F } = \{ v + A v \mid v \in F \}
$$

is also a Lagrangian subbundle of E that is complementary to L and isomorphic to $L ^ { * }$ via some bundle map α: $L ^ { * } \to { \tilde { F } }$ . Now show that id  α: ${ \cal L } \oplus { \cal L } ^ { * } \to { \cal L } \oplus \tilde { F } \simeq E$ is a symplectic bundle isomorphism.)

12. Action-Angle Coordinates. Proposition 4 can be used to show the existence of socalled action angle coordinates in the neighborhood of a compact level set of a completely integrable Hamiltonian system. (See Lecture 5). Here is how this goes: Let $( M ^ { 2 n } , \Omega )$ be a symplectic manifold and let $f = ( f ^ { 1 } , \dots , f ^ { n } ) \colon M \to \mathbb { R } ^ { n }$ be a smooth submersion with the property that the coordinate functions $f ^ { i }$ are in involution, i.e., $\{ f ^ { i } , f ^ { j } \} = 0$ . Suppose that, for some $c \in \mathbb { R } ^ { n }$ , the f -level set $M _ { c } = f ^ { - 1 } ( c )$ is compact. Replacing f by $f - c ,$ , we may assume that $c = 0$ , which we do from now on.

Show that $M _ { 0 } \subset M$ is a closed Lagrangian submanifold of M.

Use Proposition 4 to show that there is an open neighborhood B of $0 \in \mathbb { R } ^ { n }$ so that $\left( f ^ { - 1 } ( B ) , \Omega \right)$ is symplectomorphic to a neighborhood U of the zero section in $T ^ { * } M _ { 0 }$ (endowed with its standard symplectic structure) in such a way that, for each $b \in B$ , the submanifold $M _ { b } = f ^ { - 1 } ( b )$ is identified with the graph of a closed 1-form $\omega _ { b }$ on $M _ { 0 }$ . Show that it is possible to choose $b _ { 1 } , \ldots , b _ { n }$ in B so that the corresponding closed 1-forms $\omega _ { 1 } , \ldots , \omega _ { n }$ are linearly independent at every point of $M _ { 0 }$

Conclude that $M _ { 0 }$ is diffeomorphic to a torus $T = \mathbb { R } ^ { n } / \Lambda$ where $\Lambda \subset \mathbb { R } ^ { n }$ is a lattice, in such a way that the forms $\omega _ { i }$ become identified with $d \theta _ { i }$ where $\theta _ { i }$ are the corresponding linear coordinates on $\mathbb { R } ^ { n }$

Now prove that for any $b \in B$ , the 1-form $\omega _ { b }$ must be a linear combination of the $\omega _ { i }$ with constant coefficients. Thus, there are functions $a ^ { i }$ on $B \ \mathrm { s o }$ that $\omega _ { b } = a ^ { i } ( b ) \omega _ { i }$ . (Hint: Show that the coefficients must be invariant under the flows of the vector fields dual to the $\omega _ { i \cdot } )$

Conclude that, under the symplectic map identifying $M _ { B }$ with $U$ , the form Ω gets identified with $d a ^ { i } { \wedge } d \theta _ { i }$ . The functions $a ^ { i }$ and $\theta _ { i }$ are the so-called “action-angle coordinates”.

Extra Credit: Trace through the methods used to prove Proposition 4 and show that, in fact, the action-angle coordinates can be constructed using quadrature and “finite” operations.

## Lecture 7:

## Classical Reduction

In this section, we return to the study of group actions. This time, however, we will concentrate on group actions on symplectic manifolds that preserve the symplectic structure. Such actions happen to have quite interesting properties and moreover, turn out to have a wide variety of applications.

Symplectic Group Actions. First, the basic definition.

Definition 1: Let $( M , \Omega )$ be a symplectic manifold and let G be a Lie group. A left action $\lambda \colon G \times M \to M$ of G on M is a symplectic action if $\lambda _ { a } ^ { * } ( \Omega ) = \Omega$ for all $a \in G$

We have already encountered several examples:

Example: Lagrangian Symmetries. If G acts on a manifold M is such a way that it preserves a non-degenerate Lagrangian $L \colon T M \to \mathbb { R }$ , then, by construction, it preserves the symplectic 2-form dωL.

Example: Cotangent Actions. A left G-action λ: $G \times M \to M$ , induces an action $\tilde { \lambda }$ of G on $T ^ { * } M$ . Namely, for each $a \in G$ , the diffeomorphism $\lambda _ { a } \colon M \to M$ induces a diffeomorphism $\tilde { \lambda } _ { a } \colon T ^ { * } M \to T ^ { * } M$ Since the natural symplectic structure on $T ^ { * } M$ is invariant under diffeomorphisms, it follows that $\tilde { \lambda }$ is a symplectic action.

Example: Coadjoint Orbits. As we saw in Lecture 5, for every $\xi \in { \mathfrak { g } } ^ { * }$ , the coadjoint orbit $G \cdot \xi$ carries a natural G-invariant symplectic structure $\Omega _ { \xi }$ . Thus, the left action of G on $G \cdot \xi$ is symplectic.

Example: Circle Actions on $\mathbb { C } ^ { n }$ . Let $z ^ { 1 } , \ldots , z ^ { n }$ be linear complex coordinates on $\mathbb { C } ^ { n }$ and let this vector space be endowed with the symplectic structure

$$
\begin{array} { c } { \Omega = \frac { i } { 2 } \big ( d z ^ { 1 } \wedge d \bar { z } ^ { 1 } + \cdot \cdot \cdot + d z ^ { n } \wedge d \bar { z } ^ { n } \big ) } \\ { = d x ^ { 1 } \wedge d y ^ { 1 } + \cdot \cdot \cdot + d x ^ { n } \wedge d y ^ { n } } \end{array}
$$

where $z ^ { k } = x ^ { k } + i y ^ { k }$ . Then for any integers $\left( k _ { 1 } , \ldots , k _ { n } \right)$ , we can define an action of $S ^ { 1 }$ on $\mathbb { C } ^ { n }$ by the formula

$$
e ^ { i \theta } \cdot \left( \begin{array} { c } { { z ^ { 1 } } } \\ { { \vdots } } \\ { { z ^ { n } } } \end{array} \right) = \left( \begin{array} { c } { { e ^ { i k _ { 1 } \theta } z ^ { 1 } } } \\ { { \vdots } } \\ { { e ^ { i k _ { n } \theta } z ^ { n } } } \end{array} \right)
$$

The reader can easily check that this defines a symplectic circle action on $\mathbb { C } ^ { n }$

Generally what we will be interested in is the following: Y will be a Hamiltonian vector field on a symplectic manifold (M, Ω) and G will act symplectically on M as a group of symmetries of the flow of Y . We want to understand how to use the action of G to “reduce” the problem of integrating the flow of Y .

In Lecture 3, we saw that when Y was the Euler-Lagrange vector field associated to a non-degenerate Lagrangian L, then the infinitesimal generators of symmetries of L could be used to generate conserved quantities for the flow of Y . We want to extend this process (as far as is reasonable) to the general case.

For the rest of the lecture, I will assume that G is a Lie group with a symplectic action λ on a connected symplectic manifold (M, Ω).

Since λ is symplectic, it follows that the mapping $\lambda _ { * } \colon { \mathfrak { g } } \to { \mathfrak { X } } ( M )$ actually has image in $s { \mathfrak { p } } ( \Omega )$ , the algebra of symplectic vector fields on M. As we saw in Lecture $3 , \lambda _ { * }$ is an anti-homomorphism, i.e., $\bar { \lambda } _ { * } \bigl ( [ x , y ] \bigr ) = - \bigl [ \lambda _ { * } ( x ) , \lambda _ { * } ( y ) \bigr ]$ . Since, as we saw in Lecture $5 , \ [ s \mathfrak { p } ( \Omega ) , s \mathfrak { p } ( \Omega ) ] \subset \mathfrak { h } ( \Omega )$ , it follows that $\lambda _ { * } \bigl ( [ { \mathfrak { g } } , { \mathfrak { g } } ] \bigr ) \subset { \mathfrak { h } } ( \Omega )$ Thus, $H _ { \lambda } \colon { \mathfrak { g } } \to H _ { d R } ^ { 1 } ( M , \mathbb { R } )$ defined by $H _ { \lambda } ( x ) = \lceil \lambda _ { * } ( x ) \lrcorner \Omega \rceil$ is a homomorphism of Lie algebras with kernel containing the commutator subalgebra [g, g].

The map $H _ { \lambda }$ is the obstruction to finding a Hamiltonian function associated to each infinitesimal symmetry $\lambda _ { * } ( x )$ since $H _ { \lambda } ( x ) = 0$ if and only if $\lambda _ { * } ( x ) \lrcorner \Omega = - d f$ for some $f \in C ^ { \infty } ( M )$ .

Definition 2: A symplectic action $\lambda \colon G \times M \to M$ is said to be Hamiltonian if $H _ { \lambda } = 0$ i.e., if $\lambda _ { * } ( { \mathfrak { g } } ) \subset { \mathfrak { h } } ( \Omega )$

There are a few particularly interesting cases where the obstruction $H _ { \lambda }$ must vanish:

If $H _ { d R } ^ { 1 } ( M , \mathbb { R } ) = 0$ . In particular, if M is simply connected.

• If g is perfect, ${ \mathfrak { i . e . , ~ } } [ { \mathfrak { g } } , { \mathfrak { g } } ] = { \mathfrak { g } }$ For example this happens whenever the Killing form on g is non-degenerate (this is the first Whitehead Lemma, see Exercise 3). However, this is not the only case: For example, if G is the group of rigid motions in $\mathbb { R } ^ { n }$ for $n \geq 3$ , then g has this property, even though its Killing form is degenerate.

If there exists a 1-form ω on M that is invariant under G and satisfies $\Omega = d \omega$ (This is the case of symmetries of a Lagrangian.) To see this, note that if X is a vector field on M that preserves ω, then

$$
0 = \mathfrak { L } _ { X } \omega = d ( X \lrcorner \omega ) + X \lrcorner \Omega ,
$$

so $X \lrcorner \Omega$ is exact.

For a Hamiltonian action λ, every infinitesimal symmetry $\lambda _ { * } ( x )$ has a Hamiltonian function $f _ { x } \in C ^ { \infty }$ . However, the choice of $f _ { x }$ is not unique since we can add any constant to $f _ { x }$ without changing its Hamiltonian vector field. This non-uniqueness causes some problems in the theory we wish to develop.

To see why, suppose that we choose a (linear) lifting $\rho \colon { \mathfrak { g } } \to C ^ { \infty } ( M ) \ { \mathrm { o f } } - \lambda _ { * } \colon { \mathfrak { g } } \to { \mathrm { h } } ( \Omega )$ (The choice of −λ∗ instead of $\lambda _ { * }$ was made to get rid of the annoying sign in the formula for the bracket.)

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c } & & & { \mathfrak { g } } & & & & & & & & & & & & & & \\ { 0 } & { \to } & { \mathbb { R } } & { \to } & { \operatorname { \mathcal { C } } ^ { \infty } ( M ) } & { \to } & { \mathfrak { h } ( \Omega ) } & { \to } & { 0 } & & & & & & & & & \end{array}
$$

Thus, for every $x \in { \mathfrak { g } }$ , we have $\lambda _ { * } ( x ) \lrcorner \Omega = d \big ( \rho ( x ) \big )$ . A short calculation (see the Exercises) now shows that $\{ \rho ( x ) , \rho ( y ) \}$ is a Hamiltonian function for $- \lambda _ { * } ( [ x , y ] )$ , i.e., that

$$
\lambda _ { * } \big ( [ x , y ] \big ) \lrcorner \Omega = d \big ( \{ \rho ( x ) , \rho ( y ) \} \big ) .
$$

In particular, it follows (since M is connected) that there must be a skew-symmetric bilinear map $c _ { \rho } \colon { \mathfrak { g } } \times { \mathfrak { g } } \to \mathbb { R }$ so that

$$
\{ \rho ( x ) , \rho ( y ) \} = \rho \bigl ( [ x , y ] \bigr ) + c _ { \rho } ( x , y ) .
$$

An application of the Jacobi identity implies that the map $c _ { \rho }$ satisfies the condition

$$
c _ { \rho } ( [ x , y ] , z ) + c _ { \rho } ( [ y , z ] , x ) + c _ { \rho } ( [ z , x ] , y ) = 0 \quad { \mathrm { f o r ~ a l l ~ } } x , y , z \in \mathfrak { g } .
$$

This condition is known as the 2-cocycle condition for $c _ { \rho }$ regarded as an element of $A ^ { 2 } ( { \mathfrak { g } } ) =$ $\Lambda ^ { 2 } ( { \mathfrak { g } } ^ { * } )$ . (See Exercise 3 for an explanation of this terminology.)

For purposes of simplicity, it would be nice if we could choose $\rho$ so that $c _ { \rho }$ were identically zero. In order to see whether this is possible, let us choose another linear map ${ \tilde { \rho } } \colon { \mathfrak { g } } \to C ^ { \infty } ( M )$ that satisfies $\tilde { \rho } ( x ) = \rho ( x ) + \xi ( x )$ where $\xi \colon { \mathfrak { g } }  \mathbb { R }$ is any linear map. Every possible lifting of $- \lambda _ { * }$ is clearly of this form for some $\xi$ . Now we compute that

$$
\begin{array} { c } { { \left\{ \tilde { \rho } ( x ) , \tilde { \rho } ( y ) \right\} = \left\{ \rho ( x ) , \rho ( y ) \right\} = \rho \big ( [ x , y ] \big ) + c _ { \rho } ( x , y ) } } \\ { { = \tilde { \rho } \big ( [ x , y ] \big ) + c _ { \rho } ( x , y ) - \xi \big ( [ x , y ] \big ) . } } \end{array}
$$

Thus, $c _ { \tilde { \rho } } ( x , y ) = c _ { \rho } ( x , y ) - \xi \big ( [ x , y ] \big )$ . Thus, in order to be able to choose $\tilde { \rho }$ so that $c _ { \tilde { \rho } } = 0$ we see that there must exist $\mathfrak { a } \ \xi \in \mathfrak { g } ^ { * }$ so that $c _ { \rho } = - \delta \xi$ where $\delta \xi$ is the skew-symmetric bilinear map on g that satisfies $\delta \xi ( x , y ) = - \xi { \big ( } [ x , y ] { \big ) }$ (see the Exercises for an explanation of this notation). This is known as the 2-coboundary condition.

There are several important cases where we can assure that $c _ { \rho }$ can be written in the form $- \delta \xi$ . Among them are:

• If M is compact, then the sequence

$$
0 \to \mathbb { R } \to C ^ { \infty } ( M ) \to { \mathsf { H } } ( \Omega ) \to 0
$$

splits: If we let $C _ { 0 } ^ { \infty } ( M , \Omega ) \subset C ^ { \infty } ( M )$ denote the space of functions f for which $\textstyle \int _ { M } f \ d \Omega ^ { n } =$ 0, then these functions are closed under Poisson bracket (see Exercise 5.6 for a hint as to why this is true) and we have a splitting of Lie algebras $C ^ { \infty } ( M ) = \mathbb { R } \oplus C _ { 0 } ^ { \infty } ( M , \Omega )$ . Now just choose the unique $\rho$ so that it takes values in $C _ { 0 } ^ { \infty } ( M , \Omega )$ . This will clearly have $c _ { \rho } = 0$

• If g has the property that every 2-cocycle for g is actually a 2-coboundary. This happens, for example, if the Killing form of g is non-degenerate (this is the second Whitehead Lemma, see Exercise 3), though it can also happen for other Lie algebras. For example, for the non-abelian Lie algebra of dimension 2, it is easy to see that every 2-cocycle is a 2-coboundary.If there is a 1-form $\omega$ on $M$ that is preserved by the $G$ action and satisfies $d \omega = \Omega$ (This is true in the case of symmetries of a Lagrangian.) In this case, we can merely take $\rho ( x ) = - \omega \big ( \lambda _ { * } ( x ) \big )$ . I leave as an exercise for the reader to check that this works.

Definition 3: A Hamiltonian action $\lambda \colon G \times M \to M$ is said to be a Poisson action if there exists a lifting $\rho$ with $c _ { \rho } = 0$ .

Henceforth in this Lecture, I am only going to consider Poisson actions. By my previous remarks, this case includes all of the Lagrangians with symmetries, but it also includes many others.

I will assume that, in addition to having a Poisson action $\lambda \colon G \times M \to M$ specified, we have chosen a lifting $\rho \colon { \mathfrak { g } }  C ^ { \infty } ( M )$ of $- \lambda _ { * }$ that satisfies $\left\{ \rho ( x ) , \rho ( y ) \right\} = \rho { \bigl ( } [ x , y ] { \bigr ) }$ for all $x , y \in { \mathfrak { g } }$ . Note that such a $\rho$ is unique up to replacement by $\tilde { \rho } = \rho + \xi$ where $\xi : { \mathfrak { g } }  \mathbb { R }$ 4 satisfies $\delta \xi = 0$ . Such $\xi ~ ( \mathrm { i f } ~ $ any non-zero ones exist) are fixed under the co-adjoint action of the identity component of $G$

The Momentum Mapping. We are now ready to make one of the most important constructions in the theory.

Definition 4: The momentum mapping associated to $\lambda$ and $\rho$ is the mapping $\mu \colon M \to { \mathfrak { g } } ^ { * }$ that satisfies

$$
\mu ( m ) ( y ) = \rho ( y ) ( m ) .
$$

Note that, for fixed $m \in M$ , the assignment $y \mapsto \rho ( y ) ( m )$ is a linear map from g to R, so the definition makes sense.

It is worth pausing to consider why this mapping is called the momentum mapping. The reader should calculate this mapping in the case of a free particle or a rigid body moving in space. In either case, the Lagrangian is invariant under the action of the group $G$ of rigid motions of space. If $y \in { \mathfrak { g } }$ corresponds to a translation, then $\rho ( y )$ gives the function on $T \mathbb { R } ^ { 3 }$ that evaluates at each point (i.e., each position-plus-velocity) to be the linear momentum in the direction of translation. If $y$ corresponds to rotation about a fixed axis, then $\rho ( y )$ turns out to be the angular momentum of the body about that axis.

One important reason for studying the momentum mapping is the following formulation of the classical conservation of momentum theorems:

Proposition 1: If f is a function on M that is invariant under the action of $G _ { i }$ , then $\mu$ is constant on the integral curves of the Hamiltonian vector field $X _ { f }$ 

In particular, $\mu$ provides conserved quantities for any G-invariant Hamiltonian.

The main result about the momentum mapping is the following one.

Theorem 1: If G is connected, then the momentum mapping µ: $M \to { \mathfrak { g } } ^ { * }$ is G-equivariant.

Proof: Recall that the coadjoint action of $G$ on ${ \mathfrak { g } } ^ { * }$ is defined by ${ \operatorname { A d } } ^ { * } ( g ) ( \xi ) ( x ) ~ =$ $\xi \big ( \mathrm { A d } ( g ^ { - 1 } ) \ d x \big )$ . The condition that $\mu$ be G-equivariant, i.e., that $\mu ( g \cdot m ) = \mathrm { A d } ^ { * } ( g ) ( \mu ( m ) )$ for all $m \in M$ and $g \in G$ , is thus seen to be equivalent to the condition that

$$
\rho \bigl ( \mathrm { A d } ( g ^ { - 1 } ) y \bigr ) ( m ) = \rho ( y ) ( g \cdot m )
$$

for all $m \in M , g \in G $ , and $y \in { \mathfrak { g } }$ . This is the identity I shall prove.

Since G is connected and since each side of the above equation represents a $G \mathrm { - a c t i o n }$ , if we prove that the above formula holds for $g$ of the form $g = e ^ { t x }$ for any $x \in { \mathfrak { g } }$ and any $t \in \mathbb { R }$ , the formula for general g will follow. Thus, we want to prove that

$$
\rho \bigl ( \mathrm { A d } ( e ^ { - t x } ) y \bigr ) ( m ) = \rho ( y ) ( e ^ { t x } \cdot m )
$$

for all t. Since this latter equation holds at $t = 0$ , it is enough to show that both sides have the same derivative with respect to t.

Now the derivative of the right hand side of the formula is

$$
\begin{array} { r l } & { d \bigl ( \rho ( y ) \bigr ) \bigl ( \lambda _ { * } ( x ) ( e ^ { t x } \cdot m ) \bigr ) = \Omega \bigl ( \lambda _ { * } ( y ) ( e ^ { t x } \cdot m ) , \lambda _ { * } ( x ) ( e ^ { t x } \cdot m ) \bigr ) } \\ & { \qquad = \Omega \bigl ( \lambda _ { * } \bigl ( \mathrm { A d } ( e ^ { - t x } ) y ) ( m ) , \lambda _ { * } \bigl ( \mathrm { A d } ( e ^ { - t x } ) x \bigr ) ( m ) \bigr ) \bigr ) } \\ & { \qquad = \Omega \bigl ( \lambda _ { * } \bigl ( \mathrm { A d } ( e ^ { - t x } ) y ) ( m ) , \lambda _ { * } ( x ) ( m ) \bigr ) } \end{array}
$$

where, to verify the second equality we have used the identity

$$
\lambda _ { a } ^ { \prime } \bigl ( \lambda _ { * } ( y ) ( m ) \bigr ) = \lambda _ { * } \bigl ( \mathrm { A d } ( a ) y \bigr ) ( a \cdot m )
$$

and the fact that Ω is G-invariant.

On the other hand, the derivative of the left hand side of the formula is clearly

$$
\begin{array} { r l } & { \rho \big ( [ - x , \mathrm { A d } ( e ^ { - t x } ) y ] \big ) ( m ) = - \big \{ \rho ( x ) , \rho \big ( \mathrm { A d } ( e ^ { - t x } ) y \big ) \big \} ( m ) } \\ & { \qquad = \Omega \big ( \lambda _ { * } \big ( \mathrm { A d } ( e ^ { - t x } ) y \big ) ( m ) , \lambda _ { * } ( x ) ( m ) \big ) } \end{array}
$$

so we are done. (Note that I have used my assumption that $c _ { \rho } = 0 ! )$

Example: Left-Invariant Metrics on Lie Groups. Let G be a Lie group and let $Q \colon { \mathfrak { g } } $ R be a non-degenerate quadratic form with associated inner product $\langle , \rangle _ { Q }$ . Let $L \colon T G \to \mathbb { R }$ be the Lagrangian

$$
\begin{array} { r } { L = \frac { 1 } { 2 } Q ( \omega ) } \end{array}
$$

where $\omega \colon T G \to { \mathfrak { g } }$ is, as usual, the canonical left-invariant form on G. Then, using the basepoint map $\pi \colon T G \to G .$ we compute that

$$
\omega _ { L } = \left. \omega , \pi ^ { * } ( \omega ) \right. _ { Q } .
$$

As we saw in Lecture 3, the assumption that $Q$ is non-degenerate implies that $d \omega _ { L }$ is a symplectic form on T G. Now, since the flow of a right-invariant vector field $Y _ { x }$ is multiplication on the left by $e ^ { t x }$ , it follows that, for this action, we may define

$$
\rho ( x ) = - \omega _ { L } \big ( Y _ { x } ^ { \prime } \big ) = - \big < \omega , \omega \big ( Y _ { x } \big ) \big > _ { Q } = - \big < \omega , \mathrm { A d } ( g ^ { - 1 } ) x \big > _ { Q }
$$

(where $g \colon T G \to G$ is merely a more descriptive name for the base point map than $\pi )$

Now, there is an isomorphism $\tau _ { Q } \colon      { \mathfrak { g } } \ \to \ { \mathfrak { g } } ^ { * }$ , called transpose with respect to $Q$ that satisfies $\tau _ { Q } ( x ) ( y ) = \langle x , y \rangle _ { Q }$ for all x, $y \in { \mathfrak { g } }$ . In terms of $\tau _ { Q }$ , we can express the momentum mapping as

$$
\mu ( v ) = - \mathrm { A d } ^ { * } ( g ) \bigl ( \tau _ { Q } ( \omega ( v ) ) \bigr )
$$

for all $v \in T G$ . Note that $\mu$ is G-equivariant, as promised by the theorem.

According to the Proposition 1, the function $\mu$ is a conserved quantity for the solutions of the Euler-Lagrange equations. In one of the Exercises, you are asked to show how this information can be used to help solve the Euler-Lagrange equations for the L-critical curves.

Example: Coadjoint Orbits. Let G be a Lie group and consider $\xi \in { \mathfrak { g } } ^ { * }$ with stabilizer subgroup $G _ { \xi } \subset G$ . The orbit $G \cdot \xi \subset { \mathfrak { g } } ^ { * }$ is canonically identified with $G / G _ { \xi }$ ( identify $a \cdot \xi$ with $a G _ { \xi } )$ and we have seen that there is a canonical G-invariant symplectic form $\Omega _ { \xi }$ on $G / G _ { \xi }$ that satisfies $\pi _ { \xi } ^ { * } ( \Omega _ { \xi } ) = d \omega _ { \xi }$ where $\pi _ { \xi } : G \to G / G _ { \xi }$ is the coset projection, ω is the tautological left-invariant 1-form on $G ,$ , and $\omega _ { \xi } = \xi ( \omega )$

Recall also that, for each $x \in { \mathfrak { g } }$ , the right-invariant vector field $Y _ { x }$ on G is defined so that $Y _ { x } ( e ) = x \in { \mathfrak { g } }$ . Then the vector field $\lambda _ { * } ( x )$ on $G / G _ { \xi }$ is πξ-related to $Y _ { x }$ , so

$$
\pi _ { \xi } ^ { * } \left( \lambda _ { * } ( x ) \lrcorner \Omega _ { \xi } \right) = Y _ { x } \lrcorner d \omega _ { \xi } = d \bigl ( - \omega _ { \xi } ( Y _ { x } ) \bigr ) .
$$

(This last equality follows because $\omega _ { \xi }$ , being left-invariant, is invariant under the flow of $Y _ { x \cdot } )$ Now, the value of the function $\omega _ { \xi } ( Y _ { x } )$ at $a \in G$ is

$$
\omega _ { \xi } ( Y _ { x } ) ( a ) = \xi { \big ( } \omega ( Y _ { x } ( a ) ) { \big ) } = \xi { \big ( } \operatorname { A d } ( a ^ { - 1 } ) ( x ) { \big ) } = \operatorname { A d } ^ { * } ( a ) ( \xi ) ( x ) = ( a \cdot \xi ) ( x ) .
$$

Thus, it follows that the natural left action of G on $G \cdot \xi$ is Poisson, with momentum mapping $\mu : G { \cdot } \xi \to { \mathfrak { g } } ^ { * }$ given by

$$
\mu ( a \cdot \xi ) = - a \cdot \xi .
$$

(Note: some authors do not have a minus sign here, but that is because their $\Omega _ { \xi }$ is the negative of ours.)

Reduction. I now want to discuss a method of taking quotients by group actions in the symplectic category. Now, when a Lie group $G$ acts symplectically on the left on a symplectic manifold M , it is not generally true that the space of orbits $G \backslash M$ can be given a symplectic structure, even when this orbit space can be given the structure of a smooth manifold (for example, the quotient need not be even dimensional).

However, when the action is Poisson, there is a natural method of breaking the orbit space $G \backslash M$ into a union of symplectic submanifolds provided that certain regularity criteria are met. The procedure I will describe is known as symplectic reduction. It is due, in its modern form, to Marsden and Weinstein (see [GS 2]).

The idea is simple: If $\mu \colon M \to { \mathfrak { g } } ^ { * }$ is the momentum mapping, then the G-equivariance of $\mu$ implies that there is a well-defined set map

$$
{ \bar { \mu } } \colon G \backslash M \to G \backslash { \mathfrak { g } } ^ { * } .
$$

The theorem we are about to prove asserts that, provided certain regularity criteria are met, the subsets $M _ { \xi } = \bar { \mu } ^ { - 1 } ( \bar { \xi } ) \subset G \backslash M$ are symplectic manifolds in a natural way.

Definition 4: Let $f \colon X \to Y$ be a smooth map. A point $y \in Y$ is a clean value of $f$ if the set $f ^ { - 1 } ( y ) \subset X$ is a smooth submanifold of X and, moreover, if $T _ { x } f ^ { - 1 } ( y ) = \ker f ^ { \prime } ( x )$ for each $x \in f ^ { - 1 } ( y )$

Note: While every regular value of f is clean, not every clean value of f need be regular. The concept of cleanliness is very frequently encountered in the reduction theory we are about to develop.

Theorem 2: Let $\lambda \colon G \times M \to M$ be a Poisson action on the symplectic manifold M. Let $\mu \colon M \to { \mathfrak { g } } ^ { * }$ be a momentum mapping for λ. Suppose that, $\xi \in { \mathfrak { g } } ^ { * }$ is a clean value of $\mu$ Then $G _ { \xi }$ acts smoothly on $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ . Suppose further that the space of $G _ { \xi } { \mathrm { - } } O r b i t s$ in $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ , say, $M _ { \xi } = G _ { \xi } \backslash \left( \mu ^ { - 1 } ( \xi ) \right)$ , can be given the structure of a smooth manifold in such a way that the quotient mapping $\pi _ { \xi } \colon \mu ^ { - 1 } ( \xi ) \to M _ { \xi }$ is a smooth submersion. Then there exists a symplectic structure $\Omega _ { \xi }$ on $M _ { \xi }$ that is defined by the condition that $\pi _ { \xi } ^ { * } ( \Omega _ { \xi } )$ be the pullback of Ω to $\mu ^ { - 1 } ( \boldsymbol { \xi } )$

Proof: Since $\xi$ is a clean value of $\mu ,$ we know that $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ is a smooth submanifold of $M$ By the G-equivariance of the momentum mapping, the stabilizer subgroup $G _ { \xi } \subset G$ acts on M preserving the submanifold $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ . The restricted action of $G _ { \xi }$ on $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ is easily seen to be smooth.

Now, I claim that, for each $m \in \mu ^ { - 1 } ( \xi )$ , the Ω-complementary subspace to $T _ { m } \bigl ( \mu ^ { - 1 } ( \xi ) \bigr )$ is the space $T _ { m } ( G \cdot m )$ , i.e., the tangent to the G-orbit through $m$ . To see this, first note that the space $T _ { m } ( G \cdot m )$ is spanned by the values at m assumed by the vector fields $\lambda _ { * } ( x )$ for $x \ \in \ { \mathfrak { g } }$ . Thus, a vector $v \in T _ { m } M$ lies in the Ω-complementary space of $T _ { m } ( G \cdot m )$ if and only if v satisfies $\Omega \big ( \lambda _ { * } ( x ) ( m ) , v \big ) \ = \ 0$ for all $x \in { \mathfrak { g } }$ . Since, by definition, $\Omega \big ( \lambda _ { * } ( x ) ( m ) , v \big ) = d \big ( \rho ( x ) \big ) ( v )$ , it follows that this condition on v is equivalent to the condition that v lie in ker $\mu ^ { \prime } ( m )$ . However, since $\xi$ is a clean value of $\mu ,$ we have ker $\mu ^ { \prime } ( m ) = T _ { m } { \big ( } \mu ^ { - 1 } ( \xi ) { \big ) }$ , as claimed.

Now, the G-equivariance of $\mu$ implies that $\mu ^ { - 1 } ( \xi ) \cap \left( G \cdot m \right) = G _ { \xi } \cdot m$ for all $m \in \mu ^ { - 1 } ( \xi )$ In particular, $T _ { m } \big ( G _ { \xi } { \cdot } m \big ) \subseteq T _ { m } \big ( \mu ^ { - 1 } ( \xi ) \big ) \cap T _ { m } \big ( G { \cdot } m \big )$ . To demonstrate the reverse inclusion, suppose that v lies in both $T _ { m } \bigl ( \mu ^ { - 1 } ( \xi ) \bigr )$ and $T _ { m } \left( G \cdot m \right)$ . Then $v = \lambda _ { * } ( x ) ( m )$ for some $x \in { \mathfrak { g } }$ , and, by the G-equivariance of the momentum mapping and the assumption that $\xi$ is clean (so that $T _ { m } \bigl ( \mu ^ { - 1 } ( \xi ) \bigr ) = \ker \mu ^ { \prime } ( m ) \bigr )$ we have

$$
0 = \mu ^ { \prime } ( m ) ( v ) = \mu ^ { \prime } ( m ) { \bigl ( } \lambda _ { * } ( x ) ( m ) { \bigr ) } = { \bigl ( } { \mathrm { A d } } ^ { * } { \bigr ) } _ { * } ( x ) ( \mu ( m ) ) = { \bigl ( } { \mathrm { A d } } ^ { * } { \bigr ) } _ { * } ( x ) ( \xi )
$$

so that x must lie in ${ \mathfrak { g } } _ { \xi }$ . Consequently, $v = \lambda _ { * } ( x ) ( m )$ is tangent to the orbit $G _ { \xi } \cdot m$ and thus,

$$
T _ { m } { \big ( } \mu ^ { - 1 } ( \xi ) { \big ) } \cap T _ { m } ( G \cdot m ) = \ker \mu ^ { \prime } ( m ) \cap T _ { m } { \big ( } G \cdot m { \big ) } = T _ { m } { \big ( } G _ { \xi } \cdot m { \big ) } .
$$

As a result, since the Ω-complementary spaces $T _ { m } \bigl ( \mu ^ { - 1 } ( \xi ) \bigr )$ and $T _ { m } \left( G \cdot m \right)$ intersect in the tangents to the $G _ { \xi ^ { - } } \mathrm { o r b i t s }$ , it follows that if $\tilde { \Omega } _ { \xi }$ denotes the pullback of Ω to $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ , then the null space of $\tilde { \Omega } _ { \xi }$ at m is precisely $T _ { m } \mathopen { } \mathclose \bgroup \left( G _ { \xi } \cdot m \aftergroup \egroup \right)$

Finally, let us assume, as in the theorem, that there is a smooth manifold structure on the orbit space $M _ { \xi } = G _ { \xi } \backslash \mu ^ { - 1 } ( \xi )$ so that the orbit space projection $\pi _ { \xi } \colon \mu ^ { - 1 } ( \xi ) \to M _ { \xi }$ is a smooth submersion. Since $\tilde { \Omega } _ { \xi }$ is clearly $G _ { \xi }$ invariant and closed and moreover, since its null space at each point of M is precisely the tangent space to the fibers of $\pi _ { \xi }$ , it follows that there exists a unique “push down” 2-form $\Omega _ { \xi }$ on $M _ { \xi }$ as described in the statement of the theorem. That $\Omega _ { \xi }$ is closed and non-degenerate is now immediate. 

The point of Theorem 2 is that, even though the quotient of a symplectic manifold by a symplectic group action is not, in general, a symplectic manifold, there is a way to produce a family of symplectic quotients parametrized by the elements of the space ${ \mathfrak { g } } ^ { * }$ The quotients $M _ { \xi }$ often turn out to be quite interesting, even when the original symplectic manifold M is very simple.

Before I pass on to the examples, let me make a few comments about the hypotheses in Theorem 2.

First, there will always be clean values $\xi$ of $\mu$ for which $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ is not empty (even when there are no such regular values). This follows because, if we look at the closed subset $D _ { \mu } \subset M$ consisting of points m where $\mu ^ { \prime } ( m )$ does not reach its maximum rank, then $\mu ( D _ { \mu } )$ can be shown (by a sort of Sard’s Theorem argument) to be a proper subset of $\mu ( M )$ . Meanwhile, it is not hard to show that any element $\xi \in \mu ( M )$ that does not lie in $\mu ( D _ { \mu } )$ is clean.

Second, it quite frequently does happen that the $G _ { \xi } .$ -orbit space $M _ { \xi }$ has a manifold structure for which $\pi _ { \xi }$ is a submersion. This can be guaranteed by various hypotheses that are often met with in practice. For example, if $G _ { \xi }$ is compact and acts freely on $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ then $M _ { \xi }$ will be a manifold. (More generally, if the orbits $G _ { \xi }$ ·m are compact and all of the stabilizer subgroups $G _ { m } \subset G _ { \xi }$ are conjugate in $G _ { \xi }$ , then $M _ { \xi }$ will have a manifold structure of the required kind.)

Weaker hypotheses also work. Basically, one needs to know that, at every point m of $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ , there is a smooth slice to the action of $G _ { \xi } , \mathrm { i . e . }$ , a smoothly embedded disk D in $\mu ^ { - 1 } ( \xi )$ that passes through m and intersects each $G _ { \xi ^ { - } } \mathrm { o r b i t }$ in $G _ { \xi } \cdot D$ transversely and in exactly one point. (Compare the construction of a smooth structure on each G-orbit in Theorem 1 of Lecture 3.)

Even when there is not a slice around each point of $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ , there is very often a nearslice, i.e., a smoothly embedded disk D in $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ that passes through m and intersects each $G _ { \xi ^ { - } } \mathrm { o r b i t }$ in $G _ { \xi } \cdot D$ transversely and in a finite number of points. In this case, the quotient space $M _ { \xi }$ inherits the structure of a symplectic orbifold, and these ‘generalized manifolds’ have turned out to be quite useful.

Finally, it is worth computing the dimension of $M _ { \xi }$ when it does turn out to be a manifold. Let $G _ { m } \subset G$ be the stabilizer of $m \in \mu ^ { - 1 } ( \xi )$ . I leave as an exercise for the reader to check that

$$
\begin{array} { r l } & { \dim \ M _ { \xi } = \dim \ M - \dim \ G - \dim \ G _ { \xi } + 2 \dim \ G _ { m } } \\ & { \qquad \quad = \dim \ M - 2 \dim \ G / G _ { m } + \dim \ G / G _ { \xi } . } \end{array}
$$

Since we will see so many examples in the next Lecture, I will content myself with only mentioning two here:

Let $M = T ^ { * } G$ and let G act on $T ^ { * } G$ on the left in the obvious way. Then the reader can easily check that, for each $x \in { \mathfrak { g } }$ , we have $\rho ( x ) ( \alpha ) = \alpha { \big ( } Y _ { x } ( a ) { \big ) }$ for all $\alpha \in T _ { a } ^ { * } G$ where, as usual, $Y _ { x }$ denotes the right invariant vector field on G whose value at e is $x \in { \mathfrak { g } }$ g. Hence, $\mu \colon T ^ { * } G \to { \mathfrak { g } } ^ { * }$ is given by $\mu ( \alpha ) = R _ { \pi ( \alpha ) } ^ { * } ( \alpha )$

Consequently, $\mu ^ { - 1 } ( \xi ) \subset T ^ { * } G$ is merely the graph in $T ^ { * } G$ of the left-invariant 1-form $\omega _ { \xi } \ \left( \mathrm { i . e . } \right.$ , the left-invariant 1-form whose value at $e { \mathrm { ~ i s ~ } } \xi \in { \mathfrak { g } } ^ { * } )$ Thus, we can use $\omega _ { \xi }$ as a section of $T ^ { * } G$ to pull back Ω (the canonical symplectic form on $T ^ { * } G$ , which is clearly G-invariant) to get the 2-form $d \omega _ { \xi }$ on $G .$ . As we already saw in Lecture 5, and is now borne out by Theorem 2, the null space of dωξ at any point $a \in G$ is $T _ { a } a G _ { \xi }$ , the quotient by $G _ { \xi }$ is merely the coadjoint orbit $G / G _ { \xi }$ , and the symplectic structure $\Omega _ { \xi }$ is just the one we already constructed.

Note, by the way, that every value of $\mu$ is clean in this example (in fact, they are all regular), even though the dimensions of the quotients $G / G _ { \xi }$ vary with $\xi .$

• Let $G = \mathrm { S O ( 3 ) }$ act on $\mathbb { R } ^ { 6 } = T ^ { * } \mathbb { R } ^ { 3 }$ by the extension of rotation about the origin in $\mathbb { R } ^ { 3 }$ . Then, in standard coordinates $( x , y )$ (where $x , y \in \mathbb { R } ^ { 3 } )$ , the action is simply $g \cdot ( x , y ) =$ $( g x , g y )$ , and the symplectic form is $\Omega = d x \cdot d y = { ^ { t } d x \wedge d y }$

We can identify ${ \mathfrak { s o } } ( 3 ) ^ { * }$ with $\mathfrak { s o } ( 3 )$ itself by interpreting $a \in { \mathfrak { s o } } ( 3 )$ as the linear functional $b \mapsto - \mathrm { t r } ( a b )$ . It is easy to see that the co-adjoint action in this case gets identified with the adjoint action.

We compute that $\rho ( a ) ( x , y ) = - \mathit { \Pi } _ { x a y } ^ { t }$ , so it follows without too much difficulty that, with respect to our identification of ${ \mathfrak { s o } } ( 3 ) ^ { * }$ with $\mathfrak { s o } ( 3 )$ , we have $\mu ( x , y ) = x ^ { t } y - y ^ { t } x$

The reader can check that all of the values of $\mu$ are clean except for $0 \in { \mathfrak { s o } } ( 3 )$ . Even this value would be clean if, instead of taking M to be all of $\mathbb { R } ^ { 6 }$ , we let M be $\mathbb { R } ^ { 6 }$ minus the origin $( x , y ) = ( 0 , 0 )$

I leave it to the reader to check that the G-invariant map $P \colon \mathbb { R } ^ { 6 }  \mathbb { R } ^ { 3 }$ defined by

$$
P ( x , y ) = ( x \cdot x , x \cdot y , y \cdot y )
$$

maps the set $\mu ^ { - 1 } ( 0 )$ onto the “cone” consisting of those points $( a , b , c ) \in \mathbb { R } ^ { 3 }$ with $a , c \geq 0$ and $b ^ { 2 } = a c$ and the fibers of $P$ are the $G _ { 0 }$ -orbits of the points in $\mu ^ { - 1 } ( 0 )$

For $\xi \neq 0$ , the P -image of the set $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ is one nappe of the hyperboloid of two sheets described as $a c - b ^ { 2 } = - \mathrm { t r } ( \xi ^ { 2 } )$ . The reader should compute the area forms $\Omega _ { \xi }$ on these sheets.

# Exercise Set 7:

# Classical Reduction

1. Let M be the torus $\mathbb { R } ^ { 2 } / \mathbb { Z } ^ { 2 }$ and let dx and dy be the standard 1-forms on M. Let $\Omega = d x \wedge d y$ . Show that the “translation action” $( a , b ) \cdot [ x , y ] = [ x + a , y + b ]$ of $\mathbb { R } ^ { 2 }$ on M is symplectic but not Hamiltonian.

2. Let $( M , \Omega )$ be a connected symplectic manifold and let $\lambda \colon G \times M \to M$ be a Hamiltonian group action.

(i) Prove that, if $\rho \colon { \mathfrak { g } }  C ^ { \infty } ( M )$ is a linear mapping that satisfies $\lambda _ { * } ( x ) \lrcorner \Omega = d \big ( \rho ( x ) \big )$ then $\lambda _ { * } \bigl ( [ x , y ] \bigr ) \lrcorner \Omega = d \bigl ( \{ \rho ( x ) , \rho ( y ) \} \bigr )$

(ii) Show that the associated linear mapping $c _ { \rho } \colon { \mathfrak { g } } \times { \mathfrak { g } }  \mathbb { R }$ defined in the text does indeed satisfy $c _ { \rho } \big ( [ x , y ] , z \big ) + c _ { \rho } \big ( [ y , z ] , x \big ) + c _ { \rho } \big ( [ z , \dot { x } ] , y \big ) = 0$ for all $x , y , z \in { \mathfrak { g } }$ . (Hint: Use the fact the Poisson bracket satisfies the Jacobi identity and that the Poisson bracket of a constant function with any other function is zero.)

3. Lie Algebra Cohomology. The purpose of this exercise is to acquaint the reader with the rudiments of Lie algebra cohomology.

The Lie bracket of a Lie algebra g can be regarded as a linear map $\partial \colon \Lambda ^ { 2 } ( { \mathfrak { g } } ) \to { \mathfrak { g } }$ The dual of this linear map is a map $- \delta \colon { \mathfrak { g } } ^ { * } \  \ \Lambda ^ { 2 } ( { \mathfrak { g } } ^ { * } )$ (Thus, for $\xi \in \mathfrak { g } ^ { * }$ , we have $\delta \xi ( x , y ) = - \xi \big ( [ x , y ] \big ) . \big )$ This map δ can be extended uniquely to a graded, degree-one derivation $\delta \colon \Lambda ^ { * } ( { \mathfrak { g } } ^ { * } ) \to \Lambda ^ { * } ( { \mathfrak { g } } ^ { * } )$

(i) For any $c \in \Lambda ^ { 2 } ( { \mathfrak { g } } ^ { * } )$ , show that $\delta c ( x , y , z ) = - c \big ( [ x , y ] , z \big ) - c \big ( [ y , z ] , x \big ) - c \big ( [ z , x ] , y \big )$ (Hint: Every $c \in \Lambda ^ { 2 } ( { \mathfrak { g } } ^ { * } )$ is a sum of wedge products $\xi \wedge \eta$ where $\xi , \eta \in { \mathfrak { g } } ^ { * } . )$ Conclude that the Jacobi identity in g is equivalent to the condition that $\delta ^ { 2 } = 0$ on all of $\Lambda ^ { * } ( { \mathfrak { g } } ^ { * } )$ .   
Thus, for any Lie algebra g, we can define the k’th cohomology group of g, denoted $H ^ { k } ( { \mathfrak { g } } )$ ,   
as the kernel of δ in $\Lambda ^ { k } ( { \mathfrak { g } } ^ { * } )$ modulo the subspace $\delta \big ( \Lambda ^ { k - 1 } ( { \mathfrak { g } } ^ { * } ) \big )$

(ii) Let G be a Lie group whose Lie algebra is g. For each $\Phi \doteq \Lambda ^ { k } \bigl ( \mathfrak { g } ^ { * } \bigr )$ , define $\omega _ { \Phi }$ to be the left-invariant k-form on G whose value at the identity is Φ. Show that $d \omega _ { \Phi } = \omega _ { \delta \Phi }$ (Hint: the space of left-invariant forms on G is clearly closed under exterior derivative and is generated over R by the left-invariant 1-forms. Thus, it suffices to prove this formula for Φ of degree 1. Why?)

Thus, the cohomology groups $H ^ { k } ( { \mathfrak { g } } )$ measure “closed-mod-exact” in the space of leftinvariant forms on G. If G is compact, then these cohomology groups are isomorphic to the corresponding deRham cohomology groups of the manifold G.

(iii) (The Whitehead Lemmas) Show that if the Killing form of g is non-degenerate, then $H ^ { 1 } ( { \mathfrak { g } } ) = H ^ { 2 } ( { \mathfrak { g } } ) = 0$ . (Hint: You should have already shown that if κ is nondegenerate, then $[ { \mathfrak { g } } , { \mathfrak { g } } ] = { \mathfrak { g } }$ . Show that this implies that $H ^ { 1 } ( { \mathfrak { g } } ) { = } 0$ . Next show that for $\Phi \in \Lambda ^ { 2 } ( { \mathfrak { g } } ^ { * } )$ , we can write $\Phi ( x , y ) = \kappa ( L x , y )$ where $L \colon { \mathfrak { g } } \to { \mathfrak { g } }$ is skew-symmetric. Then show that if $\delta \Phi = 0$ , then L is a derivation of g. Now see Exercise 3.3, part (iv).)

4. Homogeneous Symplectic Manifolds. Suppose that $( M , \Omega )$ is a symplectic manifold and suppose that there exists a transitive symplectic action $\lambda \colon G \times M \to M$ where $G$ is a group whose Lie algebra satisfies $H ^ { 1 } ( { \mathfrak { g } } ) = H ^ { 2 } ( { \mathfrak { g } } ) = 0$ . Show that there is a G-equivariant symplectic covering map $\pi \colon M \to G / G _ { \xi }$ for some $\xi \in { \mathfrak { g } } ^ { * }$ . Thus, up to passing to covers, the only symplectic homogeneous spaces of a Lie group satisfying $H ^ { 1 } ( { \mathfrak { g } } ) = H ^ { 2 } ( { \mathfrak { g } } ) = 0$ are the coadjoint orbits. This result is usually associated with the names Kostant, Souriau, and Symes.

(Hint: Since G acts homogeneously on M , it follows that, as G-spaces, $M = G / H$ for some closed subgroup $H \subset G$ that is the stabilizer of a point m of M . Let $\phi \colon G \to M$ be $\phi ( g ) = g \cdot m$ Now consider the left-invariant 2-form $\phi ^ { * } ( \Omega )$ on G in light of the previous Exercise. Why do we also need the hypothesis that $H ^ { 1 } ( { \mathfrak { g } } ) = 0 ? )$

I warn the reader that this characterization of homogeneous symplectic spaces is sometimes misquoted. Either the covering ambiguity is overlooked or else, instead of hypotheses about the cohomology groups, sometimes compactness is assumed, either for M or G. The example of $S ^ { 1 } \times S ^ { 1 }$ acting on itself and preserving the bi-invariant area form shows that compactness is not generally helpful. Here is an example that shows that you must allow for the covering possibility: Let $H \subset \mathrm { S L } ( 2 , \mathbb { R } )$ be the subgroup of diagonal matrices with positive entries on the diagonal. Then $\operatorname { S L } ( 2 , \mathbb { R } ) / H$ has an $\operatorname { S L } ( 2 , \mathbb { R } )$ -invariant area form, but it double covers the associated coadjoint orbit.

5. Verify the claim made in the text that, if there exists a G-invariant 1-form $\omega$ on M so that $d \omega = \Omega$ , then the formula $\rho ( x ) = - \omega \big ( \lambda _ { * } ( x ) \big )$ yields a lifting $\rho$ for which $c _ { \rho } = 0$

6. Show that if $\mathbb { R } ^ { 2 }$ acts on itself by translation then, with respect to the standard area form $\Omega = d x \wedge d y$ , this action is Hamiltonian but not Poisson.

7. Verify the claim made in the proof of Theorem 1 that the following identity holds for all $a \in G$ , all $y \in { \mathfrak { g } }$ , and all $m \in M$ :

$$
\lambda _ { a } ^ { \prime } \bigl ( \lambda _ { * } ( y ) ( m ) \bigr ) = \lambda _ { * } \bigl ( \mathrm { A d } ( a ) y \bigr ) ( a \cdot m ) .
$$

8. Matrix Calculations. The purpose of this exercise is to let you get some practice in a case where everything can be written out in coordinates.

Let $G = \operatorname { G L } ( n , \mathbb { R } )$ and let $Q \colon { \mathfrak { g l } } ( n , \mathbb { R } ) \ $ R be a non-degenerate quadratic form. Show that if we use the inclusion mapping x: $\operatorname { G L } ( n , \mathbb { R } ) \to { \mathcal { M } } _ { n \times n }$ as a coordinate chart, then, in the associated canonical coordinates $( x , p )$ , the Lagrangian $L$ takes the form $L = { \textstyle \frac { 1 } { 2 } } \langle x ^ { - 1 } p , x ^ { - 1 } p \rangle _ { Q }$ . Show also that $\omega _ { L } = \langle x ^ { - 1 } p , x ^ { - 1 } d x \rangle _ { Q }$

Now compute the expression for the momentum mapping $\mu$ and the Euler-Lagrange equations for motion under the Lagrangian L. Show directly that $\mu$ is constant on the solutions of the Euler-Lagrange equations.

Suppose that $Q$ is Ad-invariant, i.e., $Q { \big ( } \operatorname { A d } ( g ) ( x ) { \big ) } = Q ( x )$ for all $g \in G$ and $x \in { \mathfrak { g } }$ Show that the constancy of $\mu$ is equivalent to the assertion that $p x ^ { - 1 }$ is constant on the solutions of the Euler-Lagrange equations. Show that, in this case, the L-critical curves in G are just the curves $\gamma ( t ) = \gamma _ { 0 } e ^ { t v }$ where $\gamma _ { 0 } \in G$ and $v \in { \mathfrak { g } }$ are arbitrary.

Finally, repeat all of these constructions for the general Lie group $G ,$ translating everything into invariant notation (as opposed to matrix notation).

9. Euler’s Equation. Look back over the example given in the Lecture of left-invariant metrics on Lie groups. Suppose that $\gamma \colon \mathbb { R }  G$ is an L-critical curve. Define $\xi ( t ) =$ $\tau _ { Q } \big ( \omega ( \dot { \gamma } ( t ) ) \big )$ Thus, $\xi \colon \mathbb { R } \to { \mathfrak { g } } ^ { * }$ Show that the image of $\xi$ lies on a single coadjoint orbit. Moreover, show that $\xi$ satisfies Euler’s Equation:

$$
\dot { \xi } + \mathrm { a d } ^ { * } \left( \tau _ { Q } ^ { - 1 } ( \xi ) \right) ( \xi ) = 0 .
$$

The reason Euler’s Equation is so remarkable is that it only involves ‘half of the variables’ of the curve $\dot { \gamma }$ in T G.

Once a solution to Euler’s Equation is found, the equation for finding the original curve $\gamma$ is just $\dot { \gamma } = L _ { \gamma } ^ { \prime } \big ( \tau _ { Q } ^ { - 1 } ( \xi ) \big )$ , which is a Lie equation for $\gamma$ and hence is amenable to Lie’s method of reduction.

Actually more is true. Show that, if we set $\xi ( 0 ) = \xi _ { 0 }$ , then the equation $\mathrm { A d } ^ { * } ( \gamma ) ( \xi ) = \xi _ { 0 }$ determines the solution $\gamma$ of the Lie equation with initial condition $\gamma ( 0 ) = e$ up to right multiplication by a curve in the stabilizer subgroup $G _ { \xi _ { 0 } }$ . Thus, we are reduced to solving a Lie equation for a curve in $G _ { \xi _ { 0 } }$ . (It may be of some interest to note that the stabilizer of the generic element $\eta \in { \mathfrak { g } } ^ { * }$ is a solvable group. Of course, for such $\eta ,$ the corresponding Lie equation can be solved by quadratures.)

10. Project: Analysis of the Rigid Body in $\mathbb { R } ^ { 3 }$ . Go back to the example of the motion of a rigid body in $\mathbb { R } ^ { 3 }$ presented in Lecture 4. Use the information provided in the previous two Exercises to show that the equations of motion for a free rigid body are integrable by quadratures. You will want to first compute the coadjoint action and describe the coadjoint orbits and their stabilizers.

11. Verify that, under the hypotheses of Theorem 2, the dimension of the reduced space $M _ { \xi }$ is given by the formula

$$
\dim \ M _ { \xi } = \dim \ M - \dim \ G - \dim \ G _ { \xi } + 2 \dim \ G _ { m }
$$

where $G _ { m }$ is the stabilizer of any $m \in \mu ^ { - 1 } ( \xi )$

(Hint: Show that for any m $\in \mu ^ { - 1 } ( \xi )$ , we have

$$
\dim T _ { m } \mu ^ { - 1 } ( \xi ) + \dim T _ { m } { \big ( } G \cdot m { \big ) } = \dim M
$$

and then do some arithmetic.)

12. In the reduction process, what is the relationship between $M _ { \xi }$ and $M _ { \mathrm { A d ^ { * } ( \boldsymbol { g } ) ( \boldsymbol { \xi } ) } } ?$

13. Suppose that $\lambda \colon G \times M \to M$ is a Poisson action and that Y is a symplectic vector field on M that is G-invariant. Then according to Proposition 1, Y is tangent to each of the submanifolds $\mu ^ { - 1 } ( \boldsymbol { \xi } )$ (when $\xi$ is a clean value of $\mu )$ . Show that, when the symplectic quotient $M _ { \xi }$ exists, then there exists a unique vector field $Y _ { \xi }$ on $M _ { \xi }$ that satisfies $Y _ { \xi } \bigl ( \pi _ { \xi } ( m ) \bigr ) = \pi _ { \xi } ^ { \prime } \bigl ( \bar { Y ( m ) } \bigr )$ . Show also that $Y _ { \xi }$ is symplectic. Finally show that, given an integral curve $\gamma \colon \mathbb { R }  M _ { \xi }$ of $Y _ { \xi }$ , then the problem of lifting this to an integral curve of $Y$ is reducible by “finite” operations to solving a Lie equation for $G _ { \xi }$

This procedure is extremely helpful for two reasons: First, since $M _ { \xi }$ is generally quite a bit smaller than M, it should, in principle, be easier to find integral curves of $Y _ { \xi }$ than integral curves of $Y .$ . For example, if $M _ { \xi }$ is two dimensional, then $Y _ { \xi }$ can be integrated by quadratures (Why?). Second, it very frequently happens that $G _ { \xi }$ is a solvable group. As we have already seen, when this happens the “lifting problem” can be integrated by (a sequence of) quadratures.

## Lecture 8:

## Recent Applications of Reduction

In this Lecture, we will see some examples of symplectic reduction and its generalizations in somewhat non-classical settings.

In many cases, we will be concerned with extra structure on M that can be carried along in the reduction process to produce extra structure on $M _ { \xi }$ . Often this extra structure takes the form of a Riemannian metric with special holonomy, so we begin with a short review of this topic.

Riemannian Holonomy. Let $M ^ { n }$ be a connected and simply connected n-manifold, and let $g$ be a Riemannian metric on M. Associated to g is the notion of parallel transport along curves. Thus, for each (piecewise $C ^ { 1 } )$ curve $\gamma \colon [ 0 , 1 ] \to M$ , there is associated a linear mapping $P _ { \gamma } { : } T _ { \gamma ( 0 ) } M \to T _ { \gamma ( 1 ) } M$ , called ‘parallel transport along $\gamma ^ { \prime }$ , which is an isometry of vector spaces and which satisfies the conditions $P _ { \bar { \gamma } } = P _ { \gamma } ^ { - 1 }$ and $P _ { \gamma _ { 2 } \gamma _ { 1 } } = P _ { \gamma _ { 2 } } \circ P _ { \gamma _ { 1 } }$ where $\bar { \gamma }$ is the path defined by $\bar { \gamma } ( t ) = \gamma ( 1 - t )$ and $\gamma _ { 2 } \gamma _ { 1 }$ is defined only when $\gamma _ { 1 } ( 1 ) = \gamma _ { 2 } ( 0 )$ and, in this case, is given by the formula

$$
\gamma _ { 2 } \gamma _ { 1 } ( t ) = { \left\{ \begin{array} { l l } { \gamma _ { 1 } ( 2 t ) } & { { \mathrm { f o r ~ } } 0 \leq t \leq { \frac { 1 } { 2 } } , } \\ { \gamma _ { 2 } ( 2 t - 1 ) } & { { \mathrm { f o r ~ } } { \frac { 1 } { 2 } } \leq t \leq 1 . } \end{array} \right. }
$$

These properties imply that, for any $x \in M$ , the set of linear transformations of the form $P _ { \gamma }$ where $\gamma ( 0 ) = \gamma ( 1 ) = x$ is a subgroup $H _ { x } \subset \operatorname { O } ( T _ { x } M )$ and that, for any other point $y \in M$ we have $H _ { y } = P _ { \gamma } H _ { x } P _ { \bar { \gamma } }$ where $\gamma \colon [ 0 , 1 ] \to M$ satisfies $\gamma ( 0 ) = x$ and $\gamma ( 1 ) = y$ . Because we are assuming that M is simply connected, it is easy to show that $H _ { x }$ is actually connected and hence is a subgroup of $\mathrm { S O } ( T _ { x } M )$

Elie Cartan was the first to define and study ´ $H _ { x }$ . He called it the holonomy of g at x. He assumed that $H _ { x }$ was always a closed Lie subgroup of $\mathrm { S O } ( T _ { x } M )$ , a result that was only later proved by Borel and Lichnerowitz (see [KN]).

Georges de Rham, a student of Cartan, proved that, if there is a splitting $T _ { x } M =$ $V _ { 1 } \oplus V _ { 2 }$ that remains invariant under all the action of $H _ { x }$ , then, in fact, the metric g is locally a product metric in the following sense: The metric g can be written as a sum of the form $g = g _ { 1 } + g _ { 2 }$ in such a way that, for every point $y \in M$ there exists a neighborhood U of $y ,$ , a coordinate chart $( x _ { 1 } , x _ { 2 } ) \colon U  \mathbb { R } ^ { d _ { 1 } } \times \bar { \mathbb { R } } ^ { d _ { 2 } }$ , and metrics $\bar { g } _ { i }$ on $\mathbb { R } ^ { d _ { i } }$ so that $g _ { i } = x _ { i } ^ { * } ( \bar { g } _ { i } )$

He also showed that in this reducible case the holonomy group $H _ { x }$ is a direct product of the form $H _ { x } ^ { 1 } \times H _ { x } ^ { 2 }$ where $H _ { x } ^ { i } \subset \operatorname { S O } ( V _ { i } )$ . Moreover, it turns out (although this is not obvious) that, for each of the factor groups $H _ { x } ^ { i }$ , there is a submanifold $M _ { i } \subset M$ so that $T _ { x } M _ { i } = V _ { i }$ and so that $H _ { x } ^ { i }$ is the holonomy of the Riemannian metric $g _ { i }$ on $M _ { i }$

From this discussion it follows that, in order to know which subgroups of ${ \mathrm { S O } } ( n )$ can occur as holonomy groups of simply connected Riemannian manifolds, it is enough to find the ones that, in addition, act irreducibly on $\mathbb { R } ^ { n }$ . Using a great deal of machinery from the theory of representations of Lie groups, M. Berger [Ber] determined a relatively short list of possibilities for irreducible Riemannian holonomy groups. This list was slightly reduced a few years later, independently by Alexseevski and by Brown and Gray. The result of their work can be stated as follows:

Theorem 1: Suppose that g is a Riemannian metric on a connected and simply connected n-manifold M and that the holonomy $H _ { x }$ acts irreducibly on $T _ { x } M$ for some (and hence every) $x \in M$ Then either $( M , g )$ is locally isometric to an irreducible Riemannian symmetric space or else there is an isometry ι: $T _ { x } M  \mathbb { R } ^ { n }$ so that $H = \iota H _ { x } \iota ^ { - 1 }$ is one of the subgroups of ${ \mathrm { S O } } ( n )$ in the following table.

Irreducible Holonomies of Non-Symmetric Metrics
<table><tr><td>Subgroup</td><td>Conditions</td><td>Geometrical Type</td></tr><tr><td> ${ \mathrm { S O } } ( n )$   $\mathrm { U } ( m )$   $\mathrm { S U } ( m )$   $\mathrm { S p } ( m ) \mathrm { S p } ( 1 )$   $\operatorname { S p } ( m )$   $\mathrm { G _ { 2 } }$   $\mathrm { S p i n } ( 7 )$ </td><td>any n  $n = 2 m > 2$   $n = 2 m > 2$   $n = 4 m > 4$   $n = 4 m > 4$   $n = 7$   $n = 8$ </td><td>generic metric Kähler Ricci-flat Kähler Quaternionic Kähler hyperKähler Associative</td></tr></table>

A few words of explanation and comment about Theorem 1 are in order.

First, a Riemannian symmetric space is a Riemannian manifold diffeomorphic to a homogeneous space $G / H$ where $H \subset G$ is essentially the fixed subgroup of an involutory homomorphism $\sigma { \colon G } \to G$ that is endowed with a G-invariant metric g that is also invariant under the involution $\iota \colon G / H \to G / H$ defined by $\iota ( a H ) = \sigma ( a ) H$ . The classification of the Riemannian symmetric spaces reduces to a classification problem in the theory of Lie algebras and was solved by Cartan. Thus, the Riemannian symmetric spaces may be regarded as known.

Second, among the holonomies of non-symmetric metrics listed in the table, the ranges for n have been restricted so as to avoid repetition or triviality. Thus, $\mathrm { U } ( 1 ) = \mathrm { S O } ( 2 )$ and $\mathrm { S U } ( 1 ) = \{ e \}$ while $\mathrm { S p } ( 1 ) = \mathrm { S U } ( 2 )$ , and $\mathrm { S p } ( 1 ) \mathrm { S p } ( 1 ) = \mathrm { S O } ( 4 )$

Third, according to S. T. Yau’s celebrated proof of the Calabi Conjecture, any compact complex manifold for which the canonical bundle is trivial and that has a K¨ahler metric also has a Ricci-flat K¨ahler metric (see [Bes]). For this reason, metrics with holonomy SU(m) are often referred to as Calabi-Yau metrics.

Finally, I will not attempt to discuss the proof of Theorem 1 in these notes. Even with modern methods, the proof of this result is non-trivial and, in any case, would take us far from our present interests. Instead, I will content myself with the remark that it is now known that every one of these groups does, in fact, occur as the holonomy of a Riemannian metric on a manifold of the appropriate dimension. I refer the reader to [Bes] for a complete discussion.

We will be particularly interested in the K¨ahler and hyperK¨ahler cases since these cases can be characterized by the condition that the holonomy of g leaves invariant certain closed non-degenerate 2-forms. Hence these cases represent symplectic manifolds with “extra structure”, namely a compatible metric.

The basic result will be that, for a manifold M that carries one of these two structures, there is a reduction process that can be applied to suitable group actions on M that preserve the structure.

## K¨ahler Manifolds and Algebraic Geometry.

In this section, we give a very brief introduction to K¨ahler manifolds. These are symplectic manifolds that are also complex manifolds in such a way that the complex structure is “maximally compatible” with the symplectic structure. These manifolds arise with great frequency in Algebraic Geometry, and it is beyond the scope of these Lectures to do more than make an introduction to their uses here.

Hermitian Linear Algebra. As usual, we begin with some linear algebra. Let $\begin{array} { r } { H { : } \mathbb { C } ^ { n } \times \mathbb { C } ^ { n } \to \mathbb { C } } \end{array}$ be the hermitian inner product given by

$$
{ \cal H } ( z , w ) = \bar { z } w = \bar { z } ^ { 1 } w ^ { 1 } + \cdot \cdot \cdot + \bar { z } ^ { n } w ^ { n } .
$$

Then $\mathrm { U } ( n ) \subset \mathrm { G L } ( n , \mathbb { C } )$ is the group of complex linear transformations of $\mathbb { C } ^ { n }$ that preserve H since $H ( A z , A w ) = H ( z , w )$ for all $z , w \in \mathbb { C } ^ { n }$ if and only if ${ } ^ { t } \bar { A } A = I _ { n }$

Now, H can be split into real and imaginary parts as

$$
\begin{array} { r } { H ( z , w ) = \langle { z } , w \rangle + \imath \Omega ( z , w ) . } \end{array}
$$

It is clear from the relation $H ( z , w ) = { \overline { { H ( w , z ) } } }$ that h, i is symmetric and Ω is skewsymmetric. I leave it to the reader to show that , is positive definite and that Ω is non-degenerate.

Moreover, since $H ( z , \imath w ) = \imath H ( z , w )$ , it also follows that $\Omega ( z , w ) = \langle \imath z , w \rangle$ and ${ \langle z , w \rangle = \Omega ( z , \imath w ) }$ . It easily follows from these equations that, if we let $J \colon \mathbb { C } ^ { n } \to \ \mathbb { C } ^ { n }$ denote multiplication by ı, then knowing any two of the three objects h, i, Ω, or J on $\mathbb { R } ^ { 2 n }$ determines the third.

Definition 1: Let V be a vector space over R. A non-degenerate 2-form Ω on V and a complex structure $J \colon V  V$ are said to be compatible if $\Omega ( x , J y ) = \Omega ( y , J x )$ for all $x , y \in V$ If the pair $( \Omega , J )$ is compatible, then we say that the pair forms an Hermitian structure on V if, in addition, $\Omega ( x , J x ) > 0$ for all non-zero $x \in V$ . The positive definite quadratic form $g ( x , x ) = \Omega ( x , J x )$ is called the associated metric on V .

I leave as an exercise for the reader the task of showing that any two Hermitian structures on V are isomorphic via some invertible endomorphism of V .

It is easy to show that, if g is the quadratic form associated to a compatible pair $\left( \Omega , J \right)$ 7 then $\Omega ( v , w ) = g ( J v , w )$ . It follows that any two elements of the triple $( \Omega , J , g )$ determine the third.

In an extension of the notion of compatibility, we define a quadratic form g on $V$ to be compatible with a non-degenerate 2-form Ω on V if the linear map $J \colon V  V$ defined by the relation $\Omega ( v , w ) = g ( J v , w )$ satisfies $J ^ { 2 } = - 1$ . Similarly, we define a quadratic form g on V to be compatible with a complex structure J on V if $g ( J v , w ) = - g ( J w , v )$ , so that $\Omega ( v , w ) = g ( J v , w )$ defines a 2-form on V .

Almost Hermitian Manifolds. Since our main interest is in symplectic and complex structures, I will introduce the notion of an almost Hermitian structure on a manifold in terms of its almost complex and almost symplectic structures:

Definition 2: Let $M ^ { 2 n }$ be a manifold. A 2-form Ω and an almost complex structure J define an almost Hermitian structure on M if, for each $m \in M$ , the pair $\left( \Omega _ { m } , J _ { m } \right)$ defines a Hermitian structure on $T _ { m } M$

When $( \Omega , J )$ defines an almost Hermitian structure on M, the Riemannian metric g on M defined by $g ( v ) = \Omega ( v , J v )$ is called the associated metric.

Just as one must place conditions on an almost symplectic structure in order to get a symplectic structure, there are conditions that an almost complex structure must satisfy in order to be a complex structure.

Definition 3: An almost complex structure J on $M ^ { 2 n }$ is integrable if each point of M has a neighborhood U on which there exists a coordinate chart $z \colon U \to \mathbb { C } ^ { n }$ so that $z ^ { \prime } ( J v ) = \imath z ^ { \prime } ( v )$ for all $v \in T U$ . Such a coordinate chart is said to be J-holomorphic.

According to the Korn-Lichtenstein theorem, when $n = 1$ all almost complex structures are integrable. However, for $n \geq 2$ , one can easily write down examples of almost complex structures J that are not integrable. (See the Exercises.)

When J is an integrable almost complex structure on $M$ , the set

$$
\mathcal { U } _ { J } = \{ ( U , z ) \mid z \colon U \to \mathbb { C } ^ { n } \mathrm { ~ i s ~ } J \mathrm { - h o l o m o r p h i c } \}
$$

forms an atlas of charts that are holomorphic on overlaps. Thus, $\mathcal { U } _ { J }$ defines a holomorphic structure on M .

The reader may be wondering just how one determines whether an almost complex structure is integrable or not. In the Exercises, you are asked to show that, for an integrable almost complex structure J , the identity $\mathfrak { L } _ { J X } J - J \circ \mathfrak { L } _ { X } J = 0$ must hold for all vector fields X on M. It is a remarkable result, due to Newlander and Nirenberg, that this condition is sufficient for J to be integrable.

The reason that I mention this condition is that it shows that integrability is determined by J and its first derivatives in any local coordinate system. This condition can be rephrased as the condition that the vanishing of a certain tensor $N _ { J } ,$ , called the Nijenhuis tensor of J and constructed out of the first-order jet of J at each point, is necessary and sufficient for the integrability of J.

We are now ready to name the various integrability conditions that can be defined for an almost Hermitian manifold.

Definition 4: We call an almost Hermitian pair $( \Omega , J )$ on a manifold M almost K¨ahler if Ω is closed, Hermitian if J is integrable, and K¨ahler if Ω is closed and J is integrable.

We already saw in Lecture 6 that a manifold has an almost complex structure if and only if it has an almost symplectic structure. However, this relationship does not, in general, hold between complex structures and symplectic structures.

Example: Here is a complex manifold that has no symplectic structure. Let Z act on $M = \bar { \mathbb { C } } ^ { 2 } \backslash \{ 0 \}$ } by $n \cdot z = 2 ^ { n } z$ . This free action preserves the standard complex structure on M . Let $N = \mathbb { Z } \backslash { \tilde { M } }$ , then, via the quotient mapping, N inherits the structure of a complex manifold.

However, N is diffeomorphic to $S ^ { 1 } \times S ^ { 3 }$ as a smooth manifold. Thus N is a compact manifold satisfying $H _ { d R } ^ { 2 } ( N , \mathbb { R } ) = 0$ . In particular, by the cohomology ring obstruction discussed in Lecture 6, we see that M cannot be given a symplectic structure.

Example: Here is an example due to Thurston, of a compact 4-manifold that has a complex structure and has a symplectic structure, but has no K¨ahler structure.

Let $H _ { 3 } \subset \mathrm { G L } ( 3 , \mathbb { R } )$ be the Heisenberg group, defined in Lecture 2 as the set of matrices of the form

$$
g = { \left( \begin{array} { l l l } { 1 } & { x } & { z + { \frac { 1 } { 2 } } x y } \\ { 0 } & { 1 } & { y } \\ { 0 } & { 0 } & { 1 } \end{array} \right) } ~ .
$$

The left invariant forms and their structure equations on $H _ { 3 }$ are easily computed in these coordinates as

$$
\begin{array} { l l l } { { \omega _ { 1 } = d x } } & { { } } & { { d \omega _ { 1 } = 0 } } \\ { { \omega _ { 2 } = d y } } & { { } } & { { d \omega _ { 2 } = 0 } } \\ { { \omega _ { 3 } = d z - { \frac { 1 } { 2 } } ( x d y - y d x ) } } & { { } } & { { d \omega _ { 3 } = - \omega _ { 1 } \wedge \omega _ { 2 } } } \end{array}
$$

Now, let $\Gamma = H _ { 3 } \cap \mathrm { G L } ( 3 , \mathbb { Z } )$ be the subgroup of $H _ { 3 }$ consisting of those elements of $H _ { 3 }$ all of whose entries are integers. Let $X = \Gamma \backslash H _ { 3 }$ be the space of right cosets of Γ. Since the forms $\omega _ { i }$ are left-invariant, it follows that they are well-defined on X and form a basis for the 1-forms on X.

Now let $M = X \times S ^ { 1 }$ and let $\omega _ { 4 } = d \theta$ be the standard 1-form on $S ^ { 1 }$ . Then the forms $\omega _ { i }$ for $1 \leq i \leq 4$ form a basis for the 1-forms on M. Since $d \omega _ { 4 } = 0$ , it follows that the 2-form

$$
\Omega = \omega _ { 1 } \wedge \omega _ { 3 } + \omega _ { 2 } \wedge \omega _ { 4 }
$$

is closed and non-degenerate on M . Thus, M has a symplectic structure.

Next, I want to construct a complex structure on M. In order to do this, I will produce the appropriate local holomorphic coordinates on M. Let $\tilde { M } = H _ { 3 } \times$ R be the simply connected cover of M with coordinates $( x , y , z , \theta )$ . We regard $\tilde { M }$ as a Lie group. Define the functions $w ^ { 1 } = x + \imath y$ and $w ^ { 2 } = z + \textstyle { \dot { \imath } } \left( \theta + { \textstyle { \frac { 1 } { 4 } } } ( x ^ { 2 } + y ^ { 2 } ) \right)$ on M˜ . Then I leave to the reader to check that, if $g _ { 0 }$ is the element of M˜ with coordinates $( x _ { 0 } , y _ { 0 } , z _ { 0 } , \theta _ { 0 } )$ , then

$$
L _ { g _ { 0 } } ^ { * } ( w ^ { 1 } ) = w ^ { 1 } + w _ { 0 } ^ { 1 } \qquad \mathrm { a n d } \qquad L _ { g _ { 0 } } ^ { * } ( w ^ { 2 } ) = w ^ { 2 } + ( \imath / 2 ) \bar { w } _ { 0 } ^ { 1 } w ^ { 1 } + w _ { 0 } ^ { 2 } .
$$

Thus, the coordinates $w ^ { 1 }$ and $w ^ { 2 }$ define a left-invariant complex structure on $\tilde { M }$ . Since M is obtained from $\tilde { M }$ by dividing by the obvious left action of $\Gamma \times \mathbb { Z } ,$ it follows that there is a unique complex structure on M for which the covering projection is holomorphic.

Finally, we show that M cannot carry a K¨ahler structure. Since Γ is a discrete subgroup of $H _ { 3 }$ , the projection $H _ { 3 }  X$ is a covering map. Since $H _ { 3 } = \mathbb { R } ^ { 3 }$ as manifolds, it follows that $\pi _ { 1 } ( X ) = \Gamma$ Moreover, X is compact since it is the image under the projection of the cube in $H _ { 3 }$ consisting of those elements whose entries lie in the closed interval [0, 1]. On the other hand, since $[ \Gamma , \Gamma ] \simeq \mathbb { Z } ,$ it follows that $\Gamma / [ \Gamma , \Gamma ] \simeq \mathbb { Z } ^ { 2 }$ Thus, $H ^ { 1 } ( M , \bar { \mathbb { Z } } ) \stackrel { } { = } H ^ { 1 } ( X \times S ^ { 1 } , \mathbb { Z } ) = \mathbb { Z } ^ { 2 } \oplus \mathbb { Z } .$ From this, we get that $H _ { d R } ^ { 1 } ( M , \mathbb { R } ) = \mathbb { R } ^ { 3 }$ . In particular, the first Betti number of M is 3. Now, it is a standard result in K¨ahler geometry that the odd degree Betti numbers of a compact K¨ahler manifold must be even (for example, see [Ch]). Hence, M cannot carry any K¨ahler metric.

Example: Because of the classification of compact complex surfaces due to Kodaira, we know exactly which compact 4-manifolds can carry complex structures. Fernandez, Gotay, and Gray [FGG] have constructed a compact, symplectic 4-manifold M whose underlying manifold is not on Kodaira’s list, thus, providing an example of a compact symplectic 4-manifold that carries no complex structure.

The fundamental theorem relating the two “integrability conditions” to the idea of holonomy is the following one. We only give the idea of the proof because a complete proof would require the development of considerable machinery.

Theorem 2: An almost Hermitian structure $( \Omega , J )$ on a manifold M is K¨ahler if and only if the form Ω is parallel with respect to the parallel transport of the associated metric g .

Proof: (Idea) Once the formulas are developed, it is not difficult to see that the covariant derivatives of Ω with respect to the Levi-Civita connection of g are expressible in terms of the exterior derivative of Ω and the Nijenhuis tensor of J. Conversely, the exterior derivative of Ω and the Nijenhuis tensor of J can be expressed in terms of the covariant derivative of Ω with respect to the Levi-Civita connection of $g .$ Thus, Ω is covariant constant (i.e., invariant under parallel translation with respect to g) if and only it is closed and J is integrable. 

◮ It is worth remarking that J is invariant under parallel transport with respect to g if and only if Ω is.

The reason for this is that J is determined from and determines Ω once g is fixed. The observation now follows, since g is invariant under parallel transport with respect to its own Levi-Civita connection.

K¨ahler Reduction. We are now ready to state the first of the reduction theorems we will discuss in this Lecture.

It turns out that it’s a good idea to discuss a special case first.

Theorem 3: Kahler Reduction at¨ 0. Let $( \Omega , g )$ be a K¨ahler structure on $M ^ { 2 n }$ Let $\lambda \colon G \times M \to M$ be a left action that is Poisson with respect to Ω and preserves the metric g. Let $\mu \colon M \to { \mathfrak { g } } ^ { * }$ be the associated momentum mapping. Suppose that $0 \in { \mathfrak { g } } ^ { * }$ is a clean value of $\mu$ and that there is a smooth structure on the orbit space $M _ { 0 } = G \backslash \mu ^ { - 1 } ( 0 )$ for which the natural projection $\pi _ { 0 } : \mu ^ { - 1 } ( 0 ) \to G \backslash \mu ^ { - 1 } ( 0 )$ is a smooth submersion. Then there is a unique K¨ahler structure $\left( \Omega _ { 0 } , g _ { 0 } \right)$ on $M _ { 0 }$ defined by the conditions that $\pi _ { 0 } ^ { * } ( \Omega _ { 0 } )$ be equal to the pullback of Ω to $\mu ^ { - 1 } ( 0 ) \subset M$ and that $\pi _ { 0 } \colon \mu ^ { - 1 } ( 0 ) \to M _ { 0 }$ be a Riemannian submersion.

Proof: Let $\tilde { g } _ { 0 }$ and $\tilde { \Omega } _ { 0 }$ be the pullbacks of $g$ and Ω respectively to $\mu ^ { - 1 } ( 0 )$ . By hypotheses, $\tilde { g } _ { 0 }$ and $\tilde { \Omega } _ { 0 }$ are invariant under the action of $G$

From Theorem 2 of Lecture $^ { 7 , }$ we already know that there exists a unique symplectic structure $\Omega _ { 0 }$ on $M _ { 0 }$ for which $\pi _ { 0 } ^ { * } ( \Omega _ { 0 } ) = \tilde { \Omega } _ { 0 }$

Here is how we construct $g _ { 0 }$ . For any $m \in \mu ^ { - 1 } ( 0 )$ , there is a well defined $\tilde { g } _ { 0 }$ -orthogonal splitting

$$
T _ { m } \mu ^ { - 1 } ( 0 ) = T _ { m } \bigl ( G \cdot m \bigr ) \oplus H _ { m }
$$

that is clearly G-invariant. Since, by hypothesis, $\pi _ { 0 } \colon \mu ^ { - 1 } ( 0 ) \to M _ { 0 }$ is a submersion, it easily follows that $\pi _ { 0 } ^ { \prime } ( m ) \colon H _ { m } \to T _ { \pi _ { 0 } ( m ) } M _ { 0 }$ is an isomorphism of vector spaces. Moreover, the G-invariance of $\tilde { g }$ shows that there is a well-defined quadratic form $g _ { 0 } ( m )$ on $T _ { \pi _ { 0 } ( m ) } M _ { 0 }$ that corresponds to the restriction of $\tilde { g } _ { 0 }$ to $H _ { m }$ under this isomorphism. By the very definition of Riemannian submersion, it follows that $g _ { 0 }$ is a Riemannian metric on $M _ { 0 }$ for which $\pi _ { 0 }$ is a Riemannian submersion.

It remains to show that $\left( \Omega _ { 0 } , g _ { 0 } \right)$ defines a K¨ahler structure on $M _ { 0 }$ . First, we show that it is an almost K¨ahler structure, i.e., that $\Omega _ { 0 }$ and $g _ { 0 }$ are actually compatible. Since $\pi _ { 0 } ^ { \prime } ( m ) \colon H _ { m } \to T _ { \pi _ { 0 } ( m ) } M _ { 0 }$ is an isomorphism of vector spaces that identifies $\left( \Omega _ { 0 } , g _ { 0 } \right)$ with the restriction of $( \Omega , g )$ to $H _ { m }$ , it suffices to show that $H _ { m }$ is invariant under the action of J .

Here is how we do this. Tracing back through the definitions, we see that $x \in T _ { m } M$ lies in the subspace $H _ { m }$ if and only if x satisfies both of the conditions $\Omega ( x , y ) = 0$ and $g ( x , y ) = 0$ for all $y \in T _ { m } ( G \cdot m )$ . However, since $\Omega ( x , y ) = g ( J x , y )$ for all $y ,$ it follows that the necessary and sufficient conditions that x lie in $H _ { m }$ can also be expressed as the two conditions $g ( J x , y ) = 0$ and $\Omega ( J x , y ) = 0$ for all $y \in T _ { m } ( G \cdot m )$ . Of course, these conditions are exactly the conditions that Jx lie in $H _ { m }$ . Thus, $x \in H _ { m }$ implies that $J x \in H _ { m }$ , as desired.

Finally, in order to show that the almost K¨ahler structure on $M _ { 0 }$ is actually K¨ahler, it must be shown that $\Omega _ { 0 }$ is parallel with respect to the Levi-Civita connection of $g _ { 0 }$ This is a straightforward calculation using the structure equations and will not be done here. (Alternatively, to prove that the structure is actually K¨ahler, one could instead show that the induced almost complex structure is integrable. This is somewhat easier and the interested reader can consult the Exercises, where a proof is outlined.) 

Now, it seems unreasonable to consider only reduction at $0 \in { \mathfrak { g } } ^ { * }$ However, some caution is in order because the na¨ıve attempt to generalize Theorem 3 to reduction at a general $\xi \in { \mathfrak { g } } ^ { * }$ fails: Let $\lambda : G \times M \to M$ be a Poisson action on a K¨ahler manifold $( M , \Omega , g )$ that preserves g and let $\mu : M \to { \mathfrak { g } } ^ { * }$ be a Poisson momentum mapping. Then for every clean value $\xi \in { \mathfrak { g } } ^ { * }$ for which the orbit space $M _ { \xi } = G _ { \xi } \backslash \mu ^ { - 1 } ( \xi )$ has a smooth structure that makes $\pi _ { \xi } : \mu ^ { - 1 } ( \xi ) \to M _ { \xi }$ a smooth submersion, there is a symplectic structure $\Omega _ { \xi }$ on $M _ { \xi }$ that is induced by reduction in the usual way. Moreover, there is a unique metric $g _ { \xi }$ on $M _ { \xi }$ for which $\pi _ { \xi }$ is a Riemannian submersion (when $\mu ^ { - 1 } ( \xi ) \subset M$ is given the induced submanifold metric). Unfortunately, it is $n o t$ , in general, true that $g _ { \xi }$ is compatible with $\Omega _ { \xi }$ (See the Exercises for an example.)

If you examine the proof given above in the general case, you’ll see that the main problem is that the ‘horizontal space’ $H _ { m }$ need not be stable under $J .$ . In fact, what one knows in the general case is that $H _ { m }$ is g-orthogonal to both $T _ { m } G _ { \xi } { \cdot } m$ and to $J ( T _ { m } G { \cdot } m )$ However, when $G _ { \xi }$ is a proper subgroup of G (i.e., when $\xi$ is not a fixed point of the coadjoint action), we won’t have $T _ { m } G _ { \xi } { \cdot } m = T _ { m } G { \cdot } m$ , which is what we needed in the proof to show that $H _ { m }$ is stable under $J _ { \parallel }$

In fact, the proof does work when $G _ { \xi } = G$ , but this can be seen directly from the fact that, in this case, the ‘shifted’ momentum mapping $\mu ^ { \xi } = \mu - \xi$ still satisfies G-equivariance and we are simply performing reduction at 0 for the shifted momentum mapping $\mu ^ { \xi }$

Reduction at Kahler coadjoint orbits. ¨ Generalizing the case where $G \cdot \xi = \{ \xi \}$ , there is a way to define K¨ahler reduction at certain values of $\xi \in { \mathfrak { g } } ^ { * }$ , by relying on the ‘shifting trick’ described in the Exercises of Lecture 7:

In many cases, a coadjoint orbit $G { \cdot } \xi \subset { \mathfrak { g } } ^ { * }$ can be equipped with a G-invariant metric $h _ { \xi }$ for which the pair $( \Omega _ { \xi } , h _ { \xi } )$ defines a K¨ahler structure on the orbit $G \cdot \xi$ . (For example, this is always the case when G is compact.) In such a case, the shifting trick allows us to define a K¨ahler metric on $M _ { \xi } = G _ { \xi } \backslash \mu ^ { - 1 } ( 0 )$ by doing K¨ahler reduction at 0 on $M \times G { \cdot } \xi$ endowed with the product K¨ahler structure. In the cases in which there is only one G-invariant K¨ahler metric $h _ { \xi }$ on $G \cdot \xi$ that is compatible with $\Omega _ { \xi }$ (and, again, this always holds when G is compact), this defines a canonical K¨ahler reduction procedure for $\xi \in { \mathfrak { g } } ^ { * }$

Example: Kahler reduction in Algebraic Geometry. ¨ By far the most common examples of K¨ahler manifolds arise in Algebraic Geometry. Here is a sample of what K¨ahler reduction yields:

Let $M = \mathbb { C } ^ { n + 1 }$ with complex coordinates $z ^ { 0 } , z ^ { 1 } , \dots , z ^ { n }$ . We let $z ^ { k } = x ^ { k } + \imath y ^ { k }$ define real coordinates on M . Let $G = S ^ { 1 }$ act on M by the rule

$$
e ^ { \imath \theta } \cdot z = e ^ { \imath \theta } z .
$$

Then G clearly preserves the K¨ahler structure defined by the natural complex structure on M and the symplectic form

$$
\Omega = { \frac { \ i } { 2 } } ^ { t } d z \wedge d \bar { z } = d x ^ { 1 } \wedge d y ^ { 1 } + \cdot \cdot \cdot + d x ^ { n } \wedge d y ^ { n } .
$$

The associated metric is easily seen to be just

$$
g = ^ { t } d z \circ d \bar { z } = \left( d x ^ { 1 } \right) ^ { 2 } + \left( d y ^ { 1 } \right) ^ { 2 } + \cdot \cdot \cdot + \left( d x ^ { n } \right) ^ { 2 } + \left( d y ^ { n } \right) ^ { 2 } .
$$

Now, setting $\begin{array} { r } { X = \frac { \partial } { \partial \theta } } \end{array}$ , we can compute that

$$
\lambda _ { * } ( X ) = x ^ { k } { \frac { \partial } { \partial y ^ { k } } } - y ^ { k } { \frac { \partial } { \partial x ^ { k } } } .
$$

Thus, it follows that

$$
d \rho ( X ) = \lambda _ { * } ( X ) \lrcorner \Omega = - x ^ { k } d x ^ { k } - y ^ { k } d y ^ { k } = d \bigl ( - { \textstyle { \frac { 1 } { 2 } } } | z | ^ { 2 } \bigr ) .
$$

Thus, identifying ${ \mathfrak { g } } ^ { * }$ with R, we have that $\mu \colon \mathbb { C } ^ { n } \to \mathbb { R }$ is merely $\begin{array} { r } { \mu ( z ) = - \frac { 1 } { 2 } | z | ^ { 2 } } \end{array}$

It follows that every negative number is a non-trivial clean value for $\mu .$ . For example, $S ^ { 2 n + 1 } = \mu ^ { - 1 } ( - { \textstyle \frac { 1 } { 2 } } )$ . Clearly $G = S ^ { 1 }$ itself is the stabilizer subgroup of all of the values of $\mu .$ Thus, $M _ { - { \frac { 1 } { 2 } } }$ is the quotient of the unit sphere by the action of $S ^ { 1 }$ . Since each G-orbit is merely the intersection of $S ^ { 2 n + 1 }$ with a (unique) complex line through the origin, it is clear that $M _ { - { \frac { 1 } { 2 } } }$ is diffeomorphic to $\mathbb { C P } ^ { n }$

Since the coadjoint action is trivial, reduction at $\xi = - \textstyle { \frac { 1 } { 2 } }$ will define a K¨ahler structure on $\mathbb { C P } ^ { n }$ . It is instructive to compute what this K¨ahler structure looks like in local coordinates. Let $\mathbb { A } _ { 0 } \subset \mathbb { C P } ^ { n }$ be the subset consisting of those points $\left[ z ^ { 0 } , \dots , z ^ { n } \right]$ for which $z ^ { 0 } \neq 0$ . Then $\mathbb { A } _ { 0 }$ can be parametrized by $\phi : \mathbb { C } ^ { n } \to \mathbb { A } _ { 0 }$ where $\phi ( w ) = [ 1 , w ]$ . Now, over $\mathbb { A } _ { 0 }$ , we can choose a section $\sigma \colon \mathbb { A } _ { 0 } \to S ^ { 2 n + 1 }$ by the rule

$$
\sigma \circ \phi ( w ) = \frac { ( 1 , w ) } { W }
$$

where $W ^ { 2 } = 1 + | w ^ { 1 } | ^ { 2 } + \cdot \cdot \cdot + | w ^ { n } | ^ { 2 } > 0$ . It follows that

$$
\begin{array} { l } { { \displaystyle { \phi ^ { * } ( \Omega _ { - \frac { 1 } { 2 } } ) = ( \sigma \circ \phi ) ^ { * } ( \Omega ) = \frac { \imath } { 2 } \left( d \big ( \frac { w ^ { k } } { W } \big ) \wedge d \big ( \frac { \bar { w } ^ { k } } { W } \big ) \right) } } } \\ { { \displaystyle ~ = \frac { \imath } { 2 } \left( \frac { d w ^ { k } \wedge d \bar { w } ^ { k } } { W ^ { 2 } } + ( w ^ { k } d \bar { w } ^ { k } - \bar { w } ^ { k } d w ^ { k } ) \wedge \frac { d W } { W ^ { 3 } } \right) } } \\ { { \displaystyle ~ = \frac { \imath } { 2 } \left( \frac { W ^ { 2 } \delta _ { j k } - \bar { w } ^ { j } w ^ { k } } { W ^ { 4 } } \right) d w ^ { j } \wedge d \bar { w } ^ { k } . } }  \end{array}
$$

I leave it to the reader to check that the quotient metric $( \mathrm { i . e . , }$ the one for which the submersion $S ^ { 2 n + 1 } \to \mathbb { C P } ^ { n }$ is Riemannian) is given by the formula

$$
g _ { - { \frac { 1 } { 2 } } } = \left( { \frac { W ^ { 2 } \delta _ { j k } - \bar { w } ^ { j } w ^ { k } } { W ^ { 4 } } } \right) d w ^ { j } \circ d \bar { w } ^ { k } .
$$

In particular, it follows that the functions $w ^ { k }$ are holomorphic functions with respect to the induced almost complex structure, verifying directly that the pair $( \Omega _ { - \frac { 1 } { 2 } } , g _ { - \frac { 1 } { 2 } } )$ is indeed a K¨ahler structure on $\mathbb { C P } ^ { n }$ . Up to a normalizing constant, this is the usual formula for the Fubini-Study K¨ahler structure on $\mathbb { C P } ^ { n }$ in an affine chart.

Of course, the Fubini-Study metric induces a K¨ahler structure on every complex submanifold of $\mathbb { C P } ^ { n }$ . However, we can just as easily see how this arises from the reduction procedure: If $P ( z ^ { 0 } , \ldots , z ^ { n } )$ is a non-zero homogeneous polynomial of degree $d ,$ then the set $\tilde { M } _ { P } = P ^ { - 1 } ( 0 ) \subset \mathbb { C } ^ { n + 1 }$ is a complex subvariety of $\mathbb { C } ^ { n + 1 }$ that is invariant under the $S ^ { 1 }$ action since, by homogeneity, we have

$$
P ( e ^ { \imath \theta } \cdot z ) = e ^ { \imath d \theta } P ( z ) .
$$

It is easy to show that if the variety $\tilde { M } _ { P }$ has no singularity other than $0 \in \mathbb { C } ^ { n + 1 }$ , then the K¨ahler reduction of the K¨ahler structure that it inherits from the standard structure on $\mathbb { C } ^ { n + 1 }$ is just the K¨ahler structure on the corresponding projectivized variety $M _ { P } \subset \mathbb { C P } ^ { n }$ that is induced by restriction of the Fubini-Study structure.

“Example”: Flat Bundles over Compact Riemann Surfaces. The following is not really an example of the theory as we have developed it since it will deal with “infinite dimensional manifolds”, however it is suggestive and the formal calculations yield an interesting result. (For a review of the terminology used in this and the next example, see the Appendix.)

Let G be a Lie group with Lie algebra g, and let $\langle , \rangle$ be a positive definite, Ad-invariant inner product on g. (For example, if $G = { \mathrm { S U } } ( n )$ , we could take $\langle x , y \rangle = - \mathrm { t r } ( x y ) . )$

Let Σ be a connected compact Riemann surface. Then there is a star operation ^ $\kappa \colon \mathcal { A } ^ { 1 } ( \Sigma )  \mathcal { A } ^ { 1 } ( \Sigma )$ that satisfies $* ^ { 2 } = - i d .$ , and $\alpha \wedge * \alpha \geq 0$ for all 1-forms α on $\Sigma$

Let P be a principal right G-bundle over Σ, and let $\operatorname { A d } ( P ) = P \times _ { \operatorname { A d } { \mathfrak { g } } }$ denote the vector bundle over M associated to the adjoint representation Ad: $G \to \operatorname { A u t } ( { \mathfrak { g } } )$ . Let Aut(P ) denote the group of automorphisms of P , also known as the gauge group of P .

Let $\mathfrak { A } ( P )$ denote the space of connections on P . Then it is well known that $\mathfrak { A } ( P )$ is an affine space modeled on the vector space $\ A ^ { 1 } \left( { \mathrm { A d } } ( P ) \right)$ , which consists of the 1-forms on M with values in $\operatorname { A d } ( P )$ . Thus, in particular, for every $A \in { \mathfrak { A } } ( P )$ , we have a natural isomorphism

$$
T _ { A } \mathfrak { A } ( P ) = \mathcal { A } ^ { 1 } \big ( \mathrm { A d } ( P ) \big ) .
$$

I now want to define a “K¨ahler” structure on $\mathfrak { A } ( P )$ . In order to do this, I will define the metric g and the 2-form Ω.

First, for $\alpha \in T _ { A } \mathfrak { A } ( P )$ , I define

$$
{ \bf g } ( \alpha ) = \int _ { \Sigma } \langle \alpha , \ast \alpha \rangle .
$$

(I extend the operator  in the obvious way to $\mathcal { A } ^ { 1 } \big ( \mathrm { A d } ( P ) \big ) . \big )$ It is clear that ${ \bf g } ( \alpha ) \geq 0$ with equality if and only if $\alpha = 0$ . Thus, g defines a “Riemannian metric” on $\mathfrak { A } ( P )$ . Since g is “translation invariant”, it “follows” that g is $\mathrm { ^ { 6 6 } f l a t ^ { 9 } }$

Second, I define Ω by the rule:

$$
\Omega ( \alpha , \beta ) = \int _ { \Sigma } \langle \alpha , \beta \rangle .
$$Since $\Omega ( \alpha , \beta ) = \mathfrak { g } ( \alpha , * \beta )$ , it follows that Ω is actually non-degenerate. Moreover, because Ω too is “translation invariant”, it “must” be “parallel” with respect to g.

Thus, $\left( \Omega , { \mathfrak { g } } \right)$ is a “flat K¨ahler” structure on $\mathfrak { A } ( P )$ . Now, I claim that both $\Omega$ and g are invariant under the natural right action of $\mathsf { A u t } ( P )$ on $\mathfrak { A } ( P )$ . To see this, note that an element $\phi \in \operatorname { A u t } ( P )$ determines a map $\varphi { \colon } P \to G$ by the rule $p \cdot \varphi ( p ) = \phi ( p )$ and that this $\varphi$ satisfies the identity $\varphi ( p \cdot g ) = g ^ { - 1 } \varphi ( p ) g$ . In terms of $\varphi ,$ , the action of $\operatorname { A u t } ( P )$ on $\mathfrak { A } ( P )$ is given by the classical formula

$$
A \cdot \phi = \phi ^ { * } ( A ) = \varphi ^ { * } ( \omega _ { G } ) + \mathrm { A d } \big ( \varphi ^ { - 1 } \big ) ( A ) .
$$

From this, it follows easily that Ω and g are $\mathsf { A u t } ( P )$ -invariant.

Now, I want to compute the momentum mappping µ. The Lie algebra of $\operatorname { A u t } ( P )$ , namely aut $( P )$ , can be naturally identified with $\mathcal { A } ^ { 0 } \big ( \mathrm { A d } ( P ) \big )$ , the space of sections of the bundle $\operatorname { A d } ( P )$ . I leave to the reader the task of showing that the induced map from $\operatorname { a u t } ( P )$ to vector fields on $\mathfrak { A } ( P )$ is given by $d _ { A } \colon { \mathcal { A } } ^ { 0 } \left( \operatorname { A d } ( P ) \right) \to { \mathcal { A } } ^ { 1 } \left( \operatorname { A d } ( P ) \right)$ . Thus, in order to construct the momentum mapping, we must find, for each $f \in { \mathcal { A } } ^ { 0 } { \bigl ( } \mathrm { A d } ( P ) { \bigr ) }$ , a function $\rho ( f )$ on A so that the 1-form $d \rho ( f )$ is given by

$$
d \pmb { \theta } ( f ) ( \alpha ) = d _ { A } f \lrcorner \Omega ( \alpha ) = \int _ { \Sigma } \langle d _ { A } f , \alpha \rangle = - \int _ { \Sigma } \langle f , d _ { A } \alpha \rangle .
$$

However, this is easy. We just set

$$
\rho ( f ) ( A ) = - \int _ { \Sigma } \langle f , F _ { A } \rangle
$$

and the reader can easily check that

$$
\frac { d } { d t } \Big \vert _ { t = 0 } \left( \pmb { \rho } ( f ) ( A + t \alpha ) \right) = - \int _ { \Sigma } \langle f , d _ { A } \alpha \rangle
$$

as desired. Finally, using the natural isomorphism

$$
\big ( \mathrm { a u t } ( P ) \big ) ^ { * } = \big ( \mathcal { A } ^ { 0 } \big ( \mathrm { A d } ( P ) \big ) \big ) ^ { * } = \mathcal { A } ^ { 2 } \big ( \mathrm { A d } ( P ) \big ) ,
$$

we see that (up to sign) the formula for the momentum mapping simply becomes

$$
\begin{array} { r } { \mathsf { \Pi } \mu ( A ) = F _ { A } = d A + \frac { 1 } { 2 } [ A , A ] . } \end{array}
$$

Now, can we do reduction? What we need is a clean value of µ. As a reasonable first guess, let’s try 0. Thus, $\mu ^ { - 1 } ( 0 )$ consists exactly of the flat connections on P and the reduced space ${ \mathfrak { M } } _ { 0 }$ should be the flat connections modulo gauge equivalence, i.e., $\mu ^ { - 1 } ( 0 ) / \lambda \ u \mathrm { t } ( P )$

How can we tell whether 0 is a clean value? One way to know this would be to know that 0 is a regular value. We have already seen that $\mu ^ { \prime } ( A ) ( \alpha ) = d _ { A } \alpha$ , so we are asking

whether the map $d _ { A } \colon { \mathcal { A } } ^ { 1 } \bigl ( \mathrm { A d } ( P ) \bigr ) \to { \mathcal { A } } ^ { 2 } \bigl ( \mathrm { A d } ( P ) \bigr )$ is surjective for any flat connection A. Now, because A is flat, the sequence

$$
0 \longrightarrow { \mathcal { A } } ^ { 0 } { \big ( } { \mathrm { A d } } ( P ) { \big ) } \ { \stackrel { { d } { A } } { \longrightarrow } } { \mathcal { A } } ^ { 1 } { \big ( } { \mathrm { A d } } ( P ) { \big ) } \ { \stackrel { { d } { A } } { \longrightarrow } } { \mathcal { A } } ^ { 2 } { \big ( } { \mathrm { A d } } ( P ) { \big ) } \longrightarrow 0
$$

forms a complex and the usual Hodge theory pairing shows that $H ^ { 2 } ( \Sigma , d _ { A } )$ is the dual space of $H ^ { 0 } ( \Sigma , d _ { A } )$ Thus, $\mu ^ { \prime } ( A )$ is surjective if and only if $H ^ { 0 } ( \Sigma , d _ { A } ) = 0$ . Now, an element $f \in { \mathcal { A } } ^ { 0 } { \bigl ( } \mathrm { A d } ( P ) { \bigr ) }$ that satisfies $d _ { A } f = 0$ exponentiates to a 1-parameter family of automorphisms of P that commute with the parallel transport of A. I leave to the reader to show that $H ^ { 0 } ( \Sigma , d _ { A } ) \neq 0$ is equivalent to the condition that the holonomy group $H _ { A } ( p ) \subset G$ has a centralizer of positive dimension in G for some (and hence every) point of P . For example, for $G = { \mathrm { S U } } ( 2 )$ , this would be equivalent to saying that the holonomy groups $H _ { A } ( p )$ were each contained in an $S ^ { 1 } \subset G$

Let us let ${ \tilde { \mathfrak { M } } } ^ { * } \subset { \mathfrak { k } } ^ { - 1 } ( 0 )$ denote the (open) subset consisting of those flat connections whose holonomy groups have at most discrete centralizers in G. If G is compact, of course, this implies that these centralizers are finite. Then it “follows” that ${ \mathfrak { M } } _ { 0 } ^ { * } = { \tilde { \mathfrak { M } } } ^ { * } / { \mathrm { A u t } } ( P )$ is a K¨ahler manifold wherever it is a manifold. (In general, at the connections where the centralizer of the holonomy is trivial, one expects the quotient to be a manifold.)

Since the space of flat connections on P modulo gauge equivalence is well-known to be identifiable as the space $R \big ( \pi _ { 1 } ( \Sigma , s ) , G \big ) = \mathrm { H o m } \big ( \pi _ { 1 } ( \bar { \Sigma } , s ) , G \big ) / G$ of equivalence classes of representation of $\pi _ { 1 } ( \Sigma )$ into ${ \dot { G } } ,$ , our discussion leads us to believe that this space (which is finite dimensional) should have a natural K¨ahler structure on it. This is indeed the case, and the geometry of this K¨ahler metric is the subject of current interest.

## HyperK¨ahler Manifolds.

In this section, we will generalize the K¨ahler reduction procedure to the case of manifolds with holonomy $\operatorname { S p } ( m )$ , the so-called hyperK¨ahler case.

Quaternion Hermitian Linear Algebra. We begin with some linear algebra over the ring H of quaternions. For our purposes, H can be identified with the vector space of dimension 4 over R of matrices of the form

$$
x = { \left( \begin{array} { l l } { x ^ { 0 } + \ i x ^ { 1 } } & { x ^ { 2 } + \ i x ^ { 3 } } \\ { - x ^ { 2 } + \ i x ^ { 3 } } & { x ^ { 0 } - \ i x ^ { 1 } } \end{array} \right) } \quad { \stackrel { \mathrm { d e f } } { = } } \ x ^ { 0 } 1 + x ^ { 1 } i + x ^ { 2 } j + x ^ { 3 } k .
$$

(We are identifying the 2-by-2 identity matrix with 1 in this representation.) It is easy to see that H is closed under matrix multiplication. If we define $\bar { x } = x ^ { 0 } - x ^ { 1 } i - x ^ { 2 } j - x ^ { 3 } k$ then we easily get ${ \overline { { x y } } } = { \bar { y } } { \bar { x } }$ and

$$
x \bar { x } = \left( ( x ^ { 0 } ) ^ { 2 } + ( x ^ { 1 } ) ^ { 2 } + ( x ^ { 2 } ) ^ { 2 } + ( x ^ { 3 } ) ^ { 2 } \right) 1 = \operatorname* { d e t } ( x ) 1 \ \stackrel { \mathrm { d e f } } { = } \ | x | ^ { 2 } 1 .
$$

It follows that every non-zero element of H has a multiplicative inverse. Note that the space of quaternions of unit norm, $S ^ { 3 }$ defined by $| x | = 1$ , is simply SU(2).

Much of the linear algebra that works for the complex numbers can be generalized to the quaternions. However, some care must be taken since H is not commutative. In the following exposition, it turns out to be most convenient to define vector spaces over H as right vector spaces instead of left vector spaces. Thus, the standard H-vector space of H-dimension n is $\mathbb { H } ^ { n }$ (thought of as columns of quaternions of height n) where the action of the scalars on the right is given by

$$
\left( \begin{array} { l } { x ^ { 1 } } \\ { \vdots } \\ { x ^ { n } } \end{array} \right) \cdot q = \left( \begin{array} { l } { x ^ { 1 } q } \\ { \vdots } \\ { x ^ { n } q } \end{array} \right) .
$$

With this convention, a quaternion linear map $A \colon  { \mathbb { H } } ^ { n } \to  { \mathbb { H } } ^ { m }$ , i.e., an additive map satisfying $A ( v q ) = A ( v ) q$ , can be represented by an m-by-n matrix of quaternions acting via matrix multiplication on the $l e f t .$

Let $\boldsymbol { H } \colon \mathbb { H } ^ { n } \times \mathbb { H } ^ { n }  \mathbb { H }$ be the “quaternion Hermitian” inner product given by

$$
{ \cal H } ( z , w ) = \bar { z } w = \bar { z } ^ { 1 } w ^ { 1 } + \cdot \cdot \cdot + \bar { z } ^ { n } w ^ { n } .
$$

Then by our conventions, we have

$$
H ( z q , w ) = \bar { q } H ( z , w ) \qquad \mathrm { a n d } \qquad H ( z , w q ) = H ( z , w ) q .
$$

We also have ${ \cal H } ( z , w ) = \overline { { { \cal H } ( w , z ) } }$ , just as before.

We define $\operatorname { S p } ( n ) \subset \operatorname { G L } ( n , \mathbb { H } )$ to be the group of H-linear transformations of $\mathbb { H } ^ { n }$ that preserve $H , { \mathrm { i . e . , } } H ( A z , A w ) = H ( z , w )$ for all $z , w \in \mathbb { H } ^ { n }$ . It is easy to see that

$$
\begin{array} { r } { \mathrm { S p } ( n ) = \left\{ A \in \mathrm { G L } ( n , \mathbb { H } ) \vert ^ { t } \bar { A } A = I _ { n } \right\} . } \end{array}
$$

I leave as an exercise for the reader to show that $\operatorname { S p } ( n )$ is a compact Lie group of dimension $2 n ^ { 2 } + n$ . Also, it is not difficult to show that $\operatorname { S p } ( n )$ is connected and acts irreducibly on $\mathbb { H } ^ { n }$ . (see the Exercises)

Now H can be split into one real and three imaginary parts as

$$
H ( z , w ) = \langle z , w \rangle + \Omega _ { 1 } ( z , w ) i + \Omega _ { 2 } ( z , w ) j + \Omega _ { 3 } ( z , w ) k .
$$

It is clear from the relations above that $\langle , \rangle$ is symmetric and positive definite and that each of the $\Omega _ { a }$ is skew-symmetric. Moreover, we have the following identities:

$$
\langle z , w \rangle = \Omega _ { 1 } ( z , w i ) = \Omega _ { 2 } ( z , w j ) = \Omega _ { 3 } ( z , w k )
$$

and

$$
\begin{array} { r } { \Omega _ { 2 } ( z , w i ) = \Omega _ { 3 } ( z , w ) } \\ { \Omega _ { 3 } ( z , w j ) = \Omega _ { 1 } ( z , w ) } \\ { \Omega _ { 1 } ( z , w k ) = \Omega _ { 2 } ( z , w ) . } \end{array}
$$

Proposition 1: The subgroup of ${ \mathrm { G L } } ( 4 n , \mathbb { R } )$ that fixes the three 2-forms $\left( \Omega _ { 1 } , \Omega _ { 2 } , \Omega _ { 3 } \right)$ is equal to $\operatorname { S p } ( n )$

Proof: Let $G \subset \operatorname { G L } ( 4 n , \mathbb { R } )$ be the subgroup that fixes each of the $\Omega _ { a }$ . Clearly we have $\mathrm { S p } ( n ) \subset G$

Now, from the first of the identities above, it follows that each of the forms $\Omega _ { a }$ is non-degenerate. Then, from the second set of these identities, it follows that the subgroup G must also fix the linear transformations of $\mathbb { R } ^ { 4 n }$ that represent multiplication on the right by $i , j ,$ , and k. Of course, this, by definition, implies that G is a subgroup of $\operatorname { G L } ( n , \mathbb { H } )$ Returning to the first of the identities, it also follows that G must preserve the inner product defined by h, i. Finally, since we have now seen that G must preserve all of the components of H, it follows that G must preserve H as well. However, this was the very definition of $\operatorname { S p } ( n )$ . 

Proposition 1 motivates the way we will want to define HyperK¨ahler structures on manifolds: as triples of 2-forms that satisfy certain conditions. Here is the linear algebra definition on which the manifold definition will be based.

Definition 5: Let V be a vector space over R. A hyperK¨ahler structure on V is a choice of a triple of non-degenerate 2-forms $( \Omega _ { 1 } , \Omega _ { 2 } , \Omega _ { 3 } )$ that satisfy the following properties: First, the linear maps $R _ { i } , R _ { j }$ that are defined by the equations

$$
\begin{array} { r } { \Omega _ { 2 } ( v , R _ { i } w ) = \Omega _ { 3 } ( v , w ) \qquad \Omega _ { 1 } ( v , R _ { j } w ) = - \Omega _ { 3 } ( v , w ) } \end{array}
$$

satisfy $\left( R _ { i } \right) ^ { 2 } = \left( R _ { j } \right) ^ { 2 } = - i d$ and skew-commute, i.e., $R _ { i } R _ { j } = - R _ { j } R _ { i }$ . Second, if we set $R _ { k } = - R _ { i } R _ { j }$ , then

$$
\Omega _ { 1 } ( v , R _ { i } w ) = \Omega _ { 2 } ( v , R _ { j } w ) = \Omega _ { 3 } ( v , R _ { k } w ) = \langle v , w \rangle
$$

where h, i (which is defined by these equations) is a positive definite symmetric bilinear form on V . The inner product h, i is called the associated metric on V .

This may seem to be a rather cumbersome definition (and I admit that it is), but it is sufficient to prove the following Proposition (which I leave as an exercise for the reader).

Proposition 2: $I f \left( \Omega _ { 1 } , \Omega _ { 2 } , \Omega _ { 3 } \right)$ is a hyperK¨ahler structure on a real vector space V , then dim $( V ) = 4 n$ for some n and, moreover, there is an R-linear isomorphism of V with Hn that identifies the hyperK¨ahler structure on V with the standard one on $\mathbb { H } ^ { n }$ 

We are now ready for the analogs of Definitions 3 and 4:

Definition 6: If M is a manifold of dimension 4n, an almost hyperK¨ahler structure on M is a triple $( \Omega _ { 1 } , \Omega _ { 2 } , \Omega _ { 3 } )$ of 2-forms on M that have the property that they induce a hyperK¨ahler structure on each tangent space $T _ { m } M$

Definition 7: An almost hyperK¨ahler structure $\left( \Omega _ { 1 } , \Omega _ { 2 } , \Omega _ { 3 } \right)$ on a manifold $M ^ { 4 n }$ is a hyperK¨ahler structure on M if each of the forms $\Omega _ { a }$ is closed.

At first glance, Definition 7 may seem surprising. After all, it appears to place no conditions on the almost complex structures $R _ { i } , R _ { j }$ , and $R _ { k }$ that are defined on M by the almost hyperK¨ahler structure on M and one would surely want these to be integrable if the analogy with K¨ahler geometry is to be kept up. The nice result is that the integrability of these structures comes for free:

Theorem 4: For an almost hyperK¨ahler structure $\left( \Omega _ { 1 } , \Omega _ { 2 } , \Omega _ { 3 } \right)$ on a manifold $M ^ { 4 n }$ , the following are equivalent:

(1) $d \Omega _ { 1 } = d \Omega _ { 2 } = d \Omega _ { 3 } = 0 .$

(2) Each of the 2-forms $\Omega _ { a }$ is parallel with respect to the Levi-Civita connection of the associated metric.

(3) Each of the almost complex structures $R _ { i } , R _ { j }$ , and $R _ { k }$ are integrable.

Proof: (Idea) The proof of Theorem 4 is much like the proof of Theorem 2. One shows by local calculations in Gauss normal coordinates at any point on M that the covariant derivatives of the forms $\Omega _ { a }$ with respect to the Levi-Civita connection of the associated metric can be expressed in terms of the coefficients of their exterior derivatives and viceversa. Similarly, one shows that the formulas for the Nijenhuis tensors of the three almost complex structures on M can be expressed in terms of the covariant derivatives of the three 2-forms and vice-versa. This is a rather formidable linear algebra problem, but it is nothing more. I will not do the computation here. 

Note that Theorem 4 implies that the holonomy H of the associated metric of a hyperK¨ahler structure on $M ^ { 4 n }$ must be a subgroup of $\operatorname { S p } ( n )$ . If H is a proper subgroup of $\operatorname { S p } ( n )$ , then by Theorem 1, the associated metric must be locally a product metric. Now, as is easy to verify, the only products from Berger’s List that can appear as subgroups of $\operatorname { S p } ( n )$ are products of the form

$$
\{ e \} _ { n _ { 0 } } \times \mathrm { S p } ( n _ { 1 } ) \times \cdots \times \mathrm { S p } ( n _ { k } )
$$

where $\{ e \} _ { n _ { 0 } } \subset \mathrm { S p } ( n _ { 0 } )$ is just the identity subgroup and $n = n _ { 0 } + \cdot \cdot \cdot + n _ { k }$ . Thus, it follows that a hyperK¨ahler structure can be decomposed locally into a product of the ‘flat’ example with hyperK¨ahler structures whose holonomy is the full $\mathrm { S p } ( n _ { i } )$ . (If M is simply connected and the associated metric is complete, then the de Rham Splitting Theorem asserts that M can be globally written as a product of such metrics.) This motivates our calling a hyperK¨ahler structure on $M ^ { 4 n }$ irreducible if its holonomy is equal to $\operatorname { S p } ( n )$

The reader may be wondering just how common these hyperK¨ahler structures are (aside from the flat ones of course). The answer is that they are not so easy to come by. The first known non-flat example was the Eguchi-Hanson metric (often called a “gravitational instanton”) on $T ^ { * } \mathbb { C P } ^ { 1 }$ . The first known irreducible example in dimensions greater than 4 was discovered by Eugenio Calabi, who, working independently from Eguchi and Hanson, constructed an irreducible hyperK¨ahler structure on $T ^ { * } \mathbb { C P } ^ { n }$ for each n that happened to agree with the Eguchi-Hanson metric for $n = 1$ . (We will see Calabi’s examples a little further on.)

The first known compact example was furnished by Yau’s solution of the Calabi Conjecture:

Example: K3 Surfaces. A K3 surface is a compact simply connected 2-dimensional complex manifold S with trivial canonical bundle. What this latter condition means is that there is nowhere-vanishing holomorphic 2-form Υ on S. An example of such a surface is a smooth algebraic surface of degree 4 in $\mathbb { C P } ^ { 3 }$ •

A fundamental result of Siu [Si] is that every K3 surface is K¨ahler, i.e., that there exists a 2-form Ω on S so that the hermitian structure $( \Omega , J )$ on S is actually K¨ahler. Moreover, Yau’s solution of the Calabi Conjecture implies that Ω can be chosen so that Υ is parallel with respect to the Levi-Civita connection of the associated metric.

Multiplying Υ by an appropriate constant, we can arrange that $2 \Omega ^ { 2 } = \Upsilon \wedge \overline { { \Upsilon } }$ . Since $\Omega \wedge \Upsilon = 0$ and $\Upsilon \wedge \Upsilon = 0$ , it easily follows (see the Exercises) that if we write $\Omega = \Omega _ { 1 }$ and $\Upsilon = \Omega _ { 2 } - \iota \Omega _ { 3 }$ , then the triple $\left( \Omega _ { 1 } , \Omega _ { 2 } , \Omega _ { 3 } \right)$ defines a hyperK¨ahler structure on S.

For a long time, the K3 surfaces were the only known compact manifolds with hyperK¨ahler structures. In fact, a “proof” was published showing that there were no other compact ones. However, this turned out not to be correct.

Example: Let $M ^ { 4 n }$ be a simply connected, compact complex manifold (of complex dimension $2 n )$ with a holomorphic symplectic form Υ. Then $\Upsilon ^ { n }$ is a non-vanishing holomorphic volume form, and hence the canonical bundle of M is trivial. If M has a K¨ahler structure that is compatible with its complex structure, then, by Yau’s solution of the Calabi Conjecture, there is a K¨ahler metric $g$ on M for which the volume form $\Upsilon ^ { n }$ is parallel. This implies that the holonomy of g is a subgroup of SU(2n). However, this in turn implies that g is Ricci-flat and hence, by a Bochner vanishing argument, that every holomorphic form on M is parallel with respect to $g .$ . Thus, Υ is also parallel with respect to g and hence the holonomy is a subgroup of $\operatorname { S p } ( n )$ . If M can be constructed in such a way that it cannot be written as a non-trivial product of complex submanifolds, then the holonomy of g must act irreducibly on $\mathbb { C } ^ { 2 n }$ and hence must equal $\operatorname { S p } ( n )$

Fujita was the first to construct a simply connected, compact complex 4-manifold that carried a holomorphic 2-form and that could not be written non-trivially as a product. This work is written up in detail in a survey article by [Bea].

HyperK¨ahler Reduction. I am now ready to describe another method of constructing hyperK¨ahler structures, known as hyperK¨ahler reduction. This method first appeared in a famous paper by Hitchin, Karlhede, Lindstr¨om, and Roˇcek, [HKLR].

Theorem 5: Suppose that $( \Omega _ { 1 } , \Omega _ { 2 } , \Omega _ { 3 } )$ is a hyperK¨ahler structure on M and that there is a left action $\lambda \colon G \times M \to M$ that is Poisson with respect to each of the three symplectic forms $\Omega _ { a }$ . Let

$$
\mu = ( \mu _ { 1 } , \mu _ { 2 } , \mu _ { 3 } ) \colon M \to { \mathfrak { g } } ^ { * } \oplus { \mathfrak { g } } ^ { * } \oplus { \mathfrak { g } } ^ { * }
$$

be a G-equivariant momentum mapping. Suppose that $\boldsymbol { 0 } \in \mathfrak { g } ^ { * } \oplus \mathfrak { g } ^ { * } \oplus \mathfrak { g } ^ { * }$ is a clean value for $\mu$ and that the quotient $M _ { 0 } = G \backslash \mu ^ { - 1 } ( 0 )$ has a smooth structure for which the projection $\pi _ { 0 } \colon \mu ^ { - 1 } ( 0 ) \to M _ { 0 }$ is a smooth submersion. Then there is a unique hyperK¨ahler structure $( \Omega _ { 1 } ^ { 0 } , \Omega _ { 2 } ^ { 0 } , \Omega _ { 3 } ^ { 0 } )$ on $M _ { 0 }$ with the property that $\pi _ { 0 } ^ { * } ( \Omega _ { a } ^ { 0 } )$ is the pull back of $\Omega _ { a }$ to $\mu ^ { - 1 } ( 0 ) \subset M$ for each $a = 1 , 2$ , or 3.

Proof: Assume the hypotheses of the Theorem. Let $\tilde { \Omega } _ { a } ^ { 0 }$ be the pullback of $\Omega _ { a }$ to $\mu ^ { - 1 } ( 0 ) \subset$ M . It is clear that each of the forms $\tilde { \Omega } _ { a } ^ { 0 }$ is a closed, G-invariant 2-form on $\mu ^ { - 1 } ( 0 )$

I first want to show that each of these can be written as a pullback of a 2-form on $M _ { 0 }$ , i.e., that each is semi-basic for $\pi _ { 0 }$ . To do this, I need to characterize $T _ { m } \mu ^ { - 1 } ( 0 )$ in an appropriate fashion. Now, the assumption that 0 be a clean value for $\mu$ implies $\mu ^ { - 1 } ( 0 )$ is a smooth submanifold of M and that for $m \in \mu ^ { - 1 } ( 0 )$ any $v \in T _ { m } M$ lies in $T _ { m } \mu ^ { - 1 } ( 0 )$ if and only if $\Omega _ { a } { \left( v , \lambda _ { * } ( x ) ( m ) \right) } = 0$ for all $x \in { \mathfrak { g } }$ and all three values of a. Thus,

$$
T _ { m } \mu ^ { - 1 } ( 0 ) = \{ v \in T _ { m } M | \langle v , w i \rangle = \langle v , w j \rangle = \langle v , w k \rangle = 0 , { \mathrm { ~ f o r ~ a l l ~ } } w \in T _ { m } G \cdot m \} .
$$

Also, by G-equivariance, $G \cdot m \subset \mu ^ { - 1 } ( 0 )$ and hence $T _ { m } G { \cdot } m \subset T _ { m } { \mu } ^ { - 1 } ( 0 )$ . It follows that $v \in T _ { m } G \cdot$ m implies that v is in the null space of each of the forms $\tilde { \Omega } _ { a } ^ { 0 }$ . Thus, each of the forms $\tilde { \Omega } _ { a } ^ { 0 }$ is semi-basic for $\pi _ { 0 }$ , as we wished to show. This, combined with G-invariance, implies that there exist unique forms $\Omega _ { a } ^ { 0 }$ on $M _ { 0 }$ that satisfy $\pi _ { 0 } ^ { * } ( \Omega _ { a } ^ { 0 } ) = \tilde { \Omega } _ { a } ^ { 0 }$ . Since $\pi _ { 0 }$ is a submersion, the three 2-forms $\Omega _ { a } ^ { 0 }$ are closed.

To complete the proof, it suffices to show that the triple $( \Omega _ { 1 } ^ { 0 } , \Omega _ { 2 } ^ { 0 } , \Omega _ { 3 } ^ { 0 } )$ actually defines an almost hyperK¨ahler structure on $M _ { 0 }$ , for then we can apply Theorem 4.

We do this as follows: Use the associated metric $\langle , \rangle$ to define an orthogonal splitting

$$
T _ { m } \mu ^ { - 1 } ( 0 ) = T _ { m } G { \cdot } m \oplus H _ { m } .
$$

By the hypotheses of the theorem, the fibers of $\pi _ { 0 }$ are the G-orbits in $\mu ^ { - 1 } ( 0 )$ and, for each $m \in \mu ^ { - 1 } ( 0 )$ , the kernel of the differential $\pi _ { 0 } ^ { \prime } ( m )$ is $T _ { m } G { \cdot } m$ . Thus, $\pi _ { 0 } ^ { \prime } ( m )$ induces an isomorphism from $H _ { m }$ to $T _ { \pi _ { 0 } ( m ) } M _ { 0 }$ and, under this isomorphism, the restriction of the form $\tilde { \Omega } _ { a } ^ { 0 }$ to $H _ { m }$ is identified with $\Omega _ { a } ^ { 0 }$

Thus, it suffices to show that the forms $( \tilde { \Omega } _ { 1 } ^ { 0 } , \tilde { \Omega } _ { 2 } ^ { 0 } , \tilde { \Omega } _ { 3 } ^ { 0 } )$ define a hyperK¨ahler structure when restricted to $H _ { m }$ . By Proposition 2, to do this, it would suffice to show that $H _ { m }$ is stable under the actions of $R _ { i } , \ R _ { j }$ , and $R _ { k }$ . However, by definition, $H _ { m }$ is the subspace of $T _ { m } M$ that is orthogonal to the H-linear subspace $( T _ { m } G { \cdot } m ) \cdot \mathbb { H } \subset T _ { m } M$ . Since the orthogonal complement of an H-linear subspace of $T _ { m } \dot { M }$ is also an H-linear subspace, we are done. 

Note that the proof also shows that the dimension of the reduced space $M _ { 0 }$ is equal to dim $M - 4 \dim ( G / G _ { m } )$ , since, at each point $m \in \mu ^ { - 1 } ( 0 )$ , the space $T _ { m } G { \cdot } m$ is perpendicular to $R _ { i } \big ( T _ { m } G \cdot m \big ) \oplus R _ { j } \big ( T _ { m } G \cdot m \big ) \oplus R _ { k } \big ( T _ { m } G \cdot m \big )$ and this latter direct sum is orthogonal.

Unfortunately, it frequently happens that 0 is not a clean value of $\mu _ { ; }$ in which case, Theorem 5 cannot be applied to the action. Moreover, there does not appear to be any simple way to perform hyperK¨ahler reduction at the general clean value of $\mu$ in ${ \mathfrak { g } } ^ { * } \oplus { \mathfrak { g } } ^ { * } \oplus { \mathfrak { g } } ^ { * }$ (in marked contrast to the K¨ahler case). In fact, for the general clean value $\boldsymbol { \xi } \in \mathfrak { g } ^ { * } \oplus \mathfrak { g } ^ { * } \oplus \mathfrak { g } ^ { * }$ of $\mu ,$ the quotient space $M _ { \xi } = G _ { \xi } \backslash \mu ^ { - 1 } ( \xi )$ need not even have its dimension be divisible by 4. (See the Exercises for a cautionary example.)

However, if $[ { \mathfrak { g } } , { \mathfrak { g } } ] ^ { \perp } \subset { \mathfrak { g } } ^ { * }$ denotes the annihilator of $[ { \mathfrak { g } } , { \mathfrak { g } } ]$ in g, then the points $\xi \in [ { \mathfrak { g } } , { \mathfrak { g } } ] ^ { \perp }$ are the fixed points of the coadjoint action of G. It is then possible to perform hyperK¨ahler reduction at any clean value $\xi = ( \xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } ) \in [ { \mathfrak { g } } , { \mathfrak { g } } ] ^ { \perp } \oplus [ { \mathfrak { g } } , { \mathfrak { g } } ] ^ { \perp } \oplus [ { \mathfrak { g } } , { \mathfrak { g } } ] ^ { \perp }$ since, in this case, we again have $G _ { \xi } = G _ { \cdot }$ , and so the argument in the proof above that $H _ { m } \subset T _ { m } \mu ^ { - 1 } ( \xi )$ is a quaternionic subspace for each $m \in T _ { m } \mu ^ { - 1 } ( \xi )$ is still valid. Of course, this is not really much of a generalization, since reduction at such $\mathrm { ~ a ~ } \xi$ is simply reduction at 0 for the modified (but still G-equivariant) momentum mapping $\mu ^ { \xi } = \mu - \xi$

Example: One of the simplest things to do is take $M = \mathbb { H } ^ { n }$ and let $G \subset \operatorname { S p } ( n )$ be a closed subgroup. It is not difficult to show (see the Exercises) that the standard hyperK¨ahler structure on $\mathbb { H } ^ { n }$ has its three 2-forms given by

$$
i \Omega _ { 1 } + j \Omega _ { 2 } + k \Omega _ { 3 } = \frac { 1 } { 2 } { } ^ { t } d \bar { q } \wedge d q
$$

where $q : \mathbb { H } ^ { n } \to \mathbb { H } ^ { n }$ is the identity, thought of as a $\mathbb { H } ^ { n }$ -valued function on $\mathbb { H } ^ { n }$ . Using this formula, it is easy to show that the standard left action of $\operatorname { S p } ( n )$ on $\mathbb { H } ^ { n }$ is Poisson, with momentum mapping $\mu : \mathbb { H } ^ { n } \to { \mathfrak { s p } } ( n ) \oplus { \mathfrak { s p } } ( n ) \oplus { \mathfrak { s p } } ( n )$ given by the formula\*

$$
\mu ( q ) = \frac { 1 } { 2 } \big ( q i { } ^ { t } \bar { q } , q j ^ { t } \bar { q } , q k ^ { t } \bar { q } \big ) .
$$

Note that 0 is not a clean value of $\mu$ with respect to the full action of $\operatorname { S p } ( n )$ . However, the situation can be very different for a closed subgroup $G \subset \operatorname { S p } ( n )$ : Let $\pi _ { \mathfrak { g } } : { \mathfrak { s p } } ( n ) \to { \mathfrak { g } }$ be the orthogonal projection relative to the Ad-invariant inner product on ${ \mathfrak { s p } } ( n )$ . The momentum mapping for the action of G on $\mathbb { H } ^ { n }$ is then given by

$$
\mu _ { G } ( q ) = \frac { 1 } { 2 } \bigl ( \pi _ { \Im } ( q i ^ { t } \bar { q } ) , \pi _ { \Im } ( q j ^ { t } \bar { q } ) , \pi _ { \Im } ( q k ^ { t } \bar { q } ) \bigr ) .
$$

Since $G$ is compact, there is an orthogonal direct sum ${ \mathfrak { g } } = { \mathfrak { z } } \oplus [ { \mathfrak { g } } , { \mathfrak { g } } ]$ , where $\mathfrak { z }$ is the tangent algebra to the center of G. Thus, there will be a hyperK¨ahler reduction for each clean value of $\mu _ { G }$ that lies in z⊕z⊕z.

Let us now consider a very simple example: Let $S ^ { 1 } \subset \operatorname { S p } ( n )$ act diagonally on $\mathbb { H } ^ { n }$ by the action

$$
e ^ { i \theta } \cdot \left( \begin{array} { c } { { q ^ { 1 } } } \\ { { \vdots } } \\ { { q ^ { n } } } \end{array} \right) = \left( \begin{array} { c } { { e ^ { i \theta } q ^ { 1 } } } \\ { { \vdots } } \\ { { e ^ { i \theta } q ^ { n } } } \end{array} \right) .
$$

Then it is not difficult to see that the momentum mappping can be identified with the map

$$
\mu ( q ) = \stackrel { t _ { \overline { { { q } } } } } { { q } } i q .
$$

The reduced space $M _ { p }$ for any $p \neq 0$ is easily seen to be complex analytically equivalent to $T ^ { * } \mathbb { C P } ^ { n - 1 }$ , and the induced hyperK¨ahler structure is the one found by Calabi. In particular, for $n = 2$ , we recover the Eguchi-Hansen metric.

In the Exercises, there are other examples for you to try.

The method of hyperK¨ahler reduction has a wide variety of applications. Many of the interesting moduli spaces for Yang-Mills theory turn out to have hyperK¨ahler structures because of this reduction procedure. For example, as Atiyah and Hitchin [AH] show, the space of magnetic monopoles of “charge” k on $\mathbb { R } ^ { 3 }$ turns out to have a natural hyperK¨ahler structure that is derived by methods extremely similar to the example presented earlier of a K¨ahler structure on the moduli space of flat connections over a Riemann surface.

Peter Kronheimer [Kr] has used the method of hyperK¨ahler reduction to construct, for each quotient manifold Σ of $S ^ { 3 }$ , an asymptotically locally Euclidean (ALE) Ricci-flat self-dual Einstein metric on a 4-manifold $M _ { \Sigma }$ whose boundary at infinity is Σ. He then went on to prove that all such metrics on 4-manifolds arise in this way.

Finally, it should also be mentioned that the case of metrics on manifolds $M ^ { 4 n }$ with holonomy $\mathrm { S p } ( n ) \cdot \mathrm { S p } ( 1 )$ can also be treated by the method of reduction. I don’t have time to go into this here, but the reader can find a complete account in [GL].

# Exercise Set 8:

# Recent Applications of Reduction

1. Show that the following two definitions of compatibility between an almost complex structure J and a metric g on $M ^ { 2 n }$ are equivalent

(i) $( g , J )$ are compatible if $g ( v ) = g ( J v )$ for all $v \in T M$

(ii) $( g , J )$ are compatible if $\Omega ( v , w ) = \langle J v , w \rangle$ defines a (skew-symmetric) 2-form on M .

2. A Non-Integrable Almost Complex Structure. Let J be an almost complex structure on M . Let $\mathcal { A } ^ { 1 , 0 } \subset \mathbb { C } \otimes \mathcal { A } ^ { 1 } ( M )$ denote the space of C-valued 1-forms on M that satisfy $\alpha ( J v ) = \iota \alpha ( v )$ for all $v \in T M$

(i) Show that if we define $\mathcal { A } ^ { 0 , 1 } ( M ) \subset \mathbb { C } \otimes \mathcal { A } ^ { 1 } ( M )$ to be the space of C-valued 1-forms on M that satisfy $\alpha ( J v ) = - \iota \alpha ( v )$ for all $v \in T M$ , then $\mathcal { A } ^ { 0 , 1 } ( M ) = \overline { { \mathcal { A } ^ { 1 , 0 } ( M ) } }$ and that $\mathcal { A } ^ { 1 , 0 } ( M ) \cap \mathcal { A } ^ { 0 , 1 } ( \dot { M } ) = \{ 0 \}$

(ii) Show that if J is an integrable almost complex structure, then, for any $\alpha \in \mathcal { A } ^ { 1 , 0 } ( M )$ the 2-form dα is (at least locally) in the ideal generated by $A ^ { 1 , 0 } ( M )$ (Hint: Show that, if $z : U \to \mathbb { C } ^ { n }$ is a holomorphic coordinate chart, then, on U, the space $\mathcal { A } ^ { 1 , 0 } ( U )$ is spanned by the forms $d z ^ { 1 } , \ldots , d z ^ { n }$ . Now consider the exterior derivative of any linear combination of the $d z ^ { i } . )$

It is a celebrated result of Newlander and Nirenberg that this condition is sufficient for J to be integrable.

(iii) Show that there is an almost complex structure on $\mathbb { C } ^ { 2 }$ for which $\mathcal { A } ^ { 1 , 0 } ( \mathbb { C } ^ { 2 } )$ is spanned by the 1-forms

$$
\begin{array} { l } { { \omega ^ { 1 } = d z ^ { 1 } - \bar { z } ^ { 1 } d \bar { z } ^ { 2 } } } \\ { { \omega ^ { 2 } = d z ^ { 2 } } } \end{array}
$$

and that this almost complex structure is not integrable.

3. Let $M = \mathbb { C } ^ { n _ { 1 } } \oplus \mathbb { C } ^ { n _ { 2 } } \setminus \{ ( 0 , 0 ) \}$ . Let $G = S ^ { 1 }$ act on M by the action

$$
e ^ { \imath \theta } \cdot ( z _ { 1 } , z _ { 2 } ) = \left( e ^ { \imath d _ { 1 } \theta } z _ { 1 } , e ^ { \imath d _ { 2 } \theta } z _ { 2 } \right)
$$

where $d _ { 1 }$ and $d _ { 2 }$ are integers. Let M have the standard flat K¨ahler structure. Compute the moment map µ and the K¨ahler structures on the reduced spaces. How do the relative signs of $d _ { 1 }$ and $d _ { 2 }$ affect the answer? What interpretation can you give to these spaces?

4. Go back to the the example of the “K¨ahler structure” on the space $\mathfrak { A } ( P )$ of connections on a principal right G-bundle P over a connected compact Riemann surface Σ. Assume that $G = S ^ { 1 }$ and identify g with R in the natural way. Thus, $F _ { A }$ is a well-defined 2-form on Σ and the cohomology class $[ F _ { A } ] \in H _ { d R } ^ { 2 } ( \Sigma , \mathbb { R } )$ is independent of the choice of A. Assume that $\left[ F _ { A } \right] \neq 0$ Then, in this case, $\mu ^ { - 1 } ( 0 )$ is empty so the construction we made in the example in the Lecture is vacuous. Here is how we can still get some information.

Fix any non-vanishing 2-form Ψ on Σ so that $[ \Psi ] = [ F _ { A } ]$ . Show that even though µ has no regular values, Ψ is a non-trivial clean value of µ. Show also that, for any $A \in \mu ^ { - 1 } ( \Psi )$ the stabilizer ${ \mathsf { G } } _ { A } \subset A { \mathrm { u t } } ( P )$ is a discrete (and hence finite) subgroup of $S ^ { 1 }$ . Describe, as fully as you can, the reduced space ${ \mathfrak { M } } _ { \Psi }$ and its K¨ahler structure.

5. Verify that $\operatorname { S p } ( n )$ is a connected Lie group of dimension $2 n ^ { 2 } + n$ . (Hint: You will probably want to study the function $f ( A ) = { } ^ { t } \bar { A } A = I _ { n } . )$ Show that $\operatorname { S p } ( n )$ acts transitively on the unit sphere $S ^ { \mathrm { 4 } \mathrm { { } } \mathrm { { } } n - 1 } \subset \mathbb { H } ^ { n }$ defined by the relation $H ( x , x ) = 1$ . (Hint: First show that, by acting by diagonal matrices in $\operatorname { S p } ( n )$ , you can move any element of $\mathbb { H } ^ { n }$ into the subspace $\mathbb { R } ^ { n }$ . Then note that $\operatorname { S p } ( n )$ contains $\mathrm { S O } ( n ) . )$ By analysing the stabilizer subgroup in $\operatorname { S p } ( n )$ of an element of $S ^ { 4 n - 1 }$ , show that there is a fibration

$$
\begin{array} { c c c } { { \mathrm { S p } ( n - 1 ) } } & { {  } } & { { \mathrm { S p } ( n ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \downarrow } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { S ^ { 4 n - 1 } } } \end{array}
$$

and use this to conclude by induction that $\operatorname { S p } ( n )$ is connected and simply connected for all n.

6. Prove Proposition 2. (Hint: First show how the maps $R _ { i } , \ R _ { j }$ , and $R _ { k }$ define the structure of a right H-module on V . Then show that V has a basis $b _ { 1 } , \ldots , b _ { n }$ over H and use this to construct an H-linear isomorphism of V with $\mathbb { H } ^ { n }$ . If you pick the basis $b _ { a }$ carefully, you will be done at this point. Warning: You must use the positive definiteness of h, i!)

7. Determine a formula for the dimension of the Hyperk¨ahler reduced space $M _ { \xi }$ in terms of the dimensions of $M , G , G _ { \xi }$ and $G _ { m }$ (where m lies in $\mu ^ { - 1 } ( \xi ) )$ ).

8. Apply the Hyperk¨ahler reduction procedure to $\mathbb { H } ^ { 2 }$ with R acting by the rule

$$
\theta \cdot \left( \begin{array} { l } { { q ^ { 1 } } } \\ { { q ^ { 2 } } } \end{array} \right) = \left( \begin{array} { l } { { e ^ { i \theta } q ^ { 1 } } } \\ { { q ^ { 2 } + \theta } } \end{array} \right) .
$$

Determine which values of $\mu$ are clean and describe the resulting complex surfaces and their Hyperk¨ahler structures.

## Lecture 9:

## The Gromov School of Symplectic Geometry

In this lecture, I want to describe some of the remarkable new information we have about symplectic manifolds owing to the influence of the ideas of Mikhail Gromov. The basic reference for much of this material is Gromov’s remarkable book Partial Differential Relations.

The fundamental idea of studying complex structures “tamed by” a given symplectic structure was developed by Gromov in a remarkable paper Pseudo-holomorphic Curves on Almost Complex Manifolds and has proved extraordinarily fruitful. In the latter part of this lecture, I will try to introduce the reader to this theory.

## Soft Techniques in Symplectic Manifolds

Symplectic Immersions and Embeddings. Before beginning on the topic of symplectic immersions, let me recall how the theory of immersions in the ordinary sense goes.

Recall that the Whitney Immersion Theorem (in the weak form) asserts that any smooth n-manifold M has an immersion into $\mathbb { R } ^ { 2 n }$ . This result is proved by first immersing M into some $\mathbb { R } ^ { N }$ for $N \gg 0$ and then using Sard’s Theorem to show that if $N > 2 n$ one can find a vector $u \in \mathbb { R } ^ { N }$ so that u is not tangent to $f ( M )$ at any point. Then the projection of $f ( M )$ onto a hyperplane orthogonal to u is still an immersion, but now into $\mathbf { \mathbb { R } } ^ { N - 1 }$ .

This result is not the best possible. Whitney himself showed that one could always immerse $M ^ { n }$ into $\mathbb { R } ^ { 2 n - 1 }$ , although “general position” arguments are not sufficient to do this. This raises the question of determining what the best possible immersion or embedding dimension is.

One topological obstruction to immersing $M ^ { n }$ into $\mathbb { R } ^ { n + k }$ can be described as follows: If $f \colon M \to \mathbf { \tilde { \mathbb { R } } } ^ { n + \asymp }$ is an immersion, then the trivial bundle $f ^ { * } ( T \mathbb { R } ^ { n + k } ) = M \times \mathbb { R } ^ { n + k }$ can be split into a direct sum $f ^ { * } ( T \mathbb { R } ^ { n + k } ) = T M \oplus \nu ^ { f }$ where $\nu ^ { f }$ is the normal bundle of the immersion $f .$ . Thus, if there is no bundle ν of rank k over M so that $T M \oplus \nu$ is trivial, then there can be no immersion of M into $\mathbb { R } ^ { n + k }$

The remarkable fact is that this topological necessary condition is almost sufficient. In fact, we have the following result of Hirsch and Smale for the general immersion problem.

Theorem 1: Let M and N be connected smooth manifolds and suppose either that M is non-compact or else that dim $( M ) < \dim ( N )$ . Let $f \colon M \to N$ be a continuous map, and suppose that there is a vector bundle ν over M so that $f ^ { * } ( T N ) = T M \oplus \nu$ . Then f is homotopic to an immersion of M into N

Theorem 1 can be interpreted as an example of what Gromov calls the h-principle, which I now want to describe.

The h-Principle. Let $\pi \colon V \to X$ be a surjective submersion. A section of $\pi$ is, by definition, a map $\sigma { \colon X }  V$ that satisfies $\pi \circ \sigma = i d _ { X }$ . Let $J ^ { k } ( X , V )$ denote the space of k-jets of sections of V , and let $\pi ^ { k } { \colon } J ^ { k } ( X , V ) \to X$ denote the basepoint or ‘source’ projection. Given any section s of $\pi ,$ there is an associated section $j ^ { k } ( s )$ of $\pi ^ { k }$ that is defined by letting $j ^ { k } ( s ) ( x )$ be the k-jet of s at $x \in X$ . A section σ of $\pi ^ { k }$ is said to be holonomic if $\sigma = j ^ { k } ( s )$ for some section s of π.

A partial differential relation of order k for π is a subset $R \subset J ^ { k } ( X , V )$ . A section s of $\pi$ is said to satisfy R if $j ^ { k } ( s ) ( X ) \subset R$ . We can now make the following definition:

Definition 1: A partial differential relation $R \subset J ^ { k } ( X , V )$ satisfies the h-principle if, for every section $\sigma$ of $\pi ^ { k }$ that satisfies $\sigma ( X ) \subset R$ , there is a one-parameter family of sections $\sigma _ { t } ~ ( 0 \leq t \leq 1 )$ of $\pi ^ { k }$ that satisfy the conditions that $\sigma _ { t } ( X ) \subset R$ for all t, that $\sigma _ { 0 } = \sigma$ , and that $\sigma _ { 1 }$ is holonomic.

Very roughly speaking, a partial differential relation satisfies the h-principle if, whenever the “topological” conditions for a solution to exist are satisfied, then a solution exists.

For example, if $X = M$ and $V = M \times N$ , where $\dim ( N ) \geq \dim ( M )$ , then there is an (open) subset $R = { \mathrm { I m m } } ( M , N ) \subset J ^ { 1 } ( M , M \times N )$ that consists of the 1-jets of graphs of (local) immersions of M into N. What the Hirsch-Smale immersion theory says is that Imm(M, N) satisfies the h-principle if either dim M = dim N and M has no compact component or else dim M < dim N.

Of course, the h-principle does not hold for every relation R. The real question is how to determine when the h-principle holds for a given R. Gromov has developed several extremely general methods for proving that the h-principle holds for various partial differential relations R that arise in geometry. These methods include his theory of topological sheaves and techniques like his method of convex integration. They generally work in situations where the local solutions of a given partial differential relation R are easy to come by and it is mainly a question of ‘patching together’ local solutions which are fairly ‘flexible’.

Gromov calls this collection of techniques ‘soft’ to distinguish them from the ‘hard’ techniques, such as elliptic theory, that come from analysis and deal with situations where the local solutions are somewhat ‘rigid’.

Here is a sample of some of the results that Gromov obtains by these methods:

Theorem 2: Let $X ^ { 2 n }$ be a smooth manifold and let $V \subset \Lambda ^ { 2 } ( T ^ { * } ( M ) )$ denote the open subbundle consisting of non-degenerate 2-forms $\omega \in T _ { x } X$ Let $Z ^ { 1 } ( { \dot { X } } , V ) \subset J ^ { 1 } ( X , V )$ denote the space of 1-jets of closed non-degenerate 2-forms on X. Then, if X has no compact component, $Z ^ { 1 } ( X , V )$ satisfies the h-principle.

In particular, Theorem 2 implies that a non-compact, connected X has a symplectic structure if and only if it has an almost symplectic structure.

Note that this result is definitely not true for compact manifolds. We have already seen several examples, e.g., $S ^ { 1 } \times S ^ { 3 }$ , that have almost symplectic structures but no symplectic structures because they do not satisfy the cohomology ring obstruction. Gromov has asked the following:

Question : $I f X ^ { 2 n }$ is compact and connected and satisfies the condition that there exists an element $u \in H _ { d R } ^ { 2 } ( X , \mathbb { R } )$ that satisfies $u ^ { n } \neq 0$ , does $Z ^ { 1 } ( X , V )$ satisfy the h-principle?

The next result I want to describe is Gromov’s theorem on symplectic immersions. This theorem is an example of a sort of ‘restricted $h { \mathrm { - p r i n c i p l e } } ^ { \prime }$ in that it is only required to apply to sections σ that satisfy specified cohomological conditions.

First, let me make a few definitions: Let $( X , \Xi )$ and $( Y , \Psi )$ be two connected symplectic manifolds. Let ${ \mathcal { S } } ( X , Y ) \subset J ^ { 1 } ( X , X \times Y )$ denote the space of 1-jets of graphs of (local) symplectic maps $f \colon X \to Y$ i.e., (local) maps $f \colon X \to Y$ that satisfy $f ^ { * } ( \Psi ) = \Xi$ . Let $\tau \colon \mathcal { S } ( X , Y )  Y$ be the obvious “target projection”.

Theorem 3: If either X is non-compact, or dim $( X ) < \dim ( Y )$ , then any section σ of ${ \mathcal { S } } ( X , Y )$ for which the induced map $s = \tau \circ \sigma \colon X  Y$ satisfies the cohomological condition $s ^ { * } ( [ \Psi ] ) = [ \Xi ]$ is homotopic to a holonomic section of ${ \mathcal { S } } ( X , Y )$

This result can be also stated as follows: Suppose that either X is non-compact or else that dim $( X ) < \dim ( Y )$ . Let $\phi \colon X \to Y$ be a smooth map that satisfies the cohomological condition $\phi ^ { * } \big ( [ \Psi ] \big ) = [ \Xi ]$ . Suppose that there exists a bundle map $f \colon T X \to \phi ^ { * } ( T Y )$ that is symplectic in the obvious sense. Then $\phi$ is homotopic to a symplectic immersion.

As an application of Theorem 3, we can now prove the following result of Narasimham and Ramanan.

Corollary : Any compact symplectic manifold $( M , \Omega )$ for which the cohomology class [Ω] is integral admits a symplectic immersion into $( \mathbb { C P } ^ { N } , \Omega _ { N } )$ for some $N \gg n$

Proof: Since the cohomology class [Ω] is integral, there exists a smooth map φ: $M \to \mathbb { C P } ^ { N }$ for some N sufficiently large so that $\dot { { \boldsymbol { \phi } } } ^ { * } \big ( [ { \boldsymbol { \Omega } } _ { N } ] \big ) = [ { \boldsymbol { \Omega } } ]$ Then, choosing $N \gg n .$ , we can arrange that there also exists a symplectic bundle map $f \colon T M \to f ^ { * } ( T \mathbb { C P } ^ { N } )$ (see the Exercises). Now apply Theorem 3. 

As a final example along these lines, let me state Gromov’s embedding result. Here, the reader should be thinking of the difference between the Whitney Immersion Theorems and the Whitney Embedding Theorems: One needs slightly more room to embed than to immerse.

Theorem 4: Suppose that $( X , \Xi )$ and $( Y , \Psi )$ are connected symplectic manifolds and that either X is non-compact and dim $( X ) < \dim ( Y )$ or else that dim $( X ) < \dim ( Y ) - 2$ Suppose that there exists a smooth embedding φ: $X  Y$ and that the induced map on bundles φ′: $T X \to \phi ^ { * } ( T Y )$ is homotopic through a 1-parameter family of injective bundle maps $\varphi _ { t } \colon T X \to \phi ^ { * } ( T Y )$ (with $\varphi _ { 0 } = \phi ^ { \prime } )$ to a symplectic bundle map $\varphi _ { 1 } { : } T X \to \phi ^ { * } ( T Y )$ Then $\phi$ is isotopic to a symplectic embedding $\varphi \colon X \to Y$

This result is actually the best possible, for, as Gromov has shown using “hard” techniques (see below), there are counterexamples if one leaves out the dimensional restrictions. Note by the way that, because Theorem 4 deals with embeddings rather than immersions, it not straightforward to place it in the framework of the h-principle.

Blowing $\mathbf { U p }$ in the Symplectic Category. We have already seen in Lecture 6 that certain operations on smooth manifolds cannot be carried out in the symplectic category. For example, one cannot form connected sums in the symplectic category.

However, certain of the operations from the geometry of complex manifolds can be carried out. Gromov has shown how to define the operation of “blowing $\mathrm { u p } ^ { \mathrm { , } }$ in the symplectic category.

Recall how one “blows $\mathrm { u p } ^ { \mathrm { , } }$ the origin in $\mathbb { C } ^ { n }$ . To avoid triviality, let me assume that $n > 1$ . Consider the subvariety

$$
\begin{array} { r } { X = \{ ( v , [ w ] ) \in \mathbb { C } ^ { n } \times \mathbb { C P } ^ { n - 1 } | v \in [ w ] \} \subset \mathbb { C } ^ { n } \times \mathbb { C P } ^ { n - 1 } . } \end{array}
$$

It is easy to see that X is a smooth embedded submanifold of the product and that the projection $\pi \colon X \to \mathbb { C } ^ { n }$ is a biholomorphism away from the “exceptional poin ${ \bf \Phi } , \ " _ { 0 } \in \mathbb { C } ^ { n }$ Moreover, if $\Omega _ { 0 }$ and Φ are the standard K¨ahler 2-forms on $\mathbb { C } ^ { n }$ and $\mathbb { C P } ^ { n - 1 }$ respectively, then, for each $\epsilon > 0$ , the 2-form $\Omega _ { \epsilon } = \Omega _ { 0 } + \epsilon \Phi$ is a K¨ahler 2-form on $X$

Now, Gromov realized that this can be generalized to a “blow $\mathrm { u p } ^ { \mathrm { , } }$ construction for any point p on any symplectic manifold $( M ^ { 2 n } , \Omega )$ . Here is how this goes:

First, choose a neighborhood U of $p$ on which there exists a local chart $z \colon U \to \mathbb { C } ^ { n }$ that is symplectic, i.e., satisfies $z ^ { * } ( \Omega _ { 0 } ) = \Omega$ , and satisfies $z ( p ) = 0$ . Suppose that the ball $B _ { 2 \delta } ( 0 )$ in $\mathbb { C } ^ { n }$ of radius $2 \delta$ centered on 0 lies inside $z ( U )$ . Since $\pi \colon \pi ^ { - 1 } \bigl ( B _ { 2 \delta } ^ { \ast } ( 0 ) \bigr ) \to B _ { 2 \delta } ^ { \ast } ( 0 )$ is a diffeomorphism, there exists a closed 2-form $\tilde { \Phi }$ on $B _ { 2 \delta } ^ { * } ( 0 )$ so that $\pi ^ { * } ( \tilde { \Phi } ) = \Phi$ . Since $H _ { d R } ^ { 2 } { \left( B _ { 2 \delta } ^ { * } ( 0 ) \right) } = 0$ , there exists a 1-form $\varphi$ on $B _ { 2 \delta } ^ { * } ( 0 )$ so that $d \varphi = \Phi$ .

Now consider the family of symplectic forms $\Omega _ { 0 } + \epsilon d \varphi$ on $B _ { 2 \delta } ^ { * } ( 0 )$ . By using a homotopy argument exactly like the one used to Prove Theorem 1 in Lecture 6, it easily follows that for all $t > 0$ sufficiently small, there exists an open annulus $A ( \delta - \varepsilon , \delta + \varepsilon )$ and a oneparameter family of diffeomorphisms $\phi _ { t } \colon A ( \delta - \varepsilon , \delta + \varepsilon ) \to B _ { 2 \delta } ^ { * } ( 0 )$ so that

$$
\phi _ { t } ^ { * } ( \Omega _ { 0 } ) = \Omega _ { 0 } + t d \varphi .
$$

It follows that we can set

$$
\hat { M } = \pi ^ { - 1 } \big ( B _ { \delta + \varepsilon } ^ { * } ( 0 ) \big ) \cup _ { \psi _ { t } } M \setminus z ^ { - 1 } \big ( \phi _ { t } \big ( B _ { \delta - \varepsilon } ^ { * } ( 0 ) \big ) \big )
$$

where

$$
\psi _ { t } \colon \pi ^ { - 1 } \bigl ( A ( \delta - \varepsilon , \delta + \varepsilon ) \bigr )  M \setminus z ^ { - 1 } \bigl ( \phi _ { t } \bigl ( A ( \delta - \varepsilon , \delta + \varepsilon ) \bigr ) \bigr )
$$

is given by $\psi _ { t } = z ^ { - 1 } \circ \phi _ { t } \circ \pi$ Since $\psi _ { t }$ identifies the symplectic structure $\Omega _ { t }$ with $\Omega _ { 0 }$ on the annulus $^ { 6 \circ } \mathrm { o v e r l a p } ^ { \prime \mathrm { \prime } }$ , it follows that $\hat { M }$ is symplectic. This is Gromov’s symplectic blow up procedure. Note that it can be effected in such a way that the symplectic structure on $M \backslash \{ p \}$ is not disturbed outside of an arbitrarily small ball around $p .$ . Note also that there is a parameter involved, and that the symplectic structure is certainly not unique.

This is only describes a simple case. However, Gromov has shown how any compact symplectic submanifold $S ^ { 2 k }$ of $M ^ { 2 n }$ can be blown up to become a symplectic “hypersurface” $\check { S }$ in a new symplectic manifold $\hat { M }$ that has the property that $M \setminus S$ is diffeomorphic to $\hat { M } \setminus \hat { S }$

The basic idea is the same as what we have already done: First, one mimics the topological operations that would be performed if one were blowing up a complex submanifold of a complex manifold. Thus, the submanifold S gets ‘replaced’ by the complex projectivization $\hat { S } = \mathbb { P } N _ { S }$ of a complex normal bundle. Second, one shows how to define a symplectic structure on the resulting smooth manifold that can be made to agree with the old structure outside of an arbitrarily small neighborhood of the blow up.

The details in the general case are somewhat more complicated than the case of blowing up a single point, and Dusa McDuff ([McDuff 1984]) has written out a careful construction. She has also used the method of blow ups to produce an example of a simply connected compact symplectic manifold that has no K¨ahler structure.

Hard Techniques in Symplectic Manifolds.

(Pseudo-) holomorphic curves. I begin with a fundamental definition.

Definition 2: Let $M ^ { 2 n }$ be a smooth manifold and let $J \colon T M \ \to \ T M$ be an almost complex structure on M. For any Riemann surface Σ, we say that a map $f \colon \Sigma  M$ is J-holomorphic if $f ^ { \prime } ( \imath v ) = J f ^ { \prime } ( v )$ for all $v \in T \Sigma$

Often, when J is clear from context, I will simply say $^ { 6 6 } f$ is holomorphic”. Several authors use the terminology “almost holomorphic” or “pseudo-holomorphic” for this concept, reserving the word “holomorphic” for use only when the almost complex structure on M is integrable to an actual complex structure. This distinction does not seem to be particularly useful, so I will not maintain it.

It is instructive to see what this looks like in local coordinates. Let $z = x + \imath y$ be a local holomorphic coordinate on Σ and let $\boldsymbol { w } \colon U \to \mathbb { R } ^ { 2 n }$ be a local coordinate on M. Then there exists a matrix $\boldsymbol { \mathrm { J } } ( \boldsymbol { w } )$ of functions on $w ( U ) \subset \mathbb { R } ^ { 2 n }$ that satisfies $w ^ { \prime } ( J v ) = \boldsymbol { \mathrm { J } } \bigl ( w ( p ) \bigr ) w ^ { \prime } ( v )$ for all $v \in T _ { p } U$ . This matrix of functions satisfies the relation ${ \boldsymbol { \mathrm { J } } } ^ { 2 } = - I _ { 2 n }$ . Now, if $f \colon \Sigma \to M$ is holomorphic and carries the domain of the z-coordinate into U, then $F = w \circ f$ is easily seen to satisfy the first order system of partial differential equations

$$
\frac { \partial F } { \partial y } = \ J ( F ) \frac { \partial F } { \partial x } .
$$

Since ${ \boldsymbol { \mathrm { J } } } ^ { 2 } = - I _ { 2 n }$ , it follows that this is a first-order, elliptic, determined system of partial differential equations for F . In fact, the “principal symbol” of these equations is the same as that for the Cauchy-Riemann equations. Assuming that J is sufficiently regular $( C ^ { \infty }$ is sufficient and we will always have this) there are plenty of local solutions. What is at issue is the nature of the global solutions.

A parametrized holomorphic curve in M is a holomorphic map $f \colon \Sigma \to M$ . Sometimes we will want to consider unparametrized holomorphic curves in M, namely equivalence classes $[ \Sigma , f ]$ of holomorphic curves in M where $( \Sigma _ { 1 } , f _ { 1 } )$ is equivalent to $\left( \Sigma _ { 2 } , f _ { 2 } \right)$ if there exists a holomorphic map $\phi \colon \Sigma _ { 1 }  \Sigma _ { 2 }$ satisfying $f _ { 1 } = f _ { 2 } \circ \phi$

We are going to be particularly interested in the space of holomorphic curves in M. Here are some properties that hold in the case of holomorphic curves in actual complex manifolds and it would be nice to know if they also hold for holomorphic curves in almost complex manifolds.

Local Finite Dimensionality. If Σ is a compact Riemann surface, and $f \colon \Sigma \to M$ is a holomorphic curve, it is reasonable to ask what the space of “nearby” holomorphic curves looks like. Because the equations that determine these mappings are elliptic and because Σ is compact, it follows without too much difficulty that the space of nearby holomorphic curves is finite dimensional. (We do not, in general know that it is a smooth manifold!)

Intersections. A pair of distinct complex curves in a complex surface always intersect at isolated points and with positive “multiplicity.” This follows from complex analytic geometry. This result is extremely useful because it allows us to derive information about actual numbers of intersection points of holomorphic curves by applying topological intersection formulas. (Usually, these topological intersection formulas only count the number of signed intersections, but if the surfaces can only intersect positively, then the topological intersection numbers (counted with multiplicity) are the actual intersection numbers.)

Kahler Area Bounds. ¨ If M happens to be a K¨ahler manifold, with K¨ahler form Ω, then the area of the image of a holomorphic curve f: Σ → M is given by the formula

$$
\mathrm { A r e a } \big ( f ( \Sigma ) \big ) = \int _ { \Sigma } f ^ { * } ( \Omega ) .
$$

In particular, since Ω is closed, the right hand side of this equation depends only on the homotopy class of f as a map into M. Thus, if $\textstyle ( \sum _ { t } , f _ { t } )$ is a continuous one-parameter family of closed holomorphic curves in a K¨ahler manifold, then they all have the same area. This is a powerful constraint on how the images can behave, as we shall see.

Now the first two of these properties go through without change in the case of almost complex manifolds.

In the case of local finiteness, this is purely an elliptic theory result. Studying the linearization of the equations at a solution will even allow one to predict, using the Atiyah-Singer Index Theorem, an upper bound for the local dimension of the moduli space and, in some cases, will allow us to conclude that the moduli space near a given closed curve is actually a smooth manifold (see below).

As for pairs of complex curves in an almost complex surface, Gromov has shown that they do indeed only intersect in isolated points and with positive multiplicity (unless they have a common component, of course). Both Gromov and Dusa McDuff have used this fact to study the geometry of symplectic 4-manifolds.

The third property is only valid for K¨ahler manifolds, but it is highly desirable. The behaviour of holomorphic curves in compact K¨ahler manifolds is well understood in a large part because of this area bound. This motivated Gromov to investigate ways of generalizing this property.

Symplectic Tamings. Following Gromov, we make the following definition.

Definition 3: A symplectic form Ω on M tames an almost complex structure J if it is J-positive, i.e., if it satisfies $\Omega ( v , J v ) > 0$ for all non-zero tangent vectors $v \in T M$

The reader should be thinking of K¨ahler geometry. In that case, the symplectic form Ω and the complex structure J satisfy $\Omega ( v , J v ) = \langle v , v \rangle > 0$ . Of course, this generalizes to the case of an arbitrary almost K¨ahler structure.

Now, if M is compact and Ω tames J, then for any Riemannian metric g on $M$ (not necessarily compatible with either J or Ω) there is a constant $C > 0$ so that

$$
| v \wedge J v | \leq C \Omega ( v , J v )
$$

where $| v \land J v |$ represents the area in $T _ { p } M$ of the parallelogram spanned by v and Jv in $T _ { p } M$ (see the Exercises). In particular, it follows that, for any holomorphic curve $f \colon \Sigma \to M$ we have the inequality

$$
\mathrm { A r e a } \big ( f ( \Sigma ) \big ) \leq C \int _ { \Sigma } f ^ { * } ( \Omega ) .
$$

Just as in the K¨ahler case, the integral on the right hand side depends only on the homotopy class of f. Thus, if an almost complex structure can be tamed, it follows that, in any metric on M, there is a uniform upper bound on the areas of the curves in any continuous family of compact holomorphic curves in M.

Example: Let $N _ { 3 } ^ { \mathbb { C } }$ denote the complex Heisenberg group. Thus, $N _ { 3 } ^ { \mathbb { C } }$ is the complex Lie group of matrices of the form

$$
g = { \left( \begin{array} { l l l } { 1 } & { x } & { z } \\ { 0 } & { 1 } & { y } \\ { 0 } & { 0 } & { 1 } \end{array} \right) } ~ .
$$

Let $\Gamma \subset N _ { 3 } ^ { \mathbb { C } }$ be the subgroup all of whose entries belong to the ring of Gaussian integers $\mathbb { Z } [ i ]$

Let $M = N _ { 3 } ^ { \mathbb { C } } / \Gamma$ . Then M is a compact complex 3-manifold. I claim that the complex structure on M cannot be tamed by any symplectic form.

To see this, consider the right-invariant 1-form

$$
d g g ^ { - 1 } = \left( \begin{array} { c c c } { { 0 } } & { { \omega _ { 1 } } } & { { \omega _ { 3 } } } \\ { { 0 } } & { { 0 } } & { { \omega _ { 2 } } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) .
$$

Since they are right-invariant, it follows that the complex 1-forms $\omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 }$ are also welldefined on M. Define the metric G on M to be the quadratic form

$$
G = \omega _ { 1 } \circ \overline { { \omega _ { 1 } } } + \omega _ { 2 } \circ \overline { { \omega _ { 2 } } } + \omega _ { 3 } \circ \overline { { \omega _ { 3 } } } .
$$

Now consider the holomorphic curve $Y \colon \mathbb { C } \to N _ { 3 } ^ { \mathbb { C } }$ defined by

$$
Y ( y ) = \left( \begin{array} { l l l } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { y } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) .
$$

Let $\psi : \mathbb { C } \to M$ be the composition. It is clear that $\psi$ is doubly periodic and hence defines an embedding of a complex torus into M. It is clear that the G-area of this torus is 1.

Now $N _ { 3 } ^ { \mathbb { C } }$ acts holomorphically on M on the left (not by G-isometries, of course). We can consider what happens to the area of the torus $\psi ( \mathbb { C } )$ under the action of this group. Specifically, for $x \in \mathbb { C }$ , let $\psi _ { x }$ denote $\psi$ acted on by left multiplication by the matrix

$$
\left( \begin{array} { c c c } { { 1 } } & { { x } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) .
$$

Then, as the reader can easily check, we have

$$
\psi _ { x } ^ { * } ( G ) = { \big ( } 1 + | x | ^ { 2 } { \big ) } { \big | } d y { \big | } ^ { 2 } .
$$

Thus, the G-area of the torus $\psi _ { x } ( \mathbb { C } )$ goes off to infinity as x tends to infinity. Obviously, there can be no taming of the complex manifold M. (In particular, M cannot carry a K¨ahler structure compatible with its complex structure.)

Gromov’s Compactness Theorem. In this section, I want to discuss Gromov’s approach to compactifying the connected components of the space of unparametrized holomorphic curves in M .

Example: Before looking at the general case, let us look at what happens in a very familiar case: The case of algebraic curves in $\mathbb { C P } ^ { 2 }$ with its standard Fubini-Study metric and symplectic form Ω (normalized so as to give the lines in $\mathbb { C P } ^ { 2 }$ an area of 1).

Since this is a K¨ahler metric, we know that the area of a connected one-parameter family of holomorphic curves $\textstyle ( \sum _ { t } , f _ { t } )$ in $\mathbb { C P } ^ { 2 }$ is constant and is equal to an integer $d =$ $\int _ { \Sigma _ { t } } f _ { t } ^ { * } ( \Omega )$ called the degree. To make matters as simple as possible, let me consider the curves degree by degree.

$d = 0$ . In this case, the “curves” are just the constant maps and (in the unparametrized case) clearly constitute a copy of $\mathbb { C P } ^ { 2 }$ itself. Note that this is already compact.

$d = 1$ . In this case, the only possibility is that each $\Sigma _ { t }$ is just $\mathbb { C P } ^ { 1 }$ and the holomorphic map $f _ { t }$ must be just a biholomorphism onto a line in $\mathbb { C P } ^ { 2 }$ Of course, the space of lines in $\mathbb { C P } ^ { 2 }$ is compact, just being a copy of the dual $\mathbb { C P } ^ { 2 }$ . Thus, the space ${ \mathfrak { M } } _ { 1 }$ of unparametrized holomorphic curves in $\mathbb { C P } ^ { 2 }$ is compact. Note, however, that the space ${ \mathfrak { H } } _ { 1 }$ of holomorphic maps $f \colon { \bar { \mathbb { C P } } } ^ { 1 } \to \mathbb { C P } ^ { 2 }$ of degree 1 is not compact. In fact, the fibers of the natural map ${ \mathfrak { H } } _ { 1 } \to { \mathfrak { M } } _ { 1 }$ are copies of $\operatorname { A u t } ( \mathbb { C P } ^ { 1 } ) = \operatorname { P S L } ( 2 , \mathbb { C } )$

$d = 2$ This is the first really interesting case. Here again, degree 2 (connected, parametrized) curves in $\mathbb { C P } ^ { 2 }$ consist of rational curves, and the images $f \colon { \dot { \mathbb { C P } } } ^ { 1 } \to \mathbb { C P } ^ { 2 }$ are of two kinds: the smooth conics and the double covers of lines. However, not only is this space not compact, the corresponding space of unparametrized curves is not compact either, for it is fairly clear that one can approach a pair of intersecting lines as closely as one wishes.

In fact, the reader may want to contemplate the one-parameter family of hyperbolas $x y = \lambda ^ { 2 } { \mathrm { ~ a s ~ } } \lambda \to 0$ . If we choose the parametrization

$$
f _ { \lambda } ( t ) = [ t , \lambda t ^ { 2 } , \lambda ] = [ 1 , x , y ] ,
$$

then the pullback $\Phi _ { \lambda } = f _ { \lambda } ^ { \ast } ( \Omega )$ is an area form on $\mathbb { C P } ^ { 1 }$ whose total integral is 2, but (and the reader should check this), as $\lambda \to 0$ , the form $\Phi _ { \lambda }$ accumulates equally at the points $t = 0$ and $t = \infty$ and goes to zero everywhere else. (See the Exercises for a further discussion.)

Now, if we go ahead and add in the pairs of lines, then this “completed” moduli space is indeed compact. It is just the space of non-zero quadratic forms in three variables (irreducible or not) up to constant multiples. It is well known that this forms a $\mathbb { C P } ^ { 5 }$

In fact, a further analysis of low degree mappings indicates that the following phenomena are typical: If one takes a sequence $\left( \Sigma _ { k } , f _ { k } \right)$ of smooth holomorphic curves in $\mathbb { C P } ^ { 2 }$ then after reparametrizing and passing to a subsequence, one can arrange that the holomorphic curves have the property that, at a finite number of points $p _ { k } ^ { \alpha } \in \Sigma$ , the induced metric $f _ { k } ^ { * } ( \Omega )$ on the surface goes to infinity and the integral of the induced area form on a neighborhood of each of these points approaches an integer while along a finite number of loops $\gamma _ { i }$ , the induced metric goes to zero.

The first type of phenomenon is called “bubbling”, for what is happening is that a small 2-sphere is inflating and “breaking off” from the surface and covering a line in $\mathbb { C P } ^ { 2 }$ The second type of phenomenon is called “vanishing cycles”, a loop in the surface is literally contracting to a point. It turns out that the limiting object in $\mathbb { C P } ^ { 2 }$ is a union of algebraic curves whose total degree is the same as that of the members of the varying family.

Thus, for $\mathbb { C P } ^ { 2 }$ , the moduli space ${ \mathfrak { M } } _ { d }$ of unparametrized curves of degree d has a compactification $\mathfrak { M } _ { d }$ where the extra points represent decomposable or degenerate curves with “cusps”.

Other instances of this “bubbling” phenomena have been discovered. Sacks and Uhlenbeck showed that when one wants to study the question of representing elements of $\pi _ { 2 } ( X )$ (where X is a Riemannian manifold) by harmonic or minimal surfaces, one has to deal with the possibility of pieces of the surface “bubbling off” in exactly the fashion described above.

More recently, this sort of phenomenon has been used in “reverse” by Taubes to construct solutions to the (anti-)self dual Yang-Mills equations over compact 4-manifolds.

With all of this evidence of good compactifications of moduli spaces in other problems, Gromov had the idea of trying to compactify the connected components of the “modulispace” M of holomorphic curves in a general almost complex manifold M. Since one would certainly expect the area function to be continuous on each compactified component, it follows that there is not much hope of finding a good compactification of the components of M in a case where the area function is not bounded on the components of M (as in the case of the Heisenberg example above).

However, it is still possible that one might be able to produce such a compactification if one can get an area bound on the curves in each component. Gromov’s insight was that having the area bound was enough to furnish a priori estimates on the derivatives of curves with an area bound, at least away from a finite number of points.

With all of this in mind, I can now very roughly state Gromov’s Compactification Theorem:

Theorem 5: Let M be a compact almost complex manifold with almost complex structure J and suppose that Ω tames J. Then every component ${ \mathfrak { M } } _ { \alpha }$ of the moduli space M of connected unparametrized holomorphic curves in M can be compactified to a space ${ \mathfrak { M } } _ { \alpha }$ by adding a set of “cusp” curves, where a cusp curve is essentially a finite union of (possibly) singular holomorphic curves in M that is obtained as a limit of a sequence of connected curves in ${ \mathfrak { M } } _ { \alpha }$ by ‘pinching loops’ and ‘bubbling’.

For the precise definition of ‘cusp curve’ consult [Gr 1], [Wo], or [Pa]. The method that Gromov uses to prove his compactness theorem is basically a generalization of the Schwarz Lemma. This allows him to get control of the sup-norm of the first derivatives of a holomorphic curve in M terms of the $L _ { 1 } ^ { 2 } .$ -norm (i.e., area norm) at least in regions where the area form stays bounded.

Unfortunately, although the ideas are intuitively compelling, the actual details are non-trivial. However, there are, by now, several good sources, from different viewpoints, for proofs of Gromov’s Compactification Theorem. The articles [M 4] and [Wo] listed in the Bibliography are very readable accounts and are highly recommended. I hear that the (unpublished) [Pa] is also an excellent account that is closer in spirit to Gromov’s original ideas of how the proof should go. Finally, there is the quite recent [Ye], which generalizes this compactification theorem to the case of curves with boundary.

Actually, the most fruitful applications of these ideas have been in the situation when, for various reasons, it turns out that there cannot be any cusp curves, so that, by Gromov’s compactness theorem, the moduli space is already compact. Here is a case where this happens.

Proposition 1: Suppose that $( M , J )$ is a compact, almost complex manifold and that Ω is a 2-form that tames J. Suppose that there exists a non-constant holomorphic curve $f \colon S ^ { 2 } \to M$ , and suppose that there is a number $A > 0$ so that $\int _ { S ^ { 2 } } f ^ { * } ( \Omega ) \geq A$ for all non-constant holomorphic maps $f \colon S ^ { 2 } \ \to \ M$ Then for any $B \ < \ 2 A$ , the set ${ \mathfrak { M } } _ { B }$ of unparametrized holomorphic curves $f ( S ^ { 2 } ) \subset M$ that satisfy $\int _ { S ^ { 2 } } f ^ { * } ( \Omega ) = B$ is compact.

Proof: (Idea) If the space ${ \mathfrak { M } } _ { B }$ were not compact, then a point of the compactification would would correspond a union of cusp curves that would contain at least two distinct non-constant holomorphic maps of $S ^ { 2 }$ into M. Of course, this would imply that the limiting value of the integral of Ω over this curve would be at least $2 A > B$ , a contradiction. 

An example of this phenomenon is when the taming form Ω represents an integral class in cohomology. Then the presence of any holomorphic rational curves at all implies that there is a compact moduli space at some level.

Applications. It is reasonable to ask how the Compactness Theorem can be applied in symplectic geometry.

To do this, what one typically does is first fix a symplectic manifold $( M , \Omega )$ and then considers the space J(Ω) of almost complex structures on M that Ω tames. We already know from Lecture 5 that $\mathcal { J } ( \Omega )$ is not empty. We even know that the space $\mathcal { K } ( \Omega ) \subset \mathcal { J } ( \Omega )$ of Ω-compatible almost complex structures is non-empty. Moreover, it is not hard to show that these spaces are contractible (see the Exercises).

Thus, any invariant of the almost complex structures $J \in \mathcal { J } ( \Omega )$ or of the almost K¨ahler structures $J \in \mathcal { K } ( \Omega )$ that is constant under homotopy through such structures is an invariant of the underlying symplectic manifold (M, Ω).

This idea is extremely powerful. Gromov has used it to construct many new invariants of symplectic manifolds. He has then gone on to use these invariants to detect features of symplectic manifolds that are not presently accessible by any other means.

Here is a sample of some of the applications of Gromov’s work on holomorphic curves. Unfortunately, I will not have time to discuss the proofs of any of these results.

Theorem 6: (Gromov) If there is a symplectic embedding of $B ^ { 2 n } ( r ) \subset \mathbb { R } ^ { 2 n }$ into $B ^ { 2 } ( R ) \times  { \mathbb { R } } ^ { 2 n - 2 }$ , then $r \leq R$

One corollary of Theorem 6 is that any diffeomorphism of a symplectic manifold that is a $C ^ { 0 } .$ -limit of symplectomorphisms is itself a symplectomorphism.

Theorem 7: (Gromov) If Ω is a symplectic structure on $\mathbb { C P } ^ { 2 }$ and there exists an embedded Ω-symplectic sphere $S \subset \mathbb { C P } ^ { 2 }$ , then Ω is equivalent to the standard symplectic structure.

The next two theorems depend on the notion of asymptotic flatness: We say that a non-compact symplectic manifold $M ^ { 2 n }$ is asymptotically flat if there is a compact set $K _ { 1 } \subset M ^ { 2 n }$ and a compact set $K _ { 2 } \subset \mathbb { R } ^ { 2 n }$ so that $M \backslash K _ { 1 }$ is symplectomorphic to $\mathbb { R } ^ { 2 n } \backslash K _ { 2 }$ (with the standard symplectic structure on $\mathbb { R } ^ { 2 n } )$

Theorem 8: (McDuff) Suppose that $M ^ { 4 }$ is a non-compact symplectic manifold that is asymptotically flat. Then $M ^ { 4 }$ is symplectomorphic to $\mathbb { R } ^ { 4 }$ with a finite number of points blown up.

Theorem 9: (McDuff, Floer, Eliashberg) Suppose that $M ^ { 2 n }$ is asymptotically flat and contains no symplectic 2-spheres. Then $M ^ { 2 n }$ is diffeomorphic to $\mathbb { R } ^ { 2 n }$

It is not known whether one might replace “diffeomorphic” with “symplectomorphic” in this theorem for $n > 2$ •

## Epilogue

I hope that this Lecture has intrigued you as to the possibilities of applying the ideas of Gromov in modern geometry. Let me close by quoting from Gromov’s survey paper on symplectic geometry in the Proceedings of the 1986 ICM:

Differential forms (of any degree) taming partial differential equations provide a major (if not the only) source of integro-differential inequalities needed for a priori estimates and vanishing theorems. These forms are defined on spaces of jets (of solutions of equations) and they are often (e.g., in Bochner-Weitzenbock formulas) exact and invariant under pertinent (infinitesimal) symmetry groups. Similarly, convex (in an appropriate sense) functions on spaces of jets are responsible for the maximum principles. A great part of hard analysis of PDE will become redundant when the algebraic and geometric structure of taming forms and corresponding convex functions is clarified. (From the PDE point of view, symplectic geometry appears as a taming device on the space of 0-jets of solutions of the Cauchy-Riemann equation.)

# Exercise Set 9:

# The Gromov School of Symplectic Geometry

1. Use the fact that an orientable 3-manifold $M ^ { 3 }$ is parallelizable (i.e., its tangent bundle is trivial) and Theorem 1 to show that a compact 3-manifold can always be immersed in $\mathbb { R } ^ { 4 }$ and a 3-manifold with no compact component can always be immersed in $\mathbb { R } ^ { 3 }$

2. Show that Theorem 2 does, in fact imply that any connected non-compact symplectic manifold that has an almost complex structure has a symplectic structure. (Hint: Show that the natural projection $Z ^ { 1 } ( X , V ) \to V$ has contractible fibers (in fact, $Z ^ { 1 } ( X , V )$ is an affine bundle over V , and then use this to show that a non-degenerate 2-form on X can be homotoped to a closed non-degenerate 2-form on X.)

3. Show that the hypothesis in Theorem 3 that X either be non-compact or that dim $( X ) <$ dim(Y ) is essential.

4. Show that if E is a symplectic bundle over a compact manifold $M ^ { 2 n }$ whose rank is $2 n + 2 k$ for some $k > 0$ , then there exists a symplectic splitting $E = F \oplus T$ where $T$ is a trivial symplectic bundle over M of rank k. (Hint: Use transversality to pick a nonvanishing section of E. Now what?)

Show also that, if E is a symplectic bundle over a compact manifold $M ^ { 2 n }$ , then there exists another symplectic bundle $E ^ { \prime }$ over M so that $E \oplus E ^ { \prime }$ is trivial. (Hint: Mimic the proof for complex bundles.)

Finally, use these results to complete the proof of the Corollary to Theorem 3.

5. Show that if a symplectic manifold M is simply connected, then the symplectic blow up Mˆ of M along a symplectic submanifold S of M is also simply connected. (Hint: Any loop in $\hat { M }$ can be deformed into a loop that misses ${ \hat { S } } .$ . Now what?)

6. Prove, as stated in the text, that if M is compact and Ω tames J, then for any Riemannian metric $g$ on $M$ (not necessarily compatible with either J or Ω) there is a constant $C > 0$ so that

$$
| v \wedge J v | \leq C \Omega ( v , J v )
$$

where $| v \land J v |$ represents the area in $T _ { p } M$ of the parallelogram spanned by v and Jv in $T _ { p } M$

7. First Order Equations and Holomorphic Curves. The point of this problem is to show how elliptic quasi-linear determined PDE for two functions of two unknowns can be reformulated as a problem in holomorphic curves in an almost complex manifold.

Suppose that π: $V ^ { 4 }  X ^ { 2 }$ is a smooth submersion from a 4-manifold onto a 2-manifold. Suppose also that $R \subset J ^ { 1 } ( X , V )$ is smooth submanifold of dimension 6 that has the property that it locally represents an elliptic, quasi-linear pair of first order PDE for sections s of π. Show that there exists a unique almost complex structure on V so that a section s of π is a solution of R if and only if its graph in V is an (unparametrized) holomorphic curve in V .

(Hint: The hypotheses on the relation R are equivalent to the following conditions. For every point $v \in V$ , there are coordinates x, y, f, g on a neighborhood of v in V with the property that x and y are local coordinates on a neighborhood of $\pi ( v )$ and so that a local section s of the form $f = F ( x , y ) , g = G ( x , y )$ is a solution of R if and only if they satisfy a pair of equations of the form

$$
\begin{array} { r } { A _ { 1 } f _ { x } + B _ { 1 } f _ { y } + C _ { 1 } g _ { x } + D _ { 1 } g _ { y } + E _ { 1 } = 0 } \\ { A _ { 2 } f _ { x } + B _ { 2 } f _ { y } + C _ { 2 } g _ { x } + D _ { 2 } g _ { y } + E _ { 2 } = 0 } \end{array}
$$

where the $A _ { 1 } , \ldots , E _ { 2 }$ are specific functions of $( x , y , f , g )$ . The ellipticity condition is equivalent to the assumption that

$$
\operatorname * { d e t } \left( \begin{array} { l l } { A _ { 1 } \xi + B _ { 1 } \eta } & { C _ { 1 } \xi + D _ { 1 } \eta } \\ { A _ { 2 } \xi + B _ { 2 } \eta } & { C _ { 2 } \xi + D _ { 2 } \eta } \end{array} \right) > 0
$$

for all $( \xi , \eta ) \neq ( 0 , 0 ) . )$

Show that the problem of isometrically embedding a metric g of positive Gauss curvature on a surface Σ into $\mathbb { R } ^ { 3 }$ can be turned into a problem of finding a holomorphic section of an almost complex bundle $\pi \colon V  \Sigma$ . Do this by showing that the bundle V whose sections are the quadratic forms that have positive g-trace and that satisfy the algebraic condition imposed by the Gauss equation on quadratic forms that are second fundamental forms for isometric embeddings of g is a smooth rank 2 disk bundle over Σ and that the Codazzi equations then reduce to a pair of elliptic first order quasi-linear PDE for sections of this bundle.

Show that, if Σ is topologically $S ^ { 2 }$ , then the topological self-intersection number of a global section of V is −4. Conclude, using the fact that distinct holomorphic curves in V must have positive intersection number, that (up to sign) there cannot be more that one second fundamental form on Σ that satisfies both the Gauss and Codazzi equations. Thus, conclude that a closed surface of positive Gauss curvature in $\mathbb { R } ^ { 3 }$ is rigid.

This approach to isometric embedding of surfaces has been extensively studied by Labourie [La].

8. Prove, as claimed in the text that, for the map $f _ { \lambda } \colon { \mathbb { C P } } ^ { 1 } \to { \mathbb { C P } } ^ { 2 }$ given by the rule

$$
f _ { \lambda } ( t ) = [ t , \lambda t ^ { 2 } , \lambda ] = [ 1 , x , y ] ,
$$

the pull-back of the Fubini-Study metric accumulates at the points $t = 0$ and $t = \infty$ and goes to zero everywhere else. What would have happened if, instead we had used the map

$$
g _ { \lambda } ( t ) = [ t , t ^ { 2 } , \lambda ^ { 2 } ] = [ 1 , x , y ] ^ { ? }
$$

Is there a contradiction here?

9. Verify the claim made in the text that, for a symplectic manifold $( M , \Omega )$ , the spaces $\mathcal { K } ( \Omega )$ and $\mathcal { J } ( \Omega )$ of Ω-compatible and Ω-tame almost complex structures on M are indeed contractible. (Hint: Fix an element $J _ { 0 } \in \mathcal { K } ( \Omega )$ , with associated inner product $\langle , \rangle _ { 0 }$ and show that, for any $J \in { \mathcal { J } } ( \Omega )$ , we can write $J = J _ { 0 } ( S + A )$ where $S$ is symmetric and positive definite with respect to $\langle , \rangle _ { 0 }$ and A is anti-symmetric. Now what?)

10. The point of this exercise is to get a look at the pseudo-holomorphic curves of a nonintegrable almost complex structure. Let $X ^ { 4 } = \mathbb { C } \times \bar { \Delta } = \{ ( w , z ) \in \bar { \mathbb { C } } ^ { 2 } | | z | < 1 \}$ , and give $X ^ { 4 }$ the almost complex structure for which the complex valued 1-forms $\alpha = d w + \bar { z } d \bar { w }$ and $\beta = d z$ are a basis for the $( 1 , 0 )$ -forms. Verify that this does indeed define a non-integrable almost complex structure on the 4-manifold X. Show that the pseudo-holomorphic curves in X can be described explicitly as follows: If M is a Riemann surface and φ $\rangle \colon M ^ { 2 } \to X$ is a pseudo-holomorphic mapping, then one of the following is true: Either $\phi ^ { * } ( \beta ) = 0$ and there exists a holomorphic function h on M and a constant $z _ { \mathrm { 0 } }$ so that

$$
\phi = \big ( h - \bar { z } _ { 0 } \bar { h } , z _ { 0 } \big ) ,
$$

or else there exists a non-constant holomorphic function g on M that satisfies $| g | < 1$ , a meromorphic function f on M so that f dg and fg dg are holomorphic 1-forms without periods on $M ,$ , and a constant $w _ { 0 }$ so that

$$
\phi ( p ) = \Biggl ( w _ { 0 } + \int _ { p _ { 0 } } ^ { p } ( f d g - { \overline { { f g d g } } } ) , g ( p ) \Biggr )
$$

where the integral is taken to be taken over any path from some basepoint $p _ { 0 }$ to $p$ in $M$

(Hint: It is obvious that you must take $g = \phi ^ { * } ( z )$ , but it is not completely obvious where f will be found. However, if g is not a constant function, then it will clearly be holomorphic, now consider the “function”

$$
f = { \frac { \phi ^ { * } ( \alpha ) } { \left( 1 - | g | ^ { 2 } \right) d g } }
$$

and show that it must be meromorphic, with poles at worst along the zeroes of $d g . )$

[A] V. I. Arnol’d, Mathematical Methods of Classical Mechanics, Second Edition, Springer-Verlag, Berlin, Heidelberg, New York, 1989.

[AH] M. F. Atiyah and N. Hitchin, The Geometry and Dynamics of Magnetic Monopoles, Princeton University Press, Princeton, 1988.

[Bea] A. Beauville, Vari´et´es K¨ahleriennes dont la premi\`ere classe de Chern est nulle, J. Differential Geom. 18 (1983), 755–782.

[Ber] M. Berger, Sur les groupes d’holonomie homog\`ene des vari´et´es a connexion affine et des vari´et´es Riemanniennes, Bull. Soc. Math. France 83 (1955), 279–330.

[Bes] A. Besse, Einstein Manifolds, Springer-Verlag, Berlin, Heidelberg, New York, 1987.

[Ch] S.-S. Chern, On a generalization of K¨ahler geometry, in Algebraic Geometry and Topology: A Symposium in Honor of S. Lefshetz, Princeton University Press, 1957, 103–121.

[FGG] M. Fernandez, M. Gotay, and A. Gray, Four-dimensional parallelizable symplectic and complex manifolds, Proc. Amer. Math. Soc. 103 (1988), 1209–1212.

[Fo] A. T. Fomenko, Symplectic Geometry, Gordon and Breach, New York, 1988.

[GL] K. Galicki and H.B. Lawson, Quaternionic Reduction and quaternionic orbifolds, Math. Ann. 282 (1988), 1–21.

[GG] M. Golubitsky and V. Guillemin , Stable Mappings and their Singularities, Graduate Texts in Mathematics 14, Springer-Verlag, Berlin, Heidelberg, New York, 1973.

[Gr 1] M. Gromov, Pseudo-holomorphic curves on almost complex manifolds, Inventiones Mathematicae 82 (1985), 307–347.

[Gr 2] M. Gromov, Partial Differential Relations, Ergebnisse der Math., Springer-Verlag, Berlin, Heidelberg, New York, 1986.

[Gr 3] M. Gromov, Soft and hard symplectic geometry, Proceedings of the ICM at Berkeley, 1986, 1987, vol. 1, Amer. Math. Soc., Providence, R.I., 81–98.

[GS 1] V. Guillemin and S. Sternberg, Geometric Asymptotics, Mathematical Surveys 14, Amer. Math. Soc., Providence, R.I., 1977.

[GS 2] V. Guillemin and S. Sternberg, Symplectic Techniques in Physics, Cambridge University, Cambridge and New York, 1984.

[GS 3] V. Guillemin and S. Sternberg, Variations on a Theme of Kepler, Colloquium Publications 42, Amer. Math. Soc., Providence, R.I., 1990.

[Ha] R. Hamilton, The inverse function theorem of Nash and Moser, Bulletin of the AMS 7 (1982), 65–222.

[He] S. Helgason, Differential Geometry, Lie Groups, and Symmetric Spaces, Academic Press, Princeton, 1978.

[Hi] N. Hitchin, Metrics on moduli spaces, in Contemporary Mathematics 58 (1986), Amer. Math. Soc., Providence, R.I., 157–178.

[HKLR] N. Hitchin, A. Karlhede, U. Lindstrom, ¨ and M. Rocek, ˇ HyperK¨ahler metrics and supersymmetry, Comm. Math. Phys. 108 (1987), 535–589.

[Ki] F. Kirwan, Cohomology of Quotients in Symplectic and Algebraic Geometry, Mathematical Notes 31, Princeton University Press, Princeton, 1984.

[KN] S. Kobayashi and K. Nomizu, Foundations of Differential Geometry, vols. I and II, John Wiley & Sons, New York, 1963.

[Kr] P. Kronheimer, The construction of ALE spaces as hyper-K¨ahler quotients, J. Differential Geometry 29 (1989), 665-683.

[La] F. Labourie, Immersions isom´etriques elliptiques et courbes pseudo-holomorphes, J. Differential Geometry 30 (1989), 395-424.

[M 1] D. McDuff, Symplectic diffeomorphisms and the flux homomorphism, Inventiones Mathematicae 77 (1984), 353–366.

[M 2] D. McDuff, Examples of simply-connected symplectic non-K¨ahlerian manifolds, J. Differential Geom. 20 (1984), 267–277.

[M 3] D. McDuff, Examples of symplectic structures, Inventiones Mathematicae 89 (1987), 13–36.

[M 4] D. McDuff, Symplectic 4-manifolds, Proceedings of the ICM at Kyoto, 1990, to appear

[M 5] D. McDuff, Elliptic methods in symplectic geometry, Bull. Amer. Math. Soc. 23 (1990), 311–358.

[MS] J. Milnor and J. Stasheff, Characteristic Classes, Annals of Math. Studies 76, Princeton University Press, Princeton, 1974.

[Mo] J. Moser, On the volume element on manifolds, Trans. Amer. Math. Soc. 120 (1965), 280–296.

[Pa] P. Pansu, Pseudo-holomorphic curves in symplectic manifolds, preprint, Ecole Poly- ´ technique, Palaiseau, 1986.

[Po] I. Postnikov, Groupes et alg\`ebras de Lie, (French translation of the Russian original), Editions Mir, Moscow 1985. ´

[Sa] S. Salamon, Riemannian geometry and holonomy groups, Pitman Research Notes in Math. no. 201, Longman scientific & Technical, Essex, 1989.

[Si] Y. T. Siu, Every K3 surface is K¨ahler, Inventiones Math. 73 (1983), 139–150.

[SS] I. Singer and S. Sternberg, The infinite groups of Lie and Cartan, I (The transitive groups), Journal d’Analyse 15 (1965).

[Wa] F. Warner, Foundations of Differentiable Manifolds and Lie Groups, Springer-Verlag, Berlin Heidelberg New York, 1983.

[We] A. Weinstein, Lectures on Symplectic Manifolds, Regional Conference Series in Mathematics 29, Amer. Math. Soc., Providence, R.I., 1976.

[Wo] J. Wolfson, Gromov’s compactness of pseudo-holomorphic curves and symplectic geometry, J. Differential Geom. 28 (1988), 383–405.

[Ye] R. Ye, Gromov’s compactness theorem for pseudo-holomorphic curves, Transactions of the AMS , to appear.